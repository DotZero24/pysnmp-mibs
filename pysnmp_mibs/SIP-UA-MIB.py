#
# PySNMP MIB module SIP-UA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/SIP-UA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
applIndex, = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
SipTCEntityRole, = mibBuilder.importSymbols("SIP-TC-MIB", "SipTCEntityRole")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SIP-UA-MIB", sipUAMIBObjects=sipUAMIBObjects, sipUACompliance=sipUACompliance, sipUACfgServer=sipUACfgServer, sipUAMIBCompliances=sipUAMIBCompliances, sipUACfgServerTable=sipUACfgServerTable, sipUACfgServerAddressType=sipUACfgServerAddressType, sipUACfgServerIndex=sipUACfgServerIndex, sipUAMIB=sipUAMIB, sipUAMIBGroups=sipUAMIBGroups, sipUAMIBConformance=sipUAMIBConformance, PYSNMP_MODULE_ID=sipUAMIB, sipUACfgServerEntry=sipUACfgServerEntry, sipUACfgServerRole=sipUACfgServerRole, sipUACfgServerAddress=sipUACfgServerAddress, sipUAConfigGroup=sipUAConfigGroup)
