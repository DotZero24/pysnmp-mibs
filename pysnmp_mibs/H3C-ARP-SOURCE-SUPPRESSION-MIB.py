_C='current'
_B='read-write'
_A='Unsigned32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cARPSourceSuppression=ModuleIdentity((1,3,6,1,4,1,2011,10,2,146))
if mibBuilder.loadTexts:h3cARPSourceSuppression.setRevisions(('2013-10-14 18:00',))
_H3cARPSourceSuppressionObjects_ObjectIdentity=ObjectIdentity
h3cARPSourceSuppressionObjects=_H3cARPSourceSuppressionObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,146,1))
_H3cARPSourceSuppressionGlobal_ObjectIdentity=ObjectIdentity
h3cARPSourceSuppressionGlobal=_H3cARPSourceSuppressionGlobal_ObjectIdentity((1,3,6,1,4,1,2011,10,2,146,1,1))
_H3cARPSourceSuppressionEnable_Type=TruthValue
_H3cARPSourceSuppressionEnable_Object=MibScalar
h3cARPSourceSuppressionEnable=_H3cARPSourceSuppressionEnable_Object((1,3,6,1,4,1,2011,10,2,146,1,1,1),_H3cARPSourceSuppressionEnable_Type())
h3cARPSourceSuppressionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cARPSourceSuppressionEnable.setStatus(_C)
class _H3cARPSourceSuppressionLimit_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1024))
_H3cARPSourceSuppressionLimit_Type.__name__=_A
_H3cARPSourceSuppressionLimit_Object=MibScalar
h3cARPSourceSuppressionLimit=_H3cARPSourceSuppressionLimit_Object((1,3,6,1,4,1,2011,10,2,146,1,1,2),_H3cARPSourceSuppressionLimit_Type())
h3cARPSourceSuppressionLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cARPSourceSuppressionLimit.setStatus(_C)
mibBuilder.exportSymbols('H3C-ARP-SOURCE-SUPPRESSION-MIB',**{'h3cARPSourceSuppression':h3cARPSourceSuppression,'h3cARPSourceSuppressionObjects':h3cARPSourceSuppressionObjects,'h3cARPSourceSuppressionGlobal':h3cARPSourceSuppressionGlobal,'h3cARPSourceSuppressionEnable':h3cARPSourceSuppressionEnable,'h3cARPSourceSuppressionLimit':h3cARPSourceSuppressionLimit})