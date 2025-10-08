#
# PySNMP MIB module TPT-PORT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-PORT-CONFIG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("TPT-PORT-CONFIG-MIB", PYSNMP_MODULE_ID=tpt_port_config_objs, portConfigLineSpeed=portConfigLineSpeed, FailoverAction=FailoverAction, portConfigFailover=portConfigFailover, DuplexSetting=DuplexSetting, portConfigLDSMode=portConfigLDSMode, portConfigShutdown=portConfigShutdown, portConfigLoopback=portConfigLoopback, portConfigLDSTimeout=portConfigLDSTimeout, AutoNegotiation=AutoNegotiation, portConfigTable=portConfigTable, LineSpeed=LineSpeed, portConfigDuplex=portConfigDuplex, portConfigPort=portConfigPort, LinkDownMode=LinkDownMode, portConfigEntry=portConfigEntry, tpt_port_config_objs=tpt_port_config_objs, portConfigAutoNeg=portConfigAutoNeg, EnabledOrNot=EnabledOrNot, portConfigSlot=portConfigSlot)
