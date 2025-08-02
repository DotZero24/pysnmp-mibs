_u='eventErrorMsg'
_t='eventWarningMsg'
_s='eventInformMsg'
_r='diskPerformanceIndex'
_q='targetIndex'
_p='lunIndex'
_o='volumeIndex'
_n='poolIndex'
_m='raidIndex'
_l='msataDiskIndex'
_k='abnormal'
_j='diskIndex'
_i='cpuIndex'
_h='systemPowerIndex'
_g='systemFanIndex'
_f='enclosureIndex'
_e='sysVolumeIndexEX'
_d='sysFanIndexEX'
_c='ifIndexEX'
_b='jBODHdIndex8'
_a='jBODHdIndex7'
_Z='jBODHdIndex6'
_Y='jBODHdIndex5'
_X='jBODHdIndex4'
_W='jBODHdIndex3'
_V='jBODHdIndex2'
_U='jBODHdIndex1'
_T='jBODid'
_S='sysVolumeIndex'
_R='sysFanIndex'
_Q='ifIndex'
_P='NotificationType'
_O='warning'
_N='error'
_M='hdIndex'
_L='yes'
_K='no'
_J='unknown'
_I='noDisk'
_H='invalid'
_G='rwError'
_F='ready'
_E='Integer32'
_D='NAS-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_P,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_P,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Storage_ObjectIdentity=ObjectIdentity
storage=_Storage_ObjectIdentity((1,3,6,1,4,1,24681))
_StorageSystem_ObjectIdentity=ObjectIdentity
storageSystem=_StorageSystem_ObjectIdentity((1,3,6,1,4,1,24681,1))
_SystemEventMsg_ObjectIdentity=ObjectIdentity
systemEventMsg=_SystemEventMsg_ObjectIdentity((1,3,6,1,4,1,24681,1,1))
_EventInformMsg_Type=DisplayString
_EventInformMsg_Object=MibScalar
eventInformMsg=_EventInformMsg_Object((1,3,6,1,4,1,24681,1,1,101),_EventInformMsg_Type())
eventInformMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eventInformMsg.setStatus(_A)
_EventWarningMsg_Type=DisplayString
_EventWarningMsg_Object=MibScalar
eventWarningMsg=_EventWarningMsg_Object((1,3,6,1,4,1,24681,1,1,102),_EventWarningMsg_Type())
eventWarningMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eventWarningMsg.setStatus(_A)
_EventErrorMsg_Type=DisplayString
_EventErrorMsg_Object=MibScalar
eventErrorMsg=_EventErrorMsg_Object((1,3,6,1,4,1,24681,1,1,103),_EventErrorMsg_Type())
eventErrorMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eventErrorMsg.setStatus(_A)
_SystemInfo_ObjectIdentity=ObjectIdentity
systemInfo=_SystemInfo_ObjectIdentity((1,3,6,1,4,1,24681,1,2))
_SystemCPU_Usage_Type=DisplayString
_SystemCPU_Usage_Object=MibScalar
systemCPU_Usage=_SystemCPU_Usage_Object((1,3,6,1,4,1,24681,1,2,1),_SystemCPU_Usage_Type())
systemCPU_Usage.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCPU_Usage.setStatus(_A)
_SystemTotalMem_Type=DisplayString
_SystemTotalMem_Object=MibScalar
systemTotalMem=_SystemTotalMem_Object((1,3,6,1,4,1,24681,1,2,2),_SystemTotalMem_Type())
systemTotalMem.setMaxAccess(_B)
if mibBuilder.loadTexts:systemTotalMem.setStatus(_A)
_SystemFreeMem_Type=DisplayString
_SystemFreeMem_Object=MibScalar
systemFreeMem=_SystemFreeMem_Object((1,3,6,1,4,1,24681,1,2,3),_SystemFreeMem_Type())
systemFreeMem.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFreeMem.setStatus(_A)
_SystemUptime_Type=TimeTicks
_SystemUptime_Object=MibScalar
systemUptime=_SystemUptime_Object((1,3,6,1,4,1,24681,1,2,4),_SystemUptime_Type())
systemUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:systemUptime.setStatus(_A)
_Cpu_Temperature_Type=DisplayString
_Cpu_Temperature_Object=MibScalar
cpu_Temperature=_Cpu_Temperature_Object((1,3,6,1,4,1,24681,1,2,5),_Cpu_Temperature_Type())
cpu_Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cpu_Temperature.setStatus(_A)
_SystemTemperature_Type=DisplayString
_SystemTemperature_Object=MibScalar
systemTemperature=_SystemTemperature_Object((1,3,6,1,4,1,24681,1,2,6),_SystemTemperature_Type())
systemTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:systemTemperature.setStatus(_A)
_IfNumber_Type=Integer32
_IfNumber_Object=MibScalar
ifNumber=_IfNumber_Object((1,3,6,1,4,1,24681,1,2,8),_IfNumber_Type())
ifNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ifNumber.setStatus(_A)
_SystemIfTable_Object=MibTable
systemIfTable=_SystemIfTable_Object((1,3,6,1,4,1,24681,1,2,9))
if mibBuilder.loadTexts:systemIfTable.setStatus(_A)
_IfEntry_Object=MibTableRow
ifEntry=_IfEntry_Object((1,3,6,1,4,1,24681,1,2,9,1))
ifEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:ifEntry.setStatus(_A)
_IfIndex_Type=Integer32
_IfIndex_Object=MibTableColumn
ifIndex=_IfIndex_Object((1,3,6,1,4,1,24681,1,2,9,1,1),_IfIndex_Type())
ifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIndex.setStatus(_A)
class _IfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfDescr_Type.__name__=_C
_IfDescr_Object=MibTableColumn
ifDescr=_IfDescr_Object((1,3,6,1,4,1,24681,1,2,9,1,2),_IfDescr_Type())
ifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ifDescr.setStatus(_A)
_IfPacketsReceived_Type=Counter32
_IfPacketsReceived_Object=MibTableColumn
ifPacketsReceived=_IfPacketsReceived_Object((1,3,6,1,4,1,24681,1,2,9,1,3),_IfPacketsReceived_Type())
ifPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPacketsReceived.setStatus(_A)
_IfPacketsSent_Type=Counter32
_IfPacketsSent_Object=MibTableColumn
ifPacketsSent=_IfPacketsSent_Object((1,3,6,1,4,1,24681,1,2,9,1,4),_IfPacketsSent_Type())
ifPacketsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPacketsSent.setStatus(_A)
_IfErrorPackets_Type=Counter32
_IfErrorPackets_Object=MibTableColumn
ifErrorPackets=_IfErrorPackets_Object((1,3,6,1,4,1,24681,1,2,9,1,5),_IfErrorPackets_Type())
ifErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifErrorPackets.setStatus(_A)
_HdNumber_Type=Integer32
_HdNumber_Object=MibScalar
hdNumber=_HdNumber_Object((1,3,6,1,4,1,24681,1,2,10),_HdNumber_Type())
hdNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hdNumber.setStatus(_A)
_SystemHdTable_Object=MibTable
systemHdTable=_SystemHdTable_Object((1,3,6,1,4,1,24681,1,2,11))
if mibBuilder.loadTexts:systemHdTable.setStatus(_A)
_HdEntry_Object=MibTableRow
hdEntry=_HdEntry_Object((1,3,6,1,4,1,24681,1,2,11,1))
hdEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:hdEntry.setStatus(_A)
_HdIndex_Type=Integer32
_HdIndex_Object=MibTableColumn
hdIndex=_HdIndex_Object((1,3,6,1,4,1,24681,1,2,11,1,1),_HdIndex_Type())
hdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hdIndex.setStatus(_A)
class _HdDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HdDescr_Type.__name__=_C
_HdDescr_Object=MibTableColumn
hdDescr=_HdDescr_Object((1,3,6,1,4,1,24681,1,2,11,1,2),_HdDescr_Type())
hdDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hdDescr.setStatus(_A)
_HdTemperature_Type=DisplayString
_HdTemperature_Object=MibTableColumn
hdTemperature=_HdTemperature_Object((1,3,6,1,4,1,24681,1,2,11,1,3),_HdTemperature_Type())
hdTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hdTemperature.setStatus(_A)
class _HdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_HdStatus_Type.__name__=_E
_HdStatus_Object=MibTableColumn
hdStatus=_HdStatus_Object((1,3,6,1,4,1,24681,1,2,11,1,4),_HdStatus_Type())
hdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hdStatus.setStatus(_A)
_HdModel_Type=DisplayString
_HdModel_Object=MibTableColumn
hdModel=_HdModel_Object((1,3,6,1,4,1,24681,1,2,11,1,5),_HdModel_Type())
hdModel.setMaxAccess(_B)
if mibBuilder.loadTexts:hdModel.setStatus(_A)
_HdCapacity_Type=DisplayString
_HdCapacity_Object=MibTableColumn
hdCapacity=_HdCapacity_Object((1,3,6,1,4,1,24681,1,2,11,1,6),_HdCapacity_Type())
hdCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hdCapacity.setStatus(_A)
_HdSmartInfo_Type=DisplayString
_HdSmartInfo_Object=MibTableColumn
hdSmartInfo=_HdSmartInfo_Object((1,3,6,1,4,1,24681,1,2,11,1,7),_HdSmartInfo_Type())
hdSmartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hdSmartInfo.setStatus(_A)
_ModelName_Type=DisplayString
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,24681,1,2,12),_ModelName_Type())
modelName.setMaxAccess(_B)
if mibBuilder.loadTexts:modelName.setStatus(_A)
_HostName_Type=DisplayString
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,24681,1,2,13),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
_SysFanNumber_Type=Integer32
_SysFanNumber_Object=MibScalar
sysFanNumber=_SysFanNumber_Object((1,3,6,1,4,1,24681,1,2,14),_SysFanNumber_Type())
sysFanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanNumber.setStatus(_A)
_SystemFanTable_Object=MibTable
systemFanTable=_SystemFanTable_Object((1,3,6,1,4,1,24681,1,2,15))
if mibBuilder.loadTexts:systemFanTable.setStatus(_A)
_SysFanEntry_Object=MibTableRow
sysFanEntry=_SysFanEntry_Object((1,3,6,1,4,1,24681,1,2,15,1))
sysFanEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:sysFanEntry.setStatus(_A)
_SysFanIndex_Type=Integer32
_SysFanIndex_Object=MibTableColumn
sysFanIndex=_SysFanIndex_Object((1,3,6,1,4,1,24681,1,2,15,1,1),_SysFanIndex_Type())
sysFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanIndex.setStatus(_A)
class _SysFanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysFanDescr_Type.__name__=_C
_SysFanDescr_Object=MibTableColumn
sysFanDescr=_SysFanDescr_Object((1,3,6,1,4,1,24681,1,2,15,1,2),_SysFanDescr_Type())
sysFanDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanDescr.setStatus(_A)
class _SysFanSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysFanSpeed_Type.__name__=_C
_SysFanSpeed_Object=MibTableColumn
sysFanSpeed=_SysFanSpeed_Object((1,3,6,1,4,1,24681,1,2,15,1,3),_SysFanSpeed_Type())
sysFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanSpeed.setStatus(_A)
_SysVolumeNumber_Type=Integer32
_SysVolumeNumber_Object=MibScalar
sysVolumeNumber=_SysVolumeNumber_Object((1,3,6,1,4,1,24681,1,2,16),_SysVolumeNumber_Type())
sysVolumeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeNumber.setStatus(_A)
_SystemVolumeTable_Object=MibTable
systemVolumeTable=_SystemVolumeTable_Object((1,3,6,1,4,1,24681,1,2,17))
if mibBuilder.loadTexts:systemVolumeTable.setStatus(_A)
_SysVolumeEntry_Object=MibTableRow
sysVolumeEntry=_SysVolumeEntry_Object((1,3,6,1,4,1,24681,1,2,17,1))
sysVolumeEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:sysVolumeEntry.setStatus(_A)
_SysVolumeIndex_Type=Integer32
_SysVolumeIndex_Object=MibTableColumn
sysVolumeIndex=_SysVolumeIndex_Object((1,3,6,1,4,1,24681,1,2,17,1,1),_SysVolumeIndex_Type())
sysVolumeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeIndex.setStatus(_A)
class _SysVolumeDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysVolumeDescr_Type.__name__=_C
_SysVolumeDescr_Object=MibTableColumn
sysVolumeDescr=_SysVolumeDescr_Object((1,3,6,1,4,1,24681,1,2,17,1,2),_SysVolumeDescr_Type())
sysVolumeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeDescr.setStatus(_A)
class _SysVolumeFS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysVolumeFS_Type.__name__=_C
_SysVolumeFS_Object=MibTableColumn
sysVolumeFS=_SysVolumeFS_Object((1,3,6,1,4,1,24681,1,2,17,1,3),_SysVolumeFS_Type())
sysVolumeFS.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeFS.setStatus(_A)
class _SysVolumeTotalSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysVolumeTotalSize_Type.__name__=_C
_SysVolumeTotalSize_Object=MibTableColumn
sysVolumeTotalSize=_SysVolumeTotalSize_Object((1,3,6,1,4,1,24681,1,2,17,1,4),_SysVolumeTotalSize_Type())
sysVolumeTotalSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeTotalSize.setStatus(_A)
class _SysVolumeFreeSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysVolumeFreeSize_Type.__name__=_C
_SysVolumeFreeSize_Object=MibTableColumn
sysVolumeFreeSize=_SysVolumeFreeSize_Object((1,3,6,1,4,1,24681,1,2,17,1,5),_SysVolumeFreeSize_Type())
sysVolumeFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeFreeSize.setStatus(_A)
class _SysVolumeStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysVolumeStatus_Type.__name__=_C
_SysVolumeStatus_Object=MibTableColumn
sysVolumeStatus=_SysVolumeStatus_Object((1,3,6,1,4,1,24681,1,2,17,1,6),_SysVolumeStatus_Type())
sysVolumeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeStatus.setStatus(_A)
_JBODInfo_Type=DisplayString
_JBODInfo_Object=MibScalar
jBODInfo=_JBODInfo_Object((1,3,6,1,4,1,24681,1,2,18),_JBODInfo_Type())
jBODInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODInfo.setStatus(_A)
_JBODBitmap_Type=DisplayString
_JBODBitmap_Object=MibScalar
jBODBitmap=_JBODBitmap_Object((1,3,6,1,4,1,24681,1,2,18,1),_JBODBitmap_Type())
jBODBitmap.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODBitmap.setStatus(_A)
_JBODInfos_Object=MibTable
jBODInfos=_JBODInfos_Object((1,3,6,1,4,1,24681,1,2,18,2))
if mibBuilder.loadTexts:jBODInfos.setStatus(_A)
_JBODInfosEntry_Object=MibTableRow
jBODInfosEntry=_JBODInfosEntry_Object((1,3,6,1,4,1,24681,1,2,18,2,1))
jBODInfosEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:jBODInfosEntry.setStatus(_A)
_JBODid_Type=Integer32
_JBODid_Object=MibTableColumn
jBODid=_JBODid_Object((1,3,6,1,4,1,24681,1,2,18,2,1,1),_JBODid_Type())
jBODid.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODid.setStatus(_A)
_JBODHdNumber_Type=Integer32
_JBODHdNumber_Object=MibTableColumn
jBODHdNumber=_JBODHdNumber_Object((1,3,6,1,4,1,24681,1,2,18,2,1,2),_JBODHdNumber_Type())
jBODHdNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdNumber.setStatus(_A)
_JBODHdTable1_Object=MibTable
jBODHdTable1=_JBODHdTable1_Object((1,3,6,1,4,1,24681,1,2,18,3))
if mibBuilder.loadTexts:jBODHdTable1.setStatus(_A)
_JBODHdEntry1_Object=MibTableRow
jBODHdEntry1=_JBODHdEntry1_Object((1,3,6,1,4,1,24681,1,2,18,3,1))
jBODHdEntry1.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:jBODHdEntry1.setStatus(_A)
_JBODHdIndex1_Type=Integer32
_JBODHdIndex1_Object=MibTableColumn
jBODHdIndex1=_JBODHdIndex1_Object((1,3,6,1,4,1,24681,1,2,18,3,1,1),_JBODHdIndex1_Type())
jBODHdIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex1.setStatus(_A)
class _JBODHdDescr1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr1_Type.__name__=_C
_JBODHdDescr1_Object=MibTableColumn
jBODHdDescr1=_JBODHdDescr1_Object((1,3,6,1,4,1,24681,1,2,18,3,1,2),_JBODHdDescr1_Type())
jBODHdDescr1.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr1.setStatus(_A)
_JBODHdTemperature1_Type=DisplayString
_JBODHdTemperature1_Object=MibTableColumn
jBODHdTemperature1=_JBODHdTemperature1_Object((1,3,6,1,4,1,24681,1,2,18,3,1,3),_JBODHdTemperature1_Type())
jBODHdTemperature1.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature1.setStatus(_A)
class _JBODHdStatus1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus1_Type.__name__=_E
_JBODHdStatus1_Object=MibTableColumn
jBODHdStatus1=_JBODHdStatus1_Object((1,3,6,1,4,1,24681,1,2,18,3,1,4),_JBODHdStatus1_Type())
jBODHdStatus1.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus1.setStatus(_A)
_JBODHdModel1_Type=DisplayString
_JBODHdModel1_Object=MibTableColumn
jBODHdModel1=_JBODHdModel1_Object((1,3,6,1,4,1,24681,1,2,18,3,1,5),_JBODHdModel1_Type())
jBODHdModel1.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel1.setStatus(_A)
_JBODHdCapacity1_Type=DisplayString
_JBODHdCapacity1_Object=MibTableColumn
jBODHdCapacity1=_JBODHdCapacity1_Object((1,3,6,1,4,1,24681,1,2,18,3,1,6),_JBODHdCapacity1_Type())
jBODHdCapacity1.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity1.setStatus(_A)
_JBODHdSmartInfo1_Type=DisplayString
_JBODHdSmartInfo1_Object=MibTableColumn
jBODHdSmartInfo1=_JBODHdSmartInfo1_Object((1,3,6,1,4,1,24681,1,2,18,3,1,7),_JBODHdSmartInfo1_Type())
jBODHdSmartInfo1.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo1.setStatus(_A)
_JBODHdTable2_Object=MibTable
jBODHdTable2=_JBODHdTable2_Object((1,3,6,1,4,1,24681,1,2,18,4))
if mibBuilder.loadTexts:jBODHdTable2.setStatus(_A)
_JBODHdEntry2_Object=MibTableRow
jBODHdEntry2=_JBODHdEntry2_Object((1,3,6,1,4,1,24681,1,2,18,4,1))
jBODHdEntry2.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:jBODHdEntry2.setStatus(_A)
_JBODHdIndex2_Type=Integer32
_JBODHdIndex2_Object=MibTableColumn
jBODHdIndex2=_JBODHdIndex2_Object((1,3,6,1,4,1,24681,1,2,18,4,1,1),_JBODHdIndex2_Type())
jBODHdIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex2.setStatus(_A)
class _JBODHdDescr2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr2_Type.__name__=_C
_JBODHdDescr2_Object=MibTableColumn
jBODHdDescr2=_JBODHdDescr2_Object((1,3,6,1,4,1,24681,1,2,18,4,1,2),_JBODHdDescr2_Type())
jBODHdDescr2.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr2.setStatus(_A)
_JBODHdTemperature2_Type=DisplayString
_JBODHdTemperature2_Object=MibTableColumn
jBODHdTemperature2=_JBODHdTemperature2_Object((1,3,6,1,4,1,24681,1,2,18,4,1,3),_JBODHdTemperature2_Type())
jBODHdTemperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature2.setStatus(_A)
class _JBODHdStatus2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus2_Type.__name__=_E
_JBODHdStatus2_Object=MibTableColumn
jBODHdStatus2=_JBODHdStatus2_Object((1,3,6,1,4,1,24681,1,2,18,4,1,4),_JBODHdStatus2_Type())
jBODHdStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus2.setStatus(_A)
_JBODHdModel2_Type=DisplayString
_JBODHdModel2_Object=MibTableColumn
jBODHdModel2=_JBODHdModel2_Object((1,3,6,1,4,1,24681,1,2,18,4,1,5),_JBODHdModel2_Type())
jBODHdModel2.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel2.setStatus(_A)
_JBODHdCapacity2_Type=DisplayString
_JBODHdCapacity2_Object=MibTableColumn
jBODHdCapacity2=_JBODHdCapacity2_Object((1,3,6,1,4,1,24681,1,2,18,4,1,6),_JBODHdCapacity2_Type())
jBODHdCapacity2.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity2.setStatus(_A)
_JBODHdSmartInfo2_Type=DisplayString
_JBODHdSmartInfo2_Object=MibTableColumn
jBODHdSmartInfo2=_JBODHdSmartInfo2_Object((1,3,6,1,4,1,24681,1,2,18,4,1,7),_JBODHdSmartInfo2_Type())
jBODHdSmartInfo2.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo2.setStatus(_A)
_JBODHdTable3_Object=MibTable
jBODHdTable3=_JBODHdTable3_Object((1,3,6,1,4,1,24681,1,2,18,5))
if mibBuilder.loadTexts:jBODHdTable3.setStatus(_A)
_JBODHdEntry3_Object=MibTableRow
jBODHdEntry3=_JBODHdEntry3_Object((1,3,6,1,4,1,24681,1,2,18,5,1))
jBODHdEntry3.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:jBODHdEntry3.setStatus(_A)
_JBODHdIndex3_Type=Integer32
_JBODHdIndex3_Object=MibTableColumn
jBODHdIndex3=_JBODHdIndex3_Object((1,3,6,1,4,1,24681,1,2,18,5,1,1),_JBODHdIndex3_Type())
jBODHdIndex3.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex3.setStatus(_A)
class _JBODHdDescr3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr3_Type.__name__=_C
_JBODHdDescr3_Object=MibTableColumn
jBODHdDescr3=_JBODHdDescr3_Object((1,3,6,1,4,1,24681,1,2,18,5,1,2),_JBODHdDescr3_Type())
jBODHdDescr3.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr3.setStatus(_A)
_JBODHdTemperature3_Type=DisplayString
_JBODHdTemperature3_Object=MibTableColumn
jBODHdTemperature3=_JBODHdTemperature3_Object((1,3,6,1,4,1,24681,1,2,18,5,1,3),_JBODHdTemperature3_Type())
jBODHdTemperature3.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature3.setStatus(_A)
class _JBODHdStatus3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus3_Type.__name__=_E
_JBODHdStatus3_Object=MibTableColumn
jBODHdStatus3=_JBODHdStatus3_Object((1,3,6,1,4,1,24681,1,2,18,5,1,4),_JBODHdStatus3_Type())
jBODHdStatus3.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus3.setStatus(_A)
_JBODHdModel3_Type=DisplayString
_JBODHdModel3_Object=MibTableColumn
jBODHdModel3=_JBODHdModel3_Object((1,3,6,1,4,1,24681,1,2,18,5,1,5),_JBODHdModel3_Type())
jBODHdModel3.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel3.setStatus(_A)
_JBODHdCapacity3_Type=DisplayString
_JBODHdCapacity3_Object=MibTableColumn
jBODHdCapacity3=_JBODHdCapacity3_Object((1,3,6,1,4,1,24681,1,2,18,5,1,6),_JBODHdCapacity3_Type())
jBODHdCapacity3.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity3.setStatus(_A)
_JBODHdSmartInfo3_Type=DisplayString
_JBODHdSmartInfo3_Object=MibTableColumn
jBODHdSmartInfo3=_JBODHdSmartInfo3_Object((1,3,6,1,4,1,24681,1,2,18,5,1,7),_JBODHdSmartInfo3_Type())
jBODHdSmartInfo3.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo3.setStatus(_A)
_JBODHdTable4_Object=MibTable
jBODHdTable4=_JBODHdTable4_Object((1,3,6,1,4,1,24681,1,2,18,6))
if mibBuilder.loadTexts:jBODHdTable4.setStatus(_A)
_JBODHdEntry4_Object=MibTableRow
jBODHdEntry4=_JBODHdEntry4_Object((1,3,6,1,4,1,24681,1,2,18,6,1))
jBODHdEntry4.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:jBODHdEntry4.setStatus(_A)
_JBODHdIndex4_Type=Integer32
_JBODHdIndex4_Object=MibTableColumn
jBODHdIndex4=_JBODHdIndex4_Object((1,3,6,1,4,1,24681,1,2,18,6,1,1),_JBODHdIndex4_Type())
jBODHdIndex4.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex4.setStatus(_A)
class _JBODHdDescr4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr4_Type.__name__=_C
_JBODHdDescr4_Object=MibTableColumn
jBODHdDescr4=_JBODHdDescr4_Object((1,3,6,1,4,1,24681,1,2,18,6,1,2),_JBODHdDescr4_Type())
jBODHdDescr4.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr4.setStatus(_A)
_JBODHdTemperature4_Type=DisplayString
_JBODHdTemperature4_Object=MibTableColumn
jBODHdTemperature4=_JBODHdTemperature4_Object((1,3,6,1,4,1,24681,1,2,18,6,1,3),_JBODHdTemperature4_Type())
jBODHdTemperature4.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature4.setStatus(_A)
class _JBODHdStatus4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus4_Type.__name__=_E
_JBODHdStatus4_Object=MibTableColumn
jBODHdStatus4=_JBODHdStatus4_Object((1,3,6,1,4,1,24681,1,2,18,6,1,4),_JBODHdStatus4_Type())
jBODHdStatus4.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus4.setStatus(_A)
_JBODHdModel4_Type=DisplayString
_JBODHdModel4_Object=MibTableColumn
jBODHdModel4=_JBODHdModel4_Object((1,3,6,1,4,1,24681,1,2,18,6,1,5),_JBODHdModel4_Type())
jBODHdModel4.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel4.setStatus(_A)
_JBODHdCapacity4_Type=DisplayString
_JBODHdCapacity4_Object=MibTableColumn
jBODHdCapacity4=_JBODHdCapacity4_Object((1,3,6,1,4,1,24681,1,2,18,6,1,6),_JBODHdCapacity4_Type())
jBODHdCapacity4.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity4.setStatus(_A)
_JBODHdSmartInfo4_Type=DisplayString
_JBODHdSmartInfo4_Object=MibTableColumn
jBODHdSmartInfo4=_JBODHdSmartInfo4_Object((1,3,6,1,4,1,24681,1,2,18,6,1,7),_JBODHdSmartInfo4_Type())
jBODHdSmartInfo4.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo4.setStatus(_A)
_JBODHdTable5_Object=MibTable
jBODHdTable5=_JBODHdTable5_Object((1,3,6,1,4,1,24681,1,2,18,7))
if mibBuilder.loadTexts:jBODHdTable5.setStatus(_A)
_JBODHdEntry5_Object=MibTableRow
jBODHdEntry5=_JBODHdEntry5_Object((1,3,6,1,4,1,24681,1,2,18,7,1))
jBODHdEntry5.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:jBODHdEntry5.setStatus(_A)
_JBODHdIndex5_Type=Integer32
_JBODHdIndex5_Object=MibTableColumn
jBODHdIndex5=_JBODHdIndex5_Object((1,3,6,1,4,1,24681,1,2,18,7,1,1),_JBODHdIndex5_Type())
jBODHdIndex5.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex5.setStatus(_A)
class _JBODHdDescr5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr5_Type.__name__=_C
_JBODHdDescr5_Object=MibTableColumn
jBODHdDescr5=_JBODHdDescr5_Object((1,3,6,1,4,1,24681,1,2,18,7,1,2),_JBODHdDescr5_Type())
jBODHdDescr5.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr5.setStatus(_A)
_JBODHdTemperature5_Type=DisplayString
_JBODHdTemperature5_Object=MibTableColumn
jBODHdTemperature5=_JBODHdTemperature5_Object((1,3,6,1,4,1,24681,1,2,18,7,1,3),_JBODHdTemperature5_Type())
jBODHdTemperature5.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature5.setStatus(_A)
class _JBODHdStatus5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus5_Type.__name__=_E
_JBODHdStatus5_Object=MibTableColumn
jBODHdStatus5=_JBODHdStatus5_Object((1,3,6,1,4,1,24681,1,2,18,7,1,4),_JBODHdStatus5_Type())
jBODHdStatus5.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus5.setStatus(_A)
_JBODHdModel5_Type=DisplayString
_JBODHdModel5_Object=MibTableColumn
jBODHdModel5=_JBODHdModel5_Object((1,3,6,1,4,1,24681,1,2,18,7,1,5),_JBODHdModel5_Type())
jBODHdModel5.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel5.setStatus(_A)
_JBODHdCapacity5_Type=DisplayString
_JBODHdCapacity5_Object=MibTableColumn
jBODHdCapacity5=_JBODHdCapacity5_Object((1,3,6,1,4,1,24681,1,2,18,7,1,6),_JBODHdCapacity5_Type())
jBODHdCapacity5.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity5.setStatus(_A)
_JBODHdSmartInfo5_Type=DisplayString
_JBODHdSmartInfo5_Object=MibTableColumn
jBODHdSmartInfo5=_JBODHdSmartInfo5_Object((1,3,6,1,4,1,24681,1,2,18,7,1,7),_JBODHdSmartInfo5_Type())
jBODHdSmartInfo5.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo5.setStatus(_A)
_JBODHdTable6_Object=MibTable
jBODHdTable6=_JBODHdTable6_Object((1,3,6,1,4,1,24681,1,2,18,8))
if mibBuilder.loadTexts:jBODHdTable6.setStatus(_A)
_JBODHdEntry6_Object=MibTableRow
jBODHdEntry6=_JBODHdEntry6_Object((1,3,6,1,4,1,24681,1,2,18,8,1))
jBODHdEntry6.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:jBODHdEntry6.setStatus(_A)
_JBODHdIndex6_Type=Integer32
_JBODHdIndex6_Object=MibTableColumn
jBODHdIndex6=_JBODHdIndex6_Object((1,3,6,1,4,1,24681,1,2,18,8,1,1),_JBODHdIndex6_Type())
jBODHdIndex6.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex6.setStatus(_A)
class _JBODHdDescr6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr6_Type.__name__=_C
_JBODHdDescr6_Object=MibTableColumn
jBODHdDescr6=_JBODHdDescr6_Object((1,3,6,1,4,1,24681,1,2,18,8,1,2),_JBODHdDescr6_Type())
jBODHdDescr6.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr6.setStatus(_A)
_JBODHdTemperature6_Type=DisplayString
_JBODHdTemperature6_Object=MibTableColumn
jBODHdTemperature6=_JBODHdTemperature6_Object((1,3,6,1,4,1,24681,1,2,18,8,1,3),_JBODHdTemperature6_Type())
jBODHdTemperature6.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature6.setStatus(_A)
class _JBODHdStatus6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus6_Type.__name__=_E
_JBODHdStatus6_Object=MibTableColumn
jBODHdStatus6=_JBODHdStatus6_Object((1,3,6,1,4,1,24681,1,2,18,8,1,4),_JBODHdStatus6_Type())
jBODHdStatus6.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus6.setStatus(_A)
_JBODHdModel6_Type=DisplayString
_JBODHdModel6_Object=MibTableColumn
jBODHdModel6=_JBODHdModel6_Object((1,3,6,1,4,1,24681,1,2,18,8,1,5),_JBODHdModel6_Type())
jBODHdModel6.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel6.setStatus(_A)
_JBODHdCapacity6_Type=DisplayString
_JBODHdCapacity6_Object=MibTableColumn
jBODHdCapacity6=_JBODHdCapacity6_Object((1,3,6,1,4,1,24681,1,2,18,8,1,6),_JBODHdCapacity6_Type())
jBODHdCapacity6.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity6.setStatus(_A)
_JBODHdSmartInfo6_Type=DisplayString
_JBODHdSmartInfo6_Object=MibTableColumn
jBODHdSmartInfo6=_JBODHdSmartInfo6_Object((1,3,6,1,4,1,24681,1,2,18,8,1,7),_JBODHdSmartInfo6_Type())
jBODHdSmartInfo6.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo6.setStatus(_A)
_JBODHdTable7_Object=MibTable
jBODHdTable7=_JBODHdTable7_Object((1,3,6,1,4,1,24681,1,2,18,9))
if mibBuilder.loadTexts:jBODHdTable7.setStatus(_A)
_JBODHdEntry7_Object=MibTableRow
jBODHdEntry7=_JBODHdEntry7_Object((1,3,6,1,4,1,24681,1,2,18,9,1))
jBODHdEntry7.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:jBODHdEntry7.setStatus(_A)
_JBODHdIndex7_Type=Integer32
_JBODHdIndex7_Object=MibTableColumn
jBODHdIndex7=_JBODHdIndex7_Object((1,3,6,1,4,1,24681,1,2,18,9,1,1),_JBODHdIndex7_Type())
jBODHdIndex7.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex7.setStatus(_A)
class _JBODHdDescr7_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr7_Type.__name__=_C
_JBODHdDescr7_Object=MibTableColumn
jBODHdDescr7=_JBODHdDescr7_Object((1,3,6,1,4,1,24681,1,2,18,9,1,2),_JBODHdDescr7_Type())
jBODHdDescr7.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr7.setStatus(_A)
_JBODHdTemperature7_Type=DisplayString
_JBODHdTemperature7_Object=MibTableColumn
jBODHdTemperature7=_JBODHdTemperature7_Object((1,3,6,1,4,1,24681,1,2,18,9,1,3),_JBODHdTemperature7_Type())
jBODHdTemperature7.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature7.setStatus(_A)
class _JBODHdStatus7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus7_Type.__name__=_E
_JBODHdStatus7_Object=MibTableColumn
jBODHdStatus7=_JBODHdStatus7_Object((1,3,6,1,4,1,24681,1,2,18,9,1,4),_JBODHdStatus7_Type())
jBODHdStatus7.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus7.setStatus(_A)
_JBODHdModel7_Type=DisplayString
_JBODHdModel7_Object=MibTableColumn
jBODHdModel7=_JBODHdModel7_Object((1,3,6,1,4,1,24681,1,2,18,9,1,5),_JBODHdModel7_Type())
jBODHdModel7.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel7.setStatus(_A)
_JBODHdCapacity7_Type=DisplayString
_JBODHdCapacity7_Object=MibTableColumn
jBODHdCapacity7=_JBODHdCapacity7_Object((1,3,6,1,4,1,24681,1,2,18,9,1,6),_JBODHdCapacity7_Type())
jBODHdCapacity7.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity7.setStatus(_A)
_JBODHdSmartInfo7_Type=DisplayString
_JBODHdSmartInfo7_Object=MibTableColumn
jBODHdSmartInfo7=_JBODHdSmartInfo7_Object((1,3,6,1,4,1,24681,1,2,18,9,1,7),_JBODHdSmartInfo7_Type())
jBODHdSmartInfo7.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo7.setStatus(_A)
_JBODHdTable8_Object=MibTable
jBODHdTable8=_JBODHdTable8_Object((1,3,6,1,4,1,24681,1,2,18,10))
if mibBuilder.loadTexts:jBODHdTable8.setStatus(_A)
_JBODHdEntry8_Object=MibTableRow
jBODHdEntry8=_JBODHdEntry8_Object((1,3,6,1,4,1,24681,1,2,18,10,1))
jBODHdEntry8.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:jBODHdEntry8.setStatus(_A)
_JBODHdIndex8_Type=Integer32
_JBODHdIndex8_Object=MibTableColumn
jBODHdIndex8=_JBODHdIndex8_Object((1,3,6,1,4,1,24681,1,2,18,10,1,1),_JBODHdIndex8_Type())
jBODHdIndex8.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdIndex8.setStatus(_A)
class _JBODHdDescr8_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JBODHdDescr8_Type.__name__=_C
_JBODHdDescr8_Object=MibTableColumn
jBODHdDescr8=_JBODHdDescr8_Object((1,3,6,1,4,1,24681,1,2,18,10,1,2),_JBODHdDescr8_Type())
jBODHdDescr8.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdDescr8.setStatus(_A)
_JBODHdTemperature8_Type=DisplayString
_JBODHdTemperature8_Object=MibTableColumn
jBODHdTemperature8=_JBODHdTemperature8_Object((1,3,6,1,4,1,24681,1,2,18,10,1,3),_JBODHdTemperature8_Type())
jBODHdTemperature8.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdTemperature8.setStatus(_A)
class _JBODHdStatus8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_JBODHdStatus8_Type.__name__=_E
_JBODHdStatus8_Object=MibTableColumn
jBODHdStatus8=_JBODHdStatus8_Object((1,3,6,1,4,1,24681,1,2,18,10,1,4),_JBODHdStatus8_Type())
jBODHdStatus8.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdStatus8.setStatus(_A)
_JBODHdModel8_Type=DisplayString
_JBODHdModel8_Object=MibTableColumn
jBODHdModel8=_JBODHdModel8_Object((1,3,6,1,4,1,24681,1,2,18,10,1,5),_JBODHdModel8_Type())
jBODHdModel8.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdModel8.setStatus(_A)
_JBODHdCapacity8_Type=DisplayString
_JBODHdCapacity8_Object=MibTableColumn
jBODHdCapacity8=_JBODHdCapacity8_Object((1,3,6,1,4,1,24681,1,2,18,10,1,6),_JBODHdCapacity8_Type())
jBODHdCapacity8.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdCapacity8.setStatus(_A)
_JBODHdSmartInfo8_Type=DisplayString
_JBODHdSmartInfo8_Object=MibTableColumn
jBODHdSmartInfo8=_JBODHdSmartInfo8_Object((1,3,6,1,4,1,24681,1,2,18,10,1,7),_JBODHdSmartInfo8_Type())
jBODHdSmartInfo8.setMaxAccess(_B)
if mibBuilder.loadTexts:jBODHdSmartInfo8.setStatus(_A)
_SystemInfoEx_ObjectIdentity=ObjectIdentity
systemInfoEx=_SystemInfoEx_ObjectIdentity((1,3,6,1,4,1,24681,1,3))
_SystemCPU_UsageEX_Type=Integer32
_SystemCPU_UsageEX_Object=MibScalar
systemCPU_UsageEX=_SystemCPU_UsageEX_Object((1,3,6,1,4,1,24681,1,3,1),_SystemCPU_UsageEX_Type())
systemCPU_UsageEX.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCPU_UsageEX.setStatus(_A)
_SystemTotalMemEX_Type=Counter64
_SystemTotalMemEX_Object=MibScalar
systemTotalMemEX=_SystemTotalMemEX_Object((1,3,6,1,4,1,24681,1,3,2),_SystemTotalMemEX_Type())
systemTotalMemEX.setMaxAccess(_B)
if mibBuilder.loadTexts:systemTotalMemEX.setStatus(_A)
_SystemFreeMemEX_Type=Counter64
_SystemFreeMemEX_Object=MibScalar
systemFreeMemEX=_SystemFreeMemEX_Object((1,3,6,1,4,1,24681,1,3,3),_SystemFreeMemEX_Type())
systemFreeMemEX.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFreeMemEX.setStatus(_A)
_SystemUptimeEX_Type=TimeTicks
_SystemUptimeEX_Object=MibScalar
systemUptimeEX=_SystemUptimeEX_Object((1,3,6,1,4,1,24681,1,3,4),_SystemUptimeEX_Type())
systemUptimeEX.setMaxAccess(_B)
if mibBuilder.loadTexts:systemUptimeEX.setStatus(_A)
_Cpu_TemperatureEX_Type=Integer32
_Cpu_TemperatureEX_Object=MibScalar
cpu_TemperatureEX=_Cpu_TemperatureEX_Object((1,3,6,1,4,1,24681,1,3,5),_Cpu_TemperatureEX_Type())
cpu_TemperatureEX.setMaxAccess(_B)
if mibBuilder.loadTexts:cpu_TemperatureEX.setStatus(_A)
_SystemTemperatureEX_Type=Integer32
_SystemTemperatureEX_Object=MibScalar
systemTemperatureEX=_SystemTemperatureEX_Object((1,3,6,1,4,1,24681,1,3,6),_SystemTemperatureEX_Type())
systemTemperatureEX.setMaxAccess(_B)
if mibBuilder.loadTexts:systemTemperatureEX.setStatus(_A)
_IfNumberEX_Type=Integer32
_IfNumberEX_Object=MibScalar
ifNumberEX=_IfNumberEX_Object((1,3,6,1,4,1,24681,1,3,8),_IfNumberEX_Type())
ifNumberEX.setMaxAccess(_B)
if mibBuilder.loadTexts:ifNumberEX.setStatus(_A)
_SystemIfTableEx_Object=MibTable
systemIfTableEx=_SystemIfTableEx_Object((1,3,6,1,4,1,24681,1,3,9))
if mibBuilder.loadTexts:systemIfTableEx.setStatus(_A)
_IfEntryEx_Object=MibTableRow
ifEntryEx=_IfEntryEx_Object((1,3,6,1,4,1,24681,1,3,9,1))
ifEntryEx.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:ifEntryEx.setStatus(_A)
_IfIndexEX_Type=Integer32
_IfIndexEX_Object=MibTableColumn
ifIndexEX=_IfIndexEX_Object((1,3,6,1,4,1,24681,1,3,9,1,1),_IfIndexEX_Type())
ifIndexEX.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIndexEX.setStatus(_A)
class _IfDescrEX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfDescrEX_Type.__name__=_C
_IfDescrEX_Object=MibTableColumn
ifDescrEX=_IfDescrEX_Object((1,3,6,1,4,1,24681,1,3,9,1,2),_IfDescrEX_Type())
ifDescrEX.setMaxAccess(_B)
if mibBuilder.loadTexts:ifDescrEX.setStatus(_A)
_IfPacketsReceivedEX_Type=Counter32
_IfPacketsReceivedEX_Object=MibTableColumn
ifPacketsReceivedEX=_IfPacketsReceivedEX_Object((1,3,6,1,4,1,24681,1,3,9,1,3),_IfPacketsReceivedEX_Type())
ifPacketsReceivedEX.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPacketsReceivedEX.setStatus(_A)
_IfPacketsSentEX_Type=Counter32
_IfPacketsSentEX_Object=MibTableColumn
ifPacketsSentEX=_IfPacketsSentEX_Object((1,3,6,1,4,1,24681,1,3,9,1,4),_IfPacketsSentEX_Type())
ifPacketsSentEX.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPacketsSentEX.setStatus(_A)
_IfErrorPacketsEX_Type=Counter32
_IfErrorPacketsEX_Object=MibTableColumn
ifErrorPacketsEX=_IfErrorPacketsEX_Object((1,3,6,1,4,1,24681,1,3,9,1,5),_IfErrorPacketsEX_Type())
ifErrorPacketsEX.setMaxAccess(_B)
if mibBuilder.loadTexts:ifErrorPacketsEX.setStatus(_A)
_HdNumberEX_Type=Integer32
_HdNumberEX_Object=MibScalar
hdNumberEX=_HdNumberEX_Object((1,3,6,1,4,1,24681,1,3,10),_HdNumberEX_Type())
hdNumberEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdNumberEX.setStatus(_A)
_SystemHdTableEX_Object=MibTable
systemHdTableEX=_SystemHdTableEX_Object((1,3,6,1,4,1,24681,1,3,11))
if mibBuilder.loadTexts:systemHdTableEX.setStatus(_A)
_HdEntryEx_Object=MibTableRow
hdEntryEx=_HdEntryEx_Object((1,3,6,1,4,1,24681,1,3,11,1))
hdEntryEx.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:hdEntryEx.setStatus(_A)
_HdIndexEX_Type=Integer32
_HdIndexEX_Object=MibTableColumn
hdIndexEX=_HdIndexEX_Object((1,3,6,1,4,1,24681,1,3,11,1,1),_HdIndexEX_Type())
hdIndexEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdIndexEX.setStatus(_A)
class _HdDescrEX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HdDescrEX_Type.__name__=_C
_HdDescrEX_Object=MibTableColumn
hdDescrEX=_HdDescrEX_Object((1,3,6,1,4,1,24681,1,3,11,1,2),_HdDescrEX_Type())
hdDescrEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdDescrEX.setStatus(_A)
_HdTemperatureEX_Type=Integer32
_HdTemperatureEX_Object=MibTableColumn
hdTemperatureEX=_HdTemperatureEX_Object((1,3,6,1,4,1,24681,1,3,11,1,3),_HdTemperatureEX_Type())
hdTemperatureEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdTemperatureEX.setStatus(_A)
class _HdStatusEX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*((_G,-9),(_H,-6),(_I,-5),(_J,-4),(_F,0)))
_HdStatusEX_Type.__name__=_E
_HdStatusEX_Object=MibTableColumn
hdStatusEX=_HdStatusEX_Object((1,3,6,1,4,1,24681,1,3,11,1,4),_HdStatusEX_Type())
hdStatusEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdStatusEX.setStatus(_A)
_HdModelEX_Type=DisplayString
_HdModelEX_Object=MibTableColumn
hdModelEX=_HdModelEX_Object((1,3,6,1,4,1,24681,1,3,11,1,5),_HdModelEX_Type())
hdModelEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdModelEX.setStatus(_A)
_HdCapacityEX_Type=Counter64
_HdCapacityEX_Object=MibTableColumn
hdCapacityEX=_HdCapacityEX_Object((1,3,6,1,4,1,24681,1,3,11,1,6),_HdCapacityEX_Type())
hdCapacityEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdCapacityEX.setStatus(_A)
_HdSmartInfoEX_Type=DisplayString
_HdSmartInfoEX_Object=MibTableColumn
hdSmartInfoEX=_HdSmartInfoEX_Object((1,3,6,1,4,1,24681,1,3,11,1,7),_HdSmartInfoEX_Type())
hdSmartInfoEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hdSmartInfoEX.setStatus(_A)
_ModelNameEX_Type=DisplayString
_ModelNameEX_Object=MibScalar
modelNameEX=_ModelNameEX_Object((1,3,6,1,4,1,24681,1,3,12),_ModelNameEX_Type())
modelNameEX.setMaxAccess(_B)
if mibBuilder.loadTexts:modelNameEX.setStatus(_A)
_HostNameEX_Type=DisplayString
_HostNameEX_Object=MibScalar
hostNameEX=_HostNameEX_Object((1,3,6,1,4,1,24681,1,3,13),_HostNameEX_Type())
hostNameEX.setMaxAccess(_B)
if mibBuilder.loadTexts:hostNameEX.setStatus(_A)
_SysFanNumberEX_Type=Integer32
_SysFanNumberEX_Object=MibScalar
sysFanNumberEX=_SysFanNumberEX_Object((1,3,6,1,4,1,24681,1,3,14),_SysFanNumberEX_Type())
sysFanNumberEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanNumberEX.setStatus(_A)
_SystemFanTableEx_Object=MibTable
systemFanTableEx=_SystemFanTableEx_Object((1,3,6,1,4,1,24681,1,3,15))
if mibBuilder.loadTexts:systemFanTableEx.setStatus(_A)
_SysFanEntryEx_Object=MibTableRow
sysFanEntryEx=_SysFanEntryEx_Object((1,3,6,1,4,1,24681,1,3,15,1))
sysFanEntryEx.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:sysFanEntryEx.setStatus(_A)
_SysFanIndexEX_Type=Integer32
_SysFanIndexEX_Object=MibTableColumn
sysFanIndexEX=_SysFanIndexEX_Object((1,3,6,1,4,1,24681,1,3,15,1,1),_SysFanIndexEX_Type())
sysFanIndexEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanIndexEX.setStatus(_A)
class _SysFanDescrEX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysFanDescrEX_Type.__name__=_C
_SysFanDescrEX_Object=MibTableColumn
sysFanDescrEX=_SysFanDescrEX_Object((1,3,6,1,4,1,24681,1,3,15,1,2),_SysFanDescrEX_Type())
sysFanDescrEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanDescrEX.setStatus(_A)
_SysFanSpeedEX_Type=Integer32
_SysFanSpeedEX_Object=MibTableColumn
sysFanSpeedEX=_SysFanSpeedEX_Object((1,3,6,1,4,1,24681,1,3,15,1,3),_SysFanSpeedEX_Type())
sysFanSpeedEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanSpeedEX.setStatus(_A)
_SysVolumeNumberEX_Type=Integer32
_SysVolumeNumberEX_Object=MibScalar
sysVolumeNumberEX=_SysVolumeNumberEX_Object((1,3,6,1,4,1,24681,1,3,16),_SysVolumeNumberEX_Type())
sysVolumeNumberEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeNumberEX.setStatus(_A)
_SystemVolumeTableEx_Object=MibTable
systemVolumeTableEx=_SystemVolumeTableEx_Object((1,3,6,1,4,1,24681,1,3,17))
if mibBuilder.loadTexts:systemVolumeTableEx.setStatus(_A)
_SysVolumeEntryEx_Object=MibTableRow
sysVolumeEntryEx=_SysVolumeEntryEx_Object((1,3,6,1,4,1,24681,1,3,17,1))
sysVolumeEntryEx.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:sysVolumeEntryEx.setStatus(_A)
_SysVolumeIndexEX_Type=Integer32
_SysVolumeIndexEX_Object=MibTableColumn
sysVolumeIndexEX=_SysVolumeIndexEX_Object((1,3,6,1,4,1,24681,1,3,17,1,1),_SysVolumeIndexEX_Type())
sysVolumeIndexEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeIndexEX.setStatus(_A)
class _SysVolumeDescrEX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysVolumeDescrEX_Type.__name__=_C
_SysVolumeDescrEX_Object=MibTableColumn
sysVolumeDescrEX=_SysVolumeDescrEX_Object((1,3,6,1,4,1,24681,1,3,17,1,2),_SysVolumeDescrEX_Type())
sysVolumeDescrEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeDescrEX.setStatus(_A)
class _SysVolumeFSEX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysVolumeFSEX_Type.__name__=_C
_SysVolumeFSEX_Object=MibTableColumn
sysVolumeFSEX=_SysVolumeFSEX_Object((1,3,6,1,4,1,24681,1,3,17,1,3),_SysVolumeFSEX_Type())
sysVolumeFSEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeFSEX.setStatus(_A)
_SysVolumeTotalSizeEX_Type=Counter64
_SysVolumeTotalSizeEX_Object=MibTableColumn
sysVolumeTotalSizeEX=_SysVolumeTotalSizeEX_Object((1,3,6,1,4,1,24681,1,3,17,1,4),_SysVolumeTotalSizeEX_Type())
sysVolumeTotalSizeEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeTotalSizeEX.setStatus(_A)
_SysVolumeFreeSizeEX_Type=Counter64
_SysVolumeFreeSizeEX_Object=MibTableColumn
sysVolumeFreeSizeEX=_SysVolumeFreeSizeEX_Object((1,3,6,1,4,1,24681,1,3,17,1,5),_SysVolumeFreeSizeEX_Type())
sysVolumeFreeSizeEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeFreeSizeEX.setStatus(_A)
class _SysVolumeStatusEX_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysVolumeStatusEX_Type.__name__=_C
_SysVolumeStatusEX_Object=MibTableColumn
sysVolumeStatusEX=_SysVolumeStatusEX_Object((1,3,6,1,4,1,24681,1,3,17,1,6),_SysVolumeStatusEX_Type())
sysVolumeStatusEX.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVolumeStatusEX.setStatus(_A)
_StorageSystemEx_ObjectIdentity=ObjectIdentity
storageSystemEx=_StorageSystemEx_ObjectIdentity((1,3,6,1,4,1,24681,1,4))
_SystemSettings_ObjectIdentity=ObjectIdentity
systemSettings=_SystemSettings_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1))
_StorageManager_ObjectIdentity=ObjectIdentity
storageManager=_StorageManager_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1))
_NasStorage_ObjectIdentity=ObjectIdentity
nasStorage=_NasStorage_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1))
_Components_ObjectIdentity=ObjectIdentity
components=_Components_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,1))
_Enclosure_ObjectIdentity=ObjectIdentity
enclosure=_Enclosure_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,1,1))
_EnclosurelNumber_Type=Integer32
_EnclosurelNumber_Object=MibScalar
enclosurelNumber=_EnclosurelNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,1),_EnclosurelNumber_Type())
enclosurelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosurelNumber.setStatus(_A)
_EnclosureTable_Object=MibTable
enclosureTable=_EnclosureTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2))
if mibBuilder.loadTexts:enclosureTable.setStatus(_A)
_EnclosureTableEntry_Object=MibTableRow
enclosureTableEntry=_EnclosureTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1))
enclosureTableEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:enclosureTableEntry.setStatus(_A)
_EnclosureIndex_Type=Integer32
_EnclosureIndex_Object=MibTableColumn
enclosureIndex=_EnclosureIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1,1),_EnclosureIndex_Type())
enclosureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureIndex.setStatus(_A)
_EnclosureID_Type=Integer32
_EnclosureID_Object=MibTableColumn
enclosureID=_EnclosureID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1,2),_EnclosureID_Type())
enclosureID.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureID.setStatus(_A)
class _EnclosureModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EnclosureModel_Type.__name__=_C
_EnclosureModel_Object=MibTableColumn
enclosureModel=_EnclosureModel_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1,3),_EnclosureModel_Type())
enclosureModel.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureModel.setStatus(_A)
class _EnclosureSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EnclosureSerialNum_Type.__name__=_C
_EnclosureSerialNum_Object=MibTableColumn
enclosureSerialNum=_EnclosureSerialNum_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1,4),_EnclosureSerialNum_Type())
enclosureSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureSerialNum.setStatus(_A)
_EnclosureSlot_Type=Integer32
_EnclosureSlot_Object=MibTableColumn
enclosureSlot=_EnclosureSlot_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1,5),_EnclosureSlot_Type())
enclosureSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureSlot.setStatus(_A)
_EnclosureName_Type=DisplayString
_EnclosureName_Object=MibTableColumn
enclosureName=_EnclosureName_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1,6),_EnclosureName_Type())
enclosureName.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureName.setStatus(_A)
_EnclosureSystemTemp_Type=Integer32
_EnclosureSystemTemp_Object=MibTableColumn
enclosureSystemTemp=_EnclosureSystemTemp_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,1,2,1,7),_EnclosureSystemTemp_Type())
enclosureSystemTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:enclosureSystemTemp.setStatus(_A)
_SystemFan_ObjectIdentity=ObjectIdentity
systemFan=_SystemFan_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,1,2))
_SystemFanNumber_Type=Integer32
_SystemFanNumber_Object=MibScalar
systemFanNumber=_SystemFanNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,1),_SystemFanNumber_Type())
systemFanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFanNumber.setStatus(_A)
_SystemFan2Table_Object=MibTable
systemFan2Table=_SystemFan2Table_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,2))
if mibBuilder.loadTexts:systemFan2Table.setStatus(_A)
_SystemFan2TableEntry_Object=MibTableRow
systemFan2TableEntry=_SystemFan2TableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,2,1))
systemFan2TableEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:systemFan2TableEntry.setStatus(_A)
_SystemFanIndex_Type=Integer32
_SystemFanIndex_Object=MibTableColumn
systemFanIndex=_SystemFanIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,2,1,1),_SystemFanIndex_Type())
systemFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFanIndex.setStatus(_A)
_SystemFanID_Type=Integer32
_SystemFanID_Object=MibTableColumn
systemFanID=_SystemFanID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,2,1,2),_SystemFanID_Type())
systemFanID.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFanID.setStatus(_A)
_SystemFanEnclosureID_Type=Integer32
_SystemFanEnclosureID_Object=MibTableColumn
systemFanEnclosureID=_SystemFanEnclosureID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,2,1,3),_SystemFanEnclosureID_Type())
systemFanEnclosureID.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFanEnclosureID.setStatus(_A)
class _SystemFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0)));namedValues=NamedValues(*(('fail',-1),('ok',0)))
_SystemFanStatus_Type.__name__=_E
_SystemFanStatus_Object=MibTableColumn
systemFanStatus=_SystemFanStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,2,1,4),_SystemFanStatus_Type())
systemFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFanStatus.setStatus(_A)
_SystemFanSpeed_Type=Integer32
_SystemFanSpeed_Object=MibTableColumn
systemFanSpeed=_SystemFanSpeed_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,2,2,1,5),_SystemFanSpeed_Type())
systemFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFanSpeed.setStatus(_A)
_SystemPower_ObjectIdentity=ObjectIdentity
systemPower=_SystemPower_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,1,3))
_SystemPowerNumber_Type=Integer32
_SystemPowerNumber_Object=MibScalar
systemPowerNumber=_SystemPowerNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,1),_SystemPowerNumber_Type())
systemPowerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPowerNumber.setStatus(_A)
_SystemPowerTable_Object=MibTable
systemPowerTable=_SystemPowerTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2))
if mibBuilder.loadTexts:systemPowerTable.setStatus(_A)
_SystemPowerTableEntry_Object=MibTableRow
systemPowerTableEntry=_SystemPowerTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2,1))
systemPowerTableEntry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:systemPowerTableEntry.setStatus(_A)
_SystemPowerIndex_Type=Integer32
_SystemPowerIndex_Object=MibTableColumn
systemPowerIndex=_SystemPowerIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2,1,1),_SystemPowerIndex_Type())
systemPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPowerIndex.setStatus(_A)
_SystemPowerID_Type=Integer32
_SystemPowerID_Object=MibTableColumn
systemPowerID=_SystemPowerID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2,1,2),_SystemPowerID_Type())
systemPowerID.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPowerID.setStatus(_A)
_SystemPowerEnclosureID_Type=Integer32
_SystemPowerEnclosureID_Object=MibTableColumn
systemPowerEnclosureID=_SystemPowerEnclosureID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2,1,3),_SystemPowerEnclosureID_Type())
systemPowerEnclosureID.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPowerEnclosureID.setStatus(_A)
class _SystemPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0)));namedValues=NamedValues(*(('fail',-1),('ok',0)))
_SystemPowerStatus_Type.__name__=_E
_SystemPowerStatus_Object=MibTableColumn
systemPowerStatus=_SystemPowerStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2,1,4),_SystemPowerStatus_Type())
systemPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPowerStatus.setStatus(_A)
_SystemPowerFanSpeed_Type=Integer32
_SystemPowerFanSpeed_Object=MibTableColumn
systemPowerFanSpeed=_SystemPowerFanSpeed_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2,1,5),_SystemPowerFanSpeed_Type())
systemPowerFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPowerFanSpeed.setStatus(_A)
_SystemPowerTemp_Type=Integer32
_SystemPowerTemp_Object=MibTableColumn
systemPowerTemp=_SystemPowerTemp_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,3,2,1,6),_SystemPowerTemp_Type())
systemPowerTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:systemPowerTemp.setStatus(_A)
_Cpu_ObjectIdentity=ObjectIdentity
cpu=_Cpu_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,1,4))
_CpuNumber_Type=Integer32
_CpuNumber_Object=MibScalar
cpuNumber=_CpuNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,4,1),_CpuNumber_Type())
cpuNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuNumber.setStatus(_A)
_CpuTemp_Type=Integer32
_CpuTemp_Object=MibScalar
cpuTemp=_CpuTemp_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,4,2),_CpuTemp_Type())
cpuTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuTemp.setStatus(_A)
_CpuTable_Object=MibTable
cpuTable=_CpuTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,4,3))
if mibBuilder.loadTexts:cpuTable.setStatus(_A)
_CpuTableEntry_Object=MibTableRow
cpuTableEntry=_CpuTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,4,3,1))
cpuTableEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:cpuTableEntry.setStatus(_A)
_CpuIndex_Type=Integer32
_CpuIndex_Object=MibTableColumn
cpuIndex=_CpuIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,4,3,1,1),_CpuIndex_Type())
cpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuIndex.setStatus(_A)
_CpuID_Type=Integer32
_CpuID_Object=MibTableColumn
cpuID=_CpuID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,4,3,1,2),_CpuID_Type())
cpuID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuID.setStatus(_A)
_CpuUsage_Type=Integer32
_CpuUsage_Object=MibTableColumn
cpuUsage=_CpuUsage_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,4,3,1,3),_CpuUsage_Type())
cpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUsage.setStatus(_A)
_Disk_ObjectIdentity=ObjectIdentity
disk=_Disk_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,1,5))
_DiskNumber_Type=Integer32
_DiskNumber_Object=MibScalar
diskNumber=_DiskNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,1),_DiskNumber_Type())
diskNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:diskNumber.setStatus(_A)
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2))
if mibBuilder.loadTexts:diskTable.setStatus(_A)
_DiskTableEntry_Object=MibTableRow
diskTableEntry=_DiskTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1))
diskTableEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:diskTableEntry.setStatus(_A)
_DiskIndex_Type=Integer32
_DiskIndex_Object=MibTableColumn
diskIndex=_DiskIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,1),_DiskIndex_Type())
diskIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:diskIndex.setStatus(_A)
_DiskID_Type=Integer32
_DiskID_Object=MibTableColumn
diskID=_DiskID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,2),_DiskID_Type())
diskID.setMaxAccess(_B)
if mibBuilder.loadTexts:diskID.setStatus(_A)
_DiskEnclosureID_Type=Integer32
_DiskEnclosureID_Object=MibTableColumn
diskEnclosureID=_DiskEnclosureID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,3),_DiskEnclosureID_Type())
diskEnclosureID.setMaxAccess(_B)
if mibBuilder.loadTexts:diskEnclosureID.setStatus(_A)
class _DiskSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DiskSummary_Type.__name__=_C
_DiskSummary_Object=MibTableColumn
diskSummary=_DiskSummary_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,4),_DiskSummary_Type())
diskSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:diskSummary.setStatus(_A)
class _DiskSmartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*((_N,-1),('good',0),(_O,1),(_k,2)))
_DiskSmartInfo_Type.__name__=_E
_DiskSmartInfo_Object=MibTableColumn
diskSmartInfo=_DiskSmartInfo_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,5),_DiskSmartInfo_Type())
diskSmartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:diskSmartInfo.setStatus(_A)
_DiskTemperture_Type=Integer32
_DiskTemperture_Object=MibTableColumn
diskTemperture=_DiskTemperture_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,6),_DiskTemperture_Type())
diskTemperture.setMaxAccess(_B)
if mibBuilder.loadTexts:diskTemperture.setStatus(_A)
class _DiskGlobalSpare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DiskGlobalSpare_Type.__name__=_E
_DiskGlobalSpare_Object=MibTableColumn
diskGlobalSpare=_DiskGlobalSpare_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,7),_DiskGlobalSpare_Type())
diskGlobalSpare.setMaxAccess(_B)
if mibBuilder.loadTexts:diskGlobalSpare.setStatus(_A)
class _DiskModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DiskModel_Type.__name__=_C
_DiskModel_Object=MibTableColumn
diskModel=_DiskModel_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,8),_DiskModel_Type())
diskModel.setMaxAccess(_B)
if mibBuilder.loadTexts:diskModel.setStatus(_A)
_DiskCapacity_Type=Counter64
_DiskCapacity_Object=MibTableColumn
diskCapacity=_DiskCapacity_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,5,2,1,9),_DiskCapacity_Type())
diskCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:diskCapacity.setStatus(_A)
_MsataDisk_ObjectIdentity=ObjectIdentity
msataDisk=_MsataDisk_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,1,6))
_MsataDiskNumber_Type=Integer32
_MsataDiskNumber_Object=MibScalar
msataDiskNumber=_MsataDiskNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,1),_MsataDiskNumber_Type())
msataDiskNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskNumber.setStatus(_A)
_MsataDiskTable_Object=MibTable
msataDiskTable=_MsataDiskTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2))
if mibBuilder.loadTexts:msataDiskTable.setStatus(_A)
_MsataDiskTableEntry_Object=MibTableRow
msataDiskTableEntry=_MsataDiskTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1))
msataDiskTableEntry.setIndexNames((0,_D,_l))
if mibBuilder.loadTexts:msataDiskTableEntry.setStatus(_A)
_MsataDiskIndex_Type=Integer32
_MsataDiskIndex_Object=MibTableColumn
msataDiskIndex=_MsataDiskIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,1),_MsataDiskIndex_Type())
msataDiskIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskIndex.setStatus(_A)
_MsataDiskID_Type=Integer32
_MsataDiskID_Object=MibTableColumn
msataDiskID=_MsataDiskID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,2),_MsataDiskID_Type())
msataDiskID.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskID.setStatus(_A)
_MsataDiskEnclosureID_Type=Integer32
_MsataDiskEnclosureID_Object=MibTableColumn
msataDiskEnclosureID=_MsataDiskEnclosureID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,3),_MsataDiskEnclosureID_Type())
msataDiskEnclosureID.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskEnclosureID.setStatus(_A)
class _MsataDiskSummary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsataDiskSummary_Type.__name__=_C
_MsataDiskSummary_Object=MibTableColumn
msataDiskSummary=_MsataDiskSummary_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,4),_MsataDiskSummary_Type())
msataDiskSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskSummary.setStatus(_A)
class _MsataDiskSmartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*((_N,-1),('good',0),(_O,1),(_k,2)))
_MsataDiskSmartInfo_Type.__name__=_E
_MsataDiskSmartInfo_Object=MibTableColumn
msataDiskSmartInfo=_MsataDiskSmartInfo_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,5),_MsataDiskSmartInfo_Type())
msataDiskSmartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskSmartInfo.setStatus(_A)
_MsataDiskTemperture_Type=Integer32
_MsataDiskTemperture_Object=MibTableColumn
msataDiskTemperture=_MsataDiskTemperture_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,6),_MsataDiskTemperture_Type())
msataDiskTemperture.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskTemperture.setStatus(_A)
class _MsataDiskGlobalSpare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_MsataDiskGlobalSpare_Type.__name__=_E
_MsataDiskGlobalSpare_Object=MibTableColumn
msataDiskGlobalSpare=_MsataDiskGlobalSpare_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,7),_MsataDiskGlobalSpare_Type())
msataDiskGlobalSpare.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskGlobalSpare.setStatus(_A)
class _MsataDiskModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsataDiskModel_Type.__name__=_C
_MsataDiskModel_Object=MibTableColumn
msataDiskModel=_MsataDiskModel_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,8),_MsataDiskModel_Type())
msataDiskModel.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskModel.setStatus(_A)
_MsataDiskCapacity_Type=Counter64
_MsataDiskCapacity_Object=MibTableColumn
msataDiskCapacity=_MsataDiskCapacity_Object((1,3,6,1,4,1,24681,1,4,1,1,1,1,6,2,1,9),_MsataDiskCapacity_Type())
msataDiskCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:msataDiskCapacity.setStatus(_A)
_StorageSpace_ObjectIdentity=ObjectIdentity
storageSpace=_StorageSpace_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,2))
_Raid_ObjectIdentity=ObjectIdentity
raid=_Raid_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,2,1))
_RaidNumber_Type=Integer32
_RaidNumber_Object=MibScalar
raidNumber=_RaidNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,1),_RaidNumber_Type())
raidNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:raidNumber.setStatus(_A)
_RaidGroupTable_Object=MibTable
raidGroupTable=_RaidGroupTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2))
if mibBuilder.loadTexts:raidGroupTable.setStatus(_A)
_RaidGroupTableEntry_Object=MibTableRow
raidGroupTableEntry=_RaidGroupTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1))
raidGroupTableEntry.setIndexNames((0,_D,_m))
if mibBuilder.loadTexts:raidGroupTableEntry.setStatus(_A)
_RaidIndex_Type=Integer32
_RaidIndex_Object=MibTableColumn
raidIndex=_RaidIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1,1),_RaidIndex_Type())
raidIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raidIndex.setStatus(_A)
_RaidID_Type=Integer32
_RaidID_Object=MibTableColumn
raidID=_RaidID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1,2),_RaidID_Type())
raidID.setMaxAccess(_B)
if mibBuilder.loadTexts:raidID.setStatus(_A)
_RaidCapacity_Type=Counter64
_RaidCapacity_Object=MibTableColumn
raidCapacity=_RaidCapacity_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1,3),_RaidCapacity_Type())
raidCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:raidCapacity.setStatus(_A)
_RaidFreeSize_Type=Counter64
_RaidFreeSize_Object=MibTableColumn
raidFreeSize=_RaidFreeSize_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1,4),_RaidFreeSize_Type())
raidFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raidFreeSize.setStatus(_A)
class _RaidStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RaidStatus_Type.__name__=_C
_RaidStatus_Object=MibTableColumn
raidStatus=_RaidStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1,5),_RaidStatus_Type())
raidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raidStatus.setStatus(_A)
class _RaidBitmap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_RaidBitmap_Type.__name__=_E
_RaidBitmap_Object=MibTableColumn
raidBitmap=_RaidBitmap_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1,6),_RaidBitmap_Type())
raidBitmap.setMaxAccess(_B)
if mibBuilder.loadTexts:raidBitmap.setStatus(_A)
class _RaidLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RaidLevel_Type.__name__=_C
_RaidLevel_Object=MibTableColumn
raidLevel=_RaidLevel_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,1,2,1,7),_RaidLevel_Type())
raidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:raidLevel.setStatus(_A)
_Pool_ObjectIdentity=ObjectIdentity
pool=_Pool_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,2,2))
_PoolNumber_Type=Integer32
_PoolNumber_Object=MibScalar
poolNumber=_PoolNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,1),_PoolNumber_Type())
poolNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:poolNumber.setStatus(_A)
_PoolTable_Object=MibTable
poolTable=_PoolTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,2))
if mibBuilder.loadTexts:poolTable.setStatus(_A)
_PoolTableEntry_Object=MibTableRow
poolTableEntry=_PoolTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,2,1))
poolTableEntry.setIndexNames((0,_D,_n))
if mibBuilder.loadTexts:poolTableEntry.setStatus(_A)
_PoolIndex_Type=Integer32
_PoolIndex_Object=MibTableColumn
poolIndex=_PoolIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,2,1,1),_PoolIndex_Type())
poolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:poolIndex.setStatus(_A)
_PoolID_Type=Integer32
_PoolID_Object=MibTableColumn
poolID=_PoolID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,2,1,2),_PoolID_Type())
poolID.setMaxAccess(_B)
if mibBuilder.loadTexts:poolID.setStatus(_A)
_PoolCapacity_Type=Counter64
_PoolCapacity_Object=MibTableColumn
poolCapacity=_PoolCapacity_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,2,1,3),_PoolCapacity_Type())
poolCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:poolCapacity.setStatus(_A)
_PoolFreeSize_Type=Counter64
_PoolFreeSize_Object=MibTableColumn
poolFreeSize=_PoolFreeSize_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,2,1,4),_PoolFreeSize_Type())
poolFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:poolFreeSize.setStatus(_A)
class _PoolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-3,-2,-1,0)));namedValues=NamedValues(*((_N,-3),('notReady',-2),(_O,-1),(_F,0)))
_PoolStatus_Type.__name__=_E
_PoolStatus_Object=MibTableColumn
poolStatus=_PoolStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,2,2,1,5),_PoolStatus_Type())
poolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:poolStatus.setStatus(_A)
_Volume_ObjectIdentity=ObjectIdentity
volume=_Volume_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,2,3))
_VolumeNumber_Type=Integer32
_VolumeNumber_Object=MibScalar
volumeNumber=_VolumeNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,1),_VolumeNumber_Type())
volumeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeNumber.setStatus(_A)
_VolumeTable_Object=MibTable
volumeTable=_VolumeTable_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2))
if mibBuilder.loadTexts:volumeTable.setStatus(_A)
_VolumeTableEntry_Object=MibTableRow
volumeTableEntry=_VolumeTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1))
volumeTableEntry.setIndexNames((0,_D,_o))
if mibBuilder.loadTexts:volumeTableEntry.setStatus(_A)
_VolumeIndex_Type=Integer32
_VolumeIndex_Object=MibTableColumn
volumeIndex=_VolumeIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,1),_VolumeIndex_Type())
volumeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeIndex.setStatus(_A)
_VolumeID_Type=Integer32
_VolumeID_Object=MibTableColumn
volumeID=_VolumeID_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,2),_VolumeID_Type())
volumeID.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeID.setStatus(_A)
_VolumeCapacity_Type=Counter64
_VolumeCapacity_Object=MibTableColumn
volumeCapacity=_VolumeCapacity_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,3),_VolumeCapacity_Type())
volumeCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeCapacity.setStatus(_A)
_VolumeFreeSize_Type=Counter64
_VolumeFreeSize_Object=MibTableColumn
volumeFreeSize=_VolumeFreeSize_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,4),_VolumeFreeSize_Type())
volumeFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeFreeSize.setStatus(_A)
class _VolumeStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VolumeStatus_Type.__name__=_C
_VolumeStatus_Object=MibTableColumn
volumeStatus=_VolumeStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,5),_VolumeStatus_Type())
volumeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeStatus.setStatus(_A)
class _VolumeSSDCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_VolumeSSDCache_Type.__name__=_E
_VolumeSSDCache_Object=MibTableColumn
volumeSSDCache=_VolumeSSDCache_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,6),_VolumeSSDCache_Type())
volumeSSDCache.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeSSDCache.setStatus(_A)
class _VolumeThin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_VolumeThin_Type.__name__=_E
_VolumeThin_Object=MibTableColumn
volumeThin=_VolumeThin_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,7),_VolumeThin_Type())
volumeThin.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeThin.setStatus(_A)
class _VolumeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VolumeName_Type.__name__=_C
_VolumeName_Object=MibTableColumn
volumeName=_VolumeName_Object((1,3,6,1,4,1,24681,1,4,1,1,1,2,3,2,1,8),_VolumeName_Type())
volumeName.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeName.setStatus(_A)
_CacheAcceleration_ObjectIdentity=ObjectIdentity
cacheAcceleration=_CacheAcceleration_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,1,3))
class _Service_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_Service_Type.__name__=_E
_Service_Object=MibScalar
service=_Service_Object((1,3,6,1,4,1,24681,1,4,1,1,1,3,1),_Service_Type())
service.setMaxAccess(_B)
if mibBuilder.loadTexts:service.setStatus(_A)
_AvailablePercent_Type=Integer32
_AvailablePercent_Object=MibScalar
availablePercent=_AvailablePercent_Object((1,3,6,1,4,1,24681,1,4,1,1,1,3,2),_AvailablePercent_Type())
availablePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:availablePercent.setStatus(_A)
_ReadHitRate_Type=Integer32
_ReadHitRate_Object=MibScalar
readHitRate=_ReadHitRate_Object((1,3,6,1,4,1,24681,1,4,1,1,1,3,3),_ReadHitRate_Type())
readHitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:readHitRate.setStatus(_A)
_WriteHitRate_Type=Integer32
_WriteHitRate_Object=MibScalar
writeHitRate=_WriteHitRate_Object((1,3,6,1,4,1,24681,1,4,1,1,1,3,4),_WriteHitRate_Type())
writeHitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:writeHitRate.setStatus(_A)
class _Status_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Status_Type.__name__=_C
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,24681,1,4,1,1,1,3,5),_Status_Type())
status.setMaxAccess(_B)
if mibBuilder.loadTexts:status.setStatus(_A)
_ISCSI_ObjectIdentity=ObjectIdentity
iSCSI=_ISCSI_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,2))
_ISCSIStorage_ObjectIdentity=ObjectIdentity
iSCSIStorage=_ISCSIStorage_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,2,1))
class _ISCSIService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ISCSIService_Type.__name__=_E
_ISCSIService_Object=MibScalar
iSCSIService=_ISCSIService_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,1),_ISCSIService_Type())
iSCSIService.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSIService.setStatus(_A)
_ISCSIServicePort_Type=Integer32
_ISCSIServicePort_Object=MibScalar
iSCSIServicePort=_ISCSIServicePort_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,2),_ISCSIServicePort_Type())
iSCSIServicePort.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSIServicePort.setStatus(_A)
class _ISNSService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ISNSService_Type.__name__=_E
_ISNSService_Object=MibScalar
iSNSService=_ISNSService_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,3),_ISNSService_Type())
iSNSService.setMaxAccess(_B)
if mibBuilder.loadTexts:iSNSService.setStatus(_A)
_ISNSIP_Type=IpAddress
_ISNSIP_Object=MibScalar
iSNSIP=_ISNSIP_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,4),_ISNSIP_Type())
iSNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:iSNSIP.setStatus(_A)
_Lun_ObjectIdentity=ObjectIdentity
lun=_Lun_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,2,1,10))
_LunNumber_Type=Integer32
_LunNumber_Object=MibScalar
lunNumber=_LunNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,1),_LunNumber_Type())
lunNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lunNumber.setStatus(_A)
_LunTable_Object=MibTable
lunTable=_LunTable_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2))
if mibBuilder.loadTexts:lunTable.setStatus(_A)
_LunTableEntry_Object=MibTableRow
lunTableEntry=_LunTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1))
lunTableEntry.setIndexNames((0,_D,_p))
if mibBuilder.loadTexts:lunTableEntry.setStatus(_A)
_LunIndex_Type=Integer32
_LunIndex_Object=MibTableColumn
lunIndex=_LunIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,1),_LunIndex_Type())
lunIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lunIndex.setStatus(_A)
_LunID_Type=Integer32
_LunID_Object=MibTableColumn
lunID=_LunID_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,2),_LunID_Type())
lunID.setMaxAccess(_B)
if mibBuilder.loadTexts:lunID.setStatus(_A)
_LunCapacity_Type=Counter64
_LunCapacity_Object=MibTableColumn
lunCapacity=_LunCapacity_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,3),_LunCapacity_Type())
lunCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lunCapacity.setStatus(_A)
_LunUsedPercent_Type=Integer32
_LunUsedPercent_Object=MibTableColumn
lunUsedPercent=_LunUsedPercent_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,4),_LunUsedPercent_Type())
lunUsedPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:lunUsedPercent.setStatus(_A)
class _LunStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LunStatus_Type.__name__=_C
_LunStatus_Object=MibTableColumn
lunStatus=_LunStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,5),_LunStatus_Type())
lunStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lunStatus.setStatus(_A)
class _LunName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LunName_Type.__name__=_C
_LunName_Object=MibTableColumn
lunName=_LunName_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,6),_LunName_Type())
lunName.setMaxAccess(_B)
if mibBuilder.loadTexts:lunName.setStatus(_A)
class _LunBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('backup',1),('restore',2),('snapshot',3)))
_LunBackupStatus_Type.__name__=_E
_LunBackupStatus_Object=MibTableColumn
lunBackupStatus=_LunBackupStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,7),_LunBackupStatus_Type())
lunBackupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lunBackupStatus.setStatus(_A)
class _LunIsMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unmapped',0),('mapped',1)))
_LunIsMap_Type.__name__=_E
_LunIsMap_Object=MibTableColumn
lunIsMap=_LunIsMap_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,10,2,1,8),_LunIsMap_Type())
lunIsMap.setMaxAccess(_B)
if mibBuilder.loadTexts:lunIsMap.setStatus(_A)
_Target_ObjectIdentity=ObjectIdentity
target=_Target_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,1,2,1,11))
_TargetNumber_Type=Integer32
_TargetNumber_Object=MibScalar
targetNumber=_TargetNumber_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,1),_TargetNumber_Type())
targetNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:targetNumber.setStatus(_A)
_TargeTable_Object=MibTable
targeTable=_TargeTable_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,2))
if mibBuilder.loadTexts:targeTable.setStatus(_A)
_TargeTableEntry_Object=MibTableRow
targeTableEntry=_TargeTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,2,1))
targeTableEntry.setIndexNames((0,_D,_q))
if mibBuilder.loadTexts:targeTableEntry.setStatus(_A)
_TargetIndex_Type=Integer32
_TargetIndex_Object=MibTableColumn
targetIndex=_TargetIndex_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,2,1,1),_TargetIndex_Type())
targetIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:targetIndex.setStatus(_A)
_TargetID_Type=Integer32
_TargetID_Object=MibTableColumn
targetID=_TargetID_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,2,1,2),_TargetID_Type())
targetID.setMaxAccess(_B)
if mibBuilder.loadTexts:targetID.setStatus(_A)
class _TargetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TargetName_Type.__name__=_C
_TargetName_Object=MibTableColumn
targetName=_TargetName_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,2,1,3),_TargetName_Type())
targetName.setMaxAccess(_B)
if mibBuilder.loadTexts:targetName.setStatus(_A)
class _TargetIQN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TargetIQN_Type.__name__=_C
_TargetIQN_Object=MibTableColumn
targetIQN=_TargetIQN_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,2,1,4),_TargetIQN_Type())
targetIQN.setMaxAccess(_B)
if mibBuilder.loadTexts:targetIQN.setStatus(_A)
class _TargetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*(('offline',-1),(_F,0),('connected',1)))
_TargetStatus_Type.__name__=_E
_TargetStatus_Object=MibTableColumn
targetStatus=_TargetStatus_Object((1,3,6,1,4,1,24681,1,4,1,1,2,1,11,2,1,5),_TargetStatus_Type())
targetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:targetStatus.setStatus(_A)
_SystemStatus_ObjectIdentity=ObjectIdentity
systemStatus=_SystemStatus_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,11))
_ResourceMonitor_ObjectIdentity=ObjectIdentity
resourceMonitor=_ResourceMonitor_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,11,5))
_DiskPerformance_ObjectIdentity=ObjectIdentity
diskPerformance=_DiskPerformance_ObjectIdentity((1,3,6,1,4,1,24681,1,4,1,11,5,6))
_DiskPerformanceNumber_Type=Integer32
_DiskPerformanceNumber_Object=MibScalar
diskPerformanceNumber=_DiskPerformanceNumber_Object((1,3,6,1,4,1,24681,1,4,1,11,5,6,1),_DiskPerformanceNumber_Type())
diskPerformanceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:diskPerformanceNumber.setStatus(_A)
_DiskPerformanceTable_Object=MibTable
diskPerformanceTable=_DiskPerformanceTable_Object((1,3,6,1,4,1,24681,1,4,1,11,5,6,2))
if mibBuilder.loadTexts:diskPerformanceTable.setStatus(_A)
_DiskPerformanceTableEntry_Object=MibTableRow
diskPerformanceTableEntry=_DiskPerformanceTableEntry_Object((1,3,6,1,4,1,24681,1,4,1,11,5,6,2,1))
diskPerformanceTableEntry.setIndexNames((0,_D,_r))
if mibBuilder.loadTexts:diskPerformanceTableEntry.setStatus(_A)
_DiskPerformanceIndex_Type=Integer32
_DiskPerformanceIndex_Object=MibTableColumn
diskPerformanceIndex=_DiskPerformanceIndex_Object((1,3,6,1,4,1,24681,1,4,1,11,5,6,2,1,1),_DiskPerformanceIndex_Type())
diskPerformanceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:diskPerformanceIndex.setStatus(_A)
_BlvID_Type=Integer32
_BlvID_Object=MibTableColumn
blvID=_BlvID_Object((1,3,6,1,4,1,24681,1,4,1,11,5,6,2,1,2),_BlvID_Type())
blvID.setMaxAccess(_B)
if mibBuilder.loadTexts:blvID.setStatus(_A)
_Iops_Type=Integer32
_Iops_Object=MibTableColumn
iops=_Iops_Object((1,3,6,1,4,1,24681,1,4,1,11,5,6,2,1,3),_Iops_Type())
iops.setMaxAccess(_B)
if mibBuilder.loadTexts:iops.setStatus(_A)
_Latency_Type=Integer32
_Latency_Object=MibTableColumn
latency=_Latency_Object((1,3,6,1,4,1,24681,1,4,1,11,5,6,2,1,4),_Latency_Type())
latency.setMaxAccess(_B)
if mibBuilder.loadTexts:latency.setStatus(_A)
_SystemTraps_ObjectIdentity=ObjectIdentity
systemTraps=_SystemTraps_ObjectIdentity((1,3,6,1,4,1,24681,1,10))
eventInform=NotificationType((1,3,6,1,4,1,24681,1,10,1))
eventInform.setObjects((_D,_s))
if mibBuilder.loadTexts:eventInform.setStatus(_A)
eventWarning=NotificationType((1,3,6,1,4,1,24681,1,10,2))
eventWarning.setObjects((_D,_t))
if mibBuilder.loadTexts:eventWarning.setStatus(_A)
eventError=NotificationType((1,3,6,1,4,1,24681,1,10,4))
eventError.setObjects((_D,_u))
if mibBuilder.loadTexts:eventError.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_C:DisplayString,'storage':storage,'storageSystem':storageSystem,'systemEventMsg':systemEventMsg,_s:eventInformMsg,_t:eventWarningMsg,_u:eventErrorMsg,'systemInfo':systemInfo,'systemCPU-Usage':systemCPU_Usage,'systemTotalMem':systemTotalMem,'systemFreeMem':systemFreeMem,'systemUptime':systemUptime,'cpu-Temperature':cpu_Temperature,'systemTemperature':systemTemperature,'ifNumber':ifNumber,'systemIfTable':systemIfTable,'ifEntry':ifEntry,_Q:ifIndex,'ifDescr':ifDescr,'ifPacketsReceived':ifPacketsReceived,'ifPacketsSent':ifPacketsSent,'ifErrorPackets':ifErrorPackets,'hdNumber':hdNumber,'systemHdTable':systemHdTable,'hdEntry':hdEntry,_M:hdIndex,'hdDescr':hdDescr,'hdTemperature':hdTemperature,'hdStatus':hdStatus,'hdModel':hdModel,'hdCapacity':hdCapacity,'hdSmartInfo':hdSmartInfo,'modelName':modelName,'hostName':hostName,'sysFanNumber':sysFanNumber,'systemFanTable':systemFanTable,'sysFanEntry':sysFanEntry,_R:sysFanIndex,'sysFanDescr':sysFanDescr,'sysFanSpeed':sysFanSpeed,'sysVolumeNumber':sysVolumeNumber,'systemVolumeTable':systemVolumeTable,'sysVolumeEntry':sysVolumeEntry,_S:sysVolumeIndex,'sysVolumeDescr':sysVolumeDescr,'sysVolumeFS':sysVolumeFS,'sysVolumeTotalSize':sysVolumeTotalSize,'sysVolumeFreeSize':sysVolumeFreeSize,'sysVolumeStatus':sysVolumeStatus,'jBODInfo':jBODInfo,'jBODBitmap':jBODBitmap,'jBODInfos':jBODInfos,'jBODInfosEntry':jBODInfosEntry,_T:jBODid,'jBODHdNumber':jBODHdNumber,'jBODHdTable1':jBODHdTable1,'jBODHdEntry1':jBODHdEntry1,_U:jBODHdIndex1,'jBODHdDescr1':jBODHdDescr1,'jBODHdTemperature1':jBODHdTemperature1,'jBODHdStatus1':jBODHdStatus1,'jBODHdModel1':jBODHdModel1,'jBODHdCapacity1':jBODHdCapacity1,'jBODHdSmartInfo1':jBODHdSmartInfo1,'jBODHdTable2':jBODHdTable2,'jBODHdEntry2':jBODHdEntry2,_V:jBODHdIndex2,'jBODHdDescr2':jBODHdDescr2,'jBODHdTemperature2':jBODHdTemperature2,'jBODHdStatus2':jBODHdStatus2,'jBODHdModel2':jBODHdModel2,'jBODHdCapacity2':jBODHdCapacity2,'jBODHdSmartInfo2':jBODHdSmartInfo2,'jBODHdTable3':jBODHdTable3,'jBODHdEntry3':jBODHdEntry3,_W:jBODHdIndex3,'jBODHdDescr3':jBODHdDescr3,'jBODHdTemperature3':jBODHdTemperature3,'jBODHdStatus3':jBODHdStatus3,'jBODHdModel3':jBODHdModel3,'jBODHdCapacity3':jBODHdCapacity3,'jBODHdSmartInfo3':jBODHdSmartInfo3,'jBODHdTable4':jBODHdTable4,'jBODHdEntry4':jBODHdEntry4,_X:jBODHdIndex4,'jBODHdDescr4':jBODHdDescr4,'jBODHdTemperature4':jBODHdTemperature4,'jBODHdStatus4':jBODHdStatus4,'jBODHdModel4':jBODHdModel4,'jBODHdCapacity4':jBODHdCapacity4,'jBODHdSmartInfo4':jBODHdSmartInfo4,'jBODHdTable5':jBODHdTable5,'jBODHdEntry5':jBODHdEntry5,_Y:jBODHdIndex5,'jBODHdDescr5':jBODHdDescr5,'jBODHdTemperature5':jBODHdTemperature5,'jBODHdStatus5':jBODHdStatus5,'jBODHdModel5':jBODHdModel5,'jBODHdCapacity5':jBODHdCapacity5,'jBODHdSmartInfo5':jBODHdSmartInfo5,'jBODHdTable6':jBODHdTable6,'jBODHdEntry6':jBODHdEntry6,_Z:jBODHdIndex6,'jBODHdDescr6':jBODHdDescr6,'jBODHdTemperature6':jBODHdTemperature6,'jBODHdStatus6':jBODHdStatus6,'jBODHdModel6':jBODHdModel6,'jBODHdCapacity6':jBODHdCapacity6,'jBODHdSmartInfo6':jBODHdSmartInfo6,'jBODHdTable7':jBODHdTable7,'jBODHdEntry7':jBODHdEntry7,_a:jBODHdIndex7,'jBODHdDescr7':jBODHdDescr7,'jBODHdTemperature7':jBODHdTemperature7,'jBODHdStatus7':jBODHdStatus7,'jBODHdModel7':jBODHdModel7,'jBODHdCapacity7':jBODHdCapacity7,'jBODHdSmartInfo7':jBODHdSmartInfo7,'jBODHdTable8':jBODHdTable8,'jBODHdEntry8':jBODHdEntry8,_b:jBODHdIndex8,'jBODHdDescr8':jBODHdDescr8,'jBODHdTemperature8':jBODHdTemperature8,'jBODHdStatus8':jBODHdStatus8,'jBODHdModel8':jBODHdModel8,'jBODHdCapacity8':jBODHdCapacity8,'jBODHdSmartInfo8':jBODHdSmartInfo8,'systemInfoEx':systemInfoEx,'systemCPU-UsageEX':systemCPU_UsageEX,'systemTotalMemEX':systemTotalMemEX,'systemFreeMemEX':systemFreeMemEX,'systemUptimeEX':systemUptimeEX,'cpu-TemperatureEX':cpu_TemperatureEX,'systemTemperatureEX':systemTemperatureEX,'ifNumberEX':ifNumberEX,'systemIfTableEx':systemIfTableEx,'ifEntryEx':ifEntryEx,_c:ifIndexEX,'ifDescrEX':ifDescrEX,'ifPacketsReceivedEX':ifPacketsReceivedEX,'ifPacketsSentEX':ifPacketsSentEX,'ifErrorPacketsEX':ifErrorPacketsEX,'hdNumberEX':hdNumberEX,'systemHdTableEX':systemHdTableEX,'hdEntryEx':hdEntryEx,'hdIndexEX':hdIndexEX,'hdDescrEX':hdDescrEX,'hdTemperatureEX':hdTemperatureEX,'hdStatusEX':hdStatusEX,'hdModelEX':hdModelEX,'hdCapacityEX':hdCapacityEX,'hdSmartInfoEX':hdSmartInfoEX,'modelNameEX':modelNameEX,'hostNameEX':hostNameEX,'sysFanNumberEX':sysFanNumberEX,'systemFanTableEx':systemFanTableEx,'sysFanEntryEx':sysFanEntryEx,_d:sysFanIndexEX,'sysFanDescrEX':sysFanDescrEX,'sysFanSpeedEX':sysFanSpeedEX,'sysVolumeNumberEX':sysVolumeNumberEX,'systemVolumeTableEx':systemVolumeTableEx,'sysVolumeEntryEx':sysVolumeEntryEx,_e:sysVolumeIndexEX,'sysVolumeDescrEX':sysVolumeDescrEX,'sysVolumeFSEX':sysVolumeFSEX,'sysVolumeTotalSizeEX':sysVolumeTotalSizeEX,'sysVolumeFreeSizeEX':sysVolumeFreeSizeEX,'sysVolumeStatusEX':sysVolumeStatusEX,'storageSystemEx':storageSystemEx,'systemSettings':systemSettings,'storageManager':storageManager,'nasStorage':nasStorage,'components':components,'enclosure':enclosure,'enclosurelNumber':enclosurelNumber,'enclosureTable':enclosureTable,'enclosureTableEntry':enclosureTableEntry,_f:enclosureIndex,'enclosureID':enclosureID,'enclosureModel':enclosureModel,'enclosureSerialNum':enclosureSerialNum,'enclosureSlot':enclosureSlot,'enclosureName':enclosureName,'enclosureSystemTemp':enclosureSystemTemp,'systemFan':systemFan,'systemFanNumber':systemFanNumber,'systemFan2Table':systemFan2Table,'systemFan2TableEntry':systemFan2TableEntry,_g:systemFanIndex,'systemFanID':systemFanID,'systemFanEnclosureID':systemFanEnclosureID,'systemFanStatus':systemFanStatus,'systemFanSpeed':systemFanSpeed,'systemPower':systemPower,'systemPowerNumber':systemPowerNumber,'systemPowerTable':systemPowerTable,'systemPowerTableEntry':systemPowerTableEntry,_h:systemPowerIndex,'systemPowerID':systemPowerID,'systemPowerEnclosureID':systemPowerEnclosureID,'systemPowerStatus':systemPowerStatus,'systemPowerFanSpeed':systemPowerFanSpeed,'systemPowerTemp':systemPowerTemp,'cpu':cpu,'cpuNumber':cpuNumber,'cpuTemp':cpuTemp,'cpuTable':cpuTable,'cpuTableEntry':cpuTableEntry,_i:cpuIndex,'cpuID':cpuID,'cpuUsage':cpuUsage,'disk':disk,'diskNumber':diskNumber,'diskTable':diskTable,'diskTableEntry':diskTableEntry,_j:diskIndex,'diskID':diskID,'diskEnclosureID':diskEnclosureID,'diskSummary':diskSummary,'diskSmartInfo':diskSmartInfo,'diskTemperture':diskTemperture,'diskGlobalSpare':diskGlobalSpare,'diskModel':diskModel,'diskCapacity':diskCapacity,'msataDisk':msataDisk,'msataDiskNumber':msataDiskNumber,'msataDiskTable':msataDiskTable,'msataDiskTableEntry':msataDiskTableEntry,_l:msataDiskIndex,'msataDiskID':msataDiskID,'msataDiskEnclosureID':msataDiskEnclosureID,'msataDiskSummary':msataDiskSummary,'msataDiskSmartInfo':msataDiskSmartInfo,'msataDiskTemperture':msataDiskTemperture,'msataDiskGlobalSpare':msataDiskGlobalSpare,'msataDiskModel':msataDiskModel,'msataDiskCapacity':msataDiskCapacity,'storageSpace':storageSpace,'raid':raid,'raidNumber':raidNumber,'raidGroupTable':raidGroupTable,'raidGroupTableEntry':raidGroupTableEntry,_m:raidIndex,'raidID':raidID,'raidCapacity':raidCapacity,'raidFreeSize':raidFreeSize,'raidStatus':raidStatus,'raidBitmap':raidBitmap,'raidLevel':raidLevel,'pool':pool,'poolNumber':poolNumber,'poolTable':poolTable,'poolTableEntry':poolTableEntry,_n:poolIndex,'poolID':poolID,'poolCapacity':poolCapacity,'poolFreeSize':poolFreeSize,'poolStatus':poolStatus,'volume':volume,'volumeNumber':volumeNumber,'volumeTable':volumeTable,'volumeTableEntry':volumeTableEntry,_o:volumeIndex,'volumeID':volumeID,'volumeCapacity':volumeCapacity,'volumeFreeSize':volumeFreeSize,'volumeStatus':volumeStatus,'volumeSSDCache':volumeSSDCache,'volumeThin':volumeThin,'volumeName':volumeName,'cacheAcceleration':cacheAcceleration,'service':service,'availablePercent':availablePercent,'readHitRate':readHitRate,'writeHitRate':writeHitRate,'status':status,'iSCSI':iSCSI,'iSCSIStorage':iSCSIStorage,'iSCSIService':iSCSIService,'iSCSIServicePort':iSCSIServicePort,'iSNSService':iSNSService,'iSNSIP':iSNSIP,'lun':lun,'lunNumber':lunNumber,'lunTable':lunTable,'lunTableEntry':lunTableEntry,_p:lunIndex,'lunID':lunID,'lunCapacity':lunCapacity,'lunUsedPercent':lunUsedPercent,'lunStatus':lunStatus,'lunName':lunName,'lunBackupStatus':lunBackupStatus,'lunIsMap':lunIsMap,'target':target,'targetNumber':targetNumber,'targeTable':targeTable,'targeTableEntry':targeTableEntry,_q:targetIndex,'targetID':targetID,'targetName':targetName,'targetIQN':targetIQN,'targetStatus':targetStatus,'systemStatus':systemStatus,'resourceMonitor':resourceMonitor,'diskPerformance':diskPerformance,'diskPerformanceNumber':diskPerformanceNumber,'diskPerformanceTable':diskPerformanceTable,'diskPerformanceTableEntry':diskPerformanceTableEntry,_r:diskPerformanceIndex,'blvID':blvID,'iops':iops,'latency':latency,'systemTraps':systemTraps,'eventInform':eventInform,'eventWarning':eventWarning,'eventError':eventError})