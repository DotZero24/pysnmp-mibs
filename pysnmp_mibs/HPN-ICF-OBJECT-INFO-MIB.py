#
# PySNMP MIB module HPN-ICF-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-OBJECT-INFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HPN-ICF-OBJECT-INFO-MIB", hpnicfObjectInfoTableGroup=hpnicfObjectInfoTableGroup, hpnicfObjectInfoTable=hpnicfObjectInfoTable, hpnicfObjectInformation=hpnicfObjectInformation, hpnicfObjectInfoType=hpnicfObjectInfoType, hpnicfObjectInfoTypeExtension=hpnicfObjectInfoTypeExtension, hpnicfObjectInfoMIBConformance=hpnicfObjectInfoMIBConformance, PYSNMP_MODULE_ID=hpnicfObjectInfo, hpnicfObjectInfoMIBCompliances=hpnicfObjectInfoMIBCompliances, hpnicfObjectInfo=hpnicfObjectInfo, hpnicfObjectInfoValue=hpnicfObjectInfoValue, hpnicfObjectInfoMIBCompliance=hpnicfObjectInfoMIBCompliance, hpnicfObjectInfoMIBGroups=hpnicfObjectInfoMIBGroups, hpnicfObjectInfoOID=hpnicfObjectInfoOID, hpnicfObjectInfoEntry=hpnicfObjectInfoEntry)
