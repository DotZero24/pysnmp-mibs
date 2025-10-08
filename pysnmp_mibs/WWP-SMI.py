#
# PySNMP MIB module WWP-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/WWP-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("WWP-SMI", wwpProducts=wwpProducts, PYSNMP_MODULE_ID=wwp, wwpModules=wwpModules, wwpModulesLeosTce=wwpModulesLeosTce, wwpModulesLeos=wwpModulesLeos, wwp=wwp)
