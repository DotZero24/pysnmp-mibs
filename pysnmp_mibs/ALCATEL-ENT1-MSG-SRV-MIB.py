#
# PySNMP MIB module ALCATEL-ENT1-MSG-SRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel-ent1/ALCATEL-ENT1-MSG-SRV-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
softentIND1MsgSrvMIB, = mibBuilder.importSymbols("ALCATEL-ENT1-BASE", "softentIND1MsgSrvMIB")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "DateAndTime", "TextualConvention")
alcatelIND1MsgSrvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1))
alcatelIND1MsgSrvMIB.setRevisions(('2013-06-05 00:00',))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIB.setLastUpdated('201306050000Z')
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIB.setOrganization('Alcatel - Architects Of An Internet World')
alcatelIND1MsgSrvMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 0))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBNotifications.setStatus('current')
alcatelIND1MsgSrvMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBObjects.setStatus('current')
alcatelIND1MsgSrvMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBConformance.setStatus('current')
alcatelIND1MsgSrvMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBGroups.setStatus('current')
alcatelIND1MsgSrvMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1MsgSrvMIBCompliances.setStatus('current')
alaMsgSrvGlobalConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaMsgSrvGlobalConfigStatus.setStatus('current')
alaMsgSrvGlobalRestart = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("restart", 2))).clone('inactive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaMsgSrvGlobalRestart.setStatus('current')
alcatelIND1MsgSrvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 2, 1)).setObjects(("ALCATEL-ENT1-MSG-SRV-MIB", "alaMsgSrvGlobalConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1MsgSrvMIBCompliance = alcatelIND1MsgSrvMIBCompliance.setStatus('current')
alaMsgSrvGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 79, 1, 2, 1, 1)).setObjects(("ALCATEL-ENT1-MSG-SRV-MIB", "alaMsgSrvGlobalConfigStatus"), ("ALCATEL-ENT1-MSG-SRV-MIB", "alaMsgSrvGlobalRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaMsgSrvGlobalConfigGroup = alaMsgSrvGlobalConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-ENT1-MSG-SRV-MIB", alcatelIND1MsgSrvMIBNotifications=alcatelIND1MsgSrvMIBNotifications, alcatelIND1MsgSrvMIBConformance=alcatelIND1MsgSrvMIBConformance, PYSNMP_MODULE_ID=alcatelIND1MsgSrvMIB, alcatelIND1MsgSrvMIB=alcatelIND1MsgSrvMIB, alcatelIND1MsgSrvMIBGroups=alcatelIND1MsgSrvMIBGroups, alcatelIND1MsgSrvMIBCompliances=alcatelIND1MsgSrvMIBCompliances, alaMsgSrvGlobalRestart=alaMsgSrvGlobalRestart, alaMsgSrvGlobalConfigStatus=alaMsgSrvGlobalConfigStatus, alcatelIND1MsgSrvMIBObjects=alcatelIND1MsgSrvMIBObjects, alcatelIND1MsgSrvMIBCompliance=alcatelIND1MsgSrvMIBCompliance, alaMsgSrvGlobalConfigGroup=alaMsgSrvGlobalConfigGroup)
