_H='tpSyslogHostIndex'
_G='TPLINK-SYSLOG-MIB'
_F='OctetString'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSyslogMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,24))
if mibBuilder.loadTexts:tplinkSyslogMIB.setRevisions(('2012-11-29 00:00',))
class MessageLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('informational',6),('debug',7)))
_TplinkSyslogMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSyslogMIBObjects=_TplinkSyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,24,1))
_TpSyslogBuffer_ObjectIdentity=ObjectIdentity
tpSyslogBuffer=_TpSyslogBuffer_ObjectIdentity((1,3,6,1,4,1,11863,6,24,1,1))
_TpSyslogBufferSeverity_Type=MessageLevelType
_TpSyslogBufferSeverity_Object=MibScalar
tpSyslogBufferSeverity=_TpSyslogBufferSeverity_Object((1,3,6,1,4,1,11863,6,24,1,1,1),_TpSyslogBufferSeverity_Type())
tpSyslogBufferSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogBufferSeverity.setStatus(_A)
class _TpSyslogBufferState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSyslogBufferState_Type.__name__=_C
_TpSyslogBufferState_Object=MibScalar
tpSyslogBufferState=_TpSyslogBufferState_Object((1,3,6,1,4,1,11863,6,24,1,1,2),_TpSyslogBufferState_Type())
tpSyslogBufferState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogBufferState.setStatus(_A)
_TpSyslogConsole_ObjectIdentity=ObjectIdentity
tpSyslogConsole=_TpSyslogConsole_ObjectIdentity((1,3,6,1,4,1,11863,6,24,1,2))
_TpSyslogConsoleSeverity_Type=MessageLevelType
_TpSyslogConsoleSeverity_Object=MibScalar
tpSyslogConsoleSeverity=_TpSyslogConsoleSeverity_Object((1,3,6,1,4,1,11863,6,24,1,2,1),_TpSyslogConsoleSeverity_Type())
tpSyslogConsoleSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogConsoleSeverity.setStatus(_A)
class _TpSyslogConsoleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSyslogConsoleState_Type.__name__=_C
_TpSyslogConsoleState_Object=MibScalar
tpSyslogConsoleState=_TpSyslogConsoleState_Object((1,3,6,1,4,1,11863,6,24,1,2,2),_TpSyslogConsoleState_Type())
tpSyslogConsoleState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogConsoleState.setStatus(_A)
_TpSyslogFlash_ObjectIdentity=ObjectIdentity
tpSyslogFlash=_TpSyslogFlash_ObjectIdentity((1,3,6,1,4,1,11863,6,24,1,3))
_TpSyslogFlashSeverity_Type=MessageLevelType
_TpSyslogFlashSeverity_Object=MibScalar
tpSyslogFlashSeverity=_TpSyslogFlashSeverity_Object((1,3,6,1,4,1,11863,6,24,1,3,1),_TpSyslogFlashSeverity_Type())
tpSyslogFlashSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogFlashSeverity.setStatus(_A)
class _TpSyslogFlashState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSyslogFlashState_Type.__name__=_C
_TpSyslogFlashState_Object=MibScalar
tpSyslogFlashState=_TpSyslogFlashState_Object((1,3,6,1,4,1,11863,6,24,1,3,2),_TpSyslogFlashState_Type())
tpSyslogFlashState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogFlashState.setStatus(_A)
class _TpSyslogFlashSyncFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_TpSyslogFlashSyncFrequency_Type.__name__=_C
_TpSyslogFlashSyncFrequency_Object=MibScalar
tpSyslogFlashSyncFrequency=_TpSyslogFlashSyncFrequency_Object((1,3,6,1,4,1,11863,6,24,1,3,3),_TpSyslogFlashSyncFrequency_Type())
tpSyslogFlashSyncFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogFlashSyncFrequency.setStatus(_A)
_TpSyslogMonitor_ObjectIdentity=ObjectIdentity
tpSyslogMonitor=_TpSyslogMonitor_ObjectIdentity((1,3,6,1,4,1,11863,6,24,1,4))
_TpSyslogMonitorSeverity_Type=MessageLevelType
_TpSyslogMonitorSeverity_Object=MibScalar
tpSyslogMonitorSeverity=_TpSyslogMonitorSeverity_Object((1,3,6,1,4,1,11863,6,24,1,4,1),_TpSyslogMonitorSeverity_Type())
tpSyslogMonitorSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogMonitorSeverity.setStatus(_A)
class _TpSyslogMonitorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSyslogMonitorState_Type.__name__=_C
_TpSyslogMonitorState_Object=MibScalar
tpSyslogMonitorState=_TpSyslogMonitorState_Object((1,3,6,1,4,1,11863,6,24,1,4,2),_TpSyslogMonitorState_Type())
tpSyslogMonitorState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogMonitorState.setStatus(_A)
_TpSyslogHostTable_Object=MibTable
tpSyslogHostTable=_TpSyslogHostTable_Object((1,3,6,1,4,1,11863,6,24,1,5))
if mibBuilder.loadTexts:tpSyslogHostTable.setStatus(_A)
_TpSyslogHostEntry_Object=MibTableRow
tpSyslogHostEntry=_TpSyslogHostEntry_Object((1,3,6,1,4,1,11863,6,24,1,5,1))
tpSyslogHostEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpSyslogHostEntry.setStatus(_A)
class _TpSyslogHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_TpSyslogHostIndex_Type.__name__=_C
_TpSyslogHostIndex_Object=MibTableColumn
tpSyslogHostIndex=_TpSyslogHostIndex_Object((1,3,6,1,4,1,11863,6,24,1,5,1,1),_TpSyslogHostIndex_Type())
tpSyslogHostIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:tpSyslogHostIndex.setStatus(_A)
class _TpSyslogHostIPAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(46,46));fixedLength=46
_TpSyslogHostIPAddress_Type.__name__=_F
_TpSyslogHostIPAddress_Object=MibTableColumn
tpSyslogHostIPAddress=_TpSyslogHostIPAddress_Object((1,3,6,1,4,1,11863,6,24,1,5,1,2),_TpSyslogHostIPAddress_Type())
tpSyslogHostIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogHostIPAddress.setStatus(_A)
_TpSyslogHostSeverity_Type=MessageLevelType
_TpSyslogHostSeverity_Object=MibTableColumn
tpSyslogHostSeverity=_TpSyslogHostSeverity_Object((1,3,6,1,4,1,11863,6,24,1,5,1,3),_TpSyslogHostSeverity_Type())
tpSyslogHostSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogHostSeverity.setStatus(_A)
class _TpSyslogHostState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpSyslogHostState_Type.__name__=_C
_TpSyslogHostState_Object=MibTableColumn
tpSyslogHostState=_TpSyslogHostState_Object((1,3,6,1,4,1,11863,6,24,1,5,1,4),_TpSyslogHostState_Type())
tpSyslogHostState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpSyslogHostState.setStatus(_A)
_TplinkSyslogNotifications_ObjectIdentity=ObjectIdentity
tplinkSyslogNotifications=_TplinkSyslogNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,24,2))
mibBuilder.exportSymbols(_G,**{'MessageLevelType':MessageLevelType,'tplinkSyslogMIB':tplinkSyslogMIB,'tplinkSyslogMIBObjects':tplinkSyslogMIBObjects,'tpSyslogBuffer':tpSyslogBuffer,'tpSyslogBufferSeverity':tpSyslogBufferSeverity,'tpSyslogBufferState':tpSyslogBufferState,'tpSyslogConsole':tpSyslogConsole,'tpSyslogConsoleSeverity':tpSyslogConsoleSeverity,'tpSyslogConsoleState':tpSyslogConsoleState,'tpSyslogFlash':tpSyslogFlash,'tpSyslogFlashSeverity':tpSyslogFlashSeverity,'tpSyslogFlashState':tpSyslogFlashState,'tpSyslogFlashSyncFrequency':tpSyslogFlashSyncFrequency,'tpSyslogMonitor':tpSyslogMonitor,'tpSyslogMonitorSeverity':tpSyslogMonitorSeverity,'tpSyslogMonitorState':tpSyslogMonitorState,'tpSyslogHostTable':tpSyslogHostTable,'tpSyslogHostEntry':tpSyslogHostEntry,_H:tpSyslogHostIndex,'tpSyslogHostIPAddress':tpSyslogHostIPAddress,'tpSyslogHostSeverity':tpSyslogHostSeverity,'tpSyslogHostState':tpSyslogHostState,'tplinkSyslogNotifications':tplinkSyslogNotifications})