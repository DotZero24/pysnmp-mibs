#
# PySNMP MIB module H3C-ARP-ENTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-ARP-ENTRY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cARPEntry = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 168))
h3cARPEntry.setRevisions(('2017-03-14 00:00',))
if mibBuilder.loadTexts: h3cARPEntry.setLastUpdated('201703140000Z')
if mibBuilder.loadTexts: h3cARPEntry.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cARPEntryCountObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 168, 1))
h3cARPEntryOpenFlowCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 168, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cARPEntryOpenFlowCount.setStatus('current')
mibBuilder.exportSymbols("H3C-ARP-ENTRY-MIB", h3cARPEntryCountObjects=h3cARPEntryCountObjects, h3cARPEntry=h3cARPEntry, h3cARPEntryOpenFlowCount=h3cARPEntryOpenFlowCount, PYSNMP_MODULE_ID=h3cARPEntry)
