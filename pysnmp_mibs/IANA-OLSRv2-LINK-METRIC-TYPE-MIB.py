#
# PySNMP MIB module IANA-OLSRv2-LINK-METRIC-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/IANA-OLSRv2-LINK-METRIC-TYPE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaolsrv2LinkMetricType = ModuleIdentity((1, 3, 6, 1, 2, 1, 221))
ianaolsrv2LinkMetricType.setRevisions(('2014-04-09 00:00',))
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setOrganization('IANA')
class IANAolsrv2LinkMetricTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("unknown", 0))

mibBuilder.exportSymbols("IANA-OLSRv2-LINK-METRIC-TYPE-MIB", IANAolsrv2LinkMetricTypeTC=IANAolsrv2LinkMetricTypeTC, ianaolsrv2LinkMetricType=ianaolsrv2LinkMetricType, PYSNMP_MODULE_ID=ianaolsrv2LinkMetricType)
