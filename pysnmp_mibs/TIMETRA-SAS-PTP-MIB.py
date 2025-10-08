#
# PySNMP MIB module TIMETRA-SAS-PTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TIMETRA-SAS-PTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:20:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, TruthValue, RowStatus, DateAndTime, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TruthValue", "RowStatus", "DateAndTime", "RowPointer", "TextualConvention")
tmnxCpmCardOscillatorType, tmnxChassisNotifyChassisId, tmnxCpmCardEntry, tmnxChassisNotifyHwIndex = mibBuilder.importSymbols("TIMETRA-CHASSIS-MIB", "tmnxCpmCardOscillatorType", "tmnxChassisNotifyChassisId", "tmnxCpmCardEntry", "tmnxChassisNotifyHwIndex")
tmnxSRNotifyPrefix, tmnxSRObjs, timetraSRMIBModules, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRNotifyPrefix", "tmnxSRObjs", "timetraSRMIBModules", "tmnxSRConfs")
TmnxPtpLogInterval, = mibBuilder.importSymbols("TIMETRA-PTP-MIB", "TmnxPtpLogInterval")
timetraSASObjs, timetraSASConfs, timetraSASModules, timetraSASNotifyPrefix = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASObjs", "timetraSASConfs", "timetraSASModules", "timetraSASNotifyPrefix")
TItemDescription, TmnxOperState, TmnxAdminState = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TItemDescription", "TmnxOperState", "TmnxAdminState")
vRtrID, = mibBuilder.importSymbols("TIMETRA-VRTR-MIB", "vRtrID")
timetraSASPtpMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 74))
timetraSASPtpMIBModule.setRevisions(('2011-02-01 00:00',))
if mibBuilder.loadTexts: timetraSASPtpMIBModule.setLastUpdated('201102010000Z')
if mibBuilder.loadTexts: timetraSASPtpMIBModule.setOrganization('Alcatel-Lucent')
tmnxSASPtp1588Objs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 74))
tmnxSASPtpClockConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 74, 1))
tmnxPtpLogSyncInterval = MibScalar((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 74, 1, 1), TmnxPtpLogInterval().subtype(subtypeSpec=ValueRangeConstraint(-6, -3)).clone(-6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxPtpLogSyncInterval.setStatus('current')
tmnxSASPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 74))
tmnxSASPtpV5v0Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 74, 1)).setObjects(("TIMETRA-SAS-PTP-MIB", "tmnxPtpLogSyncInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASPtpV5v0Group = tmnxSASPtpV5v0Group.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-SAS-PTP-MIB", tmnxSASPtpClockConfig=tmnxSASPtpClockConfig, tmnxSASPtp1588Objs=tmnxSASPtp1588Objs, tmnxSASPtpV5v0Group=tmnxSASPtpV5v0Group, timetraSASPtpMIBModule=timetraSASPtpMIBModule, tmnxPtpLogSyncInterval=tmnxPtpLogSyncInterval, PYSNMP_MODULE_ID=timetraSASPtpMIBModule, tmnxSASPtpGroups=tmnxSASPtpGroups)
