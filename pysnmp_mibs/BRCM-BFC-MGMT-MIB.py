_J='bfcEventIndex'
_I='bfcEventId'
_H='bfcAppIndex'
_G='Bytes'
_F='read-write'
_E='not-accessible'
_D='BRCM-BFC-MGMT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
bfcMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,9))
if mibBuilder.loadTexts:bfcMgmt.setRevisions(('2011-04-20 00:00','2010-02-01 00:00','2009-08-26 00:00','2009-06-30 00:00','2008-06-30 00:00','2007-02-05 00:00','2006-09-05 00:00','2005-05-05 00:00','2003-12-04 00:00'))
_BfcMgmtBase_ObjectIdentity=ObjectIdentity
bfcMgmtBase=_BfcMgmtBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1))
_BfcSoftware_ObjectIdentity=ObjectIdentity
bfcSoftware=_BfcSoftware_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,1))
_BfcSwDateTime_Type=DisplayString
_BfcSwDateTime_Object=MibScalar
bfcSwDateTime=_BfcSwDateTime_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,1),_BfcSwDateTime_Type())
bfcSwDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcSwDateTime.setStatus(_A)
_BfcSwBuiltBy_Type=DisplayString
_BfcSwBuiltBy_Object=MibScalar
bfcSwBuiltBy=_BfcSwBuiltBy_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,2),_BfcSwBuiltBy_Type())
bfcSwBuiltBy.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcSwBuiltBy.setStatus(_A)
_BfcSwOperatingSystem_Type=DisplayString
_BfcSwOperatingSystem_Object=MibScalar
bfcSwOperatingSystem=_BfcSwOperatingSystem_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,3),_BfcSwOperatingSystem_Type())
bfcSwOperatingSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcSwOperatingSystem.setStatus(_A)
_BfcSwSnmpAgent_Type=DisplayString
_BfcSwSnmpAgent_Object=MibScalar
bfcSwSnmpAgent=_BfcSwSnmpAgent_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,4),_BfcSwSnmpAgent_Type())
bfcSwSnmpAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcSwSnmpAgent.setStatus(_A)
_BfcApplicationTable_Object=MibTable
bfcApplicationTable=_BfcApplicationTable_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,5))
if mibBuilder.loadTexts:bfcApplicationTable.setStatus(_A)
_BfcApplicationEntry_Object=MibTableRow
bfcApplicationEntry=_BfcApplicationEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,5,1))
bfcApplicationEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:bfcApplicationEntry.setStatus(_A)
class _BfcAppIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_BfcAppIndex_Type.__name__=_C
_BfcAppIndex_Object=MibTableColumn
bfcAppIndex=_BfcAppIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,5,1,1),_BfcAppIndex_Type())
bfcAppIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bfcAppIndex.setStatus(_A)
_BfcAppName_Type=DisplayString
_BfcAppName_Object=MibTableColumn
bfcAppName=_BfcAppName_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,5,1,2),_BfcAppName_Type())
bfcAppName.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcAppName.setStatus(_A)
_BfcAppVersion_Type=DisplayString
_BfcAppVersion_Object=MibTableColumn
bfcAppVersion=_BfcAppVersion_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,5,1,3),_BfcAppVersion_Type())
bfcAppVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcAppVersion.setStatus(_A)
class _BfcAppReleaseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('release',1),('preRelease',2)))
_BfcAppReleaseState_Type.__name__=_C
_BfcAppReleaseState_Object=MibTableColumn
bfcAppReleaseState=_BfcAppReleaseState_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,5,1,4),_BfcAppReleaseState_Type())
bfcAppReleaseState.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcAppReleaseState.setStatus(_A)
_BfcAppFeatures_Type=DisplayString
_BfcAppFeatures_Object=MibTableColumn
bfcAppFeatures=_BfcAppFeatures_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,5,1,5),_BfcAppFeatures_Type())
bfcAppFeatures.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcAppFeatures.setStatus(_A)
_BfcSwNumBoots_Type=Unsigned32
_BfcSwNumBoots_Object=MibScalar
bfcSwNumBoots=_BfcSwNumBoots_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,6),_BfcSwNumBoots_Type())
bfcSwNumBoots.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcSwNumBoots.setStatus(_A)
_BfcSwImageName_Type=DisplayString
_BfcSwImageName_Object=MibScalar
bfcSwImageName=_BfcSwImageName_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,7),_BfcSwImageName_Type())
bfcSwImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcSwImageName.setStatus(_A)
_BfcSwImagePath_Type=DisplayString
_BfcSwImagePath_Object=MibScalar
bfcSwImagePath=_BfcSwImagePath_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,1,8),_BfcSwImagePath_Type())
bfcSwImagePath.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcSwImagePath.setStatus(_A)
_BfcSystem_ObjectIdentity=ObjectIdentity
bfcSystem=_BfcSystem_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,2))
class _BfcSerialConsoleMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('readOnly',1),('readWrite',2)))
_BfcSerialConsoleMode_Type.__name__=_C
_BfcSerialConsoleMode_Object=MibScalar
bfcSerialConsoleMode=_BfcSerialConsoleMode_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,2,1),_BfcSerialConsoleMode_Type())
bfcSerialConsoleMode.setMaxAccess(_F)
if mibBuilder.loadTexts:bfcSerialConsoleMode.setStatus(_A)
_BfcMemoryAvailable_Type=Gauge32
_BfcMemoryAvailable_Object=MibScalar
bfcMemoryAvailable=_BfcMemoryAvailable_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,2,2),_BfcMemoryAvailable_Type())
bfcMemoryAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcMemoryAvailable.setStatus(_A)
if mibBuilder.loadTexts:bfcMemoryAvailable.setUnits(_G)
_BfcMemoryLargestBlock_Type=Gauge32
_BfcMemoryLargestBlock_Object=MibScalar
bfcMemoryLargestBlock=_BfcMemoryLargestBlock_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,2,3),_BfcMemoryLargestBlock_Type())
bfcMemoryLargestBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcMemoryLargestBlock.setStatus(_A)
if mibBuilder.loadTexts:bfcMemoryLargestBlock.setUnits(_G)
_BfcMemoryLowWater_Type=Gauge32
_BfcMemoryLowWater_Object=MibScalar
bfcMemoryLowWater=_BfcMemoryLowWater_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,2,4),_BfcMemoryLowWater_Type())
bfcMemoryLowWater.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcMemoryLowWater.setStatus(_A)
if mibBuilder.loadTexts:bfcMemoryLowWater.setUnits(_G)
class _BfcMemoryFragmentation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BfcMemoryFragmentation_Type.__name__=_C
_BfcMemoryFragmentation_Object=MibScalar
bfcMemoryFragmentation=_BfcMemoryFragmentation_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,2,5),_BfcMemoryFragmentation_Type())
bfcMemoryFragmentation.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcMemoryFragmentation.setStatus(_A)
if mibBuilder.loadTexts:bfcMemoryFragmentation.setUnits('percent')
_BfcEventLog_ObjectIdentity=ObjectIdentity
bfcEventLog=_BfcEventLog_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,3))
_BfcEvents_ObjectIdentity=ObjectIdentity
bfcEvents=_BfcEvents_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,1))
_BfcSystemEvents_ObjectIdentity=ObjectIdentity
bfcSystemEvents=_BfcSystemEvents_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,1,1))
_BfcSystemEvent_ObjectIdentity=ObjectIdentity
bfcSystemEvent=_BfcSystemEvent_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,1,1,1))
if mibBuilder.loadTexts:bfcSystemEvent.setStatus(_A)
_BfcSystemResetEvent_ObjectIdentity=ObjectIdentity
bfcSystemResetEvent=_BfcSystemResetEvent_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,1,1,2))
if mibBuilder.loadTexts:bfcSystemResetEvent.setStatus(_A)
_BfcSystemTransientEvent_ObjectIdentity=ObjectIdentity
bfcSystemTransientEvent=_BfcSystemTransientEvent_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,1,1,3))
if mibBuilder.loadTexts:bfcSystemTransientEvent.setStatus(_A)
_BfcEventLogTable_Object=MibTable
bfcEventLogTable=_BfcEventLogTable_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,2))
if mibBuilder.loadTexts:bfcEventLogTable.setStatus(_A)
_BfcEventLogEntry_Object=MibTableRow
bfcEventLogEntry=_BfcEventLogEntry_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,2,1))
bfcEventLogEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:bfcEventLogEntry.setStatus(_A)
_BfcEventId_Type=AutonomousType
_BfcEventId_Object=MibTableColumn
bfcEventId=_BfcEventId_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,2,1,1),_BfcEventId_Type())
bfcEventId.setMaxAccess(_E)
if mibBuilder.loadTexts:bfcEventId.setStatus(_A)
class _BfcEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BfcEventIndex_Type.__name__=_C
_BfcEventIndex_Object=MibTableColumn
bfcEventIndex=_BfcEventIndex_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,2,1,2),_BfcEventIndex_Type())
bfcEventIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bfcEventIndex.setStatus(_A)
_BfcEventTime_Type=DateAndTime
_BfcEventTime_Object=MibTableColumn
bfcEventTime=_BfcEventTime_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,2,1,3),_BfcEventTime_Type())
bfcEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcEventTime.setStatus(_A)
_BfcEventText_Type=DisplayString
_BfcEventText_Object=MibTableColumn
bfcEventText=_BfcEventText_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,2,1,4),_BfcEventText_Type())
bfcEventText.setMaxAccess(_B)
if mibBuilder.loadTexts:bfcEventText.setStatus(_A)
_BfcEventLogReset_Type=TruthValue
_BfcEventLogReset_Object=MibScalar
bfcEventLogReset=_BfcEventLogReset_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,3),_BfcEventLogReset_Type())
bfcEventLogReset.setMaxAccess(_F)
if mibBuilder.loadTexts:bfcEventLogReset.setStatus(_A)
_BfcEventLogTransientEvent_Type=DisplayString
_BfcEventLogTransientEvent_Object=MibScalar
bfcEventLogTransientEvent=_BfcEventLogTransientEvent_Object((1,3,6,1,4,1,4413,2,2,2,1,9,1,3,4),_BfcEventLogTransientEvent_Type())
bfcEventLogTransientEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:bfcEventLogTransientEvent.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bfcMgmt':bfcMgmt,'bfcMgmtBase':bfcMgmtBase,'bfcSoftware':bfcSoftware,'bfcSwDateTime':bfcSwDateTime,'bfcSwBuiltBy':bfcSwBuiltBy,'bfcSwOperatingSystem':bfcSwOperatingSystem,'bfcSwSnmpAgent':bfcSwSnmpAgent,'bfcApplicationTable':bfcApplicationTable,'bfcApplicationEntry':bfcApplicationEntry,_H:bfcAppIndex,'bfcAppName':bfcAppName,'bfcAppVersion':bfcAppVersion,'bfcAppReleaseState':bfcAppReleaseState,'bfcAppFeatures':bfcAppFeatures,'bfcSwNumBoots':bfcSwNumBoots,'bfcSwImageName':bfcSwImageName,'bfcSwImagePath':bfcSwImagePath,'bfcSystem':bfcSystem,'bfcSerialConsoleMode':bfcSerialConsoleMode,'bfcMemoryAvailable':bfcMemoryAvailable,'bfcMemoryLargestBlock':bfcMemoryLargestBlock,'bfcMemoryLowWater':bfcMemoryLowWater,'bfcMemoryFragmentation':bfcMemoryFragmentation,'bfcEventLog':bfcEventLog,'bfcEvents':bfcEvents,'bfcSystemEvents':bfcSystemEvents,'bfcSystemEvent':bfcSystemEvent,'bfcSystemResetEvent':bfcSystemResetEvent,'bfcSystemTransientEvent':bfcSystemTransientEvent,'bfcEventLogTable':bfcEventLogTable,'bfcEventLogEntry':bfcEventLogEntry,_I:bfcEventId,_J:bfcEventIndex,'bfcEventTime':bfcEventTime,'bfcEventText':bfcEventText,'bfcEventLogReset':bfcEventLogReset,'bfcEventLogTransientEvent':bfcEventLogTransientEvent})