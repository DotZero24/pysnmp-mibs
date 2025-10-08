#
# PySNMP MIB module CISCO-ATM-SERVICE-REGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ATM-SERVICE-REGISTRY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoAtmServiceRegistryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 50))
ciscoAtmServiceRegistryMIB.setRevisions(('1996-02-04 00:00',))
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setLastUpdated('9602210000Z')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setOrganization('Cisco Systems, Inc.')
ciscoAtmServiceRegistryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 1))
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

asrSrvcRegTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1), )
if mibBuilder.loadTexts: asrSrvcRegTable.setStatus('current')
asrSrvcRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1), ).setIndexNames((0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegPort"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegServiceID"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegAddressIndex"))
if mibBuilder.loadTexts: asrSrvcRegEntry.setStatus('current')
asrSrvcRegPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: asrSrvcRegPort.setStatus('current')
asrSrvcRegServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: asrSrvcRegServiceID.setStatus('current')
asrSrvcRegATMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 3), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegATMAddress.setStatus('current')
asrSrvcRegAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: asrSrvcRegAddressIndex.setStatus('current')
asrSrvcRegParm1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegParm1.setStatus('current')
asrSrvcRegRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegRowStatus.setStatus('current')
asrSrvcRegMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3))
asrSrvcRegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1))
asrSrvcRegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2))
asrSrvcRegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBCompliance = asrSrvcRegMIBCompliance.setStatus('current')
asrSrvcRegMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegATMAddress"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegParm1"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBGroup = asrSrvcRegMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-SERVICE-REGISTRY-MIB", InterfaceIndexOrZero=InterfaceIndexOrZero, asrSrvcRegMIBCompliance=asrSrvcRegMIBCompliance, asrSrvcRegTable=asrSrvcRegTable, asrSrvcRegEntry=asrSrvcRegEntry, asrSrvcRegATMAddress=asrSrvcRegATMAddress, asrSrvcRegRowStatus=asrSrvcRegRowStatus, asrSrvcRegMIBGroups=asrSrvcRegMIBGroups, asrSrvcRegServiceID=asrSrvcRegServiceID, asrSrvcRegParm1=asrSrvcRegParm1, ciscoAtmServiceRegistryMIBObjects=ciscoAtmServiceRegistryMIBObjects, asrSrvcRegPort=asrSrvcRegPort, asrSrvcRegMIBConformance=asrSrvcRegMIBConformance, AtmAddr=AtmAddr, PYSNMP_MODULE_ID=ciscoAtmServiceRegistryMIB, asrSrvcRegAddressIndex=asrSrvcRegAddressIndex, asrSrvcRegMIBCompliances=asrSrvcRegMIBCompliances, asrSrvcRegMIBGroup=asrSrvcRegMIBGroup, ciscoAtmServiceRegistryMIB=ciscoAtmServiceRegistryMIB)
