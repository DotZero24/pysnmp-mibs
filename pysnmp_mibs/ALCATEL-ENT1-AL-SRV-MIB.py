#
# PySNMP MIB module ALCATEL-ENT1-AL-SRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel-ent1/ALCATEL-ENT1-AL-SRV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:00:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
softentIND1ActiveLeaseSrvMIB, = mibBuilder.importSymbols("ALCATEL-ENT1-BASE", "softentIND1ActiveLeaseSrvMIB")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALCATEL-ENT1-AL-SRV-MIB", PYSNMP_MODULE_ID=alcatelIND1ActiveLeaseSrvMIB, alaActiveLeaseSrvGlobalConfigGroup=alaActiveLeaseSrvGlobalConfigGroup, alaActiveLeaseSrvGlobalRestart=alaActiveLeaseSrvGlobalRestart, alcatelIND1ActiveLeaseSrvMIBObjects=alcatelIND1ActiveLeaseSrvMIBObjects, alcatelIND1ActiveLeaseSrvMIBCompliance=alcatelIND1ActiveLeaseSrvMIBCompliance, alcatelIND1ActiveLeaseSrvMIBNotifications=alcatelIND1ActiveLeaseSrvMIBNotifications, alcatelIND1ActiveLeaseSrvMIBGroups=alcatelIND1ActiveLeaseSrvMIBGroups, alcatelIND1ActiveLeaseSrvMIBCompliances=alcatelIND1ActiveLeaseSrvMIBCompliances, alaActiveLeaseSrvGlobalConfigStatus=alaActiveLeaseSrvGlobalConfigStatus, alcatelIND1ActiveLeaseSrvMIBConformance=alcatelIND1ActiveLeaseSrvMIBConformance, alcatelIND1ActiveLeaseSrvMIB=alcatelIND1ActiveLeaseSrvMIB)
