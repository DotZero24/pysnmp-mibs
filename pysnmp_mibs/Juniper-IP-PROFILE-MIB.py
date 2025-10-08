#
# PySNMP MIB module Juniper-IP-PROFILE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-IP-PROFILE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, JuniName, JuniSetMap = mibBuilder.importSymbols("Juniper-TC", "JuniEnable", "JuniName", "JuniSetMap")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniIpProfileMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26))
juniIpProfileMIB.setRevisions(('2006-09-08 10:26', '2005-09-13 17:21', '2004-10-05 14:04', '2003-09-24 15:33', '2002-10-11 13:20', '2001-01-24 20:06', '2000-05-08 00:00', '1999-08-25 00:00',))
if mibBuilder.loadTexts: juniIpProfileMIB.setLastUpdated('200609081026Z')
if mibBuilder.loadTexts: juniIpProfileMIB.setOrganization('Juniper Networks')
juniIpProfileObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1))
juniIpProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1))
juniIpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1), )
if mibBuilder.loadTexts: juniIpProfileTable.setStatus('current')
juniIpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-IP-PROFILE-MIB", "juniIpProfileId"))
if mibBuilder.loadTexts: juniIpProfileEntry.setStatus('current')
juniIpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniIpProfileId.setStatus('current')
juniIpProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileRowStatus.setStatus('deprecated')
juniIpProfileRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 3), JuniName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileRouterName.setStatus('current')
juniIpProfileIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIpAddr.setStatus('current')
juniIpProfileIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIpMask.setStatus('current')
juniIpProfileDirectedBcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 6), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileDirectedBcastEnable.setStatus('current')
juniIpProfileIcmpRedirectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 7), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileIcmpRedirectEnable.setStatus('current')
juniIpProfileAccessRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 8), JuniEnable().clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileAccessRoute.setStatus('current')
juniIpProfileMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(512, 10240), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileMtu.setStatus('current')
juniIpProfileLoopbackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileLoopbackIfIndex.setStatus('obsolete')
juniIpProfileLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileLoopback.setStatus('obsolete')
juniIpProfileSetMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 12), JuniSetMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileSetMap.setStatus('current')
juniIpProfileSrcAddrValidEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 13), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileSrcAddrValidEnable.setStatus('current')
juniIpProfileInheritNumString = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileInheritNumString.setStatus('current')
juniIpProfileTcpMss = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(160, 10240), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileTcpMss.setStatus('current')
juniIpProfileFilterOptionsAll = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 16), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileFilterOptionsAll.setStatus('current')
juniIpProfileFlowStats = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 17), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileFlowStats.setStatus('current')
juniIpProfileBlockMulticastSources = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 1, 1, 1, 1, 18), JuniEnable().clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIpProfileBlockMulticastSources.setStatus('current')
juniIpProfileMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4))
juniIpProfileMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1))
juniIpProfileMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2))
juniIpProfileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 1)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance = juniIpProfileCompliance.setStatus('obsolete')
juniIpProfileCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 2)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance1 = juniIpProfileCompliance1.setStatus('obsolete')
juniIpProfileCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 3)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance2 = juniIpProfileCompliance2.setStatus('obsolete')
juniIpProfileCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 4)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance3 = juniIpProfileCompliance3.setStatus('obsolete')
juniIpProfileCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 5)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance4 = juniIpProfileCompliance4.setStatus('obsolete')
juniIpProfileCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 6)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance5 = juniIpProfileCompliance5.setStatus('current')
juniIpProfileCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 7)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance6 = juniIpProfileCompliance6.setStatus('current')
juniIpProfileCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 1, 8)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileGroup7"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileCompliance7 = juniIpProfileCompliance7.setStatus('current')
juniIpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 1)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopbackIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup = juniIpProfileGroup.setStatus('obsolete')
juniIpProfileGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 2)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup1 = juniIpProfileGroup1.setStatus('obsolete')
juniIpProfileGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 3)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileLoopback"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup2 = juniIpProfileGroup2.setStatus('obsolete')
juniIpProfileDeprecatedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 4)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileDeprecatedGroup = juniIpProfileDeprecatedGroup.setStatus('deprecated')
juniIpProfileGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 5)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup3 = juniIpProfileGroup3.setStatus('obsolete')
juniIpProfileGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 6)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup4 = juniIpProfileGroup4.setStatus('obsolete')
juniIpProfileGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 7)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup5 = juniIpProfileGroup5.setStatus('obsolete')
juniIpProfileGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 8)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup6 = juniIpProfileGroup6.setStatus('obsolete')
juniIpProfileGroup7 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 26, 4, 2, 9)).setObjects(("Juniper-IP-PROFILE-MIB", "juniIpProfileRouterName"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpAddr"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIpMask"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileDirectedBcastEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileIcmpRedirectEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileAccessRoute"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileMtu"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSetMap"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileSrcAddrValidEnable"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileInheritNumString"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileTcpMss"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFilterOptionsAll"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileFlowStats"), ("Juniper-IP-PROFILE-MIB", "juniIpProfileBlockMulticastSources"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIpProfileGroup7 = juniIpProfileGroup7.setStatus('current')
mibBuilder.exportSymbols("Juniper-IP-PROFILE-MIB", juniIpProfileTcpMss=juniIpProfileTcpMss, juniIpProfileDirectedBcastEnable=juniIpProfileDirectedBcastEnable, juniIpProfileTable=juniIpProfileTable, juniIpProfileId=juniIpProfileId, juniIpProfileIpMask=juniIpProfileIpMask, juniIpProfileSrcAddrValidEnable=juniIpProfileSrcAddrValidEnable, juniIpProfileGroup5=juniIpProfileGroup5, juniIpProfileCompliance6=juniIpProfileCompliance6, juniIpProfileRouterName=juniIpProfileRouterName, juniIpProfileDeprecatedGroup=juniIpProfileDeprecatedGroup, juniIpProfileIpAddr=juniIpProfileIpAddr, juniIpProfileMIB=juniIpProfileMIB, juniIpProfileRowStatus=juniIpProfileRowStatus, juniIpProfileAccessRoute=juniIpProfileAccessRoute, juniIpProfileCompliance7=juniIpProfileCompliance7, juniIpProfileInheritNumString=juniIpProfileInheritNumString, juniIpProfileGroup3=juniIpProfileGroup3, juniIpProfileObjects=juniIpProfileObjects, juniIpProfileLoopback=juniIpProfileLoopback, juniIpProfileGroup7=juniIpProfileGroup7, juniIpProfile=juniIpProfile, juniIpProfileFilterOptionsAll=juniIpProfileFilterOptionsAll, juniIpProfileCompliance4=juniIpProfileCompliance4, juniIpProfileCompliance3=juniIpProfileCompliance3, juniIpProfileFlowStats=juniIpProfileFlowStats, juniIpProfileSetMap=juniIpProfileSetMap, juniIpProfileMIBConformance=juniIpProfileMIBConformance, PYSNMP_MODULE_ID=juniIpProfileMIB, juniIpProfileCompliance=juniIpProfileCompliance, juniIpProfileCompliance2=juniIpProfileCompliance2, juniIpProfileCompliance1=juniIpProfileCompliance1, juniIpProfileMtu=juniIpProfileMtu, juniIpProfileEntry=juniIpProfileEntry, juniIpProfileGroup6=juniIpProfileGroup6, juniIpProfileIcmpRedirectEnable=juniIpProfileIcmpRedirectEnable, juniIpProfileCompliance5=juniIpProfileCompliance5, juniIpProfileGroup=juniIpProfileGroup, juniIpProfileGroup2=juniIpProfileGroup2, juniIpProfileMIBGroups=juniIpProfileMIBGroups, juniIpProfileGroup4=juniIpProfileGroup4, juniIpProfileGroup1=juniIpProfileGroup1, juniIpProfileLoopbackIfIndex=juniIpProfileLoopbackIfIndex, juniIpProfileMIBCompliances=juniIpProfileMIBCompliances, juniIpProfileBlockMulticastSources=juniIpProfileBlockMulticastSources)
