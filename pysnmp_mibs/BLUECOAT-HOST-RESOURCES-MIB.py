_A='OctetString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_A,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
blueCoatHostResourcesMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,9))
if mibBuilder.loadTexts:blueCoatHostResourcesMIB.setRevisions(('2007-04-24 00:00',))
_BchrDevice_ObjectIdentity=ObjectIdentity
bchrDevice=_BchrDevice_ObjectIdentity((1,3,6,1,4,1,3417,2,9,1))
class _BchrSerial_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BchrSerial_Type.__name__=_A
_BchrSerial_Object=MibScalar
bchrSerial=_BchrSerial_Object((1,3,6,1,4,1,3417,2,9,1,1),_BchrSerial_Type())
bchrSerial.setMaxAccess('read-only')
if mibBuilder.loadTexts:bchrSerial.setStatus('deprecated')
mibBuilder.exportSymbols('BLUECOAT-HOST-RESOURCES-MIB',**{'blueCoatHostResourcesMIB':blueCoatHostResourcesMIB,'bchrDevice':bchrDevice,'bchrSerial':bchrSerial})