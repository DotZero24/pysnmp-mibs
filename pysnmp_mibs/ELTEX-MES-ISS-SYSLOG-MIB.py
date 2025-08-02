_D='DisplayString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
eltMesIssSyslogMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,22))
if mibBuilder.loadTexts:eltMesIssSyslogMIB.setRevisions(('2020-07-29 00:00',))
_EltMesIssSyslogObjects_ObjectIdentity=ObjectIdentity
eltMesIssSyslogObjects=_EltMesIssSyslogObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,22,1))
_EltMesIssSyslogGlobals_ObjectIdentity=ObjectIdentity
eltMesIssSyslogGlobals=_EltMesIssSyslogGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,22,1,1))
class _EltMesIssSyslogVersionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('empty',1),('present',2)))
_EltMesIssSyslogVersionMode_Type.__name__=_B
_EltMesIssSyslogVersionMode_Object=MibScalar
eltMesIssSyslogVersionMode=_EltMesIssSyslogVersionMode_Object((1,3,6,1,4,1,35265,1,139,22,1,1,1),_EltMesIssSyslogVersionMode_Type())
eltMesIssSyslogVersionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSyslogVersionMode.setStatus(_A)
class _EltMesIssSyslogVersionString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_EltMesIssSyslogVersionString_Type.__name__=_D
_EltMesIssSyslogVersionString_Object=MibScalar
eltMesIssSyslogVersionString=_EltMesIssSyslogVersionString_Object((1,3,6,1,4,1,35265,1,139,22,1,1,2),_EltMesIssSyslogVersionString_Type())
eltMesIssSyslogVersionString.setMaxAccess('read-only')
if mibBuilder.loadTexts:eltMesIssSyslogVersionString.setStatus(_A)
class _EltMesIssSyslogTimestampMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('legacy',1),('rfc5424',2)))
_EltMesIssSyslogTimestampMode_Type.__name__=_B
_EltMesIssSyslogTimestampMode_Object=MibScalar
eltMesIssSyslogTimestampMode=_EltMesIssSyslogTimestampMode_Object((1,3,6,1,4,1,35265,1,139,22,1,1,3),_EltMesIssSyslogTimestampMode_Type())
eltMesIssSyslogTimestampMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSyslogTimestampMode.setStatus(_A)
class _EltMesIssSyslogHostnameMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('empty',1),('string',2),('hostname',3),('ip',4),('ipv6',5)))
_EltMesIssSyslogHostnameMode_Type.__name__=_B
_EltMesIssSyslogHostnameMode_Object=MibScalar
eltMesIssSyslogHostnameMode=_EltMesIssSyslogHostnameMode_Object((1,3,6,1,4,1,35265,1,139,22,1,1,4),_EltMesIssSyslogHostnameMode_Type())
eltMesIssSyslogHostnameMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSyslogHostnameMode.setStatus(_A)
class _EltMesIssSyslogHostnameString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesIssSyslogHostnameString_Type.__name__=_D
_EltMesIssSyslogHostnameString_Object=MibScalar
eltMesIssSyslogHostnameString=_EltMesIssSyslogHostnameString_Object((1,3,6,1,4,1,35265,1,139,22,1,1,5),_EltMesIssSyslogHostnameString_Type())
eltMesIssSyslogHostnameString.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssSyslogHostnameString.setStatus(_A)
_EltMesIssSyslogNotifications_ObjectIdentity=ObjectIdentity
eltMesIssSyslogNotifications=_EltMesIssSyslogNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,22,2))
mibBuilder.exportSymbols('ELTEX-MES-ISS-SYSLOG-MIB',**{'eltMesIssSyslogMIB':eltMesIssSyslogMIB,'eltMesIssSyslogObjects':eltMesIssSyslogObjects,'eltMesIssSyslogGlobals':eltMesIssSyslogGlobals,'eltMesIssSyslogVersionMode':eltMesIssSyslogVersionMode,'eltMesIssSyslogVersionString':eltMesIssSyslogVersionString,'eltMesIssSyslogTimestampMode':eltMesIssSyslogTimestampMode,'eltMesIssSyslogHostnameMode':eltMesIssSyslogHostnameMode,'eltMesIssSyslogHostnameString':eltMesIssSyslogHostnameString,'eltMesIssSyslogNotifications':eltMesIssSyslogNotifications})