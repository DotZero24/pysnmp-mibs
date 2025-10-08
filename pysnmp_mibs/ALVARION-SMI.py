#
# PySNMP MIB module ALVARION-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alvarion/ALVARION-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionWireless = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10))
if mibBuilder.loadTexts: alvarionWireless.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionWireless.setOrganization('Alvarion Ltd.')
alvarionProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1))
if mibBuilder.loadTexts: alvarionProducts.setStatus('current')
alvarionExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 3))
if mibBuilder.loadTexts: alvarionExperiment.setStatus('current')
alvarionModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 4))
if mibBuilder.loadTexts: alvarionModules.setStatus('current')
alvarionMgmtV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5))
if mibBuilder.loadTexts: alvarionMgmtV2.setStatus('current')
variation = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 7))
if mibBuilder.loadTexts: variation.setStatus('current')
mibBuilder.exportSymbols("ALVARION-SMI", alvarionWireless=alvarionWireless, alvarionProducts=alvarionProducts, alvarionMgmtV2=alvarionMgmtV2, variation=variation, alvarionModules=alvarionModules, alvarionExperiment=alvarionExperiment, PYSNMP_MODULE_ID=alvarionWireless)
