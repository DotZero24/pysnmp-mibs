#
# PySNMP MIB module ATTO-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/atto/ATTO-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:46:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
attoProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4547, 3, 2))
attoProductsMIB.setRevisions(('2013-04-19 13:45',))
if mibBuilder.loadTexts: attoProductsMIB.setLastUpdated('201304191345Z')
if mibBuilder.loadTexts: attoProductsMIB.setOrganization('ATTO Technology, Inc.')
attotech = MibIdentifier((1, 3, 6, 1, 4, 1, 4547))
attoProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1))
attoMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 2))
attoModules = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 3))
attoAgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 4))
attoGenericDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 1))
attoHba = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 3))
attoFB6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 4))
attoFB6500N = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 5))
mibBuilder.exportSymbols("ATTO-PRODUCTS-MIB", attoAgentCapability=attoAgentCapability, attoFB6500=attoFB6500, attoGenericDevice=attoGenericDevice, attoHba=attoHba, attoFB6500N=attoFB6500N, PYSNMP_MODULE_ID=attoProductsMIB, attoModules=attoModules, attoProductsMIB=attoProductsMIB, attotech=attotech, attoMgmt=attoMgmt, attoProducts=attoProducts)
