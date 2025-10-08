#
# PySNMP MIB module H3C-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-L2TP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("H3C-L2TP-MIB", h3cL2tp=h3cL2tp, h3cL2tpStatsTotalSessions=h3cL2tpStatsTotalSessions, h3cL2tpScalar=h3cL2tpScalar, PYSNMP_MODULE_ID=h3cL2tp, h3cL2tpSessionRate=h3cL2tpSessionRate, h3cL2tpObjects=h3cL2tpObjects, h3cL2tpStats=h3cL2tpStats, h3cL2tpStatsTotalTunnels=h3cL2tpStatsTotalTunnels)
