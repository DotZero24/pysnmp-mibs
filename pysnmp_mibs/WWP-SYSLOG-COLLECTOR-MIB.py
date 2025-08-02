_H='SyslogFacility'
_G='wwpSyslogCollectorAddr'
_F='WWP-SYSLOG-COLLECTOR-MIB'
_E='TruthValue'
_D='Integer32'
_C='SyslogSeverity'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpSyslogCollectorMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,46))
if mibBuilder.loadTexts:wwpSyslogCollectorMIB.setRevisions(('2003-01-21 10:12',))
class SyslogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,99)));namedValues=NamedValues(*(('kernel',0),('user',1),('mail',2),('daemon',3),('auth',4),('syslog',5),('lpr',6),('news',7),('uucp',8),('cron',9),('authPriv',10),('ftp',11),('ntp',12),('security',13),('console',14),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23),('noMap',99)))
class SyslogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,99)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7),('other',99)))
_WwpSyslogCollMIBObjects_ObjectIdentity=ObjectIdentity
wwpSyslogCollMIBObjects=_WwpSyslogCollMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,46,1))
_WwpSyslogSystem_ObjectIdentity=ObjectIdentity
wwpSyslogSystem=_WwpSyslogSystem_ObjectIdentity((1,3,6,1,4,1,6141,2,46,1,1))
class _WwpSyslogEnable_Type(TruthValue):defaultValue=1
_WwpSyslogEnable_Type.__name__=_E
_WwpSyslogEnable_Object=MibScalar
wwpSyslogEnable=_WwpSyslogEnable_Object((1,3,6,1,4,1,6141,2,46,1,1,1),_WwpSyslogEnable_Type())
wwpSyslogEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:wwpSyslogEnable.setStatus(_A)
_WwpSyslogColl_ObjectIdentity=ObjectIdentity
wwpSyslogColl=_WwpSyslogColl_ObjectIdentity((1,3,6,1,4,1,6141,2,46,1,2))
_WwpSyslogCollectorTable_Object=MibTable
wwpSyslogCollectorTable=_WwpSyslogCollectorTable_Object((1,3,6,1,4,1,6141,2,46,1,2,1))
if mibBuilder.loadTexts:wwpSyslogCollectorTable.setStatus(_A)
_WwpSyslogCollectorEntry_Object=MibTableRow
wwpSyslogCollectorEntry=_WwpSyslogCollectorEntry_Object((1,3,6,1,4,1,6141,2,46,1,2,1,1))
wwpSyslogCollectorEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wwpSyslogCollectorEntry.setStatus(_A)
_WwpSyslogCollectorAddr_Type=IpAddress
_WwpSyslogCollectorAddr_Object=MibTableColumn
wwpSyslogCollectorAddr=_WwpSyslogCollectorAddr_Object((1,3,6,1,4,1,6141,2,46,1,2,1,1,1),_WwpSyslogCollectorAddr_Type())
wwpSyslogCollectorAddr.setMaxAccess('read-only')
if mibBuilder.loadTexts:wwpSyslogCollectorAddr.setStatus(_A)
class _WwpSyslogCollectorUDPPort_Type(Integer32):defaultValue=514;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpSyslogCollectorUDPPort_Type.__name__=_D
_WwpSyslogCollectorUDPPort_Object=MibTableColumn
wwpSyslogCollectorUDPPort=_WwpSyslogCollectorUDPPort_Object((1,3,6,1,4,1,6141,2,46,1,2,1,1,2),_WwpSyslogCollectorUDPPort_Type())
wwpSyslogCollectorUDPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSyslogCollectorUDPPort.setStatus(_A)
class _WwpSyslogCollectorFacility_Type(SyslogFacility):defaultValue=3
_WwpSyslogCollectorFacility_Type.__name__=_H
_WwpSyslogCollectorFacility_Object=MibTableColumn
wwpSyslogCollectorFacility=_WwpSyslogCollectorFacility_Object((1,3,6,1,4,1,6141,2,46,1,2,1,1,3),_WwpSyslogCollectorFacility_Type())
wwpSyslogCollectorFacility.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSyslogCollectorFacility.setStatus(_A)
class _WwpSyslogCollectorMinSeverity_Type(SyslogSeverity):defaultValue=3
_WwpSyslogCollectorMinSeverity_Type.__name__=_C
_WwpSyslogCollectorMinSeverity_Object=MibTableColumn
wwpSyslogCollectorMinSeverity=_WwpSyslogCollectorMinSeverity_Object((1,3,6,1,4,1,6141,2,46,1,2,1,1,4),_WwpSyslogCollectorMinSeverity_Type())
wwpSyslogCollectorMinSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSyslogCollectorMinSeverity.setStatus(_A)
class _WwpSyslogCollectorMaxSeverity_Type(SyslogSeverity):defaultValue=0
_WwpSyslogCollectorMaxSeverity_Type.__name__=_C
_WwpSyslogCollectorMaxSeverity_Object=MibTableColumn
wwpSyslogCollectorMaxSeverity=_WwpSyslogCollectorMaxSeverity_Object((1,3,6,1,4,1,6141,2,46,1,2,1,1,5),_WwpSyslogCollectorMaxSeverity_Type())
wwpSyslogCollectorMaxSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSyslogCollectorMaxSeverity.setStatus(_A)
_WwpSyslogCollectorStatus_Type=RowStatus
_WwpSyslogCollectorStatus_Object=MibTableColumn
wwpSyslogCollectorStatus=_WwpSyslogCollectorStatus_Object((1,3,6,1,4,1,6141,2,46,1,2,1,1,6),_WwpSyslogCollectorStatus_Type())
wwpSyslogCollectorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpSyslogCollectorStatus.setStatus(_A)
_WwpSyslogCollMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpSyslogCollMIBNotificationPrefix=_WwpSyslogCollMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,46,2))
_WwpSyslogCollMIBNotifications_ObjectIdentity=ObjectIdentity
wwpSyslogCollMIBNotifications=_WwpSyslogCollMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,46,2,0))
_WwpSyslogCollMIBConformance_ObjectIdentity=ObjectIdentity
wwpSyslogCollMIBConformance=_WwpSyslogCollMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,46,3))
_WwpSyslogCollMIBCompliances_ObjectIdentity=ObjectIdentity
wwpSyslogCollMIBCompliances=_WwpSyslogCollMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,46,3,1))
_WwpSyslogCollMIBGroups_ObjectIdentity=ObjectIdentity
wwpSyslogCollMIBGroups=_WwpSyslogCollMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,46,3,2))
mibBuilder.exportSymbols(_F,**{_H:SyslogFacility,_C:SyslogSeverity,'wwpSyslogCollectorMIB':wwpSyslogCollectorMIB,'wwpSyslogCollMIBObjects':wwpSyslogCollMIBObjects,'wwpSyslogSystem':wwpSyslogSystem,'wwpSyslogEnable':wwpSyslogEnable,'wwpSyslogColl':wwpSyslogColl,'wwpSyslogCollectorTable':wwpSyslogCollectorTable,'wwpSyslogCollectorEntry':wwpSyslogCollectorEntry,_G:wwpSyslogCollectorAddr,'wwpSyslogCollectorUDPPort':wwpSyslogCollectorUDPPort,'wwpSyslogCollectorFacility':wwpSyslogCollectorFacility,'wwpSyslogCollectorMinSeverity':wwpSyslogCollectorMinSeverity,'wwpSyslogCollectorMaxSeverity':wwpSyslogCollectorMaxSeverity,'wwpSyslogCollectorStatus':wwpSyslogCollectorStatus,'wwpSyslogCollMIBNotificationPrefix':wwpSyslogCollMIBNotificationPrefix,'wwpSyslogCollMIBNotifications':wwpSyslogCollMIBNotifications,'wwpSyslogCollMIBConformance':wwpSyslogCollMIBConformance,'wwpSyslogCollMIBCompliances':wwpSyslogCollMIBCompliances,'wwpSyslogCollMIBGroups':wwpSyslogCollMIBGroups})