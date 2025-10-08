#
# PySNMP MIB module ALCATEL-ENT1-AL-SRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel-ent1/ALCATEL-ENT1-AL-SRV-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:58 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
softentIND1ActiveLeaseSrvMIB, = mibBuilder.importSymbols("ALCATEL-ENT1-BASE", "softentIND1ActiveLeaseSrvMIB")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "DateAndTime", "TextualConvention")
alcatelIND1ActiveLeaseSrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1))
alcatelIND1ActiveLeaseSrvMIB.setRevisions(('2013-06-05 00:00',))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIB.setLastUpdated('201306050000Z')
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1ActiveLeaseSrvMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 0))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBNotifications.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBObjects.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBConformance.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBGroups.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1ActiveLeaseSrvMIBCompliances.setStatus('current')
alaActiveLeaseSrvGlobalConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaActiveLeaseSrvGlobalConfigStatus.setStatus('current')
alaActiveLeaseSrvGlobalRestart = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("restart", 2))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaActiveLeaseSrvGlobalRestart.setStatus('current')
alcatelIND1ActiveLeaseSrvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 2, 1)).setObjects(("ALCATEL-ENT1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1ActiveLeaseSrvMIBCompliance = alcatelIND1ActiveLeaseSrvMIBCompliance.setStatus('current')
alaActiveLeaseSrvGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 80, 1, 2, 1, 1)).setObjects(("ALCATEL-ENT1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalConfigStatus"), ("ALCATEL-ENT1-AL-SRV-MIB", "alaActiveLeaseSrvGlobalRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaActiveLeaseSrvGlobalConfigGroup = alaActiveLeaseSrvGlobalConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-ENT1-AL-SRV-MIB", alcatelIND1ActiveLeaseSrvMIB=alcatelIND1ActiveLeaseSrvMIB, alcatelIND1ActiveLeaseSrvMIBObjects=alcatelIND1ActiveLeaseSrvMIBObjects, alcatelIND1ActiveLeaseSrvMIBNotifications=alcatelIND1ActiveLeaseSrvMIBNotifications, alaActiveLeaseSrvGlobalConfigStatus=alaActiveLeaseSrvGlobalConfigStatus, PYSNMP_MODULE_ID=alcatelIND1ActiveLeaseSrvMIB, alcatelIND1ActiveLeaseSrvMIBGroups=alcatelIND1ActiveLeaseSrvMIBGroups, alcatelIND1ActiveLeaseSrvMIBConformance=alcatelIND1ActiveLeaseSrvMIBConformance, alaActiveLeaseSrvGlobalConfigGroup=alaActiveLeaseSrvGlobalConfigGroup, alcatelIND1ActiveLeaseSrvMIBCompliance=alcatelIND1ActiveLeaseSrvMIBCompliance, alaActiveLeaseSrvGlobalRestart=alaActiveLeaseSrvGlobalRestart, alcatelIND1ActiveLeaseSrvMIBCompliances=alcatelIND1ActiveLeaseSrvMIBCompliances)
