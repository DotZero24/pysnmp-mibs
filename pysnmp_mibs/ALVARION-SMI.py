#
# PySNMP MIB module ALVARION-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alvarion/ALVARION-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ALVARION-SMI", variation=variation, alvarionExperiment=alvarionExperiment, alvarionProducts=alvarionProducts, alvarionModules=alvarionModules, PYSNMP_MODULE_ID=alvarionWireless, alvarionWireless=alvarionWireless, alvarionMgmtV2=alvarionMgmtV2)
