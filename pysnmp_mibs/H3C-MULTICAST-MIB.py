#
# PySNMP MIB module H3C-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 50))
h3cMulticast.setRevisions(('2005-04-29 00:00',))
if mibBuilder.loadTexts: h3cMulticast.setLastUpdated('200504290000Z')
if mibBuilder.loadTexts: h3cMulticast.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

h3cMulticastObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 50, 1))
h3cMulticastEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 50, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMulticastEnable.setStatus('current')
mibBuilder.exportSymbols("H3C-MULTICAST-MIB", EnabledStatus=EnabledStatus, PYSNMP_MODULE_ID=h3cMulticast, h3cMulticastObject=h3cMulticastObject, h3cMulticastEnable=h3cMulticastEnable, h3cMulticast=h3cMulticast)
