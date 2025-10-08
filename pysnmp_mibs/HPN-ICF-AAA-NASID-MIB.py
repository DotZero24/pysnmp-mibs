#
# PySNMP MIB module HPN-ICF-AAA-NASID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-AAA-NASID-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfAAANasId = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114))
hpnicfAAANasId.setRevisions(('2011-03-09 09:45',))
if mibBuilder.loadTexts: hpnicfAAANasId.setLastUpdated('201103090945Z')
if mibBuilder.loadTexts: hpnicfAAANasId.setOrganization('')
hpnicfAAANasIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1))
hpnicfAAANasIdTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1), )
if mibBuilder.loadTexts: hpnicfAAANasIdTable.setStatus('current')
hpnicfAAANasIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-AAA-NASID-MIB", "hpnicfAAANasIdName"))
if mibBuilder.loadTexts: hpnicfAAANasIdEntry.setStatus('current')
hpnicfAAANasIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfAAANasIdName.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-AAA-NASID-MIB", hpnicfAAANasIdName=hpnicfAAANasIdName, hpnicfAAANasIdTable=hpnicfAAANasIdTable, PYSNMP_MODULE_ID=hpnicfAAANasId, hpnicfAAANasId=hpnicfAAANasId, hpnicfAAANasIdObjects=hpnicfAAANasIdObjects, hpnicfAAANasIdEntry=hpnicfAAANasIdEntry)
