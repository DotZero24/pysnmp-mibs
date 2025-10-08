#
# PySNMP MIB module NET-SNMP-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/net-snmp/NET-SNMP-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netSnmpObjects, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpModuleIDs")
Float, = mibBuilder.importSymbols("NET-SNMP-TC", "Float")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netSnmpSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 4))
netSnmpSystemMIB.setRevisions(('2002-02-09 00:00',))
if mibBuilder.loadTexts: netSnmpSystemMIB.setLastUpdated('200202090000Z')
if mibBuilder.loadTexts: netSnmpSystemMIB.setOrganization('www.net-snmp.org')
nsMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 31))
nsSwap = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 32))
nsCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 33))
nsLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 34))
nsDiskIO = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 35))
mibBuilder.exportSymbols("NET-SNMP-SYSTEM-MIB", nsCPU=nsCPU, nsLoad=nsLoad, PYSNMP_MODULE_ID=netSnmpSystemMIB, netSnmpSystemMIB=netSnmpSystemMIB, nsDiskIO=nsDiskIO, nsMemory=nsMemory, nsSwap=nsSwap)
