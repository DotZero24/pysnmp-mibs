#
# PySNMP MIB module ENERGY-OBJECT-CONTEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/ENERGY-OBJECT-CONTEXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
IANAEnergyRelationship, = mibBuilder.importSymbols("IANA-ENERGY-RELATION-MIB", "IANAEnergyRelationship")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, MacAddress, RowStatus, StorageType, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "StorageType", "TruthValue", "TextualConvention")
UUIDorZero, = mibBuilder.importSymbols("UUID-TC-MIB", "UUIDorZero")
energyObjectContextMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 231))
energyObjectContextMIB.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: energyObjectContextMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: energyObjectContextMIB.setOrganization('IETF EMAN Working Group')
energyObjectContextMIBNotifs = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 0))
energyObjectContextMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 1))
energyObjectContextMIBConform = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2))
class PethPsePortIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PethPsePortGroupIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class LldpPortNumberOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4096)

class EnergyObjectKeywordList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

eoTable = MibTable((1, 3, 6, 1, 2, 1, 231, 1, 1), )
if mibBuilder.loadTexts: eoTable.setStatus('current')
eoEntry = MibTableRow((1, 3, 6, 1, 2, 1, 231, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: eoEntry.setStatus('current')
eoEthPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 1), PethPsePortIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoEthPortIndex.setStatus('current')
eoEthPortGrpIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 2), PethPsePortGroupIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoEthPortGrpIndex.setStatus('current')
eoLldpPortNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 3), LldpPortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoLldpPortNumber.setStatus('current')
eoMgmtMacAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtMacAddress.setStatus('current')
eoMgmtAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtAddressType.setStatus('current')
eoMgmtAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtAddress.setStatus('current')
eoMgmtDNSName = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoMgmtDNSName.setStatus('current')
eoDomainName = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoDomainName.setStatus('current')
eoRoleDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoRoleDescription.setStatus('current')
eoKeywords = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 10), EnergyObjectKeywordList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoKeywords.setStatus('current')
eoImportance = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoImportance.setStatus('current')
eoPowerCategory = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("consumer", 0), ("producer", 1), ("meter", 2), ("distributor", 3), ("store", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoPowerCategory.setStatus('current')
eoAlternateKey = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 13), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eoAlternateKey.setStatus('current')
eoPowerInterfaceType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inlet", 0), ("outlet", 1), ("both", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eoPowerInterfaceType.setStatus('current')
eoRelationTable = MibTable((1, 3, 6, 1, 2, 1, 231, 1, 2), )
if mibBuilder.loadTexts: eoRelationTable.setStatus('current')
eoRelationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 231, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "ENERGY-OBJECT-CONTEXT-MIB", "eoRelationIndex"))
if mibBuilder.loadTexts: eoRelationEntry.setStatus('current')
eoRelationIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: eoRelationIndex.setStatus('current')
eoRelationID = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 2), UUIDorZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationID.setStatus('current')
eoRelationship = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 3), IANAEnergyRelationship()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationship.setStatus('current')
eoRelationStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationStatus.setStatus('current')
eoRelationStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 231, 1, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eoRelationStorageType.setStatus('current')
energyObjectContextMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2, 1))
energyObjectContextMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 231, 2, 2))
energyObjectContextMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 231, 2, 1, 1)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectContextMIBTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectRelationTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectOptionalMIBTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBFullCompliance = energyObjectContextMIBFullCompliance.setStatus('current')
energyObjectContextMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 231, 2, 1, 2)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectContextMIBTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectRelationTableGroup"), ("ENERGY-OBJECT-CONTEXT-MIB", "energyObjectOptionalMIBTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBReadOnlyCompliance = energyObjectContextMIBReadOnlyCompliance.setStatus('current')
energyObjectContextMIBTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 1)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoDomainName"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRoleDescription"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoAlternateKey"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoKeywords"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoImportance"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerCategory"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoPowerInterfaceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectContextMIBTableGroup = energyObjectContextMIBTableGroup.setStatus('current')
energyObjectOptionalMIBTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 2)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortIndex"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoEthPortGrpIndex"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoLldpPortNumber"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtMacAddress"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddressType"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtAddress"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoMgmtDNSName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectOptionalMIBTableGroup = energyObjectOptionalMIBTableGroup.setStatus('current')
energyObjectRelationTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 231, 2, 2, 3)).setObjects(("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationID"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationship"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStatus"), ("ENERGY-OBJECT-CONTEXT-MIB", "eoRelationStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    energyObjectRelationTableGroup = energyObjectRelationTableGroup.setStatus('current')
mibBuilder.exportSymbols("ENERGY-OBJECT-CONTEXT-MIB", eoEthPortGrpIndex=eoEthPortGrpIndex, eoLldpPortNumber=eoLldpPortNumber, PYSNMP_MODULE_ID=energyObjectContextMIB, eoRoleDescription=eoRoleDescription, eoRelationIndex=eoRelationIndex, eoImportance=eoImportance, energyObjectContextMIBGroups=energyObjectContextMIBGroups, energyObjectContextMIBTableGroup=energyObjectContextMIBTableGroup, PethPsePortGroupIndexOrZero=PethPsePortGroupIndexOrZero, eoRelationStorageType=eoRelationStorageType, energyObjectOptionalMIBTableGroup=energyObjectOptionalMIBTableGroup, energyObjectContextMIBCompliances=energyObjectContextMIBCompliances, PethPsePortIndexOrZero=PethPsePortIndexOrZero, eoRelationEntry=eoRelationEntry, eoPowerInterfaceType=eoPowerInterfaceType, eoRelationStatus=eoRelationStatus, eoTable=eoTable, energyObjectContextMIBFullCompliance=energyObjectContextMIBFullCompliance, eoRelationID=eoRelationID, energyObjectRelationTableGroup=energyObjectRelationTableGroup, energyObjectContextMIBConform=energyObjectContextMIBConform, eoEthPortIndex=eoEthPortIndex, eoMgmtDNSName=eoMgmtDNSName, eoPowerCategory=eoPowerCategory, eoMgmtMacAddress=eoMgmtMacAddress, energyObjectContextMIBObjects=energyObjectContextMIBObjects, eoRelationship=eoRelationship, EnergyObjectKeywordList=EnergyObjectKeywordList, eoMgmtAddress=eoMgmtAddress, eoRelationTable=eoRelationTable, eoKeywords=eoKeywords, energyObjectContextMIBNotifs=energyObjectContextMIBNotifs, energyObjectContextMIBReadOnlyCompliance=energyObjectContextMIBReadOnlyCompliance, LldpPortNumberOrZero=LldpPortNumberOrZero, eoMgmtAddressType=eoMgmtAddressType, eoDomainName=eoDomainName, eoAlternateKey=eoAlternateKey, eoEntry=eoEntry, energyObjectContextMIB=energyObjectContextMIB)
