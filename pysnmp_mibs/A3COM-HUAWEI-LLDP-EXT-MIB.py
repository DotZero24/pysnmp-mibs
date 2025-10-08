#
# PySNMP MIB module A3COM-HUAWEI-LLDP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-LLDP-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
LldpPortNumber, = mibBuilder.importSymbols("LLDP-MIB", "LldpPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("A3COM-HUAWEI-LLDP-EXT-MIB", h3clldpComplianceCDPStatus=h3clldpComplianceCDPStatus, h3clldpConfiguration=h3clldpConfiguration, h3clldpPortConfigTable=h3clldpPortConfigTable, h3clldp=h3clldp, h3clldpObjects=h3clldpObjects, h3clldpAdminStatus=h3clldpAdminStatus, h3clldpPortConfigCDPComplianceStatus=h3clldpPortConfigCDPComplianceStatus, PYSNMP_MODULE_ID=h3clldp, h3clldpPortConfigEntry=h3clldpPortConfigEntry, h3clldpPortConfigPortNum=h3clldpPortConfigPortNum)
