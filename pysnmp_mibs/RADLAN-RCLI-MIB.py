#
# PySNMP MIB module RADLAN-RCLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/RADLAN-RCLI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlRCli = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 70))
rlRCli.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlRCli.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlRCli.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlRCliMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 70, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRCliMibVersion.setStatus('current')
rlRCliUserPassword = MibScalar((1, 3, 6, 1, 4, 1, 89, 70, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRCliUserPassword.setStatus('current')
rlRCliEnablePassword = MibScalar((1, 3, 6, 1, 4, 1, 89, 70, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRCliEnablePassword.setStatus('current')
rlRCliConfigPassword = MibScalar((1, 3, 6, 1, 4, 1, 89, 70, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRCliConfigPassword.setStatus('current')
rlRCliTimer = MibScalar((1, 3, 6, 1, 4, 1, 89, 70, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRCliTimer.setStatus('current')
rlRcliFileAction = MibScalar((1, 3, 6, 1, 4, 1, 89, 70, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notUsedAfterReset", 1), ("usedAfterReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRcliFileAction.setStatus('current')
mibBuilder.exportSymbols("RADLAN-RCLI-MIB", PYSNMP_MODULE_ID=rlRCli, rlRCliUserPassword=rlRCliUserPassword, rlRcliFileAction=rlRcliFileAction, rlRCliTimer=rlRCliTimer, rlRCliEnablePassword=rlRCliEnablePassword, rlRCliMibVersion=rlRCliMibVersion, rlRCliConfigPassword=rlRCliConfigPassword, rlRCli=rlRCli)
