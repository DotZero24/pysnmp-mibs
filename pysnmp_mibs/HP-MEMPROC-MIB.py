#
# PySNMP MIB module HP-MEMPROC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-MEMPROC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpProcurveCommon, = mibBuilder.importSymbols("HP-BASE-MIB", "hpProcurveCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Opaque")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
hpMemprocMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5))
hpMemprocMIB.setRevisions(('2005-02-01 14:55',))
if mibBuilder.loadTexts: hpMemprocMIB.setLastUpdated('200502011455Z')
if mibBuilder.loadTexts: hpMemprocMIB.setOrganization('Hewlett Packard Company, ProCurve Networking Business')
hpMemprocMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1))
hpMemprocNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 2))
hpMemprocMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3))
hpmpCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1))
hpmpMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2))
class Float(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

hpmpCPUTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1), )
if mibBuilder.loadTexts: hpmpCPUTable.setStatus('current')
hpmpCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1), ).setIndexNames((0, "HP-MEMPROC-MIB", "hpmpCPUIndex"))
if mibBuilder.loadTexts: hpmpCPUEntry.setStatus('current')
hpmpCPUIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: hpmpCPUIndex.setStatus('current')
hpmpCPULoad1min = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpCPULoad1min.setStatus('current')
hpmpCPULoad5min = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpCPULoad5min.setStatus('current')
hpmpCPULoad15min = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpCPULoad15min.setStatus('current')
hpmpCPUPctBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 1, 1, 1, 5), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpCPUPctBusy.setStatus('current')
hpmpMemTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1), )
if mibBuilder.loadTexts: hpmpMemTable.setStatus('current')
hpmpMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1), ).setIndexNames((0, "HP-MEMPROC-MIB", "hpmpMemIndex"))
if mibBuilder.loadTexts: hpmpMemEntry.setStatus('current')
hpmpMemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: hpmpMemIndex.setStatus('current')
hpmpMemDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpMemDescr.setStatus('current')
hpmpMemInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 3), Unsigned32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpMemInUse.setStatus('current')
hpmpMemTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 4), Unsigned32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpMemTotal.setStatus('current')
hpmpMemPctInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 1, 2, 1, 1, 5), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpmpMemPctInUse.setStatus('current')
hpMemprocNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 2, 0))
hpmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 1))
hpmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 2))
hpMemprocMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 1, 1)).setObjects(("HP-MEMPROC-MIB", "hpmpCPUGroup"), ("HP-MEMPROC-MIB", "hpmpMemoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpMemprocMIBCompliance1 = hpMemprocMIBCompliance1.setStatus('current')
hpmpCPUGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 2, 1)).setObjects(("HP-MEMPROC-MIB", "hpmpCPULoad1min"), ("HP-MEMPROC-MIB", "hpmpCPULoad5min"), ("HP-MEMPROC-MIB", "hpmpCPULoad15min"), ("HP-MEMPROC-MIB", "hpmpCPUPctBusy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpmpCPUGroup = hpmpCPUGroup.setStatus('current')
hpmpMemoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1, 5, 3, 2, 2)).setObjects(("HP-MEMPROC-MIB", "hpmpMemDescr"), ("HP-MEMPROC-MIB", "hpmpMemInUse"), ("HP-MEMPROC-MIB", "hpmpMemTotal"), ("HP-MEMPROC-MIB", "hpmpMemPctInUse"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpmpMemoryGroup = hpmpMemoryGroup.setStatus('current')
mibBuilder.exportSymbols("HP-MEMPROC-MIB", hpmpCompliances=hpmpCompliances, hpmpCPULoad5min=hpmpCPULoad5min, hpmpMemoryGroup=hpmpMemoryGroup, hpmpCPUTable=hpmpCPUTable, hpmpCPUEntry=hpmpCPUEntry, hpMemprocMIBObjects=hpMemprocMIBObjects, hpmpMemory=hpmpMemory, hpMemprocMIBConformance=hpMemprocMIBConformance, hpmpGroups=hpmpGroups, PYSNMP_MODULE_ID=hpMemprocMIB, hpmpCPUPctBusy=hpmpCPUPctBusy, hpmpMemEntry=hpmpMemEntry, hpmpMemInUse=hpmpMemInUse, hpMemprocNotificationsPrefix=hpMemprocNotificationsPrefix, hpmpMemPctInUse=hpmpMemPctInUse, hpmpMemTable=hpmpMemTable, hpmpCPULoad15min=hpmpCPULoad15min, hpmpMemDescr=hpmpMemDescr, hpMemprocMIB=hpMemprocMIB, hpmpCPU=hpmpCPU, hpmpMemIndex=hpmpMemIndex, hpmpCPULoad1min=hpmpCPULoad1min, hpmpCPUGroup=hpmpCPUGroup, hpmpCPUIndex=hpmpCPUIndex, hpmpMemTotal=hpmpMemTotal, hpMemprocNotifications=hpMemprocNotifications, Float=Float, hpMemprocMIBCompliance1=hpMemprocMIBCompliance1)
