_D='EnableVar'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_D)
rcSntp=ModuleIdentity((1,3,6,1,4,1,8886,6,1,8))
if mibBuilder.loadTexts:rcSntp.setRevisions(('1904-12-20 00:00',))
_RcSntpServer_ObjectIdentity=ObjectIdentity
rcSntpServer=_RcSntpServer_ObjectIdentity((1,3,6,1,4,1,8886,6,1,8,1))
class _RcSntpServerEnable_Type(EnableVar):defaultValue=2
_RcSntpServerEnable_Type.__name__=_D
_RcSntpServerEnable_Object=MibScalar
rcSntpServerEnable=_RcSntpServerEnable_Object((1,3,6,1,4,1,8886,6,1,8,1,1),_RcSntpServerEnable_Type())
rcSntpServerEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:rcSntpServerEnable.setStatus(_B)
_RcSntpServerBroadcastAddress_Type=IpAddress
_RcSntpServerBroadcastAddress_Object=MibScalar
rcSntpServerBroadcastAddress=_RcSntpServerBroadcastAddress_Object((1,3,6,1,4,1,8886,6,1,8,1,2),_RcSntpServerBroadcastAddress_Type())
rcSntpServerBroadcastAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:rcSntpServerBroadcastAddress.setStatus(_B)
class _RcSntpServerSendInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcSntpServerSendInterval_Type.__name__=_C
_RcSntpServerSendInterval_Object=MibScalar
rcSntpServerSendInterval=_RcSntpServerSendInterval_Object((1,3,6,1,4,1,8886,6,1,8,1,3),_RcSntpServerSendInterval_Type())
rcSntpServerSendInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:rcSntpServerSendInterval.setStatus(_B)
_RcSntpClient_ObjectIdentity=ObjectIdentity
rcSntpClient=_RcSntpClient_ObjectIdentity((1,3,6,1,4,1,8886,6,1,8,2))
_RcSntpClientAddress_Type=IpAddress
_RcSntpClientAddress_Object=MibScalar
rcSntpClientAddress=_RcSntpClientAddress_Object((1,3,6,1,4,1,8886,6,1,8,2,1),_RcSntpClientAddress_Type())
rcSntpClientAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:rcSntpClientAddress.setStatus(_B)
class _RcSntpClientGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('get',1))
_RcSntpClientGet_Type.__name__=_C
_RcSntpClientGet_Object=MibScalar
rcSntpClientGet=_RcSntpClientGet_Object((1,3,6,1,4,1,8886,6,1,8,2,2),_RcSntpClientGet_Type())
rcSntpClientGet.setMaxAccess(_A)
if mibBuilder.loadTexts:rcSntpClientGet.setStatus(_B)
class _RcSntpClientListenEnable_Type(EnableVar):defaultValue=2
_RcSntpClientListenEnable_Type.__name__=_D
_RcSntpClientListenEnable_Object=MibScalar
rcSntpClientListenEnable=_RcSntpClientListenEnable_Object((1,3,6,1,4,1,8886,6,1,8,2,3),_RcSntpClientListenEnable_Type())
rcSntpClientListenEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:rcSntpClientListenEnable.setStatus(_B)
mibBuilder.exportSymbols('SWITCH-SNTP-MIB',**{'rcSntp':rcSntp,'rcSntpServer':rcSntpServer,'rcSntpServerEnable':rcSntpServerEnable,'rcSntpServerBroadcastAddress':rcSntpServerBroadcastAddress,'rcSntpServerSendInterval':rcSntpServerSendInterval,'rcSntpClient':rcSntpClient,'rcSntpClientAddress':rcSntpClientAddress,'rcSntpClientGet':rcSntpClientGet,'rcSntpClientListenEnable':rcSntpClientListenEnable})