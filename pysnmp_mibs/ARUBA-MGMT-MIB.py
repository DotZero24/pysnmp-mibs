#
# PySNMP MIB module ARUBA-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/ARUBA-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
arubaMgmt, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMgmt")
ArubaEnableValue, = mibBuilder.importSymbols("ARUBA-TC", "ArubaEnableValue")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, snmpModules, iso, MibIdentifier, ObjectName, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "snmpModules", "iso", "MibIdentifier", "ObjectName", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, TestAndIncr, PhysAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TestAndIncr", "PhysAddress", "TruthValue", "TextualConvention")
arubaMgmtExtensions = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 3, 3))
if mibBuilder.loadTexts: arubaMgmtExtensions.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: arubaMgmtExtensions.setOrganization('Aruba, a Hewlett Packard Enterprise company')
arubaMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1))
arubaGetTable = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: arubaGetTable.setStatus('current')
arubaNumberOfRows = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: arubaNumberOfRows.setStatus('current')
arubaRowInstance = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 3), ObjectIdentifier())
if mibBuilder.loadTexts: arubaRowInstance.setStatus('current')
arubaGetTableStatus = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("endTable", 1), ("moreTable", 2), ("retrieveError", 3), ("noAmpSupport", 4), ("invalidColumnID", 5), ("resourceAllocationFailure", 6))))
if mibBuilder.loadTexts: arubaGetTableStatus.setStatus('current')
arubaNumberOfColumns = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: arubaNumberOfColumns.setStatus('current')
arubaSwitchAMPSupport = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 6), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaSwitchAMPSupport.setStatus('current')
mibBuilder.exportSymbols("ARUBA-MGMT-MIB", arubaMgmtGroup=arubaMgmtGroup, arubaMgmtExtensions=arubaMgmtExtensions, arubaNumberOfRows=arubaNumberOfRows, arubaNumberOfColumns=arubaNumberOfColumns, PYSNMP_MODULE_ID=arubaMgmtExtensions, arubaRowInstance=arubaRowInstance, arubaGetTable=arubaGetTable, arubaGetTableStatus=arubaGetTableStatus, arubaSwitchAMPSupport=arubaSwitchAMPSupport)
