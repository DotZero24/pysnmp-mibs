#
# PySNMP MIB module MPKEEPALIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/maipu/MPKEEPALIVE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectSyntax, iso, MibIdentifier, ObjectName, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectSyntax", "iso", "MibIdentifier", "ObjectName", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
mpKeepaliveMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651, 3, 800))
if mibBuilder.loadTexts: mpKeepaliveMib.setLastUpdated('0704060952Z')
if mibBuilder.loadTexts: mpKeepaliveMib.setOrganization('ĴͨŹɷ\u07b9˾, Maipu (Sichuan) Communication Technology Co. LTD.')
mpKeepaliveTable = MibTable((1, 3, 6, 1, 4, 1, 5651, 3, 800, 1), )
if mibBuilder.loadTexts: mpKeepaliveTable.setStatus('current')
mpKeepaliveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1), ).setIndexNames((0, "MPKEEPALIVE-MIB", "mpIfNmae"))
if mibBuilder.loadTexts: mpKeepaliveEntry.setStatus('current')
mpKaIfNmae = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: mpKaIfNmae.setStatus('current')
mpKaTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpKaTimeout.setStatus('current')
mpKaRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpKaRetry.setStatus('current')
mpKaGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpKaGateway.setStatus('current')
mpKaRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5651, 3, 800, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpKaRowstatus.setStatus('current')
mibBuilder.exportSymbols("MPKEEPALIVE-MIB", mpKaRowstatus=mpKaRowstatus, mpKaTimeout=mpKaTimeout, mpKeepaliveEntry=mpKeepaliveEntry, PYSNMP_MODULE_ID=mpKeepaliveMib, mpKaRetry=mpKaRetry, mpKeepaliveMib=mpKeepaliveMib, mpKaGateway=mpKaGateway, mpKeepaliveTable=mpKeepaliveTable, mpKaIfNmae=mpKaIfNmae)
