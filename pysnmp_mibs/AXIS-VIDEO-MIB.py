_r='storageGroup'
_q='casingGroup'
_p='tempSensorGroup'
_o='videoObjectGroup'
_n='alarmSingle'
_m='alarmCleared'
_l='alarmNew'
_k='obsolete'
_j='storageId'
_i='casingId'
_h='audioChannelId'
_g='noSignal'
_f='signalOk'
_e='videoChannelId'
_d='tempSensorId'
_c='tempSensorType'
_b='housing'
_a='fanType'
_Z='powerSupplyId'
_Y='powerSupplyType'
_X='videoNotificationGroup'
_W='storageName'
_V='storageDisruptionDetected'
_U='casingStatus'
_T='casingName'
_S='audioSignalStatus'
_R='videoSignalStatus'
_Q='tempSensorValue'
_P='tempSensorStatus'
_O='fanStatus'
_N='powerSupplyStatus'
_M='accessible-for-notify'
_L='failure'
_K='common'
_J='SnmpAdminString'
_I='alarmText'
_H='alarmName'
_G='alarmID'
_F='Unsigned32'
_E='read-only'
_D='not-accessible'
_C='Integer32'
_B='current'
_A='AXIS-VIDEO-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
axis,products=mibBuilder.importSymbols('AXIS-ROOT-MIB','axis','products')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
video=ModuleIdentity((1,3,6,1,4,1,368,4))
if mibBuilder.loadTexts:video.setRevisions(('2016-09-23 12:18','2012-12-12 12:02'))
_VideoBased_ObjectIdentity=ObjectIdentity
videoBased=_VideoBased_ObjectIdentity((1,3,6,1,4,1,368,1,1))
_VideoObjects_ObjectIdentity=ObjectIdentity
videoObjects=_VideoObjects_ObjectIdentity((1,3,6,1,4,1,368,4,1))
_PowerSupplyTable_Object=MibTable
powerSupplyTable=_PowerSupplyTable_Object((1,3,6,1,4,1,368,4,1,1))
if mibBuilder.loadTexts:powerSupplyTable.setStatus(_B)
_PowerSupplyEntry_Object=MibTableRow
powerSupplyEntry=_PowerSupplyEntry_Object((1,3,6,1,4,1,368,4,1,1,1))
powerSupplyEntry.setIndexNames((0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:powerSupplyEntry.setStatus(_B)
class _PowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('internal',2),('external',3)))
_PowerSupplyType_Type.__name__=_C
_PowerSupplyType_Object=MibTableColumn
powerSupplyType=_PowerSupplyType_Object((1,3,6,1,4,1,368,4,1,1,1,1),_PowerSupplyType_Type())
powerSupplyType.setMaxAccess(_D)
if mibBuilder.loadTexts:powerSupplyType.setStatus(_B)
class _PowerSupplyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PowerSupplyId_Type.__name__=_F
_PowerSupplyId_Object=MibTableColumn
powerSupplyId=_PowerSupplyId_Object((1,3,6,1,4,1,368,4,1,1,1,2),_PowerSupplyId_Type())
powerSupplyId.setMaxAccess(_D)
if mibBuilder.loadTexts:powerSupplyId.setStatus(_B)
class _PowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_L,2)))
_PowerSupplyStatus_Type.__name__=_C
_PowerSupplyStatus_Object=MibTableColumn
powerSupplyStatus=_PowerSupplyStatus_Object((1,3,6,1,4,1,368,4,1,1,1,3),_PowerSupplyStatus_Type())
powerSupplyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:powerSupplyStatus.setStatus(_B)
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,368,4,1,2))
if mibBuilder.loadTexts:fanTable.setStatus(_B)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,368,4,1,2,1))
fanEntry.setIndexNames((0,_A,_a),(0,_A,'fanId'))
if mibBuilder.loadTexts:fanEntry.setStatus(_B)
class _FanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_b,2),('rack',3),('cpu',4)))
_FanType_Type.__name__=_C
_FanType_Object=MibTableColumn
fanType=_FanType_Object((1,3,6,1,4,1,368,4,1,2,1,1),_FanType_Type())
fanType.setMaxAccess(_D)
if mibBuilder.loadTexts:fanType.setStatus(_B)
class _FanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_FanId_Type.__name__=_F
_FanId_Object=MibTableColumn
fanId=_FanId_Object((1,3,6,1,4,1,368,4,1,2,1,2),_FanId_Type())
fanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fanId.setStatus(_B)
class _FanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_L,2)))
_FanStatus_Type.__name__=_C
_FanStatus_Object=MibTableColumn
fanStatus=_FanStatus_Object((1,3,6,1,4,1,368,4,1,2,1,3),_FanStatus_Type())
fanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fanStatus.setStatus(_B)
_TempSensorTable_Object=MibTable
tempSensorTable=_TempSensorTable_Object((1,3,6,1,4,1,368,4,1,3))
if mibBuilder.loadTexts:tempSensorTable.setStatus(_B)
_TempSensorEntry_Object=MibTableRow
tempSensorEntry=_TempSensorEntry_Object((1,3,6,1,4,1,368,4,1,3,1))
tempSensorEntry.setIndexNames((0,_A,_c),(0,_A,_d))
if mibBuilder.loadTexts:tempSensorEntry.setStatus(_B)
class _TempSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_b,2),('rack',3),('cpu',4)))
_TempSensorType_Type.__name__=_C
_TempSensorType_Object=MibTableColumn
tempSensorType=_TempSensorType_Object((1,3,6,1,4,1,368,4,1,3,1,1),_TempSensorType_Type())
tempSensorType.setMaxAccess(_D)
if mibBuilder.loadTexts:tempSensorType.setStatus(_B)
class _TempSensorId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_TempSensorId_Type.__name__=_F
_TempSensorId_Object=MibTableColumn
tempSensorId=_TempSensorId_Object((1,3,6,1,4,1,368,4,1,3,1,2),_TempSensorId_Type())
tempSensorId.setMaxAccess(_D)
if mibBuilder.loadTexts:tempSensorId.setStatus(_B)
class _TempSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),(_L,2),('outOfBoundary',3)))
_TempSensorStatus_Type.__name__=_C
_TempSensorStatus_Object=MibTableColumn
tempSensorStatus=_TempSensorStatus_Object((1,3,6,1,4,1,368,4,1,3,1,3),_TempSensorStatus_Type())
tempSensorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tempSensorStatus.setStatus(_B)
class _TempSensorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-176,150))
_TempSensorValue_Type.__name__=_C
_TempSensorValue_Object=MibTableColumn
tempSensorValue=_TempSensorValue_Object((1,3,6,1,4,1,368,4,1,3,1,4),_TempSensorValue_Type())
tempSensorValue.setMaxAccess(_E)
if mibBuilder.loadTexts:tempSensorValue.setStatus(_B)
_VideoChannelTable_Object=MibTable
videoChannelTable=_VideoChannelTable_Object((1,3,6,1,4,1,368,4,1,4))
if mibBuilder.loadTexts:videoChannelTable.setStatus(_B)
_VideoChannelEntry_Object=MibTableRow
videoChannelEntry=_VideoChannelEntry_Object((1,3,6,1,4,1,368,4,1,4,1))
videoChannelEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:videoChannelEntry.setStatus(_B)
class _VideoChannelId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_VideoChannelId_Type.__name__=_F
_VideoChannelId_Object=MibTableColumn
videoChannelId=_VideoChannelId_Object((1,3,6,1,4,1,368,4,1,4,1,1),_VideoChannelId_Type())
videoChannelId.setMaxAccess(_D)
if mibBuilder.loadTexts:videoChannelId.setStatus(_B)
class _VideoSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_VideoSignalStatus_Type.__name__=_C
_VideoSignalStatus_Object=MibTableColumn
videoSignalStatus=_VideoSignalStatus_Object((1,3,6,1,4,1,368,4,1,4,1,2),_VideoSignalStatus_Type())
videoSignalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:videoSignalStatus.setStatus(_B)
_AudioChannelTable_Object=MibTable
audioChannelTable=_AudioChannelTable_Object((1,3,6,1,4,1,368,4,1,5))
if mibBuilder.loadTexts:audioChannelTable.setStatus(_B)
_AudioChannelEntry_Object=MibTableRow
audioChannelEntry=_AudioChannelEntry_Object((1,3,6,1,4,1,368,4,1,5,1))
audioChannelEntry.setIndexNames((0,_A,_h))
if mibBuilder.loadTexts:audioChannelEntry.setStatus(_B)
class _AudioChannelId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_AudioChannelId_Type.__name__=_F
_AudioChannelId_Object=MibTableColumn
audioChannelId=_AudioChannelId_Object((1,3,6,1,4,1,368,4,1,5,1,1),_AudioChannelId_Type())
audioChannelId.setMaxAccess(_D)
if mibBuilder.loadTexts:audioChannelId.setStatus(_B)
class _AudioSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_AudioSignalStatus_Type.__name__=_C
_AudioSignalStatus_Object=MibTableColumn
audioSignalStatus=_AudioSignalStatus_Object((1,3,6,1,4,1,368,4,1,5,1,2),_AudioSignalStatus_Type())
audioSignalStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:audioSignalStatus.setStatus(_B)
_CasingTable_Object=MibTable
casingTable=_CasingTable_Object((1,3,6,1,4,1,368,4,1,6))
if mibBuilder.loadTexts:casingTable.setStatus(_B)
_CasingEntry_Object=MibTableRow
casingEntry=_CasingEntry_Object((1,3,6,1,4,1,368,4,1,6,1))
casingEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:casingEntry.setStatus(_B)
class _CasingId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CasingId_Type.__name__=_F
_CasingId_Object=MibTableColumn
casingId=_CasingId_Object((1,3,6,1,4,1,368,4,1,6,1,1),_CasingId_Type())
casingId.setMaxAccess(_D)
if mibBuilder.loadTexts:casingId.setStatus(_B)
class _CasingName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CasingName_Type.__name__=_J
_CasingName_Object=MibTableColumn
casingName=_CasingName_Object((1,3,6,1,4,1,368,4,1,6,1,2),_CasingName_Type())
casingName.setMaxAccess(_E)
if mibBuilder.loadTexts:casingName.setStatus(_B)
class _CasingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('closed',1),('open',2)))
_CasingStatus_Type.__name__=_C
_CasingStatus_Object=MibTableColumn
casingStatus=_CasingStatus_Object((1,3,6,1,4,1,368,4,1,6,1,3),_CasingStatus_Type())
casingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:casingStatus.setStatus(_B)
_StorageTable_Object=MibTable
storageTable=_StorageTable_Object((1,3,6,1,4,1,368,4,1,8))
if mibBuilder.loadTexts:storageTable.setStatus(_B)
_StorageEntry_Object=MibTableRow
storageEntry=_StorageEntry_Object((1,3,6,1,4,1,368,4,1,8,1))
storageEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:storageEntry.setStatus(_B)
class _StorageId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_StorageId_Type.__name__=_F
_StorageId_Object=MibTableColumn
storageId=_StorageId_Object((1,3,6,1,4,1,368,4,1,8,1,1),_StorageId_Type())
storageId.setMaxAccess(_D)
if mibBuilder.loadTexts:storageId.setStatus(_B)
class _StorageName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_StorageName_Type.__name__=_J
_StorageName_Object=MibTableColumn
storageName=_StorageName_Object((1,3,6,1,4,1,368,4,1,8,1,2),_StorageName_Type())
storageName.setMaxAccess(_E)
if mibBuilder.loadTexts:storageName.setStatus(_B)
class _StorageDisruptionDetected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_StorageDisruptionDetected_Type.__name__=_C
_StorageDisruptionDetected_Object=MibTableColumn
storageDisruptionDetected=_StorageDisruptionDetected_Object((1,3,6,1,4,1,368,4,1,8,1,3),_StorageDisruptionDetected_Type())
storageDisruptionDetected.setMaxAccess(_E)
if mibBuilder.loadTexts:storageDisruptionDetected.setStatus(_B)
_VideoNotifications_ObjectIdentity=ObjectIdentity
videoNotifications=_VideoNotifications_ObjectIdentity((1,3,6,1,4,1,368,4,2))
_VideoNotificationPrefix_ObjectIdentity=ObjectIdentity
videoNotificationPrefix=_VideoNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,368,4,2,0))
_AlarmID_Type=Unsigned32
_AlarmID_Object=MibScalar
alarmID=_AlarmID_Object((1,3,6,1,4,1,368,4,2,1),_AlarmID_Type())
alarmID.setMaxAccess(_M)
if mibBuilder.loadTexts:alarmID.setStatus(_B)
_AlarmName_Type=SnmpAdminString
_AlarmName_Object=MibScalar
alarmName=_AlarmName_Object((1,3,6,1,4,1,368,4,2,2),_AlarmName_Type())
alarmName.setMaxAccess(_M)
if mibBuilder.loadTexts:alarmName.setStatus(_B)
_AlarmText_Type=SnmpAdminString
_AlarmText_Object=MibScalar
alarmText=_AlarmText_Object((1,3,6,1,4,1,368,4,2,3),_AlarmText_Type())
alarmText.setMaxAccess(_M)
if mibBuilder.loadTexts:alarmText.setStatus(_B)
_VideoConformance_ObjectIdentity=ObjectIdentity
videoConformance=_VideoConformance_ObjectIdentity((1,3,6,1,4,1,368,4,3))
_VideoGroups_ObjectIdentity=ObjectIdentity
videoGroups=_VideoGroups_ObjectIdentity((1,3,6,1,4,1,368,4,3,1))
_VideoCompliances_ObjectIdentity=ObjectIdentity
videoCompliances=_VideoCompliances_ObjectIdentity((1,3,6,1,4,1,368,4,3,2))
videoObjectGroup=ObjectGroup((1,3,6,1,4,1,368,4,3,1,1))
videoObjectGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:videoObjectGroup.setStatus(_k)
tempSensorGroup=ObjectGroup((1,3,6,1,4,1,368,4,3,1,3))
tempSensorGroup.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:tempSensorGroup.setStatus(_B)
casingGroup=ObjectGroup((1,3,6,1,4,1,368,4,3,1,4))
casingGroup.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:casingGroup.setStatus(_B)
storageGroup=ObjectGroup((1,3,6,1,4,1,368,4,3,1,5))
storageGroup.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:storageGroup.setStatus(_B)
alarmNew=NotificationType((1,3,6,1,4,1,368,4,2,0,1))
alarmNew.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:alarmNew.setStatus(_B)
alarmCleared=NotificationType((1,3,6,1,4,1,368,4,2,0,2))
alarmCleared.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:alarmCleared.setStatus(_B)
alarmSingle=NotificationType((1,3,6,1,4,1,368,4,2,0,3))
alarmSingle.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:alarmSingle.setStatus(_B)
videoNotificationGroup=NotificationGroup((1,3,6,1,4,1,368,4,3,1,2))
videoNotificationGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:videoNotificationGroup.setStatus(_B)
videoCompliance=ModuleCompliance((1,3,6,1,4,1,368,4,3,2,1))
videoCompliance.setObjects(*((_A,_o),(_A,_X)))
if mibBuilder.loadTexts:videoCompliance.setStatus(_k)
videoComplianceRev2=ModuleCompliance((1,3,6,1,4,1,368,4,3,2,2))
videoComplianceRev2.setObjects(*((_A,_X),(_A,_N),(_A,_O),(_A,_p),(_A,_R),(_A,_S),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:videoComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'videoBased':videoBased,'video':video,'videoObjects':videoObjects,'powerSupplyTable':powerSupplyTable,'powerSupplyEntry':powerSupplyEntry,_Y:powerSupplyType,_Z:powerSupplyId,_N:powerSupplyStatus,'fanTable':fanTable,'fanEntry':fanEntry,_a:fanType,'fanId':fanId,_O:fanStatus,'tempSensorTable':tempSensorTable,'tempSensorEntry':tempSensorEntry,_c:tempSensorType,_d:tempSensorId,_P:tempSensorStatus,_Q:tempSensorValue,'videoChannelTable':videoChannelTable,'videoChannelEntry':videoChannelEntry,_e:videoChannelId,_R:videoSignalStatus,'audioChannelTable':audioChannelTable,'audioChannelEntry':audioChannelEntry,_h:audioChannelId,_S:audioSignalStatus,'casingTable':casingTable,'casingEntry':casingEntry,_i:casingId,_T:casingName,_U:casingStatus,'storageTable':storageTable,'storageEntry':storageEntry,_j:storageId,_W:storageName,_V:storageDisruptionDetected,'videoNotifications':videoNotifications,'videoNotificationPrefix':videoNotificationPrefix,_l:alarmNew,_m:alarmCleared,_n:alarmSingle,_G:alarmID,_H:alarmName,_I:alarmText,'videoConformance':videoConformance,'videoGroups':videoGroups,_o:videoObjectGroup,_X:videoNotificationGroup,_p:tempSensorGroup,_q:casingGroup,_r:storageGroup,'videoCompliances':videoCompliances,'videoCompliance':videoCompliance,'videoComplianceRev2':videoComplianceRev2})