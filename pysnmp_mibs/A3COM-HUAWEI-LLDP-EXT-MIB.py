#
# PySNMP MIB module A3COM-HUAWEI-LLDP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-LLDP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
LldpPortNumber, = mibBuilder.importSymbols("LLDP-MIB", "LldpPortNumber")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
h3clldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100))
h3clldp.setRevisions(('2009-03-21 00:00',))
if mibBuilder.loadTexts: h3clldp.setLastUpdated('200903210000Z')
if mibBuilder.loadTexts: h3clldp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3clldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1))
h3clldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1))
h3clldpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3clldpAdminStatus.setStatus('current')
h3clldpComplianceCDPStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3clldpComplianceCDPStatus.setStatus('current')
h3clldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3), )
if mibBuilder.loadTexts: h3clldpPortConfigTable.setStatus('current')
h3clldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-LLDP-EXT-MIB", "h3clldpPortConfigPortNum"))
if mibBuilder.loadTexts: h3clldpPortConfigEntry.setStatus('current')
h3clldpPortConfigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: h3clldpPortConfigPortNum.setStatus('current')
h3clldpPortConfigCDPComplianceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("txAndRx", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3clldpPortConfigCDPComplianceStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-LLDP-EXT-MIB", h3clldpPortConfigPortNum=h3clldpPortConfigPortNum, PYSNMP_MODULE_ID=h3clldp, h3clldpPortConfigEntry=h3clldpPortConfigEntry, h3clldpPortConfigCDPComplianceStatus=h3clldpPortConfigCDPComplianceStatus, h3clldpAdminStatus=h3clldpAdminStatus, h3clldpObjects=h3clldpObjects, h3clldpComplianceCDPStatus=h3clldpComplianceCDPStatus, h3clldp=h3clldp, h3clldpConfiguration=h3clldpConfiguration, h3clldpPortConfigTable=h3clldpPortConfigTable)
