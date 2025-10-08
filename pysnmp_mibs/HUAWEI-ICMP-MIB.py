#
# PySNMP MIB module HUAWEI-ICMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/HUAWEI-ICMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
huawei, hwInternetProtocol, hwLocal = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "huawei", "hwInternetProtocol", "hwLocal")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2))
icmpInBadCode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInBadCode.setStatus('mandatory')
icmpInBadLen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInBadLen.setStatus('mandatory')
icmpInChecksum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInChecksum.setStatus('mandatory')
icmpInTooShort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInTooShort.setStatus('mandatory')
icmpOutOldIcmp = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutOldIcmp.setStatus('mandatory')
icmpOutShort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 1, 3, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutShort.setStatus('mandatory')
mibBuilder.exportSymbols("HUAWEI-ICMP-MIB", icmpOutShort=icmpOutShort, rIcmp=rIcmp, icmpInChecksum=icmpInChecksum, icmpOutOldIcmp=icmpOutOldIcmp, icmpInTooShort=icmpInTooShort, icmpInBadCode=icmpInBadCode, icmpInBadLen=icmpInBadLen)
