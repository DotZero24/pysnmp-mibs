#
# PySNMP MIB module H3C-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-FCOE-MODE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135))
h3cFcoeMode.setRevisions(('2013-03-08 11:00',))
if mibBuilder.loadTexts: h3cFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: h3cFcoeMode.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1))
h3cFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFcoeModeCfgMode.setStatus('current')
h3cFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcoeModeCfgLastResult.setStatus('current')
mibBuilder.exportSymbols("H3C-FCOE-MODE-MIB", h3cFcoeMode=h3cFcoeMode, h3cFcoeModeCfgMode=h3cFcoeModeCfgMode, h3cFcoeModeMibObjects=h3cFcoeModeMibObjects, PYSNMP_MODULE_ID=h3cFcoeMode, h3cFcoeModeCfgLastResult=h3cFcoeModeCfgLastResult)
