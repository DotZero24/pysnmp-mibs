#
# PySNMP MIB module DLINKPRIME-SSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-SSL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("DLINKPRIME-SSL-MIB", dpSslConfiguration=dpSslConfiguration, dpSslConformance=dpSslConformance, dpSslServiceEnabled=dpSslServiceEnabled, dpSslNotifications=dpSslNotifications, dlinkPrimeSslMIB=dlinkPrimeSslMIB, dpSslObjects=dpSslObjects, PYSNMP_MODULE_ID=dlinkPrimeSslMIB)
