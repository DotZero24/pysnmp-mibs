#
# PySNMP MIB module MPKEEPALIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/maipu/MPKEEPALIVE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectSyntax, Counter32, ModuleIdentity, TimeTicks, Counter64, ObjectIdentity, Gauge32, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectSyntax", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "ObjectName")
RowStatus, DateAndTime, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("MPKEEPALIVE-MIB", mpKaRetry=mpKaRetry, mpKeepaliveMib=mpKeepaliveMib, mpKaGateway=mpKaGateway, mpKaIfNmae=mpKaIfNmae, mpKeepaliveEntry=mpKeepaliveEntry, mpKaRowstatus=mpKaRowstatus, PYSNMP_MODULE_ID=mpKeepaliveMib, mpKaTimeout=mpKaTimeout, mpKeepaliveTable=mpKeepaliveTable)
