_B='d-1'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
insidePlantIdent,=mibBuilder.importSymbols('SCTE-HMS-ROOTS','insidePlantIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
headEndIdentMib=ModuleIdentity((1,3,6,1,4,1,5591,1,11,0))
if mibBuilder.loadTexts:headEndIdentMib.setRevisions(('2008-01-16 13:00','2007-10-03 00:00'))
class HeTenthVolt(TextualConvention,Integer32):status=_A;displayHint=_B
class HeTenthdBm(TextualConvention,Integer32):status=_A;displayHint=_B
class HeTenthdBmV(TextualConvention,Integer32):status=_A;displayHint=_B
class HeTenthCentigrade(TextualConvention,Integer32):status=_A;displayHint=_B
class HeHundredthNanoMeter(TextualConvention,Unsigned32):status=_A;displayHint='d-2'
class HeTenthdB(TextualConvention,Integer32):status=_A;displayHint=_B
class HeOnOffControl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('on',2),('meaningless',3)))
class HeOnOffStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
class HeFaultStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('fault',2)))
class HeLaserType(DisplayString):status=_A
class HeMilliAmp(TextualConvention,Unsigned32):status=_A;displayHint='d-3'
class HeHundredthWatts(TextualConvention,Unsigned32):status=_A;displayHint='d-2'
_HeOptics_ObjectIdentity=ObjectIdentity
heOptics=_HeOptics_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1))
if mibBuilder.loadTexts:heOptics.setStatus(_A)
_HeBaseIdent_ObjectIdentity=ObjectIdentity
heBaseIdent=_HeBaseIdent_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2))
if mibBuilder.loadTexts:heBaseIdent.setStatus(_A)
_HeCommon_ObjectIdentity=ObjectIdentity
heCommon=_HeCommon_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1))
if mibBuilder.loadTexts:heCommon.setStatus(_A)
_HePowerSupply_ObjectIdentity=ObjectIdentity
hePowerSupply=_HePowerSupply_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,2))
if mibBuilder.loadTexts:hePowerSupply.setStatus(_A)
_HeFans_ObjectIdentity=ObjectIdentity
heFans=_HeFans_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,3))
if mibBuilder.loadTexts:heFans.setStatus(_A)
_HeHMTS_ObjectIdentity=ObjectIdentity
heHMTS=_HeHMTS_ObjectIdentity((1,3,6,1,4,1,5591,1,11,3))
if mibBuilder.loadTexts:heHMTS.setStatus(_A)
_HeRF_ObjectIdentity=ObjectIdentity
heRF=_HeRF_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4))
if mibBuilder.loadTexts:heRF.setStatus(_A)
_HeDigital_ObjectIdentity=ObjectIdentity
heDigital=_HeDigital_ObjectIdentity((1,3,6,1,4,1,5591,1,11,5))
if mibBuilder.loadTexts:heDigital.setStatus(_A)
_HeManagedServer_ObjectIdentity=ObjectIdentity
heManagedServer=_HeManagedServer_ObjectIdentity((1,3,6,1,4,1,5591,1,11,6))
if mibBuilder.loadTexts:heManagedServer.setStatus(_A)
mibBuilder.exportSymbols('SCTE-HMS-HEADENDIDENT-MIB',**{'HeTenthVolt':HeTenthVolt,'HeTenthdBm':HeTenthdBm,'HeTenthdBmV':HeTenthdBmV,'HeTenthCentigrade':HeTenthCentigrade,'HeHundredthNanoMeter':HeHundredthNanoMeter,'HeTenthdB':HeTenthdB,'HeOnOffControl':HeOnOffControl,'HeOnOffStatus':HeOnOffStatus,'HeFaultStatus':HeFaultStatus,'HeLaserType':HeLaserType,'HeMilliAmp':HeMilliAmp,'HeHundredthWatts':HeHundredthWatts,'headEndIdentMib':headEndIdentMib,'heOptics':heOptics,'heBaseIdent':heBaseIdent,'heCommon':heCommon,'hePowerSupply':hePowerSupply,'heFans':heFans,'heHMTS':heHMTS,'heRF':heRF,'heDigital':heDigital,'heManagedServer':heManagedServer})