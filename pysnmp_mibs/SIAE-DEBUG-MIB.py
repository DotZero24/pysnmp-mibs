_O='uploadDownloadFTPStatus'
_N='memoryIdNumber'
_M='deviceId'
_L='equipIpSnmpAgentAddress'
_K='SIAE-EQUIP-MIB'
_J='AlarmSeverityCode'
_I='enable'
_H='disable'
_G='DisplayString'
_F='SIAE-DEBUG-MIB'
_E='read-only'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus,alarmTrap=mibBuilder.importSymbols('SIAE-ALARM-MIB',_J,'AlarmStatus','alarmTrap')
equipIpSnmpAgentAddress,=mibBuilder.importSymbols(_K,_L)
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
debug=ModuleIdentity((1,3,6,1,4,1,3373,1103,41))
if mibBuilder.loadTexts:debug.setRevisions(('2015-03-23 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class _DebugMibVersion_Type(Integer32):defaultValue=1
_DebugMibVersion_Type.__name__=_D
_DebugMibVersion_Object=MibScalar
debugMibVersion=_DebugMibVersion_Object((1,3,6,1,4,1,3373,1103,41,1),_DebugMibVersion_Type())
debugMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:debugMibVersion.setStatus(_A)
_DeviceTable_Object=MibTable
deviceTable=_DeviceTable_Object((1,3,6,1,4,1,3373,1103,41,2))
if mibBuilder.loadTexts:deviceTable.setStatus(_A)
_DeviceEntry_Object=MibTableRow
deviceEntry=_DeviceEntry_Object((1,3,6,1,4,1,3373,1103,41,2,1))
deviceEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:deviceEntry.setStatus(_A)
_DeviceId_Type=Integer32
_DeviceId_Object=MibTableColumn
deviceId=_DeviceId_Object((1,3,6,1,4,1,3373,1103,41,2,1,1),_DeviceId_Type())
deviceId.setMaxAccess(_E)
if mibBuilder.loadTexts:deviceId.setStatus(_A)
class _DeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('serial',1),('parallel',2),('delete',3)))
_DeviceType_Type.__name__=_D
_DeviceType_Object=MibTableColumn
deviceType=_DeviceType_Object((1,3,6,1,4,1,3373,1103,41,2,1,2),_DeviceType_Type())
deviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
class _DeviceLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_DeviceLabel_Type.__name__=_G
_DeviceLabel_Object=MibTableColumn
deviceLabel=_DeviceLabel_Object((1,3,6,1,4,1,3373,1103,41,2,1,3),_DeviceLabel_Type())
deviceLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceLabel.setStatus(_A)
class _DeviceStartAddressBase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DeviceStartAddressBase_Type.__name__=_C
_DeviceStartAddressBase_Object=MibTableColumn
deviceStartAddressBase=_DeviceStartAddressBase_Object((1,3,6,1,4,1,3373,1103,41,2,1,4),_DeviceStartAddressBase_Type())
deviceStartAddressBase.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceStartAddressBase.setStatus(_A)
class _DeviceStartAddressOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DeviceStartAddressOffset_Type.__name__=_C
_DeviceStartAddressOffset_Object=MibTableColumn
deviceStartAddressOffset=_DeviceStartAddressOffset_Object((1,3,6,1,4,1,3373,1103,41,2,1,5),_DeviceStartAddressOffset_Type())
deviceStartAddressOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceStartAddressOffset.setStatus(_A)
class _DeviceEndAddressBase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DeviceEndAddressBase_Type.__name__=_C
_DeviceEndAddressBase_Object=MibTableColumn
deviceEndAddressBase=_DeviceEndAddressBase_Object((1,3,6,1,4,1,3373,1103,41,2,1,6),_DeviceEndAddressBase_Type())
deviceEndAddressBase.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceEndAddressBase.setStatus(_A)
class _DeviceEndAddressOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DeviceEndAddressOffset_Type.__name__=_C
_DeviceEndAddressOffset_Object=MibTableColumn
deviceEndAddressOffset=_DeviceEndAddressOffset_Object((1,3,6,1,4,1,3373,1103,41,2,1,7),_DeviceEndAddressOffset_Type())
deviceEndAddressOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceEndAddressOffset.setStatus(_A)
_MemoryTable_Object=MibTable
memoryTable=_MemoryTable_Object((1,3,6,1,4,1,3373,1103,41,3))
if mibBuilder.loadTexts:memoryTable.setStatus(_A)
_MemoryEntry_Object=MibTableRow
memoryEntry=_MemoryEntry_Object((1,3,6,1,4,1,3373,1103,41,3,1))
memoryEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:memoryEntry.setStatus(_A)
_MemoryIdNumber_Type=Integer32
_MemoryIdNumber_Object=MibTableColumn
memoryIdNumber=_MemoryIdNumber_Object((1,3,6,1,4,1,3373,1103,41,3,1,1),_MemoryIdNumber_Type())
memoryIdNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:memoryIdNumber.setStatus(_A)
class _MemoryAddressBase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MemoryAddressBase_Type.__name__=_C
_MemoryAddressBase_Object=MibTableColumn
memoryAddressBase=_MemoryAddressBase_Object((1,3,6,1,4,1,3373,1103,41,3,1,2),_MemoryAddressBase_Type())
memoryAddressBase.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryAddressBase.setStatus(_A)
class _MemoryAddressOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MemoryAddressOffset_Type.__name__=_C
_MemoryAddressOffset_Object=MibTableColumn
memoryAddressOffset=_MemoryAddressOffset_Object((1,3,6,1,4,1,3373,1103,41,3,1,3),_MemoryAddressOffset_Type())
memoryAddressOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryAddressOffset.setStatus(_A)
class _MemoryValue_Type(Integer32):defaultValue=0
_MemoryValue_Type.__name__=_D
_MemoryValue_Object=MibTableColumn
memoryValue=_MemoryValue_Object((1,3,6,1,4,1,3373,1103,41,3,1,4),_MemoryValue_Type())
memoryValue.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryValue.setStatus(_A)
class _MemoryDumpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('enableuntiltrigger',3)))
_MemoryDumpEnable_Type.__name__=_D
_MemoryDumpEnable_Object=MibTableColumn
memoryDumpEnable=_MemoryDumpEnable_Object((1,3,6,1,4,1,3373,1103,41,3,1,5),_MemoryDumpEnable_Type())
memoryDumpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryDumpEnable.setStatus(_A)
class _MemoryDumpSize_Type(Integer32):defaultValue=50
_MemoryDumpSize_Type.__name__=_D
_MemoryDumpSize_Object=MibTableColumn
memoryDumpSize=_MemoryDumpSize_Object((1,3,6,1,4,1,3373,1103,41,3,1,6),_MemoryDumpSize_Type())
memoryDumpSize.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryDumpSize.setStatus(_A)
class _MemoryDump_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32768,32768));fixedLength=32768
_MemoryDump_Type.__name__=_C
_MemoryDump_Object=MibTableColumn
memoryDump=_MemoryDump_Object((1,3,6,1,4,1,3373,1103,41,3,1,7),_MemoryDump_Type())
memoryDump.setMaxAccess(_E)
if mibBuilder.loadTexts:memoryDump.setStatus(_A)
class _TriggerMemoryAddressBase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_TriggerMemoryAddressBase_Type.__name__=_C
_TriggerMemoryAddressBase_Object=MibTableColumn
triggerMemoryAddressBase=_TriggerMemoryAddressBase_Object((1,3,6,1,4,1,3373,1103,41,3,1,8),_TriggerMemoryAddressBase_Type())
triggerMemoryAddressBase.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerMemoryAddressBase.setStatus(_A)
class _TriggerMemoryAddressOffset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_TriggerMemoryAddressOffset_Type.__name__=_C
_TriggerMemoryAddressOffset_Object=MibTableColumn
triggerMemoryAddressOffset=_TriggerMemoryAddressOffset_Object((1,3,6,1,4,1,3373,1103,41,3,1,9),_TriggerMemoryAddressOffset_Type())
triggerMemoryAddressOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerMemoryAddressOffset.setStatus(_A)
class _TriggerMemoryValue_Type(Integer32):defaultValue=0
_TriggerMemoryValue_Type.__name__=_D
_TriggerMemoryValue_Object=MibTableColumn
triggerMemoryValue=_TriggerMemoryValue_Object((1,3,6,1,4,1,3373,1103,41,3,1,10),_TriggerMemoryValue_Type())
triggerMemoryValue.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerMemoryValue.setStatus(_A)
class _TriggerMemoryMask_Type(Integer32):defaultValue=255
_TriggerMemoryMask_Type.__name__=_D
_TriggerMemoryMask_Object=MibTableColumn
triggerMemoryMask=_TriggerMemoryMask_Object((1,3,6,1,4,1,3373,1103,41,3,1,11),_TriggerMemoryMask_Type())
triggerMemoryMask.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerMemoryMask.setStatus(_A)
class _TriggerEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TriggerEnable_Type.__name__=_D
_TriggerEnable_Object=MibTableColumn
triggerEnable=_TriggerEnable_Object((1,3,6,1,4,1,3373,1103,41,3,1,12),_TriggerEnable_Type())
triggerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerEnable.setStatus(_A)
_TriggerAlarm_Type=AlarmStatus
_TriggerAlarm_Object=MibTableColumn
triggerAlarm=_TriggerAlarm_Object((1,3,6,1,4,1,3373,1103,41,3,1,13),_TriggerAlarm_Type())
triggerAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:triggerAlarm.setStatus(_A)
class _TriggerAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_TriggerAlarmSeverityCode_Type.__name__=_J
_TriggerAlarmSeverityCode_Object=MibScalar
triggerAlarmSeverityCode=_TriggerAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,41,4),_TriggerAlarmSeverityCode_Type())
triggerAlarmSeverityCode.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerAlarmSeverityCode.setStatus(_A)
class _UploadMemoryAddressBaseStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_UploadMemoryAddressBaseStart_Type.__name__=_C
_UploadMemoryAddressBaseStart_Object=MibScalar
uploadMemoryAddressBaseStart=_UploadMemoryAddressBaseStart_Object((1,3,6,1,4,1,3373,1103,41,5),_UploadMemoryAddressBaseStart_Type())
uploadMemoryAddressBaseStart.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadMemoryAddressBaseStart.setStatus(_A)
class _UploadMemoryAddressOffsetStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_UploadMemoryAddressOffsetStart_Type.__name__=_C
_UploadMemoryAddressOffsetStart_Object=MibScalar
uploadMemoryAddressOffsetStart=_UploadMemoryAddressOffsetStart_Object((1,3,6,1,4,1,3373,1103,41,6),_UploadMemoryAddressOffsetStart_Type())
uploadMemoryAddressOffsetStart.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadMemoryAddressOffsetStart.setStatus(_A)
class _UploadMemoryAddressBaseEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_UploadMemoryAddressBaseEnd_Type.__name__=_C
_UploadMemoryAddressBaseEnd_Object=MibScalar
uploadMemoryAddressBaseEnd=_UploadMemoryAddressBaseEnd_Object((1,3,6,1,4,1,3373,1103,41,7),_UploadMemoryAddressBaseEnd_Type())
uploadMemoryAddressBaseEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadMemoryAddressBaseEnd.setStatus(_A)
class _UploadMemoryAddressOffsetEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_UploadMemoryAddressOffsetEnd_Type.__name__=_C
_UploadMemoryAddressOffsetEnd_Object=MibScalar
uploadMemoryAddressOffsetEnd=_UploadMemoryAddressOffsetEnd_Object((1,3,6,1,4,1,3373,1103,41,8),_UploadMemoryAddressOffsetEnd_Type())
uploadMemoryAddressOffsetEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadMemoryAddressOffsetEnd.setStatus(_A)
class _UploadDownloadActionRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upload',1),('download',2)))
_UploadDownloadActionRequest_Type.__name__=_D
_UploadDownloadActionRequest_Object=MibScalar
uploadDownloadActionRequest=_UploadDownloadActionRequest_Object((1,3,6,1,4,1,3373,1103,41,9),_UploadDownloadActionRequest_Type())
uploadDownloadActionRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadDownloadActionRequest.setStatus(_A)
class _UploadDownloadFTPfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UploadDownloadFTPfile_Type.__name__=_G
_UploadDownloadFTPfile_Object=MibScalar
uploadDownloadFTPfile=_UploadDownloadFTPfile_Object((1,3,6,1,4,1,3373,1103,41,10),_UploadDownloadFTPfile_Type())
uploadDownloadFTPfile.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadDownloadFTPfile.setStatus(_A)
class _UploadDownloadFTPStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('transferring',1),('completed',2),('interrupted',3),('empty',4)))
_UploadDownloadFTPStatus_Type.__name__=_D
_UploadDownloadFTPStatus_Object=MibScalar
uploadDownloadFTPStatus=_UploadDownloadFTPStatus_Object((1,3,6,1,4,1,3373,1103,41,11),_UploadDownloadFTPStatus_Type())
uploadDownloadFTPStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:uploadDownloadFTPStatus.setStatus(_A)
class _UploadDownloadFTPStatusTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,34)));namedValues=NamedValues(*(('trapDisable',1),('trapEnable',2),('trapEnableWithACK',34)))
_UploadDownloadFTPStatusTrapNotification_Type.__name__=_D
_UploadDownloadFTPStatusTrapNotification_Object=MibScalar
uploadDownloadFTPStatusTrapNotification=_UploadDownloadFTPStatusTrapNotification_Object((1,3,6,1,4,1,3373,1103,41,12),_UploadDownloadFTPStatusTrapNotification_Type())
uploadDownloadFTPStatusTrapNotification.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadDownloadFTPStatusTrapNotification.setStatus(_A)
class _DebugEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_DebugEnable_Type.__name__=_D
_DebugEnable_Object=MibScalar
debugEnable=_DebugEnable_Object((1,3,6,1,4,1,3373,1103,41,13),_DebugEnable_Type())
debugEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:debugEnable.setStatus(_A)
uploadDownloadFTPStatusTrap=NotificationType((1,3,6,1,4,1,3373,1103,0,4103))
uploadDownloadFTPStatusTrap.setObjects(*((_K,_L),(_F,_O)))
if mibBuilder.loadTexts:uploadDownloadFTPStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'uploadDownloadFTPStatusTrap':uploadDownloadFTPStatusTrap,'debug':debug,'debugMibVersion':debugMibVersion,'deviceTable':deviceTable,'deviceEntry':deviceEntry,_M:deviceId,'deviceType':deviceType,'deviceLabel':deviceLabel,'deviceStartAddressBase':deviceStartAddressBase,'deviceStartAddressOffset':deviceStartAddressOffset,'deviceEndAddressBase':deviceEndAddressBase,'deviceEndAddressOffset':deviceEndAddressOffset,'memoryTable':memoryTable,'memoryEntry':memoryEntry,_N:memoryIdNumber,'memoryAddressBase':memoryAddressBase,'memoryAddressOffset':memoryAddressOffset,'memoryValue':memoryValue,'memoryDumpEnable':memoryDumpEnable,'memoryDumpSize':memoryDumpSize,'memoryDump':memoryDump,'triggerMemoryAddressBase':triggerMemoryAddressBase,'triggerMemoryAddressOffset':triggerMemoryAddressOffset,'triggerMemoryValue':triggerMemoryValue,'triggerMemoryMask':triggerMemoryMask,'triggerEnable':triggerEnable,'triggerAlarm':triggerAlarm,'triggerAlarmSeverityCode':triggerAlarmSeverityCode,'uploadMemoryAddressBaseStart':uploadMemoryAddressBaseStart,'uploadMemoryAddressOffsetStart':uploadMemoryAddressOffsetStart,'uploadMemoryAddressBaseEnd':uploadMemoryAddressBaseEnd,'uploadMemoryAddressOffsetEnd':uploadMemoryAddressOffsetEnd,'uploadDownloadActionRequest':uploadDownloadActionRequest,'uploadDownloadFTPfile':uploadDownloadFTPfile,_O:uploadDownloadFTPStatus,'uploadDownloadFTPStatusTrapNotification':uploadDownloadFTPStatusTrapNotification,'debugEnable':debugEnable})