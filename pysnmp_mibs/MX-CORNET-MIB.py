#
# PySNMP MIB module MX-CORNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-CORNET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixIpTelephonySignaling, ipAddressConfig, ipAddressStatus = mibBuilder.importSymbols("MX-SMI", "mediatrixIpTelephonySignaling", "ipAddressConfig", "ipAddressStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
corNet = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 20, 40))
if mibBuilder.loadTexts: corNet.setStatus('current')
ipAddressStatusCorNet = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 1, 130))
ipAddressConfigCorNet = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 1, 130))
ipAddressConfigCorNetStatic = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10))
mibBuilder.exportSymbols("MX-CORNET-MIB", ipAddressConfigCorNetStatic=ipAddressConfigCorNetStatic, corNet=corNet, ipAddressStatusCorNet=ipAddressStatusCorNet, ipAddressConfigCorNet=ipAddressConfigCorNet)
