_B='notSupported'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsMib=ModuleIdentity((1,3,6,1,4,1,629,250))
class Unsigned16TC(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class Unsigned64TC(TextualConvention,Counter64):status=_A
class WritableU64(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NbsTcTemperature(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,1000))
class NbsTcMilliVolt(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000000))
class NbsTcMilliAmp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000000))
class NbsTcMicroAmp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
class NbsTcMilliDb(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,100000))
class NbsTcMilliWatts(TextualConvention,Integer32):status=_A
class NbsTcMHz(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class NbsTcStatusSimple(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('bad',2),('good',3),('notInstalled',4)))
class NbsTcStatusLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_B,1),('statusLowError',2),('statusLowWarning',3),('statusGood',4),('statusHighWarning',5),('statusHighError',6)))
class NbsTcPartIndex(TextualConvention,Unsigned32):status=_A
class NbsTcStagingCommit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('supported',2),('revertToCommitted',3),('apply',4)))
_Nbs_ObjectIdentity=ObjectIdentity
nbs=_Nbs_ObjectIdentity((1,3,6,1,4,1,629))
if mibBuilder.loadTexts:nbs.setStatus(_A)
mibBuilder.exportSymbols('NBS-MIB',**{'Unsigned16TC':Unsigned16TC,'Unsigned64TC':Unsigned64TC,'WritableU64':WritableU64,'NbsTcTemperature':NbsTcTemperature,'NbsTcMilliVolt':NbsTcMilliVolt,'NbsTcMilliAmp':NbsTcMilliAmp,'NbsTcMicroAmp':NbsTcMicroAmp,'NbsTcMilliDb':NbsTcMilliDb,'NbsTcMilliWatts':NbsTcMilliWatts,'NbsTcMHz':NbsTcMHz,'NbsTcStatusSimple':NbsTcStatusSimple,'NbsTcStatusLevel':NbsTcStatusLevel,'NbsTcPartIndex':NbsTcPartIndex,'NbsTcStagingCommit':NbsTcStagingCommit,'nbs':nbs,'nbsMib':nbsMib})