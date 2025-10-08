#
# PySNMP MIB module H3C-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-OBJECT-INFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55))
h3cObjectInfo.setRevisions(('2004-12-27 00:00',))
if mibBuilder.loadTexts: h3cObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: h3cObjectInfo.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1))
h3cObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1), )
if mibBuilder.loadTexts: h3cObjectInfoTable.setStatus('current')
h3cObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1), ).setIndexNames((0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoOID"), (0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoType"), (0, "H3C-OBJECT-INFO-MIB", "h3cObjectInfoTypeExtension"))
if mibBuilder.loadTexts: h3cObjectInfoEntry.setStatus('current')
h3cObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: h3cObjectInfoOID.setStatus('current')
h3cObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: h3cObjectInfoType.setStatus('current')
h3cObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: h3cObjectInfoTypeExtension.setStatus('current')
h3cObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cObjectInfoValue.setStatus('current')
h3cObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2))
h3cObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 1))
h3cObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 1, 1)).setObjects(("H3C-OBJECT-INFO-MIB", "h3cObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoMIBCompliance = h3cObjectInfoMIBCompliance.setStatus('current')
h3cObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 2))
h3cObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 55, 2, 2, 1)).setObjects(("H3C-OBJECT-INFO-MIB", "h3cObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cObjectInfoTableGroup = h3cObjectInfoTableGroup.setStatus('current')
mibBuilder.exportSymbols("H3C-OBJECT-INFO-MIB", h3cObjectInfoEntry=h3cObjectInfoEntry, h3cObjectInfoMIBCompliances=h3cObjectInfoMIBCompliances, h3cObjectInfoValue=h3cObjectInfoValue, h3cObjectInfoTable=h3cObjectInfoTable, h3cObjectInfoType=h3cObjectInfoType, h3cObjectInfoMIBCompliance=h3cObjectInfoMIBCompliance, h3cObjectInfoMIBConformance=h3cObjectInfoMIBConformance, PYSNMP_MODULE_ID=h3cObjectInfo, h3cObjectInfoMIBGroups=h3cObjectInfoMIBGroups, h3cObjectInfoTableGroup=h3cObjectInfoTableGroup, h3cObjectInfo=h3cObjectInfo, h3cObjectInfoOID=h3cObjectInfoOID, h3cObjectInformation=h3cObjectInformation, h3cObjectInfoTypeExtension=h3cObjectInfoTypeExtension)
