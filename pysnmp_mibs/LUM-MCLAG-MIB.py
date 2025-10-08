#
# PySNMP MIB module LUM-MCLAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-MCLAG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumMclagMIB, lumModules = mibBuilder.importSymbols("LUM-REG", "lumMclagMIB", "lumModules")
FaultStatus, MgmtNameString = mibBuilder.importSymbols("LUM-TC", "FaultStatus", "MgmtNameString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
lumMclagMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 62))
lumMclagMIBModule.setRevisions(('2017-06-15 00:00', '2015-01-14 00:00', '2014-11-05 00:00',))
if mibBuilder.loadTexts: lumMclagMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumMclagMIBModule.setOrganization('Infinera Corporation')
lumMclagConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 62, 1))
lumMclagGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 1))
lumMclagCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 2))
lumMclagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2))
mclagGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1))
mclagList = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2))
class MclagLabel(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1048575)

class MclagIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mclagGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mclagGeneralLastChangeTime.setStatus('current')
mclagGeneralStateLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mclagGeneralStateLastChangeTime.setStatus('current')
mclagGeneralMclagTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mclagGeneralMclagTableSize.setStatus('current')
mclagTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1), )
if mibBuilder.loadTexts: mclagTable.setStatus('current')
mclagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1), ).setIndexNames((0, "LUM-MCLAG-MIB", "mclagIndex"))
if mibBuilder.loadTexts: mclagEntry.setStatus('current')
mclagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mclagIndex.setStatus('current')
mclagName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mclagName.setStatus('current')
mclagDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mclagDescr.setStatus('current')
mclagNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mclagNodeId.setStatus('current')
mclagRgId = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mclagRgId.setStatus('current')
mclagSynchronizationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unSynchronized", 1), ("synchronized", 2), ("undefined", 3))).clone('undefined')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mclagSynchronizationStatus.setStatus('current')
mclagControlledLag = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mclagControlledLag.setStatus('current')
mclagLagAdminSystemPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mclagLagAdminSystemPrio.setStatus('current')
mclagLagOperSystemPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mclagLagOperSystemPrio.setStatus('current')
mclagLagAdminPortPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mclagLagAdminPortPrio.setStatus('current')
mclagLagOperPortPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mclagLagOperPortPrio.setStatus('current')
mclagLagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standby", 1), ("active", 2))).clone('standby')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mclagLagStatus.setStatus('current')
mclagProtectionStateFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 13), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mclagProtectionStateFailure.setStatus('current')
mclagProtectionStateDegraded = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 14), FaultStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mclagProtectionStateDegraded.setStatus('current')
mclagInternalReference = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 62, 2, 2, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mclagInternalReference.setStatus('current')
mclagGeneralGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 1, 1)).setObjects(("LUM-MCLAG-MIB", "mclagGeneralLastChangeTime"), ("LUM-MCLAG-MIB", "mclagGeneralStateLastChangeTime"), ("LUM-MCLAG-MIB", "mclagGeneralMclagTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mclagGeneralGroupV1 = mclagGeneralGroupV1.setStatus('current')
mclagGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 1, 2)).setObjects(("LUM-MCLAG-MIB", "mclagIndex"), ("LUM-MCLAG-MIB", "mclagName"), ("LUM-MCLAG-MIB", "mclagDescr"), ("LUM-MCLAG-MIB", "mclagNodeId"), ("LUM-MCLAG-MIB", "mclagRgId"), ("LUM-MCLAG-MIB", "mclagSynchronizationStatus"), ("LUM-MCLAG-MIB", "mclagControlledLag"), ("LUM-MCLAG-MIB", "mclagLagAdminSystemPrio"), ("LUM-MCLAG-MIB", "mclagLagOperSystemPrio"), ("LUM-MCLAG-MIB", "mclagLagAdminPortPrio"), ("LUM-MCLAG-MIB", "mclagLagOperPortPrio"), ("LUM-MCLAG-MIB", "mclagLagStatus"), ("LUM-MCLAG-MIB", "mclagProtectionStateFailure"), ("LUM-MCLAG-MIB", "mclagProtectionStateDegraded"), ("LUM-MCLAG-MIB", "mclagInternalReference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mclagGroupV1 = mclagGroupV1.setStatus('current')
lumMclagBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 62, 1, 2, 1)).setObjects(("LUM-MCLAG-MIB", "mclagGroupV1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumMclagBasicComplV1 = lumMclagBasicComplV1.setStatus('current')
mibBuilder.exportSymbols("LUM-MCLAG-MIB", mclagLagStatus=mclagLagStatus, mclagEntry=mclagEntry, lumMclagBasicComplV1=lumMclagBasicComplV1, PYSNMP_MODULE_ID=lumMclagMIBModule, mclagList=mclagList, mclagLagAdminPortPrio=mclagLagAdminPortPrio, mclagGeneralLastChangeTime=mclagGeneralLastChangeTime, lumMclagConfs=lumMclagConfs, mclagRgId=mclagRgId, mclagProtectionStateDegraded=mclagProtectionStateDegraded, lumMclagCompl=lumMclagCompl, mclagIndex=mclagIndex, mclagLagOperSystemPrio=mclagLagOperSystemPrio, mclagGeneralStateLastChangeTime=mclagGeneralStateLastChangeTime, mclagLagOperPortPrio=mclagLagOperPortPrio, mclagGeneralGroupV1=mclagGeneralGroupV1, lumMclagMIBObjects=lumMclagMIBObjects, mclagControlledLag=mclagControlledLag, mclagGeneral=mclagGeneral, mclagName=mclagName, MclagLabel=MclagLabel, lumMclagGroups=lumMclagGroups, mclagGeneralMclagTableSize=mclagGeneralMclagTableSize, mclagProtectionStateFailure=mclagProtectionStateFailure, mclagLagAdminSystemPrio=mclagLagAdminSystemPrio, mclagInternalReference=mclagInternalReference, mclagNodeId=mclagNodeId, mclagTable=mclagTable, mclagDescr=mclagDescr, mclagSynchronizationStatus=mclagSynchronizationStatus, MclagIdentifier=MclagIdentifier, mclagGroupV1=mclagGroupV1, lumMclagMIBModule=lumMclagMIBModule)
