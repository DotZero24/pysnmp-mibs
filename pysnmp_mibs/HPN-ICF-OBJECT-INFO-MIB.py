#
# PySNMP MIB module HPN-ICF-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-OBJECT-INFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55))
hpnicfObjectInfo.setRevisions(('2004-12-27 00:00',))
if mibBuilder.loadTexts: hpnicfObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: hpnicfObjectInfo.setOrganization('')
hpnicfObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1))
hpnicfObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1), )
if mibBuilder.loadTexts: hpnicfObjectInfoTable.setStatus('current')
hpnicfObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoOID"), (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoType"), (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTypeExtension"))
if mibBuilder.loadTexts: hpnicfObjectInfoEntry.setStatus('current')
hpnicfObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: hpnicfObjectInfoOID.setStatus('current')
hpnicfObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: hpnicfObjectInfoType.setStatus('current')
hpnicfObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hpnicfObjectInfoTypeExtension.setStatus('current')
hpnicfObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfObjectInfoValue.setStatus('current')
hpnicfObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2))
hpnicfObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1))
hpnicfObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1, 1)).setObjects(("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfObjectInfoMIBCompliance = hpnicfObjectInfoMIBCompliance.setStatus('current')
hpnicfObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2))
hpnicfObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2, 1)).setObjects(("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfObjectInfoTableGroup = hpnicfObjectInfoTableGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-OBJECT-INFO-MIB", hpnicfObjectInfoOID=hpnicfObjectInfoOID, hpnicfObjectInfoTable=hpnicfObjectInfoTable, hpnicfObjectInfoTypeExtension=hpnicfObjectInfoTypeExtension, hpnicfObjectInfoMIBCompliances=hpnicfObjectInfoMIBCompliances, PYSNMP_MODULE_ID=hpnicfObjectInfo, hpnicfObjectInfoMIBCompliance=hpnicfObjectInfoMIBCompliance, hpnicfObjectInfo=hpnicfObjectInfo, hpnicfObjectInfoEntry=hpnicfObjectInfoEntry, hpnicfObjectInfoMIBGroups=hpnicfObjectInfoMIBGroups, hpnicfObjectInfoMIBConformance=hpnicfObjectInfoMIBConformance, hpnicfObjectInfoType=hpnicfObjectInfoType, hpnicfObjectInfoValue=hpnicfObjectInfoValue, hpnicfObjectInformation=hpnicfObjectInformation, hpnicfObjectInfoTableGroup=hpnicfObjectInfoTableGroup)
