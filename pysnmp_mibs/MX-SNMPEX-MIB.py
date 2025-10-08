#
# PySNMP MIB module MX-SNMPEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-SNMPEX-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:02 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
snmpMIBObjects, = mibBuilder.importSymbols("MX-SNMP-MIB", "snmpMIBObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpExMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 100))
snmpExMIB.setRevisions(('1904-11-15 00:00',))
if mibBuilder.loadTexts: snmpExMIB.setLastUpdated('0411150000Z')
if mibBuilder.loadTexts: snmpExMIB.setOrganization(' Mediatrix Telecom, Inc. ')
snmpExMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 100, 1))
access = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 100, 1, 100))
lastResult = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 100, 1, 100, 100), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastResult.setStatus('current')
command = MibScalar((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 900, 1, 100, 1, 100, 200), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: command.setStatus('current')
mibBuilder.exportSymbols("MX-SNMPEX-MIB", access=access, snmpExMIBObjects=snmpExMIBObjects, command=command, snmpExMIB=snmpExMIB, lastResult=lastResult, PYSNMP_MODULE_ID=snmpExMIB)
