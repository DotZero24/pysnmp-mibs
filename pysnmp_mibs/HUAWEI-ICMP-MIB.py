#
# PySNMP MIB module HUAWEI-ICMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/HUAWEI-ICMP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hwLocal, hwInternetProtocol, huawei = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "hwLocal", "hwInternetProtocol", "huawei")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HUAWEI-ICMP-MIB", icmpOutOldIcmp=icmpOutOldIcmp, icmpInBadCode=icmpInBadCode, icmpInBadLen=icmpInBadLen, rIcmp=rIcmp, icmpInTooShort=icmpInTooShort, icmpOutShort=icmpOutShort, icmpInChecksum=icmpInChecksum)
