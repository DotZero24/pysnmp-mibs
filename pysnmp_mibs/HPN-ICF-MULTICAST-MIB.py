_B='EnabledStatus'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfMulticast=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,50))
if mibBuilder.loadTexts:hpnicfMulticast.setRevisions(('2005-04-29 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfMulticastObject_ObjectIdentity=ObjectIdentity
hpnicfMulticastObject=_HpnicfMulticastObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,50,1))
class _HpnicfMulticastEnable_Type(EnabledStatus):defaultValue=2
_HpnicfMulticastEnable_Type.__name__=_B
_HpnicfMulticastEnable_Object=MibScalar
hpnicfMulticastEnable=_HpnicfMulticastEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,50,1,1),_HpnicfMulticastEnable_Type())
hpnicfMulticastEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfMulticastEnable.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-MULTICAST-MIB',**{_B:EnabledStatus,'hpnicfMulticast':hpnicfMulticast,'hpnicfMulticastObject':hpnicfMulticastObject,'hpnicfMulticastEnable':hpnicfMulticastEnable})