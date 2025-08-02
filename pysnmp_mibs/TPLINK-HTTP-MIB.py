_E='enable'
_D='disable'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkHttp=ModuleIdentity((1,3,6,1,4,1,11863,6,51))
if mibBuilder.loadTexts:tplinkHttp.setRevisions(('2015-01-21 10:30',))
_TplinkHttpMIBObjects_ObjectIdentity=ObjectIdentity
tplinkHttpMIBObjects=_TplinkHttpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,51,1))
class _HttpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HttpEnable_Type.__name__=_C
_HttpEnable_Object=MibScalar
httpEnable=_HttpEnable_Object((1,3,6,1,4,1,11863,6,51,1,1),_HttpEnable_Type())
httpEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:httpEnable.setStatus(_B)
class _HttpSessionTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_HttpSessionTimeOut_Type.__name__=_C
_HttpSessionTimeOut_Object=MibScalar
httpSessionTimeOut=_HttpSessionTimeOut_Object((1,3,6,1,4,1,11863,6,51,1,2),_HttpSessionTimeOut_Type())
httpSessionTimeOut.setMaxAccess(_A)
if mibBuilder.loadTexts:httpSessionTimeOut.setStatus(_B)
class _HttpUserLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HttpUserLimitEnable_Type.__name__=_C
_HttpUserLimitEnable_Object=MibScalar
httpUserLimitEnable=_HttpUserLimitEnable_Object((1,3,6,1,4,1,11863,6,51,1,3),_HttpUserLimitEnable_Type())
httpUserLimitEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:httpUserLimitEnable.setStatus(_B)
_HttpUserLimitMaxAdminNum_Type=Integer32
_HttpUserLimitMaxAdminNum_Object=MibScalar
httpUserLimitMaxAdminNum=_HttpUserLimitMaxAdminNum_Object((1,3,6,1,4,1,11863,6,51,1,4),_HttpUserLimitMaxAdminNum_Type())
httpUserLimitMaxAdminNum.setMaxAccess(_A)
if mibBuilder.loadTexts:httpUserLimitMaxAdminNum.setStatus(_B)
_HttpUserLimitMaxOperatorNum_Type=Integer32
_HttpUserLimitMaxOperatorNum_Object=MibScalar
httpUserLimitMaxOperatorNum=_HttpUserLimitMaxOperatorNum_Object((1,3,6,1,4,1,11863,6,51,1,5),_HttpUserLimitMaxOperatorNum_Type())
httpUserLimitMaxOperatorNum.setMaxAccess(_A)
if mibBuilder.loadTexts:httpUserLimitMaxOperatorNum.setStatus(_B)
_HttpUserLimitMaxPowerUserNum_Type=Integer32
_HttpUserLimitMaxPowerUserNum_Object=MibScalar
httpUserLimitMaxPowerUserNum=_HttpUserLimitMaxPowerUserNum_Object((1,3,6,1,4,1,11863,6,51,1,6),_HttpUserLimitMaxPowerUserNum_Type())
httpUserLimitMaxPowerUserNum.setMaxAccess(_A)
if mibBuilder.loadTexts:httpUserLimitMaxPowerUserNum.setStatus(_B)
_HttpUserLimitMaxUserNum_Type=Integer32
_HttpUserLimitMaxUserNum_Object=MibScalar
httpUserLimitMaxUserNum=_HttpUserLimitMaxUserNum_Object((1,3,6,1,4,1,11863,6,51,1,7),_HttpUserLimitMaxUserNum_Type())
httpUserLimitMaxUserNum.setMaxAccess(_A)
if mibBuilder.loadTexts:httpUserLimitMaxUserNum.setStatus(_B)
class _HttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HttpPort_Type.__name__=_C
_HttpPort_Object=MibScalar
httpPort=_HttpPort_Object((1,3,6,1,4,1,11863,6,51,1,8),_HttpPort_Type())
httpPort.setMaxAccess(_A)
if mibBuilder.loadTexts:httpPort.setStatus(_B)
_TplinkHttpMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkHttpMIBNotifications=_TplinkHttpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,51,2))
mibBuilder.exportSymbols('TPLINK-HTTP-MIB',**{'tplinkHttp':tplinkHttp,'tplinkHttpMIBObjects':tplinkHttpMIBObjects,'httpEnable':httpEnable,'httpSessionTimeOut':httpSessionTimeOut,'httpUserLimitEnable':httpUserLimitEnable,'httpUserLimitMaxAdminNum':httpUserLimitMaxAdminNum,'httpUserLimitMaxOperatorNum':httpUserLimitMaxOperatorNum,'httpUserLimitMaxPowerUserNum':httpUserLimitMaxPowerUserNum,'httpUserLimitMaxUserNum':httpUserLimitMaxUserNum,'httpPort':httpPort,'tplinkHttpMIBNotifications':tplinkHttpMIBNotifications})