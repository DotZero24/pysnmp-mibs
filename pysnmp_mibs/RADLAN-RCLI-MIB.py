#
# PySNMP MIB module RADLAN-RCLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/RADLAN-RCLI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RADLAN-RCLI-MIB", rlRCliUserPassword=rlRCliUserPassword, rlRCliConfigPassword=rlRCliConfigPassword, rlRCliEnablePassword=rlRCliEnablePassword, rlRCli=rlRCli, rlRCliTimer=rlRCliTimer, rlRcliFileAction=rlRcliFileAction, rlRCliMibVersion=rlRCliMibVersion, PYSNMP_MODULE_ID=rlRCli)
