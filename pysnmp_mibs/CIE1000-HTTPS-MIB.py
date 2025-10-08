#
# PySNMP MIB module CIE1000-HTTPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CIE1000-HTTPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cie1000SwitchMgmt, = mibBuilder.importSymbols("CISCO-IE1000-MIB", "cie1000SwitchMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CIE1000-HTTPS-MIB", cie1000HttpsConfigGlobalsInfoGroup=cie1000HttpsConfigGlobalsInfoGroup, cie1000HttpsConfigGlobalsMode=cie1000HttpsConfigGlobalsMode, cie1000HttpsMibGroups=cie1000HttpsMibGroups, cie1000HttpsConfig=cie1000HttpsConfig, cie1000HttpsConfigGlobals=cie1000HttpsConfigGlobals, cie1000HttpsMibCompliances=cie1000HttpsMibCompliances, cie1000HttpsMib=cie1000HttpsMib, cie1000HttpsMibConformance=cie1000HttpsMibConformance, PYSNMP_MODULE_ID=cie1000HttpsMib, cie1000HttpsConfigGlobalsRedirectToHttps=cie1000HttpsConfigGlobalsRedirectToHttps, cie1000HttpsMibCompliance=cie1000HttpsMibCompliance, cie1000HttpsMibObjects=cie1000HttpsMibObjects)
