#
# PySNMP MIB module MARVELL-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/MARVELL-Dlf-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('200809151234Z')
if mibBuilder.loadTexts: rlDlf.setOrganization('MARVELL Semiconductor, Inc.')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 89, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
mibBuilder.exportSymbols("MARVELL-Dlf-MIB", rlDlfPortList=rlDlfPortList, PYSNMP_MODULE_ID=rlDlf, rlDlf=rlDlf)
