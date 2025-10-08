#
# PySNMP MIB module NET-SNMP-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/net-snmp/NET-SNMP-MONITOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netSnmpObjects, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpModuleIDs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netSnmpMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 3))
netSnmpMonitorMIB.setRevisions(('2002-02-09 00:00',))
if mibBuilder.loadTexts: netSnmpMonitorMIB.setLastUpdated('200202090000Z')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setOrganization('www.net-snmp.org')
nsProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 21))
nsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 22))
nsFile = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 23))
nsLog = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 24))
mibBuilder.exportSymbols("NET-SNMP-MONITOR-MIB", nsDisk=nsDisk, nsProcess=nsProcess, PYSNMP_MODULE_ID=netSnmpMonitorMIB, netSnmpMonitorMIB=netSnmpMonitorMIB, nsFile=nsFile, nsLog=nsLog)
