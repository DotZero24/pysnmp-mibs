_B='other'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fibrolanCommon=ModuleIdentity((1,3,6,1,4,1,4467,1000,1))
if mibBuilder.loadTexts:fibrolanCommon.setRevisions(('2015-08-10 00:00','2009-01-26 00:00'))
class FlUtilization(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class FlTemperature(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
class FlFileServerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_B,1),('ftp',2),('tftp',3)))
class FlFileXferDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('getFromServer',1),('putOnServer',2)))
class FlClockSourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,99)));namedValues=NamedValues(*(('gps',1),('bits',2),('syncE',3),('ptp',4),('external',5),('oscillator',6),(_B,99)))
class FlClockQuality(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,7,8,10,11,12,13,15,99)));namedValues=NamedValues(*(('stu',0),('prs',1),('prc',2),('tnc',4),('st2',7),('ssu-b',8),('st3',10),('sec',11),('smc',12),('st3e',13),('dus',15),(_B,99)))
class FlGeoCoordinateAxis(TextualConvention,OctetString):status=_A;displayHint='1a1d:1d:1d.1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Fibrolan_ObjectIdentity=ObjectIdentity
fibrolan=_Fibrolan_ObjectIdentity((1,3,6,1,4,1,4467))
_FibrolanGeneric_ObjectIdentity=ObjectIdentity
fibrolanGeneric=_FibrolanGeneric_ObjectIdentity((1,3,6,1,4,1,4467,1000))
mibBuilder.exportSymbols('FIBROLAN-COMMON-MIB',**{'FlUtilization':FlUtilization,'FlTemperature':FlTemperature,'FlFileServerType':FlFileServerType,'FlFileXferDirection':FlFileXferDirection,'FlClockSourceType':FlClockSourceType,'FlClockQuality':FlClockQuality,'FlGeoCoordinateAxis':FlGeoCoordinateAxis,'fibrolan':fibrolan,'fibrolanGeneric':fibrolanGeneric,'fibrolanCommon':fibrolanCommon})