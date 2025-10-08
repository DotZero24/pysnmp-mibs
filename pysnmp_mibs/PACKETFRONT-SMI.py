#
# PySNMP MIB module PACKETFRONT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/packetfront/PACKETFRONT-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
packetfront = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303))
packetfront.setRevisions(('2009-03-23 10:39', '2008-01-17 14:05', '2007-05-11 12:28',))
if mibBuilder.loadTexts: packetfront.setLastUpdated('200903231039Z')
if mibBuilder.loadTexts: packetfront.setOrganization('PacketFront Systems AB')
pfProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1))
if mibBuilder.loadTexts: pfProduct.setStatus('current')
pfConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2))
if mibBuilder.loadTexts: pfConfig.setStatus('current')
ipdConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2, 1))
if mibBuilder.loadTexts: ipdConfig.setStatus('current')
pfExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 3))
if mibBuilder.loadTexts: pfExperiment.setStatus('current')
pfMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 4))
if mibBuilder.loadTexts: pfMgmt.setStatus('current')
pfModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 5))
if mibBuilder.loadTexts: pfModules.setStatus('current')
mibBuilder.exportSymbols("PACKETFRONT-SMI", packetfront=packetfront, pfModules=pfModules, pfProduct=pfProduct, pfConfig=pfConfig, pfMgmt=pfMgmt, pfExperiment=pfExperiment, PYSNMP_MODULE_ID=packetfront, ipdConfig=ipdConfig)
