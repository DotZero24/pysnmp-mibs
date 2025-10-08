#
# PySNMP MIB module INT-SERV-GUARANTEED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/INT-SERV-GUARANTEED-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
intSrv, = mibBuilder.importSymbols("INT-SERV-MIB", "intSrv")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
intSrvGuaranteed = ModuleIdentity((1, 3, 6, 1, 2, 1, 52, 4))
if mibBuilder.loadTexts: intSrvGuaranteed.setLastUpdated('9511030500Z')
if mibBuilder.loadTexts: intSrvGuaranteed.setOrganization('IETF Integrated Services Working Group')
intSrvGuaranteedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 1))
intSrvGuaranteedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 2))
intSrvGuaranteedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3))
intSrvGuaranteedIfTable = MibTable((1, 3, 6, 1, 2, 1, 52, 4, 1, 1), )
if mibBuilder.loadTexts: intSrvGuaranteedIfTable.setStatus('current')
intSrvGuaranteedIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: intSrvGuaranteedIfEntry.setStatus('current')
intSrvGuaranteedIfC = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfC.setStatus('current')
intSrvGuaranteedIfD = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfD.setStatus('current')
intSrvGuaranteedIfSlack = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 268435455))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfSlack.setStatus('current')
intSrvGuaranteedIfStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 52, 4, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: intSrvGuaranteedIfStatus.setStatus('current')
intSrvGuaranteedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3, 1))
intSrvGuaranteedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 52, 4, 3, 2))
intSrvGuaranteedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 52, 4, 3, 2, 1)).setObjects(("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfAttribGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedCompliance = intSrvGuaranteedCompliance.setStatus('current')
intSrvGuaranteedIfAttribGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 52, 4, 3, 1, 2)).setObjects(("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfC"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfD"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfSlack"), ("INT-SERV-GUARANTEED-MIB", "intSrvGuaranteedIfStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    intSrvGuaranteedIfAttribGroup = intSrvGuaranteedIfAttribGroup.setStatus('current')
mibBuilder.exportSymbols("INT-SERV-GUARANTEED-MIB", intSrvGuaranteedIfSlack=intSrvGuaranteedIfSlack, intSrvGuaranteedConformance=intSrvGuaranteedConformance, intSrvGuaranteedObjects=intSrvGuaranteedObjects, intSrvGuaranteedIfStatus=intSrvGuaranteedIfStatus, intSrvGuaranteedGroups=intSrvGuaranteedGroups, intSrvGuaranteedIfD=intSrvGuaranteedIfD, intSrvGuaranteedCompliance=intSrvGuaranteedCompliance, intSrvGuaranteedCompliances=intSrvGuaranteedCompliances, intSrvGuaranteedIfC=intSrvGuaranteedIfC, intSrvGuaranteedNotifications=intSrvGuaranteedNotifications, PYSNMP_MODULE_ID=intSrvGuaranteed, intSrvGuaranteedIfEntry=intSrvGuaranteedIfEntry, intSrvGuaranteedIfAttribGroup=intSrvGuaranteedIfAttribGroup, intSrvGuaranteed=intSrvGuaranteed, intSrvGuaranteedIfTable=intSrvGuaranteedIfTable)
