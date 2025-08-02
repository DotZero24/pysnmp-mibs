_V='zxAnMduConfigFileCRC32'
_U='zxAnMduType'
_T='zxAnMduHgVoiceVlan'
_S='zxAnMduHgVideoVlan'
_R='zxAnMduHgDataVlan'
_Q='zxAnMduEnvSwitchIndex'
_P='read-create'
_O='zxAnMduEnvEnvDeviceIndex'
_N='zxAnMduHgMacFeatureCodeId'
_M='zxAnMduEnvSwitchCurrentStatus'
_L='zxAnMduEnvSwitchNormalStatus'
_K='zxAnMduEnvEnvDeviceName'
_J='zxAnMduEnvDeviceId'
_I='zxAnMduHgMac'
_H='zxAnMduPortIfIndex'
_G='not-accessible'
_F='DisplayString'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='ZTE-AN-MDU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
VlanId,ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','VlanId','ZxAnIfindex','zxAn')
zxAnMduMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,1016))
_ZxAnMduSysCtrlObjects_ObjectIdentity=ObjectIdentity
zxAnMduSysCtrlObjects=_ZxAnMduSysCtrlObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,2))
_ZxAnMduSysDataMgmt_ObjectIdentity=ObjectIdentity
zxAnMduSysDataMgmt=_ZxAnMduSysDataMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,2,1))
class _ZxAnMduSaveModifiedToNvmInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_ZxAnMduSaveModifiedToNvmInterval_Type.__name__=_C
_ZxAnMduSaveModifiedToNvmInterval_Object=MibScalar
zxAnMduSaveModifiedToNvmInterval=_ZxAnMduSaveModifiedToNvmInterval_Object((1,3,6,1,4,1,3902,1015,1016,2,1,1),_ZxAnMduSaveModifiedToNvmInterval_Type())
zxAnMduSaveModifiedToNvmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduSaveModifiedToNvmInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnMduSaveModifiedToNvmInterval.setUnits('minutes')
class _ZxAnMduSaveToNvmInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8760))
_ZxAnMduSaveToNvmInterval_Type.__name__=_C
_ZxAnMduSaveToNvmInterval_Object=MibScalar
zxAnMduSaveToNvmInterval=_ZxAnMduSaveToNvmInterval_Object((1,3,6,1,4,1,3902,1015,1016,2,1,2),_ZxAnMduSaveToNvmInterval_Type())
zxAnMduSaveToNvmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduSaveToNvmInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnMduSaveToNvmInterval.setUnits('hours')
_ZxAnMduServiceObjects_ObjectIdentity=ObjectIdentity
zxAnMduServiceObjects=_ZxAnMduServiceObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,3))
_ZxAnMduHgMacFeatureCodeTable_Object=MibTable
zxAnMduHgMacFeatureCodeTable=_ZxAnMduHgMacFeatureCodeTable_Object((1,3,6,1,4,1,3902,1015,1016,3,1))
if mibBuilder.loadTexts:zxAnMduHgMacFeatureCodeTable.setStatus(_A)
_ZxAnMduHgMacFeatureCodeEntry_Object=MibTableRow
zxAnMduHgMacFeatureCodeEntry=_ZxAnMduHgMacFeatureCodeEntry_Object((1,3,6,1,4,1,3902,1015,1016,3,1,1))
zxAnMduHgMacFeatureCodeEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:zxAnMduHgMacFeatureCodeEntry.setStatus(_A)
_ZxAnMduHgMacFeatureCodeId_Type=Integer32
_ZxAnMduHgMacFeatureCodeId_Object=MibTableColumn
zxAnMduHgMacFeatureCodeId=_ZxAnMduHgMacFeatureCodeId_Object((1,3,6,1,4,1,3902,1015,1016,3,1,1,1),_ZxAnMduHgMacFeatureCodeId_Type())
zxAnMduHgMacFeatureCodeId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMduHgMacFeatureCodeId.setStatus(_A)
class _ZxAnMduHgMacFeatureCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnMduHgMacFeatureCode_Type.__name__=_F
_ZxAnMduHgMacFeatureCode_Object=MibTableColumn
zxAnMduHgMacFeatureCode=_ZxAnMduHgMacFeatureCode_Object((1,3,6,1,4,1,3902,1015,1016,3,1,1,2),_ZxAnMduHgMacFeatureCode_Type())
zxAnMduHgMacFeatureCode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduHgMacFeatureCode.setStatus(_A)
_ZxAnMduHgMgmtVlan_Type=Integer32
_ZxAnMduHgMgmtVlan_Object=MibScalar
zxAnMduHgMgmtVlan=_ZxAnMduHgMgmtVlan_Object((1,3,6,1,4,1,3902,1015,1016,3,2),_ZxAnMduHgMgmtVlan_Type())
zxAnMduHgMgmtVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduHgMgmtVlan.setStatus(_A)
class _ZxAnMduConfigFileCRC32_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_ZxAnMduConfigFileCRC32_Type.__name__=_F
_ZxAnMduConfigFileCRC32_Object=MibScalar
zxAnMduConfigFileCRC32=_ZxAnMduConfigFileCRC32_Object((1,3,6,1,4,1,3902,1015,1016,3,3),_ZxAnMduConfigFileCRC32_Type())
zxAnMduConfigFileCRC32.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMduConfigFileCRC32.setStatus(_A)
class _ZxAnMduLoadSettings_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('loadFactoryDefaults',1))
_ZxAnMduLoadSettings_Type.__name__=_C
_ZxAnMduLoadSettings_Object=MibScalar
zxAnMduLoadSettings=_ZxAnMduLoadSettings_Object((1,3,6,1,4,1,3902,1015,1016,3,4),_ZxAnMduLoadSettings_Type())
zxAnMduLoadSettings.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduLoadSettings.setStatus(_A)
_ZxAnMduHgTable_Object=MibTable
zxAnMduHgTable=_ZxAnMduHgTable_Object((1,3,6,1,4,1,3902,1015,1016,3,21))
if mibBuilder.loadTexts:zxAnMduHgTable.setStatus(_A)
_ZxAnMduHgEntry_Object=MibTableRow
zxAnMduHgEntry=_ZxAnMduHgEntry_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1))
zxAnMduHgEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:zxAnMduHgEntry.setStatus(_A)
_ZxAnMduPortIfIndex_Type=ZxAnIfindex
_ZxAnMduPortIfIndex_Object=MibTableColumn
zxAnMduPortIfIndex=_ZxAnMduPortIfIndex_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1,1),_ZxAnMduPortIfIndex_Type())
zxAnMduPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMduPortIfIndex.setStatus(_A)
_ZxAnMduHgMac_Type=MacAddress
_ZxAnMduHgMac_Object=MibTableColumn
zxAnMduHgMac=_ZxAnMduHgMac_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1,2),_ZxAnMduHgMac_Type())
zxAnMduHgMac.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMduHgMac.setStatus(_A)
class _ZxAnMduHgReportStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('failed',0),('success',1)))
_ZxAnMduHgReportStatus_Type.__name__=_C
_ZxAnMduHgReportStatus_Object=MibTableColumn
zxAnMduHgReportStatus=_ZxAnMduHgReportStatus_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1,3),_ZxAnMduHgReportStatus_Type())
zxAnMduHgReportStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduHgReportStatus.setStatus(_A)
_ZxAnMduHgDataVlan_Type=Integer32
_ZxAnMduHgDataVlan_Object=MibTableColumn
zxAnMduHgDataVlan=_ZxAnMduHgDataVlan_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1,4),_ZxAnMduHgDataVlan_Type())
zxAnMduHgDataVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMduHgDataVlan.setStatus(_A)
_ZxAnMduHgVideoVlan_Type=Integer32
_ZxAnMduHgVideoVlan_Object=MibTableColumn
zxAnMduHgVideoVlan=_ZxAnMduHgVideoVlan_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1,5),_ZxAnMduHgVideoVlan_Type())
zxAnMduHgVideoVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMduHgVideoVlan.setStatus(_A)
_ZxAnMduHgVoiceVlan_Type=Integer32
_ZxAnMduHgVoiceVlan_Object=MibTableColumn
zxAnMduHgVoiceVlan=_ZxAnMduHgVoiceVlan_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1,6),_ZxAnMduHgVoiceVlan_Type())
zxAnMduHgVoiceVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMduHgVoiceVlan.setStatus(_A)
class _ZxAnMduType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_ZxAnMduType_Type.__name__=_F
_ZxAnMduType_Object=MibTableColumn
zxAnMduType=_ZxAnMduType_Object((1,3,6,1,4,1,3902,1015,1016,3,21,1,7),_ZxAnMduType_Type())
zxAnMduType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMduType.setStatus(_A)
_ZxAnMduEquipObjects_ObjectIdentity=ObjectIdentity
zxAnMduEquipObjects=_ZxAnMduEquipObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,10))
_ZxAnMduEnvSwitchMgmt_ObjectIdentity=ObjectIdentity
zxAnMduEnvSwitchMgmt=_ZxAnMduEnvSwitchMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,10,21))
_ZxAnMduEnvDeviceTable_Object=MibTable
zxAnMduEnvDeviceTable=_ZxAnMduEnvDeviceTable_Object((1,3,6,1,4,1,3902,1015,1016,10,21,11))
if mibBuilder.loadTexts:zxAnMduEnvDeviceTable.setStatus(_A)
_ZxAnMduEnvDeviceEntry_Object=MibTableRow
zxAnMduEnvDeviceEntry=_ZxAnMduEnvDeviceEntry_Object((1,3,6,1,4,1,3902,1015,1016,10,21,11,1))
zxAnMduEnvDeviceEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:zxAnMduEnvDeviceEntry.setStatus(_A)
_ZxAnMduEnvEnvDeviceIndex_Type=Integer32
_ZxAnMduEnvEnvDeviceIndex_Object=MibTableColumn
zxAnMduEnvEnvDeviceIndex=_ZxAnMduEnvEnvDeviceIndex_Object((1,3,6,1,4,1,3902,1015,1016,10,21,11,1,1),_ZxAnMduEnvEnvDeviceIndex_Type())
zxAnMduEnvEnvDeviceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMduEnvEnvDeviceIndex.setStatus(_A)
class _ZxAnMduEnvEnvDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnMduEnvEnvDeviceName_Type.__name__=_F
_ZxAnMduEnvEnvDeviceName_Object=MibTableColumn
zxAnMduEnvEnvDeviceName=_ZxAnMduEnvEnvDeviceName_Object((1,3,6,1,4,1,3902,1015,1016,10,21,11,1,2),_ZxAnMduEnvEnvDeviceName_Type())
zxAnMduEnvEnvDeviceName.setMaxAccess(_P)
if mibBuilder.loadTexts:zxAnMduEnvEnvDeviceName.setStatus(_A)
_ZxAnMduEnvDeviceRowStatus_Type=RowStatus
_ZxAnMduEnvDeviceRowStatus_Object=MibTableColumn
zxAnMduEnvDeviceRowStatus=_ZxAnMduEnvDeviceRowStatus_Object((1,3,6,1,4,1,3902,1015,1016,10,21,11,1,3),_ZxAnMduEnvDeviceRowStatus_Type())
zxAnMduEnvDeviceRowStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:zxAnMduEnvDeviceRowStatus.setStatus(_A)
_ZxAnMduSwitchTable_Object=MibTable
zxAnMduSwitchTable=_ZxAnMduSwitchTable_Object((1,3,6,1,4,1,3902,1015,1016,10,21,12))
if mibBuilder.loadTexts:zxAnMduSwitchTable.setStatus(_A)
_ZxAnMduSwitchEntry_Object=MibTableRow
zxAnMduSwitchEntry=_ZxAnMduSwitchEntry_Object((1,3,6,1,4,1,3902,1015,1016,10,21,12,1))
zxAnMduSwitchEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:zxAnMduSwitchEntry.setStatus(_A)
_ZxAnMduEnvSwitchIndex_Type=Integer32
_ZxAnMduEnvSwitchIndex_Object=MibTableColumn
zxAnMduEnvSwitchIndex=_ZxAnMduEnvSwitchIndex_Object((1,3,6,1,4,1,3902,1015,1016,10,21,12,1,1),_ZxAnMduEnvSwitchIndex_Type())
zxAnMduEnvSwitchIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnMduEnvSwitchIndex.setStatus(_A)
class _ZxAnMduEnvDeviceId_Type(Integer32):defaultValue=0
_ZxAnMduEnvDeviceId_Type.__name__=_C
_ZxAnMduEnvDeviceId_Object=MibTableColumn
zxAnMduEnvDeviceId=_ZxAnMduEnvDeviceId_Object((1,3,6,1,4,1,3902,1015,1016,10,21,12,1,2),_ZxAnMduEnvDeviceId_Type())
zxAnMduEnvDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduEnvDeviceId.setStatus(_A)
class _ZxAnMduEnvSwitchNormalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_ZxAnMduEnvSwitchNormalStatus_Type.__name__=_C
_ZxAnMduEnvSwitchNormalStatus_Object=MibTableColumn
zxAnMduEnvSwitchNormalStatus=_ZxAnMduEnvSwitchNormalStatus_Object((1,3,6,1,4,1,3902,1015,1016,10,21,12,1,3),_ZxAnMduEnvSwitchNormalStatus_Type())
zxAnMduEnvSwitchNormalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduEnvSwitchNormalStatus.setStatus(_A)
class _ZxAnMduEnvSwitchEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ZxAnMduEnvSwitchEnable_Type.__name__=_C
_ZxAnMduEnvSwitchEnable_Object=MibTableColumn
zxAnMduEnvSwitchEnable=_ZxAnMduEnvSwitchEnable_Object((1,3,6,1,4,1,3902,1015,1016,10,21,12,1,4),_ZxAnMduEnvSwitchEnable_Type())
zxAnMduEnvSwitchEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMduEnvSwitchEnable.setStatus(_A)
class _ZxAnMduEnvSwitchCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_ZxAnMduEnvSwitchCurrentStatus_Type.__name__=_C
_ZxAnMduEnvSwitchCurrentStatus_Object=MibTableColumn
zxAnMduEnvSwitchCurrentStatus=_ZxAnMduEnvSwitchCurrentStatus_Object((1,3,6,1,4,1,3902,1015,1016,10,21,12,1,5),_ZxAnMduEnvSwitchCurrentStatus_Type())
zxAnMduEnvSwitchCurrentStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMduEnvSwitchCurrentStatus.setStatus(_A)
_ZxAnMduTrapObjects_ObjectIdentity=ObjectIdentity
zxAnMduTrapObjects=_ZxAnMduTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,20))
_ZxAnMduServiceTrapObjects_ObjectIdentity=ObjectIdentity
zxAnMduServiceTrapObjects=_ZxAnMduServiceTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,20,3))
_ZxAnMduEquipTrapObjects_ObjectIdentity=ObjectIdentity
zxAnMduEquipTrapObjects=_ZxAnMduEquipTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1016,20,10))
_ZxAnMduMibEnd_Type=Integer32
_ZxAnMduMibEnd_Object=MibScalar
zxAnMduMibEnd=_ZxAnMduMibEnd_Object((1,3,6,1,4,1,3902,1015,1016,100),_ZxAnMduMibEnd_Type())
zxAnMduMibEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnMduMibEnd.setStatus(_A)
zxAnMduNetworkAccessRequest=NotificationType((1,3,6,1,4,1,3902,1015,1016,20,3,1))
zxAnMduNetworkAccessRequest.setObjects(*((_B,_H),(_B,_I),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:zxAnMduNetworkAccessRequest.setStatus(_A)
zxAnMduUploadConfigFileRequest=NotificationType((1,3,6,1,4,1,3902,1015,1016,20,3,2))
zxAnMduUploadConfigFileRequest.setObjects(*((_B,_H),(_B,_V)))
if mibBuilder.loadTexts:zxAnMduUploadConfigFileRequest.setStatus(_A)
zxAnMduEnvSwitchFailed=NotificationType((1,3,6,1,4,1,3902,1015,1016,20,10,1))
zxAnMduEnvSwitchFailed.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:zxAnMduEnvSwitchFailed.setStatus(_A)
zxAnMduEnvSwitchRecovered=NotificationType((1,3,6,1,4,1,3902,1015,1016,20,10,2))
zxAnMduEnvSwitchRecovered.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:zxAnMduEnvSwitchRecovered.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnMduMib':zxAnMduMib,'zxAnMduSysCtrlObjects':zxAnMduSysCtrlObjects,'zxAnMduSysDataMgmt':zxAnMduSysDataMgmt,'zxAnMduSaveModifiedToNvmInterval':zxAnMduSaveModifiedToNvmInterval,'zxAnMduSaveToNvmInterval':zxAnMduSaveToNvmInterval,'zxAnMduServiceObjects':zxAnMduServiceObjects,'zxAnMduHgMacFeatureCodeTable':zxAnMduHgMacFeatureCodeTable,'zxAnMduHgMacFeatureCodeEntry':zxAnMduHgMacFeatureCodeEntry,_N:zxAnMduHgMacFeatureCodeId,'zxAnMduHgMacFeatureCode':zxAnMduHgMacFeatureCode,'zxAnMduHgMgmtVlan':zxAnMduHgMgmtVlan,_V:zxAnMduConfigFileCRC32,'zxAnMduLoadSettings':zxAnMduLoadSettings,'zxAnMduHgTable':zxAnMduHgTable,'zxAnMduHgEntry':zxAnMduHgEntry,_H:zxAnMduPortIfIndex,_I:zxAnMduHgMac,'zxAnMduHgReportStatus':zxAnMduHgReportStatus,_R:zxAnMduHgDataVlan,_S:zxAnMduHgVideoVlan,_T:zxAnMduHgVoiceVlan,_U:zxAnMduType,'zxAnMduEquipObjects':zxAnMduEquipObjects,'zxAnMduEnvSwitchMgmt':zxAnMduEnvSwitchMgmt,'zxAnMduEnvDeviceTable':zxAnMduEnvDeviceTable,'zxAnMduEnvDeviceEntry':zxAnMduEnvDeviceEntry,_O:zxAnMduEnvEnvDeviceIndex,_K:zxAnMduEnvEnvDeviceName,'zxAnMduEnvDeviceRowStatus':zxAnMduEnvDeviceRowStatus,'zxAnMduSwitchTable':zxAnMduSwitchTable,'zxAnMduSwitchEntry':zxAnMduSwitchEntry,_Q:zxAnMduEnvSwitchIndex,_J:zxAnMduEnvDeviceId,_L:zxAnMduEnvSwitchNormalStatus,'zxAnMduEnvSwitchEnable':zxAnMduEnvSwitchEnable,_M:zxAnMduEnvSwitchCurrentStatus,'zxAnMduTrapObjects':zxAnMduTrapObjects,'zxAnMduServiceTrapObjects':zxAnMduServiceTrapObjects,'zxAnMduNetworkAccessRequest':zxAnMduNetworkAccessRequest,'zxAnMduUploadConfigFileRequest':zxAnMduUploadConfigFileRequest,'zxAnMduEquipTrapObjects':zxAnMduEquipTrapObjects,'zxAnMduEnvSwitchFailed':zxAnMduEnvSwitchFailed,'zxAnMduEnvSwitchRecovered':zxAnMduEnvSwitchRecovered,'zxAnMduMibEnd':zxAnMduMibEnd})