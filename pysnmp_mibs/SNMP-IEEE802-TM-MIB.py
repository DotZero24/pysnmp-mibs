#
# PySNMP MIB module SNMP-IEEE802-TM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SNMP-IEEE802-TM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, snmpDomains, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, iso, Counter32, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "snmpDomains", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "iso", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpIeee802TmMib = ModuleIdentity((1, 3, 6, 1, 6, 3, 21))
snmpIeee802TmMib.setRevisions(('2006-11-21 00:00',))
if mibBuilder.loadTexts: snmpIeee802TmMib.setLastUpdated('200611210000Z')
if mibBuilder.loadTexts: snmpIeee802TmMib.setOrganization('IETF Operations and Management Area')
snmpIeee802Domain = ObjectIdentity((1, 3, 6, 1, 6, 1, 6))
if mibBuilder.loadTexts: snmpIeee802Domain.setStatus('current')
mibBuilder.exportSymbols("SNMP-IEEE802-TM-MIB", PYSNMP_MODULE_ID=snmpIeee802TmMib, snmpIeee802Domain=snmpIeee802Domain, snmpIeee802TmMib=snmpIeee802TmMib)
