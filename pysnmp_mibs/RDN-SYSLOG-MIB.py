_T='rdnSyslogTrapSeverity'
_S='rdnSyslogMessageIndex'
_R='not-accessible'
_Q='rdnSyslogServerIndex'
_P='read-only'
_O='OctetString'
_N='emergencies'
_M='alerts'
_L='critical'
_K='errors'
_J='warnings'
_I='notifications'
_H='informational'
_G='disable'
_F='disabled'
_E='enabled'
_D='RDN-SYSLOG-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
riverdelta,=mibBuilder.importSymbols('RDN-MIB','riverdelta')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdnSyslog=ModuleIdentity((1,3,6,1,4,1,4981,3))
if mibBuilder.loadTexts:rdnSyslog.setRevisions(('2008-08-08 00:00','2004-01-23 00:00','2003-11-05 00:00','2003-01-30 00:00','2000-06-14 00:00','2000-06-08 00:00','2000-05-23 00:00','2000-05-17 00:00'))
_RdnSyslogMIB_ObjectIdentity=ObjectIdentity
rdnSyslogMIB=_RdnSyslogMIB_ObjectIdentity((1,3,6,1,4,1,4981,3,0))
_RdnSyslogTraps_ObjectIdentity=ObjectIdentity
rdnSyslogTraps=_RdnSyslogTraps_ObjectIdentity((1,3,6,1,4,1,4981,3,0,0))
_RdnSyslogSize_Type=Integer32
_RdnSyslogSize_Object=MibScalar
rdnSyslogSize=_RdnSyslogSize_Object((1,3,6,1,4,1,4981,3,1),_RdnSyslogSize_Type())
rdnSyslogSize.setMaxAccess(_P)
if mibBuilder.loadTexts:rdnSyslogSize.setStatus(_A)
class _RdnSyslogMaxSize_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,5242880))
_RdnSyslogMaxSize_Type.__name__=_B
_RdnSyslogMaxSize_Object=MibScalar
rdnSyslogMaxSize=_RdnSyslogMaxSize_Object((1,3,6,1,4,1,4981,3,2),_RdnSyslogMaxSize_Type())
rdnSyslogMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogMaxSize.setStatus(_A)
class _RdnSyslogServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RdnSyslogServerEnable_Type.__name__=_B
_RdnSyslogServerEnable_Object=MibScalar
rdnSyslogServerEnable=_RdnSyslogServerEnable_Object((1,3,6,1,4,1,4981,3,3),_RdnSyslogServerEnable_Type())
rdnSyslogServerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogServerEnable.setStatus(_A)
_RdnSyslogServerTable_Object=MibTable
rdnSyslogServerTable=_RdnSyslogServerTable_Object((1,3,6,1,4,1,4981,3,4))
if mibBuilder.loadTexts:rdnSyslogServerTable.setStatus(_A)
_RdnSyslogServerEntry_Object=MibTableRow
rdnSyslogServerEntry=_RdnSyslogServerEntry_Object((1,3,6,1,4,1,4981,3,4,1))
rdnSyslogServerEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:rdnSyslogServerEntry.setStatus(_A)
_RdnSyslogServerIndex_Type=Integer32
_RdnSyslogServerIndex_Object=MibTableColumn
rdnSyslogServerIndex=_RdnSyslogServerIndex_Object((1,3,6,1,4,1,4981,3,4,1,1),_RdnSyslogServerIndex_Type())
rdnSyslogServerIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:rdnSyslogServerIndex.setStatus(_A)
_RdnSyslogServerAddress_Type=IpAddress
_RdnSyslogServerAddress_Object=MibTableColumn
rdnSyslogServerAddress=_RdnSyslogServerAddress_Object((1,3,6,1,4,1,4981,3,4,1,2),_RdnSyslogServerAddress_Type())
rdnSyslogServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogServerAddress.setStatus(_A)
class _RdnSyslogServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RdnSyslogServerStatus_Type.__name__=_B
_RdnSyslogServerStatus_Object=MibTableColumn
rdnSyslogServerStatus=_RdnSyslogServerStatus_Object((1,3,6,1,4,1,4981,3,4,1,3),_RdnSyslogServerStatus_Type())
rdnSyslogServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogServerStatus.setStatus(_A)
class _RdnSyslogSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7)))
_RdnSyslogSeverity_Type.__name__=_B
_RdnSyslogSeverity_Object=MibScalar
rdnSyslogSeverity=_RdnSyslogSeverity_Object((1,3,6,1,4,1,4981,3,5),_RdnSyslogSeverity_Type())
rdnSyslogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogSeverity.setStatus(_A)
class _RdnSyslogConsoleSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7)))
_RdnSyslogConsoleSeverity_Type.__name__=_B
_RdnSyslogConsoleSeverity_Object=MibScalar
rdnSyslogConsoleSeverity=_RdnSyslogConsoleSeverity_Object((1,3,6,1,4,1,4981,3,6),_RdnSyslogConsoleSeverity_Type())
rdnSyslogConsoleSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogConsoleSeverity.setStatus(_A)
class _RdnSyslogClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_RdnSyslogClear_Type.__name__=_B
_RdnSyslogClear_Object=MibScalar
rdnSyslogClear=_RdnSyslogClear_Object((1,3,6,1,4,1,4981,3,7),_RdnSyslogClear_Type())
rdnSyslogClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogClear.setStatus(_A)
class _RdnSyslogTrapSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7)))
_RdnSyslogTrapSeverity_Type.__name__=_B
_RdnSyslogTrapSeverity_Object=MibScalar
rdnSyslogTrapSeverity=_RdnSyslogTrapSeverity_Object((1,3,6,1,4,1,4981,3,8),_RdnSyslogTrapSeverity_Type())
rdnSyslogTrapSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogTrapSeverity.setStatus(_A)
_RdnSyslogMessageTable_Object=MibTable
rdnSyslogMessageTable=_RdnSyslogMessageTable_Object((1,3,6,1,4,1,4981,3,9))
if mibBuilder.loadTexts:rdnSyslogMessageTable.setStatus(_A)
_RdnSyslogMessageTableEntry_Object=MibTableRow
rdnSyslogMessageTableEntry=_RdnSyslogMessageTableEntry_Object((1,3,6,1,4,1,4981,3,9,1))
rdnSyslogMessageTableEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:rdnSyslogMessageTableEntry.setStatus(_A)
_RdnSyslogMessageIndex_Type=Integer32
_RdnSyslogMessageIndex_Object=MibTableColumn
rdnSyslogMessageIndex=_RdnSyslogMessageIndex_Object((1,3,6,1,4,1,4981,3,9,1,1),_RdnSyslogMessageIndex_Type())
rdnSyslogMessageIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:rdnSyslogMessageIndex.setStatus(_A)
class _RdnSyslogMessageString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_RdnSyslogMessageString_Type.__name__=_O
_RdnSyslogMessageString_Object=MibTableColumn
rdnSyslogMessageString=_RdnSyslogMessageString_Object((1,3,6,1,4,1,4981,3,9,1,2),_RdnSyslogMessageString_Type())
rdnSyslogMessageString.setMaxAccess(_P)
if mibBuilder.loadTexts:rdnSyslogMessageString.setStatus(_A)
class _RdnSyslogRateLimitAutoRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RdnSyslogRateLimitAutoRestart_Type.__name__=_B
_RdnSyslogRateLimitAutoRestart_Object=MibScalar
rdnSyslogRateLimitAutoRestart=_RdnSyslogRateLimitAutoRestart_Object((1,3,6,1,4,1,4981,3,10),_RdnSyslogRateLimitAutoRestart_Type())
rdnSyslogRateLimitAutoRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSyslogRateLimitAutoRestart.setStatus('obsolete')
rdnSyslogSeverityTrap=NotificationType((1,3,6,1,4,1,4981,3,0,0,1))
rdnSyslogSeverityTrap.setObjects((_D,_T))
if mibBuilder.loadTexts:rdnSyslogSeverityTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rdnSyslog':rdnSyslog,'rdnSyslogMIB':rdnSyslogMIB,'rdnSyslogTraps':rdnSyslogTraps,'rdnSyslogSeverityTrap':rdnSyslogSeverityTrap,'rdnSyslogSize':rdnSyslogSize,'rdnSyslogMaxSize':rdnSyslogMaxSize,'rdnSyslogServerEnable':rdnSyslogServerEnable,'rdnSyslogServerTable':rdnSyslogServerTable,'rdnSyslogServerEntry':rdnSyslogServerEntry,_Q:rdnSyslogServerIndex,'rdnSyslogServerAddress':rdnSyslogServerAddress,'rdnSyslogServerStatus':rdnSyslogServerStatus,'rdnSyslogSeverity':rdnSyslogSeverity,'rdnSyslogConsoleSeverity':rdnSyslogConsoleSeverity,'rdnSyslogClear':rdnSyslogClear,_T:rdnSyslogTrapSeverity,'rdnSyslogMessageTable':rdnSyslogMessageTable,'rdnSyslogMessageTableEntry':rdnSyslogMessageTableEntry,_S:rdnSyslogMessageIndex,'rdnSyslogMessageString':rdnSyslogMessageString,'rdnSyslogRateLimitAutoRestart':rdnSyslogRateLimitAutoRestart})