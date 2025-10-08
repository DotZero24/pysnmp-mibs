#
# PySNMP MIB module ARUBA-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/ARUBA-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
arubaMgmt, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMgmt")
ArubaEnableValue, = mibBuilder.importSymbols("ARUBA-TC", "ArubaEnableValue")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, snmpModules, Gauge32, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "snmpModules", "Gauge32", "ObjectName")
TextualConvention, TestAndIncr, PhysAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TestAndIncr", "PhysAddress", "TruthValue", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("ARUBA-MGMT-MIB", arubaNumberOfColumns=arubaNumberOfColumns, arubaRowInstance=arubaRowInstance, arubaNumberOfRows=arubaNumberOfRows, arubaSwitchAMPSupport=arubaSwitchAMPSupport, arubaMgmtGroup=arubaMgmtGroup, arubaGetTableStatus=arubaGetTableStatus, arubaMgmtExtensions=arubaMgmtExtensions, arubaGetTable=arubaGetTable, PYSNMP_MODULE_ID=arubaMgmtExtensions)
