_B='EnabledStatus'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cMulticast=ModuleIdentity((1,3,6,1,4,1,2011,10,2,50))
if mibBuilder.loadTexts:h3cMulticast.setRevisions(('2005-04-29 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cMulticastObject_ObjectIdentity=ObjectIdentity
h3cMulticastObject=_H3cMulticastObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,50,1))
class _H3cMulticastEnable_Type(EnabledStatus):defaultValue=2
_H3cMulticastEnable_Type.__name__=_B
_H3cMulticastEnable_Object=MibScalar
h3cMulticastEnable=_H3cMulticastEnable_Object((1,3,6,1,4,1,2011,10,2,50,1,1),_H3cMulticastEnable_Type())
h3cMulticastEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cMulticastEnable.setStatus(_A)
mibBuilder.exportSymbols('H3C-MULTICAST-MIB',**{_B:EnabledStatus,'h3cMulticast':h3cMulticast,'h3cMulticastObject':h3cMulticastObject,'h3cMulticastEnable':h3cMulticastEnable})