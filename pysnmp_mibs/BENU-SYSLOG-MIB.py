_N='debugging'
_M='informational'
_L='notifications'
_K='warnings'
_J='errors'
_I='critical'
_H='alerts'
_G='emergencies'
_F='bSyslogServerIndex'
_E='BENU-SYSLOG-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuPlatform,=mibBuilder.importSymbols('BENU-PLATFORM-MIB','benuPlatform')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
benuSyslog=ModuleIdentity((1,3,6,1,4,1,39406,1,3))
if mibBuilder.loadTexts:benuSyslog.setRevisions(('2015-01-09 00:00','2014-11-06 00:00','2013-11-22 00:00'))
_BSyslogNotifications_ObjectIdentity=ObjectIdentity
bSyslogNotifications=_BSyslogNotifications_ObjectIdentity((1,3,6,1,4,1,39406,1,3,0))
_BSyslogSize_Type=Unsigned32
_BSyslogSize_Object=MibScalar
bSyslogSize=_BSyslogSize_Object((1,3,6,1,4,1,39406,1,3,1),_BSyslogSize_Type())
bSyslogSize.setMaxAccess(_D)
if mibBuilder.loadTexts:bSyslogSize.setStatus(_A)
class _BSyslogMaxSize_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,5242880))
_BSyslogMaxSize_Type.__name__=_B
_BSyslogMaxSize_Object=MibScalar
bSyslogMaxSize=_BSyslogMaxSize_Object((1,3,6,1,4,1,39406,1,3,2),_BSyslogMaxSize_Type())
bSyslogMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:bSyslogMaxSize.setStatus(_A)
class _BSyslogServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_BSyslogServerEnable_Type.__name__=_B
_BSyslogServerEnable_Object=MibScalar
bSyslogServerEnable=_BSyslogServerEnable_Object((1,3,6,1,4,1,39406,1,3,3),_BSyslogServerEnable_Type())
bSyslogServerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bSyslogServerEnable.setStatus(_A)
_BSyslogServerTable_Object=MibTable
bSyslogServerTable=_BSyslogServerTable_Object((1,3,6,1,4,1,39406,1,3,4))
if mibBuilder.loadTexts:bSyslogServerTable.setStatus(_A)
_BSyslogServerEntry_Object=MibTableRow
bSyslogServerEntry=_BSyslogServerEntry_Object((1,3,6,1,4,1,39406,1,3,4,1))
bSyslogServerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:bSyslogServerEntry.setStatus(_A)
_BSyslogServerIndex_Type=Unsigned32
_BSyslogServerIndex_Object=MibTableColumn
bSyslogServerIndex=_BSyslogServerIndex_Object((1,3,6,1,4,1,39406,1,3,4,1,1),_BSyslogServerIndex_Type())
bSyslogServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bSyslogServerIndex.setStatus(_A)
_BSyslogServerAddress_Type=IpAddress
_BSyslogServerAddress_Object=MibTableColumn
bSyslogServerAddress=_BSyslogServerAddress_Object((1,3,6,1,4,1,39406,1,3,4,1,2),_BSyslogServerAddress_Type())
bSyslogServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:bSyslogServerAddress.setStatus(_A)
_BSyslogServerPort_Type=InetPortNumber
_BSyslogServerPort_Object=MibTableColumn
bSyslogServerPort=_BSyslogServerPort_Object((1,3,6,1,4,1,39406,1,3,4,1,3),_BSyslogServerPort_Type())
bSyslogServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:bSyslogServerPort.setStatus(_A)
class _BSyslogSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7)))
_BSyslogSeverity_Type.__name__=_B
_BSyslogSeverity_Object=MibScalar
bSyslogSeverity=_BSyslogSeverity_Object((1,3,6,1,4,1,39406,1,3,5),_BSyslogSeverity_Type())
bSyslogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:bSyslogSeverity.setStatus(_A)
class _BSyslogConsoleSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7)))
_BSyslogConsoleSeverity_Type.__name__=_B
_BSyslogConsoleSeverity_Object=MibScalar
bSyslogConsoleSeverity=_BSyslogConsoleSeverity_Object((1,3,6,1,4,1,39406,1,3,6),_BSyslogConsoleSeverity_Type())
bSyslogConsoleSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:bSyslogConsoleSeverity.setStatus(_A)
class _BSyslogClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_BSyslogClear_Type.__name__=_B
_BSyslogClear_Object=MibScalar
bSyslogClear=_BSyslogClear_Object((1,3,6,1,4,1,39406,1,3,7),_BSyslogClear_Type())
bSyslogClear.setMaxAccess(_C)
if mibBuilder.loadTexts:bSyslogClear.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'benuSyslog':benuSyslog,'bSyslogNotifications':bSyslogNotifications,'bSyslogSize':bSyslogSize,'bSyslogMaxSize':bSyslogMaxSize,'bSyslogServerEnable':bSyslogServerEnable,'bSyslogServerTable':bSyslogServerTable,'bSyslogServerEntry':bSyslogServerEntry,_F:bSyslogServerIndex,'bSyslogServerAddress':bSyslogServerAddress,'bSyslogServerPort':bSyslogServerPort,'bSyslogSeverity':bSyslogSeverity,'bSyslogConsoleSeverity':bSyslogConsoleSeverity,'bSyslogClear':bSyslogClear})