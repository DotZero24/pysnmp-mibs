#
# PySNMP MIB module CALIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/calix/CALIX-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
calixNetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 6321))
calixNetworks.setRevisions(('2000-08-31 00:26',))
if mibBuilder.loadTexts: calixNetworks.setLastUpdated('200008310026Z')
if mibBuilder.loadTexts: calixNetworks.setOrganization('Calix Networks, Inc.')
calixRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1))
if mibBuilder.loadTexts: calixRegistrations.setStatus('current')
calixModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1, 1))
if mibBuilder.loadTexts: calixModules.setStatus('current')
calixProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 1, 2))
if mibBuilder.loadTexts: calixProducts.setStatus('current')
calixManagement = ObjectIdentity((1, 3, 6, 1, 4, 1, 6321, 2))
if mibBuilder.loadTexts: calixManagement.setStatus('current')
mibBuilder.exportSymbols("CALIX-SMI", calixRegistrations=calixRegistrations, PYSNMP_MODULE_ID=calixNetworks, calixProducts=calixProducts, calixNetworks=calixNetworks, calixModules=calixModules, calixManagement=calixManagement)
