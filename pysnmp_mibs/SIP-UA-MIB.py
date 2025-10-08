#
# PySNMP MIB module SIP-UA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SIP-UA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
applIndex, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
SipTCEntityRole, = mibBuilder.importSymbols("SIP-TC-MIB", "SipTCEntityRole")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sipUAMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 150))
sipUAMIB.setRevisions(('2007-04-20 00:00',))
if mibBuilder.loadTexts: sipUAMIB.setLastUpdated('200704200000Z')
if mibBuilder.loadTexts: sipUAMIB.setOrganization('IETF Session Initiation Protocol Working Group')
sipUAMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 1))
sipUAMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 2))
sipUACfgServer = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 1, 1))
sipUACfgServerTable = MibTable((1, 3, 6, 1, 2, 1, 150, 1, 1, 1), )
if mibBuilder.loadTexts: sipUACfgServerTable.setStatus('current')
sipUACfgServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-UA-MIB", "sipUACfgServerIndex"))
if mibBuilder.loadTexts: sipUACfgServerEntry.setStatus('current')
sipUACfgServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sipUACfgServerIndex.setStatus('current')
sipUACfgServerAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipUACfgServerAddressType.setStatus('current')
sipUACfgServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipUACfgServerAddress.setStatus('current')
sipUACfgServerRole = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 4), SipTCEntityRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipUACfgServerRole.setStatus('current')
sipUAMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 2, 1))
sipUAMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 2, 2))
sipUACompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 150, 2, 1, 1)).setObjects(("SIP-UA-MIB", "sipUAConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipUACompliance = sipUACompliance.setStatus('current')
sipUAConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 150, 2, 2, 1)).setObjects(("SIP-UA-MIB", "sipUACfgServerAddressType"), ("SIP-UA-MIB", "sipUACfgServerAddress"), ("SIP-UA-MIB", "sipUACfgServerRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipUAConfigGroup = sipUAConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SIP-UA-MIB", sipUAMIBGroups=sipUAMIBGroups, sipUACfgServer=sipUACfgServer, sipUAMIB=sipUAMIB, sipUAMIBObjects=sipUAMIBObjects, sipUACfgServerAddressType=sipUACfgServerAddressType, sipUAMIBCompliances=sipUAMIBCompliances, sipUACfgServerRole=sipUACfgServerRole, sipUAConfigGroup=sipUAConfigGroup, sipUACfgServerIndex=sipUACfgServerIndex, sipUACfgServerEntry=sipUACfgServerEntry, sipUACfgServerAddress=sipUACfgServerAddress, sipUAMIBConformance=sipUAMIBConformance, sipUACompliance=sipUACompliance, PYSNMP_MODULE_ID=sipUAMIB, sipUACfgServerTable=sipUACfgServerTable)
