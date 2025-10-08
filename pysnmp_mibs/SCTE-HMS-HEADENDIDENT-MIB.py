#
# PySNMP MIB module SCTE-HMS-HEADENDIDENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/scte/SCTE-HMS-HEADENDIDENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
insidePlantIdent, = mibBuilder.importSymbols("SCTE-HMS-ROOTS", "insidePlantIdent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
headEndIdentMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 0))
headEndIdentMib.setRevisions(('2008-01-16 13:00', '2007-10-03 00:00',))
if mibBuilder.loadTexts: headEndIdentMib.setLastUpdated('200801161300Z')
if mibBuilder.loadTexts: headEndIdentMib.setOrganization('SCTE HMS Working Group')
heOptics = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 1))
if mibBuilder.loadTexts: heOptics.setStatus('current')
heBaseIdent = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2))
if mibBuilder.loadTexts: heBaseIdent.setStatus('current')
heCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1))
if mibBuilder.loadTexts: heCommon.setStatus('current')
hePowerSupply = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2))
if mibBuilder.loadTexts: hePowerSupply.setStatus('current')
heFans = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3))
if mibBuilder.loadTexts: heFans.setStatus('current')
heHMTS = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 3))
if mibBuilder.loadTexts: heHMTS.setStatus('current')
heRF = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 4))
if mibBuilder.loadTexts: heRF.setStatus('current')
heDigital = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5))
if mibBuilder.loadTexts: heDigital.setStatus('current')
heManagedServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 6))
if mibBuilder.loadTexts: heManagedServer.setStatus('current')
class HeTenthVolt(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeTenthdBm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeTenthdBmV(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeTenthCentigrade(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeHundredthNanoMeter(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-2'

class HeTenthdB(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class HeOnOffControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("meaningless", 3))

class HeOnOffStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("off", 1), ("on", 2))

class HeFaultStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("fault", 2))

class HeLaserType(DisplayString):
    status = 'current'

class HeMilliAmp(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-3'

class HeHundredthWatts(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-2'

mibBuilder.exportSymbols("SCTE-HMS-HEADENDIDENT-MIB", heHMTS=heHMTS, heDigital=heDigital, HeTenthVolt=HeTenthVolt, HeTenthCentigrade=HeTenthCentigrade, HeMilliAmp=HeMilliAmp, HeTenthdB=HeTenthdB, HeOnOffControl=HeOnOffControl, HeOnOffStatus=HeOnOffStatus, HeTenthdBm=HeTenthdBm, hePowerSupply=hePowerSupply, PYSNMP_MODULE_ID=headEndIdentMib, heBaseIdent=heBaseIdent, heOptics=heOptics, heCommon=heCommon, HeTenthdBmV=HeTenthdBmV, HeLaserType=HeLaserType, heRF=heRF, HeHundredthNanoMeter=HeHundredthNanoMeter, heFans=heFans, headEndIdentMib=headEndIdentMib, heManagedServer=heManagedServer, HeHundredthWatts=HeHundredthWatts, HeFaultStatus=HeFaultStatus)
