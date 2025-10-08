#
# PySNMP MIB module TIMETRA-SAS-IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TIMETRA-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:36:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1xAuthConfigEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthConfigEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
timetraSASModules, timetraSASNotifyPrefix, timetraSASConfs, timetraSASObjs = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASModules", "timetraSASNotifyPrefix", "timetraSASConfs", "timetraSASObjs")
TPolicyStatementNameOrEmpty, TNamedItem, ServiceAdminStatus = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TPolicyStatementNameOrEmpty", "TNamedItem", "ServiceAdminStatus")
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
mibBuilder.exportSymbols("TIMETRA-SAS-IEEE8021-PAE-MIB", tmnxSASDot1xConformance=tmnxSASDot1xConformance, timeraSASIEEE8021PaeMIBModule=timeraSASIEEE8021PaeMIBModule, tmnxSASDot1xAuthenticatorObjs=tmnxSASDot1xAuthenticatorObjs, PYSNMP_MODULE_ID=timeraSASIEEE8021PaeMIBModule, tmnxDot1xSASGroups=tmnxDot1xSASGroups, dot1xAuthConfigExtnTable=dot1xAuthConfigExtnTable, dot1xAuthConfigExtnCompliance=dot1xAuthConfigExtnCompliance, dot1xAuthConfigExtnGroup=dot1xAuthConfigExtnGroup, dot1xPortEtherTunnel=dot1xPortEtherTunnel, tmnxSASDot1xObjs=tmnxSASDot1xObjs, tmnxDot1xSASCompliancs=tmnxDot1xSASCompliancs, dot1xAuthConfigExtnEntry=dot1xAuthConfigExtnEntry)
