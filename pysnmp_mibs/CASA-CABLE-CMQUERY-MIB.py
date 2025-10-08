#
# PySNMP MIB module CASA-CABLE-CMQUERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/casa/CASA-CABLE-CMQUERY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeInterval, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeInterval", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
casaCmQueryMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 10, 18))
if mibBuilder.loadTexts: casaCmQueryMib.setLastUpdated('200809051453Z')
if mibBuilder.loadTexts: casaCmQueryMib.setOrganization('Casa Systems Inc')
class TenthdBmV(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class TenthdB(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

casaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10))
casaCmQueryMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1))
casaCmQueryTable = MibTable((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1), )
if mibBuilder.loadTexts: casaCmQueryTable.setStatus('current')
casaCmQueryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1), ).setIndexNames((0, "CASA-CABLE-CMQUERY-MIB", "casaQueryCmMacAddress"))
if mibBuilder.loadTexts: casaCmQueryEntry.setStatus('current')
casaQueryCmMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: casaQueryCmMacAddress.setStatus('current')
casaQueryCmIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmIpAddress.setStatus('current')
casaQueryCmTxTimeOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmTxTimeOffset.setStatus('current')
casaQueryCmMicroReflection = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('dBc').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmMicroReflection.setStatus('current')
casaQueryCmStatusTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 5), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmStatusTxPower.setStatus('current')
casaQueryCmStatusRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 6), TenthdBmV()).setUnits('dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmStatusRxPower.setStatus('current')
casaQueryCmSigQSignalNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 7), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmSigQSignalNoise.setStatus('current')
casaQueryCmtsSigQSignalNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 18, 1, 1, 1, 8), TenthdB()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaQueryCmtsSigQSignalNoise.setStatus('current')
casaCmQueryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 2))
casaCmQueryroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20858, 10, 18, 2, 1)).setObjects(("CASA-CABLE-CMQUERY-MIB", "casaQueryCmIpAddress"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmTxTimeOffset"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmMicroReflection"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusTxPower"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmStatusRxPower"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmSigQSignalNoise"), ("CASA-CABLE-CMQUERY-MIB", "casaQueryCmtsSigQSignalNoise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmQueryroup = casaCmQueryroup.setStatus('current')
casaCmQueryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 18, 3))
casaCmQueryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 20858, 10, 18, 3, 1)).setObjects(("CASA-CABLE-CMQUERY-MIB", "casaCmQueryroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmQueryCompliance = casaCmQueryCompliance.setStatus('current')
mibBuilder.exportSymbols("CASA-CABLE-CMQUERY-MIB", casaQueryCmMacAddress=casaQueryCmMacAddress, TenthdB=TenthdB, casaCmQueryCompliances=casaCmQueryCompliances, casaQueryCmSigQSignalNoise=casaQueryCmSigQSignalNoise, casaCmQueryroup=casaCmQueryroup, casaCmQueryEntry=casaCmQueryEntry, casaCmQueryCompliance=casaCmQueryCompliance, casaCmQueryTable=casaCmQueryTable, PYSNMP_MODULE_ID=casaCmQueryMib, casaQueryCmIpAddress=casaQueryCmIpAddress, TenthdBmV=TenthdBmV, casaQueryCmMicroReflection=casaQueryCmMicroReflection, casaQueryCmTxTimeOffset=casaQueryCmTxTimeOffset, casaCmQueryGroups=casaCmQueryGroups, casaQueryCmtsSigQSignalNoise=casaQueryCmtsSigQSignalNoise, casaCmQueryMib=casaCmQueryMib, casaQueryCmStatusRxPower=casaQueryCmStatusRxPower, casaCmQueryMibObjects=casaCmQueryMibObjects, casaQueryCmStatusTxPower=casaQueryCmStatusTxPower, casaMgmt=casaMgmt)
