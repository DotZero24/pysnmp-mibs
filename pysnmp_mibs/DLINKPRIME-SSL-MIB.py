#
# PySNMP MIB module DLINKPRIME-SSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-SSL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
dlinkPrimeSslMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 16))
dlinkPrimeSslMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeSslMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeSslMIB.setOrganization('D-Link Corp.')
dpSslNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 16, 0))
dpSslObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 16, 1))
dpSslConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 16, 2))
dpSslConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 16, 1, 1))
dpSslServiceEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 16, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpSslServiceEnabled.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-SSL-MIB", dpSslServiceEnabled=dpSslServiceEnabled, PYSNMP_MODULE_ID=dlinkPrimeSslMIB, dlinkPrimeSslMIB=dlinkPrimeSslMIB, dpSslObjects=dpSslObjects, dpSslConformance=dpSslConformance, dpSslConfiguration=dpSslConfiguration, dpSslNotifications=dpSslNotifications)
