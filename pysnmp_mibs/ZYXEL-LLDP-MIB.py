#
# PySNMP MIB module ZYXEL-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-LLDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-LLDP-MIB", zyLldpRemoteInfoClearPorts=zyLldpRemoteInfoClearPorts, zyxelLldpSetup=zyxelLldpSetup, zyLldpStatisticsClear=zyLldpStatisticsClear, zyLldpRemoteInfoClear=zyLldpRemoteInfoClear, zyLldpState=zyLldpState, PYSNMP_MODULE_ID=zyxelLldp, zyxelLldp=zyxelLldp, zyxelLldpStatus=zyxelLldpStatus)
