#
# PySNMP MIB module SNMP-USM-HMAC-SHA2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/SNMP-USM-HMAC-SHA2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snmpAuthProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpAuthProtocols")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpUsmHmacSha2MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 235))
snmpUsmHmacSha2MIB.setRevisions(('2016-04-18 00:00', '2015-10-14 00:00',))
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setLastUpdated('201604180000Z')
if mibBuilder.loadTexts: snmpUsmHmacSha2MIB.setOrganization('SNMPv3 Working Group')
usmHMAC128SHA224AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 4))
if mibBuilder.loadTexts: usmHMAC128SHA224AuthProtocol.setStatus('current')
usmHMAC192SHA256AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 5))
if mibBuilder.loadTexts: usmHMAC192SHA256AuthProtocol.setStatus('current')
usmHMAC256SHA384AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 6))
if mibBuilder.loadTexts: usmHMAC256SHA384AuthProtocol.setStatus('current')
usmHMAC384SHA512AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 7))
if mibBuilder.loadTexts: usmHMAC384SHA512AuthProtocol.setStatus('current')
mibBuilder.exportSymbols("SNMP-USM-HMAC-SHA2-MIB", usmHMAC384SHA512AuthProtocol=usmHMAC384SHA512AuthProtocol, PYSNMP_MODULE_ID=snmpUsmHmacSha2MIB, snmpUsmHmacSha2MIB=snmpUsmHmacSha2MIB, usmHMAC256SHA384AuthProtocol=usmHMAC256SHA384AuthProtocol, usmHMAC128SHA224AuthProtocol=usmHMAC128SHA224AuthProtocol, usmHMAC192SHA256AuthProtocol=usmHMAC192SHA256AuthProtocol)
