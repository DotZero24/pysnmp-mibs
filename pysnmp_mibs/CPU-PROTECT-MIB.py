#
# PySNMP MIB module CPU-PROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/CPU-PROTECT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("CPU-PROTECT-MIB", swCPUProtectMIB=swCPUProtectMIB, swCPUProtectGlobalMgmt=swCPUProtectGlobalMgmt, PYSNMP_MODULE_ID=swCPUProtectMIB, swCPUProtectProtocolTable=swCPUProtectProtocolTable, swCPUProtectState=swCPUProtectState, swCPUProtectProtocolType=swCPUProtectProtocolType, swCPUProtectProtocolEntry=swCPUProtectProtocolEntry, swCPUProtectProtocolRate=swCPUProtectProtocolRate)
