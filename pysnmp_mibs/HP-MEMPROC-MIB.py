#
# PySNMP MIB module HP-MEMPROC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-MEMPROC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpProcurveCommon, = mibBuilder.importSymbols("HP-BASE-MIB", "hpProcurveCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Opaque, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Opaque", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("HP-MEMPROC-MIB", PYSNMP_MODULE_ID=hpMemprocMIB, hpmpMemEntry=hpmpMemEntry, hpMemprocMIBCompliance1=hpMemprocMIBCompliance1, hpmpMemIndex=hpmpMemIndex, hpmpCPUIndex=hpmpCPUIndex, hpmpMemTable=hpmpMemTable, hpmpCPULoad15min=hpmpCPULoad15min, hpmpCPUTable=hpmpCPUTable, Float=Float, hpmpCPULoad1min=hpmpCPULoad1min, hpmpMemInUse=hpmpMemInUse, hpMemprocMIBObjects=hpMemprocMIBObjects, hpmpMemDescr=hpmpMemDescr, hpmpCPULoad5min=hpmpCPULoad5min, hpmpMemory=hpmpMemory, hpmpGroups=hpmpGroups, hpmpMemoryGroup=hpmpMemoryGroup, hpMemprocMIBConformance=hpMemprocMIBConformance, hpmpMemTotal=hpmpMemTotal, hpmpMemPctInUse=hpmpMemPctInUse, hpmpCPUGroup=hpmpCPUGroup, hpmpCompliances=hpmpCompliances, hpmpCPUEntry=hpmpCPUEntry, hpMemprocMIB=hpMemprocMIB, hpMemprocNotificationsPrefix=hpMemprocNotificationsPrefix, hpmpCPU=hpmpCPU, hpMemprocNotifications=hpMemprocNotifications, hpmpCPUPctBusy=hpmpCPUPctBusy)
