#
# PySNMP MIB module MX-H323-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-H323-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixIpTelephonySignaling, ipAddressConfig, ipAddressStatus = mibBuilder.importSymbols("MX-SMI", "mediatrixIpTelephonySignaling", "ipAddressConfig", "ipAddressStatus")
MxIpConfigSource, MxIpSelectConfigSource = mibBuilder.importSymbols("MX-TC", "MxIpConfigSource", "MxIpSelectConfigSource")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-H323-MIB", ipAddressConfigH323Dhcp=ipAddressConfigH323Dhcp, ipAddressStatusH323=ipAddressStatusH323, ipAddressConfigH323Static=ipAddressConfigH323Static, ipAddressConfigH323=ipAddressConfigH323, h323=h323, h323ConfigSource=h323ConfigSource, h323SelectConfigSource=h323SelectConfigSource)
