#
# PySNMP MIB module CALIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/calix/CALIX-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 09:59:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CALIX-SMI", calixManagement=calixManagement, PYSNMP_MODULE_ID=calixNetworks, calixModules=calixModules, calixProducts=calixProducts, calixRegistrations=calixRegistrations, calixNetworks=calixNetworks)
