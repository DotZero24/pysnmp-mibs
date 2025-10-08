#
# PySNMP MIB module NEWTEC-ENCAPDECAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-ENCAPDECAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NEWTEC-ENCAPDECAP-MIB", ntcEncapDecapObjects=ntcEncapDecapObjects, ntcEncapDecapConfCompV1Standard=ntcEncapDecapConfCompV1Standard, ntcEncapDecapConformance=ntcEncapDecapConformance, ntcEncapDecap=ntcEncapDecap, ntcEncapDecapConfCompliance=ntcEncapDecapConfCompliance, ntcEncapDecapConfGroup=ntcEncapDecapConfGroup, ntcEncapDecapConfGrpV1Standard=ntcEncapDecapConfGrpV1Standard, ntcEncapDecapForwardingMode=ntcEncapDecapForwardingMode, PYSNMP_MODULE_ID=ntcEncapDecap)
