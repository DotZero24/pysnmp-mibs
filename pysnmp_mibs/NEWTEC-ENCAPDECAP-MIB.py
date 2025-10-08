#
# PySNMP MIB module NEWTEC-ENCAPDECAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-ENCAPDECAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcEncapDecap = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220))
ntcEncapDecap.setRevisions(('2014-02-03 12:00',))
if mibBuilder.loadTexts: ntcEncapDecap.setLastUpdated('201402031200Z')
if mibBuilder.loadTexts: ntcEncapDecap.setOrganization('Newtec Cy')
ntcEncapDecapObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 1))
if mibBuilder.loadTexts: ntcEncapDecapObjects.setStatus('current')
ntcEncapDecapConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2))
if mibBuilder.loadTexts: ntcEncapDecapConformance.setStatus('current')
ntcEncapDecapConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 1))
if mibBuilder.loadTexts: ntcEncapDecapConfCompliance.setStatus('current')
ntcEncapDecapConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 2))
if mibBuilder.loadTexts: ntcEncapDecapConfGroup.setStatus('current')
ntcEncapDecapForwardingMode = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("l2", 0), ("l3", 1))).clone('l3')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcEncapDecapForwardingMode.setStatus('current')
ntcEncapDecapConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 2, 1)).setObjects(("NEWTEC-ENCAPDECAP-MIB", "ntcEncapDecapForwardingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcEncapDecapConfGrpV1Standard = ntcEncapDecapConfGrpV1Standard.setStatus('current')
ntcEncapDecapConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2220, 2, 1, 1)).setObjects(("NEWTEC-ENCAPDECAP-MIB", "ntcEncapDecapConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcEncapDecapConfCompV1Standard = ntcEncapDecapConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-ENCAPDECAP-MIB", ntcEncapDecapConfCompV1Standard=ntcEncapDecapConfCompV1Standard, PYSNMP_MODULE_ID=ntcEncapDecap, ntcEncapDecapConformance=ntcEncapDecapConformance, ntcEncapDecapConfGroup=ntcEncapDecapConfGroup, ntcEncapDecap=ntcEncapDecap, ntcEncapDecapForwardingMode=ntcEncapDecapForwardingMode, ntcEncapDecapConfGrpV1Standard=ntcEncapDecapConfGrpV1Standard, ntcEncapDecapConfCompliance=ntcEncapDecapConfCompliance, ntcEncapDecapObjects=ntcEncapDecapObjects)
