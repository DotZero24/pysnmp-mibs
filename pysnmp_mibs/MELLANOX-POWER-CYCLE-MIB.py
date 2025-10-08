#
# PySNMP MIB module MELLANOX-POWER-CYCLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mellanox/MELLANOX-POWER-CYCLE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mellanoxPowerCycle, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxPowerCycle")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MELLANOX-POWER-CYCLE-MIB", mellanoxPowerCycleMib=mellanoxPowerCycleMib, mellanoxPowerCycleMibObjects=mellanoxPowerCycleMibObjects, PYSNMP_MODULE_ID=mellanoxPowerCycleMib, mellanoxPowerCycleCmdStatus=mellanoxPowerCycleCmdStatus, mellanoxPowerCycleCmdExecute=mellanoxPowerCycleCmdExecute, mellanoxPowerCycleCmdStatusString=mellanoxPowerCycleCmdStatusString, mellanoxPowerCyclePlannedReload=mellanoxPowerCyclePlannedReload, mellanoxPowerCycleCmd=mellanoxPowerCycleCmd, mellanoxPowerCycleNotifications=mellanoxPowerCycleNotifications)
