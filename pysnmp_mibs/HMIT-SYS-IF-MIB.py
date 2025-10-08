#
# PySNMP MIB module HMIT-SYS-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HMIT-SYS-IF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmITSystem, = mibBuilder.importSymbols("HMIT-SMI", "hmITSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmITSysIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11))
hmITSysIfMIB.setRevisions(('2010-01-08 17:00',))
if mibBuilder.loadTexts: hmITSysIfMIB.setLastUpdated('201001081700Z')
if mibBuilder.loadTexts: hmITSysIfMIB.setOrganization('Belden Singapore Pte Ltd.')
hmITSysIfTable = MibTable((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1), )
if mibBuilder.loadTexts: hmITSysIfTable.setStatus('current')
hmITSysIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1), ).setIndexNames((0, "HMIT-SYS-IF-MIB", "hmITSysIfIndex"))
if mibBuilder.loadTexts: hmITSysIfEntry.setStatus('current')
hmITSysIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hmITSysIfIndex.setStatus('current')
hmITSysIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 39))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmITSysIfName.setStatus('current')
hmITSysIfReliability = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmITSysIfReliability.setStatus('current')
mibBuilder.exportSymbols("HMIT-SYS-IF-MIB", hmITSysIfEntry=hmITSysIfEntry, PYSNMP_MODULE_ID=hmITSysIfMIB, hmITSysIfName=hmITSysIfName, hmITSysIfTable=hmITSysIfTable, hmITSysIfIndex=hmITSysIfIndex, hmITSysIfMIB=hmITSysIfMIB, hmITSysIfReliability=hmITSysIfReliability)
