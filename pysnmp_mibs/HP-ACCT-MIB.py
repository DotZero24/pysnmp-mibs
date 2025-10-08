#
# PySNMP MIB module HP-ACCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ACCT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpSwitchAccountingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17))
hpSwitchAccountingMIB.setRevisions(('2019-09-26 00:00', '2017-11-22 00:00', '2014-08-04 00:00', '2011-03-05 00:00', '2009-07-14 00:00', '2008-07-11 00:00', '2001-08-22 02:38',))
if mibBuilder.loadTexts: hpSwitchAccountingMIB.setLastUpdated('201909260000Z')
if mibBuilder.loadTexts: hpSwitchAccountingMIB.setOrganization('HP Networking')
hpSwitchAccountingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1))
hpSwitchAcctUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 525600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAcctUpdateInterval.setStatus('current')
hpSwitchAcctSuppressNullUserName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAcctSuppressNullUserName.setStatus('current')
hpSwitchAcctSessionIdentification = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unique", 1), ("common", 2))).clone('unique')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAcctSessionIdentification.setStatus('current')
hpSwitchAcctSessIdIncSwitchIdentity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAcctSessIdIncSwitchIdentity.setStatus('current')
hpSwitchAcctServiceTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2), )
if mibBuilder.loadTexts: hpSwitchAcctServiceTable.setStatus('current')
hpSwitchAcctServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1), ).setIndexNames((0, "HP-ACCT-MIB", "hpSwitchAcctServiceIndex"))
if mibBuilder.loadTexts: hpSwitchAcctServiceEntry.setStatus('current')
hpSwitchAcctServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("network", 1), ("exec", 2), ("system", 3), ("commands", 4), ("restUri", 5))))
if mibBuilder.loadTexts: hpSwitchAcctServiceIndex.setStatus('current')
hpSwitchAcctServiceMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("radius", 2), ("syslog", 3), ("tacacs", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAcctServiceMethod.setStatus('current')
hpSwitchAcctServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("startStop", 2), ("stopOnly", 3), ("interimUpdate", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAcctServiceMode.setStatus('current')
hpSwitchAcctServiceServerGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAcctServiceServerGroupName.setStatus('current')
hpSwitchAccountingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3))
hpSwitchAccountingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 1))
hpSwitchAccountingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 2))
hpSwitchAccountingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 1, 1)).setObjects(("HP-ACCT-MIB", "hpSwitchAccountingConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAccountingMIBCompliance = hpSwitchAccountingMIBCompliance.setStatus('deprecated')
hpSwitchAccountingMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 1, 2)).setObjects(("HP-ACCT-MIB", "hpSwitchAccountingConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAccountingMIBCompliance1 = hpSwitchAccountingMIBCompliance1.setStatus('current')
hpSwitchAccountingConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 2, 1)).setObjects(("HP-ACCT-MIB", "hpSwitchAcctUpdateInterval"), ("HP-ACCT-MIB", "hpSwitchAcctSuppressNullUserName"), ("HP-ACCT-MIB", "hpSwitchAcctSessionIdentification"), ("HP-ACCT-MIB", "hpSwitchAcctServiceMethod"), ("HP-ACCT-MIB", "hpSwitchAcctServiceMode"), ("HP-ACCT-MIB", "hpSwitchAcctServiceServerGroupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAccountingConfigGroup = hpSwitchAccountingConfigGroup.setStatus('deprecated')
hpSwitchAccountingConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17, 3, 2, 2)).setObjects(("HP-ACCT-MIB", "hpSwitchAcctUpdateInterval"), ("HP-ACCT-MIB", "hpSwitchAcctSuppressNullUserName"), ("HP-ACCT-MIB", "hpSwitchAcctSessionIdentification"), ("HP-ACCT-MIB", "hpSwitchAcctServiceMethod"), ("HP-ACCT-MIB", "hpSwitchAcctServiceMode"), ("HP-ACCT-MIB", "hpSwitchAcctServiceServerGroupName"), ("HP-ACCT-MIB", "hpSwitchAcctSessIdIncSwitchIdentity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAccountingConfigGroup1 = hpSwitchAccountingConfigGroup1.setStatus('current')
mibBuilder.exportSymbols("HP-ACCT-MIB", hpSwitchAccountingMIBConformance=hpSwitchAccountingMIBConformance, hpSwitchAcctServiceTable=hpSwitchAcctServiceTable, hpSwitchAcctSuppressNullUserName=hpSwitchAcctSuppressNullUserName, hpSwitchAccountingConfigGroup1=hpSwitchAccountingConfigGroup1, hpSwitchAccountingMIB=hpSwitchAccountingMIB, hpSwitchAcctServiceServerGroupName=hpSwitchAcctServiceServerGroupName, hpSwitchAccountingMIBCompliances=hpSwitchAccountingMIBCompliances, hpSwitchAcctSessionIdentification=hpSwitchAcctSessionIdentification, hpSwitchAccountingMIBGroups=hpSwitchAccountingMIBGroups, hpSwitchAcctSessIdIncSwitchIdentity=hpSwitchAcctSessIdIncSwitchIdentity, hpSwitchAccountingMIBCompliance=hpSwitchAccountingMIBCompliance, hpSwitchAcctServiceMode=hpSwitchAcctServiceMode, PYSNMP_MODULE_ID=hpSwitchAccountingMIB, hpSwitchAcctUpdateInterval=hpSwitchAcctUpdateInterval, hpSwitchAcctServiceEntry=hpSwitchAcctServiceEntry, hpSwitchAcctServiceIndex=hpSwitchAcctServiceIndex, hpSwitchAcctServiceMethod=hpSwitchAcctServiceMethod, hpSwitchAccountingConfig=hpSwitchAccountingConfig, hpSwitchAccountingConfigGroup=hpSwitchAccountingConfigGroup, hpSwitchAccountingMIBCompliance1=hpSwitchAccountingMIBCompliance1)
