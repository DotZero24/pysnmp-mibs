#
# PySNMP MIB module ALCATEL-ENT1-MSG-SRV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel-ent1/ALCATEL-ENT1-MSG-SRV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:59:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
softentIND1MsgSrvMIB, = mibBuilder.importSymbols("ALCATEL-ENT1-BASE", "softentIND1MsgSrvMIB")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALCATEL-ENT1-MSG-SRV-MIB", PYSNMP_MODULE_ID=alcatelIND1MsgSrvMIB, alcatelIND1MsgSrvMIBCompliance=alcatelIND1MsgSrvMIBCompliance, alaMsgSrvGlobalConfigGroup=alaMsgSrvGlobalConfigGroup, alcatelIND1MsgSrvMIBConformance=alcatelIND1MsgSrvMIBConformance, alcatelIND1MsgSrvMIBNotifications=alcatelIND1MsgSrvMIBNotifications, alaMsgSrvGlobalRestart=alaMsgSrvGlobalRestart, alcatelIND1MsgSrvMIBCompliances=alcatelIND1MsgSrvMIBCompliances, alcatelIND1MsgSrvMIB=alcatelIND1MsgSrvMIB, alcatelIND1MsgSrvMIBObjects=alcatelIND1MsgSrvMIBObjects, alaMsgSrvGlobalConfigStatus=alaMsgSrvGlobalConfigStatus, alcatelIND1MsgSrvMIBGroups=alcatelIND1MsgSrvMIBGroups)
