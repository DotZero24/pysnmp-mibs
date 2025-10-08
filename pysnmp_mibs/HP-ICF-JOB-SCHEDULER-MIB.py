#
# PySNMP MIB module HP-ICF-JOB-SCHEDULER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-JOB-SCHEDULER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
hpicfJobSchedulerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105))
hpicfJobSchedulerMIB.setRevisions(('2016-05-04 00:00', '2016-04-19 00:00', '2015-08-27 00:00', '2015-05-13 00:00', '2013-10-05 00:00',))
if mibBuilder.loadTexts: hpicfJobSchedulerMIB.setLastUpdated('201605040000Z')
if mibBuilder.loadTexts: hpicfJobSchedulerMIB.setOrganization('HP Networking')
hpicfJobSchedulerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1))
hpicfJobSchedulerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2))
hpicfJobSchedulerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1), )
if mibBuilder.loadTexts: hpicfJobSchedulerTable.setStatus('current')
hpicfJobSchedulerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1), ).setIndexNames((0, "HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerName"))
if mibBuilder.loadTexts: hpicfJobSchedulerEntry.setStatus('current')
hpicfJobSchedulerName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40)))
if mibBuilder.loadTexts: hpicfJobSchedulerName.setStatus('current')
hpicfJobSchedulerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfJobSchedulerRowStatus.setStatus('current')
hpicfJobSchedulerCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerCommand.setStatus('current')
hpicfJobSchedulerConfigSave = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerConfigSave.setStatus('current')
hpicfJobSchedulerRunCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfJobSchedulerRunCount.setStatus('current')
hpicfJobSchedulerErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfJobSchedulerErrorCount.setStatus('current')
hpicfJobSchedulerLastOutput = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfJobSchedulerLastOutput.setStatus('current')
hpicfJobSchedulerEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 8), Bits().clone(namedValues=NamedValues(("reboot", 0), ("failover", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerEvent.setStatus('current')
hpicfJobSchedulerCalendarMonth = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 9), Bits().clone(namedValues=NamedValues(("january", 0), ("february", 1), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), ("november", 10), ("december", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerCalendarMonth.setStatus('current')
hpicfJobSchedulerCalendarDayOfMonth = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 10), Bits().clone(namedValues=NamedValues(("d1", 0), ("d2", 1), ("d3", 2), ("d4", 3), ("d5", 4), ("d6", 5), ("d7", 6), ("d8", 7), ("d9", 8), ("d10", 9), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("r30", 60), ("r31", 61)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerCalendarDayOfMonth.setStatus('current')
hpicfJobSchedulerCalendarDayOfWeek = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 11), Bits().clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerCalendarDayOfWeek.setStatus('current')
hpicfJobSchedulerCalendarHour = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 12), Bits().clone(namedValues=NamedValues(("h0", 0), ("h1", 1), ("h2", 2), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerCalendarHour.setStatus('current')
hpicfJobSchedulerCalendarMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 13), Bits().clone(namedValues=NamedValues(("m0", 0), ("m1", 1), ("m2", 2), ("m3", 3), ("m4", 4), ("m5", 5), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerCalendarMinute.setStatus('current')
hpicfJobSchedulerDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 527039))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerDelay.setStatus('current')
hpicfJobSchedulerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerCount.setStatus('current')
hpicfJobSchedulerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 16), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfJobSchedulerStatus.setStatus('current')
hpicfJobSchedulerRunningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("expired", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfJobSchedulerRunningStatus.setStatus('current')
hpicfJobSchedulerLastRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 18), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfJobSchedulerLastRunTime.setStatus('current')
hpicfJobSchedulerSkipCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfJobSchedulerSkipCount.setStatus('current')
hpicfJobSchedulerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 1)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerGroup = hpicfJobSchedulerGroup.setStatus('deprecated')
hpicfJobSchedulerGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 2)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerDelay"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerGroup1 = hpicfJobSchedulerGroup1.setStatus('deprecated')
hpicfJobSchedulerGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 3)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerDelay"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunningStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastRunTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerGroup2 = hpicfJobSchedulerGroup2.setStatus('deprecated')
hpicfJobSchedulerGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 4)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerDelay"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCount"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunningStatus"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastRunTime"), ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerSkipCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerGroup3 = hpicfJobSchedulerGroup3.setStatus('current')
hpicfJobSchedulerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1))
hpicfJobSchedulerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2))
hpicfJobSchedulerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 1)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerMIBCompliance = hpicfJobSchedulerMIBCompliance.setStatus('deprecated')
hpicfJobSchedulerMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 2)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerMIBCompliance1 = hpicfJobSchedulerMIBCompliance1.setStatus('deprecated')
hpicfJobSchedulerMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 3)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerMIBCompliance2 = hpicfJobSchedulerMIBCompliance2.setStatus('deprecated')
hpicfJobSchedulerMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 4)).setObjects(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJobSchedulerMIBCompliance3 = hpicfJobSchedulerMIBCompliance3.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-JOB-SCHEDULER-MIB", hpicfJobSchedulerGroup=hpicfJobSchedulerGroup, hpicfJobSchedulerRowStatus=hpicfJobSchedulerRowStatus, hpicfJobSchedulerSkipCount=hpicfJobSchedulerSkipCount, hpicfJobSchedulerObjects=hpicfJobSchedulerObjects, hpicfJobSchedulerMIBCompliance=hpicfJobSchedulerMIBCompliance, hpicfJobSchedulerMIBCompliance3=hpicfJobSchedulerMIBCompliance3, hpicfJobSchedulerCalendarDayOfMonth=hpicfJobSchedulerCalendarDayOfMonth, hpicfJobSchedulerStatus=hpicfJobSchedulerStatus, hpicfJobSchedulerMIBCompliance2=hpicfJobSchedulerMIBCompliance2, hpicfJobSchedulerLastOutput=hpicfJobSchedulerLastOutput, hpicfJobSchedulerConfigSave=hpicfJobSchedulerConfigSave, hpicfJobSchedulerMIB=hpicfJobSchedulerMIB, hpicfJobSchedulerRunningStatus=hpicfJobSchedulerRunningStatus, hpicfJobSchedulerLastRunTime=hpicfJobSchedulerLastRunTime, hpicfJobSchedulerCalendarMinute=hpicfJobSchedulerCalendarMinute, hpicfJobSchedulerName=hpicfJobSchedulerName, hpicfJobSchedulerCalendarDayOfWeek=hpicfJobSchedulerCalendarDayOfWeek, hpicfJobSchedulerMIBCompliance1=hpicfJobSchedulerMIBCompliance1, hpicfJobSchedulerErrorCount=hpicfJobSchedulerErrorCount, hpicfJobSchedulerEvent=hpicfJobSchedulerEvent, hpicfJobSchedulerConformance=hpicfJobSchedulerConformance, hpicfJobSchedulerCommand=hpicfJobSchedulerCommand, hpicfJobSchedulerDelay=hpicfJobSchedulerDelay, hpicfJobSchedulerCount=hpicfJobSchedulerCount, hpicfJobSchedulerRunCount=hpicfJobSchedulerRunCount, hpicfJobSchedulerMIBCompliances=hpicfJobSchedulerMIBCompliances, hpicfJobSchedulerCalendarMonth=hpicfJobSchedulerCalendarMonth, hpicfJobSchedulerGroup2=hpicfJobSchedulerGroup2, hpicfJobSchedulerEntry=hpicfJobSchedulerEntry, hpicfJobSchedulerTable=hpicfJobSchedulerTable, hpicfJobSchedulerCalendarHour=hpicfJobSchedulerCalendarHour, hpicfJobSchedulerMIBGroups=hpicfJobSchedulerMIBGroups, hpicfJobSchedulerGroup3=hpicfJobSchedulerGroup3, PYSNMP_MODULE_ID=hpicfJobSchedulerMIB, hpicfJobSchedulerGroup1=hpicfJobSchedulerGroup1)
