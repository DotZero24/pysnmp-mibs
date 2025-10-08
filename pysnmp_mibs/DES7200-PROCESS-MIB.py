#
# PySNMP MIB module DES7200-PROCESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-PROCESS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
myProcessMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36))
myProcessMIB.setRevisions(('2003-10-14 00:00',))
if mibBuilder.loadTexts: myProcessMIB.setLastUpdated('200310140000Z')
if mibBuilder.loadTexts: myProcessMIB.setOrganization('D-Link Crop.')
class Percent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

myCPUMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1))
myCpuGeneralMibsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1))
myCPUUtilization5Sec = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 1), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization5Sec.setStatus('current')
myCPUUtilization1Min = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 2), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization1Min.setStatus('current')
myCPUUtilization5Min = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myCPUUtilization5Min.setStatus('current')
myCPUUtilizationWarning = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 4), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCPUUtilizationWarning.setStatus('current')
myCPUUtilizationCritical = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 1, 5), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myCPUUtilizationCritical.setStatus('current')
myNodeCPUTotalTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2), )
if mibBuilder.loadTexts: myNodeCPUTotalTable.setStatus('current')
myNodeCPUTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1), ).setIndexNames((0, "DES7200-PROCESS-MIB", "myNodeCPUTotalIndex"))
if mibBuilder.loadTexts: myNodeCPUTotalEntry.setStatus('current')
myNodeCPUTotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotalIndex.setStatus('current')
myNodeCPUTotalName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotalName.setStatus('current')
myNodeCPUTotal5sec = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal5sec.setStatus('current')
myNodeCPUTotal1min = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 4), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal1min.setStatus('current')
myNodeCPUTotal5min = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 5), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myNodeCPUTotal5min.setStatus('current')
myNodeCPUTotalWarning = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 6), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeCPUTotalWarning.setStatus('current')
myNodeCPUTotalCritical = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 1, 2, 1, 7), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myNodeCPUTotalCritical.setStatus('current')
myProcessMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2))
myProcessMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1))
myProcessMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2))
myProcessMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 1, 1)).setObjects(("DES7200-PROCESS-MIB", "myCPUUtilizationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myProcessMIBCompliance = myProcessMIBCompliance.setStatus('current')
myCPUUtilizationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 1)).setObjects(("DES7200-PROCESS-MIB", "myCPUUtilization5Sec"), ("DES7200-PROCESS-MIB", "myCPUUtilization1Min"), ("DES7200-PROCESS-MIB", "myCPUUtilization5Min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myCPUUtilizationMIBGroup = myCPUUtilizationMIBGroup.setStatus('current')
myNodeCPUTotalGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 36, 2, 2, 2)).setObjects(("DES7200-PROCESS-MIB", "myNodeCPUTotalIndex"), ("DES7200-PROCESS-MIB", "myNodeCPUTotalName"), ("DES7200-PROCESS-MIB", "myNodeCPUTotal5sec"), ("DES7200-PROCESS-MIB", "myNodeCPUTotal1min"), ("DES7200-PROCESS-MIB", "myNodeCPUTotal5min"), ("DES7200-PROCESS-MIB", "myNodeCPUTotalWarning"), ("DES7200-PROCESS-MIB", "myNodeCPUTotalCritical"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNodeCPUTotalGroups = myNodeCPUTotalGroups.setStatus('current')
mibBuilder.exportSymbols("DES7200-PROCESS-MIB", myNodeCPUTotalWarning=myNodeCPUTotalWarning, myProcessMIBGroups=myProcessMIBGroups, myNodeCPUTotal5min=myNodeCPUTotal5min, PYSNMP_MODULE_ID=myProcessMIB, myNodeCPUTotal1min=myNodeCPUTotal1min, myNodeCPUTotalName=myNodeCPUTotalName, myCpuGeneralMibsGroup=myCpuGeneralMibsGroup, Percent=Percent, myCPUUtilizationMIBGroup=myCPUUtilizationMIBGroup, myCPUMIBObjects=myCPUMIBObjects, myNodeCPUTotalIndex=myNodeCPUTotalIndex, myCPUUtilizationWarning=myCPUUtilizationWarning, myNodeCPUTotalEntry=myNodeCPUTotalEntry, myProcessMIBCompliances=myProcessMIBCompliances, myProcessMIB=myProcessMIB, myProcessMIBConformance=myProcessMIBConformance, myCPUUtilization1Min=myCPUUtilization1Min, myNodeCPUTotalTable=myNodeCPUTotalTable, myNodeCPUTotal5sec=myNodeCPUTotal5sec, myCPUUtilization5Min=myCPUUtilization5Min, myNodeCPUTotalCritical=myNodeCPUTotalCritical, myNodeCPUTotalGroups=myNodeCPUTotalGroups, myProcessMIBCompliance=myProcessMIBCompliance, myCPUUtilizationCritical=myCPUUtilizationCritical, myCPUUtilization5Sec=myCPUUtilization5Sec)
