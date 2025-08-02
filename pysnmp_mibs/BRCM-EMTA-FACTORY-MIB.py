_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataFactory,=mibBuilder.importSymbols('BRCM-CABLEDATA-FACTORY-MIB','cableDataFactory')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
emtaFactory=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,6))
if mibBuilder.loadTexts:emtaFactory.setRevisions(('2007-02-05 00:00','2005-11-14 00:00','2005-06-28 00:00','2005-06-14 00:00','2004-03-24 00:00','2002-08-23 00:00'))
_EmtaFactoryBase_ObjectIdentity=ObjectIdentity
emtaFactoryBase=_EmtaFactoryBase_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,6,1))
_EmtaHighVoltageRingEnabled_Type=TruthValue
_EmtaHighVoltageRingEnabled_Object=MibScalar
emtaHighVoltageRingEnabled=_EmtaHighVoltageRingEnabled_Object((1,3,6,1,4,1,4413,2,99,1,1,2,6,1,1),_EmtaHighVoltageRingEnabled_Type())
emtaHighVoltageRingEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:emtaHighVoltageRingEnabled.setStatus(_B)
_EmtaDynamicLoadBalancingEnabled_Type=TruthValue
_EmtaDynamicLoadBalancingEnabled_Object=MibScalar
emtaDynamicLoadBalancingEnabled=_EmtaDynamicLoadBalancingEnabled_Object((1,3,6,1,4,1,4413,2,99,1,1,2,6,1,2),_EmtaDynamicLoadBalancingEnabled_Type())
emtaDynamicLoadBalancingEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:emtaDynamicLoadBalancingEnabled.setStatus(_B)
_EmtaFactorySecurity_ObjectIdentity=ObjectIdentity
emtaFactorySecurity=_EmtaFactorySecurity_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,6,2))
_EmtaTelephonyRootCertificate_Type=OctetString
_EmtaTelephonyRootCertificate_Object=MibScalar
emtaTelephonyRootCertificate=_EmtaTelephonyRootCertificate_Object((1,3,6,1,4,1,4413,2,99,1,1,2,6,2,1),_EmtaTelephonyRootCertificate_Type())
emtaTelephonyRootCertificate.setMaxAccess(_A)
if mibBuilder.loadTexts:emtaTelephonyRootCertificate.setStatus(_B)
_EmtaManufacturerCertificate_Type=OctetString
_EmtaManufacturerCertificate_Object=MibScalar
emtaManufacturerCertificate=_EmtaManufacturerCertificate_Object((1,3,6,1,4,1,4413,2,99,1,1,2,6,2,2),_EmtaManufacturerCertificate_Type())
emtaManufacturerCertificate.setMaxAccess(_A)
if mibBuilder.loadTexts:emtaManufacturerCertificate.setStatus(_B)
_EmtaDeviceCertificate_Type=OctetString
_EmtaDeviceCertificate_Object=MibScalar
emtaDeviceCertificate=_EmtaDeviceCertificate_Object((1,3,6,1,4,1,4413,2,99,1,1,2,6,2,3),_EmtaDeviceCertificate_Type())
emtaDeviceCertificate.setMaxAccess(_A)
if mibBuilder.loadTexts:emtaDeviceCertificate.setStatus(_B)
_EmtaDevPrivKeyModulus_Type=OctetString
_EmtaDevPrivKeyModulus_Object=MibScalar
emtaDevPrivKeyModulus=_EmtaDevPrivKeyModulus_Object((1,3,6,1,4,1,4413,2,99,1,1,2,6,2,4),_EmtaDevPrivKeyModulus_Type())
emtaDevPrivKeyModulus.setMaxAccess(_A)
if mibBuilder.loadTexts:emtaDevPrivKeyModulus.setStatus(_B)
_EmtaDevPrivKeyExponent_Type=OctetString
_EmtaDevPrivKeyExponent_Object=MibScalar
emtaDevPrivKeyExponent=_EmtaDevPrivKeyExponent_Object((1,3,6,1,4,1,4413,2,99,1,1,2,6,2,5),_EmtaDevPrivKeyExponent_Type())
emtaDevPrivKeyExponent.setMaxAccess(_A)
if mibBuilder.loadTexts:emtaDevPrivKeyExponent.setStatus(_B)
mibBuilder.exportSymbols('BRCM-EMTA-FACTORY-MIB',**{'emtaFactory':emtaFactory,'emtaFactoryBase':emtaFactoryBase,'emtaHighVoltageRingEnabled':emtaHighVoltageRingEnabled,'emtaDynamicLoadBalancingEnabled':emtaDynamicLoadBalancingEnabled,'emtaFactorySecurity':emtaFactorySecurity,'emtaTelephonyRootCertificate':emtaTelephonyRootCertificate,'emtaManufacturerCertificate':emtaManufacturerCertificate,'emtaDeviceCertificate':emtaDeviceCertificate,'emtaDevPrivKeyModulus':emtaDevPrivKeyModulus,'emtaDevPrivKeyExponent':emtaDevPrivKeyExponent})