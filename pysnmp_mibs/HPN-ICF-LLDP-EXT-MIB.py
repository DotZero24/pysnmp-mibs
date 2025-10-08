#
# PySNMP MIB module HPN-ICF-LLDP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-LLDP-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
LldpPortNumber, = mibBuilder.importSymbols("LLDP-MIB", "LldpPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
hpnicflldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100))
hpnicflldp.setRevisions(('2009-03-21 00:00',))
if mibBuilder.loadTexts: hpnicflldp.setLastUpdated('200903210000Z')
if mibBuilder.loadTexts: hpnicflldp.setOrganization('')
hpnicflldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1))
hpnicflldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1))
hpnicflldpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicflldpAdminStatus.setStatus('current')
hpnicflldpComplianceCDPStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicflldpComplianceCDPStatus.setStatus('current')
hpnicflldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicflldpPortConfigTable.setStatus('current')
hpnicflldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-LLDP-EXT-MIB", "hpnicflldpPortConfigPortNum"))
if mibBuilder.loadTexts: hpnicflldpPortConfigEntry.setStatus('current')
hpnicflldpPortConfigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: hpnicflldpPortConfigPortNum.setStatus('current')
hpnicflldpPortConfigCDPComplianceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("txAndRx", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicflldpPortConfigCDPComplianceStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LLDP-EXT-MIB", hpnicflldpPortConfigTable=hpnicflldpPortConfigTable, hpnicflldpAdminStatus=hpnicflldpAdminStatus, PYSNMP_MODULE_ID=hpnicflldp, hpnicflldpPortConfigEntry=hpnicflldpPortConfigEntry, hpnicflldpComplianceCDPStatus=hpnicflldpComplianceCDPStatus, hpnicflldpPortConfigPortNum=hpnicflldpPortConfigPortNum, hpnicflldpPortConfigCDPComplianceStatus=hpnicflldpPortConfigCDPComplianceStatus, hpnicflldp=hpnicflldp, hpnicflldpObjects=hpnicflldpObjects, hpnicflldpConfiguration=hpnicflldpConfiguration)
