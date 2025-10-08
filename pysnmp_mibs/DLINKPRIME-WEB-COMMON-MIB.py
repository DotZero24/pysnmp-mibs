#
# PySNMP MIB module DLINKPRIME-WEB-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-WEB-COMMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DLINKPRIME-WEB-COMMON-MIB", dpSslServerObjects=dpSslServerObjects, dlinkPrimeWebCommonMIB=dlinkPrimeWebCommonMIB, dpWebMIBObjects=dpWebMIBObjects, PYSNMP_MODULE_ID=dlinkPrimeWebCommonMIB, dpSslServerStatus=dpSslServerStatus, dpSslServerGroups=dpSslServerGroups, dpWebSessionTimeout=dpWebSessionTimeout, dpWebSessionGroups=dpWebSessionGroups, dpWebCommonGroups=dpWebCommonGroups, dpWebMIBCompliance=dpWebMIBCompliance, dpWebSessionObjects=dpWebSessionObjects, dpWebCommonMIBCompliances=dpWebCommonMIBCompliances, dpWebCommonMIBConformance=dpWebCommonMIBConformance, dpWebCommonMIBNotifications=dpWebCommonMIBNotifications)
