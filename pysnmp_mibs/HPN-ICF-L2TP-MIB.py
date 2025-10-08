#
# PySNMP MIB module HPN-ICF-L2TP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-L2TP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HPN-ICF-L2TP-MIB", hpnicfL2tpSessionRate=hpnicfL2tpSessionRate, PYSNMP_MODULE_ID=hpnicfL2tp, hpnicfL2tpStatsTotalTunnels=hpnicfL2tpStatsTotalTunnels, hpnicfL2tpStatsTotalSessions=hpnicfL2tpStatsTotalSessions, hpnicfL2tp=hpnicfL2tp, hpnicfL2tpScalar=hpnicfL2tpScalar, hpnicfL2tpObjects=hpnicfL2tpObjects, hpnicfL2tpStats=hpnicfL2tpStats)
