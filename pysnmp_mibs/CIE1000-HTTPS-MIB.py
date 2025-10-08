#
# PySNMP MIB module CIE1000-HTTPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CIE1000-HTTPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:56 2025
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
cie1000HttpsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47))
cie1000HttpsMib.setRevisions(('2014-10-10 00:00', '2014-07-01 00:00',))
if mibBuilder.loadTexts: cie1000HttpsMib.setLastUpdated('201410100000Z')
if mibBuilder.loadTexts: cie1000HttpsMib.setOrganization('Cisco Systems, Inc.')
cie1000HttpsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1))
cie1000HttpsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2))
cie1000HttpsConfigGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2, 1))
cie1000HttpsConfigGlobalsMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000HttpsConfigGlobalsMode.setStatus('current')
cie1000HttpsConfigGlobalsRedirectToHttps = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000HttpsConfigGlobalsRedirectToHttps.setStatus('current')
cie1000HttpsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2))
cie1000HttpsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 1))
cie1000HttpsMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 2))
cie1000HttpsConfigGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 2, 1)).setObjects(("CIE1000-HTTPS-MIB", "cie1000HttpsConfigGlobalsMode"), ("CIE1000-HTTPS-MIB", "cie1000HttpsConfigGlobalsRedirectToHttps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000HttpsConfigGlobalsInfoGroup = cie1000HttpsConfigGlobalsInfoGroup.setStatus('current')
cie1000HttpsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 47, 2, 1, 1)).setObjects(("CIE1000-HTTPS-MIB", "cie1000HttpsConfigGlobalsInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000HttpsMibCompliance = cie1000HttpsMibCompliance.setStatus('current')
mibBuilder.exportSymbols("CIE1000-HTTPS-MIB", cie1000HttpsMibCompliances=cie1000HttpsMibCompliances, PYSNMP_MODULE_ID=cie1000HttpsMib, cie1000HttpsMib=cie1000HttpsMib, cie1000HttpsMibCompliance=cie1000HttpsMibCompliance, cie1000HttpsConfig=cie1000HttpsConfig, cie1000HttpsMibGroups=cie1000HttpsMibGroups, cie1000HttpsMibConformance=cie1000HttpsMibConformance, cie1000HttpsConfigGlobalsMode=cie1000HttpsConfigGlobalsMode, cie1000HttpsMibObjects=cie1000HttpsMibObjects, cie1000HttpsConfigGlobalsInfoGroup=cie1000HttpsConfigGlobalsInfoGroup, cie1000HttpsConfigGlobalsRedirectToHttps=cie1000HttpsConfigGlobalsRedirectToHttps, cie1000HttpsConfigGlobals=cie1000HttpsConfigGlobals)
