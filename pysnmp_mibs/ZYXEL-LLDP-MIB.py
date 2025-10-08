#
# PySNMP MIB module ZYXEL-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-LLDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43))
if mibBuilder.loadTexts: zyxelLldp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLldp.setOrganization('Enterprise Solution ZyXEL')
zyxelLldpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1))
zyxelLldpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2))
zyLldpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpState.setStatus('current')
zyLldpRemoteInfoClear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpRemoteInfoClear.setStatus('current')
zyLldpRemoteInfoClearPorts = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpRemoteInfoClearPorts.setStatus('current')
zyLldpStatisticsClear = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 43, 2, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLldpStatisticsClear.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-LLDP-MIB", zyxelLldp=zyxelLldp, zyxelLldpSetup=zyxelLldpSetup, zyxelLldpStatus=zyxelLldpStatus, zyLldpRemoteInfoClearPorts=zyLldpRemoteInfoClearPorts, zyLldpStatisticsClear=zyLldpStatisticsClear, zyLldpState=zyLldpState, zyLldpRemoteInfoClear=zyLldpRemoteInfoClear, PYSNMP_MODULE_ID=zyxelLldp)
