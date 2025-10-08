#
# PySNMP MIB module LUM-IFMC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-IFMC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumIfMcMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumIfMcMIB", "lumModules")
PortNumber, FaultStatus, MgmtNameString, BoardOrInterfaceOperStatus, SlotNumber, SubrackNumber, BoardOrInterfaceAdminStatus = mibBuilder.importSymbols("LUM-TC", "PortNumber", "FaultStatus", "MgmtNameString", "BoardOrInterfaceOperStatus", "SlotNumber", "SubrackNumber", "BoardOrInterfaceAdminStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
lumIfMcMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 64))
lumIfMcMIBModule.setRevisions(('2018-07-09 00:00', '2018-04-13 00:00', '2017-09-01 00:00', '2017-06-15 00:00', '2015-03-15 00:00',))
if mibBuilder.loadTexts: lumIfMcMIBModule.setLastUpdated('201807090000Z')
if mibBuilder.loadTexts: lumIfMcMIBModule.setOrganization('Infinera Corporation')
lumIfMcConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1))
lumIfMcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1))
lumIfMcCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2))
lumIfMcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2))
ifMcGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1))
ifMcPortList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2))
class IfMcExpectedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ethernet100gLanSR10", 1), ("ethernet12x10gLan", 2), ("frontplane12x10g", 3), ("frontplane100g", 4), ("filter10x10g", 5), ("notApplicable", 6))

class IfMcMpoCableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("straight", 1), ("completeFanout", 2), ("fanout2x5", 3), ("notApplicable", 4))

ifMcGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcGeneralConfigLastChangeTime.setStatus('current')
ifMcGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcGeneralStateLastChangeTime.setStatus('current')
ifMcGeneralIfMcPortTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcGeneralIfMcPortTableSize.setStatus('current')
ifMcGeneralIfMcPortConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcGeneralIfMcPortConfigLastChangeTime.setStatus('current')
ifMcGeneralIfMcPortStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcGeneralIfMcPortStateLastChangeTime.setStatus('current')
ifMcPortTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1), )
if mibBuilder.loadTexts: ifMcPortTable.setStatus('current')
ifMcPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1), ).setIndexNames((0, "LUM-IFMC-MIB", "ifMcPortIndex"))
if mibBuilder.loadTexts: ifMcPortEntry.setStatus('current')
ifMcPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 1), MgmtNameString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifMcPortName.setStatus('current')
ifMcPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifMcPortIndex.setStatus('current')
ifMcPortDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMcPortDescr.setStatus('current')
ifMcPortExpectedType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 4), IfMcExpectedType().clone('ethernet100gLanSR10')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMcPortExpectedType.setStatus('current')
ifMcPortIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifMcPortIdx.setStatus('current')
ifMcPortSubrack = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 6), SubrackNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifMcPortSubrack.setStatus('current')
ifMcPortSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 7), SlotNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifMcPortSlot.setStatus('current')
ifMcPortIfNo = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 8), PortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifMcPortIfNo.setStatus('current')
ifMcPortLossOfSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 9), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcPortLossOfSignal.setStatus('current')
ifMcPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 10), BoardOrInterfaceAdminStatus().clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMcPortAdminStatus.setStatus('current')
ifMcPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 11), BoardOrInterfaceOperStatus().clone('notPresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcPortOperStatus.setStatus('current')
ifMcPortTrxClass = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcPortTrxClass.setStatus('current')
ifMcPortReceivedPowerLow = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 13), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMcPortReceivedPowerLow.setStatus('current')
ifMcPortMpoCableType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 14), IfMcMpoCableType().clone('notApplicable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifMcPortMpoCableType.setStatus('current')
ifMcGeneralGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 1)).setObjects(("LUM-IFMC-MIB", "ifMcGeneralConfigLastChangeTime"), ("LUM-IFMC-MIB", "ifMcGeneralStateLastChangeTime"), ("LUM-IFMC-MIB", "ifMcGeneralIfMcPortTableSize"), ("LUM-IFMC-MIB", "ifMcGeneralIfMcPortConfigLastChangeTime"), ("LUM-IFMC-MIB", "ifMcGeneralIfMcPortStateLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifMcGeneralGroupV1 = ifMcGeneralGroupV1.setStatus('current')
ifMcPortGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 2)).setObjects(("LUM-IFMC-MIB", "ifMcPortName"), ("LUM-IFMC-MIB", "ifMcPortIndex"), ("LUM-IFMC-MIB", "ifMcPortDescr"), ("LUM-IFMC-MIB", "ifMcPortExpectedType"), ("LUM-IFMC-MIB", "ifMcPortIdx"), ("LUM-IFMC-MIB", "ifMcPortSubrack"), ("LUM-IFMC-MIB", "ifMcPortSlot"), ("LUM-IFMC-MIB", "ifMcPortIfNo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifMcPortGroupV1 = ifMcPortGroupV1.setStatus('deprecated')
ifMcPortGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 3)).setObjects(("LUM-IFMC-MIB", "ifMcPortName"), ("LUM-IFMC-MIB", "ifMcPortIndex"), ("LUM-IFMC-MIB", "ifMcPortDescr"), ("LUM-IFMC-MIB", "ifMcPortExpectedType"), ("LUM-IFMC-MIB", "ifMcPortIdx"), ("LUM-IFMC-MIB", "ifMcPortSubrack"), ("LUM-IFMC-MIB", "ifMcPortSlot"), ("LUM-IFMC-MIB", "ifMcPortIfNo"), ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifMcPortGroupV2 = ifMcPortGroupV2.setStatus('deprecated')
ifMcPortGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 4)).setObjects(("LUM-IFMC-MIB", "ifMcPortName"), ("LUM-IFMC-MIB", "ifMcPortIndex"), ("LUM-IFMC-MIB", "ifMcPortDescr"), ("LUM-IFMC-MIB", "ifMcPortExpectedType"), ("LUM-IFMC-MIB", "ifMcPortIdx"), ("LUM-IFMC-MIB", "ifMcPortSubrack"), ("LUM-IFMC-MIB", "ifMcPortSlot"), ("LUM-IFMC-MIB", "ifMcPortIfNo"), ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"), ("LUM-IFMC-MIB", "ifMcPortAdminStatus"), ("LUM-IFMC-MIB", "ifMcPortOperStatus"), ("LUM-IFMC-MIB", "ifMcPortTrxClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifMcPortGroupV3 = ifMcPortGroupV3.setStatus('deprecated')
ifMcPortGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 5)).setObjects(("LUM-IFMC-MIB", "ifMcPortName"), ("LUM-IFMC-MIB", "ifMcPortIndex"), ("LUM-IFMC-MIB", "ifMcPortDescr"), ("LUM-IFMC-MIB", "ifMcPortExpectedType"), ("LUM-IFMC-MIB", "ifMcPortIdx"), ("LUM-IFMC-MIB", "ifMcPortSubrack"), ("LUM-IFMC-MIB", "ifMcPortSlot"), ("LUM-IFMC-MIB", "ifMcPortIfNo"), ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"), ("LUM-IFMC-MIB", "ifMcPortAdminStatus"), ("LUM-IFMC-MIB", "ifMcPortOperStatus"), ("LUM-IFMC-MIB", "ifMcPortTrxClass"), ("LUM-IFMC-MIB", "ifMcPortReceivedPowerLow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifMcPortGroupV4 = ifMcPortGroupV4.setStatus('deprecated')
ifMcPortGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 6)).setObjects(("LUM-IFMC-MIB", "ifMcPortName"), ("LUM-IFMC-MIB", "ifMcPortIndex"), ("LUM-IFMC-MIB", "ifMcPortDescr"), ("LUM-IFMC-MIB", "ifMcPortExpectedType"), ("LUM-IFMC-MIB", "ifMcPortIdx"), ("LUM-IFMC-MIB", "ifMcPortSubrack"), ("LUM-IFMC-MIB", "ifMcPortSlot"), ("LUM-IFMC-MIB", "ifMcPortIfNo"), ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"), ("LUM-IFMC-MIB", "ifMcPortAdminStatus"), ("LUM-IFMC-MIB", "ifMcPortOperStatus"), ("LUM-IFMC-MIB", "ifMcPortTrxClass"), ("LUM-IFMC-MIB", "ifMcPortReceivedPowerLow"), ("LUM-IFMC-MIB", "ifMcPortMpoCableType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifMcPortGroupV5 = ifMcPortGroupV5.setStatus('current')
lumIfMcComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 1)).setObjects(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"), ("LUM-IFMC-MIB", "ifMcPortGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumIfMcComplV1 = lumIfMcComplV1.setStatus('deprecated')
lumIfMcComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 2)).setObjects(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"), ("LUM-IFMC-MIB", "ifMcPortGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumIfMcComplV2 = lumIfMcComplV2.setStatus('deprecated')
lumIfMcComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 3)).setObjects(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"), ("LUM-IFMC-MIB", "ifMcPortGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumIfMcComplV3 = lumIfMcComplV3.setStatus('deprecated')
lumIfMcComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 4)).setObjects(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"), ("LUM-IFMC-MIB", "ifMcPortGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumIfMcComplV4 = lumIfMcComplV4.setStatus('deprecated')
lumIfMcComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 5)).setObjects(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"), ("LUM-IFMC-MIB", "ifMcPortGroupV5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumIfMcComplV5 = lumIfMcComplV5.setStatus('current')
mibBuilder.exportSymbols("LUM-IFMC-MIB", IfMcExpectedType=IfMcExpectedType, ifMcPortLossOfSignal=ifMcPortLossOfSignal, lumIfMcCompl=lumIfMcCompl, lumIfMcComplV2=lumIfMcComplV2, ifMcGeneralConfigLastChangeTime=ifMcGeneralConfigLastChangeTime, ifMcPortGroupV2=ifMcPortGroupV2, ifMcGeneralGroupV1=ifMcGeneralGroupV1, ifMcPortIfNo=ifMcPortIfNo, ifMcPortList=ifMcPortList, ifMcPortTable=ifMcPortTable, PYSNMP_MODULE_ID=lumIfMcMIBModule, IfMcMpoCableType=IfMcMpoCableType, ifMcPortEntry=ifMcPortEntry, ifMcPortMpoCableType=ifMcPortMpoCableType, lumIfMcComplV5=lumIfMcComplV5, lumIfMcGroups=lumIfMcGroups, ifMcPortTrxClass=ifMcPortTrxClass, lumIfMcComplV1=lumIfMcComplV1, lumIfMcComplV3=lumIfMcComplV3, ifMcPortSubrack=ifMcPortSubrack, ifMcPortGroupV3=ifMcPortGroupV3, ifMcPortIdx=ifMcPortIdx, ifMcGeneralIfMcPortStateLastChangeTime=ifMcGeneralIfMcPortStateLastChangeTime, ifMcPortOperStatus=ifMcPortOperStatus, ifMcPortGroupV4=ifMcPortGroupV4, ifMcGeneralIfMcPortTableSize=ifMcGeneralIfMcPortTableSize, lumIfMcConfs=lumIfMcConfs, ifMcGeneralIfMcPortConfigLastChangeTime=ifMcGeneralIfMcPortConfigLastChangeTime, ifMcPortDescr=ifMcPortDescr, lumIfMcMIBObjects=lumIfMcMIBObjects, ifMcPortIndex=ifMcPortIndex, ifMcPortSlot=ifMcPortSlot, ifMcPortReceivedPowerLow=ifMcPortReceivedPowerLow, ifMcPortGroupV5=ifMcPortGroupV5, ifMcGeneral=ifMcGeneral, ifMcPortExpectedType=ifMcPortExpectedType, ifMcPortAdminStatus=ifMcPortAdminStatus, lumIfMcComplV4=lumIfMcComplV4, ifMcGeneralStateLastChangeTime=ifMcGeneralStateLastChangeTime, ifMcPortGroupV1=ifMcPortGroupV1, ifMcPortName=ifMcPortName, lumIfMcMIBModule=lumIfMcMIBModule)
