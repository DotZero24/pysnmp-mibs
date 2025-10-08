#
# PySNMP MIB module NET-SNMP-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/net-snmp/NET-SNMP-MONITOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netSnmpObjects, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpModuleIDs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 3))
netSnmpMonitorMIB.setRevisions(('2002-02-09 00:00',))
if mibBuilder.loadTexts: netSnmpMonitorMIB.setLastUpdated('200202090000Z')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setOrganization('www.net-snmp.org')
nsProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 21))
nsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 22))
nsFile = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 23))
nsLog = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 24))
mibBuilder.exportSymbols("NET-SNMP-MONITOR-MIB", nsLog=nsLog, nsDisk=nsDisk, nsProcess=nsProcess, netSnmpMonitorMIB=netSnmpMonitorMIB, nsFile=nsFile, PYSNMP_MODULE_ID=netSnmpMonitorMIB)
