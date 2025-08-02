_O='infinetSyslogMessageGenerated'
_N='infinetSyslogServerAddress'
_M='DisplayString'
_L='sysTrapSequence'
_K='sysSerialNumber'
_J='infinetSyslogMessageIdentity'
_I='infinetSyslogMessageTimestamp'
_H='infinetSyslogMessageFacility'
_G='infinetSyslogMessageText'
_F='infinetSyslogMessageSeverity'
_E='AQUASYSTEM-MIB'
_D='infinetSyslogMessageIndex'
_C='read-only'
_B='current'
_A='INFINET-SYSLOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysSerialNumber,sysTrapSequence=mibBuilder.importSymbols(_E,_K,_L)
wanflex,=mibBuilder.importSymbols('INFINET-MIB','wanflex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'PhysAddress','TextualConvention')
infinetSyslogMIB=ModuleIdentity((1,3,6,1,4,1,3942,1,1,6))
if mibBuilder.loadTexts:infinetSyslogMIB.setRevisions(('2008-02-07 11:36',))
class InfinetSyslogFacility(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('user',1),('mail',2),('daemon',3),('authentication',4),('syslog',5),('lpr',6),('news',7),('uucp',8),('cron',9),('authpriv',10),('ftp',11),('ntp',12),('security',13),('console',14),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
class InfinetSyslogSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_InfinetSyslogObjects_ObjectIdentity=ObjectIdentity
infinetSyslogObjects=_InfinetSyslogObjects_ObjectIdentity((1,3,6,1,4,1,3942,1,1,6,1))
_InfinetSyslogServerAddress_Type=IpAddress
_InfinetSyslogServerAddress_Object=MibScalar
infinetSyslogServerAddress=_InfinetSyslogServerAddress_Object((1,3,6,1,4,1,3942,1,1,6,1,1),_InfinetSyslogServerAddress_Type())
infinetSyslogServerAddress.setMaxAccess('read-write')
if mibBuilder.loadTexts:infinetSyslogServerAddress.setStatus(_B)
_InfinetSyslogMessagesTable_Object=MibTable
infinetSyslogMessagesTable=_InfinetSyslogMessagesTable_Object((1,3,6,1,4,1,3942,1,1,6,1,2))
if mibBuilder.loadTexts:infinetSyslogMessagesTable.setStatus(_B)
_InfinetSyslogMessageEntry_Object=MibTableRow
infinetSyslogMessageEntry=_InfinetSyslogMessageEntry_Object((1,3,6,1,4,1,3942,1,1,6,1,2,1))
infinetSyslogMessageEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:infinetSyslogMessageEntry.setStatus(_B)
_InfinetSyslogMessageIndex_Type=Counter32
_InfinetSyslogMessageIndex_Object=MibTableColumn
infinetSyslogMessageIndex=_InfinetSyslogMessageIndex_Object((1,3,6,1,4,1,3942,1,1,6,1,2,1,1),_InfinetSyslogMessageIndex_Type())
infinetSyslogMessageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:infinetSyslogMessageIndex.setStatus(_B)
_InfinetSyslogMessageSeverity_Type=InfinetSyslogSeverity
_InfinetSyslogMessageSeverity_Object=MibTableColumn
infinetSyslogMessageSeverity=_InfinetSyslogMessageSeverity_Object((1,3,6,1,4,1,3942,1,1,6,1,2,1,2),_InfinetSyslogMessageSeverity_Type())
infinetSyslogMessageSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:infinetSyslogMessageSeverity.setStatus(_B)
_InfinetSyslogMessageFacility_Type=InfinetSyslogFacility
_InfinetSyslogMessageFacility_Object=MibTableColumn
infinetSyslogMessageFacility=_InfinetSyslogMessageFacility_Object((1,3,6,1,4,1,3942,1,1,6,1,2,1,3),_InfinetSyslogMessageFacility_Type())
infinetSyslogMessageFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:infinetSyslogMessageFacility.setStatus(_B)
_InfinetSyslogMessageTimestamp_Type=DateAndTime
_InfinetSyslogMessageTimestamp_Object=MibTableColumn
infinetSyslogMessageTimestamp=_InfinetSyslogMessageTimestamp_Object((1,3,6,1,4,1,3942,1,1,6,1,2,1,4),_InfinetSyslogMessageTimestamp_Type())
infinetSyslogMessageTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:infinetSyslogMessageTimestamp.setStatus(_B)
_InfinetSyslogMessageIdentity_Type=DisplayString
_InfinetSyslogMessageIdentity_Object=MibTableColumn
infinetSyslogMessageIdentity=_InfinetSyslogMessageIdentity_Object((1,3,6,1,4,1,3942,1,1,6,1,2,1,5),_InfinetSyslogMessageIdentity_Type())
infinetSyslogMessageIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:infinetSyslogMessageIdentity.setStatus(_B)
class _InfinetSyslogMessageText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_InfinetSyslogMessageText_Type.__name__=_M
_InfinetSyslogMessageText_Object=MibTableColumn
infinetSyslogMessageText=_InfinetSyslogMessageText_Object((1,3,6,1,4,1,3942,1,1,6,1,2,1,6),_InfinetSyslogMessageText_Type())
infinetSyslogMessageText.setMaxAccess(_C)
if mibBuilder.loadTexts:infinetSyslogMessageText.setStatus(_B)
_InfinetSyslogEventsPrefix_ObjectIdentity=ObjectIdentity
infinetSyslogEventsPrefix=_InfinetSyslogEventsPrefix_ObjectIdentity((1,3,6,1,4,1,3942,1,1,6,2))
_InfinetSyslogEvents_ObjectIdentity=ObjectIdentity
infinetSyslogEvents=_InfinetSyslogEvents_ObjectIdentity((1,3,6,1,4,1,3942,1,1,6,2,0))
_InfinetSyslogConf_ObjectIdentity=ObjectIdentity
infinetSyslogConf=_InfinetSyslogConf_ObjectIdentity((1,3,6,1,4,1,3942,1,1,6,3))
_InfinetSyslogGroups_ObjectIdentity=ObjectIdentity
infinetSyslogGroups=_InfinetSyslogGroups_ObjectIdentity((1,3,6,1,4,1,3942,1,1,6,3,1))
_InfinetSyslogCompls_ObjectIdentity=ObjectIdentity
infinetSyslogCompls=_InfinetSyslogCompls_ObjectIdentity((1,3,6,1,4,1,3942,1,1,6,3,2))
infinetSyslogBasicGroup=ObjectGroup((1,3,6,1,4,1,3942,1,1,6,3,1,1))
infinetSyslogBasicGroup.setObjects(*((_A,_N),(_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:infinetSyslogBasicGroup.setStatus(_B)
infinetSyslogMessageGenerated=NotificationType((1,3,6,1,4,1,3942,1,1,6,2,0,1))
infinetSyslogMessageGenerated.setObjects(*((_E,_K),(_E,_L),(_A,_D),(_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_G)))
if mibBuilder.loadTexts:infinetSyslogMessageGenerated.setStatus(_B)
infinetSyslogBasicEvents=NotificationGroup((1,3,6,1,4,1,3942,1,1,6,3,1,2))
infinetSyslogBasicEvents.setObjects((_A,_O))
if mibBuilder.loadTexts:infinetSyslogBasicEvents.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'InfinetSyslogFacility':InfinetSyslogFacility,'InfinetSyslogSeverity':InfinetSyslogSeverity,'infinetSyslogMIB':infinetSyslogMIB,'infinetSyslogObjects':infinetSyslogObjects,_N:infinetSyslogServerAddress,'infinetSyslogMessagesTable':infinetSyslogMessagesTable,'infinetSyslogMessageEntry':infinetSyslogMessageEntry,_D:infinetSyslogMessageIndex,_F:infinetSyslogMessageSeverity,_H:infinetSyslogMessageFacility,_I:infinetSyslogMessageTimestamp,_J:infinetSyslogMessageIdentity,_G:infinetSyslogMessageText,'infinetSyslogEventsPrefix':infinetSyslogEventsPrefix,'infinetSyslogEvents':infinetSyslogEvents,_O:infinetSyslogMessageGenerated,'infinetSyslogConf':infinetSyslogConf,'infinetSyslogGroups':infinetSyslogGroups,'infinetSyslogBasicGroup':infinetSyslogBasicGroup,'infinetSyslogBasicEvents':infinetSyslogBasicEvents,'infinetSyslogCompls':infinetSyslogCompls})