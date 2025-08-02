_t='cpqSiSystemTelemetryThresholdStatus'
_s='cpqSiSystemTelemetryMetric'
_r='cpqSiHotPlugSlotErrorStatus'
_q='cpqSiMemConfigChangeData'
_p='cpqSiRackEnclosureMgrIndex'
_o='cpqSiFruIndex'
_n='cpqSiFirmwareCfgName'
_m='cpqSiFirmwareRevIndex'
_l='cpqSiBoardRevIndex'
_k='cpqSiBoardRevSlotIndex'
_j='absent'
_i='cpqSiPerfStateIndex'
_h='cpqSiProcMicroPatchIndex'
_g='supported'
_f='cpqSiMemModuleIndex'
_e='cpqSiMemBoardIndex'
_d='cpqSiVirtualSystemIndex'
_c='cpqSiOsCommonModuleIndex'
_b='NotificationType'
_a='cpqSiMemErrorIndex'
_Z='notSupported'
_Y='cpqSiSysBatterySerialNum'
_X='cpqSiSysBatteryIndex'
_W='cpqSiHotPlugSlotIndex'
_V='cpqSiHotPlugSlotChassis'
_U='cpqSiMonitorIndex'
_T='read-write'
_S='failed'
_R='unknown'
_Q='OctetString'
_P='degraded'
_O='enabled'
_N='disabled'
_M='ok'
_L='deprecated'
_K='sysName'
_J='SNMPv2-MIB'
_I='cpqHoTrapFlags'
_H='CPQHOST-MIB'
_G='CPQSINFO-MIB'
_F='other'
_E='DisplayString'
_D='optional'
_C='Integer32'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_H,'compaq',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_b,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_b,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_CpqSystemInfo_ObjectIdentity=ObjectIdentity
cpqSystemInfo=_CpqSystemInfo_ObjectIdentity((1,3,6,1,4,1,232,2))
_CpqSiMibRev_ObjectIdentity=ObjectIdentity
cpqSiMibRev=_CpqSiMibRev_ObjectIdentity((1,3,6,1,4,1,232,2,1))
class _CpqSiMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSiMibRevMajor_Type.__name__=_C
_CpqSiMibRevMajor_Object=MibScalar
cpqSiMibRevMajor=_CpqSiMibRevMajor_Object((1,3,6,1,4,1,232,2,1,1),_CpqSiMibRevMajor_Type())
cpqSiMibRevMajor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMibRevMajor.setStatus(_B)
class _CpqSiMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMibRevMinor_Type.__name__=_C
_CpqSiMibRevMinor_Object=MibScalar
cpqSiMibRevMinor=_CpqSiMibRevMinor_Object((1,3,6,1,4,1,232,2,1,2),_CpqSiMibRevMinor_Type())
cpqSiMibRevMinor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMibRevMinor.setStatus(_B)
class _CpqSiMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiMibCondition_Type.__name__=_C
_CpqSiMibCondition_Object=MibScalar
cpqSiMibCondition=_CpqSiMibCondition_Object((1,3,6,1,4,1,232,2,1,3),_CpqSiMibCondition_Type())
cpqSiMibCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMibCondition.setStatus(_B)
_CpqSiComponent_ObjectIdentity=ObjectIdentity
cpqSiComponent=_CpqSiComponent_ObjectIdentity((1,3,6,1,4,1,232,2,2))
_CpqSiInterface_ObjectIdentity=ObjectIdentity
cpqSiInterface=_CpqSiInterface_ObjectIdentity((1,3,6,1,4,1,232,2,2,1))
_CpqSiOsCommon_ObjectIdentity=ObjectIdentity
cpqSiOsCommon=_CpqSiOsCommon_ObjectIdentity((1,3,6,1,4,1,232,2,2,1,4))
class _CpqSiOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiOsCommonPollFreq_Type.__name__=_C
_CpqSiOsCommonPollFreq_Object=MibScalar
cpqSiOsCommonPollFreq=_CpqSiOsCommonPollFreq_Object((1,3,6,1,4,1,232,2,2,1,4,1),_CpqSiOsCommonPollFreq_Type())
cpqSiOsCommonPollFreq.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiOsCommonPollFreq.setStatus(_B)
_CpqSiOsCommonModuleTable_Object=MibTable
cpqSiOsCommonModuleTable=_CpqSiOsCommonModuleTable_Object((1,3,6,1,4,1,232,2,2,1,4,2))
if mibBuilder.loadTexts:cpqSiOsCommonModuleTable.setStatus(_L)
_CpqSiOsCommonModuleEntry_Object=MibTableRow
cpqSiOsCommonModuleEntry=_CpqSiOsCommonModuleEntry_Object((1,3,6,1,4,1,232,2,2,1,4,2,1))
cpqSiOsCommonModuleEntry.setIndexNames((0,_G,_c))
if mibBuilder.loadTexts:cpqSiOsCommonModuleEntry.setStatus(_L)
class _CpqSiOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiOsCommonModuleIndex_Type.__name__=_C
_CpqSiOsCommonModuleIndex_Object=MibTableColumn
cpqSiOsCommonModuleIndex=_CpqSiOsCommonModuleIndex_Object((1,3,6,1,4,1,232,2,2,1,4,2,1,1),_CpqSiOsCommonModuleIndex_Type())
cpqSiOsCommonModuleIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiOsCommonModuleIndex.setStatus(_L)
class _CpqSiOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiOsCommonModuleName_Type.__name__=_E
_CpqSiOsCommonModuleName_Object=MibTableColumn
cpqSiOsCommonModuleName=_CpqSiOsCommonModuleName_Object((1,3,6,1,4,1,232,2,2,1,4,2,1,2),_CpqSiOsCommonModuleName_Type())
cpqSiOsCommonModuleName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiOsCommonModuleName.setStatus(_L)
class _CpqSiOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqSiOsCommonModuleVersion_Type.__name__=_E
_CpqSiOsCommonModuleVersion_Object=MibTableColumn
cpqSiOsCommonModuleVersion=_CpqSiOsCommonModuleVersion_Object((1,3,6,1,4,1,232,2,2,1,4,2,1,3),_CpqSiOsCommonModuleVersion_Type())
cpqSiOsCommonModuleVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiOsCommonModuleVersion.setStatus(_L)
class _CpqSiOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSiOsCommonModuleDate_Type.__name__=_Q
_CpqSiOsCommonModuleDate_Object=MibTableColumn
cpqSiOsCommonModuleDate=_CpqSiOsCommonModuleDate_Object((1,3,6,1,4,1,232,2,2,1,4,2,1,4),_CpqSiOsCommonModuleDate_Type())
cpqSiOsCommonModuleDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiOsCommonModuleDate.setStatus(_L)
class _CpqSiOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiOsCommonModulePurpose_Type.__name__=_E
_CpqSiOsCommonModulePurpose_Object=MibTableColumn
cpqSiOsCommonModulePurpose=_CpqSiOsCommonModulePurpose_Object((1,3,6,1,4,1,232,2,2,1,4,2,1,5),_CpqSiOsCommonModulePurpose_Type())
cpqSiOsCommonModulePurpose.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiOsCommonModulePurpose.setStatus(_L)
_CpqSiAsset_ObjectIdentity=ObjectIdentity
cpqSiAsset=_CpqSiAsset_ObjectIdentity((1,3,6,1,4,1,232,2,2,2))
class _CpqSiSysSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysSerialNum_Type.__name__=_E
_CpqSiSysSerialNum_Object=MibScalar
cpqSiSysSerialNum=_CpqSiSysSerialNum_Object((1,3,6,1,4,1,232,2,2,2,1),_CpqSiSysSerialNum_Type())
cpqSiSysSerialNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysSerialNum.setStatus(_B)
class _CpqSiFormFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_R,1),('portable',2),('laptop',3),('desktop',4),('tower',5),('mini-tower',6),('rack-mount',7),('multiboard-chasis',8),('blade',9),('blade-enclosure',10)))
_CpqSiFormFactor_Type.__name__=_C
_CpqSiFormFactor_Object=MibScalar
cpqSiFormFactor=_CpqSiFormFactor_Object((1,3,6,1,4,1,232,2,2,2,2),_CpqSiFormFactor_Type())
cpqSiFormFactor.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiFormFactor.setStatus(_B)
class _CpqSiAssetTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiAssetTag_Type.__name__=_E
_CpqSiAssetTag_Object=MibScalar
cpqSiAssetTag=_CpqSiAssetTag_Object((1,3,6,1,4,1,232,2,2,2,3),_CpqSiAssetTag_Type())
cpqSiAssetTag.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiAssetTag.setStatus(_B)
class _CpqSiOwnershipTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CpqSiOwnershipTag_Type.__name__=_E
_CpqSiOwnershipTag_Object=MibScalar
cpqSiOwnershipTag=_CpqSiOwnershipTag_Object((1,3,6,1,4,1,232,2,2,2,4),_CpqSiOwnershipTag_Type())
cpqSiOwnershipTag.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiOwnershipTag.setStatus(_B)
class _CpqSiSysServiceNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysServiceNum_Type.__name__=_E
_CpqSiSysServiceNum_Object=MibScalar
cpqSiSysServiceNum=_CpqSiSysServiceNum_Object((1,3,6,1,4,1,232,2,2,2,5),_CpqSiSysServiceNum_Type())
cpqSiSysServiceNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysServiceNum.setStatus(_B)
class _CpqSiSysProductId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysProductId_Type.__name__=_E
_CpqSiSysProductId_Object=MibScalar
cpqSiSysProductId=_CpqSiSysProductId_Object((1,3,6,1,4,1,232,2,2,2,6),_CpqSiSysProductId_Type())
cpqSiSysProductId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysProductId.setStatus(_B)
_CpqSiAssetTagMaxLength_Type=Integer32
_CpqSiAssetTagMaxLength_Object=MibScalar
cpqSiAssetTagMaxLength=_CpqSiAssetTagMaxLength_Object((1,3,6,1,4,1,232,2,2,2,7),_CpqSiAssetTagMaxLength_Type())
cpqSiAssetTagMaxLength.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiAssetTagMaxLength.setStatus(_D)
_CpqSiVirtualSystemTable_Object=MibTable
cpqSiVirtualSystemTable=_CpqSiVirtualSystemTable_Object((1,3,6,1,4,1,232,2,2,2,8))
if mibBuilder.loadTexts:cpqSiVirtualSystemTable.setStatus(_D)
_CpqSiVirtualSystemEntry_Object=MibTableRow
cpqSiVirtualSystemEntry=_CpqSiVirtualSystemEntry_Object((1,3,6,1,4,1,232,2,2,2,8,1))
cpqSiVirtualSystemEntry.setIndexNames((0,_G,_d))
if mibBuilder.loadTexts:cpqSiVirtualSystemEntry.setStatus(_D)
class _CpqSiVirtualSystemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiVirtualSystemIndex_Type.__name__=_C
_CpqSiVirtualSystemIndex_Object=MibTableColumn
cpqSiVirtualSystemIndex=_CpqSiVirtualSystemIndex_Object((1,3,6,1,4,1,232,2,2,2,8,1,1),_CpqSiVirtualSystemIndex_Type())
cpqSiVirtualSystemIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVirtualSystemIndex.setStatus(_D)
_CpqSiVirtualSystemSerialNumber_Type=DisplayString
_CpqSiVirtualSystemSerialNumber_Object=MibTableColumn
cpqSiVirtualSystemSerialNumber=_CpqSiVirtualSystemSerialNumber_Object((1,3,6,1,4,1,232,2,2,2,8,1,2),_CpqSiVirtualSystemSerialNumber_Type())
cpqSiVirtualSystemSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVirtualSystemSerialNumber.setStatus(_D)
_CpqSiVirtualSystemUUID_Type=DisplayString
_CpqSiVirtualSystemUUID_Object=MibTableColumn
cpqSiVirtualSystemUUID=_CpqSiVirtualSystemUUID_Object((1,3,6,1,4,1,232,2,2,2,8,1,3),_CpqSiVirtualSystemUUID_Type())
cpqSiVirtualSystemUUID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVirtualSystemUUID.setStatus(_D)
_CpqSiSecurity_ObjectIdentity=ObjectIdentity
cpqSiSecurity=_CpqSiSecurity_ObjectIdentity((1,3,6,1,4,1,232,2,2,3))
class _CpqSiPowerOnPassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiPowerOnPassword_Type.__name__=_C
_CpqSiPowerOnPassword_Object=MibScalar
cpqSiPowerOnPassword=_CpqSiPowerOnPassword_Object((1,3,6,1,4,1,232,2,2,3,1),_CpqSiPowerOnPassword_Type())
cpqSiPowerOnPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPowerOnPassword.setStatus(_B)
class _CpqSiNetServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiNetServerMode_Type.__name__=_C
_CpqSiNetServerMode_Object=MibScalar
cpqSiNetServerMode=_CpqSiNetServerMode_Object((1,3,6,1,4,1,232,2,2,3,2),_CpqSiNetServerMode_Type())
cpqSiNetServerMode.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiNetServerMode.setStatus(_B)
class _CpqSiQuickLockPassword_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiQuickLockPassword_Type.__name__=_C
_CpqSiQuickLockPassword_Object=MibScalar
cpqSiQuickLockPassword=_CpqSiQuickLockPassword_Object((1,3,6,1,4,1,232,2,2,3,3),_CpqSiQuickLockPassword_Type())
cpqSiQuickLockPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiQuickLockPassword.setStatus(_B)
class _CpqSiQuickBlank_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiQuickBlank_Type.__name__=_C
_CpqSiQuickBlank_Object=MibScalar
cpqSiQuickBlank=_CpqSiQuickBlank_Object((1,3,6,1,4,1,232,2,2,3,4),_CpqSiQuickBlank_Type())
cpqSiQuickBlank.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiQuickBlank.setStatus(_B)
class _CpqSiDisketteBootControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiDisketteBootControl_Type.__name__=_C
_CpqSiDisketteBootControl_Object=MibScalar
cpqSiDisketteBootControl=_CpqSiDisketteBootControl_Object((1,3,6,1,4,1,232,2,2,3,5),_CpqSiDisketteBootControl_Type())
cpqSiDisketteBootControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiDisketteBootControl.setStatus(_B)
class _CpqSiSerialPortAControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiSerialPortAControl_Type.__name__=_C
_CpqSiSerialPortAControl_Object=MibScalar
cpqSiSerialPortAControl=_CpqSiSerialPortAControl_Object((1,3,6,1,4,1,232,2,2,3,6),_CpqSiSerialPortAControl_Type())
cpqSiSerialPortAControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSerialPortAControl.setStatus(_B)
class _CpqSiSerialPortBControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiSerialPortBControl_Type.__name__=_C
_CpqSiSerialPortBControl_Object=MibScalar
cpqSiSerialPortBControl=_CpqSiSerialPortBControl_Object((1,3,6,1,4,1,232,2,2,3,7),_CpqSiSerialPortBControl_Type())
cpqSiSerialPortBControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSerialPortBControl.setStatus(_B)
class _CpqSiParallelPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiParallelPortControl_Type.__name__=_C
_CpqSiParallelPortControl_Object=MibScalar
cpqSiParallelPortControl=_CpqSiParallelPortControl_Object((1,3,6,1,4,1,232,2,2,3,8),_CpqSiParallelPortControl_Type())
cpqSiParallelPortControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiParallelPortControl.setStatus(_B)
class _CpqSiFloppyDiskControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiFloppyDiskControl_Type.__name__=_C
_CpqSiFloppyDiskControl_Object=MibScalar
cpqSiFloppyDiskControl=_CpqSiFloppyDiskControl_Object((1,3,6,1,4,1,232,2,2,3,9),_CpqSiFloppyDiskControl_Type())
cpqSiFloppyDiskControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFloppyDiskControl.setStatus(_B)
class _CpqSiFixedDiskControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiFixedDiskControl_Type.__name__=_C
_CpqSiFixedDiskControl_Object=MibScalar
cpqSiFixedDiskControl=_CpqSiFixedDiskControl_Object((1,3,6,1,4,1,232,2,2,3,10),_CpqSiFixedDiskControl_Type())
cpqSiFixedDiskControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFixedDiskControl.setStatus(_B)
class _CpqSiHoodRemovedTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiHoodRemovedTime_Type.__name__=_E
_CpqSiHoodRemovedTime_Object=MibScalar
cpqSiHoodRemovedTime=_CpqSiHoodRemovedTime_Object((1,3,6,1,4,1,232,2,2,3,11),_CpqSiHoodRemovedTime_Type())
cpqSiHoodRemovedTime.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHoodRemovedTime.setStatus(_B)
class _CpqSiHoodSensorConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_N,2),('notifyUser',3),('adminPasswordProtected',4)))
_CpqSiHoodSensorConfiguration_Type.__name__=_C
_CpqSiHoodSensorConfiguration_Object=MibScalar
cpqSiHoodSensorConfiguration=_CpqSiHoodSensorConfiguration_Object((1,3,6,1,4,1,232,2,2,3,12),_CpqSiHoodSensorConfiguration_Type())
cpqSiHoodSensorConfiguration.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHoodSensorConfiguration.setStatus(_B)
class _CpqSiSmartCoverLockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('unlocked',2),('locked',3)))
_CpqSiSmartCoverLockStatus_Type.__name__=_C
_CpqSiSmartCoverLockStatus_Object=MibScalar
cpqSiSmartCoverLockStatus=_CpqSiSmartCoverLockStatus_Object((1,3,6,1,4,1,232,2,2,3,13),_CpqSiSmartCoverLockStatus_Type())
cpqSiSmartCoverLockStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSmartCoverLockStatus.setStatus(_B)
class _CpqSiUSBPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3),('legacydisabled',4),('externalportdisabled',5)))
_CpqSiUSBPortControl_Type.__name__=_C
_CpqSiUSBPortControl_Object=MibScalar
cpqSiUSBPortControl=_CpqSiUSBPortControl_Object((1,3,6,1,4,1,232,2,2,3,14),_CpqSiUSBPortControl_Type())
cpqSiUSBPortControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiUSBPortControl.setStatus(_B)
class _CpqSiVirtualSerialPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiVirtualSerialPortControl_Type.__name__=_C
_CpqSiVirtualSerialPortControl_Object=MibScalar
cpqSiVirtualSerialPortControl=_CpqSiVirtualSerialPortControl_Object((1,3,6,1,4,1,232,2,2,3,15),_CpqSiVirtualSerialPortControl_Type())
cpqSiVirtualSerialPortControl.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVirtualSerialPortControl.setStatus(_B)
class _CpqSiChassisHoodStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('not-installed',2),('hood-ok',3),('hood-removed',4)))
_CpqSiChassisHoodStatus_Type.__name__=_C
_CpqSiChassisHoodStatus_Object=MibScalar
cpqSiChassisHoodStatus=_CpqSiChassisHoodStatus_Object((1,3,6,1,4,1,232,2,2,3,16),_CpqSiChassisHoodStatus_Type())
cpqSiChassisHoodStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiChassisHoodStatus.setStatus(_B)
_CpqSiSystemBoard_ObjectIdentity=ObjectIdentity
cpqSiSystemBoard=_CpqSiSystemBoard_ObjectIdentity((1,3,6,1,4,1,232,2,2,4))
class _CpqSiProductId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSiProductId_Type.__name__=_C
_CpqSiProductId_Object=MibScalar
cpqSiProductId=_CpqSiProductId_Object((1,3,6,1,4,1,232,2,2,4,1),_CpqSiProductId_Type())
cpqSiProductId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiProductId.setStatus(_B)
class _CpqSiProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiProductName_Type.__name__=_E
_CpqSiProductName_Object=MibScalar
cpqSiProductName=_CpqSiProductName_Object((1,3,6,1,4,1,232,2,2,4,2),_CpqSiProductName_Type())
cpqSiProductName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiProductName.setStatus(_B)
class _CpqSiAuxiliaryInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiAuxiliaryInput_Type.__name__=_C
_CpqSiAuxiliaryInput_Object=MibScalar
cpqSiAuxiliaryInput=_CpqSiAuxiliaryInput_Object((1,3,6,1,4,1,232,2,2,4,4),_CpqSiAuxiliaryInput_Type())
cpqSiAuxiliaryInput.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiAuxiliaryInput.setStatus(_B)
_CpqSiMemModuleTable_Object=MibTable
cpqSiMemModuleTable=_CpqSiMemModuleTable_Object((1,3,6,1,4,1,232,2,2,4,5))
if mibBuilder.loadTexts:cpqSiMemModuleTable.setStatus(_B)
_CpqSiMemModuleEntry_Object=MibTableRow
cpqSiMemModuleEntry=_CpqSiMemModuleEntry_Object((1,3,6,1,4,1,232,2,2,4,5,1))
cpqSiMemModuleEntry.setIndexNames((0,_G,_e),(0,_G,_f))
if mibBuilder.loadTexts:cpqSiMemModuleEntry.setStatus(_B)
class _CpqSiMemBoardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiMemBoardIndex_Type.__name__=_C
_CpqSiMemBoardIndex_Object=MibTableColumn
cpqSiMemBoardIndex=_CpqSiMemBoardIndex_Object((1,3,6,1,4,1,232,2,2,4,5,1,1),_CpqSiMemBoardIndex_Type())
cpqSiMemBoardIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemBoardIndex.setStatus(_B)
class _CpqSiMemModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMemModuleIndex_Type.__name__=_C
_CpqSiMemModuleIndex_Object=MibTableColumn
cpqSiMemModuleIndex=_CpqSiMemModuleIndex_Object((1,3,6,1,4,1,232,2,2,4,5,1,2),_CpqSiMemModuleIndex_Type())
cpqSiMemModuleIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleIndex.setStatus(_B)
class _CpqSiMemModuleSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSiMemModuleSize_Type.__name__=_C
_CpqSiMemModuleSize_Object=MibTableColumn
cpqSiMemModuleSize=_CpqSiMemModuleSize_Object((1,3,6,1,4,1,232,2,2,4,5,1,3),_CpqSiMemModuleSize_Type())
cpqSiMemModuleSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleSize.setStatus(_B)
class _CpqSiMemModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_F,1),('board',2),('cpqSingleWidthModule',3),('cpqDoubleWidthModule',4),('simm',5),('pcmcia',6),('compaq-specific',7),('dimm',8),('smallOutlineDimm',9),('rimm',10),('srimm',11),('fb-dimm',12)))
_CpqSiMemModuleType_Type.__name__=_C
_CpqSiMemModuleType_Object=MibTableColumn
cpqSiMemModuleType=_CpqSiMemModuleType_Object((1,3,6,1,4,1,232,2,2,4,5,1,4),_CpqSiMemModuleType_Type())
cpqSiMemModuleType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleType.setStatus(_B)
class _CpqSiMemModuleSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMemModuleSpeed_Type.__name__=_C
_CpqSiMemModuleSpeed_Object=MibTableColumn
cpqSiMemModuleSpeed=_CpqSiMemModuleSpeed_Object((1,3,6,1,4,1,232,2,2,4,5,1,5),_CpqSiMemModuleSpeed_Type())
cpqSiMemModuleSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleSpeed.setStatus(_L)
class _CpqSiMemModuleTechnology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('fastPageMode',2),('edoPageMode',3),('burstEdoPageMode',4),('synchronous',5),('rdram',6)))
_CpqSiMemModuleTechnology_Type.__name__=_C
_CpqSiMemModuleTechnology_Object=MibTableColumn
cpqSiMemModuleTechnology=_CpqSiMemModuleTechnology_Object((1,3,6,1,4,1,232,2,2,4,5,1,6),_CpqSiMemModuleTechnology_Type())
cpqSiMemModuleTechnology.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleTechnology.setStatus(_B)
class _CpqSiMemModuleManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMemModuleManufacturer_Type.__name__=_E
_CpqSiMemModuleManufacturer_Object=MibTableColumn
cpqSiMemModuleManufacturer=_CpqSiMemModuleManufacturer_Object((1,3,6,1,4,1,232,2,2,4,5,1,7),_CpqSiMemModuleManufacturer_Type())
cpqSiMemModuleManufacturer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleManufacturer.setStatus(_B)
class _CpqSiMemModulePartNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMemModulePartNo_Type.__name__=_E
_CpqSiMemModulePartNo_Object=MibTableColumn
cpqSiMemModulePartNo=_CpqSiMemModulePartNo_Object((1,3,6,1,4,1,232,2,2,4,5,1,8),_CpqSiMemModulePartNo_Type())
cpqSiMemModulePartNo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModulePartNo.setStatus(_B)
class _CpqSiMemModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSiMemModuleDate_Type.__name__=_Q
_CpqSiMemModuleDate_Object=MibTableColumn
cpqSiMemModuleDate=_CpqSiMemModuleDate_Object((1,3,6,1,4,1,232,2,2,4,5,1,9),_CpqSiMemModuleDate_Type())
cpqSiMemModuleDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleDate.setStatus(_B)
class _CpqSiMemModuleSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMemModuleSerialNo_Type.__name__=_E
_CpqSiMemModuleSerialNo_Object=MibTableColumn
cpqSiMemModuleSerialNo=_CpqSiMemModuleSerialNo_Object((1,3,6,1,4,1,232,2,2,4,5,1,10),_CpqSiMemModuleSerialNo_Type())
cpqSiMemModuleSerialNo.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiMemModuleSerialNo.setStatus(_B)
class _CpqSiMemModuleECCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),('degradedModuleIndexUnknown',4)))
_CpqSiMemModuleECCStatus_Type.__name__=_C
_CpqSiMemModuleECCStatus_Object=MibTableColumn
cpqSiMemModuleECCStatus=_CpqSiMemModuleECCStatus_Object((1,3,6,1,4,1,232,2,2,4,5,1,11),_CpqSiMemModuleECCStatus_Type())
cpqSiMemModuleECCStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleECCStatus.setStatus(_B)
class _CpqSiMemModuleHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMemModuleHwLocation_Type.__name__=_E
_CpqSiMemModuleHwLocation_Object=MibTableColumn
cpqSiMemModuleHwLocation=_CpqSiMemModuleHwLocation_Object((1,3,6,1,4,1,232,2,2,4,5,1,12),_CpqSiMemModuleHwLocation_Type())
cpqSiMemModuleHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleHwLocation.setStatus(_D)
class _CpqSiMemModuleFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMemModuleFrequency_Type.__name__=_C
_CpqSiMemModuleFrequency_Object=MibTableColumn
cpqSiMemModuleFrequency=_CpqSiMemModuleFrequency_Object((1,3,6,1,4,1,232,2,2,4,5,1,13),_CpqSiMemModuleFrequency_Type())
cpqSiMemModuleFrequency.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleFrequency.setStatus(_B)
class _CpqSiMemModuleCellTablePtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CpqSiMemModuleCellTablePtr_Type.__name__=_C
_CpqSiMemModuleCellTablePtr_Object=MibTableColumn
cpqSiMemModuleCellTablePtr=_CpqSiMemModuleCellTablePtr_Object((1,3,6,1,4,1,232,2,2,4,5,1,14),_CpqSiMemModuleCellTablePtr_Type())
cpqSiMemModuleCellTablePtr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleCellTablePtr.setStatus(_D)
class _CpqSiMemModuleCellStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),('deconfigured',3)))
_CpqSiMemModuleCellStatus_Type.__name__=_C
_CpqSiMemModuleCellStatus_Object=MibTableColumn
cpqSiMemModuleCellStatus=_CpqSiMemModuleCellStatus_Object((1,3,6,1,4,1,232,2,2,4,5,1,15),_CpqSiMemModuleCellStatus_Type())
cpqSiMemModuleCellStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleCellStatus.setStatus(_D)
class _CpqSiMemModulePartNoMfgr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMemModulePartNoMfgr_Type.__name__=_E
_CpqSiMemModulePartNoMfgr_Object=MibTableColumn
cpqSiMemModulePartNoMfgr=_CpqSiMemModulePartNoMfgr_Object((1,3,6,1,4,1,232,2,2,4,5,1,16),_CpqSiMemModulePartNoMfgr_Type())
cpqSiMemModulePartNoMfgr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModulePartNoMfgr.setStatus(_D)
class _CpqSiMemModuleSerialNoMfgr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMemModuleSerialNoMfgr_Type.__name__=_E
_CpqSiMemModuleSerialNoMfgr_Object=MibTableColumn
cpqSiMemModuleSerialNoMfgr=_CpqSiMemModuleSerialNoMfgr_Object((1,3,6,1,4,1,232,2,2,4,5,1,17),_CpqSiMemModuleSerialNoMfgr_Type())
cpqSiMemModuleSerialNoMfgr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemModuleSerialNoMfgr.setStatus(_D)
class _CpqSiSystemId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiSystemId_Type.__name__=_C
_CpqSiSystemId_Object=MibScalar
cpqSiSystemId=_CpqSiSystemId_Object((1,3,6,1,4,1,232,2,2,4,6),_CpqSiSystemId_Type())
cpqSiSystemId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSystemId.setStatus(_B)
class _CpqSiSystemCpuId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiSystemCpuId_Type.__name__=_C
_CpqSiSystemCpuId_Object=MibScalar
cpqSiSystemCpuId=_CpqSiSystemCpuId_Object((1,3,6,1,4,1,232,2,2,4,7),_CpqSiSystemCpuId_Type())
cpqSiSystemCpuId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSystemCpuId.setStatus(_B)
class _CpqSiFlashRomSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_Z,2),(_g,3)))
_CpqSiFlashRomSupport_Type.__name__=_C
_CpqSiFlashRomSupport_Object=MibScalar
cpqSiFlashRomSupport=_CpqSiFlashRomSupport_Object((1,3,6,1,4,1,232,2,2,4,8),_CpqSiFlashRomSupport_Type())
cpqSiFlashRomSupport.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFlashRomSupport.setStatus(_B)
class _CpqSiQuickTestRomDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSiQuickTestRomDate_Type.__name__=_Q
_CpqSiQuickTestRomDate_Object=MibScalar
cpqSiQuickTestRomDate=_CpqSiQuickTestRomDate_Object((1,3,6,1,4,1,232,2,2,4,9),_CpqSiQuickTestRomDate_Type())
cpqSiQuickTestRomDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiQuickTestRomDate.setStatus(_B)
class _CpqSiReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,2693,8115,9037)));namedValues=NamedValues(*(('notAvailable',1),('available',2),('defaultOnlyAvailable',3),('rebootToCpqUtils',2693),('rebootToDefault',8115),('autoShutdown',9037)))
_CpqSiReboot_Type.__name__=_C
_CpqSiReboot_Object=MibScalar
cpqSiReboot=_CpqSiReboot_Object((1,3,6,1,4,1,232,2,2,4,10),_CpqSiReboot_Type())
cpqSiReboot.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiReboot.setStatus(_L)
_CpqSiProcMicroPatchTable_Object=MibTable
cpqSiProcMicroPatchTable=_CpqSiProcMicroPatchTable_Object((1,3,6,1,4,1,232,2,2,4,11))
if mibBuilder.loadTexts:cpqSiProcMicroPatchTable.setStatus(_B)
_CpqSiProcMicroPatchEntry_Object=MibTableRow
cpqSiProcMicroPatchEntry=_CpqSiProcMicroPatchEntry_Object((1,3,6,1,4,1,232,2,2,4,11,1))
cpqSiProcMicroPatchEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:cpqSiProcMicroPatchEntry.setStatus(_B)
class _CpqSiProcMicroPatchIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CpqSiProcMicroPatchIndex_Type.__name__=_C
_CpqSiProcMicroPatchIndex_Object=MibTableColumn
cpqSiProcMicroPatchIndex=_CpqSiProcMicroPatchIndex_Object((1,3,6,1,4,1,232,2,2,4,11,1,1),_CpqSiProcMicroPatchIndex_Type())
cpqSiProcMicroPatchIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiProcMicroPatchIndex.setStatus(_B)
_CpqSiProcMicroPatchId_Type=Integer32
_CpqSiProcMicroPatchId_Object=MibTableColumn
cpqSiProcMicroPatchId=_CpqSiProcMicroPatchId_Object((1,3,6,1,4,1,232,2,2,4,11,1,2),_CpqSiProcMicroPatchId_Type())
cpqSiProcMicroPatchId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiProcMicroPatchId.setStatus(_B)
class _CpqSiProcMicroPatchDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSiProcMicroPatchDate_Type.__name__=_Q
_CpqSiProcMicroPatchDate_Object=MibTableColumn
cpqSiProcMicroPatchDate=_CpqSiProcMicroPatchDate_Object((1,3,6,1,4,1,232,2,2,4,11,1,3),_CpqSiProcMicroPatchDate_Type())
cpqSiProcMicroPatchDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiProcMicroPatchDate.setStatus(_B)
class _CpqSiProcMicroPatchFamily_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_CpqSiProcMicroPatchFamily_Type.__name__=_Q
_CpqSiProcMicroPatchFamily_Object=MibTableColumn
cpqSiProcMicroPatchFamily=_CpqSiProcMicroPatchFamily_Object((1,3,6,1,4,1,232,2,2,4,11,1,4),_CpqSiProcMicroPatchFamily_Type())
cpqSiProcMicroPatchFamily.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiProcMicroPatchFamily.setStatus(_B)
class _CpqSiPowerMgmtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3)))
_CpqSiPowerMgmtStatus_Type.__name__=_C
_CpqSiPowerMgmtStatus_Object=MibScalar
cpqSiPowerMgmtStatus=_CpqSiPowerMgmtStatus_Object((1,3,6,1,4,1,232,2,2,4,12),_CpqSiPowerMgmtStatus_Type())
cpqSiPowerMgmtStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPowerMgmtStatus.setStatus(_B)
_CpqSiRebootFlags_Type=Integer32
_CpqSiRebootFlags_Object=MibScalar
cpqSiRebootFlags=_CpqSiRebootFlags_Object((1,3,6,1,4,1,232,2,2,4,13),_CpqSiRebootFlags_Type())
cpqSiRebootFlags.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiRebootFlags.setStatus(_B)
class _CpqSiMemErrorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMemErrorIndex_Type.__name__=_C
_CpqSiMemErrorIndex_Object=MibScalar
cpqSiMemErrorIndex=_CpqSiMemErrorIndex_Object((1,3,6,1,4,1,232,2,2,4,14),_CpqSiMemErrorIndex_Type())
cpqSiMemErrorIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemErrorIndex.setStatus(_B)
class _CpqSiMemECCCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3)))
_CpqSiMemECCCondition_Type.__name__=_C
_CpqSiMemECCCondition_Object=MibScalar
cpqSiMemECCCondition=_CpqSiMemECCCondition_Object((1,3,6,1,4,1,232,2,2,4,15),_CpqSiMemECCCondition_Type())
cpqSiMemECCCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemECCCondition.setStatus(_B)
class _CpqSiMemConfigChangeData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,383))
_CpqSiMemConfigChangeData_Type.__name__=_E
_CpqSiMemConfigChangeData_Object=MibScalar
cpqSiMemConfigChangeData=_CpqSiMemConfigChangeData_Object((1,3,6,1,4,1,232,2,2,4,16),_CpqSiMemConfigChangeData_Type())
cpqSiMemConfigChangeData.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMemConfigChangeData.setStatus(_B)
class _CpqSiServerSystemId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSiServerSystemId_Type.__name__=_E
_CpqSiServerSystemId_Object=MibScalar
cpqSiServerSystemId=_CpqSiServerSystemId_Object((1,3,6,1,4,1,232,2,2,4,17),_CpqSiServerSystemId_Type())
cpqSiServerSystemId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiServerSystemId.setStatus(_B)
class _CpqSiPowerScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unsupported',1),(_F,2),('power-saver',3),('balanced',4),('high-performance',5),('user-defined',6)))
_CpqSiPowerScheme_Type.__name__=_C
_CpqSiPowerScheme_Object=MibScalar
cpqSiPowerScheme=_CpqSiPowerScheme_Object((1,3,6,1,4,1,232,2,2,4,18),_CpqSiPowerScheme_Type())
cpqSiPowerScheme.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPowerScheme.setStatus(_D)
class _CpqSiPowerSchemeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiPowerSchemeName_Type.__name__=_E
_CpqSiPowerSchemeName_Object=MibScalar
cpqSiPowerSchemeName=_CpqSiPowerSchemeName_Object((1,3,6,1,4,1,232,2,2,4,19),_CpqSiPowerSchemeName_Type())
cpqSiPowerSchemeName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPowerSchemeName.setStatus(_D)
class _CpqSiCurrentPerformanceStatePointer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiCurrentPerformanceStatePointer_Type.__name__=_C
_CpqSiCurrentPerformanceStatePointer_Object=MibScalar
cpqSiCurrentPerformanceStatePointer=_CpqSiCurrentPerformanceStatePointer_Object((1,3,6,1,4,1,232,2,2,4,20),_CpqSiCurrentPerformanceStatePointer_Type())
cpqSiCurrentPerformanceStatePointer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiCurrentPerformanceStatePointer.setStatus(_D)
class _CpqSiMinPerformanceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMinPerformanceState_Type.__name__=_C
_CpqSiMinPerformanceState_Object=MibScalar
cpqSiMinPerformanceState=_CpqSiMinPerformanceState_Object((1,3,6,1,4,1,232,2,2,4,21),_CpqSiMinPerformanceState_Type())
cpqSiMinPerformanceState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMinPerformanceState.setStatus(_D)
class _CpqSiMaxPerformanceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMaxPerformanceState_Type.__name__=_C
_CpqSiMaxPerformanceState_Object=MibScalar
cpqSiMaxPerformanceState=_CpqSiMaxPerformanceState_Object((1,3,6,1,4,1,232,2,2,4,22),_CpqSiMaxPerformanceState_Type())
cpqSiMaxPerformanceState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMaxPerformanceState.setStatus(_D)
_CpqSiPerfStateTable_Object=MibTable
cpqSiPerfStateTable=_CpqSiPerfStateTable_Object((1,3,6,1,4,1,232,2,2,4,23))
if mibBuilder.loadTexts:cpqSiPerfStateTable.setStatus(_D)
_CpqSiPerfStateEntry_Object=MibTableRow
cpqSiPerfStateEntry=_CpqSiPerfStateEntry_Object((1,3,6,1,4,1,232,2,2,4,23,1))
cpqSiPerfStateEntry.setIndexNames((0,_G,_i))
if mibBuilder.loadTexts:cpqSiPerfStateEntry.setStatus(_D)
class _CpqSiPerfStateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiPerfStateIndex_Type.__name__=_C
_CpqSiPerfStateIndex_Object=MibTableColumn
cpqSiPerfStateIndex=_CpqSiPerfStateIndex_Object((1,3,6,1,4,1,232,2,2,4,23,1,1),_CpqSiPerfStateIndex_Type())
cpqSiPerfStateIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPerfStateIndex.setStatus(_D)
class _CpqSiPerfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiPerfState_Type.__name__=_C
_CpqSiPerfState_Object=MibTableColumn
cpqSiPerfState=_CpqSiPerfState_Object((1,3,6,1,4,1,232,2,2,4,23,1,2),_CpqSiPerfState_Type())
cpqSiPerfState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPerfState.setStatus(_D)
class _CpqSiPerfStateCpuFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSiPerfStateCpuFrequency_Type.__name__=_C
_CpqSiPerfStateCpuFrequency_Object=MibTableColumn
cpqSiPerfStateCpuFrequency=_CpqSiPerfStateCpuFrequency_Object((1,3,6,1,4,1,232,2,2,4,23,1,3),_CpqSiPerfStateCpuFrequency_Type())
cpqSiPerfStateCpuFrequency.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPerfStateCpuFrequency.setStatus(_D)
class _CpqSiPerfStateCpuPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSiPerfStateCpuPower_Type.__name__=_C
_CpqSiPerfStateCpuPower_Object=MibTableColumn
cpqSiPerfStateCpuPower=_CpqSiPerfStateCpuPower_Object((1,3,6,1,4,1,232,2,2,4,23,1,4),_CpqSiPerfStateCpuPower_Type())
cpqSiPerfStateCpuPower.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPerfStateCpuPower.setStatus(_D)
class _CpqSiTPMmodule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_j,2),('presentEnabled',3),('presentDisabled',4)))
_CpqSiTPMmodule_Type.__name__=_C
_CpqSiTPMmodule_Object=MibScalar
cpqSiTPMmodule=_CpqSiTPMmodule_Object((1,3,6,1,4,1,232,2,2,4,24),_CpqSiTPMmodule_Type())
cpqSiTPMmodule.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiTPMmodule.setStatus(_D)
class _CpqSiTrustedModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiTrustedModuleType_Type.__name__=_C
_CpqSiTrustedModuleType_Object=MibScalar
cpqSiTrustedModuleType=_CpqSiTrustedModuleType_Object((1,3,6,1,4,1,232,2,2,4,25),_CpqSiTrustedModuleType_Type())
cpqSiTrustedModuleType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiTrustedModuleType.setStatus(_D)
class _CpqSiSystemTelemetryMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('cpuUtilization',1),('memoryBusUtilization',2),('ioBusUtilization',3),('cpuInterconnectUtilization',4),('jitterCount',5),('cpu0PowerUtilization',6),('cpu1PowerUtilization',7),('cpu2PowerUtilization',8),('cpu3PowerUtilization',9),('cpu0AverageFrequency',10),('cpu1AverageFrequency',11),('cpu2AverageFrequency',12),('cpu3AverageFrequency',13)))
_CpqSiSystemTelemetryMetric_Type.__name__=_C
_CpqSiSystemTelemetryMetric_Object=MibScalar
cpqSiSystemTelemetryMetric=_CpqSiSystemTelemetryMetric_Object((1,3,6,1,4,1,232,2,2,4,26),_CpqSiSystemTelemetryMetric_Type())
cpqSiSystemTelemetryMetric.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSystemTelemetryMetric.setStatus(_D)
class _CpqSiSystemTelemetryThresholdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aboveUpperThreshold',1),('belowLowerThreshold',2)))
_CpqSiSystemTelemetryThresholdStatus_Type.__name__=_C
_CpqSiSystemTelemetryThresholdStatus_Object=MibScalar
cpqSiSystemTelemetryThresholdStatus=_CpqSiSystemTelemetryThresholdStatus_Object((1,3,6,1,4,1,232,2,2,4,27),_CpqSiSystemTelemetryThresholdStatus_Type())
cpqSiSystemTelemetryThresholdStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSystemTelemetryThresholdStatus.setStatus(_D)
_CpqSiBoardRev_ObjectIdentity=ObjectIdentity
cpqSiBoardRev=_CpqSiBoardRev_ObjectIdentity((1,3,6,1,4,1,232,2,2,5))
class _CpqSiCurRevDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CpqSiCurRevDate_Type.__name__=_E
_CpqSiCurRevDate_Object=MibScalar
cpqSiCurRevDate=_CpqSiCurRevDate_Object((1,3,6,1,4,1,232,2,2,5,1),_CpqSiCurRevDate_Type())
cpqSiCurRevDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiCurRevDate.setStatus(_B)
class _CpqSiPrevRevDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CpqSiPrevRevDate_Type.__name__=_E
_CpqSiPrevRevDate_Object=MibScalar
cpqSiPrevRevDate=_CpqSiPrevRevDate_Object((1,3,6,1,4,1,232,2,2,5,2),_CpqSiPrevRevDate_Type())
cpqSiPrevRevDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiPrevRevDate.setStatus(_B)
_CpqSiBoardRevTable_Object=MibTable
cpqSiBoardRevTable=_CpqSiBoardRevTable_Object((1,3,6,1,4,1,232,2,2,5,3))
if mibBuilder.loadTexts:cpqSiBoardRevTable.setStatus(_B)
_CpqSiBoardRevEntry_Object=MibTableRow
cpqSiBoardRevEntry=_CpqSiBoardRevEntry_Object((1,3,6,1,4,1,232,2,2,5,3,1))
cpqSiBoardRevEntry.setIndexNames((0,_G,_k),(0,_G,_l))
if mibBuilder.loadTexts:cpqSiBoardRevEntry.setStatus(_B)
class _CpqSiBoardRevSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiBoardRevSlotIndex_Type.__name__=_C
_CpqSiBoardRevSlotIndex_Object=MibTableColumn
cpqSiBoardRevSlotIndex=_CpqSiBoardRevSlotIndex_Object((1,3,6,1,4,1,232,2,2,5,3,1,1),_CpqSiBoardRevSlotIndex_Type())
cpqSiBoardRevSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiBoardRevSlotIndex.setStatus(_B)
class _CpqSiBoardRevIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiBoardRevIndex_Type.__name__=_C
_CpqSiBoardRevIndex_Object=MibTableColumn
cpqSiBoardRevIndex=_CpqSiBoardRevIndex_Object((1,3,6,1,4,1,232,2,2,5,3,1,2),_CpqSiBoardRevIndex_Type())
cpqSiBoardRevIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiBoardRevIndex.setStatus(_B)
class _CpqSiBoardRevId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqSiBoardRevId_Type.__name__=_E
_CpqSiBoardRevId_Object=MibTableColumn
cpqSiBoardRevId=_CpqSiBoardRevId_Object((1,3,6,1,4,1,232,2,2,5,3,1,3),_CpqSiBoardRevId_Type())
cpqSiBoardRevId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiBoardRevId.setStatus(_B)
class _CpqSiBoardRevCur_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSiBoardRevCur_Type.__name__=_E
_CpqSiBoardRevCur_Object=MibTableColumn
cpqSiBoardRevCur=_CpqSiBoardRevCur_Object((1,3,6,1,4,1,232,2,2,5,3,1,4),_CpqSiBoardRevCur_Type())
cpqSiBoardRevCur.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiBoardRevCur.setStatus(_B)
class _CpqSiBoardRevPrev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSiBoardRevPrev_Type.__name__=_E
_CpqSiBoardRevPrev_Object=MibTableColumn
cpqSiBoardRevPrev=_CpqSiBoardRevPrev_Object((1,3,6,1,4,1,232,2,2,5,3,1,5),_CpqSiBoardRevPrev_Type())
cpqSiBoardRevPrev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiBoardRevPrev.setStatus(_B)
class _CpqSiBoardRevHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiBoardRevHwLocation_Type.__name__=_E
_CpqSiBoardRevHwLocation_Object=MibTableColumn
cpqSiBoardRevHwLocation=_CpqSiBoardRevHwLocation_Object((1,3,6,1,4,1,232,2,2,5,3,1,6),_CpqSiBoardRevHwLocation_Type())
cpqSiBoardRevHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiBoardRevHwLocation.setStatus(_D)
_CpqSiFirmwareRevTable_Object=MibTable
cpqSiFirmwareRevTable=_CpqSiFirmwareRevTable_Object((1,3,6,1,4,1,232,2,2,5,4))
if mibBuilder.loadTexts:cpqSiFirmwareRevTable.setStatus(_B)
_CpqSiFirmwareRevEntry_Object=MibTableRow
cpqSiFirmwareRevEntry=_CpqSiFirmwareRevEntry_Object((1,3,6,1,4,1,232,2,2,5,4,1))
cpqSiFirmwareRevEntry.setIndexNames((0,_G,_m))
if mibBuilder.loadTexts:cpqSiFirmwareRevEntry.setStatus(_B)
_CpqSiFirmwareRevIndex_Type=Integer32
_CpqSiFirmwareRevIndex_Object=MibTableColumn
cpqSiFirmwareRevIndex=_CpqSiFirmwareRevIndex_Object((1,3,6,1,4,1,232,2,2,5,4,1,1),_CpqSiFirmwareRevIndex_Type())
cpqSiFirmwareRevIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareRevIndex.setStatus(_B)
_CpqSiFirmwareRevDesc_Type=DisplayString
_CpqSiFirmwareRevDesc_Object=MibTableColumn
cpqSiFirmwareRevDesc=_CpqSiFirmwareRevDesc_Object((1,3,6,1,4,1,232,2,2,5,4,1,2),_CpqSiFirmwareRevDesc_Type())
cpqSiFirmwareRevDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareRevDesc.setStatus(_B)
_CpqSiFirmwareRevString_Type=DisplayString
_CpqSiFirmwareRevString_Object=MibTableColumn
cpqSiFirmwareRevString=_CpqSiFirmwareRevString_Object((1,3,6,1,4,1,232,2,2,5,4,1,3),_CpqSiFirmwareRevString_Type())
cpqSiFirmwareRevString.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareRevString.setStatus(_B)
_CpqSiFirmwareRevCellTablePtr_Type=Integer32
_CpqSiFirmwareRevCellTablePtr_Object=MibTableColumn
cpqSiFirmwareRevCellTablePtr=_CpqSiFirmwareRevCellTablePtr_Object((1,3,6,1,4,1,232,2,2,5,4,1,4),_CpqSiFirmwareRevCellTablePtr_Type())
cpqSiFirmwareRevCellTablePtr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareRevCellTablePtr.setStatus(_L)
class _CpqSiFirmwareLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiFirmwareLocation_Type.__name__=_E
_CpqSiFirmwareLocation_Object=MibTableColumn
cpqSiFirmwareLocation=_CpqSiFirmwareLocation_Object((1,3,6,1,4,1,232,2,2,5,4,1,5),_CpqSiFirmwareLocation_Type())
cpqSiFirmwareLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareLocation.setStatus(_D)
class _CpqSiFirmwareStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('active',2),('inactive',3)))
_CpqSiFirmwareStatus_Type.__name__=_C
_CpqSiFirmwareStatus_Object=MibTableColumn
cpqSiFirmwareStatus=_CpqSiFirmwareStatus_Object((1,3,6,1,4,1,232,2,2,5,4,1,6),_CpqSiFirmwareStatus_Type())
cpqSiFirmwareStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareStatus.setStatus(_D)
_CpqSiFirmwareCfgTable_Object=MibTable
cpqSiFirmwareCfgTable=_CpqSiFirmwareCfgTable_Object((1,3,6,1,4,1,232,2,2,5,5))
if mibBuilder.loadTexts:cpqSiFirmwareCfgTable.setStatus(_B)
_CpqSiFirmwareCfgEntry_Object=MibTableRow
cpqSiFirmwareCfgEntry=_CpqSiFirmwareCfgEntry_Object((1,3,6,1,4,1,232,2,2,5,5,1))
cpqSiFirmwareCfgEntry.setIndexNames((0,_G,_n))
if mibBuilder.loadTexts:cpqSiFirmwareCfgEntry.setStatus(_B)
_CpqSiFirmwareCfgName_Type=DisplayString
_CpqSiFirmwareCfgName_Object=MibTableColumn
cpqSiFirmwareCfgName=_CpqSiFirmwareCfgName_Object((1,3,6,1,4,1,232,2,2,5,5,1,1),_CpqSiFirmwareCfgName_Type())
cpqSiFirmwareCfgName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareCfgName.setStatus(_B)
_CpqSiFirmwareCfgValue_Type=DisplayString
_CpqSiFirmwareCfgValue_Object=MibTableColumn
cpqSiFirmwareCfgValue=_CpqSiFirmwareCfgValue_Object((1,3,6,1,4,1,232,2,2,5,5,1,2),_CpqSiFirmwareCfgValue_Type())
cpqSiFirmwareCfgValue.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFirmwareCfgValue.setStatus(_B)
_CpqSiRackServer_ObjectIdentity=ObjectIdentity
cpqSiRackServer=_CpqSiRackServer_ObjectIdentity((1,3,6,1,4,1,232,2,2,6))
class _CpqSiRackServerShutdownRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('master',2),('slave',3)))
_CpqSiRackServerShutdownRole_Type.__name__=_C
_CpqSiRackServerShutdownRole_Object=MibScalar
cpqSiRackServerShutdownRole=_CpqSiRackServerShutdownRole_Object((1,3,6,1,4,1,232,2,2,6,1),_CpqSiRackServerShutdownRole_Type())
cpqSiRackServerShutdownRole.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiRackServerShutdownRole.setStatus(_B)
class _CpqSiRackServerMasterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_CpqSiRackServerMasterName_Type.__name__=_E
_CpqSiRackServerMasterName_Object=MibScalar
cpqSiRackServerMasterName=_CpqSiRackServerMasterName_Object((1,3,6,1,4,1,232,2,2,6,2),_CpqSiRackServerMasterName_Type())
cpqSiRackServerMasterName.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiRackServerMasterName.setStatus(_B)
_CpqSiVideo_ObjectIdentity=ObjectIdentity
cpqSiVideo=_CpqSiVideo_ObjectIdentity((1,3,6,1,4,1,232,2,2,7))
class _CpqSiVideoEdidRaw_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CpqSiVideoEdidRaw_Type.__name__=_Q
_CpqSiVideoEdidRaw_Object=MibScalar
cpqSiVideoEdidRaw=_CpqSiVideoEdidRaw_Object((1,3,6,1,4,1,232,2,2,7,1),_CpqSiVideoEdidRaw_Type())
cpqSiVideoEdidRaw.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoEdidRaw.setStatus(_L)
class _CpqSiVideoDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiVideoDesc_Type.__name__=_E
_CpqSiVideoDesc_Object=MibScalar
cpqSiVideoDesc=_CpqSiVideoDesc_Object((1,3,6,1,4,1,232,2,2,7,2),_CpqSiVideoDesc_Type())
cpqSiVideoDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoDesc.setStatus(_L)
class _CpqSiVideoSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqSiVideoSerialNumber_Type.__name__=_E
_CpqSiVideoSerialNumber_Object=MibScalar
cpqSiVideoSerialNumber=_CpqSiVideoSerialNumber_Object((1,3,6,1,4,1,232,2,2,7,3),_CpqSiVideoSerialNumber_Type())
cpqSiVideoSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoSerialNumber.setStatus(_L)
class _CpqSiVideoManufactureDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSiVideoManufactureDate_Type.__name__=_Q
_CpqSiVideoManufactureDate_Object=MibScalar
cpqSiVideoManufactureDate=_CpqSiVideoManufactureDate_Object((1,3,6,1,4,1,232,2,2,7,4),_CpqSiVideoManufactureDate_Type())
cpqSiVideoManufactureDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoManufactureDate.setStatus(_L)
class _CpqSiVideoHeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiVideoHeight_Type.__name__=_C
_CpqSiVideoHeight_Object=MibScalar
cpqSiVideoHeight=_CpqSiVideoHeight_Object((1,3,6,1,4,1,232,2,2,7,5),_CpqSiVideoHeight_Type())
cpqSiVideoHeight.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoHeight.setStatus(_L)
class _CpqSiVideoWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiVideoWidth_Type.__name__=_C
_CpqSiVideoWidth_Object=MibScalar
cpqSiVideoWidth=_CpqSiVideoWidth_Object((1,3,6,1,4,1,232,2,2,7,6),_CpqSiVideoWidth_Type())
cpqSiVideoWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoWidth.setStatus(_L)
class _CpqSiVideoMaxHorPixel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiVideoMaxHorPixel_Type.__name__=_C
_CpqSiVideoMaxHorPixel_Object=MibScalar
cpqSiVideoMaxHorPixel=_CpqSiVideoMaxHorPixel_Object((1,3,6,1,4,1,232,2,2,7,7),_CpqSiVideoMaxHorPixel_Type())
cpqSiVideoMaxHorPixel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoMaxHorPixel.setStatus(_L)
class _CpqSiVideoMaxVertPixel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiVideoMaxVertPixel_Type.__name__=_C
_CpqSiVideoMaxVertPixel_Object=MibScalar
cpqSiVideoMaxVertPixel=_CpqSiVideoMaxVertPixel_Object((1,3,6,1,4,1,232,2,2,7,8),_CpqSiVideoMaxVertPixel_Type())
cpqSiVideoMaxVertPixel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoMaxVertPixel.setStatus(_L)
class _CpqSiVideoMaxRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiVideoMaxRefreshRate_Type.__name__=_C
_CpqSiVideoMaxRefreshRate_Object=MibScalar
cpqSiVideoMaxRefreshRate=_CpqSiVideoMaxRefreshRate_Object((1,3,6,1,4,1,232,2,2,7,9),_CpqSiVideoMaxRefreshRate_Type())
cpqSiVideoMaxRefreshRate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiVideoMaxRefreshRate.setStatus(_L)
_CpqSiMonitor_ObjectIdentity=ObjectIdentity
cpqSiMonitor=_CpqSiMonitor_ObjectIdentity((1,3,6,1,4,1,232,2,2,8))
class _CpqSiMonitorOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiMonitorOverallCondition_Type.__name__=_C
_CpqSiMonitorOverallCondition_Object=MibScalar
cpqSiMonitorOverallCondition=_CpqSiMonitorOverallCondition_Object((1,3,6,1,4,1,232,2,2,8,1),_CpqSiMonitorOverallCondition_Type())
cpqSiMonitorOverallCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorOverallCondition.setStatus(_B)
_CpqSiMonitorTable_Object=MibTable
cpqSiMonitorTable=_CpqSiMonitorTable_Object((1,3,6,1,4,1,232,2,2,8,2))
if mibBuilder.loadTexts:cpqSiMonitorTable.setStatus(_B)
_CpqSiMonitorEntry_Object=MibTableRow
cpqSiMonitorEntry=_CpqSiMonitorEntry_Object((1,3,6,1,4,1,232,2,2,8,2,1))
cpqSiMonitorEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:cpqSiMonitorEntry.setStatus(_B)
class _CpqSiMonitorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CpqSiMonitorIndex_Type.__name__=_C
_CpqSiMonitorIndex_Object=MibTableColumn
cpqSiMonitorIndex=_CpqSiMonitorIndex_Object((1,3,6,1,4,1,232,2,2,8,2,1,1),_CpqSiMonitorIndex_Type())
cpqSiMonitorIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorIndex.setStatus(_B)
class _CpqSiMonitorEdidRaw_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_CpqSiMonitorEdidRaw_Type.__name__=_Q
_CpqSiMonitorEdidRaw_Object=MibTableColumn
cpqSiMonitorEdidRaw=_CpqSiMonitorEdidRaw_Object((1,3,6,1,4,1,232,2,2,8,2,1,2),_CpqSiMonitorEdidRaw_Type())
cpqSiMonitorEdidRaw.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorEdidRaw.setStatus(_B)
class _CpqSiMonitorDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMonitorDesc_Type.__name__=_E
_CpqSiMonitorDesc_Object=MibTableColumn
cpqSiMonitorDesc=_CpqSiMonitorDesc_Object((1,3,6,1,4,1,232,2,2,8,2,1,3),_CpqSiMonitorDesc_Type())
cpqSiMonitorDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorDesc.setStatus(_B)
class _CpqSiMonitorSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqSiMonitorSerialNumber_Type.__name__=_E
_CpqSiMonitorSerialNumber_Object=MibTableColumn
cpqSiMonitorSerialNumber=_CpqSiMonitorSerialNumber_Object((1,3,6,1,4,1,232,2,2,8,2,1,4),_CpqSiMonitorSerialNumber_Type())
cpqSiMonitorSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorSerialNumber.setStatus(_B)
class _CpqSiMonitorManufactureDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSiMonitorManufactureDate_Type.__name__=_Q
_CpqSiMonitorManufactureDate_Object=MibTableColumn
cpqSiMonitorManufactureDate=_CpqSiMonitorManufactureDate_Object((1,3,6,1,4,1,232,2,2,8,2,1,5),_CpqSiMonitorManufactureDate_Type())
cpqSiMonitorManufactureDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorManufactureDate.setStatus(_B)
class _CpqSiMonitorHeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiMonitorHeight_Type.__name__=_C
_CpqSiMonitorHeight_Object=MibTableColumn
cpqSiMonitorHeight=_CpqSiMonitorHeight_Object((1,3,6,1,4,1,232,2,2,8,2,1,6),_CpqSiMonitorHeight_Type())
cpqSiMonitorHeight.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorHeight.setStatus(_B)
class _CpqSiMonitorWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiMonitorWidth_Type.__name__=_C
_CpqSiMonitorWidth_Object=MibTableColumn
cpqSiMonitorWidth=_CpqSiMonitorWidth_Object((1,3,6,1,4,1,232,2,2,8,2,1,7),_CpqSiMonitorWidth_Type())
cpqSiMonitorWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorWidth.setStatus(_B)
class _CpqSiMonitorMaxHorPixel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMonitorMaxHorPixel_Type.__name__=_C
_CpqSiMonitorMaxHorPixel_Object=MibTableColumn
cpqSiMonitorMaxHorPixel=_CpqSiMonitorMaxHorPixel_Object((1,3,6,1,4,1,232,2,2,8,2,1,8),_CpqSiMonitorMaxHorPixel_Type())
cpqSiMonitorMaxHorPixel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorMaxHorPixel.setStatus(_B)
class _CpqSiMonitorMaxVertPixel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMonitorMaxVertPixel_Type.__name__=_C
_CpqSiMonitorMaxVertPixel_Object=MibTableColumn
cpqSiMonitorMaxVertPixel=_CpqSiMonitorMaxVertPixel_Object((1,3,6,1,4,1,232,2,2,8,2,1,9),_CpqSiMonitorMaxVertPixel_Type())
cpqSiMonitorMaxVertPixel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorMaxVertPixel.setStatus(_B)
class _CpqSiMonitorMaxRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiMonitorMaxRefreshRate_Type.__name__=_C
_CpqSiMonitorMaxRefreshRate_Object=MibTableColumn
cpqSiMonitorMaxRefreshRate=_CpqSiMonitorMaxRefreshRate_Object((1,3,6,1,4,1,232,2,2,8,2,1,10),_CpqSiMonitorMaxRefreshRate_Type())
cpqSiMonitorMaxRefreshRate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorMaxRefreshRate.setStatus(_B)
class _CpqSiMonitorManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiMonitorManufacturer_Type.__name__=_E
_CpqSiMonitorManufacturer_Object=MibTableColumn
cpqSiMonitorManufacturer=_CpqSiMonitorManufacturer_Object((1,3,6,1,4,1,232,2,2,8,2,1,11),_CpqSiMonitorManufacturer_Type())
cpqSiMonitorManufacturer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorManufacturer.setStatus(_B)
class _CpqSiMonitorThermalCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3)))
_CpqSiMonitorThermalCondition_Type.__name__=_C
_CpqSiMonitorThermalCondition_Object=MibTableColumn
cpqSiMonitorThermalCondition=_CpqSiMonitorThermalCondition_Object((1,3,6,1,4,1,232,2,2,8,2,1,12),_CpqSiMonitorThermalCondition_Type())
cpqSiMonitorThermalCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorThermalCondition.setStatus(_B)
class _CpqSiMonitorOperationalCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiMonitorOperationalCondition_Type.__name__=_C
_CpqSiMonitorOperationalCondition_Object=MibTableColumn
cpqSiMonitorOperationalCondition=_CpqSiMonitorOperationalCondition_Object((1,3,6,1,4,1,232,2,2,8,2,1,13),_CpqSiMonitorOperationalCondition_Type())
cpqSiMonitorOperationalCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorOperationalCondition.setStatus(_B)
class _CpqSiMonitorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_R,2),(_M,3),('thermalDegraded',4),('operationalFailure',5)))
_CpqSiMonitorStatus_Type.__name__=_C
_CpqSiMonitorStatus_Object=MibTableColumn
cpqSiMonitorStatus=_CpqSiMonitorStatus_Object((1,3,6,1,4,1,232,2,2,8,2,1,14),_CpqSiMonitorStatus_Type())
cpqSiMonitorStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMonitorStatus.setStatus(_B)
_CpqSiHotPlugSlot_ObjectIdentity=ObjectIdentity
cpqSiHotPlugSlot=_CpqSiHotPlugSlot_ObjectIdentity((1,3,6,1,4,1,232,2,2,9))
class _CpqSiHotPlugSlotSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_Z,2),(_g,3)))
_CpqSiHotPlugSlotSupported_Type.__name__=_C
_CpqSiHotPlugSlotSupported_Object=MibScalar
cpqSiHotPlugSlotSupported=_CpqSiHotPlugSlotSupported_Object((1,3,6,1,4,1,232,2,2,9,1),_CpqSiHotPlugSlotSupported_Type())
cpqSiHotPlugSlotSupported.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotSupported.setStatus(_B)
class _CpqSiHotPlugSlotCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiHotPlugSlotCondition_Type.__name__=_C
_CpqSiHotPlugSlotCondition_Object=MibScalar
cpqSiHotPlugSlotCondition=_CpqSiHotPlugSlotCondition_Object((1,3,6,1,4,1,232,2,2,9,2),_CpqSiHotPlugSlotCondition_Type())
cpqSiHotPlugSlotCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotCondition.setStatus(_B)
_CpqSiHotPlugSlotChangeCount_Type=Integer32
_CpqSiHotPlugSlotChangeCount_Object=MibScalar
cpqSiHotPlugSlotChangeCount=_CpqSiHotPlugSlotChangeCount_Object((1,3,6,1,4,1,232,2,2,9,3),_CpqSiHotPlugSlotChangeCount_Type())
cpqSiHotPlugSlotChangeCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotChangeCount.setStatus(_B)
_CpqSiHotPlugSlotTable_Object=MibTable
cpqSiHotPlugSlotTable=_CpqSiHotPlugSlotTable_Object((1,3,6,1,4,1,232,2,2,9,4))
if mibBuilder.loadTexts:cpqSiHotPlugSlotTable.setStatus(_B)
_CpqSiHotPlugSlotEntry_Object=MibTableRow
cpqSiHotPlugSlotEntry=_CpqSiHotPlugSlotEntry_Object((1,3,6,1,4,1,232,2,2,9,4,1))
cpqSiHotPlugSlotEntry.setIndexNames((0,_G,_V),(0,_G,_W))
if mibBuilder.loadTexts:cpqSiHotPlugSlotEntry.setStatus(_B)
class _CpqSiHotPlugSlotChassis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiHotPlugSlotChassis_Type.__name__=_C
_CpqSiHotPlugSlotChassis_Object=MibTableColumn
cpqSiHotPlugSlotChassis=_CpqSiHotPlugSlotChassis_Object((1,3,6,1,4,1,232,2,2,9,4,1,1),_CpqSiHotPlugSlotChassis_Type())
cpqSiHotPlugSlotChassis.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotChassis.setStatus(_B)
class _CpqSiHotPlugSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiHotPlugSlotIndex_Type.__name__=_C
_CpqSiHotPlugSlotIndex_Object=MibTableColumn
cpqSiHotPlugSlotIndex=_CpqSiHotPlugSlotIndex_Object((1,3,6,1,4,1,232,2,2,9,4,1,2),_CpqSiHotPlugSlotIndex_Type())
cpqSiHotPlugSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotIndex.setStatus(_B)
class _CpqSiHotPlugSlotBoardPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('present',2),(_j,3),('presentButSuspended',4)))
_CpqSiHotPlugSlotBoardPresent_Type.__name__=_C
_CpqSiHotPlugSlotBoardPresent_Object=MibTableColumn
cpqSiHotPlugSlotBoardPresent=_CpqSiHotPlugSlotBoardPresent_Object((1,3,6,1,4,1,232,2,2,9,4,1,3),_CpqSiHotPlugSlotBoardPresent_Type())
cpqSiHotPlugSlotBoardPresent.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotBoardPresent.setStatus(_B)
class _CpqSiHotPlugSlotPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('powerOn',2),('powerOff',3)))
_CpqSiHotPlugSlotPowerState_Type.__name__=_C
_CpqSiHotPlugSlotPowerState_Object=MibTableColumn
cpqSiHotPlugSlotPowerState=_CpqSiHotPlugSlotPowerState_Object((1,3,6,1,4,1,232,2,2,9,4,1,4),_CpqSiHotPlugSlotPowerState_Type())
cpqSiHotPlugSlotPowerState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotPowerState.setStatus(_B)
class _CpqSiHotPlugSlotBoardCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiHotPlugSlotBoardCondition_Type.__name__=_C
_CpqSiHotPlugSlotBoardCondition_Object=MibTableColumn
cpqSiHotPlugSlotBoardCondition=_CpqSiHotPlugSlotBoardCondition_Object((1,3,6,1,4,1,232,2,2,9,4,1,5),_CpqSiHotPlugSlotBoardCondition_Type())
cpqSiHotPlugSlotBoardCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotBoardCondition.setStatus(_B)
class _CpqSiHotPlugSlotErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noError',1),('generalError',2),('wrongRevision',3),('wrongBoard',4),('cannotConfig',5),('powerFault',6),('unexpectedPowerLoss',7),('wrongSpeed',8),('functionalFailure',9)))
_CpqSiHotPlugSlotErrorStatus_Type.__name__=_C
_CpqSiHotPlugSlotErrorStatus_Object=MibTableColumn
cpqSiHotPlugSlotErrorStatus=_CpqSiHotPlugSlotErrorStatus_Object((1,3,6,1,4,1,232,2,2,9,4,1,6),_CpqSiHotPlugSlotErrorStatus_Type())
cpqSiHotPlugSlotErrorStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotErrorStatus.setStatus(_B)
class _CpqSiHotPlugSlotHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiHotPlugSlotHwLocation_Type.__name__=_E
_CpqSiHotPlugSlotHwLocation_Object=MibTableColumn
cpqSiHotPlugSlotHwLocation=_CpqSiHotPlugSlotHwLocation_Object((1,3,6,1,4,1,232,2,2,9,4,1,7),_CpqSiHotPlugSlotHwLocation_Type())
cpqSiHotPlugSlotHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiHotPlugSlotHwLocation.setStatus(_D)
_CpqSiSystemBattery_ObjectIdentity=ObjectIdentity
cpqSiSystemBattery=_CpqSiSystemBattery_ObjectIdentity((1,3,6,1,4,1,232,2,2,10))
class _CpqSiSystemBatteryOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiSystemBatteryOverallCondition_Type.__name__=_C
_CpqSiSystemBatteryOverallCondition_Object=MibScalar
cpqSiSystemBatteryOverallCondition=_CpqSiSystemBatteryOverallCondition_Object((1,3,6,1,4,1,232,2,2,10,1),_CpqSiSystemBatteryOverallCondition_Type())
cpqSiSystemBatteryOverallCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSystemBatteryOverallCondition.setStatus(_B)
_CpqSiSysBatteryTable_Object=MibTable
cpqSiSysBatteryTable=_CpqSiSysBatteryTable_Object((1,3,6,1,4,1,232,2,2,10,2))
if mibBuilder.loadTexts:cpqSiSysBatteryTable.setStatus(_B)
_CpqSiSysBatteryEntry_Object=MibTableRow
cpqSiSysBatteryEntry=_CpqSiSysBatteryEntry_Object((1,3,6,1,4,1,232,2,2,10,2,1))
cpqSiSysBatteryEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:cpqSiSysBatteryEntry.setStatus(_B)
class _CpqSiSysBatteryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiSysBatteryIndex_Type.__name__=_C
_CpqSiSysBatteryIndex_Object=MibTableColumn
cpqSiSysBatteryIndex=_CpqSiSysBatteryIndex_Object((1,3,6,1,4,1,232,2,2,10,2,1,1),_CpqSiSysBatteryIndex_Type())
cpqSiSysBatteryIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryIndex.setStatus(_B)
class _CpqSiSysBatteryModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysBatteryModel_Type.__name__=_E
_CpqSiSysBatteryModel_Object=MibTableColumn
cpqSiSysBatteryModel=_CpqSiSysBatteryModel_Object((1,3,6,1,4,1,232,2,2,10,2,1,2),_CpqSiSysBatteryModel_Type())
cpqSiSysBatteryModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryModel.setStatus(_B)
class _CpqSiSysBatterySerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysBatterySerialNum_Type.__name__=_E
_CpqSiSysBatterySerialNum_Object=MibTableColumn
cpqSiSysBatterySerialNum=_CpqSiSysBatterySerialNum_Object((1,3,6,1,4,1,232,2,2,10,2,1,3),_CpqSiSysBatterySerialNum_Type())
cpqSiSysBatterySerialNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatterySerialNum.setStatus(_B)
class _CpqSiSysBatteryAssetTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysBatteryAssetTag_Type.__name__=_E
_CpqSiSysBatteryAssetTag_Object=MibTableColumn
cpqSiSysBatteryAssetTag=_CpqSiSysBatteryAssetTag_Object((1,3,6,1,4,1,232,2,2,10,2,1,4),_CpqSiSysBatteryAssetTag_Type())
cpqSiSysBatteryAssetTag.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryAssetTag.setStatus(_B)
class _CpqSiSysBatteryManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysBatteryManufacturer_Type.__name__=_E
_CpqSiSysBatteryManufacturer_Object=MibTableColumn
cpqSiSysBatteryManufacturer=_CpqSiSysBatteryManufacturer_Object((1,3,6,1,4,1,232,2,2,10,2,1,5),_CpqSiSysBatteryManufacturer_Type())
cpqSiSysBatteryManufacturer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryManufacturer.setStatus(_B)
class _CpqSiSysBatteryDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSiSysBatteryDate_Type.__name__=_Q
_CpqSiSysBatteryDate_Object=MibTableColumn
cpqSiSysBatteryDate=_CpqSiSysBatteryDate_Object((1,3,6,1,4,1,232,2,2,10,2,1,6),_CpqSiSysBatteryDate_Type())
cpqSiSysBatteryDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryDate.setStatus(_B)
class _CpqSiSysBatterySmartVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysBatterySmartVersion_Type.__name__=_E
_CpqSiSysBatterySmartVersion_Object=MibTableColumn
cpqSiSysBatterySmartVersion=_CpqSiSysBatterySmartVersion_Object((1,3,6,1,4,1,232,2,2,10,2,1,7),_CpqSiSysBatterySmartVersion_Type())
cpqSiSysBatterySmartVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatterySmartVersion.setStatus(_B)
class _CpqSiSysBatteryCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiSysBatteryCondition_Type.__name__=_C
_CpqSiSysBatteryCondition_Object=MibTableColumn
cpqSiSysBatteryCondition=_CpqSiSysBatteryCondition_Object((1,3,6,1,4,1,232,2,2,10,2,1,8),_CpqSiSysBatteryCondition_Type())
cpqSiSysBatteryCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryCondition.setStatus(_B)
class _CpqSiSysBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_M,2),('capacityDegraded',3),('chargeFault',4),('batteryFailure',5)))
_CpqSiSysBatteryStatus_Type.__name__=_C
_CpqSiSysBatteryStatus_Object=MibTableColumn
cpqSiSysBatteryStatus=_CpqSiSysBatteryStatus_Object((1,3,6,1,4,1,232,2,2,10,2,1,9),_CpqSiSysBatteryStatus_Type())
cpqSiSysBatteryStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryStatus.setStatus(_B)
class _CpqSiSysBatteryChemistry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),(_R,2),('lead-Acid',3),('nickel-Cadmium',4),('nickel-Metal-Hydride',5),('lithium-Ion',6),('zinc-Air',7),('lithium-Polymer',8)))
_CpqSiSysBatteryChemistry_Type.__name__=_C
_CpqSiSysBatteryChemistry_Object=MibTableColumn
cpqSiSysBatteryChemistry=_CpqSiSysBatteryChemistry_Object((1,3,6,1,4,1,232,2,2,10,2,1,10),_CpqSiSysBatteryChemistry_Type())
cpqSiSysBatteryChemistry.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryChemistry.setStatus(_B)
class _CpqSiSysBatteryRemainingCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiSysBatteryRemainingCap_Type.__name__=_C
_CpqSiSysBatteryRemainingCap_Object=MibTableColumn
cpqSiSysBatteryRemainingCap=_CpqSiSysBatteryRemainingCap_Object((1,3,6,1,4,1,232,2,2,10,2,1,11),_CpqSiSysBatteryRemainingCap_Type())
cpqSiSysBatteryRemainingCap.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryRemainingCap.setStatus(_B)
class _CpqSiSysBatteryFirmwareRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiSysBatteryFirmwareRevision_Type.__name__=_C
_CpqSiSysBatteryFirmwareRevision_Object=MibTableColumn
cpqSiSysBatteryFirmwareRevision=_CpqSiSysBatteryFirmwareRevision_Object((1,3,6,1,4,1,232,2,2,10,2,1,12),_CpqSiSysBatteryFirmwareRevision_Type())
cpqSiSysBatteryFirmwareRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryFirmwareRevision.setStatus(_B)
class _CpqSiSysBatteryHardwareRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSiSysBatteryHardwareRevision_Type.__name__=_C
_CpqSiSysBatteryHardwareRevision_Object=MibTableColumn
cpqSiSysBatteryHardwareRevision=_CpqSiSysBatteryHardwareRevision_Object((1,3,6,1,4,1,232,2,2,10,2,1,13),_CpqSiSysBatteryHardwareRevision_Type())
cpqSiSysBatteryHardwareRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryHardwareRevision.setStatus(_B)
class _CpqSiSysBatteryFullCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiSysBatteryFullCap_Type.__name__=_C
_CpqSiSysBatteryFullCap_Object=MibTableColumn
cpqSiSysBatteryFullCap=_CpqSiSysBatteryFullCap_Object((1,3,6,1,4,1,232,2,2,10,2,1,14),_CpqSiSysBatteryFullCap_Type())
cpqSiSysBatteryFullCap.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryFullCap.setStatus(_B)
class _CpqSiSysBatteryDesignCap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSiSysBatteryDesignCap_Type.__name__=_C
_CpqSiSysBatteryDesignCap_Object=MibTableColumn
cpqSiSysBatteryDesignCap=_CpqSiSysBatteryDesignCap_Object((1,3,6,1,4,1,232,2,2,10,2,1,15),_CpqSiSysBatteryDesignCap_Type())
cpqSiSysBatteryDesignCap.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryDesignCap.setStatus(_B)
class _CpqSiSysBatteryHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiSysBatteryHwLocation_Type.__name__=_E
_CpqSiSysBatteryHwLocation_Object=MibTableColumn
cpqSiSysBatteryHwLocation=_CpqSiSysBatteryHwLocation_Object((1,3,6,1,4,1,232,2,2,10,2,1,16),_CpqSiSysBatteryHwLocation_Type())
cpqSiSysBatteryHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiSysBatteryHwLocation.setStatus(_D)
_CpqSiDockingStation_ObjectIdentity=ObjectIdentity
cpqSiDockingStation=_CpqSiDockingStation_ObjectIdentity((1,3,6,1,4,1,232,2,2,11))
class _CpqSiDockingStationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('docked',2),('undocked',3)))
_CpqSiDockingStationStatus_Type.__name__=_C
_CpqSiDockingStationStatus_Object=MibScalar
cpqSiDockingStationStatus=_CpqSiDockingStationStatus_Object((1,3,6,1,4,1,232,2,2,11,1),_CpqSiDockingStationStatus_Type())
cpqSiDockingStationStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiDockingStationStatus.setStatus(_B)
class _CpqSiDockingStationSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiDockingStationSerialNum_Type.__name__=_E
_CpqSiDockingStationSerialNum_Object=MibScalar
cpqSiDockingStationSerialNum=_CpqSiDockingStationSerialNum_Object((1,3,6,1,4,1,232,2,2,11,2),_CpqSiDockingStationSerialNum_Type())
cpqSiDockingStationSerialNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiDockingStationSerialNum.setStatus(_B)
class _CpqSiDockingStationModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiDockingStationModel_Type.__name__=_E
_CpqSiDockingStationModel_Object=MibScalar
cpqSiDockingStationModel=_CpqSiDockingStationModel_Object((1,3,6,1,4,1,232,2,2,11,3),_CpqSiDockingStationModel_Type())
cpqSiDockingStationModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiDockingStationModel.setStatus(_B)
class _CpqSiDockingStationAssetTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiDockingStationAssetTag_Type.__name__=_E
_CpqSiDockingStationAssetTag_Object=MibScalar
cpqSiDockingStationAssetTag=_CpqSiDockingStationAssetTag_Object((1,3,6,1,4,1,232,2,2,11,4),_CpqSiDockingStationAssetTag_Type())
cpqSiDockingStationAssetTag.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiDockingStationAssetTag.setStatus(_B)
_CpqSiFru_ObjectIdentity=ObjectIdentity
cpqSiFru=_CpqSiFru_ObjectIdentity((1,3,6,1,4,1,232,2,2,12))
_CpqSiFruTable_Object=MibTable
cpqSiFruTable=_CpqSiFruTable_Object((1,3,6,1,4,1,232,2,2,12,1))
if mibBuilder.loadTexts:cpqSiFruTable.setStatus(_B)
_CpqSiFruEntry_Object=MibTableRow
cpqSiFruEntry=_CpqSiFruEntry_Object((1,3,6,1,4,1,232,2,2,12,1,1))
cpqSiFruEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:cpqSiFruEntry.setStatus(_B)
_CpqSiFruIndex_Type=Integer32
_CpqSiFruIndex_Object=MibTableColumn
cpqSiFruIndex=_CpqSiFruIndex_Object((1,3,6,1,4,1,232,2,2,12,1,1,1),_CpqSiFruIndex_Type())
cpqSiFruIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruIndex.setStatus(_B)
class _CpqSiFruType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_R,1),(_F,2),('motherBoard',3),('processor',4),('memoryCard',5),('memoryModule',6),('peripheralDevice',7),('systemBusBridge',8),('powerSupply',9),('chassis',10),('fan',11),('ioCard',12)))
_CpqSiFruType_Type.__name__=_C
_CpqSiFruType_Object=MibTableColumn
cpqSiFruType=_CpqSiFruType_Object((1,3,6,1,4,1,232,2,2,12,1,1,2),_CpqSiFruType_Type())
cpqSiFruType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruType.setStatus(_B)
_CpqSiFruDescr_Type=DisplayString
_CpqSiFruDescr_Object=MibTableColumn
cpqSiFruDescr=_CpqSiFruDescr_Object((1,3,6,1,4,1,232,2,2,12,1,1,3),_CpqSiFruDescr_Type())
cpqSiFruDescr.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiFruDescr.setStatus(_B)
_CpqSiFruVendor_Type=DisplayString
_CpqSiFruVendor_Object=MibTableColumn
cpqSiFruVendor=_CpqSiFruVendor_Object((1,3,6,1,4,1,232,2,2,12,1,1,4),_CpqSiFruVendor_Type())
cpqSiFruVendor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruVendor.setStatus(_B)
_CpqSiFruPartNumber_Type=DisplayString
_CpqSiFruPartNumber_Object=MibTableColumn
cpqSiFruPartNumber=_CpqSiFruPartNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,5),_CpqSiFruPartNumber_Type())
cpqSiFruPartNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruPartNumber.setStatus(_B)
_CpqSiFruRevision_Type=DisplayString
_CpqSiFruRevision_Object=MibTableColumn
cpqSiFruRevision=_CpqSiFruRevision_Object((1,3,6,1,4,1,232,2,2,12,1,1,6),_CpqSiFruRevision_Type())
cpqSiFruRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruRevision.setStatus(_B)
_CpqSiFruFirmwareRevision_Type=DisplayString
_CpqSiFruFirmwareRevision_Object=MibTableColumn
cpqSiFruFirmwareRevision=_CpqSiFruFirmwareRevision_Object((1,3,6,1,4,1,232,2,2,12,1,1,7),_CpqSiFruFirmwareRevision_Type())
cpqSiFruFirmwareRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruFirmwareRevision.setStatus(_B)
_CpqSiFruSerialNumber_Type=DisplayString
_CpqSiFruSerialNumber_Object=MibTableColumn
cpqSiFruSerialNumber=_CpqSiFruSerialNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,8),_CpqSiFruSerialNumber_Type())
cpqSiFruSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruSerialNumber.setStatus(_B)
_CpqSiFruAssetNo_Type=DisplayString
_CpqSiFruAssetNo_Object=MibTableColumn
cpqSiFruAssetNo=_CpqSiFruAssetNo_Object((1,3,6,1,4,1,232,2,2,12,1,1,9),_CpqSiFruAssetNo_Type())
cpqSiFruAssetNo.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSiFruAssetNo.setStatus(_B)
class _CpqSiFruClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_R,1),(_F,2),('currentBoardInSlot',3),('priorBoardInSlot',4),('parentBoard',5),('priorParentBoard',6),('priorParentSystem',7)))
_CpqSiFruClass_Type.__name__=_C
_CpqSiFruClass_Object=MibTableColumn
cpqSiFruClass=_CpqSiFruClass_Object((1,3,6,1,4,1,232,2,2,12,1,1,10),_CpqSiFruClass_Type())
cpqSiFruClass.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruClass.setStatus(_B)
_CpqSiFruSlotNumber_Type=DisplayString
_CpqSiFruSlotNumber_Object=MibTableColumn
cpqSiFruSlotNumber=_CpqSiFruSlotNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,11),_CpqSiFruSlotNumber_Type())
cpqSiFruSlotNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruSlotNumber.setStatus(_B)
_CpqSiFruSubAssemblyNumber_Type=Integer32
_CpqSiFruSubAssemblyNumber_Object=MibTableColumn
cpqSiFruSubAssemblyNumber=_CpqSiFruSubAssemblyNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,12),_CpqSiFruSubAssemblyNumber_Type())
cpqSiFruSubAssemblyNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruSubAssemblyNumber.setStatus(_B)
_CpqSiFruAssemblyNumber_Type=Integer32
_CpqSiFruAssemblyNumber_Object=MibTableColumn
cpqSiFruAssemblyNumber=_CpqSiFruAssemblyNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,13),_CpqSiFruAssemblyNumber_Type())
cpqSiFruAssemblyNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruAssemblyNumber.setStatus(_B)
_CpqSiFruChassisNumber_Type=Integer32
_CpqSiFruChassisNumber_Object=MibTableColumn
cpqSiFruChassisNumber=_CpqSiFruChassisNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,14),_CpqSiFruChassisNumber_Type())
cpqSiFruChassisNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruChassisNumber.setStatus(_B)
_CpqSiFruPositionNumber_Type=Integer32
_CpqSiFruPositionNumber_Object=MibTableColumn
cpqSiFruPositionNumber=_CpqSiFruPositionNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,15),_CpqSiFruPositionNumber_Type())
cpqSiFruPositionNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruPositionNumber.setStatus(_B)
_CpqSiFruCabinetIDNumber_Type=Integer32
_CpqSiFruCabinetIDNumber_Object=MibTableColumn
cpqSiFruCabinetIDNumber=_CpqSiFruCabinetIDNumber_Object((1,3,6,1,4,1,232,2,2,12,1,1,16),_CpqSiFruCabinetIDNumber_Type())
cpqSiFruCabinetIDNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruCabinetIDNumber.setStatus(_B)
_CpqSiFruSiteLocation_Type=Integer32
_CpqSiFruSiteLocation_Object=MibTableColumn
cpqSiFruSiteLocation=_CpqSiFruSiteLocation_Object((1,3,6,1,4,1,232,2,2,12,1,1,17),_CpqSiFruSiteLocation_Type())
cpqSiFruSiteLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruSiteLocation.setStatus(_B)
class _CpqSiFruDiagStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_M,2),(_P,3),(_S,4),(_N,5)))
_CpqSiFruDiagStatus_Type.__name__=_C
_CpqSiFruDiagStatus_Object=MibTableColumn
cpqSiFruDiagStatus=_CpqSiFruDiagStatus_Object((1,3,6,1,4,1,232,2,2,12,1,1,18),_CpqSiFruDiagStatus_Type())
cpqSiFruDiagStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruDiagStatus.setStatus(_B)
_CpqSiFruExtendedDiagStatus_Type=Integer32
_CpqSiFruExtendedDiagStatus_Object=MibTableColumn
cpqSiFruExtendedDiagStatus=_CpqSiFruExtendedDiagStatus_Object((1,3,6,1,4,1,232,2,2,12,1,1,19),_CpqSiFruExtendedDiagStatus_Type())
cpqSiFruExtendedDiagStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruExtendedDiagStatus.setStatus(_B)
_CpqSiFruCellTablePtr_Type=Integer32
_CpqSiFruCellTablePtr_Object=MibTableColumn
cpqSiFruCellTablePtr=_CpqSiFruCellTablePtr_Object((1,3,6,1,4,1,232,2,2,12,1,1,20),_CpqSiFruCellTablePtr_Type())
cpqSiFruCellTablePtr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruCellTablePtr.setStatus(_D)
_CpqSiFruIOCTablePtr_Type=Integer32
_CpqSiFruIOCTablePtr_Object=MibTableColumn
cpqSiFruIOCTablePtr=_CpqSiFruIOCTablePtr_Object((1,3,6,1,4,1,232,2,2,12,1,1,21),_CpqSiFruIOCTablePtr_Type())
cpqSiFruIOCTablePtr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruIOCTablePtr.setStatus(_D)
class _CpqSiFruFileId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiFruFileId_Type.__name__=_E
_CpqSiFruFileId_Object=MibTableColumn
cpqSiFruFileId=_CpqSiFruFileId_Object((1,3,6,1,4,1,232,2,2,12,1,1,22),_CpqSiFruFileId_Type())
cpqSiFruFileId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruFileId.setStatus(_D)
class _CpqSiFruScanRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSiFruScanRev_Type.__name__=_E
_CpqSiFruScanRev_Object=MibTableColumn
cpqSiFruScanRev=_CpqSiFruScanRev_Object((1,3,6,1,4,1,232,2,2,12,1,1,23),_CpqSiFruScanRev_Type())
cpqSiFruScanRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiFruScanRev.setStatus(_D)
_CpqSiRackEnclosure_ObjectIdentity=ObjectIdentity
cpqSiRackEnclosure=_CpqSiRackEnclosure_ObjectIdentity((1,3,6,1,4,1,232,2,2,13))
_CpqSiRackEnclosureMgrTable_Object=MibTable
cpqSiRackEnclosureMgrTable=_CpqSiRackEnclosureMgrTable_Object((1,3,6,1,4,1,232,2,2,13,1))
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrTable.setStatus(_B)
_CpqSiRackEnclosureMgrEntry_Object=MibTableRow
cpqSiRackEnclosureMgrEntry=_CpqSiRackEnclosureMgrEntry_Object((1,3,6,1,4,1,232,2,2,13,1,1))
cpqSiRackEnclosureMgrEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrEntry.setStatus(_B)
_CpqSiRackEnclosureMgrIndex_Type=Integer32
_CpqSiRackEnclosureMgrIndex_Object=MibTableColumn
cpqSiRackEnclosureMgrIndex=_CpqSiRackEnclosureMgrIndex_Object((1,3,6,1,4,1,232,2,2,13,1,1,1),_CpqSiRackEnclosureMgrIndex_Type())
cpqSiRackEnclosureMgrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrIndex.setStatus(_B)
class _CpqSiRackEnclosureMgrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('noEnclosureManagement',2),('enclosureManagement',3),('onboardAdminManagement',4),('multiboardchassis',5)))
_CpqSiRackEnclosureMgrType_Type.__name__=_C
_CpqSiRackEnclosureMgrType_Object=MibTableColumn
cpqSiRackEnclosureMgrType=_CpqSiRackEnclosureMgrType_Object((1,3,6,1,4,1,232,2,2,13,1,1,2),_CpqSiRackEnclosureMgrType_Type())
cpqSiRackEnclosureMgrType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrType.setStatus(_B)
_CpqSiRackEnclosureMgrIpAddr_Type=DisplayString
_CpqSiRackEnclosureMgrIpAddr_Object=MibTableColumn
cpqSiRackEnclosureMgrIpAddr=_CpqSiRackEnclosureMgrIpAddr_Object((1,3,6,1,4,1,232,2,2,13,1,1,3),_CpqSiRackEnclosureMgrIpAddr_Type())
cpqSiRackEnclosureMgrIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrIpAddr.setStatus(_B)
_CpqSiRackEnclosureMgrWebLink_Type=DisplayString
_CpqSiRackEnclosureMgrWebLink_Object=MibTableColumn
cpqSiRackEnclosureMgrWebLink=_CpqSiRackEnclosureMgrWebLink_Object((1,3,6,1,4,1,232,2,2,13,1,1,4),_CpqSiRackEnclosureMgrWebLink_Type())
cpqSiRackEnclosureMgrWebLink.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrWebLink.setStatus(_B)
class _CpqSiRackEnclosureMgrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_P,3),(_S,4)))
_CpqSiRackEnclosureMgrCondition_Type.__name__=_C
_CpqSiRackEnclosureMgrCondition_Object=MibTableColumn
cpqSiRackEnclosureMgrCondition=_CpqSiRackEnclosureMgrCondition_Object((1,3,6,1,4,1,232,2,2,13,1,1,5),_CpqSiRackEnclosureMgrCondition_Type())
cpqSiRackEnclosureMgrCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrCondition.setStatus(_B)
_CpqSiRackEnclosureMgrSerialNumber_Type=DisplayString
_CpqSiRackEnclosureMgrSerialNumber_Object=MibTableColumn
cpqSiRackEnclosureMgrSerialNumber=_CpqSiRackEnclosureMgrSerialNumber_Object((1,3,6,1,4,1,232,2,2,13,1,1,6),_CpqSiRackEnclosureMgrSerialNumber_Type())
cpqSiRackEnclosureMgrSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrSerialNumber.setStatus(_B)
_CpqSiRackEnclosureMgrModel_Type=DisplayString
_CpqSiRackEnclosureMgrModel_Object=MibTableColumn
cpqSiRackEnclosureMgrModel=_CpqSiRackEnclosureMgrModel_Object((1,3,6,1,4,1,232,2,2,13,1,1,7),_CpqSiRackEnclosureMgrModel_Type())
cpqSiRackEnclosureMgrModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrModel.setStatus(_D)
_CpqSiRackEnclosureMgrName_Type=DisplayString
_CpqSiRackEnclosureMgrName_Object=MibTableColumn
cpqSiRackEnclosureMgrName=_CpqSiRackEnclosureMgrName_Object((1,3,6,1,4,1,232,2,2,13,1,1,8),_CpqSiRackEnclosureMgrName_Type())
cpqSiRackEnclosureMgrName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrName.setStatus(_D)
_CpqSiRackEnclosureMgrFwRev_Type=DisplayString
_CpqSiRackEnclosureMgrFwRev_Object=MibTableColumn
cpqSiRackEnclosureMgrFwRev=_CpqSiRackEnclosureMgrFwRev_Object((1,3,6,1,4,1,232,2,2,13,1,1,9),_CpqSiRackEnclosureMgrFwRev_Type())
cpqSiRackEnclosureMgrFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrFwRev.setStatus(_D)
_CpqSiRackEnclosureMgrProductID_Type=DisplayString
_CpqSiRackEnclosureMgrProductID_Object=MibTableColumn
cpqSiRackEnclosureMgrProductID=_CpqSiRackEnclosureMgrProductID_Object((1,3,6,1,4,1,232,2,2,13,1,1,10),_CpqSiRackEnclosureMgrProductID_Type())
cpqSiRackEnclosureMgrProductID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrProductID.setStatus(_D)
_CpqSiRackEnclosureMgrUUID_Type=DisplayString
_CpqSiRackEnclosureMgrUUID_Object=MibTableColumn
cpqSiRackEnclosureMgrUUID=_CpqSiRackEnclosureMgrUUID_Object((1,3,6,1,4,1,232,2,2,13,1,1,11),_CpqSiRackEnclosureMgrUUID_Type())
cpqSiRackEnclosureMgrUUID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrUUID.setStatus(_D)
_CpqSiRackEnclosureMgrMatrix_Type=Integer32
_CpqSiRackEnclosureMgrMatrix_Object=MibTableColumn
cpqSiRackEnclosureMgrMatrix=_CpqSiRackEnclosureMgrMatrix_Object((1,3,6,1,4,1,232,2,2,13,1,1,12),_CpqSiRackEnclosureMgrMatrix_Type())
cpqSiRackEnclosureMgrMatrix.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrMatrix.setStatus(_B)
_CpqSiRackEnclosureMgrMatrixID_Type=DisplayString
_CpqSiRackEnclosureMgrMatrixID_Object=MibTableColumn
cpqSiRackEnclosureMgrMatrixID=_CpqSiRackEnclosureMgrMatrixID_Object((1,3,6,1,4,1,232,2,2,13,1,1,13),_CpqSiRackEnclosureMgrMatrixID_Type())
cpqSiRackEnclosureMgrMatrixID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackEnclosureMgrMatrixID.setStatus(_D)
_CpqSiServerBlade_ObjectIdentity=ObjectIdentity
cpqSiServerBlade=_CpqSiServerBlade_ObjectIdentity((1,3,6,1,4,1,232,2,2,14))
_CpqSiServerBladeEnclosureBayNumber_Type=Integer32
_CpqSiServerBladeEnclosureBayNumber_Object=MibScalar
cpqSiServerBladeEnclosureBayNumber=_CpqSiServerBladeEnclosureBayNumber_Object((1,3,6,1,4,1,232,2,2,14,1),_CpqSiServerBladeEnclosureBayNumber_Type())
cpqSiServerBladeEnclosureBayNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiServerBladeEnclosureBayNumber.setStatus(_D)
class _CpqSiServerBladeHeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('halfHeightBlade',2),('fullHeightBlade',3)))
_CpqSiServerBladeHeight_Type.__name__=_C
_CpqSiServerBladeHeight_Object=MibScalar
cpqSiServerBladeHeight=_CpqSiServerBladeHeight_Object((1,3,6,1,4,1,232,2,2,14,2),_CpqSiServerBladeHeight_Type())
cpqSiServerBladeHeight.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiServerBladeHeight.setStatus(_D)
class _CpqSiServerBladeWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('singleWide',2),('doubleWide',3)))
_CpqSiServerBladeWidth_Type.__name__=_C
_CpqSiServerBladeWidth_Object=MibScalar
cpqSiServerBladeWidth=_CpqSiServerBladeWidth_Object((1,3,6,1,4,1,232,2,2,14,3),_CpqSiServerBladeWidth_Type())
cpqSiServerBladeWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiServerBladeWidth.setStatus(_D)
_CpqSiRack_ObjectIdentity=ObjectIdentity
cpqSiRack=_CpqSiRack_ObjectIdentity((1,3,6,1,4,1,232,2,2,15))
_CpqSiRackName_Type=DisplayString
_CpqSiRackName_Object=MibScalar
cpqSiRackName=_CpqSiRackName_Object((1,3,6,1,4,1,232,2,2,15,1),_CpqSiRackName_Type())
cpqSiRackName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackName.setStatus(_D)
_CpqSiRackUUID_Type=DisplayString
_CpqSiRackUUID_Object=MibScalar
cpqSiRackUUID=_CpqSiRackUUID_Object((1,3,6,1,4,1,232,2,2,15,2),_CpqSiRackUUID_Type())
cpqSiRackUUID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiRackUUID.setStatus(_D)
_CpqSiMP_ObjectIdentity=ObjectIdentity
cpqSiMP=_CpqSiMP_ObjectIdentity((1,3,6,1,4,1,232,2,2,16))
_CpqSiMPHostName_Type=DisplayString
_CpqSiMPHostName_Object=MibScalar
cpqSiMPHostName=_CpqSiMPHostName_Object((1,3,6,1,4,1,232,2,2,16,1),_CpqSiMPHostName_Type())
cpqSiMPHostName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMPHostName.setStatus(_D)
class _CpqSiMPHealthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_M,2),(_P,3),(_S,4)))
_CpqSiMPHealthStatus_Type.__name__=_C
_CpqSiMPHealthStatus_Object=MibScalar
cpqSiMPHealthStatus=_CpqSiMPHealthStatus_Object((1,3,6,1,4,1,232,2,2,16,2),_CpqSiMPHealthStatus_Type())
cpqSiMPHealthStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSiMPHealthStatus.setStatus(_D)
cpqSiHoodRemoved=NotificationType((1,3,6,1,4,1,232,0,2001))
cpqSiHoodRemoved.setObjects(*((_J,_K),(_H,_I)))
if mibBuilder.loadTexts:cpqSiHoodRemoved.setStatus('')
cpqSiMonitorConditionOK=NotificationType((1,3,6,1,4,1,232,0,2002))
cpqSiMonitorConditionOK.setObjects(*((_J,_K),(_H,_I),(_G,_U)))
if mibBuilder.loadTexts:cpqSiMonitorConditionOK.setStatus('')
cpqSiMonitorConditionDegraded=NotificationType((1,3,6,1,4,1,232,0,2003))
cpqSiMonitorConditionDegraded.setObjects(*((_J,_K),(_H,_I),(_G,_U)))
if mibBuilder.loadTexts:cpqSiMonitorConditionDegraded.setStatus('')
cpqSiMonitorConditionFailed=NotificationType((1,3,6,1,4,1,232,0,2004))
cpqSiMonitorConditionFailed.setObjects(*((_J,_K),(_H,_I),(_G,_U)))
if mibBuilder.loadTexts:cpqSiMonitorConditionFailed.setStatus('')
cpqSiCorrMemErrStatusDegraded=NotificationType((1,3,6,1,4,1,232,0,2005))
cpqSiCorrMemErrStatusDegraded.setObjects(*((_J,_K),(_H,_I),(_G,_a)))
if mibBuilder.loadTexts:cpqSiCorrMemErrStatusDegraded.setStatus('')
cpqSiCorrMemErrStatusOk=NotificationType((1,3,6,1,4,1,232,0,2006))
cpqSiCorrMemErrStatusOk.setObjects(*((_J,_K),(_H,_I),(_G,_a)))
if mibBuilder.loadTexts:cpqSiCorrMemErrStatusOk.setStatus('')
cpqSiMemConfigChange=NotificationType((1,3,6,1,4,1,232,0,2007))
cpqSiMemConfigChange.setObjects(*((_J,_K),(_H,_I),(_G,_q)))
if mibBuilder.loadTexts:cpqSiMemConfigChange.setStatus('')
cpqSiHotPlugSlotBoardRemoved=NotificationType((1,3,6,1,4,1,232,0,2008))
cpqSiHotPlugSlotBoardRemoved.setObjects(*((_J,_K),(_H,_I),(_G,_V),(_G,_W)))
if mibBuilder.loadTexts:cpqSiHotPlugSlotBoardRemoved.setStatus('')
cpqSiHotPlugSlotBoardInserted=NotificationType((1,3,6,1,4,1,232,0,2009))
cpqSiHotPlugSlotBoardInserted.setObjects(*((_J,_K),(_H,_I),(_G,_V),(_G,_W)))
if mibBuilder.loadTexts:cpqSiHotPlugSlotBoardInserted.setStatus('')
cpqSiHotPlugSlotPowerUpFailed=NotificationType((1,3,6,1,4,1,232,0,2010))
cpqSiHotPlugSlotPowerUpFailed.setObjects(*((_J,_K),(_H,_I),(_G,_V),(_G,_W),(_G,_r)))
if mibBuilder.loadTexts:cpqSiHotPlugSlotPowerUpFailed.setStatus('')
cpqSiSysBatteryFailure=NotificationType((1,3,6,1,4,1,232,0,2011))
cpqSiSysBatteryFailure.setObjects(*((_J,_K),(_H,_I),(_G,_X),(_G,_Y)))
if mibBuilder.loadTexts:cpqSiSysBatteryFailure.setStatus('')
cpqSiSysBatteryChargingDegraded=NotificationType((1,3,6,1,4,1,232,0,2012))
cpqSiSysBatteryChargingDegraded.setObjects(*((_J,_K),(_H,_I),(_G,_X),(_G,_Y)))
if mibBuilder.loadTexts:cpqSiSysBatteryChargingDegraded.setStatus('')
cpqSiSysBatteryCalibrationError=NotificationType((1,3,6,1,4,1,232,0,2013))
cpqSiSysBatteryCalibrationError.setObjects(*((_J,_K),(_H,_I),(_G,_X),(_G,_Y)))
if mibBuilder.loadTexts:cpqSiSysBatteryCalibrationError.setStatus('')
cpqSiIntrusionInstalled=NotificationType((1,3,6,1,4,1,232,0,2014))
cpqSiIntrusionInstalled.setObjects(*((_J,_K),(_H,_I)))
if mibBuilder.loadTexts:cpqSiIntrusionInstalled.setStatus('')
cpqSiIntrusionRemoved=NotificationType((1,3,6,1,4,1,232,0,2015))
cpqSiIntrusionRemoved.setObjects(*((_J,_K),(_H,_I)))
if mibBuilder.loadTexts:cpqSiIntrusionRemoved.setStatus('')
cpqSiHoodReplaced=NotificationType((1,3,6,1,4,1,232,0,2016))
cpqSiHoodReplaced.setObjects(*((_J,_K),(_H,_I)))
if mibBuilder.loadTexts:cpqSiHoodReplaced.setStatus('')
cpqSiHoodRemovedOnPowerOff=NotificationType((1,3,6,1,4,1,232,0,2017))
cpqSiHoodRemovedOnPowerOff.setObjects(*((_J,_K),(_H,_I)))
if mibBuilder.loadTexts:cpqSiHoodRemovedOnPowerOff.setStatus('')
cpqSiSysTelemetryThresholdAlert=NotificationType((1,3,6,1,4,1,232,0,2018))
cpqSiSysTelemetryThresholdAlert.setObjects(*((_J,_K),(_H,_I),(_G,_s),(_G,_t)))
if mibBuilder.loadTexts:cpqSiSysTelemetryThresholdAlert.setStatus('')
mibBuilder.exportSymbols(_G,**{'cpqSiHoodRemoved':cpqSiHoodRemoved,'cpqSiMonitorConditionOK':cpqSiMonitorConditionOK,'cpqSiMonitorConditionDegraded':cpqSiMonitorConditionDegraded,'cpqSiMonitorConditionFailed':cpqSiMonitorConditionFailed,'cpqSiCorrMemErrStatusDegraded':cpqSiCorrMemErrStatusDegraded,'cpqSiCorrMemErrStatusOk':cpqSiCorrMemErrStatusOk,'cpqSiMemConfigChange':cpqSiMemConfigChange,'cpqSiHotPlugSlotBoardRemoved':cpqSiHotPlugSlotBoardRemoved,'cpqSiHotPlugSlotBoardInserted':cpqSiHotPlugSlotBoardInserted,'cpqSiHotPlugSlotPowerUpFailed':cpqSiHotPlugSlotPowerUpFailed,'cpqSiSysBatteryFailure':cpqSiSysBatteryFailure,'cpqSiSysBatteryChargingDegraded':cpqSiSysBatteryChargingDegraded,'cpqSiSysBatteryCalibrationError':cpqSiSysBatteryCalibrationError,'cpqSiIntrusionInstalled':cpqSiIntrusionInstalled,'cpqSiIntrusionRemoved':cpqSiIntrusionRemoved,'cpqSiHoodReplaced':cpqSiHoodReplaced,'cpqSiHoodRemovedOnPowerOff':cpqSiHoodRemovedOnPowerOff,'cpqSiSysTelemetryThresholdAlert':cpqSiSysTelemetryThresholdAlert,'cpqSystemInfo':cpqSystemInfo,'cpqSiMibRev':cpqSiMibRev,'cpqSiMibRevMajor':cpqSiMibRevMajor,'cpqSiMibRevMinor':cpqSiMibRevMinor,'cpqSiMibCondition':cpqSiMibCondition,'cpqSiComponent':cpqSiComponent,'cpqSiInterface':cpqSiInterface,'cpqSiOsCommon':cpqSiOsCommon,'cpqSiOsCommonPollFreq':cpqSiOsCommonPollFreq,'cpqSiOsCommonModuleTable':cpqSiOsCommonModuleTable,'cpqSiOsCommonModuleEntry':cpqSiOsCommonModuleEntry,_c:cpqSiOsCommonModuleIndex,'cpqSiOsCommonModuleName':cpqSiOsCommonModuleName,'cpqSiOsCommonModuleVersion':cpqSiOsCommonModuleVersion,'cpqSiOsCommonModuleDate':cpqSiOsCommonModuleDate,'cpqSiOsCommonModulePurpose':cpqSiOsCommonModulePurpose,'cpqSiAsset':cpqSiAsset,'cpqSiSysSerialNum':cpqSiSysSerialNum,'cpqSiFormFactor':cpqSiFormFactor,'cpqSiAssetTag':cpqSiAssetTag,'cpqSiOwnershipTag':cpqSiOwnershipTag,'cpqSiSysServiceNum':cpqSiSysServiceNum,'cpqSiSysProductId':cpqSiSysProductId,'cpqSiAssetTagMaxLength':cpqSiAssetTagMaxLength,'cpqSiVirtualSystemTable':cpqSiVirtualSystemTable,'cpqSiVirtualSystemEntry':cpqSiVirtualSystemEntry,_d:cpqSiVirtualSystemIndex,'cpqSiVirtualSystemSerialNumber':cpqSiVirtualSystemSerialNumber,'cpqSiVirtualSystemUUID':cpqSiVirtualSystemUUID,'cpqSiSecurity':cpqSiSecurity,'cpqSiPowerOnPassword':cpqSiPowerOnPassword,'cpqSiNetServerMode':cpqSiNetServerMode,'cpqSiQuickLockPassword':cpqSiQuickLockPassword,'cpqSiQuickBlank':cpqSiQuickBlank,'cpqSiDisketteBootControl':cpqSiDisketteBootControl,'cpqSiSerialPortAControl':cpqSiSerialPortAControl,'cpqSiSerialPortBControl':cpqSiSerialPortBControl,'cpqSiParallelPortControl':cpqSiParallelPortControl,'cpqSiFloppyDiskControl':cpqSiFloppyDiskControl,'cpqSiFixedDiskControl':cpqSiFixedDiskControl,'cpqSiHoodRemovedTime':cpqSiHoodRemovedTime,'cpqSiHoodSensorConfiguration':cpqSiHoodSensorConfiguration,'cpqSiSmartCoverLockStatus':cpqSiSmartCoverLockStatus,'cpqSiUSBPortControl':cpqSiUSBPortControl,'cpqSiVirtualSerialPortControl':cpqSiVirtualSerialPortControl,'cpqSiChassisHoodStatus':cpqSiChassisHoodStatus,'cpqSiSystemBoard':cpqSiSystemBoard,'cpqSiProductId':cpqSiProductId,'cpqSiProductName':cpqSiProductName,'cpqSiAuxiliaryInput':cpqSiAuxiliaryInput,'cpqSiMemModuleTable':cpqSiMemModuleTable,'cpqSiMemModuleEntry':cpqSiMemModuleEntry,_e:cpqSiMemBoardIndex,_f:cpqSiMemModuleIndex,'cpqSiMemModuleSize':cpqSiMemModuleSize,'cpqSiMemModuleType':cpqSiMemModuleType,'cpqSiMemModuleSpeed':cpqSiMemModuleSpeed,'cpqSiMemModuleTechnology':cpqSiMemModuleTechnology,'cpqSiMemModuleManufacturer':cpqSiMemModuleManufacturer,'cpqSiMemModulePartNo':cpqSiMemModulePartNo,'cpqSiMemModuleDate':cpqSiMemModuleDate,'cpqSiMemModuleSerialNo':cpqSiMemModuleSerialNo,'cpqSiMemModuleECCStatus':cpqSiMemModuleECCStatus,'cpqSiMemModuleHwLocation':cpqSiMemModuleHwLocation,'cpqSiMemModuleFrequency':cpqSiMemModuleFrequency,'cpqSiMemModuleCellTablePtr':cpqSiMemModuleCellTablePtr,'cpqSiMemModuleCellStatus':cpqSiMemModuleCellStatus,'cpqSiMemModulePartNoMfgr':cpqSiMemModulePartNoMfgr,'cpqSiMemModuleSerialNoMfgr':cpqSiMemModuleSerialNoMfgr,'cpqSiSystemId':cpqSiSystemId,'cpqSiSystemCpuId':cpqSiSystemCpuId,'cpqSiFlashRomSupport':cpqSiFlashRomSupport,'cpqSiQuickTestRomDate':cpqSiQuickTestRomDate,'cpqSiReboot':cpqSiReboot,'cpqSiProcMicroPatchTable':cpqSiProcMicroPatchTable,'cpqSiProcMicroPatchEntry':cpqSiProcMicroPatchEntry,_h:cpqSiProcMicroPatchIndex,'cpqSiProcMicroPatchId':cpqSiProcMicroPatchId,'cpqSiProcMicroPatchDate':cpqSiProcMicroPatchDate,'cpqSiProcMicroPatchFamily':cpqSiProcMicroPatchFamily,'cpqSiPowerMgmtStatus':cpqSiPowerMgmtStatus,'cpqSiRebootFlags':cpqSiRebootFlags,_a:cpqSiMemErrorIndex,'cpqSiMemECCCondition':cpqSiMemECCCondition,_q:cpqSiMemConfigChangeData,'cpqSiServerSystemId':cpqSiServerSystemId,'cpqSiPowerScheme':cpqSiPowerScheme,'cpqSiPowerSchemeName':cpqSiPowerSchemeName,'cpqSiCurrentPerformanceStatePointer':cpqSiCurrentPerformanceStatePointer,'cpqSiMinPerformanceState':cpqSiMinPerformanceState,'cpqSiMaxPerformanceState':cpqSiMaxPerformanceState,'cpqSiPerfStateTable':cpqSiPerfStateTable,'cpqSiPerfStateEntry':cpqSiPerfStateEntry,_i:cpqSiPerfStateIndex,'cpqSiPerfState':cpqSiPerfState,'cpqSiPerfStateCpuFrequency':cpqSiPerfStateCpuFrequency,'cpqSiPerfStateCpuPower':cpqSiPerfStateCpuPower,'cpqSiTPMmodule':cpqSiTPMmodule,'cpqSiTrustedModuleType':cpqSiTrustedModuleType,_s:cpqSiSystemTelemetryMetric,_t:cpqSiSystemTelemetryThresholdStatus,'cpqSiBoardRev':cpqSiBoardRev,'cpqSiCurRevDate':cpqSiCurRevDate,'cpqSiPrevRevDate':cpqSiPrevRevDate,'cpqSiBoardRevTable':cpqSiBoardRevTable,'cpqSiBoardRevEntry':cpqSiBoardRevEntry,_k:cpqSiBoardRevSlotIndex,_l:cpqSiBoardRevIndex,'cpqSiBoardRevId':cpqSiBoardRevId,'cpqSiBoardRevCur':cpqSiBoardRevCur,'cpqSiBoardRevPrev':cpqSiBoardRevPrev,'cpqSiBoardRevHwLocation':cpqSiBoardRevHwLocation,'cpqSiFirmwareRevTable':cpqSiFirmwareRevTable,'cpqSiFirmwareRevEntry':cpqSiFirmwareRevEntry,_m:cpqSiFirmwareRevIndex,'cpqSiFirmwareRevDesc':cpqSiFirmwareRevDesc,'cpqSiFirmwareRevString':cpqSiFirmwareRevString,'cpqSiFirmwareRevCellTablePtr':cpqSiFirmwareRevCellTablePtr,'cpqSiFirmwareLocation':cpqSiFirmwareLocation,'cpqSiFirmwareStatus':cpqSiFirmwareStatus,'cpqSiFirmwareCfgTable':cpqSiFirmwareCfgTable,'cpqSiFirmwareCfgEntry':cpqSiFirmwareCfgEntry,_n:cpqSiFirmwareCfgName,'cpqSiFirmwareCfgValue':cpqSiFirmwareCfgValue,'cpqSiRackServer':cpqSiRackServer,'cpqSiRackServerShutdownRole':cpqSiRackServerShutdownRole,'cpqSiRackServerMasterName':cpqSiRackServerMasterName,'cpqSiVideo':cpqSiVideo,'cpqSiVideoEdidRaw':cpqSiVideoEdidRaw,'cpqSiVideoDesc':cpqSiVideoDesc,'cpqSiVideoSerialNumber':cpqSiVideoSerialNumber,'cpqSiVideoManufactureDate':cpqSiVideoManufactureDate,'cpqSiVideoHeight':cpqSiVideoHeight,'cpqSiVideoWidth':cpqSiVideoWidth,'cpqSiVideoMaxHorPixel':cpqSiVideoMaxHorPixel,'cpqSiVideoMaxVertPixel':cpqSiVideoMaxVertPixel,'cpqSiVideoMaxRefreshRate':cpqSiVideoMaxRefreshRate,'cpqSiMonitor':cpqSiMonitor,'cpqSiMonitorOverallCondition':cpqSiMonitorOverallCondition,'cpqSiMonitorTable':cpqSiMonitorTable,'cpqSiMonitorEntry':cpqSiMonitorEntry,_U:cpqSiMonitorIndex,'cpqSiMonitorEdidRaw':cpqSiMonitorEdidRaw,'cpqSiMonitorDesc':cpqSiMonitorDesc,'cpqSiMonitorSerialNumber':cpqSiMonitorSerialNumber,'cpqSiMonitorManufactureDate':cpqSiMonitorManufactureDate,'cpqSiMonitorHeight':cpqSiMonitorHeight,'cpqSiMonitorWidth':cpqSiMonitorWidth,'cpqSiMonitorMaxHorPixel':cpqSiMonitorMaxHorPixel,'cpqSiMonitorMaxVertPixel':cpqSiMonitorMaxVertPixel,'cpqSiMonitorMaxRefreshRate':cpqSiMonitorMaxRefreshRate,'cpqSiMonitorManufacturer':cpqSiMonitorManufacturer,'cpqSiMonitorThermalCondition':cpqSiMonitorThermalCondition,'cpqSiMonitorOperationalCondition':cpqSiMonitorOperationalCondition,'cpqSiMonitorStatus':cpqSiMonitorStatus,'cpqSiHotPlugSlot':cpqSiHotPlugSlot,'cpqSiHotPlugSlotSupported':cpqSiHotPlugSlotSupported,'cpqSiHotPlugSlotCondition':cpqSiHotPlugSlotCondition,'cpqSiHotPlugSlotChangeCount':cpqSiHotPlugSlotChangeCount,'cpqSiHotPlugSlotTable':cpqSiHotPlugSlotTable,'cpqSiHotPlugSlotEntry':cpqSiHotPlugSlotEntry,_V:cpqSiHotPlugSlotChassis,_W:cpqSiHotPlugSlotIndex,'cpqSiHotPlugSlotBoardPresent':cpqSiHotPlugSlotBoardPresent,'cpqSiHotPlugSlotPowerState':cpqSiHotPlugSlotPowerState,'cpqSiHotPlugSlotBoardCondition':cpqSiHotPlugSlotBoardCondition,_r:cpqSiHotPlugSlotErrorStatus,'cpqSiHotPlugSlotHwLocation':cpqSiHotPlugSlotHwLocation,'cpqSiSystemBattery':cpqSiSystemBattery,'cpqSiSystemBatteryOverallCondition':cpqSiSystemBatteryOverallCondition,'cpqSiSysBatteryTable':cpqSiSysBatteryTable,'cpqSiSysBatteryEntry':cpqSiSysBatteryEntry,_X:cpqSiSysBatteryIndex,'cpqSiSysBatteryModel':cpqSiSysBatteryModel,_Y:cpqSiSysBatterySerialNum,'cpqSiSysBatteryAssetTag':cpqSiSysBatteryAssetTag,'cpqSiSysBatteryManufacturer':cpqSiSysBatteryManufacturer,'cpqSiSysBatteryDate':cpqSiSysBatteryDate,'cpqSiSysBatterySmartVersion':cpqSiSysBatterySmartVersion,'cpqSiSysBatteryCondition':cpqSiSysBatteryCondition,'cpqSiSysBatteryStatus':cpqSiSysBatteryStatus,'cpqSiSysBatteryChemistry':cpqSiSysBatteryChemistry,'cpqSiSysBatteryRemainingCap':cpqSiSysBatteryRemainingCap,'cpqSiSysBatteryFirmwareRevision':cpqSiSysBatteryFirmwareRevision,'cpqSiSysBatteryHardwareRevision':cpqSiSysBatteryHardwareRevision,'cpqSiSysBatteryFullCap':cpqSiSysBatteryFullCap,'cpqSiSysBatteryDesignCap':cpqSiSysBatteryDesignCap,'cpqSiSysBatteryHwLocation':cpqSiSysBatteryHwLocation,'cpqSiDockingStation':cpqSiDockingStation,'cpqSiDockingStationStatus':cpqSiDockingStationStatus,'cpqSiDockingStationSerialNum':cpqSiDockingStationSerialNum,'cpqSiDockingStationModel':cpqSiDockingStationModel,'cpqSiDockingStationAssetTag':cpqSiDockingStationAssetTag,'cpqSiFru':cpqSiFru,'cpqSiFruTable':cpqSiFruTable,'cpqSiFruEntry':cpqSiFruEntry,_o:cpqSiFruIndex,'cpqSiFruType':cpqSiFruType,'cpqSiFruDescr':cpqSiFruDescr,'cpqSiFruVendor':cpqSiFruVendor,'cpqSiFruPartNumber':cpqSiFruPartNumber,'cpqSiFruRevision':cpqSiFruRevision,'cpqSiFruFirmwareRevision':cpqSiFruFirmwareRevision,'cpqSiFruSerialNumber':cpqSiFruSerialNumber,'cpqSiFruAssetNo':cpqSiFruAssetNo,'cpqSiFruClass':cpqSiFruClass,'cpqSiFruSlotNumber':cpqSiFruSlotNumber,'cpqSiFruSubAssemblyNumber':cpqSiFruSubAssemblyNumber,'cpqSiFruAssemblyNumber':cpqSiFruAssemblyNumber,'cpqSiFruChassisNumber':cpqSiFruChassisNumber,'cpqSiFruPositionNumber':cpqSiFruPositionNumber,'cpqSiFruCabinetIDNumber':cpqSiFruCabinetIDNumber,'cpqSiFruSiteLocation':cpqSiFruSiteLocation,'cpqSiFruDiagStatus':cpqSiFruDiagStatus,'cpqSiFruExtendedDiagStatus':cpqSiFruExtendedDiagStatus,'cpqSiFruCellTablePtr':cpqSiFruCellTablePtr,'cpqSiFruIOCTablePtr':cpqSiFruIOCTablePtr,'cpqSiFruFileId':cpqSiFruFileId,'cpqSiFruScanRev':cpqSiFruScanRev,'cpqSiRackEnclosure':cpqSiRackEnclosure,'cpqSiRackEnclosureMgrTable':cpqSiRackEnclosureMgrTable,'cpqSiRackEnclosureMgrEntry':cpqSiRackEnclosureMgrEntry,_p:cpqSiRackEnclosureMgrIndex,'cpqSiRackEnclosureMgrType':cpqSiRackEnclosureMgrType,'cpqSiRackEnclosureMgrIpAddr':cpqSiRackEnclosureMgrIpAddr,'cpqSiRackEnclosureMgrWebLink':cpqSiRackEnclosureMgrWebLink,'cpqSiRackEnclosureMgrCondition':cpqSiRackEnclosureMgrCondition,'cpqSiRackEnclosureMgrSerialNumber':cpqSiRackEnclosureMgrSerialNumber,'cpqSiRackEnclosureMgrModel':cpqSiRackEnclosureMgrModel,'cpqSiRackEnclosureMgrName':cpqSiRackEnclosureMgrName,'cpqSiRackEnclosureMgrFwRev':cpqSiRackEnclosureMgrFwRev,'cpqSiRackEnclosureMgrProductID':cpqSiRackEnclosureMgrProductID,'cpqSiRackEnclosureMgrUUID':cpqSiRackEnclosureMgrUUID,'cpqSiRackEnclosureMgrMatrix':cpqSiRackEnclosureMgrMatrix,'cpqSiRackEnclosureMgrMatrixID':cpqSiRackEnclosureMgrMatrixID,'cpqSiServerBlade':cpqSiServerBlade,'cpqSiServerBladeEnclosureBayNumber':cpqSiServerBladeEnclosureBayNumber,'cpqSiServerBladeHeight':cpqSiServerBladeHeight,'cpqSiServerBladeWidth':cpqSiServerBladeWidth,'cpqSiRack':cpqSiRack,'cpqSiRackName':cpqSiRackName,'cpqSiRackUUID':cpqSiRackUUID,'cpqSiMP':cpqSiMP,'cpqSiMPHostName':cpqSiMPHostName,'cpqSiMPHealthStatus':cpqSiMPHealthStatus})