#
# PySNMP MIB module TN-SAS-IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TN-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:39:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1xAuthConfigEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthConfigEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
tnSASObjs, tnSASModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnSASObjs", "tnSASModules")
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
mibBuilder.exportSymbols("TN-SAS-IEEE8021-PAE-MIB", tnDot1xSASCompliancs=tnDot1xSASCompliancs, tnSASDot1xMIBObjs=tnSASDot1xMIBObjs, tnDot1xAuthConfigExtnCompliance=tnDot1xAuthConfigExtnCompliance, tnDot1xAuthConfigExtnEntry=tnDot1xAuthConfigExtnEntry, PYSNMP_MODULE_ID=tnSASIEEE8021PaeMIBModule, tnDot1xPortEtherTunnel=tnDot1xPortEtherTunnel, tnSASIEEE8021PaeMIBModule=tnSASIEEE8021PaeMIBModule, tnDot1xAuthConfigExtnGroup=tnDot1xAuthConfigExtnGroup, tnDot1xSASGroups=tnDot1xSASGroups, tnDot1xAuthConfigExtnTable=tnDot1xAuthConfigExtnTable, tnSASDot1xAuthenticatorObjs=tnSASDot1xAuthenticatorObjs)
