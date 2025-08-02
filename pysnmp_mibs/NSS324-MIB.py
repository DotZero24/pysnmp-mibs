_N='eventErrorMsg'
_M='eventWarningMsg'
_L='eventInformMsg'
_K='sysVolumeIndex'
_J='sysFanIndex'
_I='hdIndex'
_H='ifIndex'
_G='NotificationType'
_F='Integer32'
_E='NSS324-MIB'
_D='current'
_C='DisplayString'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
nssAthens=ModuleIdentity((1,3,6,1,4,1,9,6,1,103,41,324,114))
if mibBuilder.loadTexts:nssAthens.setRevisions(('2011-03-24 00:00',))
class DisplayString(OctetString):0
_Cisco_ObjectIdentity=ObjectIdentity
cisco=_Cisco_ObjectIdentity((1,3,6,1,4,1,9))
_OtherEnterprises_ObjectIdentity=ObjectIdentity
otherEnterprises=_OtherEnterprises_ObjectIdentity((1,3,6,1,4,1,9,6))
_CiscoSB_ObjectIdentity=ObjectIdentity
ciscoSB=_CiscoSB_ObjectIdentity((1,3,6,1,4,1,9,6,1))
_Nas004_ObjectIdentity=ObjectIdentity
nas004=_Nas004_ObjectIdentity((1,3,6,1,4,1,9,6,1,103))
_Nss_ObjectIdentity=ObjectIdentity
nss=_Nss_ObjectIdentity((1,3,6,1,4,1,9,6,1,103,41))
_Nss324_ObjectIdentity=ObjectIdentity
nss324=_Nss324_ObjectIdentity((1,3,6,1,4,1,9,6,1,103,41,324))
_StorageSystem_ObjectIdentity=ObjectIdentity
storageSystem=_StorageSystem_ObjectIdentity((1,3,6,1,4,1,9,6,1,103,41,324,114,1))
_SystemEventMsg_ObjectIdentity=ObjectIdentity
systemEventMsg=_SystemEventMsg_ObjectIdentity((1,3,6,1,4,1,9,6,1,103,41,324,114,1,1))
_EventInformMsg_Type=DisplayString
_EventInformMsg_Object=MibScalar
eventInformMsg=_EventInformMsg_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,1,101),_EventInformMsg_Type())
eventInformMsg.setMaxAccess(_A)
if mibBuilder.loadTexts:eventInformMsg.setStatus(_D)
_EventWarningMsg_Type=DisplayString
_EventWarningMsg_Object=MibScalar
eventWarningMsg=_EventWarningMsg_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,1,102),_EventWarningMsg_Type())
eventWarningMsg.setMaxAccess(_A)
if mibBuilder.loadTexts:eventWarningMsg.setStatus(_D)
_EventErrorMsg_Type=DisplayString
_EventErrorMsg_Object=MibScalar
eventErrorMsg=_EventErrorMsg_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,1,103),_EventErrorMsg_Type())
eventErrorMsg.setMaxAccess(_A)
if mibBuilder.loadTexts:eventErrorMsg.setStatus(_D)
_SystemInfo_ObjectIdentity=ObjectIdentity
systemInfo=_SystemInfo_ObjectIdentity((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2))
_SystemCPU_Usage_Type=DisplayString
_SystemCPU_Usage_Object=MibScalar
systemCPU_Usage=_SystemCPU_Usage_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,1),_SystemCPU_Usage_Type())
systemCPU_Usage.setMaxAccess(_A)
if mibBuilder.loadTexts:systemCPU_Usage.setStatus(_D)
_SystemTotalMem_Type=DisplayString
_SystemTotalMem_Object=MibScalar
systemTotalMem=_SystemTotalMem_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,2),_SystemTotalMem_Type())
systemTotalMem.setMaxAccess(_A)
if mibBuilder.loadTexts:systemTotalMem.setStatus(_D)
_SystemFreeMem_Type=DisplayString
_SystemFreeMem_Object=MibScalar
systemFreeMem=_SystemFreeMem_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,3),_SystemFreeMem_Type())
systemFreeMem.setMaxAccess(_A)
if mibBuilder.loadTexts:systemFreeMem.setStatus(_D)
_SystemUptime_Type=TimeTicks
_SystemUptime_Object=MibScalar
systemUptime=_SystemUptime_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,4),_SystemUptime_Type())
systemUptime.setMaxAccess(_A)
if mibBuilder.loadTexts:systemUptime.setStatus(_D)
_Cpu_Temperature_Type=DisplayString
_Cpu_Temperature_Object=MibScalar
cpu_Temperature=_Cpu_Temperature_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,5),_Cpu_Temperature_Type())
cpu_Temperature.setMaxAccess(_A)
if mibBuilder.loadTexts:cpu_Temperature.setStatus(_D)
_SystemTemperature_Type=DisplayString
_SystemTemperature_Object=MibScalar
systemTemperature=_SystemTemperature_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,6),_SystemTemperature_Type())
systemTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:systemTemperature.setStatus(_D)
_IfNumber_Type=Integer32
_IfNumber_Object=MibScalar
ifNumber=_IfNumber_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,8),_IfNumber_Type())
ifNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:ifNumber.setStatus(_B)
_SystemIfTable_Object=MibTable
systemIfTable=_SystemIfTable_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,9))
if mibBuilder.loadTexts:systemIfTable.setStatus(_B)
_IfEntry_Object=MibTableRow
ifEntry=_IfEntry_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,9,1))
ifEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ifEntry.setStatus(_B)
_IfIndex_Type=Integer32
_IfIndex_Object=MibTableColumn
ifIndex=_IfIndex_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,9,1,1),_IfIndex_Type())
ifIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:ifIndex.setStatus(_B)
class _IfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IfDescr_Type.__name__=_C
_IfDescr_Object=MibTableColumn
ifDescr=_IfDescr_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,9,1,2),_IfDescr_Type())
ifDescr.setMaxAccess(_A)
if mibBuilder.loadTexts:ifDescr.setStatus(_B)
_IfPacketsReceived_Type=Counter32
_IfPacketsReceived_Object=MibTableColumn
ifPacketsReceived=_IfPacketsReceived_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,9,1,3),_IfPacketsReceived_Type())
ifPacketsReceived.setMaxAccess(_A)
if mibBuilder.loadTexts:ifPacketsReceived.setStatus(_B)
_IfPacketsSent_Type=Counter32
_IfPacketsSent_Object=MibTableColumn
ifPacketsSent=_IfPacketsSent_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,9,1,4),_IfPacketsSent_Type())
ifPacketsSent.setMaxAccess(_A)
if mibBuilder.loadTexts:ifPacketsSent.setStatus(_B)
_IfErrorPackets_Type=Counter32
_IfErrorPackets_Object=MibTableColumn
ifErrorPackets=_IfErrorPackets_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,9,1,5),_IfErrorPackets_Type())
ifErrorPackets.setMaxAccess(_A)
if mibBuilder.loadTexts:ifErrorPackets.setStatus(_B)
_HdNumber_Type=Integer32
_HdNumber_Object=MibScalar
hdNumber=_HdNumber_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,10),_HdNumber_Type())
hdNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:hdNumber.setStatus(_B)
_SystemHdTable_Object=MibTable
systemHdTable=_SystemHdTable_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11))
if mibBuilder.loadTexts:systemHdTable.setStatus(_B)
_HdEntry_Object=MibTableRow
hdEntry=_HdEntry_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1))
hdEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hdEntry.setStatus(_B)
_HdIndex_Type=Integer32
_HdIndex_Object=MibTableColumn
hdIndex=_HdIndex_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1,1),_HdIndex_Type())
hdIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:hdIndex.setStatus(_B)
class _HdDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HdDescr_Type.__name__=_C
_HdDescr_Object=MibTableColumn
hdDescr=_HdDescr_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1,2),_HdDescr_Type())
hdDescr.setMaxAccess(_A)
if mibBuilder.loadTexts:hdDescr.setStatus(_B)
_HdTemperature_Type=DisplayString
_HdTemperature_Object=MibTableColumn
hdTemperature=_HdTemperature_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1,3),_HdTemperature_Type())
hdTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:hdTemperature.setStatus(_B)
class _HdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-9,-6,-5,-4,0)));namedValues=NamedValues(*(('rwError',-9),('invalid',-6),('noDisk',-5),('unknown',-4),('ready',0)))
_HdStatus_Type.__name__=_F
_HdStatus_Object=MibTableColumn
hdStatus=_HdStatus_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1,4),_HdStatus_Type())
hdStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:hdStatus.setStatus(_B)
_HdModel_Type=DisplayString
_HdModel_Object=MibTableColumn
hdModel=_HdModel_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1,5),_HdModel_Type())
hdModel.setMaxAccess(_A)
if mibBuilder.loadTexts:hdModel.setStatus(_B)
_HdCapacity_Type=DisplayString
_HdCapacity_Object=MibTableColumn
hdCapacity=_HdCapacity_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1,6),_HdCapacity_Type())
hdCapacity.setMaxAccess(_A)
if mibBuilder.loadTexts:hdCapacity.setStatus(_B)
_HdSmartInfo_Type=DisplayString
_HdSmartInfo_Object=MibTableColumn
hdSmartInfo=_HdSmartInfo_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,11,1,7),_HdSmartInfo_Type())
hdSmartInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:hdSmartInfo.setStatus(_B)
_ModelName_Type=DisplayString
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,12),_ModelName_Type())
modelName.setMaxAccess(_A)
if mibBuilder.loadTexts:modelName.setStatus(_D)
_HostName_Type=DisplayString
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,13),_HostName_Type())
hostName.setMaxAccess(_A)
if mibBuilder.loadTexts:hostName.setStatus(_D)
_SysFanNumber_Type=Integer32
_SysFanNumber_Object=MibScalar
sysFanNumber=_SysFanNumber_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,14),_SysFanNumber_Type())
sysFanNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:sysFanNumber.setStatus(_B)
_SystemFanTable_Object=MibTable
systemFanTable=_SystemFanTable_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,15))
if mibBuilder.loadTexts:systemFanTable.setStatus(_B)
_SysFanEntry_Object=MibTableRow
sysFanEntry=_SysFanEntry_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,15,1))
sysFanEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:sysFanEntry.setStatus(_B)
_SysFanIndex_Type=Integer32
_SysFanIndex_Object=MibTableColumn
sysFanIndex=_SysFanIndex_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,15,1,1),_SysFanIndex_Type())
sysFanIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:sysFanIndex.setStatus(_B)
class _SysFanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysFanDescr_Type.__name__=_C
_SysFanDescr_Object=MibTableColumn
sysFanDescr=_SysFanDescr_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,15,1,2),_SysFanDescr_Type())
sysFanDescr.setMaxAccess(_A)
if mibBuilder.loadTexts:sysFanDescr.setStatus(_B)
class _SysFanSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysFanSpeed_Type.__name__=_C
_SysFanSpeed_Object=MibTableColumn
sysFanSpeed=_SysFanSpeed_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,15,1,3),_SysFanSpeed_Type())
sysFanSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:sysFanSpeed.setStatus(_B)
_SysVolumeNumber_Type=Integer32
_SysVolumeNumber_Object=MibScalar
sysVolumeNumber=_SysVolumeNumber_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,16),_SysVolumeNumber_Type())
sysVolumeNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:sysVolumeNumber.setStatus(_B)
_SystemVolumeTable_Object=MibTable
systemVolumeTable=_SystemVolumeTable_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17))
if mibBuilder.loadTexts:systemVolumeTable.setStatus(_B)
_SysVolumeEntry_Object=MibTableRow
sysVolumeEntry=_SysVolumeEntry_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17,1))
sysVolumeEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:sysVolumeEntry.setStatus(_B)
_SysVolumeIndex_Type=Integer32
_SysVolumeIndex_Object=MibTableColumn
sysVolumeIndex=_SysVolumeIndex_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17,1,1),_SysVolumeIndex_Type())
sysVolumeIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:sysVolumeIndex.setStatus(_B)
class _SysVolumeDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysVolumeDescr_Type.__name__=_C
_SysVolumeDescr_Object=MibTableColumn
sysVolumeDescr=_SysVolumeDescr_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17,1,2),_SysVolumeDescr_Type())
sysVolumeDescr.setMaxAccess(_A)
if mibBuilder.loadTexts:sysVolumeDescr.setStatus(_B)
class _SysVolumeFS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysVolumeFS_Type.__name__=_C
_SysVolumeFS_Object=MibTableColumn
sysVolumeFS=_SysVolumeFS_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17,1,3),_SysVolumeFS_Type())
sysVolumeFS.setMaxAccess(_A)
if mibBuilder.loadTexts:sysVolumeFS.setStatus(_B)
class _SysVolumeTotalSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysVolumeTotalSize_Type.__name__=_C
_SysVolumeTotalSize_Object=MibTableColumn
sysVolumeTotalSize=_SysVolumeTotalSize_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17,1,4),_SysVolumeTotalSize_Type())
sysVolumeTotalSize.setMaxAccess(_A)
if mibBuilder.loadTexts:sysVolumeTotalSize.setStatus(_B)
class _SysVolumeFreeSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SysVolumeFreeSize_Type.__name__=_C
_SysVolumeFreeSize_Object=MibTableColumn
sysVolumeFreeSize=_SysVolumeFreeSize_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17,1,5),_SysVolumeFreeSize_Type())
sysVolumeFreeSize.setMaxAccess(_A)
if mibBuilder.loadTexts:sysVolumeFreeSize.setStatus(_B)
class _SysVolumeStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysVolumeStatus_Type.__name__=_C
_SysVolumeStatus_Object=MibTableColumn
sysVolumeStatus=_SysVolumeStatus_Object((1,3,6,1,4,1,9,6,1,103,41,324,114,1,2,17,1,6),_SysVolumeStatus_Type())
sysVolumeStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:sysVolumeStatus.setStatus(_B)
_SystemTraps_ObjectIdentity=ObjectIdentity
systemTraps=_SystemTraps_ObjectIdentity((1,3,6,1,4,1,9,6,1,103,41,324,114,1,10))
eventInform=NotificationType((1,3,6,1,4,1,9,6,1,103,41,324,114,1,10,0,1))
eventInform.setObjects((_E,_L))
if mibBuilder.loadTexts:eventInform.setStatus('')
eventWarning=NotificationType((1,3,6,1,4,1,9,6,1,103,41,324,114,1,10,0,2))
eventWarning.setObjects((_E,_M))
if mibBuilder.loadTexts:eventWarning.setStatus('')
eventError=NotificationType((1,3,6,1,4,1,9,6,1,103,41,324,114,1,10,0,4))
eventError.setObjects((_E,_N))
if mibBuilder.loadTexts:eventError.setStatus('')
mibBuilder.exportSymbols(_E,**{_C:DisplayString,'cisco':cisco,'otherEnterprises':otherEnterprises,'ciscoSB':ciscoSB,'nas004':nas004,'nss':nss,'nss324':nss324,'nssAthens':nssAthens,'storageSystem':storageSystem,'systemEventMsg':systemEventMsg,_L:eventInformMsg,_M:eventWarningMsg,_N:eventErrorMsg,'systemInfo':systemInfo,'systemCPU-Usage':systemCPU_Usage,'systemTotalMem':systemTotalMem,'systemFreeMem':systemFreeMem,'systemUptime':systemUptime,'cpu-Temperature':cpu_Temperature,'systemTemperature':systemTemperature,'ifNumber':ifNumber,'systemIfTable':systemIfTable,'ifEntry':ifEntry,_H:ifIndex,'ifDescr':ifDescr,'ifPacketsReceived':ifPacketsReceived,'ifPacketsSent':ifPacketsSent,'ifErrorPackets':ifErrorPackets,'hdNumber':hdNumber,'systemHdTable':systemHdTable,'hdEntry':hdEntry,_I:hdIndex,'hdDescr':hdDescr,'hdTemperature':hdTemperature,'hdStatus':hdStatus,'hdModel':hdModel,'hdCapacity':hdCapacity,'hdSmartInfo':hdSmartInfo,'modelName':modelName,'hostName':hostName,'sysFanNumber':sysFanNumber,'systemFanTable':systemFanTable,'sysFanEntry':sysFanEntry,_J:sysFanIndex,'sysFanDescr':sysFanDescr,'sysFanSpeed':sysFanSpeed,'sysVolumeNumber':sysVolumeNumber,'systemVolumeTable':systemVolumeTable,'sysVolumeEntry':sysVolumeEntry,_K:sysVolumeIndex,'sysVolumeDescr':sysVolumeDescr,'sysVolumeFS':sysVolumeFS,'sysVolumeTotalSize':sysVolumeTotalSize,'sysVolumeFreeSize':sysVolumeFreeSize,'sysVolumeStatus':sysVolumeStatus,'systemTraps':systemTraps,'eventInform':eventInform,'eventWarning':eventWarning,'eventError':eventError})