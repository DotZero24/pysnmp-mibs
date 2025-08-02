_F='logIndex'
_E='AT-LOG-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
log=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,601))
if mibBuilder.loadTexts:log.setRevisions(('2008-10-08 00:00',))
_LogTable_Object=MibTable
logTable=_LogTable_Object((1,3,6,1,4,1,207,8,4,4,4,601,1))
if mibBuilder.loadTexts:logTable.setStatus(_A)
_LogEntry_Object=MibTableRow
logEntry=_LogEntry_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1))
logEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:logEntry.setStatus(_A)
_LogIndex_Type=Unsigned32
_LogIndex_Object=MibTableColumn
logIndex=_LogIndex_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1,1),_LogIndex_Type())
logIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:logIndex.setStatus(_A)
_LogDate_Type=OctetString
_LogDate_Object=MibTableColumn
logDate=_LogDate_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1,2),_LogDate_Type())
logDate.setMaxAccess(_B)
if mibBuilder.loadTexts:logDate.setStatus(_A)
_LogTime_Type=OctetString
_LogTime_Object=MibTableColumn
logTime=_LogTime_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1,3),_LogTime_Type())
logTime.setMaxAccess(_B)
if mibBuilder.loadTexts:logTime.setStatus(_A)
_LogFacility_Type=OctetString
_LogFacility_Object=MibTableColumn
logFacility=_LogFacility_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1,4),_LogFacility_Type())
logFacility.setMaxAccess(_B)
if mibBuilder.loadTexts:logFacility.setStatus(_A)
_LogSeverity_Type=OctetString
_LogSeverity_Object=MibTableColumn
logSeverity=_LogSeverity_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1,5),_LogSeverity_Type())
logSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:logSeverity.setStatus(_A)
_LogProgram_Type=OctetString
_LogProgram_Object=MibTableColumn
logProgram=_LogProgram_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1,6),_LogProgram_Type())
logProgram.setMaxAccess(_B)
if mibBuilder.loadTexts:logProgram.setStatus(_A)
_LogMessage_Type=OctetString
_LogMessage_Object=MibTableColumn
logMessage=_LogMessage_Object((1,3,6,1,4,1,207,8,4,4,4,601,1,1,7),_LogMessage_Type())
logMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:logMessage.setStatus(_A)
_LogOptions_ObjectIdentity=ObjectIdentity
logOptions=_LogOptions_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,601,2))
class _LogSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_LogSource_Type.__name__=_C
_LogSource_Object=MibScalar
logSource=_LogSource_Object((1,3,6,1,4,1,207,8,4,4,4,601,2,1),_LogSource_Type())
logSource.setMaxAccess(_D)
if mibBuilder.loadTexts:logSource.setStatus(_A)
class _LogAll_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LogAll_Type.__name__=_C
_LogAll_Object=MibScalar
logAll=_LogAll_Object((1,3,6,1,4,1,207,8,4,4,4,601,2,2),_LogAll_Type())
logAll.setMaxAccess(_D)
if mibBuilder.loadTexts:logAll.setStatus(_A)
class _ClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ClearLog_Type.__name__=_C
_ClearLog_Object=MibScalar
clearLog=_ClearLog_Object((1,3,6,1,4,1,207,8,4,4,4,601,2,3),_ClearLog_Type())
clearLog.setMaxAccess(_D)
if mibBuilder.loadTexts:clearLog.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'log':log,'logTable':logTable,'logEntry':logEntry,_F:logIndex,'logDate':logDate,'logTime':logTime,'logFacility':logFacility,'logSeverity':logSeverity,'logProgram':logProgram,'logMessage':logMessage,'logOptions':logOptions,'logSource':logSource,'logAll':logAll,'clearLog':clearLog})