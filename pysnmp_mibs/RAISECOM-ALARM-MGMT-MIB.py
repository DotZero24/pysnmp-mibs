#
# PySNMP MIB module RAISECOM-ALARM-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/RAISECOM-ALARM-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
raisecomAgent, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "raisecomAgent")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, zeroDotZero, NotificationType, Integer32, Bits, Unsigned32, mib_2, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "zeroDotZero", "NotificationType", "Integer32", "Bits", "Unsigned32", "mib-2", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Opaque")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
raisecomAlarmMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 1, 34))
if mibBuilder.loadTexts: raisecomAlarmMgmt.setLastUpdated('201103120000Z')
if mibBuilder.loadTexts: raisecomAlarmMgmt.setOrganization('Raisecom Technology Co., Ltd.')
raisecomAlarmMgmtObejcts = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1))
class AlarmStorageMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("stop", 1), ("loop", 2))

class AlarmInverseMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("auto", 2), ("manual", 3))

raisecomAlarmMgmtRaiseDelay = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtRaiseDelay.setStatus('current')
raisecomAlarmMgmtClearDelay = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtClearDelay.setStatus('current')
raisecomAlarmMgmtActiveStoreMode = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 3), AlarmStorageMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtActiveStoreMode.setStatus('current')
raisecomAlarmMgmtInhibitEnable = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtInhibitEnable.setStatus('current')
raisecomAlarmMgmtSyslogEnable = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtSyslogEnable.setStatus('current')
raisecomAlarmMgmtActiveClear = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtActiveClear.setStatus('current')
raisecomAlarmMgmtConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7), )
if mibBuilder.loadTexts: raisecomAlarmMgmtConfigTable.setStatus('current')
raisecomAlarmMgmtConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1), ).setIndexNames((0, "RAISECOM-ALARM-MGMT-MIB", "raisecomAlarmMgmtId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: raisecomAlarmMgmtConfigEntry.setStatus('current')
raisecomAlarmMgmtId = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 1), Unsigned32())
if mibBuilder.loadTexts: raisecomAlarmMgmtId.setStatus('current')
raisecomAlarmMgmtClear = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtClear.setStatus('current')
raisecomAlarmMgmtReportEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtReportEnable.setStatus('current')
raisecomAlarmMgmtMonitorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtMonitorEnable.setStatus('current')
raisecomAlarmMgmtInverseMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 5), AlarmInverseMode().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomAlarmMgmtInverseMode.setStatus('current')
raisecomAlarmMgmtModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raisecomAlarmMgmtModuleName.setStatus('current')
raisecomAlarmMgmtGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raisecomAlarmMgmtGroupName.setStatus('current')
mibBuilder.exportSymbols("RAISECOM-ALARM-MGMT-MIB", raisecomAlarmMgmtObejcts=raisecomAlarmMgmtObejcts, raisecomAlarmMgmtActiveClear=raisecomAlarmMgmtActiveClear, raisecomAlarmMgmtInhibitEnable=raisecomAlarmMgmtInhibitEnable, raisecomAlarmMgmtConfigTable=raisecomAlarmMgmtConfigTable, raisecomAlarmMgmtMonitorEnable=raisecomAlarmMgmtMonitorEnable, raisecomAlarmMgmtActiveStoreMode=raisecomAlarmMgmtActiveStoreMode, raisecomAlarmMgmtSyslogEnable=raisecomAlarmMgmtSyslogEnable, raisecomAlarmMgmtReportEnable=raisecomAlarmMgmtReportEnable, AlarmStorageMode=AlarmStorageMode, raisecomAlarmMgmtClear=raisecomAlarmMgmtClear, raisecomAlarmMgmtModuleName=raisecomAlarmMgmtModuleName, raisecomAlarmMgmtInverseMode=raisecomAlarmMgmtInverseMode, raisecomAlarmMgmtGroupName=raisecomAlarmMgmtGroupName, raisecomAlarmMgmt=raisecomAlarmMgmt, raisecomAlarmMgmtId=raisecomAlarmMgmtId, raisecomAlarmMgmtRaiseDelay=raisecomAlarmMgmtRaiseDelay, raisecomAlarmMgmtConfigEntry=raisecomAlarmMgmtConfigEntry, AlarmInverseMode=AlarmInverseMode, raisecomAlarmMgmtClearDelay=raisecomAlarmMgmtClearDelay, PYSNMP_MODULE_ID=raisecomAlarmMgmt)
