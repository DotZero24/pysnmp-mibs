#
# PySNMP MIB module SCTE-HMS-HEADENDIDENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/scte/SCTE-HMS-HEADENDIDENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
insidePlantIdent, = mibBuilder.importSymbols("SCTE-HMS-ROOTS", "insidePlantIdent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("SCTE-HMS-HEADENDIDENT-MIB", heBaseIdent=heBaseIdent, HeTenthdBmV=HeTenthdBmV, heCommon=heCommon, HeTenthCentigrade=HeTenthCentigrade, HeLaserType=HeLaserType, HeFaultStatus=HeFaultStatus, HeOnOffControl=HeOnOffControl, HeTenthVolt=HeTenthVolt, PYSNMP_MODULE_ID=headEndIdentMib, heOptics=heOptics, heRF=heRF, HeTenthdBm=HeTenthdBm, heFans=heFans, HeMilliAmp=HeMilliAmp, HeHundredthNanoMeter=HeHundredthNanoMeter, heHMTS=heHMTS, hePowerSupply=hePowerSupply, headEndIdentMib=headEndIdentMib, HeOnOffStatus=HeOnOffStatus, heManagedServer=heManagedServer, HeHundredthWatts=HeHundredthWatts, heDigital=heDigital, HeTenthdB=HeTenthdB)
