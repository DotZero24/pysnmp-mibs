#
# PySNMP MIB module DES7200-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DES7200-NTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:59:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
myNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49))
myNtpMIB.setRevisions(('2009-05-14 00:00',))
if mibBuilder.loadTexts: myNtpMIB.setLastUpdated('200905140000Z')
if mibBuilder.loadTexts: myNtpMIB.setOrganization('D-Link Crop.')
myNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1))
myNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2))
myntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1))
myNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 1))
myNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 2))
class NTPTimeStamp(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPSignedTimeValue(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPUnsignedTimeValue(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NTPRefId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

myntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myntpSysLeap.setStatus('mandatory')
myntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myntpSysStratum.setStatus('mandatory')
myntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-24, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysPrecision.setStatus('mandatory')
myntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 4), NTPSignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRootDelay.setStatus('mandatory')
myntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 5), NTPUnsignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRootDispersion.setStatus('mandatory')
myntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRefId.setStatus('mandatory')
myntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRefTime.setStatus('mandatory')
myNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 2, 1)).setObjects(("DES7200-NTP-MIB", "myntpSysLeap"), ("DES7200-NTP-MIB", "myntpSysStratum"), ("DES7200-NTP-MIB", "myntpSysPrecision"), ("DES7200-NTP-MIB", "myntpSysRootDelay"), ("DES7200-NTP-MIB", "myntpSysRootDispersion"), ("DES7200-NTP-MIB", "myntpSysRefId"), ("DES7200-NTP-MIB", "myntpSysRefTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNtpSysGroup = myNtpSysGroup.setStatus('current')
myNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 1, 1)).setObjects(("DES7200-NTP-MIB", "myNtpMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNtpMIBCompliance = myNtpMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("DES7200-NTP-MIB", NTPSignedTimeValue=NTPSignedTimeValue, myNtpMIBCompliances=myNtpMIBCompliances, NTPLeapIndicator=NTPLeapIndicator, myntpSysRootDispersion=myntpSysRootDispersion, NTPUnsignedTimeValue=NTPUnsignedTimeValue, myntpSysRefId=myntpSysRefId, myNtpMIBCompliance=myNtpMIBCompliance, NTPStratum=NTPStratum, myntpSysRefTime=myntpSysRefTime, myntpSysRootDelay=myntpSysRootDelay, myNtpMIB=myNtpMIB, myNtpMIBObjects=myNtpMIBObjects, myntpSysPrecision=myntpSysPrecision, myntpSysLeap=myntpSysLeap, myNtpMIBGroups=myNtpMIBGroups, myntpSysStratum=myntpSysStratum, NTPRefId=NTPRefId, myntpSystem=myntpSystem, NTPTimeStamp=NTPTimeStamp, myNtpMIBConformance=myNtpMIBConformance, myNtpSysGroup=myNtpSysGroup, PYSNMP_MODULE_ID=myNtpMIB)
