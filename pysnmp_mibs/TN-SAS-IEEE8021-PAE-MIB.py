#
# PySNMP MIB module TN-SAS-IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TN-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:20:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1xAuthConfigEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthConfigEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
tnSASModules, tnSASObjs = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSASModules", "tnSASObjs")
tnSASIEEE8021PaeMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 17))
tnSASIEEE8021PaeMIBModule.setRevisions(('2015-01-09 00:00',))
if mibBuilder.loadTexts: tnSASIEEE8021PaeMIBModule.setLastUpdated('201501090000Z')
if mibBuilder.loadTexts: tnSASIEEE8021PaeMIBModule.setOrganization('Nokia')
tnSASDot1xMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16))
tnSASDot1xAuthenticatorObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1))
tnDot1xSASCompliancs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 2))
tnDot1xSASGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 3))
tnDot1xAuthConfigExtnTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1, 1), )
if mibBuilder.loadTexts: tnDot1xAuthConfigExtnTable.setStatus('current')
tnDot1xAuthConfigExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1, 1, 1), )
dot1xAuthConfigEntry.registerAugmentions(("TN-SAS-IEEE8021-PAE-MIB", "tnDot1xAuthConfigExtnEntry"))
tnDot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
if mibBuilder.loadTexts: tnDot1xAuthConfigExtnEntry.setStatus('current')
tnDot1xPortEtherTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnDot1xPortEtherTunnel.setStatus('current')
tnDot1xAuthConfigExtnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 3, 1)).setObjects(("TN-SAS-IEEE8021-PAE-MIB", "tnDot1xPortEtherTunnel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnDot1xAuthConfigExtnGroup = tnDot1xAuthConfigExtnGroup.setStatus('current')
tnDot1xAuthConfigExtnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 2, 1)).setObjects(("TN-SAS-IEEE8021-PAE-MIB", "tnDot1xAuthConfigExtnGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnDot1xAuthConfigExtnCompliance = tnDot1xAuthConfigExtnCompliance.setStatus('current')
mibBuilder.exportSymbols("TN-SAS-IEEE8021-PAE-MIB", tnDot1xAuthConfigExtnTable=tnDot1xAuthConfigExtnTable, tnSASDot1xMIBObjs=tnSASDot1xMIBObjs, tnDot1xAuthConfigExtnCompliance=tnDot1xAuthConfigExtnCompliance, tnDot1xPortEtherTunnel=tnDot1xPortEtherTunnel, tnSASIEEE8021PaeMIBModule=tnSASIEEE8021PaeMIBModule, tnDot1xSASGroups=tnDot1xSASGroups, tnDot1xAuthConfigExtnEntry=tnDot1xAuthConfigExtnEntry, tnDot1xAuthConfigExtnGroup=tnDot1xAuthConfigExtnGroup, tnSASDot1xAuthenticatorObjs=tnSASDot1xAuthenticatorObjs, PYSNMP_MODULE_ID=tnSASIEEE8021PaeMIBModule, tnDot1xSASCompliancs=tnDot1xSASCompliancs)
