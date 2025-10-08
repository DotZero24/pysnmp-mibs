#
# PySNMP MIB module ELECTROLINE-COMMON-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-COMMON-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
electrolineHardwareProducts, = mibBuilder.importSymbols("ELECTROLINE-GLOBAL-REG", "electrolineHardwareProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELECTROLINE-COMMON-ROOT-MIB", commonConfiguration=commonConfiguration, PYSNMP_MODULE_ID=electrolineCommon, commonStatus=commonStatus, commonPrivate=commonPrivate, commonInventory=commonInventory, electrolineCommon=electrolineCommon)
