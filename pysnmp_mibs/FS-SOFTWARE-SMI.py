#
# PySNMP MIB module FS-SOFTWARE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-SOFTWARE-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
products, = mibBuilder.importSymbols("FS-SMI", "products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
software = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 7))
softwareMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 7, 1))
softwareMib.setRevisions(('2010-05-25 00:00',))
if mibBuilder.loadTexts: softwareMib.setLastUpdated('201408190000Z')
if mibBuilder.loadTexts: softwareMib.setOrganization('FS.COM Inc..')
fsSoftwareProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 7, 1, 1))
if mibBuilder.loadTexts: fsSoftwareProducts.setStatus('current')
mibBuilder.exportSymbols("FS-SOFTWARE-SMI", softwareMib=softwareMib, fsSoftwareProducts=fsSoftwareProducts, software=software, PYSNMP_MODULE_ID=softwareMib)
