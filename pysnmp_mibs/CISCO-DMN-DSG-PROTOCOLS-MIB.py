_E='enable'
_D='disable'
_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGProtocols=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,39))
if mibBuilder.loadTexts:ciscoDSGProtocols.setRevisions(('2013-07-10 19:03','2012-03-07 07:30'))
class _ProtocolsCtrlTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ProtocolsCtrlTelnet_Type.__name__=_A
_ProtocolsCtrlTelnet_Object=MibScalar
protocolsCtrlTelnet=_ProtocolsCtrlTelnet_Object((1,3,6,1,4,1,1429,2,2,5,39,1),_ProtocolsCtrlTelnet_Type())
protocolsCtrlTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlTelnet.setStatus(_C)
class _ProtocolsCtrlSSH_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ProtocolsCtrlSSH_Type.__name__=_A
_ProtocolsCtrlSSH_Object=MibScalar
protocolsCtrlSSH=_ProtocolsCtrlSSH_Object((1,3,6,1,4,1,1429,2,2,5,39,2),_ProtocolsCtrlSSH_Type())
protocolsCtrlSSH.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlSSH.setStatus(_C)
class _ProtocolsCtrlHTTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),('secure',3)))
_ProtocolsCtrlHTTP_Type.__name__=_A
_ProtocolsCtrlHTTP_Object=MibScalar
protocolsCtrlHTTP=_ProtocolsCtrlHTTP_Object((1,3,6,1,4,1,1429,2,2,5,39,3),_ProtocolsCtrlHTTP_Type())
protocolsCtrlHTTP.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlHTTP.setStatus(_C)
class _ProtocolsCtrlSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ProtocolsCtrlSNMP_Type.__name__=_A
_ProtocolsCtrlSNMP_Object=MibScalar
protocolsCtrlSNMP=_ProtocolsCtrlSNMP_Object((1,3,6,1,4,1,1429,2,2,5,39,5),_ProtocolsCtrlSNMP_Type())
protocolsCtrlSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlSNMP.setStatus(_C)
class _ProtocolsCtrlRIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ProtocolsCtrlRIP_Type.__name__=_A
_ProtocolsCtrlRIP_Object=MibScalar
protocolsCtrlRIP=_ProtocolsCtrlRIP_Object((1,3,6,1,4,1,1429,2,2,5,39,6),_ProtocolsCtrlRIP_Type())
protocolsCtrlRIP.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlRIP.setStatus(_C)
class _ProtocolsCtrlMPE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fwdNone',1),('fwdAll',2),('fwdFiltered',3)))
_ProtocolsCtrlMPE_Type.__name__=_A
_ProtocolsCtrlMPE_Object=MibScalar
protocolsCtrlMPE=_ProtocolsCtrlMPE_Object((1,3,6,1,4,1,1429,2,2,5,39,7),_ProtocolsCtrlMPE_Type())
protocolsCtrlMPE.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlMPE.setStatus(_C)
class _ProtocolsCtrlIGMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('v3',2),('v2',3)))
_ProtocolsCtrlIGMP_Type.__name__=_A
_ProtocolsCtrlIGMP_Object=MibScalar
protocolsCtrlIGMP=_ProtocolsCtrlIGMP_Object((1,3,6,1,4,1,1429,2,2,5,39,8),_ProtocolsCtrlIGMP_Type())
protocolsCtrlIGMP.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlIGMP.setStatus(_C)
class _ProtocolslTimeoutsIdleSessonGlobal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1209600))
_ProtocolslTimeoutsIdleSessonGlobal_Type.__name__=_A
_ProtocolslTimeoutsIdleSessonGlobal_Object=MibScalar
protocolslTimeoutsIdleSessonGlobal=_ProtocolslTimeoutsIdleSessonGlobal_Object((1,3,6,1,4,1,1429,2,2,5,39,9),_ProtocolslTimeoutsIdleSessonGlobal_Type())
protocolslTimeoutsIdleSessonGlobal.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolslTimeoutsIdleSessonGlobal.setStatus(_C)
class _ProtocolsCtrlSyslog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('legacy',2),('syslogTcp',3),('syslogUdp',4)))
_ProtocolsCtrlSyslog_Type.__name__=_A
_ProtocolsCtrlSyslog_Object=MibScalar
protocolsCtrlSyslog=_ProtocolsCtrlSyslog_Object((1,3,6,1,4,1,1429,2,2,5,39,10),_ProtocolsCtrlSyslog_Type())
protocolsCtrlSyslog.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlSyslog.setStatus(_C)
_ProtocolsCtrlSyslogCfgIpAddr_Type=IpAddress
_ProtocolsCtrlSyslogCfgIpAddr_Object=MibScalar
protocolsCtrlSyslogCfgIpAddr=_ProtocolsCtrlSyslogCfgIpAddr_Object((1,3,6,1,4,1,1429,2,2,5,39,11),_ProtocolsCtrlSyslogCfgIpAddr_Type())
protocolsCtrlSyslogCfgIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlSyslogCfgIpAddr.setStatus(_C)
class _ProtocolsCtrlSyslogCfgPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ProtocolsCtrlSyslogCfgPort_Type.__name__=_A
_ProtocolsCtrlSyslogCfgPort_Object=MibScalar
protocolsCtrlSyslogCfgPort=_ProtocolsCtrlSyslogCfgPort_Object((1,3,6,1,4,1,1429,2,2,5,39,12),_ProtocolsCtrlSyslogCfgPort_Type())
protocolsCtrlSyslogCfgPort.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolsCtrlSyslogCfgPort.setStatus(_C)
mibBuilder.exportSymbols('CISCO-DMN-DSG-PROTOCOLS-MIB',**{'ciscoDSGProtocols':ciscoDSGProtocols,'protocolsCtrlTelnet':protocolsCtrlTelnet,'protocolsCtrlSSH':protocolsCtrlSSH,'protocolsCtrlHTTP':protocolsCtrlHTTP,'protocolsCtrlSNMP':protocolsCtrlSNMP,'protocolsCtrlRIP':protocolsCtrlRIP,'protocolsCtrlMPE':protocolsCtrlMPE,'protocolsCtrlIGMP':protocolsCtrlIGMP,'protocolslTimeoutsIdleSessonGlobal':protocolslTimeoutsIdleSessonGlobal,'protocolsCtrlSyslog':protocolsCtrlSyslog,'protocolsCtrlSyslogCfgIpAddr':protocolsCtrlSyslogCfgIpAddr,'protocolsCtrlSyslogCfgPort':protocolsCtrlSyslogCfgPort})