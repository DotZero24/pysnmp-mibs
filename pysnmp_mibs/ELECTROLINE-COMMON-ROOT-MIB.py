#
# PySNMP MIB module ELECTROLINE-COMMON-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-COMMON-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
electrolineHardwareProducts, = mibBuilder.importSymbols("ELECTROLINE-GLOBAL-REG", "electrolineHardwareProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
electrolineCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4))
electrolineCommon.setRevisions(('2014-01-14 00:00',))
if mibBuilder.loadTexts: electrolineCommon.setLastUpdated('201401140000Z')
if mibBuilder.loadTexts: electrolineCommon.setOrganization('Electroline Equipment Inc')
commonInventory = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1))
if mibBuilder.loadTexts: commonInventory.setStatus('current')
commonConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2))
if mibBuilder.loadTexts: commonConfiguration.setStatus('current')
commonStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 3))
if mibBuilder.loadTexts: commonStatus.setStatus('current')
commonPrivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4))
if mibBuilder.loadTexts: commonPrivate.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-COMMON-ROOT-MIB", commonConfiguration=commonConfiguration, commonPrivate=commonPrivate, commonInventory=commonInventory, electrolineCommon=electrolineCommon, commonStatus=commonStatus, PYSNMP_MODULE_ID=electrolineCommon)
