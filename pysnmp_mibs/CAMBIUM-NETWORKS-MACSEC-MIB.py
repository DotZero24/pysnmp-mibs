#
# PySNMP MIB module CAMBIUM-NETWORKS-MACSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cambium/CAMBIUM-NETWORKS-MACSEC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
cnMacSecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 17713, 24, 10))
cnMacSecMib.setRevisions(('2021-11-28 00:00', '2021-06-04 00:00',))
if mibBuilder.loadTexts: cnMacSecMib.setLastUpdated('202111280000Z')
if mibBuilder.loadTexts: cnMacSecMib.setOrganization('Cambium Networks, Inc.')
class MacSecViolationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("protect", 1), ("restrict", 2), ("shutdown", 3))

cnMacSecPort = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1))
cnMacSecPortTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1), )
if mibBuilder.loadTexts: cnMacSecPortTable.setStatus('current')
cnMacSecPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1), ).setIndexNames((0, "CAMBIUM-NETWORKS-MACSEC-MIB", "cnMacSecPortIndex"))
if mibBuilder.loadTexts: cnMacSecPortEntry.setStatus('current')
cnMacSecPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 52)))
if mibBuilder.loadTexts: cnMacSecPortIndex.setStatus('current')
cnMacSecPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecPortStatus.setStatus('current')
cnMacSecPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 3), MacSecViolationMode().clone('protect')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecPortMode.setStatus('current')
cnMacSecPortMaxAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 4), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecPortMaxAddr.setStatus('current')
cnMacSecPortNumAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortNumAddr.setStatus('current')
cnMacSecPortNumViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortNumViolations.setStatus('current')
cnMacSecPortLastViolationAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortLastViolationAddr.setStatus('current')
cnMacSecPortLastViolationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 10, 1, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMacSecPortLastViolationTime.setStatus('current')
cnMacSecGlobalDebug = MibScalar((1, 3, 6, 1, 4, 1, 17713, 24, 10, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecGlobalDebug.setStatus('current')
cnMacSecDebugOption = MibScalar((1, 3, 6, 1, 4, 1, 17713, 24, 10, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMacSecDebugOption.setStatus('current')
mibBuilder.exportSymbols("CAMBIUM-NETWORKS-MACSEC-MIB", PYSNMP_MODULE_ID=cnMacSecMib, cnMacSecPortEntry=cnMacSecPortEntry, cnMacSecPortMaxAddr=cnMacSecPortMaxAddr, cnMacSecGlobalDebug=cnMacSecGlobalDebug, cnMacSecPortIndex=cnMacSecPortIndex, cnMacSecPortNumViolations=cnMacSecPortNumViolations, cnMacSecDebugOption=cnMacSecDebugOption, cnMacSecPortLastViolationTime=cnMacSecPortLastViolationTime, MacSecViolationMode=MacSecViolationMode, cnMacSecPortLastViolationAddr=cnMacSecPortLastViolationAddr, cnMacSecMib=cnMacSecMib, cnMacSecPort=cnMacSecPort, cnMacSecPortMode=cnMacSecPortMode, cnMacSecPortTable=cnMacSecPortTable, cnMacSecPortNumAddr=cnMacSecPortNumAddr, cnMacSecPortStatus=cnMacSecPortStatus)
