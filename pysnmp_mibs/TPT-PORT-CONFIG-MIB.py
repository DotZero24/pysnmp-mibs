#
# PySNMP MIB module TPT-PORT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trendmicro/TPT-PORT-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_port_config_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4)).setLabel("tpt-port-config-objs")
tpt_port_config_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_port_config_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_port_config_objs.setOrganization('Trend Micro, Inc.')
class LineSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("default", 0), ("gigabit", 1), ("hundred-megabit", 2), ("ten-megabit", 3), ("ten-gigabit", 4), ("fourty-gigabit", 5))

class DuplexSetting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("default", 0), ("half", 1), ("full", 2))

class AutoNegotiation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("default", 0), ("on", 1), ("off", 2))

class EnabledOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class FailoverAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("block", 0), ("permit", 1))

class LinkDownMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("hub", 0), ("breaker", 1), ("wire", 2))

portConfigTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1), )
if mibBuilder.loadTexts: portConfigTable.setStatus('current')
portConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1), ).setIndexNames((0, "TPT-PORT-CONFIG-MIB", "portConfigSlot"), (0, "TPT-PORT-CONFIG-MIB", "portConfigPort"))
if mibBuilder.loadTexts: portConfigEntry.setStatus('current')
portConfigSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigSlot.setStatus('current')
portConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigPort.setStatus('current')
portConfigLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 3), LineSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLineSpeed.setStatus('current')
portConfigDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 4), DuplexSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigDuplex.setStatus('current')
portConfigAutoNeg = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 5), AutoNegotiation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigAutoNeg.setStatus('current')
portConfigShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 6), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigShutdown.setStatus('current')
portConfigLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 7), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLoopback.setStatus('current')
portConfigFailover = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 8), FailoverAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigFailover.setStatus('current')
portConfigLDSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 9), LinkDownMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLDSMode.setStatus('current')
portConfigLDSTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLDSTimeout.setStatus('current')
mibBuilder.exportSymbols("TPT-PORT-CONFIG-MIB", portConfigSlot=portConfigSlot, portConfigLDSTimeout=portConfigLDSTimeout, LinkDownMode=LinkDownMode, DuplexSetting=DuplexSetting, portConfigLoopback=portConfigLoopback, portConfigEntry=portConfigEntry, PYSNMP_MODULE_ID=tpt_port_config_objs, LineSpeed=LineSpeed, portConfigFailover=portConfigFailover, portConfigTable=portConfigTable, portConfigAutoNeg=portConfigAutoNeg, portConfigShutdown=portConfigShutdown, portConfigLineSpeed=portConfigLineSpeed, portConfigDuplex=portConfigDuplex, AutoNegotiation=AutoNegotiation, FailoverAction=FailoverAction, tpt_port_config_objs=tpt_port_config_objs, EnabledOrNot=EnabledOrNot, portConfigPort=portConfigPort, portConfigLDSMode=portConfigLDSMode)
