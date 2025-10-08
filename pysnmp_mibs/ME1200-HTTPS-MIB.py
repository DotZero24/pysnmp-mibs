#
# PySNMP MIB module ME1200-HTTPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-HTTPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ME1200-HTTPS-MIB", me1200HttpsMIBConformance=me1200HttpsMIBConformance, me1200HttpsGlobals=me1200HttpsGlobals, me1200HttpsMIBObjects=me1200HttpsMIBObjects, me1200HttpsGlobalsMode=me1200HttpsGlobalsMode, me1200HttpsGlobalsInfoGroup=me1200HttpsGlobalsInfoGroup, me1200HttpsGlobalsRedirectToHttps=me1200HttpsGlobalsRedirectToHttps, me1200HttpsMIBCompliance=me1200HttpsMIBCompliance, me1200HttpsMIBGroups=me1200HttpsMIBGroups, PYSNMP_MODULE_ID=me1200HttpsMIB, me1200HttpsConfig=me1200HttpsConfig, me1200HttpsMIBCompliances=me1200HttpsMIBCompliances, me1200HttpsMIB=me1200HttpsMIB)
