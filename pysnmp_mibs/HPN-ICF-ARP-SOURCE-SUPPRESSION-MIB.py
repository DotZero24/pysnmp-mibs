_C='current'
_B='read-write'
_A='Unsigned32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicfARPSourceSuppression=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,146))
if mibBuilder.loadTexts:hpnicfARPSourceSuppression.setRevisions(('2013-10-14 18:00',))
_HpnicfARPSourceSuppressionObjects_ObjectIdentity=ObjectIdentity
hpnicfARPSourceSuppressionObjects=_HpnicfARPSourceSuppressionObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,146,1))
_HpnicfARPSourceSuppressionGlobal_ObjectIdentity=ObjectIdentity
hpnicfARPSourceSuppressionGlobal=_HpnicfARPSourceSuppressionGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,146,1,1))
_HpnicfARPSourceSuppressionEnable_Type=TruthValue
_HpnicfARPSourceSuppressionEnable_Object=MibScalar
hpnicfARPSourceSuppressionEnable=_HpnicfARPSourceSuppressionEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,146,1,1,1),_HpnicfARPSourceSuppressionEnable_Type())
hpnicfARPSourceSuppressionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfARPSourceSuppressionEnable.setStatus(_C)
class _HpnicfARPSourceSuppressionLimit_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1024))
_HpnicfARPSourceSuppressionLimit_Type.__name__=_A
_HpnicfARPSourceSuppressionLimit_Object=MibScalar
hpnicfARPSourceSuppressionLimit=_HpnicfARPSourceSuppressionLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,146,1,1,2),_HpnicfARPSourceSuppressionLimit_Type())
hpnicfARPSourceSuppressionLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfARPSourceSuppressionLimit.setStatus(_C)
mibBuilder.exportSymbols('HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB',**{'hpnicfARPSourceSuppression':hpnicfARPSourceSuppression,'hpnicfARPSourceSuppressionObjects':hpnicfARPSourceSuppressionObjects,'hpnicfARPSourceSuppressionGlobal':hpnicfARPSourceSuppressionGlobal,'hpnicfARPSourceSuppressionEnable':hpnicfARPSourceSuppressionEnable,'hpnicfARPSourceSuppressionLimit':hpnicfARPSourceSuppressionLimit})