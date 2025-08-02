_G='read-create'
_F='wwpSyslogServerIndex'
_E='WWP-SYSLOG-MIB'
_D='DisplayString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpSyslogMib=ModuleIdentity((1,3,6,1,4,1,6141,2,27))
if mibBuilder.loadTexts:wwpSyslogMib.setRevisions(('2006-03-09 17:00','2001-07-25 10:30'))
_WwpSyslogObjects_ObjectIdentity=ObjectIdentity
wwpSyslogObjects=_WwpSyslogObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,27,1))
_WwpSyslog_ObjectIdentity=ObjectIdentity
wwpSyslog=_WwpSyslog_ObjectIdentity((1,3,6,1,4,1,6141,2,27,1,1))
class _WwpSyslogSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('logEmergency',0),('logAlert',1),('logCritical',2),('logErrors',3),('logWarnings',4),('logNotifications',5),('logInformational',6),('logDebugging',7)))
_WwpSyslogSeverity_Type.__name__=_B
_WwpSyslogSeverity_Object=MibScalar
wwpSyslogSeverity=_WwpSyslogSeverity_Object((1,3,6,1,4,1,6141,2,27,1,1,1),_WwpSyslogSeverity_Type())
wwpSyslogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpSyslogSeverity.setStatus(_A)
_WwpSyslogServerTable_Object=MibTable
wwpSyslogServerTable=_WwpSyslogServerTable_Object((1,3,6,1,4,1,6141,2,27,1,1,2))
if mibBuilder.loadTexts:wwpSyslogServerTable.setStatus(_A)
_WwpSyslogServerEntry_Object=MibTableRow
wwpSyslogServerEntry=_WwpSyslogServerEntry_Object((1,3,6,1,4,1,6141,2,27,1,1,2,1))
wwpSyslogServerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpSyslogServerEntry.setStatus(_A)
class _WwpSyslogServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_WwpSyslogServerIndex_Type.__name__=_B
_WwpSyslogServerIndex_Object=MibTableColumn
wwpSyslogServerIndex=_WwpSyslogServerIndex_Object((1,3,6,1,4,1,6141,2,27,1,1,2,1,1),_WwpSyslogServerIndex_Type())
wwpSyslogServerIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:wwpSyslogServerIndex.setStatus(_A)
_WwpSyslogServerIPAddress_Type=IpAddress
_WwpSyslogServerIPAddress_Object=MibTableColumn
wwpSyslogServerIPAddress=_WwpSyslogServerIPAddress_Object((1,3,6,1,4,1,6141,2,27,1,1,2,1,2),_WwpSyslogServerIPAddress_Type())
wwpSyslogServerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpSyslogServerIPAddress.setStatus(_A)
class _WwpSyslogServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpSyslogServerPort_Type.__name__=_B
_WwpSyslogServerPort_Object=MibTableColumn
wwpSyslogServerPort=_WwpSyslogServerPort_Object((1,3,6,1,4,1,6141,2,27,1,1,2,1,3),_WwpSyslogServerPort_Type())
wwpSyslogServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpSyslogServerPort.setStatus(_A)
_WwpSyslogServerStatus_Type=RowStatus
_WwpSyslogServerStatus_Object=MibTableColumn
wwpSyslogServerStatus=_WwpSyslogServerStatus_Object((1,3,6,1,4,1,6141,2,27,1,1,2,1,4),_WwpSyslogServerStatus_Type())
wwpSyslogServerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpSyslogServerStatus.setStatus(_A)
class _WwpSyslogServerCustomPrefix_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpSyslogServerCustomPrefix_Type.__name__=_D
_WwpSyslogServerCustomPrefix_Object=MibTableColumn
wwpSyslogServerCustomPrefix=_WwpSyslogServerCustomPrefix_Object((1,3,6,1,4,1,6141,2,27,1,1,2,1,5),_WwpSyslogServerCustomPrefix_Type())
wwpSyslogServerCustomPrefix.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpSyslogServerCustomPrefix.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wwpSyslogMib':wwpSyslogMib,'wwpSyslogObjects':wwpSyslogObjects,'wwpSyslog':wwpSyslog,'wwpSyslogSeverity':wwpSyslogSeverity,'wwpSyslogServerTable':wwpSyslogServerTable,'wwpSyslogServerEntry':wwpSyslogServerEntry,_F:wwpSyslogServerIndex,'wwpSyslogServerIPAddress':wwpSyslogServerIPAddress,'wwpSyslogServerPort':wwpSyslogServerPort,'wwpSyslogServerStatus':wwpSyslogServerStatus,'wwpSyslogServerCustomPrefix':wwpSyslogServerCustomPrefix})