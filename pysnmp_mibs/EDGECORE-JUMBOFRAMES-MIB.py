#
# PySNMP MIB module EDGECORE-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/edgecore/EDGECORE-JUMBOFRAMES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("EDGECORE-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
mibBuilder.exportSymbols("EDGECORE-JUMBOFRAMES-MIB", PYSNMP_MODULE_ID=rlJumboFrames, rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset, rlJumboFrames=rlJumboFrames, rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus)
