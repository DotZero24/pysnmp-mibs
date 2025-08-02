_V='FacilityType'
_U='hpnicfSyslogLoghostIndex'
_T='hpnicfTrapbufferIndex'
_S='hpnicfLogbufContIndex'
_R='hpnicfLogbufferIndex'
_Q='informational'
_P='notice'
_O='warning'
_N='critical'
_M='emergency'
_L='InetAddressType'
_K='DisplayString'
_J='hpnicfSyslogModuleIndex'
_I='hpnicfSyslogChannelIndex'
_H='TimeStampType'
_G='not-accessible'
_F='read-only'
_E='HPN-ICF-SYSLOG-MIB'
_D='Integer32'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TAddress','TextualConvention','TruthValue')
hpnicfSyslog=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63))
if mibBuilder.loadTexts:hpnicfSyslog.setRevisions(('2010-06-09 10:50',))
class MessageLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_M,1),('alert',2),(_N,3),('error',4),(_O,5),(_P,6),(_Q,7),('debug',8),('invalid',9)))
class TimeStampType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('date',2),('boot',3),('dateWithoutYear',4)))
class FacilityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kernel',0),('userLevel',1),('mailSystem',2),('systemDaemons',3),('securityAuthorization',4),('internallyMessages',5),('linePrinter',6),('networkNews',7),('uucp',8),('clockDaemon',9),('securityAuthorization2',10),('ftpDaemon',11),('ntp',12),('logAudit',13),('logAlert',14),('clockDaemon2',15),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
_HpnicfSyslogObjects_ObjectIdentity=ObjectIdentity
hpnicfSyslogObjects=_HpnicfSyslogObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1))
_HpnicfSyslogObject_ObjectIdentity=ObjectIdentity
hpnicfSyslogObject=_HpnicfSyslogObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,1))
_HpnicfSyslogState_Type=TruthValue
_HpnicfSyslogState_Object=MibScalar
hpnicfSyslogState=_HpnicfSyslogState_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,1,1),_HpnicfSyslogState_Type())
hpnicfSyslogState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogState.setStatus(_A)
_HpnicfSyslogMaxLoghost_Type=Integer32
_HpnicfSyslogMaxLoghost_Object=MibScalar
hpnicfSyslogMaxLoghost=_HpnicfSyslogMaxLoghost_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,1,2),_HpnicfSyslogMaxLoghost_Type())
hpnicfSyslogMaxLoghost.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSyslogMaxLoghost.setStatus(_A)
_HpnicfSyslogMaxChannel_Type=Integer32
_HpnicfSyslogMaxChannel_Object=MibScalar
hpnicfSyslogMaxChannel=_HpnicfSyslogMaxChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,1,3),_HpnicfSyslogMaxChannel_Type())
hpnicfSyslogMaxChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSyslogMaxChannel.setStatus(_A)
_HpnicfSyslogMaxLogbufferSize_Type=Integer32
_HpnicfSyslogMaxLogbufferSize_Object=MibScalar
hpnicfSyslogMaxLogbufferSize=_HpnicfSyslogMaxLogbufferSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,1,4),_HpnicfSyslogMaxLogbufferSize_Type())
hpnicfSyslogMaxLogbufferSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSyslogMaxLogbufferSize.setStatus(_A)
_HpnicfSyslogMaxTrapbufferSize_Type=Integer32
_HpnicfSyslogMaxTrapbufferSize_Object=MibScalar
hpnicfSyslogMaxTrapbufferSize=_HpnicfSyslogMaxTrapbufferSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,1,5),_HpnicfSyslogMaxTrapbufferSize_Type())
hpnicfSyslogMaxTrapbufferSize.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSyslogMaxTrapbufferSize.setStatus(_A)
class _HpnicfSyslogState2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_HpnicfSyslogState2_Type.__name__=_D
_HpnicfSyslogState2_Object=MibScalar
hpnicfSyslogState2=_HpnicfSyslogState2_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,1,6),_HpnicfSyslogState2_Type())
hpnicfSyslogState2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogState2.setStatus(_A)
_HpnicfSyslogConsole_ObjectIdentity=ObjectIdentity
hpnicfSyslogConsole=_HpnicfSyslogConsole_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,2))
class _HpnicfSyslogConsoleChannel_Type(Integer32):defaultValue=0
_HpnicfSyslogConsoleChannel_Type.__name__=_D
_HpnicfSyslogConsoleChannel_Object=MibScalar
hpnicfSyslogConsoleChannel=_HpnicfSyslogConsoleChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,2,1),_HpnicfSyslogConsoleChannel_Type())
hpnicfSyslogConsoleChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogConsoleChannel.setStatus(_A)
_HpnicfSyslogMonitor_ObjectIdentity=ObjectIdentity
hpnicfSyslogMonitor=_HpnicfSyslogMonitor_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,3))
class _HpnicfSyslogMonitorChannel_Type(Integer32):defaultValue=1
_HpnicfSyslogMonitorChannel_Type.__name__=_D
_HpnicfSyslogMonitorChannel_Object=MibScalar
hpnicfSyslogMonitorChannel=_HpnicfSyslogMonitorChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,3,1),_HpnicfSyslogMonitorChannel_Type())
hpnicfSyslogMonitorChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogMonitorChannel.setStatus(_A)
_HpnicfSyslogSnmp_ObjectIdentity=ObjectIdentity
hpnicfSyslogSnmp=_HpnicfSyslogSnmp_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,4))
class _HpnicfSyslogSnmpChannel_Type(Integer32):defaultValue=5
_HpnicfSyslogSnmpChannel_Type.__name__=_D
_HpnicfSyslogSnmpChannel_Object=MibScalar
hpnicfSyslogSnmpChannel=_HpnicfSyslogSnmpChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,4,1),_HpnicfSyslogSnmpChannel_Type())
hpnicfSyslogSnmpChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogSnmpChannel.setStatus(_A)
_HpnicfSyslogLogbuffer_ObjectIdentity=ObjectIdentity
hpnicfSyslogLogbuffer=_HpnicfSyslogLogbuffer_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5))
class _HpnicfSyslogLogbufferChannel_Type(Integer32):defaultValue=4
_HpnicfSyslogLogbufferChannel_Type.__name__=_D
_HpnicfSyslogLogbufferChannel_Object=MibScalar
hpnicfSyslogLogbufferChannel=_HpnicfSyslogLogbufferChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,1),_HpnicfSyslogLogbufferChannel_Type())
hpnicfSyslogLogbufferChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogLogbufferChannel.setStatus(_A)
class _HpnicfSyslogLogbufferSize_Type(Integer32):defaultValue=512
_HpnicfSyslogLogbufferSize_Type.__name__=_D
_HpnicfSyslogLogbufferSize_Object=MibScalar
hpnicfSyslogLogbufferSize=_HpnicfSyslogLogbufferSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,2),_HpnicfSyslogLogbufferSize_Type())
hpnicfSyslogLogbufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogLogbufferSize.setStatus(_A)
_HpnicfSyslogLogbufferTable_Object=MibTable
hpnicfSyslogLogbufferTable=_HpnicfSyslogLogbufferTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,3))
if mibBuilder.loadTexts:hpnicfSyslogLogbufferTable.setStatus(_A)
_HpnicfSyslogLogbufferEntry_Object=MibTableRow
hpnicfSyslogLogbufferEntry=_HpnicfSyslogLogbufferEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,3,1))
hpnicfSyslogLogbufferEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:hpnicfSyslogLogbufferEntry.setStatus(_A)
_HpnicfLogbufferIndex_Type=Integer32
_HpnicfLogbufferIndex_Object=MibTableColumn
hpnicfLogbufferIndex=_HpnicfLogbufferIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,3,1,1),_HpnicfLogbufferIndex_Type())
hpnicfLogbufferIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLogbufferIndex.setStatus(_A)
_HpnicfLogbufferCurrentMessages_Type=Unsigned32
_HpnicfLogbufferCurrentMessages_Object=MibTableColumn
hpnicfLogbufferCurrentMessages=_HpnicfLogbufferCurrentMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,3,1,2),_HpnicfLogbufferCurrentMessages_Type())
hpnicfLogbufferCurrentMessages.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfLogbufferCurrentMessages.setStatus(_A)
_HpnicfLogbufferOverwrittenMessages_Type=Counter32
_HpnicfLogbufferOverwrittenMessages_Object=MibTableColumn
hpnicfLogbufferOverwrittenMessages=_HpnicfLogbufferOverwrittenMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,3,1,3),_HpnicfLogbufferOverwrittenMessages_Type())
hpnicfLogbufferOverwrittenMessages.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfLogbufferOverwrittenMessages.setStatus(_A)
_HpnicfLogbufferDroppedMessages_Type=Counter32
_HpnicfLogbufferDroppedMessages_Object=MibTableColumn
hpnicfLogbufferDroppedMessages=_HpnicfLogbufferDroppedMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,3,1,4),_HpnicfLogbufferDroppedMessages_Type())
hpnicfLogbufferDroppedMessages.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfLogbufferDroppedMessages.setStatus(_A)
_HpnicfSyslogLogbufContTable_Object=MibTable
hpnicfSyslogLogbufContTable=_HpnicfSyslogLogbufContTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,4))
if mibBuilder.loadTexts:hpnicfSyslogLogbufContTable.setStatus(_A)
_HpnicfSyslogLogbufContEntry_Object=MibTableRow
hpnicfSyslogLogbufContEntry=_HpnicfSyslogLogbufContEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,4,1))
hpnicfSyslogLogbufContEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:hpnicfSyslogLogbufContEntry.setStatus(_A)
class _HpnicfLogbufContIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfLogbufContIndex_Type.__name__=_D
_HpnicfLogbufContIndex_Object=MibTableColumn
hpnicfLogbufContIndex=_HpnicfLogbufContIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,4,1,1),_HpnicfLogbufContIndex_Type())
hpnicfLogbufContIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLogbufContIndex.setStatus(_A)
class _HpnicfLogbufContDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1600))
_HpnicfLogbufContDescription_Type.__name__=_K
_HpnicfLogbufContDescription_Object=MibTableColumn
hpnicfLogbufContDescription=_HpnicfLogbufContDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,5,4,1,2),_HpnicfLogbufContDescription_Type())
hpnicfLogbufContDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfLogbufContDescription.setStatus(_A)
_HpnicfSyslogTrapbuffer_ObjectIdentity=ObjectIdentity
hpnicfSyslogTrapbuffer=_HpnicfSyslogTrapbuffer_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6))
class _HpnicfSyslogTrapbufferChannel_Type(Integer32):defaultValue=3
_HpnicfSyslogTrapbufferChannel_Type.__name__=_D
_HpnicfSyslogTrapbufferChannel_Object=MibScalar
hpnicfSyslogTrapbufferChannel=_HpnicfSyslogTrapbufferChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,1),_HpnicfSyslogTrapbufferChannel_Type())
hpnicfSyslogTrapbufferChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogTrapbufferChannel.setStatus(_A)
class _HpnicfSyslogTrapbufferSize_Type(Integer32):defaultValue=256
_HpnicfSyslogTrapbufferSize_Type.__name__=_D
_HpnicfSyslogTrapbufferSize_Object=MibScalar
hpnicfSyslogTrapbufferSize=_HpnicfSyslogTrapbufferSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,2),_HpnicfSyslogTrapbufferSize_Type())
hpnicfSyslogTrapbufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogTrapbufferSize.setStatus(_A)
_HpnicfSyslogTrapbufferTable_Object=MibTable
hpnicfSyslogTrapbufferTable=_HpnicfSyslogTrapbufferTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,3))
if mibBuilder.loadTexts:hpnicfSyslogTrapbufferTable.setStatus(_A)
_HpnicfSyslogTrapbufferEntry_Object=MibTableRow
hpnicfSyslogTrapbufferEntry=_HpnicfSyslogTrapbufferEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,3,1))
hpnicfSyslogTrapbufferEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:hpnicfSyslogTrapbufferEntry.setStatus(_A)
_HpnicfTrapbufferIndex_Type=Integer32
_HpnicfTrapbufferIndex_Object=MibTableColumn
hpnicfTrapbufferIndex=_HpnicfTrapbufferIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,3,1,1),_HpnicfTrapbufferIndex_Type())
hpnicfTrapbufferIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTrapbufferIndex.setStatus(_A)
_HpnicfTrapbufferCurrentMessages_Type=Unsigned32
_HpnicfTrapbufferCurrentMessages_Object=MibTableColumn
hpnicfTrapbufferCurrentMessages=_HpnicfTrapbufferCurrentMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,3,1,2),_HpnicfTrapbufferCurrentMessages_Type())
hpnicfTrapbufferCurrentMessages.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTrapbufferCurrentMessages.setStatus(_A)
_HpnicfTrapbufferOverwrittenMessages_Type=Counter32
_HpnicfTrapbufferOverwrittenMessages_Object=MibTableColumn
hpnicfTrapbufferOverwrittenMessages=_HpnicfTrapbufferOverwrittenMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,3,1,3),_HpnicfTrapbufferOverwrittenMessages_Type())
hpnicfTrapbufferOverwrittenMessages.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTrapbufferOverwrittenMessages.setStatus(_A)
_HpnicfTrapbufferDroppedMessages_Type=Counter32
_HpnicfTrapbufferDroppedMessages_Object=MibTableColumn
hpnicfTrapbufferDroppedMessages=_HpnicfTrapbufferDroppedMessages_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,6,3,1,4),_HpnicfTrapbufferDroppedMessages_Type())
hpnicfTrapbufferDroppedMessages.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTrapbufferDroppedMessages.setStatus(_A)
_HpnicfSyslogLoghost_ObjectIdentity=ObjectIdentity
hpnicfSyslogLoghost=_HpnicfSyslogLoghost_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7))
_HpnicfSyslogLoghostSourceInterface_Type=Integer32
_HpnicfSyslogLoghostSourceInterface_Object=MibScalar
hpnicfSyslogLoghostSourceInterface=_HpnicfSyslogLoghostSourceInterface_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,1),_HpnicfSyslogLoghostSourceInterface_Type())
hpnicfSyslogLoghostSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogLoghostSourceInterface.setStatus(_A)
class _HpnicfSyslogLoghostTimestampType_Type(TimeStampType):defaultValue=2
_HpnicfSyslogLoghostTimestampType_Type.__name__=_H
_HpnicfSyslogLoghostTimestampType_Object=MibScalar
hpnicfSyslogLoghostTimestampType=_HpnicfSyslogLoghostTimestampType_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,2),_HpnicfSyslogLoghostTimestampType_Type())
hpnicfSyslogLoghostTimestampType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogLoghostTimestampType.setStatus(_A)
_HpnicfSyslogLoghostTable_Object=MibTable
hpnicfSyslogLoghostTable=_HpnicfSyslogLoghostTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3))
if mibBuilder.loadTexts:hpnicfSyslogLoghostTable.setStatus(_A)
_HpnicfSyslogLoghostEntry_Object=MibTableRow
hpnicfSyslogLoghostEntry=_HpnicfSyslogLoghostEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1))
hpnicfSyslogLoghostEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:hpnicfSyslogLoghostEntry.setStatus(_A)
class _HpnicfSyslogLoghostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfSyslogLoghostIndex_Type.__name__=_D
_HpnicfSyslogLoghostIndex_Object=MibTableColumn
hpnicfSyslogLoghostIndex=_HpnicfSyslogLoghostIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,1),_HpnicfSyslogLoghostIndex_Type())
hpnicfSyslogLoghostIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSyslogLoghostIndex.setStatus(_A)
class _HpnicfSyslogLoghostChannel_Type(Integer32):defaultValue=2
_HpnicfSyslogLoghostChannel_Type.__name__=_D
_HpnicfSyslogLoghostChannel_Object=MibTableColumn
hpnicfSyslogLoghostChannel=_HpnicfSyslogLoghostChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,2),_HpnicfSyslogLoghostChannel_Type())
hpnicfSyslogLoghostChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostChannel.setStatus(_A)
class _HpnicfSyslogLoghostIpaddressType_Type(InetAddressType):defaultValue=1
_HpnicfSyslogLoghostIpaddressType_Type.__name__=_L
_HpnicfSyslogLoghostIpaddressType_Object=MibTableColumn
hpnicfSyslogLoghostIpaddressType=_HpnicfSyslogLoghostIpaddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,3),_HpnicfSyslogLoghostIpaddressType_Type())
hpnicfSyslogLoghostIpaddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostIpaddressType.setStatus(_A)
_HpnicfSyslogLoghostIpaddress_Type=InetAddress
_HpnicfSyslogLoghostIpaddress_Object=MibTableColumn
hpnicfSyslogLoghostIpaddress=_HpnicfSyslogLoghostIpaddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,4),_HpnicfSyslogLoghostIpaddress_Type())
hpnicfSyslogLoghostIpaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostIpaddress.setStatus(_A)
class _HpnicfSyslogLoghostFacility_Type(FacilityType):defaultValue=23
_HpnicfSyslogLoghostFacility_Type.__name__=_V
_HpnicfSyslogLoghostFacility_Object=MibTableColumn
hpnicfSyslogLoghostFacility=_HpnicfSyslogLoghostFacility_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,5),_HpnicfSyslogLoghostFacility_Type())
hpnicfSyslogLoghostFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostFacility.setStatus(_A)
class _HpnicfSyslogLoghostLanguage_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chinese',1),('english',2)))
_HpnicfSyslogLoghostLanguage_Type.__name__=_D
_HpnicfSyslogLoghostLanguage_Object=MibTableColumn
hpnicfSyslogLoghostLanguage=_HpnicfSyslogLoghostLanguage_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,6),_HpnicfSyslogLoghostLanguage_Type())
hpnicfSyslogLoghostLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostLanguage.setStatus(_A)
_HpnicfSyslogLoghostOperateRowStatus_Type=RowStatus
_HpnicfSyslogLoghostOperateRowStatus_Object=MibTableColumn
hpnicfSyslogLoghostOperateRowStatus=_HpnicfSyslogLoghostOperateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,7),_HpnicfSyslogLoghostOperateRowStatus_Type())
hpnicfSyslogLoghostOperateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostOperateRowStatus.setStatus(_A)
class _HpnicfSyslogLoghostIpaddressPort_Type(Integer32):defaultValue=514;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfSyslogLoghostIpaddressPort_Type.__name__=_D
_HpnicfSyslogLoghostIpaddressPort_Object=MibTableColumn
hpnicfSyslogLoghostIpaddressPort=_HpnicfSyslogLoghostIpaddressPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,8),_HpnicfSyslogLoghostIpaddressPort_Type())
hpnicfSyslogLoghostIpaddressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostIpaddressPort.setStatus(_A)
_HpnicfSyslogLoghostTAddress_Type=TAddress
_HpnicfSyslogLoghostTAddress_Object=MibTableColumn
hpnicfSyslogLoghostTAddress=_HpnicfSyslogLoghostTAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,7,3,1,9),_HpnicfSyslogLoghostTAddress_Type())
hpnicfSyslogLoghostTAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLoghostTAddress.setStatus(_A)
_HpnicfSyslogChannel_ObjectIdentity=ObjectIdentity
hpnicfSyslogChannel=_HpnicfSyslogChannel_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,8))
_HpnicfSyslogChannelTable_Object=MibTable
hpnicfSyslogChannelTable=_HpnicfSyslogChannelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,8,1))
if mibBuilder.loadTexts:hpnicfSyslogChannelTable.setStatus(_A)
_HpnicfSyslogChannelEntry_Object=MibTableRow
hpnicfSyslogChannelEntry=_HpnicfSyslogChannelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,8,1,1))
hpnicfSyslogChannelEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hpnicfSyslogChannelEntry.setStatus(_A)
_HpnicfSyslogChannelIndex_Type=Integer32
_HpnicfSyslogChannelIndex_Object=MibTableColumn
hpnicfSyslogChannelIndex=_HpnicfSyslogChannelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,8,1,1,1),_HpnicfSyslogChannelIndex_Type())
hpnicfSyslogChannelIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSyslogChannelIndex.setStatus(_A)
class _HpnicfSyslogChannelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_HpnicfSyslogChannelName_Type.__name__=_K
_HpnicfSyslogChannelName_Object=MibTableColumn
hpnicfSyslogChannelName=_HpnicfSyslogChannelName_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,8,1,1,2),_HpnicfSyslogChannelName_Type())
hpnicfSyslogChannelName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogChannelName.setStatus(_A)
_HpnicfSyslogModule_ObjectIdentity=ObjectIdentity
hpnicfSyslogModule=_HpnicfSyslogModule_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,9))
_HpnicfSyslogModuleTable_Object=MibTable
hpnicfSyslogModuleTable=_HpnicfSyslogModuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,9,1))
if mibBuilder.loadTexts:hpnicfSyslogModuleTable.setStatus(_A)
_HpnicfSyslogModuleEntry_Object=MibTableRow
hpnicfSyslogModuleEntry=_HpnicfSyslogModuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,9,1,1))
hpnicfSyslogModuleEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hpnicfSyslogModuleEntry.setStatus(_A)
_HpnicfSyslogModuleIndex_Type=Integer32
_HpnicfSyslogModuleIndex_Object=MibTableColumn
hpnicfSyslogModuleIndex=_HpnicfSyslogModuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,9,1,1,1),_HpnicfSyslogModuleIndex_Type())
hpnicfSyslogModuleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSyslogModuleIndex.setStatus(_A)
class _HpnicfSyslogModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_HpnicfSyslogModuleName_Type.__name__=_K
_HpnicfSyslogModuleName_Object=MibTableColumn
hpnicfSyslogModuleName=_HpnicfSyslogModuleName_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,9,1,1,2),_HpnicfSyslogModuleName_Type())
hpnicfSyslogModuleName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSyslogModuleName.setStatus(_A)
_HpnicfSyslogLog_ObjectIdentity=ObjectIdentity
hpnicfSyslogLog=_HpnicfSyslogLog_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10))
class _HpnicfSyslogLogTimestampType_Type(TimeStampType):defaultValue=2
_HpnicfSyslogLogTimestampType_Type.__name__=_H
_HpnicfSyslogLogTimestampType_Object=MibScalar
hpnicfSyslogLogTimestampType=_HpnicfSyslogLogTimestampType_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,1),_HpnicfSyslogLogTimestampType_Type())
hpnicfSyslogLogTimestampType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogLogTimestampType.setStatus(_A)
_HpnicfSyslogLogTable_Object=MibTable
hpnicfSyslogLogTable=_HpnicfSyslogLogTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,2))
if mibBuilder.loadTexts:hpnicfSyslogLogTable.setStatus(_A)
_HpnicfSyslogLogEntry_Object=MibTableRow
hpnicfSyslogLogEntry=_HpnicfSyslogLogEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,2,1))
hpnicfSyslogLogEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:hpnicfSyslogLogEntry.setStatus(_A)
_HpnicfSyslogLogState_Type=TruthValue
_HpnicfSyslogLogState_Object=MibTableColumn
hpnicfSyslogLogState=_HpnicfSyslogLogState_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,2,1,1),_HpnicfSyslogLogState_Type())
hpnicfSyslogLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLogState.setStatus(_A)
_HpnicfSyslogLogLevel_Type=MessageLevelType
_HpnicfSyslogLogLevel_Object=MibTableColumn
hpnicfSyslogLogLevel=_HpnicfSyslogLogLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,2,1,2),_HpnicfSyslogLogLevel_Type())
hpnicfSyslogLogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLogLevel.setStatus(_A)
_HpnicfSyslogLogRowStatus_Type=RowStatus
_HpnicfSyslogLogRowStatus_Object=MibTableColumn
hpnicfSyslogLogRowStatus=_HpnicfSyslogLogRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,2,1,3),_HpnicfSyslogLogRowStatus_Type())
hpnicfSyslogLogRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogLogRowStatus.setStatus(_A)
_HpnicfSyslogLogGlobalLevel_Type=MessageLevelType
_HpnicfSyslogLogGlobalLevel_Object=MibScalar
hpnicfSyslogLogGlobalLevel=_HpnicfSyslogLogGlobalLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,3),_HpnicfSyslogLogGlobalLevel_Type())
hpnicfSyslogLogGlobalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogLogGlobalLevel.setStatus('obsolete')
class _HpnicfSyslogLogGlobalLevelRfc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,0),('alert',1),(_N,2),('error',3),(_O,4),(_P,5),(_Q,6),('debug',7)))
_HpnicfSyslogLogGlobalLevelRfc_Type.__name__=_D
_HpnicfSyslogLogGlobalLevelRfc_Object=MibScalar
hpnicfSyslogLogGlobalLevelRfc=_HpnicfSyslogLogGlobalLevelRfc_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,10,4),_HpnicfSyslogLogGlobalLevelRfc_Type())
hpnicfSyslogLogGlobalLevelRfc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogLogGlobalLevelRfc.setStatus(_A)
_HpnicfSyslogTrap_ObjectIdentity=ObjectIdentity
hpnicfSyslogTrap=_HpnicfSyslogTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,11))
class _HpnicfSyslogTrapTimestampType_Type(TimeStampType):defaultValue=2
_HpnicfSyslogTrapTimestampType_Type.__name__=_H
_HpnicfSyslogTrapTimestampType_Object=MibScalar
hpnicfSyslogTrapTimestampType=_HpnicfSyslogTrapTimestampType_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,11,1),_HpnicfSyslogTrapTimestampType_Type())
hpnicfSyslogTrapTimestampType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogTrapTimestampType.setStatus(_A)
_HpnicfSyslogTrapTable_Object=MibTable
hpnicfSyslogTrapTable=_HpnicfSyslogTrapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,11,2))
if mibBuilder.loadTexts:hpnicfSyslogTrapTable.setStatus(_A)
_HpnicfSyslogTrapEntry_Object=MibTableRow
hpnicfSyslogTrapEntry=_HpnicfSyslogTrapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,11,2,1))
hpnicfSyslogTrapEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:hpnicfSyslogTrapEntry.setStatus(_A)
_HpnicfSyslogTrapState_Type=TruthValue
_HpnicfSyslogTrapState_Object=MibTableColumn
hpnicfSyslogTrapState=_HpnicfSyslogTrapState_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,11,2,1,1),_HpnicfSyslogTrapState_Type())
hpnicfSyslogTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogTrapState.setStatus(_A)
_HpnicfSyslogTrapLevel_Type=MessageLevelType
_HpnicfSyslogTrapLevel_Object=MibTableColumn
hpnicfSyslogTrapLevel=_HpnicfSyslogTrapLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,11,2,1,2),_HpnicfSyslogTrapLevel_Type())
hpnicfSyslogTrapLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogTrapLevel.setStatus(_A)
_HpnicfSyslogTrapRowStatus_Type=RowStatus
_HpnicfSyslogTrapRowStatus_Object=MibTableColumn
hpnicfSyslogTrapRowStatus=_HpnicfSyslogTrapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,11,2,1,3),_HpnicfSyslogTrapRowStatus_Type())
hpnicfSyslogTrapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogTrapRowStatus.setStatus(_A)
_HpnicfSyslogDebug_ObjectIdentity=ObjectIdentity
hpnicfSyslogDebug=_HpnicfSyslogDebug_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,63,1,12))
class _HpnicfSyslogDebugTimestampType_Type(TimeStampType):defaultValue=3
_HpnicfSyslogDebugTimestampType_Type.__name__=_H
_HpnicfSyslogDebugTimestampType_Object=MibScalar
hpnicfSyslogDebugTimestampType=_HpnicfSyslogDebugTimestampType_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,12,1),_HpnicfSyslogDebugTimestampType_Type())
hpnicfSyslogDebugTimestampType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSyslogDebugTimestampType.setStatus(_A)
_HpnicfSyslogDebugTable_Object=MibTable
hpnicfSyslogDebugTable=_HpnicfSyslogDebugTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,12,2))
if mibBuilder.loadTexts:hpnicfSyslogDebugTable.setStatus(_A)
_HpnicfSyslogDebugEntry_Object=MibTableRow
hpnicfSyslogDebugEntry=_HpnicfSyslogDebugEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,12,2,1))
hpnicfSyslogDebugEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:hpnicfSyslogDebugEntry.setStatus(_A)
_HpnicfSyslogDebugState_Type=TruthValue
_HpnicfSyslogDebugState_Object=MibTableColumn
hpnicfSyslogDebugState=_HpnicfSyslogDebugState_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,12,2,1,1),_HpnicfSyslogDebugState_Type())
hpnicfSyslogDebugState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogDebugState.setStatus(_A)
_HpnicfSyslogDebugLevel_Type=MessageLevelType
_HpnicfSyslogDebugLevel_Object=MibTableColumn
hpnicfSyslogDebugLevel=_HpnicfSyslogDebugLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,12,2,1,2),_HpnicfSyslogDebugLevel_Type())
hpnicfSyslogDebugLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogDebugLevel.setStatus(_A)
_HpnicfSyslogDebugRowStatus_Type=RowStatus
_HpnicfSyslogDebugRowStatus_Object=MibTableColumn
hpnicfSyslogDebugRowStatus=_HpnicfSyslogDebugRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,63,1,12,2,1,3),_HpnicfSyslogDebugRowStatus_Type())
hpnicfSyslogDebugRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSyslogDebugRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MessageLevelType':MessageLevelType,_H:TimeStampType,_V:FacilityType,'hpnicfSyslog':hpnicfSyslog,'hpnicfSyslogObjects':hpnicfSyslogObjects,'hpnicfSyslogObject':hpnicfSyslogObject,'hpnicfSyslogState':hpnicfSyslogState,'hpnicfSyslogMaxLoghost':hpnicfSyslogMaxLoghost,'hpnicfSyslogMaxChannel':hpnicfSyslogMaxChannel,'hpnicfSyslogMaxLogbufferSize':hpnicfSyslogMaxLogbufferSize,'hpnicfSyslogMaxTrapbufferSize':hpnicfSyslogMaxTrapbufferSize,'hpnicfSyslogState2':hpnicfSyslogState2,'hpnicfSyslogConsole':hpnicfSyslogConsole,'hpnicfSyslogConsoleChannel':hpnicfSyslogConsoleChannel,'hpnicfSyslogMonitor':hpnicfSyslogMonitor,'hpnicfSyslogMonitorChannel':hpnicfSyslogMonitorChannel,'hpnicfSyslogSnmp':hpnicfSyslogSnmp,'hpnicfSyslogSnmpChannel':hpnicfSyslogSnmpChannel,'hpnicfSyslogLogbuffer':hpnicfSyslogLogbuffer,'hpnicfSyslogLogbufferChannel':hpnicfSyslogLogbufferChannel,'hpnicfSyslogLogbufferSize':hpnicfSyslogLogbufferSize,'hpnicfSyslogLogbufferTable':hpnicfSyslogLogbufferTable,'hpnicfSyslogLogbufferEntry':hpnicfSyslogLogbufferEntry,_R:hpnicfLogbufferIndex,'hpnicfLogbufferCurrentMessages':hpnicfLogbufferCurrentMessages,'hpnicfLogbufferOverwrittenMessages':hpnicfLogbufferOverwrittenMessages,'hpnicfLogbufferDroppedMessages':hpnicfLogbufferDroppedMessages,'hpnicfSyslogLogbufContTable':hpnicfSyslogLogbufContTable,'hpnicfSyslogLogbufContEntry':hpnicfSyslogLogbufContEntry,_S:hpnicfLogbufContIndex,'hpnicfLogbufContDescription':hpnicfLogbufContDescription,'hpnicfSyslogTrapbuffer':hpnicfSyslogTrapbuffer,'hpnicfSyslogTrapbufferChannel':hpnicfSyslogTrapbufferChannel,'hpnicfSyslogTrapbufferSize':hpnicfSyslogTrapbufferSize,'hpnicfSyslogTrapbufferTable':hpnicfSyslogTrapbufferTable,'hpnicfSyslogTrapbufferEntry':hpnicfSyslogTrapbufferEntry,_T:hpnicfTrapbufferIndex,'hpnicfTrapbufferCurrentMessages':hpnicfTrapbufferCurrentMessages,'hpnicfTrapbufferOverwrittenMessages':hpnicfTrapbufferOverwrittenMessages,'hpnicfTrapbufferDroppedMessages':hpnicfTrapbufferDroppedMessages,'hpnicfSyslogLoghost':hpnicfSyslogLoghost,'hpnicfSyslogLoghostSourceInterface':hpnicfSyslogLoghostSourceInterface,'hpnicfSyslogLoghostTimestampType':hpnicfSyslogLoghostTimestampType,'hpnicfSyslogLoghostTable':hpnicfSyslogLoghostTable,'hpnicfSyslogLoghostEntry':hpnicfSyslogLoghostEntry,_U:hpnicfSyslogLoghostIndex,'hpnicfSyslogLoghostChannel':hpnicfSyslogLoghostChannel,'hpnicfSyslogLoghostIpaddressType':hpnicfSyslogLoghostIpaddressType,'hpnicfSyslogLoghostIpaddress':hpnicfSyslogLoghostIpaddress,'hpnicfSyslogLoghostFacility':hpnicfSyslogLoghostFacility,'hpnicfSyslogLoghostLanguage':hpnicfSyslogLoghostLanguage,'hpnicfSyslogLoghostOperateRowStatus':hpnicfSyslogLoghostOperateRowStatus,'hpnicfSyslogLoghostIpaddressPort':hpnicfSyslogLoghostIpaddressPort,'hpnicfSyslogLoghostTAddress':hpnicfSyslogLoghostTAddress,'hpnicfSyslogChannel':hpnicfSyslogChannel,'hpnicfSyslogChannelTable':hpnicfSyslogChannelTable,'hpnicfSyslogChannelEntry':hpnicfSyslogChannelEntry,_I:hpnicfSyslogChannelIndex,'hpnicfSyslogChannelName':hpnicfSyslogChannelName,'hpnicfSyslogModule':hpnicfSyslogModule,'hpnicfSyslogModuleTable':hpnicfSyslogModuleTable,'hpnicfSyslogModuleEntry':hpnicfSyslogModuleEntry,_J:hpnicfSyslogModuleIndex,'hpnicfSyslogModuleName':hpnicfSyslogModuleName,'hpnicfSyslogLog':hpnicfSyslogLog,'hpnicfSyslogLogTimestampType':hpnicfSyslogLogTimestampType,'hpnicfSyslogLogTable':hpnicfSyslogLogTable,'hpnicfSyslogLogEntry':hpnicfSyslogLogEntry,'hpnicfSyslogLogState':hpnicfSyslogLogState,'hpnicfSyslogLogLevel':hpnicfSyslogLogLevel,'hpnicfSyslogLogRowStatus':hpnicfSyslogLogRowStatus,'hpnicfSyslogLogGlobalLevel':hpnicfSyslogLogGlobalLevel,'hpnicfSyslogLogGlobalLevelRfc':hpnicfSyslogLogGlobalLevelRfc,'hpnicfSyslogTrap':hpnicfSyslogTrap,'hpnicfSyslogTrapTimestampType':hpnicfSyslogTrapTimestampType,'hpnicfSyslogTrapTable':hpnicfSyslogTrapTable,'hpnicfSyslogTrapEntry':hpnicfSyslogTrapEntry,'hpnicfSyslogTrapState':hpnicfSyslogTrapState,'hpnicfSyslogTrapLevel':hpnicfSyslogTrapLevel,'hpnicfSyslogTrapRowStatus':hpnicfSyslogTrapRowStatus,'hpnicfSyslogDebug':hpnicfSyslogDebug,'hpnicfSyslogDebugTimestampType':hpnicfSyslogDebugTimestampType,'hpnicfSyslogDebugTable':hpnicfSyslogDebugTable,'hpnicfSyslogDebugEntry':hpnicfSyslogDebugEntry,'hpnicfSyslogDebugState':hpnicfSyslogDebugState,'hpnicfSyslogDebugLevel':hpnicfSyslogDebugLevel,'hpnicfSyslogDebugRowStatus':hpnicfSyslogDebugRowStatus})