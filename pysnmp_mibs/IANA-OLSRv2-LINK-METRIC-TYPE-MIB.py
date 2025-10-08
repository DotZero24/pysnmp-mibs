#
# PySNMP MIB module IANA-OLSRv2-LINK-METRIC-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/IANA-OLSRv2-LINK-METRIC-TYPE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaolsrv2LinkMetricType = ModuleIdentity((1, 3, 6, 1, 2, 1, 221))
ianaolsrv2LinkMetricType.setRevisions(('2014-04-09 00:00',))
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: ianaolsrv2LinkMetricType.setOrganization('IANA')
class IANAolsrv2LinkMetricTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("unknown", 0))

mibBuilder.exportSymbols("IANA-OLSRv2-LINK-METRIC-TYPE-MIB", IANAolsrv2LinkMetricTypeTC=IANAolsrv2LinkMetricTypeTC, PYSNMP_MODULE_ID=ianaolsrv2LinkMetricType, ianaolsrv2LinkMetricType=ianaolsrv2LinkMetricType)
