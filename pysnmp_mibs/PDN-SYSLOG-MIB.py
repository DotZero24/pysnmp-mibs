_b='pdnSyslogGroup'
_a='pdnSyslogLevel'
_Z='pdnEntitySyslogMessage'
_Y='pdnSyslogRateLimiting'
_X='pdnSyslogMsgToConsole'
_W='pdnSyslogClearTable'
_V='pdnSyslogMaxTableSize'
_U='pdnSyslogNumOfMsgInTable'
_T='pdnSyslogMessage'
_S='pdnSyslogRemoteDaemon'
_R='pdnSyslogSeverityThreshold'
_Q='pdnSyslogPort'
_P='pdnSyslogIPAddr'
_O='pdnSyslogStatus'
_N='pdnEntitySyslogNumber'
_M='not-accessible'
_L='pdnSyslogNumber'
_K='deprecated'
_J='entPhysicalIndex'
_I='ENTITY-MIB'
_H='OctetString'
_G='read-only'
_F='enable'
_E='disable'
_D='read-write'
_C='Integer32'
_B='PDN-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_I,_J)
pdn_syslog,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-syslog')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnSyslog=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,31,1))
if mibBuilder.loadTexts:pdnSyslog.setRevisions(('2003-02-13 00:00','2001-11-15 00:00','2001-04-10 00:00','2001-08-09 00:00','2000-04-24 00:00','2000-02-05 00:00'))
class _PdnSyslogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PdnSyslogStatus_Type.__name__=_C
_PdnSyslogStatus_Object=MibScalar
pdnSyslogStatus=_PdnSyslogStatus_Object((1,3,6,1,4,1,1795,2,24,2,31,1,1),_PdnSyslogStatus_Type())
pdnSyslogStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogStatus.setStatus(_A)
_PdnSyslogIPAddr_Type=IpAddress
_PdnSyslogIPAddr_Object=MibScalar
pdnSyslogIPAddr=_PdnSyslogIPAddr_Object((1,3,6,1,4,1,1795,2,24,2,31,1,2),_PdnSyslogIPAddr_Type())
pdnSyslogIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogIPAddr.setStatus(_A)
class _PdnSyslogLevel_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('emerg',1),('err',2),('norm',3),('info',4)))
_PdnSyslogLevel_Type.__name__=_C
_PdnSyslogLevel_Object=MibScalar
pdnSyslogLevel=_PdnSyslogLevel_Object((1,3,6,1,4,1,1795,2,24,2,31,1,3),_PdnSyslogLevel_Type())
pdnSyslogLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogLevel.setStatus(_K)
class _PdnSyslogPort_Type(Integer32):defaultValue=514
_PdnSyslogPort_Type.__name__=_C
_PdnSyslogPort_Object=MibScalar
pdnSyslogPort=_PdnSyslogPort_Object((1,3,6,1,4,1,1795,2,24,2,31,1,4),_PdnSyslogPort_Type())
pdnSyslogPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogPort.setStatus(_A)
class _PdnSyslogSeverityThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emerg',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_PdnSyslogSeverityThreshold_Type.__name__=_C
_PdnSyslogSeverityThreshold_Object=MibScalar
pdnSyslogSeverityThreshold=_PdnSyslogSeverityThreshold_Object((1,3,6,1,4,1,1795,2,24,2,31,1,5),_PdnSyslogSeverityThreshold_Type())
pdnSyslogSeverityThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogSeverityThreshold.setStatus(_A)
class _PdnSyslogRemoteDaemon_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PdnSyslogRemoteDaemon_Type.__name__=_C
_PdnSyslogRemoteDaemon_Object=MibScalar
pdnSyslogRemoteDaemon=_PdnSyslogRemoteDaemon_Object((1,3,6,1,4,1,1795,2,24,2,31,1,6),_PdnSyslogRemoteDaemon_Type())
pdnSyslogRemoteDaemon.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogRemoteDaemon.setStatus(_A)
_PdnSyslogTable_Object=MibTable
pdnSyslogTable=_PdnSyslogTable_Object((1,3,6,1,4,1,1795,2,24,2,31,1,7))
if mibBuilder.loadTexts:pdnSyslogTable.setStatus(_A)
_PdnSyslogEntry_Object=MibTableRow
pdnSyslogEntry=_PdnSyslogEntry_Object((1,3,6,1,4,1,1795,2,24,2,31,1,7,1))
pdnSyslogEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:pdnSyslogEntry.setStatus(_A)
_PdnSyslogNumber_Type=Integer32
_PdnSyslogNumber_Object=MibTableColumn
pdnSyslogNumber=_PdnSyslogNumber_Object((1,3,6,1,4,1,1795,2,24,2,31,1,7,1,1),_PdnSyslogNumber_Type())
pdnSyslogNumber.setMaxAccess(_M)
if mibBuilder.loadTexts:pdnSyslogNumber.setStatus(_A)
class _PdnSyslogMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1024,1024));fixedLength=1024
_PdnSyslogMessage_Type.__name__=_H
_PdnSyslogMessage_Object=MibTableColumn
pdnSyslogMessage=_PdnSyslogMessage_Object((1,3,6,1,4,1,1795,2,24,2,31,1,7,1,2),_PdnSyslogMessage_Type())
pdnSyslogMessage.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnSyslogMessage.setStatus(_A)
_PdnSyslogNumOfMsgInTable_Type=Integer32
_PdnSyslogNumOfMsgInTable_Object=MibScalar
pdnSyslogNumOfMsgInTable=_PdnSyslogNumOfMsgInTable_Object((1,3,6,1,4,1,1795,2,24,2,31,1,8),_PdnSyslogNumOfMsgInTable_Type())
pdnSyslogNumOfMsgInTable.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnSyslogNumOfMsgInTable.setStatus(_A)
_PdnSyslogMaxTableSize_Type=Integer32
_PdnSyslogMaxTableSize_Object=MibScalar
pdnSyslogMaxTableSize=_PdnSyslogMaxTableSize_Object((1,3,6,1,4,1,1795,2,24,2,31,1,9),_PdnSyslogMaxTableSize_Type())
pdnSyslogMaxTableSize.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnSyslogMaxTableSize.setStatus(_A)
class _PdnSyslogClearTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('clear',2)))
_PdnSyslogClearTable_Type.__name__=_C
_PdnSyslogClearTable_Object=MibScalar
pdnSyslogClearTable=_PdnSyslogClearTable_Object((1,3,6,1,4,1,1795,2,24,2,31,1,10),_PdnSyslogClearTable_Type())
pdnSyslogClearTable.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogClearTable.setStatus(_A)
class _PdnSyslogMsgToConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PdnSyslogMsgToConsole_Type.__name__=_C
_PdnSyslogMsgToConsole_Object=MibScalar
pdnSyslogMsgToConsole=_PdnSyslogMsgToConsole_Object((1,3,6,1,4,1,1795,2,24,2,31,1,11),_PdnSyslogMsgToConsole_Type())
pdnSyslogMsgToConsole.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogMsgToConsole.setStatus(_A)
class _PdnSyslogRateLimiting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PdnSyslogRateLimiting_Type.__name__=_C
_PdnSyslogRateLimiting_Object=MibScalar
pdnSyslogRateLimiting=_PdnSyslogRateLimiting_Object((1,3,6,1,4,1,1795,2,24,2,31,1,12),_PdnSyslogRateLimiting_Type())
pdnSyslogRateLimiting.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnSyslogRateLimiting.setStatus(_A)
_PdnEntitySyslogTable_Object=MibTable
pdnEntitySyslogTable=_PdnEntitySyslogTable_Object((1,3,6,1,4,1,1795,2,24,2,31,1,13))
if mibBuilder.loadTexts:pdnEntitySyslogTable.setStatus(_A)
_PdnEntitySyslogEntry_Object=MibTableRow
pdnEntitySyslogEntry=_PdnEntitySyslogEntry_Object((1,3,6,1,4,1,1795,2,24,2,31,1,13,1))
pdnEntitySyslogEntry.setIndexNames((0,_I,_J),(0,_B,_N))
if mibBuilder.loadTexts:pdnEntitySyslogEntry.setStatus(_A)
_PdnEntitySyslogNumber_Type=Integer32
_PdnEntitySyslogNumber_Object=MibTableColumn
pdnEntitySyslogNumber=_PdnEntitySyslogNumber_Object((1,3,6,1,4,1,1795,2,24,2,31,1,13,1,1),_PdnEntitySyslogNumber_Type())
pdnEntitySyslogNumber.setMaxAccess(_M)
if mibBuilder.loadTexts:pdnEntitySyslogNumber.setStatus(_A)
class _PdnEntitySyslogMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1024,1024));fixedLength=1024
_PdnEntitySyslogMessage_Type.__name__=_H
_PdnEntitySyslogMessage_Object=MibTableColumn
pdnEntitySyslogMessage=_PdnEntitySyslogMessage_Object((1,3,6,1,4,1,1795,2,24,2,31,1,13,1,2),_PdnEntitySyslogMessage_Type())
pdnEntitySyslogMessage.setMaxAccess(_G)
if mibBuilder.loadTexts:pdnEntitySyslogMessage.setStatus(_A)
_PdnSyslogConformance_ObjectIdentity=ObjectIdentity
pdnSyslogConformance=_PdnSyslogConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,31,14))
_PdnSyslogCompliances_ObjectIdentity=ObjectIdentity
pdnSyslogCompliances=_PdnSyslogCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,31,14,1))
_PdnSyslogGroups_ObjectIdentity=ObjectIdentity
pdnSyslogGroups=_PdnSyslogGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,31,14,2))
pdnSyslogGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,31,14,2,1))
pdnSyslogGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:pdnSyslogGroup.setStatus(_A)
pdnSyslogOptionalGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,31,14,2,2))
pdnSyslogOptionalGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:pdnSyslogOptionalGroup.setStatus(_A)
pdnSyslogDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,31,14,2,3))
pdnSyslogDeprecatedGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:pdnSyslogDeprecatedGroup.setStatus(_K)
pdnSyslogCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,31,14,1,1))
pdnSyslogCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:pdnSyslogCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnSyslog':pdnSyslog,_O:pdnSyslogStatus,_P:pdnSyslogIPAddr,_a:pdnSyslogLevel,_Q:pdnSyslogPort,_R:pdnSyslogSeverityThreshold,_S:pdnSyslogRemoteDaemon,'pdnSyslogTable':pdnSyslogTable,'pdnSyslogEntry':pdnSyslogEntry,_L:pdnSyslogNumber,_T:pdnSyslogMessage,_U:pdnSyslogNumOfMsgInTable,_V:pdnSyslogMaxTableSize,_W:pdnSyslogClearTable,_X:pdnSyslogMsgToConsole,_Y:pdnSyslogRateLimiting,'pdnEntitySyslogTable':pdnEntitySyslogTable,'pdnEntitySyslogEntry':pdnEntitySyslogEntry,_N:pdnEntitySyslogNumber,_Z:pdnEntitySyslogMessage,'pdnSyslogConformance':pdnSyslogConformance,'pdnSyslogCompliances':pdnSyslogCompliances,'pdnSyslogCompliance':pdnSyslogCompliance,'pdnSyslogGroups':pdnSyslogGroups,_b:pdnSyslogGroup,'pdnSyslogOptionalGroup':pdnSyslogOptionalGroup,'pdnSyslogDeprecatedGroup':pdnSyslogDeprecatedGroup})