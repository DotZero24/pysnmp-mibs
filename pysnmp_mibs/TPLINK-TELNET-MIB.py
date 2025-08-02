_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkTelnet=ModuleIdentity((1,3,6,1,4,1,11863,6,52))
if mibBuilder.loadTexts:tplinkTelnet.setRevisions(('2016-02-26 11:10',))
_TplinkTelnetMIBObjects_ObjectIdentity=ObjectIdentity
tplinkTelnetMIBObjects=_TplinkTelnetMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,52,1))
class _TelnetConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TelnetConfig_Type.__name__=_A
_TelnetConfig_Object=MibScalar
telnetConfig=_TelnetConfig_Object((1,3,6,1,4,1,11863,6,52,1,1),_TelnetConfig_Type())
telnetConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetConfig.setStatus(_C)
class _TelnetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TelnetPort_Type.__name__=_A
_TelnetPort_Object=MibScalar
telnetPort=_TelnetPort_Object((1,3,6,1,4,1,11863,6,52,1,2),_TelnetPort_Type())
telnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetPort.setStatus(_C)
_TplinkTelnetMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkTelnetMIBNotifications=_TplinkTelnetMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,52,2))
mibBuilder.exportSymbols('TPLINK-TELNET-MIB',**{'tplinkTelnet':tplinkTelnet,'tplinkTelnetMIBObjects':tplinkTelnetMIBObjects,'telnetConfig':telnetConfig,'telnetPort':telnetPort,'tplinkTelnetMIBNotifications':tplinkTelnetMIBNotifications})