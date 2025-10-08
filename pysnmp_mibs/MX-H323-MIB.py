#
# PySNMP MIB module MX-H323-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-H323-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ipAddressStatus, mediatrixIpTelephonySignaling, ipAddressConfig = mibBuilder.importSymbols("MX-SMI", "ipAddressStatus", "mediatrixIpTelephonySignaling", "ipAddressConfig")
MxIpConfigSource, MxIpSelectConfigSource = mibBuilder.importSymbols("MX-TC", "MxIpConfigSource", "MxIpSelectConfigSource")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h323 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 20, 30))
if mibBuilder.loadTexts: h323.setStatus('current')
ipAddressStatusH323 = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 10, 1, 90))
ipAddressConfigH323 = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 1, 90))
ipAddressConfigH323Static = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 10))
ipAddressConfigH323Dhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 15))
h323ConfigSource = MibScalar((1, 3, 6, 1, 4, 1, 4935, 10, 1, 90, 5), MxIpConfigSource().clone('dhcp')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h323ConfigSource.setStatus('current')
h323SelectConfigSource = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 1, 90, 5), MxIpSelectConfigSource().clone('dhcp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h323SelectConfigSource.setStatus('current')
mibBuilder.exportSymbols("MX-H323-MIB", ipAddressConfigH323=ipAddressConfigH323, h323ConfigSource=h323ConfigSource, ipAddressConfigH323Dhcp=ipAddressConfigH323Dhcp, h323SelectConfigSource=h323SelectConfigSource, h323=h323, ipAddressConfigH323Static=ipAddressConfigH323Static, ipAddressStatusH323=ipAddressStatusH323)
