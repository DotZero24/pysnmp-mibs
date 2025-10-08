#
# PySNMP MIB module TIMETRA-SAS-IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TIMETRA-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:19:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1xAuthConfigEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthConfigEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
timetraSASObjs, timetraSASConfs, timetraSASModules, timetraSASNotifyPrefix = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASObjs", "timetraSASConfs", "timetraSASModules", "timetraSASNotifyPrefix")
TPolicyStatementNameOrEmpty, ServiceAdminStatus, TNamedItem = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TPolicyStatementNameOrEmpty", "ServiceAdminStatus", "TNamedItem")
timeraSASIEEE8021PaeMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 17))
timeraSASIEEE8021PaeMIBModule.setRevisions(('1912-07-01 00:00',))
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setLastUpdated('1207010000Z')
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setOrganization('Alcatel-Lucent')
tmnxSASDot1xObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16))
tmnxSASDot1xAuthenticatorObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1))
tmnxSASDot1xConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12))
tmnxDot1xSASCompliancs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1))
tmnxDot1xSASGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2))
dot1xAuthConfigExtnTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1), )
if mibBuilder.loadTexts: dot1xAuthConfigExtnTable.setStatus('current')
dot1xAuthConfigExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1), )
dot1xAuthConfigEntry.registerAugmentions(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xAuthConfigExtnEntry"))
dot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
if mibBuilder.loadTexts: dot1xAuthConfigExtnEntry.setStatus('current')
dot1xPortEtherTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1, 150), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPortEtherTunnel.setStatus('current')
dot1xAuthConfigExtnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2, 1)).setObjects(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xPortEtherTunnel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xAuthConfigExtnGroup = dot1xAuthConfigExtnGroup.setStatus('current')
dot1xAuthConfigExtnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1, 1)).setObjects(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xAuthConfigExtnGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xAuthConfigExtnCompliance = dot1xAuthConfigExtnCompliance.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-SAS-IEEE8021-PAE-MIB", timeraSASIEEE8021PaeMIBModule=timeraSASIEEE8021PaeMIBModule, tmnxDot1xSASCompliancs=tmnxDot1xSASCompliancs, dot1xAuthConfigExtnCompliance=dot1xAuthConfigExtnCompliance, dot1xAuthConfigExtnTable=dot1xAuthConfigExtnTable, dot1xAuthConfigExtnGroup=dot1xAuthConfigExtnGroup, tmnxSASDot1xConformance=tmnxSASDot1xConformance, tmnxDot1xSASGroups=tmnxDot1xSASGroups, dot1xPortEtherTunnel=dot1xPortEtherTunnel, PYSNMP_MODULE_ID=timeraSASIEEE8021PaeMIBModule, dot1xAuthConfigExtnEntry=dot1xAuthConfigExtnEntry, tmnxSASDot1xObjs=tmnxSASDot1xObjs, tmnxSASDot1xAuthenticatorObjs=tmnxSASDot1xAuthenticatorObjs)
