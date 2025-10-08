#
# PySNMP MIB module LUM-OXC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-OXC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumOxcMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumOxcMIB", "lumModules")
PortNumber, FaultStatus, PortType, MgmtNameString, ObjectProperty, SlotNumber, SubrackNumber = mibBuilder.importSymbols("LUM-TC", "PortNumber", "FaultStatus", "PortType", "MgmtNameString", "ObjectProperty", "SlotNumber", "SubrackNumber")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TestAndIncr, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TestAndIncr", "DisplayString")
lumOxcMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 11))
lumOxcMIBModule.setRevisions(('2017-06-15 00:00', '2016-01-11 00:00', '2008-05-12 00:00', '2002-03-26 00:00', '2001-12-11 00:00', '2001-10-30 00:00', '2001-10-11 00:00', '2001-09-04 00:00', '2001-08-24 00:00',))
if mibBuilder.loadTexts: lumOxcMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumOxcMIBModule.setOrganization('Infinera Corporation')
lumOxcConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1))
lumOxcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1))
lumOxcCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2))
lumOxcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2))
oxcGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1))
oxcIfList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2))
oxcConfList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3))
oxcGeneralTestAndIncr = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcGeneralTestAndIncr.setStatus('current')
oxcGeneralMibSpecVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcGeneralMibSpecVersion.setStatus('current')
oxcGeneralMibImplVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcGeneralMibImplVersion.setStatus('current')
oxcGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcGeneralLastChangeTime.setStatus('current')
oxcGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcGeneralStateLastChangeTime.setStatus('current')
oxcGeneralOxcIfTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcGeneralOxcIfTableSize.setStatus('current')
oxcGeneralOxcConfTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcGeneralOxcConfTableSize.setStatus('current')
oxcIfTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1), )
if mibBuilder.loadTexts: oxcIfTable.setStatus('current')
oxcIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1), ).setIndexNames((0, "LUM-OXC-MIB", "oxcIfIndex"))
if mibBuilder.loadTexts: oxcIfEntry.setStatus('current')
oxcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfIndex.setStatus('current')
oxcIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfName.setStatus('current')
oxcIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcIfDescr.setStatus('current')
oxcIfSubrack = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 4), SubrackNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfSubrack.setStatus('current')
oxcIfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 5), SlotNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfSlot.setStatus('current')
oxcIfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 6), PortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfPort.setStatus('current')
oxcIfInvPhysIndexOrZero = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfInvPhysIndexOrZero.setStatus('current')
oxcIfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 8), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfDirection.setStatus('current')
oxcIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("down", 1), ("up", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcIfAdminStatus.setStatus('deprecated')
oxcIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notPresent", 1), ("down", 2), ("up", 3))).clone('notPresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfOperStatus.setStatus('current')
oxcIfIsReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oxcIfIsReserved.setStatus('current')
oxcIfObjectProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 2, 1, 1, 12), ObjectProperty()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcIfObjectProperty.setStatus('current')
oxcConfTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1), )
if mibBuilder.loadTexts: oxcConfTable.setStatus('current')
oxcConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1), ).setIndexNames((0, "LUM-OXC-MIB", "oxcConfIndex"))
if mibBuilder.loadTexts: oxcConfEntry.setStatus('current')
oxcConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfIndex.setStatus('current')
oxcConfName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfName.setStatus('current')
oxcConfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcConfDescr.setStatus('current')
oxcConfSubrack = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 4), SubrackNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfSubrack.setStatus('current')
oxcConfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 5), SlotNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfSlot.setStatus('current')
oxcConfInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 6), PortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfInPort.setStatus('current')
oxcConfOutPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 7), PortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcConfOutPort.setStatus('current')
oxcConfLastChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfLastChangeTime.setStatus('current')
oxcConfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oxcConfAdminStatus.setStatus('current')
oxcConfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfOperStatus.setStatus('deprecated')
oxcConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oxcConfRowStatus.setStatus('deprecated')
oxcConfServiceFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 12), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfServiceFailure.setStatus('current')
oxcConfObjectProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 10, 2, 3, 1, 1, 13), ObjectProperty()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oxcConfObjectProperty.setStatus('current')
oxcGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 1)).setObjects(("LUM-OXC-MIB", "oxcGeneralTestAndIncr"), ("LUM-OXC-MIB", "oxcGeneralMibSpecVersion"), ("LUM-OXC-MIB", "oxcGeneralMibImplVersion"), ("LUM-OXC-MIB", "oxcGeneralLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcGeneralGroup = oxcGeneralGroup.setStatus('deprecated')
oxcIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 2)).setObjects(("LUM-OXC-MIB", "oxcIfIndex"), ("LUM-OXC-MIB", "oxcIfName"), ("LUM-OXC-MIB", "oxcIfDescr"), ("LUM-OXC-MIB", "oxcIfSubrack"), ("LUM-OXC-MIB", "oxcIfSlot"), ("LUM-OXC-MIB", "oxcIfPort"), ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"), ("LUM-OXC-MIB", "oxcIfDirection"), ("LUM-OXC-MIB", "oxcIfAdminStatus"), ("LUM-OXC-MIB", "oxcIfOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcIfGroup = oxcIfGroup.setStatus('deprecated')
oxcConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 3)).setObjects(("LUM-OXC-MIB", "oxcConfIndex"), ("LUM-OXC-MIB", "oxcConfName"), ("LUM-OXC-MIB", "oxcConfDescr"), ("LUM-OXC-MIB", "oxcConfSubrack"), ("LUM-OXC-MIB", "oxcConfSlot"), ("LUM-OXC-MIB", "oxcConfInPort"), ("LUM-OXC-MIB", "oxcConfOutPort"), ("LUM-OXC-MIB", "oxcConfLastChangeTime"), ("LUM-OXC-MIB", "oxcConfAdminStatus"), ("LUM-OXC-MIB", "oxcConfOperStatus"), ("LUM-OXC-MIB", "oxcConfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcConfGroup = oxcConfGroup.setStatus('deprecated')
oxcIfGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 4)).setObjects(("LUM-OXC-MIB", "oxcIfIndex"), ("LUM-OXC-MIB", "oxcIfName"), ("LUM-OXC-MIB", "oxcIfDescr"), ("LUM-OXC-MIB", "oxcIfSubrack"), ("LUM-OXC-MIB", "oxcIfSlot"), ("LUM-OXC-MIB", "oxcIfPort"), ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"), ("LUM-OXC-MIB", "oxcIfDirection"), ("LUM-OXC-MIB", "oxcIfOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcIfGroupV2 = oxcIfGroupV2.setStatus('deprecated')
oxcConfGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 5)).setObjects(("LUM-OXC-MIB", "oxcConfIndex"), ("LUM-OXC-MIB", "oxcConfName"), ("LUM-OXC-MIB", "oxcConfDescr"), ("LUM-OXC-MIB", "oxcConfSubrack"), ("LUM-OXC-MIB", "oxcConfSlot"), ("LUM-OXC-MIB", "oxcConfInPort"), ("LUM-OXC-MIB", "oxcConfOutPort"), ("LUM-OXC-MIB", "oxcConfLastChangeTime"), ("LUM-OXC-MIB", "oxcConfAdminStatus"), ("LUM-OXC-MIB", "oxcConfOperStatus"), ("LUM-OXC-MIB", "oxcConfServiceFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcConfGroupV2 = oxcConfGroupV2.setStatus('deprecated')
oxcGeneralGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 6)).setObjects(("LUM-OXC-MIB", "oxcGeneralLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcGeneralGroupV2 = oxcGeneralGroupV2.setStatus('deprecated')
oxcConfGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 7)).setObjects(("LUM-OXC-MIB", "oxcConfIndex"), ("LUM-OXC-MIB", "oxcConfName"), ("LUM-OXC-MIB", "oxcConfDescr"), ("LUM-OXC-MIB", "oxcConfSubrack"), ("LUM-OXC-MIB", "oxcConfSlot"), ("LUM-OXC-MIB", "oxcConfInPort"), ("LUM-OXC-MIB", "oxcConfOutPort"), ("LUM-OXC-MIB", "oxcConfLastChangeTime"), ("LUM-OXC-MIB", "oxcConfAdminStatus"), ("LUM-OXC-MIB", "oxcConfServiceFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcConfGroupV3 = oxcConfGroupV3.setStatus('deprecated')
oxcGeneralGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 8)).setObjects(("LUM-OXC-MIB", "oxcGeneralLastChangeTime"), ("LUM-OXC-MIB", "oxcGeneralStateLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcGeneralGroupV3 = oxcGeneralGroupV3.setStatus('deprecated')
oxcIfGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 9)).setObjects(("LUM-OXC-MIB", "oxcIfIndex"), ("LUM-OXC-MIB", "oxcIfName"), ("LUM-OXC-MIB", "oxcIfDescr"), ("LUM-OXC-MIB", "oxcIfSubrack"), ("LUM-OXC-MIB", "oxcIfSlot"), ("LUM-OXC-MIB", "oxcIfPort"), ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"), ("LUM-OXC-MIB", "oxcIfDirection"), ("LUM-OXC-MIB", "oxcIfOperStatus"), ("LUM-OXC-MIB", "oxcIfIsReserved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcIfGroupV3 = oxcIfGroupV3.setStatus('deprecated')
oxcGeneralGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 10)).setObjects(("LUM-OXC-MIB", "oxcGeneralLastChangeTime"), ("LUM-OXC-MIB", "oxcGeneralStateLastChangeTime"), ("LUM-OXC-MIB", "oxcGeneralOxcIfTableSize"), ("LUM-OXC-MIB", "oxcGeneralOxcConfTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcGeneralGroupV4 = oxcGeneralGroupV4.setStatus('current')
oxcIfGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 11)).setObjects(("LUM-OXC-MIB", "oxcIfIndex"), ("LUM-OXC-MIB", "oxcIfName"), ("LUM-OXC-MIB", "oxcIfDescr"), ("LUM-OXC-MIB", "oxcIfSubrack"), ("LUM-OXC-MIB", "oxcIfSlot"), ("LUM-OXC-MIB", "oxcIfPort"), ("LUM-OXC-MIB", "oxcIfInvPhysIndexOrZero"), ("LUM-OXC-MIB", "oxcIfDirection"), ("LUM-OXC-MIB", "oxcIfOperStatus"), ("LUM-OXC-MIB", "oxcIfIsReserved"), ("LUM-OXC-MIB", "oxcIfObjectProperty"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcIfGroupV4 = oxcIfGroupV4.setStatus('current')
oxcConfGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 1, 12)).setObjects(("LUM-OXC-MIB", "oxcConfIndex"), ("LUM-OXC-MIB", "oxcConfName"), ("LUM-OXC-MIB", "oxcConfDescr"), ("LUM-OXC-MIB", "oxcConfSubrack"), ("LUM-OXC-MIB", "oxcConfSlot"), ("LUM-OXC-MIB", "oxcConfInPort"), ("LUM-OXC-MIB", "oxcConfOutPort"), ("LUM-OXC-MIB", "oxcConfLastChangeTime"), ("LUM-OXC-MIB", "oxcConfAdminStatus"), ("LUM-OXC-MIB", "oxcConfServiceFailure"), ("LUM-OXC-MIB", "oxcConfObjectProperty"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oxcConfGroupV4 = oxcConfGroupV4.setStatus('current')
lumOxcBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 1)).setObjects(("LUM-OXC-MIB", "oxcGeneralGroup"), ("LUM-OXC-MIB", "oxcIfGroup"), ("LUM-OXC-MIB", "oxcConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumOxcBasicComplV1 = lumOxcBasicComplV1.setStatus('deprecated')
lumOxcBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 2)).setObjects(("LUM-OXC-MIB", "oxcGeneralGroup"), ("LUM-OXC-MIB", "oxcIfGroupV2"), ("LUM-OXC-MIB", "oxcConfGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumOxcBasicComplV2 = lumOxcBasicComplV2.setStatus('deprecated')
lumOxcBasicComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 3)).setObjects(("LUM-OXC-MIB", "oxcGeneralGroupV2"), ("LUM-OXC-MIB", "oxcIfGroupV2"), ("LUM-OXC-MIB", "oxcConfGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumOxcBasicComplV3 = lumOxcBasicComplV3.setStatus('deprecated')
lumOxcBasicComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 4)).setObjects(("LUM-OXC-MIB", "oxcGeneralGroupV2"), ("LUM-OXC-MIB", "oxcIfGroupV2"), ("LUM-OXC-MIB", "oxcConfGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumOxcBasicComplV4 = lumOxcBasicComplV4.setStatus('deprecated')
lumOxcBasicComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 5)).setObjects(("LUM-OXC-MIB", "oxcGeneralGroupV3"), ("LUM-OXC-MIB", "oxcIfGroupV2"), ("LUM-OXC-MIB", "oxcConfGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumOxcBasicComplV5 = lumOxcBasicComplV5.setStatus('deprecated')
lumOxcBasicComplV6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 6)).setObjects(("LUM-OXC-MIB", "oxcGeneralGroupV4"), ("LUM-OXC-MIB", "oxcIfGroupV3"), ("LUM-OXC-MIB", "oxcConfGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumOxcBasicComplV6 = lumOxcBasicComplV6.setStatus('deprecated')
lumOxcBasicComplV7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 10, 1, 2, 7)).setObjects(("LUM-OXC-MIB", "oxcGeneralGroupV4"), ("LUM-OXC-MIB", "oxcIfGroupV4"), ("LUM-OXC-MIB", "oxcConfGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumOxcBasicComplV7 = lumOxcBasicComplV7.setStatus('current')
mibBuilder.exportSymbols("LUM-OXC-MIB", oxcConfSubrack=oxcConfSubrack, oxcGeneralStateLastChangeTime=oxcGeneralStateLastChangeTime, lumOxcBasicComplV5=lumOxcBasicComplV5, oxcIfGroupV3=oxcIfGroupV3, lumOxcBasicComplV2=lumOxcBasicComplV2, oxcConfRowStatus=oxcConfRowStatus, oxcIfEntry=oxcIfEntry, oxcIfGroupV4=oxcIfGroupV4, oxcIfInvPhysIndexOrZero=oxcIfInvPhysIndexOrZero, oxcGeneralLastChangeTime=oxcGeneralLastChangeTime, oxcConfObjectProperty=oxcConfObjectProperty, lumOxcBasicComplV6=lumOxcBasicComplV6, oxcConfGroupV4=oxcConfGroupV4, oxcConfDescr=oxcConfDescr, oxcIfOperStatus=oxcIfOperStatus, oxcIfSubrack=oxcIfSubrack, oxcConfAdminStatus=oxcConfAdminStatus, lumOxcConfs=lumOxcConfs, lumOxcBasicComplV7=lumOxcBasicComplV7, lumOxcMIBModule=lumOxcMIBModule, oxcIfPort=oxcIfPort, oxcGeneralMibSpecVersion=oxcGeneralMibSpecVersion, oxcIfTable=oxcIfTable, oxcIfIsReserved=oxcIfIsReserved, oxcConfIndex=oxcConfIndex, oxcConfLastChangeTime=oxcConfLastChangeTime, lumOxcBasicComplV3=lumOxcBasicComplV3, oxcIfObjectProperty=oxcIfObjectProperty, oxcConfTable=oxcConfTable, oxcGeneral=oxcGeneral, lumOxcCompl=lumOxcCompl, oxcGeneralMibImplVersion=oxcGeneralMibImplVersion, oxcConfName=oxcConfName, lumOxcMIBObjects=lumOxcMIBObjects, oxcConfGroup=oxcConfGroup, oxcConfInPort=oxcConfInPort, lumOxcBasicComplV4=lumOxcBasicComplV4, oxcGeneralOxcIfTableSize=oxcGeneralOxcIfTableSize, oxcIfGroupV2=oxcIfGroupV2, oxcIfSlot=oxcIfSlot, oxcGeneralGroupV3=oxcGeneralGroupV3, oxcIfDirection=oxcIfDirection, oxcGeneralGroupV4=oxcGeneralGroupV4, oxcGeneralTestAndIncr=oxcGeneralTestAndIncr, PYSNMP_MODULE_ID=lumOxcMIBModule, oxcIfDescr=oxcIfDescr, oxcIfAdminStatus=oxcIfAdminStatus, oxcConfOutPort=oxcConfOutPort, lumOxcGroups=lumOxcGroups, oxcConfServiceFailure=oxcConfServiceFailure, oxcIfGroup=oxcIfGroup, oxcConfGroupV3=oxcConfGroupV3, oxcGeneralGroup=oxcGeneralGroup, oxcConfOperStatus=oxcConfOperStatus, oxcGeneralGroupV2=oxcGeneralGroupV2, oxcConfEntry=oxcConfEntry, oxcConfGroupV2=oxcConfGroupV2, oxcGeneralOxcConfTableSize=oxcGeneralOxcConfTableSize, oxcConfList=oxcConfList, oxcIfIndex=oxcIfIndex, lumOxcBasicComplV1=lumOxcBasicComplV1, oxcConfSlot=oxcConfSlot, oxcIfList=oxcIfList, oxcIfName=oxcIfName)
