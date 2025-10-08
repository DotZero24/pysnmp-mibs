#
# PySNMP MIB module DLINK-3100-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINK-3100-CLI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINK-3100-CLI-MIB", rlCli=rlCli, rlCliFileEnable=rlCliFileEnable, PYSNMP_MODULE_ID=rlCli, rlCliFileEnableAfterReset=rlCliFileEnableAfterReset, rlCliTimer=rlCliTimer, rlCliMibVersion=rlCliMibVersion, rlCliPassword=rlCliPassword)
