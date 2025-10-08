#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-CAS-MODULE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoVoiceCasModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 389))
ciscoVoiceCasModuleMIB.setRevisions(('2004-03-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setLastUpdated('200403150000Z')
if mibBuilder.loadTexts: ciscoVoiceCasModuleMIB.setOrganization('Cisco Systems, Inc.')
ciscoVoiceCasModuleNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 0))
ciscoVoiceCasModuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 1))
cvcmCasConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1))
class CvcmCasPatternBitPosition(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dBit", 0), ("cBit", 1), ("bBit", 2), ("aBit", 3))

class CvcmCasBitAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("casBitNoAction", 1), ("casBitSetToZero", 2), ("casBitSetToOne", 3), ("casBitInvertBit", 4), ("casBitInvertABit", 5), ("casBitInvertBBit", 6), ("casBitInvertCBit", 7), ("casBitInvertDBit", 8), ("casBitABit", 9), ("casBitBBit", 10), ("casBitCBit", 11), ("casBitDBit", 12))

cvcmABCDBitTemplateConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1), )
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigTable.setStatus('current')
cvcmABCDBitTemplateConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmModuleIndex"), (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateIndex"), (0, "CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDPatternIndex"))
if mibBuilder.loadTexts: cvcmABCDBitTemplateConfigEntry.setStatus('current')
cvcmModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvcmModuleIndex.setStatus('current')
cvcmCasTemplateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvcmCasTemplateIndex.setStatus('current')
cvcmABCDPatternIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: cvcmABCDPatternIndex.setStatus('current')
cvcmModulePhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 4), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcmModulePhysicalIndex.setStatus('current')
cvcmCasTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasTemplateName.setStatus('current')
cvcmABCDIncomingPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 6), CvcmCasPatternBitPosition()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmABCDIncomingPattern.setStatus('current')
cvcmABCDOutgoingPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 7), CvcmCasPatternBitPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvcmABCDOutgoingPattern.setStatus('current')
cvcmCasABitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 8), CvcmCasBitAction().clone('casBitABit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasABitAction.setStatus('current')
cvcmCasBBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 9), CvcmCasBitAction().clone('casBitBBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasBBitAction.setStatus('current')
cvcmCasCBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 10), CvcmCasBitAction().clone('casBitCBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasCBitAction.setStatus('current')
cvcmCasDBitAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 11), CvcmCasBitAction().clone('casBitDBit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasDBitAction.setStatus('current')
cvcmCasBitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 389, 1, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcmCasBitRowStatus.setStatus('current')
cvcmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2))
cvcmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1))
cvcmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2))
ciscoVoiceCasModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 2, 1)).setObjects(("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCasModuleMIBCompliance = ciscoVoiceCasModuleMIBCompliance.setStatus('current')
cvcmCasBitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 389, 2, 1, 1)).setObjects(("CISCO-VOICE-CAS-MODULE-MIB", "cvcmModulePhysicalIndex"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasTemplateName"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDIncomingPattern"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmABCDOutgoingPattern"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasABitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasCBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasDBitAction"), ("CISCO-VOICE-CAS-MODULE-MIB", "cvcmCasBitRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCasBitGroup = cvcmCasBitGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-MIB", ciscoVoiceCasModuleObjects=ciscoVoiceCasModuleObjects, cvcmABCDIncomingPattern=cvcmABCDIncomingPattern, PYSNMP_MODULE_ID=ciscoVoiceCasModuleMIB, cvcmMIBCompliances=cvcmMIBCompliances, ciscoVoiceCasModuleNotifs=ciscoVoiceCasModuleNotifs, cvcmMIBConformance=cvcmMIBConformance, CvcmCasBitAction=CvcmCasBitAction, cvcmMIBGroups=cvcmMIBGroups, cvcmCasTemplateName=cvcmCasTemplateName, cvcmModuleIndex=cvcmModuleIndex, cvcmABCDBitTemplateConfigTable=cvcmABCDBitTemplateConfigTable, ciscoVoiceCasModuleMIBCompliance=ciscoVoiceCasModuleMIBCompliance, cvcmCasCBitAction=cvcmCasCBitAction, cvcmCasBBitAction=cvcmCasBBitAction, CvcmCasPatternBitPosition=CvcmCasPatternBitPosition, cvcmABCDOutgoingPattern=cvcmABCDOutgoingPattern, cvcmABCDBitTemplateConfigEntry=cvcmABCDBitTemplateConfigEntry, ciscoVoiceCasModuleMIB=ciscoVoiceCasModuleMIB, cvcmCasBitRowStatus=cvcmCasBitRowStatus, cvcmModulePhysicalIndex=cvcmModulePhysicalIndex, cvcmCasABitAction=cvcmCasABitAction, cvcmCasBitGroup=cvcmCasBitGroup, cvcmABCDPatternIndex=cvcmABCDPatternIndex, cvcmCasTemplateIndex=cvcmCasTemplateIndex, cvcmCasDBitAction=cvcmCasDBitAction, cvcmCasConfig=cvcmCasConfig)
