#
# PySNMP MIB module ZYXEL-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-VLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelVlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86))
if mibBuilder.loadTexts: zyxelVlan.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelVlan.setOrganization('Enterprise Solution ZyXEL')
zyxelVlanSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1))
zyVlanType = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dot1Q", 1), ("portBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanType.setStatus('current')
zyVlanIngressCheckState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanIngressCheckState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-VLAN-MIB", PYSNMP_MODULE_ID=zyxelVlan, zyxelVlan=zyxelVlan, zyVlanType=zyVlanType, zyVlanIngressCheckState=zyVlanIngressCheckState, zyxelVlanSetup=zyxelVlanSetup)
