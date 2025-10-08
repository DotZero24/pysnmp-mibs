#
# PySNMP MIB module CPU-PROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/CPU-PROTECT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
swCPUProtectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 106))
if mibBuilder.loadTexts: swCPUProtectMIB.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: swCPUProtectMIB.setOrganization('D-Link Corp.')
swCPUProtectGlobalMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 106, 1))
swCPUProtectState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 106, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCPUProtectState.setStatus('current')
swCPUProtectProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 106, 2), )
if mibBuilder.loadTexts: swCPUProtectProtocolTable.setStatus('current')
swCPUProtectProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 106, 2, 1), ).setIndexNames((0, "CPU-PROTECT-MIB", "swCPUProtectProtocolType"))
if mibBuilder.loadTexts: swCPUProtectProtocolEntry.setStatus('current')
swCPUProtectProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 106, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("arp", 1), ("bpdu", 2), ("icmp", 3), ("igmp", 4), ("snmp", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swCPUProtectProtocolType.setStatus('current')
swCPUProtectProtocolRate = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 106, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCPUProtectProtocolRate.setStatus('current')
mibBuilder.exportSymbols("CPU-PROTECT-MIB", swCPUProtectProtocolRate=swCPUProtectProtocolRate, swCPUProtectState=swCPUProtectState, swCPUProtectProtocolType=swCPUProtectProtocolType, swCPUProtectGlobalMgmt=swCPUProtectGlobalMgmt, swCPUProtectProtocolTable=swCPUProtectProtocolTable, swCPUProtectMIB=swCPUProtectMIB, PYSNMP_MODULE_ID=swCPUProtectMIB, swCPUProtectProtocolEntry=swCPUProtectProtocolEntry)
