#
# PySNMP MIB module A3COM-HUAWEI-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-OBJECT-INFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55))
h3cObjectInfo.setRevisions(('2004-12-27 00:00',))
if mibBuilder.loadTexts: h3cObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: h3cObjectInfo.setOrganization(' Huawei 3Com Technologies Co., Ltd. ')
h3cObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1))
h3cObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1), )
if mibBuilder.loadTexts: h3cObjectInfoTable.setStatus('current')
h3cObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoOID"), (0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoType"), (0, "A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoTypeExtension"))
if mibBuilder.loadTexts: h3cObjectInfoEntry.setStatus('current')
h3cObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: h3cObjectInfoOID.setStatus('current')
h3cObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: h3cObjectInfoType.setStatus('current')
h3cObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: h3cObjectInfoTypeExtension.setStatus('current')
h3cObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cObjectInfoValue.setStatus('current')
h3cObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2))
h3cObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 1))
h3cObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 1, 1)).setObjects(("A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoMIBCompliance = h3cObjectInfoMIBCompliance.setStatus('current')
h3cObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 2))
h3cObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 55, 2, 2, 1)).setObjects(("A3COM-HUAWEI-OBJECT-INFO-MIB", "h3cObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoTableGroup = h3cObjectInfoTableGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-OBJECT-INFO-MIB", h3cObjectInfoMIBCompliances=h3cObjectInfoMIBCompliances, h3cObjectInfoMIBGroups=h3cObjectInfoMIBGroups, h3cObjectInfo=h3cObjectInfo, h3cObjectInfoTableGroup=h3cObjectInfoTableGroup, h3cObjectInfoType=h3cObjectInfoType, h3cObjectInfoValue=h3cObjectInfoValue, h3cObjectInfoMIBCompliance=h3cObjectInfoMIBCompliance, h3cObjectInfoEntry=h3cObjectInfoEntry, h3cObjectInfoTypeExtension=h3cObjectInfoTypeExtension, h3cObjectInfoOID=h3cObjectInfoOID, h3cObjectInfoTable=h3cObjectInfoTable, h3cObjectInfoMIBConformance=h3cObjectInfoMIBConformance, PYSNMP_MODULE_ID=h3cObjectInfo, h3cObjectInformation=h3cObjectInformation)
