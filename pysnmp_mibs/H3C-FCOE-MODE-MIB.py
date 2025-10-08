#
# PySNMP MIB module H3C-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-FCOE-MODE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135))
h3cFcoeMode.setRevisions(('2013-03-08 11:00',))
if mibBuilder.loadTexts: h3cFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: h3cFcoeMode.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1))
h3cFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFcoeModeCfgMode.setStatus('current')
h3cFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFcoeModeCfgLastResult.setStatus('current')
mibBuilder.exportSymbols("H3C-FCOE-MODE-MIB", h3cFcoeModeCfgMode=h3cFcoeModeCfgMode, PYSNMP_MODULE_ID=h3cFcoeMode, h3cFcoeMode=h3cFcoeMode, h3cFcoeModeMibObjects=h3cFcoeModeMibObjects, h3cFcoeModeCfgLastResult=h3cFcoeModeCfgLastResult)
