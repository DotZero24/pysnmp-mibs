#
# PySNMP MIB module WWP-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/WWP-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wwp = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141))
wwp.setRevisions(('2013-02-09 01:36',))
if mibBuilder.loadTexts: wwp.setLastUpdated('201302090136Z')
if mibBuilder.loadTexts: wwp.setOrganization('Ciena, Inc.')
wwpProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 1))
if mibBuilder.loadTexts: wwpProducts.setStatus('current')
wwpModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2))
if mibBuilder.loadTexts: wwpModules.setStatus('current')
wwpModulesLeos = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60))
if mibBuilder.loadTexts: wwpModulesLeos.setStatus('current')
wwpModulesLeosTce = ObjectIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 61))
if mibBuilder.loadTexts: wwpModulesLeosTce.setStatus('current')
mibBuilder.exportSymbols("WWP-SMI", PYSNMP_MODULE_ID=wwp, wwpProducts=wwpProducts, wwp=wwp, wwpModulesLeosTce=wwpModulesLeosTce, wwpModules=wwpModules, wwpModulesLeos=wwpModulesLeos)
