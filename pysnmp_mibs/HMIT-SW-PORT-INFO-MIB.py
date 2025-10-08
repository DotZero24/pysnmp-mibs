#
# PySNMP MIB module HMIT-SW-PORT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HMIT-SW-PORT-INFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmITSwitchTech, = mibBuilder.importSymbols("HMIT-SMI", "hmITSwitchTech")
hmITSwPortmgrMIB, hmITSwPortMIB = mibBuilder.importSymbols("HMIT-SW-PORT-MGR-MIB", "hmITSwPortmgrMIB", "hmITSwPortMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmITPortInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 1))
hmITPortInfoMIB.setRevisions(('2010-01-08 17:00',))
if mibBuilder.loadTexts: hmITPortInfoMIB.setLastUpdated('201001081700Z')
if mibBuilder.loadTexts: hmITPortInfoMIB.setOrganization('Belden Singapore Pte Ltd.')
hmITMaxPortNumOfBoard = MibScalar((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmITMaxPortNumOfBoard.setStatus('current')
hmITStartPortId = MibScalar((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmITStartPortId.setStatus('current')
mibBuilder.exportSymbols("HMIT-SW-PORT-INFO-MIB", PYSNMP_MODULE_ID=hmITPortInfoMIB, hmITPortInfoMIB=hmITPortInfoMIB, hmITMaxPortNumOfBoard=hmITMaxPortNumOfBoard, hmITStartPortId=hmITStartPortId)
