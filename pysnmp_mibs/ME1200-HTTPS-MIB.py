#
# PySNMP MIB module ME1200-HTTPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/ME1200-HTTPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
me1200HttpsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47))
me1200HttpsMIB.setRevisions(('2014-01-29 00:00', '2013-10-17 00:00',))
if mibBuilder.loadTexts: me1200HttpsMIB.setLastUpdated('201401290000Z')
if mibBuilder.loadTexts: me1200HttpsMIB.setOrganization('Cisco Systems, Inc')
me1200HttpsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1))
me1200HttpsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2))
me1200HttpsGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2, 1))
me1200HttpsGlobalsMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200HttpsGlobalsMode.setStatus('current')
me1200HttpsGlobalsRedirectToHttps = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200HttpsGlobalsRedirectToHttps.setStatus('current')
me1200HttpsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2))
me1200HttpsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 1))
me1200HttpsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 2))
me1200HttpsGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 2, 1)).setObjects(("ME1200-HTTPS-MIB", "me1200HttpsGlobalsMode"), ("ME1200-HTTPS-MIB", "me1200HttpsGlobalsRedirectToHttps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200HttpsGlobalsInfoGroup = me1200HttpsGlobalsInfoGroup.setStatus('current')
me1200HttpsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 47, 2, 1, 1)).setObjects(("ME1200-HTTPS-MIB", "me1200HttpsGlobalsInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200HttpsMIBCompliance = me1200HttpsMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-HTTPS-MIB", me1200HttpsGlobalsMode=me1200HttpsGlobalsMode, PYSNMP_MODULE_ID=me1200HttpsMIB, me1200HttpsGlobalsRedirectToHttps=me1200HttpsGlobalsRedirectToHttps, me1200HttpsGlobals=me1200HttpsGlobals, me1200HttpsMIBConformance=me1200HttpsMIBConformance, me1200HttpsMIB=me1200HttpsMIB, me1200HttpsGlobalsInfoGroup=me1200HttpsGlobalsInfoGroup, me1200HttpsMIBCompliances=me1200HttpsMIBCompliances, me1200HttpsConfig=me1200HttpsConfig, me1200HttpsMIBCompliance=me1200HttpsMIBCompliance, me1200HttpsMIBGroups=me1200HttpsMIBGroups, me1200HttpsMIBObjects=me1200HttpsMIBObjects)
