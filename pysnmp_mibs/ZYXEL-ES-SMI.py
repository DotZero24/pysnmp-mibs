#
# PySNMP MIB module ZYXEL-ES-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-ES-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-ES-SMI", esConformance=esConformance, esMgmt=esMgmt, zyxelNAS=zyxelNAS, esPartnerProducts=esPartnerProducts, enterpriseSolution=enterpriseSolution, PYSNMP_MODULE_ID=enterpriseSolution, zyxel=zyxel, tenders=tenders, products=products, esProductSpecific=esProductSpecific, esAgentCapability=esAgentCapability)
