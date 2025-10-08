#
# PySNMP MIB module ZYXEL-ES-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-ES-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zyxel = MibIdentifier((1, 3, 6, 1, 4, 1, 890))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1))
enterpriseSolution = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15))
if mibBuilder.loadTexts: enterpriseSolution.setLastUpdated('201009200000Z')
if mibBuilder.loadTexts: enterpriseSolution.setOrganization('Enterprise Solution ZyXEL')
esAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 1))
if mibBuilder.loadTexts: esAgentCapability.setStatus('current')
esConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 2))
if mibBuilder.loadTexts: esConformance.setStatus('current')
esMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3))
if mibBuilder.loadTexts: esMgmt.setStatus('current')
esProductSpecific = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 4))
if mibBuilder.loadTexts: esProductSpecific.setStatus('current')
esPartnerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 5))
if mibBuilder.loadTexts: esPartnerProducts.setStatus('current')
tenders = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 4))
zyxelNAS = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 4, 4, 5))
if mibBuilder.loadTexts: zyxelNAS.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-ES-SMI", esAgentCapability=esAgentCapability, zyxel=zyxel, tenders=tenders, products=products, zyxelNAS=zyxelNAS, esPartnerProducts=esPartnerProducts, esConformance=esConformance, esProductSpecific=esProductSpecific, enterpriseSolution=enterpriseSolution, PYSNMP_MODULE_ID=enterpriseSolution, esMgmt=esMgmt)
