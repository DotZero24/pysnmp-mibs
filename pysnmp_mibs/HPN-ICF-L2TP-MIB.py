#
# PySNMP MIB module HPN-ICF-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-L2TP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfL2tp = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139))
hpnicfL2tp.setRevisions(('2013-07-05 15:18',))
if mibBuilder.loadTexts: hpnicfL2tp.setLastUpdated('201307051518Z')
if mibBuilder.loadTexts: hpnicfL2tp.setOrganization('')
hpnicfL2tpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1))
hpnicfL2tpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1))
hpnicfL2tpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1))
hpnicfL2tpStatsTotalTunnels = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalTunnels.setStatus('current')
hpnicfL2tpStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpStatsTotalSessions.setStatus('current')
hpnicfL2tpSessionRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfL2tpSessionRate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-L2TP-MIB", hpnicfL2tpObjects=hpnicfL2tpObjects, hpnicfL2tpScalar=hpnicfL2tpScalar, hpnicfL2tpSessionRate=hpnicfL2tpSessionRate, PYSNMP_MODULE_ID=hpnicfL2tp, hpnicfL2tpStatsTotalTunnels=hpnicfL2tpStatsTotalTunnels, hpnicfL2tpStatsTotalSessions=hpnicfL2tpStatsTotalSessions, hpnicfL2tp=hpnicfL2tp, hpnicfL2tpStats=hpnicfL2tpStats)
