_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
freeBSD=ModuleIdentity((1,3,6,1,4,1,2238))
if mibBuilder.loadTexts:freeBSD.setRevisions(('2006-10-31 08:00',))
_FreeBSDsrc_ObjectIdentity=ObjectIdentity
freeBSDsrc=_FreeBSDsrc_ObjectIdentity((1,3,6,1,4,1,2238,1))
if mibBuilder.loadTexts:freeBSDsrc.setStatus(_A)
_FreeBSDports_ObjectIdentity=ObjectIdentity
freeBSDports=_FreeBSDports_ObjectIdentity((1,3,6,1,4,1,2238,2))
if mibBuilder.loadTexts:freeBSDports.setStatus(_A)
_FreeBSDpeople_ObjectIdentity=ObjectIdentity
freeBSDpeople=_FreeBSDpeople_ObjectIdentity((1,3,6,1,4,1,2238,3))
if mibBuilder.loadTexts:freeBSDpeople.setStatus(_A)
_FreeBSDpeoplePhk_ObjectIdentity=ObjectIdentity
freeBSDpeoplePhk=_FreeBSDpeoplePhk_ObjectIdentity((1,3,6,1,4,1,2238,3,1))
if mibBuilder.loadTexts:freeBSDpeoplePhk.setStatus(_A)
_FreeBSDVersion_ObjectIdentity=ObjectIdentity
freeBSDVersion=_FreeBSDVersion_ObjectIdentity((1,3,6,1,4,1,2238,4))
if mibBuilder.loadTexts:freeBSDVersion.setStatus(_A)
mibBuilder.exportSymbols('FREEBSD-MIB',**{'freeBSD':freeBSD,'freeBSDsrc':freeBSDsrc,'freeBSDports':freeBSDports,'freeBSDpeople':freeBSDpeople,'freeBSDpeoplePhk':freeBSDpeoplePhk,'freeBSDVersion':freeBSDVersion})