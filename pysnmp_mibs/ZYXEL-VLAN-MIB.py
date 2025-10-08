#
# PySNMP MIB module ZYXEL-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-VLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:03:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86))
if mibBuilder.loadTexts: zyxelVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelVlan.setOrganization('Enterprise Solution ZyXEL')
zyxelVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1))
zyVlanType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot1Q", 1), ("portBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanType.setStatus('current')
zyVlanIngressCheckState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanIngressCheckState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-VLAN-MIB", zyVlanIngressCheckState=zyVlanIngressCheckState, zyxelVlanSetup=zyxelVlanSetup, PYSNMP_MODULE_ID=zyxelVlan, zyxelVlan=zyxelVlan, zyVlanType=zyVlanType)
