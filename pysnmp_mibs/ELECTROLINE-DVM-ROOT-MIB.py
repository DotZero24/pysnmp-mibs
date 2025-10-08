#
# PySNMP MIB module ELECTROLINE-DVM-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DVM-ROOT-MIB
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
class ModulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", -1), ("qam16", 0), ("qam64", 1), ("qam256", 2), ("qam1024", 3), ("qam32", 4), ("qam128", 5), ("qpsk", 6))

electrolineDVM = ModuleIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3))
electrolineDVM.setRevisions(('2003-03-20 00:00',))
if mibBuilder.loadTexts: electrolineDVM.setLastUpdated('201005180000Z')
if mibBuilder.loadTexts: electrolineDVM.setOrganization('Electroline Equipment Inc')
dvmInventory = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1))
if mibBuilder.loadTexts: dvmInventory.setStatus('current')
dvmConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2))
if mibBuilder.loadTexts: dvmConfiguration.setStatus('current')
dvmStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3))
if mibBuilder.loadTexts: dvmStatus.setStatus('current')
dvmPrivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4))
if mibBuilder.loadTexts: dvmPrivate.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-DVM-ROOT-MIB", dvmInventory=dvmInventory, PYSNMP_MODULE_ID=electrolineDVM, electrolineDVM=electrolineDVM, dvmStatus=dvmStatus, ModulationType=ModulationType, dvmPrivate=dvmPrivate, dvmConfiguration=dvmConfiguration)
