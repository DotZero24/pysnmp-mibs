_Y='perCentCPUUtilization'
_X='perCentMemoryUtilization'
_W='connectionURL'
_V='raidID'
_U='updateServiceName'
_T='keyDescription'
_S='fanName'
_R='temperatureName'
_Q='powerSupplyStatus'
_P='resourceConservationReason'
_O='raidIndex'
_N='updateIndex'
_M='keyExpirationIndex'
_L='fanIndex'
_K='not-accessible'
_J='temperatureIndex'
_I='powerSupplyIndex'
_H='memoryShortage'
_G='queueFull'
_F='queueSpaceShortage'
_E='hsmErrorReason'
_D='Integer32'
_C='ASYNCOS-MAIL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
asyncOSMail,=mibBuilder.importSymbols('IRONPORT-SMI','asyncOSMail')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
asyncOSMailObjects=ModuleIdentity((1,3,6,1,4,1,15497,1,1,1))
if mibBuilder.loadTexts:asyncOSMailObjects.setRevisions(('2011-03-07 00:00','2010-07-01 00:00','2009-04-07 00:00','2009-01-15 00:00','2005-03-07 00:00','2005-01-09 00:00'))
class _PerCentMemoryUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PerCentMemoryUtilization_Type.__name__=_D
_PerCentMemoryUtilization_Object=MibScalar
perCentMemoryUtilization=_PerCentMemoryUtilization_Object((1,3,6,1,4,1,15497,1,1,1,1),_PerCentMemoryUtilization_Type())
perCentMemoryUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:perCentMemoryUtilization.setStatus(_A)
class _PerCentCPUUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PerCentCPUUtilization_Type.__name__=_D
_PerCentCPUUtilization_Object=MibScalar
perCentCPUUtilization=_PerCentCPUUtilization_Object((1,3,6,1,4,1,15497,1,1,1,2),_PerCentCPUUtilization_Type())
perCentCPUUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:perCentCPUUtilization.setStatus(_A)
class _PerCentDiskIOUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PerCentDiskIOUtilization_Type.__name__=_D
_PerCentDiskIOUtilization_Object=MibScalar
perCentDiskIOUtilization=_PerCentDiskIOUtilization_Object((1,3,6,1,4,1,15497,1,1,1,3),_PerCentDiskIOUtilization_Type())
perCentDiskIOUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:perCentDiskIOUtilization.setStatus(_A)
class _PerCentQueueUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PerCentQueueUtilization_Type.__name__=_D
_PerCentQueueUtilization_Object=MibScalar
perCentQueueUtilization=_PerCentQueueUtilization_Object((1,3,6,1,4,1,15497,1,1,1,4),_PerCentQueueUtilization_Type())
perCentQueueUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:perCentQueueUtilization.setStatus(_A)
class _QueueAvailabilityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('queueSpaceAvailable',1),(_F,2),(_G,3)))
_QueueAvailabilityStatus_Type.__name__=_D
_QueueAvailabilityStatus_Object=MibScalar
queueAvailabilityStatus=_QueueAvailabilityStatus_Object((1,3,6,1,4,1,15497,1,1,1,5),_QueueAvailabilityStatus_Type())
queueAvailabilityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:queueAvailabilityStatus.setStatus(_A)
class _ResourceConservationReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noResourceConservation',1),(_H,2),(_F,3),(_G,4)))
_ResourceConservationReason_Type.__name__=_D
_ResourceConservationReason_Object=MibScalar
resourceConservationReason=_ResourceConservationReason_Object((1,3,6,1,4,1,15497,1,1,1,6),_ResourceConservationReason_Type())
resourceConservationReason.setMaxAccess(_B)
if mibBuilder.loadTexts:resourceConservationReason.setStatus(_A)
class _MemoryAvailabilityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('memoryAvailable',1),(_H,2),('memoryFull',3)))
_MemoryAvailabilityStatus_Type.__name__=_D
_MemoryAvailabilityStatus_Object=MibScalar
memoryAvailabilityStatus=_MemoryAvailabilityStatus_Object((1,3,6,1,4,1,15497,1,1,1,7),_MemoryAvailabilityStatus_Type())
memoryAvailabilityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryAvailabilityStatus.setStatus(_A)
_PowerSupplyTable_Object=MibTable
powerSupplyTable=_PowerSupplyTable_Object((1,3,6,1,4,1,15497,1,1,1,8))
if mibBuilder.loadTexts:powerSupplyTable.setStatus(_A)
_PowerSupplyEntry_Object=MibTableRow
powerSupplyEntry=_PowerSupplyEntry_Object((1,3,6,1,4,1,15497,1,1,1,8,1))
powerSupplyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:powerSupplyEntry.setStatus(_A)
class _PowerSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PowerSupplyIndex_Type.__name__=_D
_PowerSupplyIndex_Object=MibTableColumn
powerSupplyIndex=_PowerSupplyIndex_Object((1,3,6,1,4,1,15497,1,1,1,8,1,1),_PowerSupplyIndex_Type())
powerSupplyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyIndex.setStatus(_A)
class _PowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('powerSupplyNotInstalled',1),('powerSupplyHealthy',2),('powerSupplyNoAC',3),('powerSupplyFaulty',4)))
_PowerSupplyStatus_Type.__name__=_D
_PowerSupplyStatus_Object=MibTableColumn
powerSupplyStatus=_PowerSupplyStatus_Object((1,3,6,1,4,1,15497,1,1,1,8,1,2),_PowerSupplyStatus_Type())
powerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyStatus.setStatus(_A)
class _PowerSupplyRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerSupplyRedundancyOK',1),('powerSupplyRedundancyLost',2)))
_PowerSupplyRedundancy_Type.__name__=_D
_PowerSupplyRedundancy_Object=MibTableColumn
powerSupplyRedundancy=_PowerSupplyRedundancy_Object((1,3,6,1,4,1,15497,1,1,1,8,1,3),_PowerSupplyRedundancy_Type())
powerSupplyRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyRedundancy.setStatus(_A)
_PowerSupplyName_Type=DisplayString
_PowerSupplyName_Object=MibTableColumn
powerSupplyName=_PowerSupplyName_Object((1,3,6,1,4,1,15497,1,1,1,8,1,4),_PowerSupplyName_Type())
powerSupplyName.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSupplyName.setStatus(_A)
_TemperatureTable_Object=MibTable
temperatureTable=_TemperatureTable_Object((1,3,6,1,4,1,15497,1,1,1,9))
if mibBuilder.loadTexts:temperatureTable.setStatus(_A)
_TemperatureEntry_Object=MibTableRow
temperatureEntry=_TemperatureEntry_Object((1,3,6,1,4,1,15497,1,1,1,9,1))
temperatureEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:temperatureEntry.setStatus(_A)
class _TemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_TemperatureIndex_Type.__name__=_D
_TemperatureIndex_Object=MibTableColumn
temperatureIndex=_TemperatureIndex_Object((1,3,6,1,4,1,15497,1,1,1,9,1,1),_TemperatureIndex_Type())
temperatureIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:temperatureIndex.setStatus(_A)
_DegreesCelsius_Type=Integer32
_DegreesCelsius_Object=MibTableColumn
degreesCelsius=_DegreesCelsius_Object((1,3,6,1,4,1,15497,1,1,1,9,1,2),_DegreesCelsius_Type())
degreesCelsius.setMaxAccess(_B)
if mibBuilder.loadTexts:degreesCelsius.setStatus(_A)
_TemperatureName_Type=DisplayString
_TemperatureName_Object=MibTableColumn
temperatureName=_TemperatureName_Object((1,3,6,1,4,1,15497,1,1,1,9,1,3),_TemperatureName_Type())
temperatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:temperatureName.setStatus(_A)
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,15497,1,1,1,10))
if mibBuilder.loadTexts:fanTable.setStatus(_A)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,15497,1,1,1,10,1))
fanEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:fanEntry.setStatus(_A)
class _FanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_FanIndex_Type.__name__=_D
_FanIndex_Object=MibTableColumn
fanIndex=_FanIndex_Object((1,3,6,1,4,1,15497,1,1,1,10,1,1),_FanIndex_Type())
fanIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fanIndex.setStatus(_A)
_FanRPMs_Type=Gauge32
_FanRPMs_Object=MibTableColumn
fanRPMs=_FanRPMs_Object((1,3,6,1,4,1,15497,1,1,1,10,1,2),_FanRPMs_Type())
fanRPMs.setMaxAccess(_B)
if mibBuilder.loadTexts:fanRPMs.setStatus(_A)
_FanName_Type=DisplayString
_FanName_Object=MibTableColumn
fanName=_FanName_Object((1,3,6,1,4,1,15497,1,1,1,10,1,3),_FanName_Type())
fanName.setMaxAccess(_B)
if mibBuilder.loadTexts:fanName.setStatus(_A)
_WorkQueueMessages_Type=Gauge32
_WorkQueueMessages_Object=MibScalar
workQueueMessages=_WorkQueueMessages_Object((1,3,6,1,4,1,15497,1,1,1,11),_WorkQueueMessages_Type())
workQueueMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:workQueueMessages.setStatus(_A)
_KeyExpirationTable_Object=MibTable
keyExpirationTable=_KeyExpirationTable_Object((1,3,6,1,4,1,15497,1,1,1,12))
if mibBuilder.loadTexts:keyExpirationTable.setStatus(_A)
_KeyExpirationEntry_Object=MibTableRow
keyExpirationEntry=_KeyExpirationEntry_Object((1,3,6,1,4,1,15497,1,1,1,12,1))
keyExpirationEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:keyExpirationEntry.setStatus(_A)
class _KeyExpirationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_KeyExpirationIndex_Type.__name__=_D
_KeyExpirationIndex_Object=MibTableColumn
keyExpirationIndex=_KeyExpirationIndex_Object((1,3,6,1,4,1,15497,1,1,1,12,1,1),_KeyExpirationIndex_Type())
keyExpirationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:keyExpirationIndex.setStatus(_A)
_KeyDescription_Type=DisplayString
_KeyDescription_Object=MibTableColumn
keyDescription=_KeyDescription_Object((1,3,6,1,4,1,15497,1,1,1,12,1,2),_KeyDescription_Type())
keyDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:keyDescription.setStatus(_A)
_KeyIsPerpetual_Type=TruthValue
_KeyIsPerpetual_Object=MibTableColumn
keyIsPerpetual=_KeyIsPerpetual_Object((1,3,6,1,4,1,15497,1,1,1,12,1,3),_KeyIsPerpetual_Type())
keyIsPerpetual.setMaxAccess(_B)
if mibBuilder.loadTexts:keyIsPerpetual.setStatus(_A)
_KeySecondsUntilExpire_Type=Gauge32
_KeySecondsUntilExpire_Object=MibTableColumn
keySecondsUntilExpire=_KeySecondsUntilExpire_Object((1,3,6,1,4,1,15497,1,1,1,12,1,4),_KeySecondsUntilExpire_Type())
keySecondsUntilExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:keySecondsUntilExpire.setStatus(_A)
_UpdateTable_Object=MibTable
updateTable=_UpdateTable_Object((1,3,6,1,4,1,15497,1,1,1,13))
if mibBuilder.loadTexts:updateTable.setStatus(_A)
_UpdateEntry_Object=MibTableRow
updateEntry=_UpdateEntry_Object((1,3,6,1,4,1,15497,1,1,1,13,1))
updateEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:updateEntry.setStatus(_A)
class _UpdateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_UpdateIndex_Type.__name__=_D
_UpdateIndex_Object=MibTableColumn
updateIndex=_UpdateIndex_Object((1,3,6,1,4,1,15497,1,1,1,13,1,1),_UpdateIndex_Type())
updateIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:updateIndex.setStatus(_A)
_UpdateServiceName_Type=DisplayString
_UpdateServiceName_Object=MibTableColumn
updateServiceName=_UpdateServiceName_Object((1,3,6,1,4,1,15497,1,1,1,13,1,2),_UpdateServiceName_Type())
updateServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:updateServiceName.setStatus(_A)
_Updates_Type=Counter32
_Updates_Object=MibTableColumn
updates=_Updates_Object((1,3,6,1,4,1,15497,1,1,1,13,1,3),_Updates_Type())
updates.setMaxAccess(_B)
if mibBuilder.loadTexts:updates.setStatus(_A)
_UpdateFailures_Type=Counter32
_UpdateFailures_Object=MibTableColumn
updateFailures=_UpdateFailures_Object((1,3,6,1,4,1,15497,1,1,1,13,1,4),_UpdateFailures_Type())
updateFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:updateFailures.setStatus(_A)
_OldestMessageAge_Type=Gauge32
_OldestMessageAge_Object=MibScalar
oldestMessageAge=_OldestMessageAge_Object((1,3,6,1,4,1,15497,1,1,1,14),_OldestMessageAge_Type())
oldestMessageAge.setMaxAccess(_B)
if mibBuilder.loadTexts:oldestMessageAge.setStatus(_A)
_OutstandingDNSRequests_Type=Gauge32
_OutstandingDNSRequests_Object=MibScalar
outstandingDNSRequests=_OutstandingDNSRequests_Object((1,3,6,1,4,1,15497,1,1,1,15),_OutstandingDNSRequests_Type())
outstandingDNSRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:outstandingDNSRequests.setStatus(_A)
_PendingDNSRequests_Type=Gauge32
_PendingDNSRequests_Object=MibScalar
pendingDNSRequests=_PendingDNSRequests_Object((1,3,6,1,4,1,15497,1,1,1,16),_PendingDNSRequests_Type())
pendingDNSRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pendingDNSRequests.setStatus(_A)
_RaidEvents_Type=Counter32
_RaidEvents_Object=MibScalar
raidEvents=_RaidEvents_Object((1,3,6,1,4,1,15497,1,1,1,17),_RaidEvents_Type())
raidEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:raidEvents.setStatus(_A)
_RaidTable_Object=MibTable
raidTable=_RaidTable_Object((1,3,6,1,4,1,15497,1,1,1,18))
if mibBuilder.loadTexts:raidTable.setStatus(_A)
_RaidEntry_Object=MibTableRow
raidEntry=_RaidEntry_Object((1,3,6,1,4,1,15497,1,1,1,18,1))
raidEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:raidEntry.setStatus(_A)
class _RaidIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RaidIndex_Type.__name__=_D
_RaidIndex_Object=MibTableColumn
raidIndex=_RaidIndex_Object((1,3,6,1,4,1,15497,1,1,1,18,1,1),_RaidIndex_Type())
raidIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raidIndex.setStatus(_A)
class _RaidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('driveHealthy',1),('driveFailure',2),('driveRebuild',3)))
_RaidStatus_Type.__name__=_D
_RaidStatus_Object=MibTableColumn
raidStatus=_RaidStatus_Object((1,3,6,1,4,1,15497,1,1,1,18,1,2),_RaidStatus_Type())
raidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raidStatus.setStatus(_A)
_RaidID_Type=DisplayString
_RaidID_Object=MibTableColumn
raidID=_RaidID_Object((1,3,6,1,4,1,15497,1,1,1,18,1,3),_RaidID_Type())
raidID.setMaxAccess(_B)
if mibBuilder.loadTexts:raidID.setStatus(_A)
_RaidLastError_Type=DisplayString
_RaidLastError_Object=MibTableColumn
raidLastError=_RaidLastError_Object((1,3,6,1,4,1,15497,1,1,1,18,1,4),_RaidLastError_Type())
raidLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:raidLastError.setStatus(_A)
_OpenFilesOrSockets_Type=Gauge32
_OpenFilesOrSockets_Object=MibScalar
openFilesOrSockets=_OpenFilesOrSockets_Object((1,3,6,1,4,1,15497,1,1,1,19),_OpenFilesOrSockets_Type())
openFilesOrSockets.setMaxAccess(_B)
if mibBuilder.loadTexts:openFilesOrSockets.setStatus(_A)
_MailTransferThreads_Type=Gauge32
_MailTransferThreads_Object=MibScalar
mailTransferThreads=_MailTransferThreads_Object((1,3,6,1,4,1,15497,1,1,1,20),_MailTransferThreads_Type())
mailTransferThreads.setMaxAccess(_B)
if mibBuilder.loadTexts:mailTransferThreads.setStatus(_A)
_ConnectionURL_Type=DisplayString
_ConnectionURL_Object=MibScalar
connectionURL=_ConnectionURL_Object((1,3,6,1,4,1,15497,1,1,1,21),_ConnectionURL_Type())
connectionURL.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:connectionURL.setStatus(_A)
_HsmErrorReason_Type=DisplayString
_HsmErrorReason_Object=MibScalar
hsmErrorReason=_HsmErrorReason_Object((1,3,6,1,4,1,15497,1,1,1,22),_HsmErrorReason_Type())
hsmErrorReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hsmErrorReason.setStatus(_A)
_AsyncOSMailNotifications_ObjectIdentity=ObjectIdentity
asyncOSMailNotifications=_AsyncOSMailNotifications_ObjectIdentity((1,3,6,1,4,1,15497,1,1,2))
resourceConservationMode=NotificationType((1,3,6,1,4,1,15497,1,1,2,1))
resourceConservationMode.setObjects((_C,_P))
if mibBuilder.loadTexts:resourceConservationMode.setStatus(_A)
powerSupplyStatusChange=NotificationType((1,3,6,1,4,1,15497,1,1,2,2))
powerSupplyStatusChange.setObjects((_C,_Q))
if mibBuilder.loadTexts:powerSupplyStatusChange.setStatus(_A)
highTemperature=NotificationType((1,3,6,1,4,1,15497,1,1,2,3))
highTemperature.setObjects((_C,_R))
if mibBuilder.loadTexts:highTemperature.setStatus(_A)
fanFailure=NotificationType((1,3,6,1,4,1,15497,1,1,2,4))
fanFailure.setObjects((_C,_S))
if mibBuilder.loadTexts:fanFailure.setStatus(_A)
keyExpiration=NotificationType((1,3,6,1,4,1,15497,1,1,2,5))
keyExpiration.setObjects((_C,_T))
if mibBuilder.loadTexts:keyExpiration.setStatus(_A)
updateFailure=NotificationType((1,3,6,1,4,1,15497,1,1,2,6))
updateFailure.setObjects((_C,_U))
if mibBuilder.loadTexts:updateFailure.setStatus(_A)
raidStatusChange=NotificationType((1,3,6,1,4,1,15497,1,1,2,7))
raidStatusChange.setObjects((_C,_V))
if mibBuilder.loadTexts:raidStatusChange.setStatus(_A)
connectivityFailure=NotificationType((1,3,6,1,4,1,15497,1,1,2,8))
connectivityFailure.setObjects((_C,_W))
if mibBuilder.loadTexts:connectivityFailure.setStatus(_A)
memoryUtilizationExceeded=NotificationType((1,3,6,1,4,1,15497,1,1,2,9))
memoryUtilizationExceeded.setObjects((_C,_X))
if mibBuilder.loadTexts:memoryUtilizationExceeded.setStatus(_A)
cpuUtilizationExceeded=NotificationType((1,3,6,1,4,1,15497,1,1,2,10))
cpuUtilizationExceeded.setObjects((_C,_Y))
if mibBuilder.loadTexts:cpuUtilizationExceeded.setStatus(_A)
hsmInitializationFailure=NotificationType((1,3,6,1,4,1,15497,1,1,2,11))
hsmInitializationFailure.setObjects((_C,_E))
if mibBuilder.loadTexts:hsmInitializationFailure.setStatus(_A)
hsmResetLoginFailure=NotificationType((1,3,6,1,4,1,15497,1,1,2,12))
hsmResetLoginFailure.setObjects((_C,_E))
if mibBuilder.loadTexts:hsmResetLoginFailure.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'asyncOSMailObjects':asyncOSMailObjects,_X:perCentMemoryUtilization,_Y:perCentCPUUtilization,'perCentDiskIOUtilization':perCentDiskIOUtilization,'perCentQueueUtilization':perCentQueueUtilization,'queueAvailabilityStatus':queueAvailabilityStatus,_P:resourceConservationReason,'memoryAvailabilityStatus':memoryAvailabilityStatus,'powerSupplyTable':powerSupplyTable,'powerSupplyEntry':powerSupplyEntry,_I:powerSupplyIndex,_Q:powerSupplyStatus,'powerSupplyRedundancy':powerSupplyRedundancy,'powerSupplyName':powerSupplyName,'temperatureTable':temperatureTable,'temperatureEntry':temperatureEntry,_J:temperatureIndex,'degreesCelsius':degreesCelsius,_R:temperatureName,'fanTable':fanTable,'fanEntry':fanEntry,_L:fanIndex,'fanRPMs':fanRPMs,_S:fanName,'workQueueMessages':workQueueMessages,'keyExpirationTable':keyExpirationTable,'keyExpirationEntry':keyExpirationEntry,_M:keyExpirationIndex,_T:keyDescription,'keyIsPerpetual':keyIsPerpetual,'keySecondsUntilExpire':keySecondsUntilExpire,'updateTable':updateTable,'updateEntry':updateEntry,_N:updateIndex,_U:updateServiceName,'updates':updates,'updateFailures':updateFailures,'oldestMessageAge':oldestMessageAge,'outstandingDNSRequests':outstandingDNSRequests,'pendingDNSRequests':pendingDNSRequests,'raidEvents':raidEvents,'raidTable':raidTable,'raidEntry':raidEntry,_O:raidIndex,'raidStatus':raidStatus,_V:raidID,'raidLastError':raidLastError,'openFilesOrSockets':openFilesOrSockets,'mailTransferThreads':mailTransferThreads,_W:connectionURL,_E:hsmErrorReason,'asyncOSMailNotifications':asyncOSMailNotifications,'resourceConservationMode':resourceConservationMode,'powerSupplyStatusChange':powerSupplyStatusChange,'highTemperature':highTemperature,'fanFailure':fanFailure,'keyExpiration':keyExpiration,'updateFailure':updateFailure,'raidStatusChange':raidStatusChange,'connectivityFailure':connectivityFailure,'memoryUtilizationExceeded':memoryUtilizationExceeded,'cpuUtilizationExceeded':cpuUtilizationExceeded,'hsmInitializationFailure':hsmInitializationFailure,'hsmResetLoginFailure':hsmResetLoginFailure})