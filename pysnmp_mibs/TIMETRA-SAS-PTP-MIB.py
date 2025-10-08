#
# PySNMP MIB module TIMETRA-SAS-PTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TIMETRA-SAS-PTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:38:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, RowPointer, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "RowPointer", "TruthValue", "TimeStamp", "DisplayString")
tmnxCpmCardOscillatorType, tmnxChassisNotifyHwIndex, tmnxChassisNotifyChassisId, tmnxCpmCardEntry = mibBuilder.importSymbols("TIMETRA-CHASSIS-MIB", "tmnxCpmCardOscillatorType", "tmnxChassisNotifyHwIndex", "tmnxChassisNotifyChassisId", "tmnxCpmCardEntry")
tmnxSRObjs, timetraSRMIBModules, tmnxSRNotifyPrefix, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRObjs", "timetraSRMIBModules", "tmnxSRNotifyPrefix", "tmnxSRConfs")
TmnxPtpLogInterval, = mibBuilder.importSymbols("TIMETRA-PTP-MIB", "TmnxPtpLogInterval")
timetraSASModules, timetraSASNotifyPrefix, timetraSASConfs, timetraSASObjs = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASModules", "timetraSASNotifyPrefix", "timetraSASConfs", "timetraSASObjs")
TmnxAdminState, TItemDescription, TmnxOperState = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TmnxAdminState", "TItemDescription", "TmnxOperState")
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
mibBuilder.exportSymbols("TIMETRA-SAS-PTP-MIB", PYSNMP_MODULE_ID=timetraSASPtpMIBModule, timetraSASPtpMIBModule=timetraSASPtpMIBModule, tmnxSASPtpV5v0Group=tmnxSASPtpV5v0Group, tmnxPtpLogSyncInterval=tmnxPtpLogSyncInterval, tmnxSASPtpGroups=tmnxSASPtpGroups, tmnxSASPtpClockConfig=tmnxSASPtpClockConfig, tmnxSASPtp1588Objs=tmnxSASPtp1588Objs)
