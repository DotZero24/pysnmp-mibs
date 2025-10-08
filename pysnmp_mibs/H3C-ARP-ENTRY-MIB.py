#
# PySNMP MIB module H3C-ARP-ENTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-ARP-ENTRY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cARPEntry = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 168))
h3cARPEntry.setRevisions(('2017-03-14 00:00',))
if mibBuilder.loadTexts: h3cARPEntry.setLastUpdated('201703140000Z')
if mibBuilder.loadTexts: h3cARPEntry.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cARPEntryCountObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 168, 1))
h3cARPEntryOpenFlowCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 168, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cARPEntryOpenFlowCount.setStatus('current')
mibBuilder.exportSymbols("H3C-ARP-ENTRY-MIB", PYSNMP_MODULE_ID=h3cARPEntry, h3cARPEntryOpenFlowCount=h3cARPEntryOpenFlowCount, h3cARPEntryCountObjects=h3cARPEntryCountObjects, h3cARPEntry=h3cARPEntry)
