_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDiagnostic=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,95))
_ZyxelLocatorLedStatus_ObjectIdentity=ObjectIdentity
zyxelLocatorLedStatus=_ZyxelLocatorLedStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,95,1))
class _ZyLocatorLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_ZyLocatorLed_Type.__name__=_A
_ZyLocatorLed_Object=MibScalar
zyLocatorLed=_ZyLocatorLed_Object((1,3,6,1,4,1,890,1,15,3,95,1,1),_ZyLocatorLed_Type())
zyLocatorLed.setMaxAccess('read-write')
if mibBuilder.loadTexts:zyLocatorLed.setStatus('current')
mibBuilder.exportSymbols('ZYXEL-DIAGNOSTIC-MIB',**{'zyxelDiagnostic':zyxelDiagnostic,'zyxelLocatorLedStatus':zyxelLocatorLedStatus,'zyLocatorLed':zyLocatorLed})