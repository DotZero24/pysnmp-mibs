#
# PySNMP MIB module Juniper-PPPOE-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-PPPOE-PROFILE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniSetMap, JuniEnable = mibBuilder.importSymbols("Juniper-TC", "JuniSetMap", "JuniEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniPppoeProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46))
juniPppoeProfileMIB.setRevisions(('2008-06-18 10:29', '2005-07-13 11:40', '2004-06-10 19:25', '2003-03-11 21:58', '2002-09-16 21:44', '2002-08-15 20:34', '2002-08-15 19:07', '2001-03-21 18:32',))
if mibBuilder.loadTexts: juniPppoeProfileMIB.setLastUpdated('200806181029Z')
if mibBuilder.loadTexts: juniPppoeProfileMIB.setOrganization('Juniper Networks, Inc.')
juniPppoeProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1))
juniPppoeProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1))
juniPppoeProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1), )
if mibBuilder.loadTexts: juniPppoeProfileTable.setStatus('current')
juniPppoeProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileId"))
if mibBuilder.loadTexts: juniPppoeProfileEntry.setStatus('current')
juniPppoeProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniPppoeProfileId.setStatus('current')
juniPppoeProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 2), JuniSetMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileSetMap.setStatus('current')
juniPppoeProfileMaxNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileMaxNumSessions.setStatus('current')
juniPppoeProfileSubMotm = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileSubMotm.setStatus('current')
juniPppoeProfileSubUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileSubUrl.setStatus('current')
juniPppoeProfileDupProtect = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 6), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileDupProtect.setStatus('current')
juniPppoeProfileAcName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileAcName.setStatus('current')
juniPppoeProfilePadiFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 8), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfilePadiFlag.setStatus('current')
juniPppoeProfilePacketTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 9), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfilePacketTrace.setStatus('current')
juniPppoeProfileServiceNameTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileServiceNameTableName.setStatus('current')
juniPppoeProfilePadrRemoteCircuitIdCapture = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 11), JuniEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfilePadrRemoteCircuitIdCapture.setStatus('current')
juniPppoeProfileMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(66, 65535), )).clone(1494)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileMtu.setStatus('current')
juniPppoeProfileMaxSessionOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("override", 1), ("ignore", 2))).clone('ignore')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniPppoeProfileMaxSessionOverride.setStatus('current')
juniPppoeProfileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4))
juniPppoeProfileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1))
juniPppoeProfileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2))
juniPppoeProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 1)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileCompliance = juniPppoeProfileCompliance.setStatus('obsolete')
juniPppoeCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 2)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance2 = juniPppoeCompliance2.setStatus('obsolete')
juniPppoeCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 3)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance3 = juniPppoeCompliance3.setStatus('obsolete')
juniPppoeCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 4)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance4 = juniPppoeCompliance4.setStatus('obsolete')
juniPppoeCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 5)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance5 = juniPppoeCompliance5.setStatus('obsolete')
juniPppoeCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 6)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance6 = juniPppoeCompliance6.setStatus('obsolete')
juniPppoeCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 1, 7)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileGroup7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeCompliance7 = juniPppoeCompliance7.setStatus('current')
juniPppoeProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 1)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup = juniPppoeProfileGroup.setStatus('obsolete')
juniPppoeProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 2)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup2 = juniPppoeProfileGroup2.setStatus('obsolete')
juniPppoeProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 3)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup3 = juniPppoeProfileGroup3.setStatus('obsolete')
juniPppoeProfileGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 4)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup4 = juniPppoeProfileGroup4.setStatus('obsolete')
juniPppoeProfileGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 5)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup5 = juniPppoeProfileGroup5.setStatus('obsolete')
juniPppoeProfileGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 6)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup6 = juniPppoeProfileGroup6.setStatus('obsolete')
juniPppoeProfileGroup7 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 46, 4, 2, 7)).setObjects(("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSetMap"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxNumSessions"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubMotm"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileSubUrl"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileDupProtect"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileAcName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadiFlag"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePacketTrace"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileServiceNameTableName"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfilePadrRemoteCircuitIdCapture"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMtu"), ("Juniper-PPPOE-PROFILE-MIB", "juniPppoeProfileMaxSessionOverride"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniPppoeProfileGroup7 = juniPppoeProfileGroup7.setStatus('current')
mibBuilder.exportSymbols("Juniper-PPPOE-PROFILE-MIB", juniPppoeProfileConformance=juniPppoeProfileConformance, juniPppoeProfileObjects=juniPppoeProfileObjects, juniPppoeProfilePadiFlag=juniPppoeProfilePadiFlag, juniPppoeProfileServiceNameTableName=juniPppoeProfileServiceNameTableName, juniPppoeProfileId=juniPppoeProfileId, juniPppoeProfilePacketTrace=juniPppoeProfilePacketTrace, juniPppoeProfile=juniPppoeProfile, juniPppoeProfileGroup5=juniPppoeProfileGroup5, juniPppoeProfileGroup=juniPppoeProfileGroup, juniPppoeCompliance5=juniPppoeCompliance5, juniPppoeCompliance7=juniPppoeCompliance7, juniPppoeProfileGroup3=juniPppoeProfileGroup3, juniPppoeProfileGroups=juniPppoeProfileGroups, juniPppoeProfileGroup2=juniPppoeProfileGroup2, juniPppoeProfileSetMap=juniPppoeProfileSetMap, juniPppoeProfileMaxNumSessions=juniPppoeProfileMaxNumSessions, PYSNMP_MODULE_ID=juniPppoeProfileMIB, juniPppoeProfileMaxSessionOverride=juniPppoeProfileMaxSessionOverride, juniPppoeCompliance2=juniPppoeCompliance2, juniPppoeCompliance3=juniPppoeCompliance3, juniPppoeProfileTable=juniPppoeProfileTable, juniPppoeCompliance6=juniPppoeCompliance6, juniPppoeProfileGroup7=juniPppoeProfileGroup7, juniPppoeProfileGroup6=juniPppoeProfileGroup6, juniPppoeProfileCompliance=juniPppoeProfileCompliance, juniPppoeProfileMIB=juniPppoeProfileMIB, juniPppoeProfileGroup4=juniPppoeProfileGroup4, juniPppoeProfileMtu=juniPppoeProfileMtu, juniPppoeProfileSubMotm=juniPppoeProfileSubMotm, juniPppoeProfileAcName=juniPppoeProfileAcName, juniPppoeProfileDupProtect=juniPppoeProfileDupProtect, juniPppoeProfileEntry=juniPppoeProfileEntry, juniPppoeProfileCompliances=juniPppoeProfileCompliances, juniPppoeProfilePadrRemoteCircuitIdCapture=juniPppoeProfilePadrRemoteCircuitIdCapture, juniPppoeCompliance4=juniPppoeCompliance4, juniPppoeProfileSubUrl=juniPppoeProfileSubUrl)
