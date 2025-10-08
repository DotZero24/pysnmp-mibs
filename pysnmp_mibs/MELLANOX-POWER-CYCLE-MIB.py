#
# PySNMP MIB module MELLANOX-POWER-CYCLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mellanox/MELLANOX-POWER-CYCLE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mellanoxPowerCycle, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxPowerCycle")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mellanoxPowerCycleMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 33049, 10, 1))
mellanoxPowerCycleMib.setRevisions(('2018-06-04 00:00',))
if mibBuilder.loadTexts: mellanoxPowerCycleMib.setLastUpdated('201806040000Z')
if mibBuilder.loadTexts: mellanoxPowerCycleMib.setOrganization('Mellanox Technologies, Inc.')
mellanoxPowerCycleMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 33049, 10, 1, 1))
mellanoxPowerCycleCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2))
mellanoxPowerCycleNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 3))
mellanoxPowerCycleCmdExecute = MibScalar((1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("mellanoxPowerCycleCmdExecuteReload", 1), ("mellanoxPowerCycleCmdExecuteReloadDiscard", 2), ("mellanoxPowerCycleCmdExecuteReloadForce", 3), ("mellanoxPowerCycleCmdExecuteReloadSlave", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mellanoxPowerCycleCmdExecute.setStatus('current')
mellanoxPowerCycleCmdStatus = MibScalar((1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxPowerCycleCmdStatus.setStatus('current')
mellanoxPowerCycleCmdStatusString = MibScalar((1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxPowerCycleCmdStatusString.setStatus('current')
mellanoxPowerCyclePlannedReload = NotificationType((1, 3, 6, 1, 4, 1, 33049, 10, 1, 1, 3, 1))
if mibBuilder.loadTexts: mellanoxPowerCyclePlannedReload.setStatus('current')
mibBuilder.exportSymbols("MELLANOX-POWER-CYCLE-MIB", mellanoxPowerCycleCmdStatusString=mellanoxPowerCycleCmdStatusString, mellanoxPowerCycleNotifications=mellanoxPowerCycleNotifications, mellanoxPowerCycleMibObjects=mellanoxPowerCycleMibObjects, PYSNMP_MODULE_ID=mellanoxPowerCycleMib, mellanoxPowerCycleMib=mellanoxPowerCycleMib, mellanoxPowerCyclePlannedReload=mellanoxPowerCyclePlannedReload, mellanoxPowerCycleCmdExecute=mellanoxPowerCycleCmdExecute, mellanoxPowerCycleCmdStatus=mellanoxPowerCycleCmdStatus, mellanoxPowerCycleCmd=mellanoxPowerCycleCmd)
