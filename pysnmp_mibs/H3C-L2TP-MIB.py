#
# PySNMP MIB module H3C-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-L2TP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:55 2025
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
h3cL2tp = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 139))
h3cL2tp.setRevisions(('2013-07-05 15:18',))
if mibBuilder.loadTexts: h3cL2tp.setLastUpdated('201307051518Z')
if mibBuilder.loadTexts: h3cL2tp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cL2tpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 139, 1))
h3cL2tpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 139, 1, 1))
h3cL2tpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 139, 1, 1, 1))
h3cL2tpStatsTotalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 139, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL2tpStatsTotalTunnels.setStatus('current')
h3cL2tpStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 139, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL2tpStatsTotalSessions.setStatus('current')
h3cL2tpSessionRate = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 139, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cL2tpSessionRate.setStatus('current')
mibBuilder.exportSymbols("H3C-L2TP-MIB", h3cL2tpStats=h3cL2tpStats, h3cL2tpStatsTotalTunnels=h3cL2tpStatsTotalTunnels, h3cL2tpStatsTotalSessions=h3cL2tpStatsTotalSessions, h3cL2tpSessionRate=h3cL2tpSessionRate, h3cL2tpObjects=h3cL2tpObjects, h3cL2tpScalar=h3cL2tpScalar, h3cL2tp=h3cL2tp, PYSNMP_MODULE_ID=h3cL2tp)
