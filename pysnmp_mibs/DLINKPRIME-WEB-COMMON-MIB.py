#
# PySNMP MIB module DLINKPRIME-WEB-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-WEB-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
dlinkPrimeWebCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 28))
dlinkPrimeWebCommonMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeWebCommonMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeWebCommonMIB.setOrganization('D-Link Corp.')
dpWebCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 28, 0))
dpWebMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 28, 1))
dpWebCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 28, 2))
dpWebSessionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 1))
dpSslServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 2))
dpWebSessionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 36000)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpWebSessionTimeout.setStatus('current')
dpSslServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 28, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpSslServerStatus.setStatus('current')
dpWebCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 1))
dpWebCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 2))
dpWebMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 1, 1)).setObjects(("DLINKPRIME-WEB-COMMON-MIB", "dpWebSessionGroups"), ("DLINKPRIME-WEB-COMMON-MIB", "dpSslServerGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpWebMIBCompliance = dpWebMIBCompliance.setStatus('current')
dpWebSessionGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 2, 1)).setObjects(("DLINKPRIME-WEB-COMMON-MIB", "dpWebSessionTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpWebSessionGroups = dpWebSessionGroups.setStatus('current')
dpSslServerGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 28, 2, 2, 2)).setObjects(("DLINKPRIME-WEB-COMMON-MIB", "dpSslServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpSslServerGroups = dpSslServerGroups.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-WEB-COMMON-MIB", PYSNMP_MODULE_ID=dlinkPrimeWebCommonMIB, dpWebMIBCompliance=dpWebMIBCompliance, dpWebSessionGroups=dpWebSessionGroups, dpSslServerStatus=dpSslServerStatus, dpWebCommonMIBCompliances=dpWebCommonMIBCompliances, dpSslServerGroups=dpSslServerGroups, dlinkPrimeWebCommonMIB=dlinkPrimeWebCommonMIB, dpSslServerObjects=dpSslServerObjects, dpWebCommonGroups=dpWebCommonGroups, dpWebMIBObjects=dpWebMIBObjects, dpWebCommonMIBNotifications=dpWebCommonMIBNotifications, dpWebSessionObjects=dpWebSessionObjects, dpWebCommonMIBConformance=dpWebCommonMIBConformance, dpWebSessionTimeout=dpWebSessionTimeout)
