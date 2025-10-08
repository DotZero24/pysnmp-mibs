#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-CAS-MODULE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-MIB", cvcmCasBitRowStatus=cvcmCasBitRowStatus, cvcmABCDOutgoingPattern=cvcmABCDOutgoingPattern, ciscoVoiceCasModuleMIB=ciscoVoiceCasModuleMIB, cvcmCasBitGroup=cvcmCasBitGroup, cvcmMIBGroups=cvcmMIBGroups, cvcmABCDIncomingPattern=cvcmABCDIncomingPattern, cvcmMIBCompliances=cvcmMIBCompliances, cvcmABCDBitTemplateConfigEntry=cvcmABCDBitTemplateConfigEntry, cvcmCasCBitAction=cvcmCasCBitAction, ciscoVoiceCasModuleObjects=ciscoVoiceCasModuleObjects, cvcmCasTemplateName=cvcmCasTemplateName, cvcmCasBBitAction=cvcmCasBBitAction, cvcmABCDBitTemplateConfigTable=cvcmABCDBitTemplateConfigTable, cvcmCasTemplateIndex=cvcmCasTemplateIndex, cvcmCasConfig=cvcmCasConfig, CvcmCasPatternBitPosition=CvcmCasPatternBitPosition, cvcmMIBConformance=cvcmMIBConformance, CvcmCasBitAction=CvcmCasBitAction, cvcmModuleIndex=cvcmModuleIndex, ciscoVoiceCasModuleNotifs=ciscoVoiceCasModuleNotifs, ciscoVoiceCasModuleMIBCompliance=ciscoVoiceCasModuleMIBCompliance, cvcmABCDPatternIndex=cvcmABCDPatternIndex, cvcmCasABitAction=cvcmCasABitAction, cvcmCasDBitAction=cvcmCasDBitAction, PYSNMP_MODULE_ID=ciscoVoiceCasModuleMIB, cvcmModulePhysicalIndex=cvcmModulePhysicalIndex)
