#
# PySNMP MIB module Brocade-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/Brocade-REG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcsi = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588))
bcsi.setRevisions(('2012-02-03 00:00',))
if mibBuilder.loadTexts: bcsi.setLastUpdated('201202030000Z')
if mibBuilder.loadTexts: bcsi.setOrganization(' Brocade Communications Systems, Inc.')
commDev = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2))
if mibBuilder.loadTexts: commDev.setStatus('current')
fibrechannel = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1))
if mibBuilder.loadTexts: fibrechannel.setStatus('current')
nos = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 2))
if mibBuilder.loadTexts: nos.setStatus('current')
fcSwitch = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1))
if mibBuilder.loadTexts: fcSwitch.setStatus('current')
bcsiReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3))
if mibBuilder.loadTexts: bcsiReg.setStatus('current')
bcsiModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1))
if mibBuilder.loadTexts: bcsiModules.setStatus('current')
brocadeAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 2))
if mibBuilder.loadTexts: brocadeAgentCapability.setStatus('current')
mibBuilder.exportSymbols("Brocade-REG-MIB", bcsi=bcsi, nos=nos, PYSNMP_MODULE_ID=bcsi, fibrechannel=fibrechannel, bcsiReg=bcsiReg, fcSwitch=fcSwitch, bcsiModules=bcsiModules, brocadeAgentCapability=brocadeAgentCapability, commDev=commDev)
