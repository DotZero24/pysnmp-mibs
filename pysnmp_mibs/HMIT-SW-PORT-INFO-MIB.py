#
# PySNMP MIB module HMIT-SW-PORT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HMIT-SW-PORT-INFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmITSwitchTech, = mibBuilder.importSymbols("HMIT-SMI", "hmITSwitchTech")
hmITSwPortmgrMIB, hmITSwPortMIB = mibBuilder.importSymbols("HMIT-SW-PORT-MGR-MIB", "hmITSwPortmgrMIB", "hmITSwPortMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmITPortInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 1))
hmITPortInfoMIB.setRevisions(('2010-01-08 17:00',))
if mibBuilder.loadTexts: hmITPortInfoMIB.setLastUpdated('201001081700Z')
if mibBuilder.loadTexts: hmITPortInfoMIB.setOrganization('Belden Singapore Pte Ltd.')
hmITMaxPortNumOfBoard = MibScalar((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmITMaxPortNumOfBoard.setStatus('current')
hmITStartPortId = MibScalar((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmITStartPortId.setStatus('current')
mibBuilder.exportSymbols("HMIT-SW-PORT-INFO-MIB", hmITPortInfoMIB=hmITPortInfoMIB, hmITMaxPortNumOfBoard=hmITMaxPortNumOfBoard, hmITStartPortId=hmITStartPortId, PYSNMP_MODULE_ID=hmITPortInfoMIB)
