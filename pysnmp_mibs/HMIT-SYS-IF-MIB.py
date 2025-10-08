#
# PySNMP MIB module HMIT-SYS-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HMIT-SYS-IF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmITSystem, = mibBuilder.importSymbols("HMIT-SMI", "hmITSystem")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HMIT-SYS-IF-MIB", hmITSysIfEntry=hmITSysIfEntry, hmITSysIfTable=hmITSysIfTable, hmITSysIfIndex=hmITSysIfIndex, hmITSysIfReliability=hmITSysIfReliability, PYSNMP_MODULE_ID=hmITSysIfMIB, hmITSysIfMIB=hmITSysIfMIB, hmITSysIfName=hmITSysIfName)
