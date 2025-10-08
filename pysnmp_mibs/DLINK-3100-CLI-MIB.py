#
# PySNMP MIB module DLINK-3100-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINK-3100-CLI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlCli = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52))
rlCli.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlCli.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCli.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rlCliMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCliMibVersion.setStatus('current')
rlCliPassword = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliPassword.setStatus('current')
rlCliTimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliTimer.setStatus('current')
rlCliFileEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCliFileEnable.setStatus('current')
rlCliFileEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliFileEnableAfterReset.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-CLI-MIB", rlCli=rlCli, rlCliPassword=rlCliPassword, rlCliTimer=rlCliTimer, PYSNMP_MODULE_ID=rlCli, rlCliFileEnable=rlCliFileEnable, rlCliMibVersion=rlCliMibVersion, rlCliFileEnableAfterReset=rlCliFileEnableAfterReset)
