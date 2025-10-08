#
# PySNMP MIB module CASA-CABLE-CMQUERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/casa/CASA-CABLE-CMQUERY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, TimeInterval, MacAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeInterval", "MacAddress", "TruthValue", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("CASA-CABLE-CMQUERY-MIB", casaCmQueryGroups=casaCmQueryGroups, PYSNMP_MODULE_ID=casaCmQueryMib, casaCmQueryMib=casaCmQueryMib, casaQueryCmSigQSignalNoise=casaQueryCmSigQSignalNoise, casaCmQueryCompliance=casaCmQueryCompliance, casaQueryCmTxTimeOffset=casaQueryCmTxTimeOffset, casaQueryCmStatusRxPower=casaQueryCmStatusRxPower, casaCmQueryTable=casaCmQueryTable, TenthdB=TenthdB, casaCmQueryCompliances=casaCmQueryCompliances, casaQueryCmMacAddress=casaQueryCmMacAddress, TenthdBmV=TenthdBmV, casaCmQueryEntry=casaCmQueryEntry, casaQueryCmMicroReflection=casaQueryCmMicroReflection, casaQueryCmStatusTxPower=casaQueryCmStatusTxPower, casaQueryCmtsSigQSignalNoise=casaQueryCmtsSigQSignalNoise, casaQueryCmIpAddress=casaQueryCmIpAddress, casaMgmt=casaMgmt, casaCmQueryroup=casaCmQueryroup, casaCmQueryMibObjects=casaCmQueryMibObjects)
