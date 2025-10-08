#
# PySNMP MIB module FS-ROUTER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-ROUTER-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
products, = mibBuilder.importSymbols("FS-SMI", "products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
router = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 2))
routerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 2, 1))
routerMib.setRevisions(('2005-01-06 00:00',))
if mibBuilder.loadTexts: routerMib.setLastUpdated('200501060000Z')
if mibBuilder.loadTexts: routerMib.setOrganization('FS.COM Inc..')
fsRouterProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 2, 1, 1))
if mibBuilder.loadTexts: fsRouterProducts.setStatus('current')
mibBuilder.exportSymbols("FS-ROUTER-SMI", fsRouterProducts=fsRouterProducts, PYSNMP_MODULE_ID=routerMib, routerMib=routerMib, router=router)
