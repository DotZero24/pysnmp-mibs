#
# PySNMP MIB module ATTO-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/atto/ATTO-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ATTO-PRODUCTS-MIB", attoModules=attoModules, attoHba=attoHba, attoAgentCapability=attoAgentCapability, attotech=attotech, attoMgmt=attoMgmt, attoGenericDevice=attoGenericDevice, attoFB6500=attoFB6500, attoProductsMIB=attoProductsMIB, attoFB6500N=attoFB6500N, PYSNMP_MODULE_ID=attoProductsMIB, attoProducts=attoProducts)
