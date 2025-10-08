#
# PySNMP MIB module MX-CORNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-CORNET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ipAddressStatus, mediatrixIpTelephonySignaling, ipAddressConfig = mibBuilder.importSymbols("MX-SMI", "ipAddressStatus", "mediatrixIpTelephonySignaling", "ipAddressConfig")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
corNet = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 20, 40))
if mibBuilder.loadTexts: corNet.setStatus('current')
ipAddressStatusCorNet = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 1, 130))
ipAddressConfigCorNet = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 1, 130))
ipAddressConfigCorNetStatic = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 1, 130, 10))
mibBuilder.exportSymbols("MX-CORNET-MIB", ipAddressStatusCorNet=ipAddressStatusCorNet, ipAddressConfigCorNetStatic=ipAddressConfigCorNetStatic, corNet=corNet, ipAddressConfigCorNet=ipAddressConfigCorNet)
