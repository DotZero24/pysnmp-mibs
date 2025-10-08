#
# PySNMP MIB module SNMP-USM-HMAC-SHA2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SNMP-USM-HMAC-SHA2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
snmpAuthProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpAuthProtocols")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SNMP-USM-HMAC-SHA2-MIB", usmHMAC128SHA224AuthProtocol=usmHMAC128SHA224AuthProtocol, snmpUsmHmacSha2MIB=snmpUsmHmacSha2MIB, usmHMAC192SHA256AuthProtocol=usmHMAC192SHA256AuthProtocol, PYSNMP_MODULE_ID=snmpUsmHmacSha2MIB, usmHMAC384SHA512AuthProtocol=usmHMAC384SHA512AuthProtocol, usmHMAC256SHA384AuthProtocol=usmHMAC256SHA384AuthProtocol)
