_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzRFNoiseTc=ModuleIdentity((1,3,6,1,4,1,14525,4,22))
if mibBuilder.loadTexts:trpzRFNoiseTc.setRevisions(('2011-01-10 00:00',))
class TrpzRFNoiseSourceID(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class TrpzRFNoiseSourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,16,33,49,50,64,65,66)));namedValues=NamedValues(*(('nsUnknown',0),('nsContinuousWave',1),('nsVideo',16),('nsMicrowaveOven',33),('nsPhoneDECT',49),('nsPhoneFHSS',50),('nsBluetoothAny',64),('nsBluetoothHeadset',65),('nsBluetoothHandsfree',66)))
mibBuilder.exportSymbols('TRAPEZE-NETWORKS-RF-NOISE-TC-MIB',**{'TrpzRFNoiseSourceID':TrpzRFNoiseSourceID,'TrpzRFNoiseSourceType':TrpzRFNoiseSourceType,'trpzRFNoiseTc':trpzRFNoiseTc})