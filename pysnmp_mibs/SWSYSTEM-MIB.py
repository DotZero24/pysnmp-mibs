_R='swOperStatus'
_Q='swEventDescr'
_P='swEventRepeatCount'
_O='swEventLevel'
_N='swEventTimeInfo'
_M='informational'
_L='warning'
_K='critical'
_J='not-accessible'
_I='swSensorIndex'
_H='faulty'
_G='swEventIndex'
_F='seconds'
_E='SWSYSTEM-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SwPortIndex,SwSensorIndex=mibBuilder.importSymbols('Brocade-TC','SwPortIndex','SwSensorIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
sw,=mibBuilder.importSymbols('SWBASE-MIB','sw')
swSystem=ModuleIdentity((1,3,6,1,4,1,1588,2,1,1,1,1))
if mibBuilder.loadTexts:swSystem.setRevisions(('2019-03-20 17:00','2018-07-26 21:00','1911-04-15 18:30','1912-04-30 18:00','1916-09-23 10:30'))
class SwFwEvent(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('started',1),('changed',2),('exceeded',3),('below',4),('above',5),('inBetween',6),('lowBufferCrsd',7)))
class FcPortFlag(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('physical',0),('virtual',1)))
_SwTrapsV2_ObjectIdentity=ObjectIdentity
swTrapsV2=_SwTrapsV2_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,0))
if mibBuilder.loadTexts:swTrapsV2.setStatus(_A)
class _SwCurrentDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwCurrentDate_Type.__name__=_D
_SwCurrentDate_Object=MibScalar
swCurrentDate=_SwCurrentDate_Object((1,3,6,1,4,1,1588,2,1,1,1,1,1),_SwCurrentDate_Type())
swCurrentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:swCurrentDate.setStatus(_A)
class _SwBootDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwBootDate_Type.__name__=_D
_SwBootDate_Object=MibScalar
swBootDate=_SwBootDate_Object((1,3,6,1,4,1,1588,2,1,1,1,1,2),_SwBootDate_Type())
swBootDate.setMaxAccess(_B)
if mibBuilder.loadTexts:swBootDate.setStatus(_A)
class _SwFWLastUpdated_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwFWLastUpdated_Type.__name__=_D
_SwFWLastUpdated_Object=MibScalar
swFWLastUpdated=_SwFWLastUpdated_Object((1,3,6,1,4,1,1588,2,1,1,1,1,3),_SwFWLastUpdated_Type())
swFWLastUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:swFWLastUpdated.setStatus(_A)
class _SwFlashLastUpdated_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwFlashLastUpdated_Type.__name__=_D
_SwFlashLastUpdated_Object=MibScalar
swFlashLastUpdated=_SwFlashLastUpdated_Object((1,3,6,1,4,1,1588,2,1,1,1,1,4),_SwFlashLastUpdated_Type())
swFlashLastUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:swFlashLastUpdated.setStatus(_A)
class _SwBootPromLastUpdated_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwBootPromLastUpdated_Type.__name__=_D
_SwBootPromLastUpdated_Object=MibScalar
swBootPromLastUpdated=_SwBootPromLastUpdated_Object((1,3,6,1,4,1,1588,2,1,1,1,1,5),_SwBootPromLastUpdated_Type())
swBootPromLastUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:swBootPromLastUpdated.setStatus(_A)
class _SwFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_SwFirmwareVersion_Type.__name__=_D
_SwFirmwareVersion_Object=MibScalar
swFirmwareVersion=_SwFirmwareVersion_Object((1,3,6,1,4,1,1588,2,1,1,1,1,6),_SwFirmwareVersion_Type())
swFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swFirmwareVersion.setStatus(_A)
class _SwOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('online',1),('offline',2),('testing',3),(_H,4)))
_SwOperStatus_Type.__name__=_C
_SwOperStatus_Object=MibScalar
swOperStatus=_SwOperStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,7),_SwOperStatus_Type())
swOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swOperStatus.setStatus(_A)
class _SwSsn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwSsn_Type.__name__=_D
_SwSsn_Object=MibScalar
swSsn=_SwSsn_Object((1,3,6,1,4,1,1588,2,1,1,1,1,10),_SwSsn_Type())
swSsn.setMaxAccess(_B)
if mibBuilder.loadTexts:swSsn.setStatus(_A)
class _SwBeaconOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_SwBeaconOperStatus_Type.__name__=_C
_SwBeaconOperStatus_Object=MibScalar
swBeaconOperStatus=_SwBeaconOperStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,18),_SwBeaconOperStatus_Type())
swBeaconOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swBeaconOperStatus.setStatus(_A)
class _SwBeaconAdmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_SwBeaconAdmStatus_Type.__name__=_C
_SwBeaconAdmStatus_Object=MibScalar
swBeaconAdmStatus=_SwBeaconAdmStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,19),_SwBeaconAdmStatus_Type())
swBeaconAdmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swBeaconAdmStatus.setStatus(_A)
class _SwDiagResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sw-ok',1),('sw-faulty',2),('sw-embedded-port-fault',3)))
_SwDiagResult_Type.__name__=_C
_SwDiagResult_Object=MibScalar
swDiagResult=_SwDiagResult_Object((1,3,6,1,4,1,1588,2,1,1,1,1,20),_SwDiagResult_Type())
swDiagResult.setMaxAccess(_B)
if mibBuilder.loadTexts:swDiagResult.setStatus(_A)
class _SwNumSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwNumSensors_Type.__name__=_C
_SwNumSensors_Object=MibScalar
swNumSensors=_SwNumSensors_Object((1,3,6,1,4,1,1588,2,1,1,1,1,21),_SwNumSensors_Type())
swNumSensors.setMaxAccess(_B)
if mibBuilder.loadTexts:swNumSensors.setStatus(_A)
_SwSensorTable_Object=MibTable
swSensorTable=_SwSensorTable_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22))
if mibBuilder.loadTexts:swSensorTable.setStatus(_A)
_SwSensorEntry_Object=MibTableRow
swSensorEntry=_SwSensorEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1))
swSensorEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:swSensorEntry.setStatus(_A)
_SwSensorIndex_Type=SwSensorIndex
_SwSensorIndex_Object=MibTableColumn
swSensorIndex=_SwSensorIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,1),_SwSensorIndex_Type())
swSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorIndex.setStatus(_A)
class _SwSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('temperature',1),('fan',2),('power-supply',3)))
_SwSensorType_Type.__name__=_C
_SwSensorType_Object=MibTableColumn
swSensorType=_SwSensorType_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,2),_SwSensorType_Type())
swSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorType.setStatus(_A)
class _SwSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),(_H,2),('below-min',3),('nominal',4),('above-max',5),('absent',6)))
_SwSensorStatus_Type.__name__=_C
_SwSensorStatus_Object=MibTableColumn
swSensorStatus=_SwSensorStatus_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,3),_SwSensorStatus_Type())
swSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorStatus.setStatus(_A)
_SwSensorValue_Type=Integer32
_SwSensorValue_Object=MibTableColumn
swSensorValue=_SwSensorValue_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,4),_SwSensorValue_Type())
swSensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorValue.setStatus(_A)
class _SwSensorInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwSensorInfo_Type.__name__=_D
_SwSensorInfo_Object=MibTableColumn
swSensorInfo=_SwSensorInfo_Object((1,3,6,1,4,1,1588,2,1,1,1,1,22,1,5),_SwSensorInfo_Type())
swSensorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:swSensorInfo.setStatus(_A)
_SwID_Type=Integer32
_SwID_Object=MibScalar
swID=_SwID_Object((1,3,6,1,4,1,1588,2,1,1,1,1,24),_SwID_Type())
swID.setMaxAccess(_B)
if mibBuilder.loadTexts:swID.setStatus(_A)
_SwEtherIPAddress_Type=IpAddress
_SwEtherIPAddress_Object=MibScalar
swEtherIPAddress=_SwEtherIPAddress_Object((1,3,6,1,4,1,1588,2,1,1,1,1,25),_SwEtherIPAddress_Type())
swEtherIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherIPAddress.setStatus(_A)
_SwEtherIPMask_Type=IpAddress
_SwEtherIPMask_Object=MibScalar
swEtherIPMask=_SwEtherIPMask_Object((1,3,6,1,4,1,1588,2,1,1,1,1,26),_SwEtherIPMask_Type())
swEtherIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:swEtherIPMask.setStatus(_A)
_SwIPv6Address_Type=DisplayString
_SwIPv6Address_Object=MibScalar
swIPv6Address=_SwIPv6Address_Object((1,3,6,1,4,1,1588,2,1,1,1,1,29),_SwIPv6Address_Type())
swIPv6Address.setMaxAccess(_J)
if mibBuilder.loadTexts:swIPv6Address.setStatus(_A)
class _SwIPv6Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tentative',1),('preferred',2),('ipdeprecated',3),('inactive',4)))
_SwIPv6Status_Type.__name__=_C
_SwIPv6Status_Object=MibScalar
swIPv6Status=_SwIPv6Status_Object((1,3,6,1,4,1,1588,2,1,1,1,1,30),_SwIPv6Status_Type())
swIPv6Status.setMaxAccess(_J)
if mibBuilder.loadTexts:swIPv6Status.setStatus(_A)
_SwEvent_ObjectIdentity=ObjectIdentity
swEvent=_SwEvent_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,8))
if mibBuilder.loadTexts:swEvent.setStatus(_A)
class _SwEventTrapLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),(_K,1),('error',2),(_L,3),(_M,4),('debug',5)))
_SwEventTrapLevel_Type.__name__=_C
_SwEventTrapLevel_Object=MibScalar
swEventTrapLevel=_SwEventTrapLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,8,1),_SwEventTrapLevel_Type())
swEventTrapLevel.setMaxAccess('read-write')
if mibBuilder.loadTexts:swEventTrapLevel.setStatus('deprecated')
class _SwEventNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEventNumEntries_Type.__name__=_C
_SwEventNumEntries_Object=MibScalar
swEventNumEntries=_SwEventNumEntries_Object((1,3,6,1,4,1,1588,2,1,1,1,8,4),_SwEventNumEntries_Type())
swEventNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventNumEntries.setStatus(_A)
_SwEventTable_Object=MibTable
swEventTable=_SwEventTable_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5))
if mibBuilder.loadTexts:swEventTable.setStatus(_A)
_SwEventEntry_Object=MibTableRow
swEventEntry=_SwEventEntry_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1))
swEventEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:swEventEntry.setStatus(_A)
class _SwEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEventIndex_Type.__name__=_C
_SwEventIndex_Object=MibTableColumn
swEventIndex=_SwEventIndex_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,1),_SwEventIndex_Type())
swEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventIndex.setStatus(_A)
class _SwEventTimeInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwEventTimeInfo_Type.__name__=_D
_SwEventTimeInfo_Object=MibTableColumn
swEventTimeInfo=_SwEventTimeInfo_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,2),_SwEventTimeInfo_Type())
swEventTimeInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventTimeInfo.setStatus(_A)
class _SwEventLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('error',2),(_L,3),(_M,4),('debug',5)))
_SwEventLevel_Type.__name__=_C
_SwEventLevel_Object=MibTableColumn
swEventLevel=_SwEventLevel_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,3),_SwEventLevel_Type())
swEventLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventLevel.setStatus(_A)
class _SwEventRepeatCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwEventRepeatCount_Type.__name__=_C
_SwEventRepeatCount_Object=MibTableColumn
swEventRepeatCount=_SwEventRepeatCount_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,4),_SwEventRepeatCount_Type())
swEventRepeatCount.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventRepeatCount.setStatus(_A)
_SwEventDescr_Type=DisplayString
_SwEventDescr_Object=MibTableColumn
swEventDescr=_SwEventDescr_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,5),_SwEventDescr_Type())
swEventDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventDescr.setStatus(_A)
class _SwEventVfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwEventVfId_Type.__name__=_C
_SwEventVfId_Object=MibTableColumn
swEventVfId=_SwEventVfId_Object((1,3,6,1,4,1,1588,2,1,1,1,8,5,1,6),_SwEventVfId_Type())
swEventVfId.setMaxAccess(_B)
if mibBuilder.loadTexts:swEventVfId.setStatus(_A)
_SwCpuOrMemoryUsage_ObjectIdentity=ObjectIdentity
swCpuOrMemoryUsage=_SwCpuOrMemoryUsage_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,1,26))
if mibBuilder.loadTexts:swCpuOrMemoryUsage.setStatus(_A)
class _SwCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwCpuUsage_Type.__name__=_C
_SwCpuUsage_Object=MibScalar
swCpuUsage=_SwCpuUsage_Object((1,3,6,1,4,1,1588,2,1,1,1,26,1),_SwCpuUsage_Type())
swCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuUsage.setStatus(_A)
class _SwCpuNoOfRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwCpuNoOfRetries_Type.__name__=_C
_SwCpuNoOfRetries_Object=MibScalar
swCpuNoOfRetries=_SwCpuNoOfRetries_Object((1,3,6,1,4,1,1588,2,1,1,1,26,2),_SwCpuNoOfRetries_Type())
swCpuNoOfRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuNoOfRetries.setStatus(_A)
class _SwCpuUsageLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwCpuUsageLimit_Type.__name__=_C
_SwCpuUsageLimit_Object=MibScalar
swCpuUsageLimit=_SwCpuUsageLimit_Object((1,3,6,1,4,1,1588,2,1,1,1,26,3),_SwCpuUsageLimit_Type())
swCpuUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuUsageLimit.setStatus(_A)
class _SwCpuPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_SwCpuPollingInterval_Type.__name__=_C
_SwCpuPollingInterval_Object=MibScalar
swCpuPollingInterval=_SwCpuPollingInterval_Object((1,3,6,1,4,1,1588,2,1,1,1,26,4),_SwCpuPollingInterval_Type())
swCpuPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuPollingInterval.setStatus(_A)
if mibBuilder.loadTexts:swCpuPollingInterval.setUnits(_F)
class _SwCpuAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwCpuAction_Type.__name__=_C
_SwCpuAction_Object=MibScalar
swCpuAction=_SwCpuAction_Object((1,3,6,1,4,1,1588,2,1,1,1,26,5),_SwCpuAction_Type())
swCpuAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swCpuAction.setStatus(_A)
if mibBuilder.loadTexts:swCpuAction.setUnits(_F)
_SwMemUsage_Type=Integer32
_SwMemUsage_Object=MibScalar
swMemUsage=_SwMemUsage_Object((1,3,6,1,4,1,1588,2,1,1,1,26,6),_SwMemUsage_Type())
swMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsage.setStatus(_A)
class _SwMemNoOfRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SwMemNoOfRetries_Type.__name__=_C
_SwMemNoOfRetries_Object=MibScalar
swMemNoOfRetries=_SwMemNoOfRetries_Object((1,3,6,1,4,1,1588,2,1,1,1,26,7),_SwMemNoOfRetries_Type())
swMemNoOfRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemNoOfRetries.setStatus(_A)
_SwMemUsageLimit_Type=Integer32
_SwMemUsageLimit_Object=MibScalar
swMemUsageLimit=_SwMemUsageLimit_Object((1,3,6,1,4,1,1588,2,1,1,1,26,8),_SwMemUsageLimit_Type())
swMemUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemUsageLimit.setStatus(_A)
class _SwMemPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_SwMemPollingInterval_Type.__name__=_C
_SwMemPollingInterval_Object=MibScalar
swMemPollingInterval=_SwMemPollingInterval_Object((1,3,6,1,4,1,1588,2,1,1,1,26,9),_SwMemPollingInterval_Type())
swMemPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemPollingInterval.setStatus(_A)
if mibBuilder.loadTexts:swMemPollingInterval.setUnits(_F)
class _SwMemAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwMemAction_Type.__name__=_C
_SwMemAction_Object=MibScalar
swMemAction=_SwMemAction_Object((1,3,6,1,4,1,1588,2,1,1,1,26,10),_SwMemAction_Type())
swMemAction.setMaxAccess(_B)
if mibBuilder.loadTexts:swMemAction.setStatus(_A)
if mibBuilder.loadTexts:swMemAction.setUnits(_F)
swEventTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,4))
swEventTrap.setObjects(*((_E,_G),(_E,_N),(_E,_O),(_E,_P),(_E,_Q),(_E,'swSsn')))
if mibBuilder.loadTexts:swEventTrap.setStatus(_A)
swStateChangeTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,1,0,12))
swStateChangeTrap.setObjects((_E,_R))
if mibBuilder.loadTexts:swStateChangeTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'FcPortFlag':FcPortFlag,'SwFwEvent':SwFwEvent,'swTrapsV2':swTrapsV2,'swEventTrap':swEventTrap,'swStateChangeTrap':swStateChangeTrap,'swSystem':swSystem,'swCurrentDate':swCurrentDate,'swBootDate':swBootDate,'swFWLastUpdated':swFWLastUpdated,'swFlashLastUpdated':swFlashLastUpdated,'swBootPromLastUpdated':swBootPromLastUpdated,'swFirmwareVersion':swFirmwareVersion,_R:swOperStatus,'swSsn':swSsn,'swBeaconOperStatus':swBeaconOperStatus,'swBeaconAdmStatus':swBeaconAdmStatus,'swDiagResult':swDiagResult,'swNumSensors':swNumSensors,'swSensorTable':swSensorTable,'swSensorEntry':swSensorEntry,_I:swSensorIndex,'swSensorType':swSensorType,'swSensorStatus':swSensorStatus,'swSensorValue':swSensorValue,'swSensorInfo':swSensorInfo,'swID':swID,'swEtherIPAddress':swEtherIPAddress,'swEtherIPMask':swEtherIPMask,'swIPv6Address':swIPv6Address,'swIPv6Status':swIPv6Status,'swEvent':swEvent,'swEventTrapLevel':swEventTrapLevel,'swEventNumEntries':swEventNumEntries,'swEventTable':swEventTable,'swEventEntry':swEventEntry,_G:swEventIndex,_N:swEventTimeInfo,_O:swEventLevel,_P:swEventRepeatCount,_Q:swEventDescr,'swEventVfId':swEventVfId,'swCpuOrMemoryUsage':swCpuOrMemoryUsage,'swCpuUsage':swCpuUsage,'swCpuNoOfRetries':swCpuNoOfRetries,'swCpuUsageLimit':swCpuUsageLimit,'swCpuPollingInterval':swCpuPollingInterval,'swCpuAction':swCpuAction,'swMemUsage':swMemUsage,'swMemNoOfRetries':swMemNoOfRetries,'swMemUsageLimit':swMemUsageLimit,'swMemPollingInterval':swMemPollingInterval,'swMemAction':swMemAction})