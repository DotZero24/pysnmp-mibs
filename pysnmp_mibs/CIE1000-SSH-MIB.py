#
# PySNMP MIB module CIE1000-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CIE1000-SSH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cie1000SwitchMgmt, = mibBuilder.importSymbols("CISCO-IE1000-MIB", "cie1000SwitchMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
cie1000SshMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49))
cie1000SshMib.setRevisions(('2014-07-01 00:00',))
if mibBuilder.loadTexts: cie1000SshMib.setLastUpdated('201407010000Z')
if mibBuilder.loadTexts: cie1000SshMib.setOrganization('Cisco Systems, Inc.')
cie1000SshMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1))
cie1000SshConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1, 2))
cie1000SshConfigGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1, 2, 1))
cie1000SshConfigGlobalsAdminState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000SshConfigGlobalsAdminState.setStatus('current')
cie1000SshMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2))
cie1000SshMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 1))
cie1000SshMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 2))
cie1000SshConfigGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 2, 1)).setObjects(("CIE1000-SSH-MIB", "cie1000SshConfigGlobalsAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000SshConfigGlobalsInfoGroup = cie1000SshConfigGlobalsInfoGroup.setStatus('current')
cie1000SshMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 49, 2, 1, 1)).setObjects(("CIE1000-SSH-MIB", "cie1000SshConfigGlobalsInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000SshMibCompliance = cie1000SshMibCompliance.setStatus('current')
mibBuilder.exportSymbols("CIE1000-SSH-MIB", cie1000SshMibCompliances=cie1000SshMibCompliances, cie1000SshMibGroups=cie1000SshMibGroups, PYSNMP_MODULE_ID=cie1000SshMib, cie1000SshConfig=cie1000SshConfig, cie1000SshConfigGlobals=cie1000SshConfigGlobals, cie1000SshMib=cie1000SshMib, cie1000SshMibObjects=cie1000SshMibObjects, cie1000SshConfigGlobalsInfoGroup=cie1000SshConfigGlobalsInfoGroup, cie1000SshMibConformance=cie1000SshMibConformance, cie1000SshConfigGlobalsAdminState=cie1000SshConfigGlobalsAdminState, cie1000SshMibCompliance=cie1000SshMibCompliance)
