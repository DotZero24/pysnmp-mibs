#
# PySNMP MIB module IONLINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/IONLINE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "DateAndTime", "TextualConvention")
elite = ModuleIdentity((1, 3, 6, 1, 4, 1, 21068))
if mibBuilder.loadTexts: elite.setLastUpdated('201208220000Z')
if mibBuilder.loadTexts: elite.setOrganization('E Technologies')
ionline = ObjectIdentity((1, 3, 6, 1, 4, 1, 21068, 1))
if mibBuilder.loadTexts: ionline.setStatus('current')
ioPoolStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 21068, 1, 3))
ioPoolUsage = MibScalar((1, 3, 6, 1, 4, 1, 21068, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ioPoolUsage.setStatus('current')
ioPoolTable = MibTable((1, 3, 6, 1, 4, 1, 21068, 2), )
if mibBuilder.loadTexts: ioPoolTable.setStatus('current')
ioPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21068, 2, 1), ).setIndexNames((0, "IONLINE-MIB", "sysORIndex"))
if mibBuilder.loadTexts: ioPoolEntry.setStatus('current')
ioPoolORId = MibTableColumn((1, 3, 6, 1, 4, 1, 21068, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ioPoolORId.setStatus('current')
ioPoolORDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 21068, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ioPoolORDescr.setStatus('current')
mibBuilder.exportSymbols("IONLINE-MIB", ioPoolStatus=ioPoolStatus, elite=elite, ioPoolORDescr=ioPoolORDescr, ioPoolORId=ioPoolORId, ioPoolUsage=ioPoolUsage, PYSNMP_MODULE_ID=elite, ioPoolEntry=ioPoolEntry, ioPoolTable=ioPoolTable, ionline=ionline)
