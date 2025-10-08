#
# PySNMP MIB module H3C-ARP-SOURCE-SUPPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
h3cARPSourceSuppression = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146))
h3cARPSourceSuppression.setRevisions(('2013-10-14 18:00',))
if mibBuilder.loadTexts: h3cARPSourceSuppression.setLastUpdated('201310141800Z')
if mibBuilder.loadTexts: h3cARPSourceSuppression.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cARPSourceSuppressionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1))
h3cARPSourceSuppressionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1))
h3cARPSourceSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cARPSourceSuppressionEnable.setStatus('current')
h3cARPSourceSuppressionLimit = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 1024)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cARPSourceSuppressionLimit.setStatus('current')
mibBuilder.exportSymbols("H3C-ARP-SOURCE-SUPPRESSION-MIB", h3cARPSourceSuppressionLimit=h3cARPSourceSuppressionLimit, h3cARPSourceSuppressionGlobal=h3cARPSourceSuppressionGlobal, h3cARPSourceSuppressionEnable=h3cARPSourceSuppressionEnable, h3cARPSourceSuppressionObjects=h3cARPSourceSuppressionObjects, PYSNMP_MODULE_ID=h3cARPSourceSuppression, h3cARPSourceSuppression=h3cARPSourceSuppression)
