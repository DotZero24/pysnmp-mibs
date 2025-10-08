#
# PySNMP MIB module HPN-ICF-LLDP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-LLDP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
LldpPortNumber, = mibBuilder.importSymbols("LLDP-MIB", "LldpPortNumber")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("HPN-ICF-LLDP-EXT-MIB", hpnicflldpPortConfigEntry=hpnicflldpPortConfigEntry, hpnicflldpAdminStatus=hpnicflldpAdminStatus, hpnicflldpConfiguration=hpnicflldpConfiguration, hpnicflldp=hpnicflldp, hpnicflldpPortConfigPortNum=hpnicflldpPortConfigPortNum, hpnicflldpPortConfigTable=hpnicflldpPortConfigTable, hpnicflldpComplianceCDPStatus=hpnicflldpComplianceCDPStatus, hpnicflldpObjects=hpnicflldpObjects, hpnicflldpPortConfigCDPComplianceStatus=hpnicflldpPortConfigCDPComplianceStatus, PYSNMP_MODULE_ID=hpnicflldp)
