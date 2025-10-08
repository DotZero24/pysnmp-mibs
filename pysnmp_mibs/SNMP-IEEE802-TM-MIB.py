#
# PySNMP MIB module SNMP-IEEE802-TM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/SNMP-IEEE802-TM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, snmpModules, snmpDomains, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "snmpModules", "snmpDomains", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpIeee802TmMib = ModuleIdentity((1, 3, 6, 1, 6, 3, 21))
snmpIeee802TmMib.setRevisions(('2006-11-21 00:00',))
if mibBuilder.loadTexts: snmpIeee802TmMib.setLastUpdated('200611210000Z')
if mibBuilder.loadTexts: snmpIeee802TmMib.setOrganization('IETF Operations and Management Area')
snmpIeee802Domain = ObjectIdentity((1, 3, 6, 1, 6, 1, 6))
if mibBuilder.loadTexts: snmpIeee802Domain.setStatus('current')
mibBuilder.exportSymbols("SNMP-IEEE802-TM-MIB", snmpIeee802Domain=snmpIeee802Domain, PYSNMP_MODULE_ID=snmpIeee802TmMib, snmpIeee802TmMib=snmpIeee802TmMib)
