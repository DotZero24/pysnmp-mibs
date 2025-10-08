#
# PySNMP MIB module IONLINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/IONLINE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, snmpModules, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "snmpModules", "Gauge32")
TruthValue, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("IONLINE-MIB", ionline=ionline, ioPoolTable=ioPoolTable, ioPoolORId=ioPoolORId, ioPoolORDescr=ioPoolORDescr, ioPoolEntry=ioPoolEntry, PYSNMP_MODULE_ID=elite, elite=elite, ioPoolUsage=ioPoolUsage, ioPoolStatus=ioPoolStatus)
