#
# PySNMP MIB module TIMETRA-SAS-IEEE8021-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TIMETRA-SAS-IEEE8021-CFM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:18:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1agCfmMepEntry, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMepEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
timetraSASObjs, timetraSASConfs, timetraSASModules = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASObjs", "timetraSASConfs", "timetraSASModules")
timetraSASIEEE8021CfmMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 11))
timetraSASIEEE8021CfmMIBModule.setRevisions(('1910-01-01 00:00',))
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setLastUpdated('0902280000Z')
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setOrganization('Alcatel')
tmnxSASDot1agMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11))
tmnxSASDot1agMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7))
tmnxSASDot1agCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1))
tmnxSASDot1agNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2))
tmnxSASDot1agNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2, 1))
tmnxDot1agCfmMepExtnTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1), )
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnTable.setStatus('current')
tmnxDot1agCfmMepExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1), )
dot1agCfmMepEntry.registerAugmentions(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepExtnEntry"))
tmnxDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnEntry.setStatus('current')
tmnxDot1agCfmMepSendAisOnPortDown = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxDot1agCfmMepSendAisOnPortDown.setStatus('current')
tmnxDot1agCfmMepControlSapTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxDot1agCfmMepControlSapTag.setStatus('current')
tmnxSASDot1agCfmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1))
tmnxSASDot1agCfmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2))
tmnxSASDot1agCfmComplianceV2v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1, 2)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxSASDot1agCfmMepGroupV2v0"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmComplianceV2v0 = tmnxSASDot1agCfmComplianceV2v0.setStatus('current')
tmnxSASDot1agCfmMepGroupV2v0 = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 1)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmMepGroupV2v0 = tmnxSASDot1agCfmMepGroupV2v0.setStatus('current')
tmnxSASDot1agCfmMepGroupV4v0 = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 2)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown"), ("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepControlSapTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmMepGroupV4v0 = tmnxSASDot1agCfmMepGroupV4v0.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-SAS-IEEE8021-CFM-MIB", tmnxDot1agCfmMepExtnEntry=tmnxDot1agCfmMepExtnEntry, tmnxSASDot1agCfmGroups=tmnxSASDot1agCfmGroups, timetraSASIEEE8021CfmMIBModule=timetraSASIEEE8021CfmMIBModule, tmnxSASDot1agCfmMepGroupV2v0=tmnxSASDot1agCfmMepGroupV2v0, tmnxDot1agCfmMepControlSapTag=tmnxDot1agCfmMepControlSapTag, tmnxSASDot1agMIBObjs=tmnxSASDot1agMIBObjs, tmnxSASDot1agNotificationsPrefix=tmnxSASDot1agNotificationsPrefix, tmnxDot1agCfmMepExtnTable=tmnxDot1agCfmMepExtnTable, tmnxSASDot1agCfmComplianceV2v0=tmnxSASDot1agCfmComplianceV2v0, tmnxSASDot1agCfmMepGroupV4v0=tmnxSASDot1agCfmMepGroupV4v0, tmnxSASDot1agCfmMep=tmnxSASDot1agCfmMep, PYSNMP_MODULE_ID=timetraSASIEEE8021CfmMIBModule, tmnxSASDot1agNotifications=tmnxSASDot1agNotifications, tmnxSASDot1agMIBConformance=tmnxSASDot1agMIBConformance, tmnxSASDot1agCfmCompliances=tmnxSASDot1agCfmCompliances, tmnxDot1agCfmMepSendAisOnPortDown=tmnxDot1agCfmMepSendAisOnPortDown)
