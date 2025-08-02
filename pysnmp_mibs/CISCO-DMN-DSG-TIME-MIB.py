_D='DisplayString'
_C='read-write'
_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ciscoDSGTime=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,23))
if mibBuilder.loadTexts:ciscoDSGTime.setRevisions(('2010-08-30 11:00','2010-04-12 06:00','2009-12-20 12:00'))
_TimeInfo_ObjectIdentity=ObjectIdentity
timeInfo=_TimeInfo_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,23,1))
class _TimeFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('twentyFourHr',1),('twentyFourHrSuspendZero',2),('twelveHr',3),('twelveHrSuspendZero',4)))
_TimeFormat_Type.__name__=_A
_TimeFormat_Object=MibScalar
timeFormat=_TimeFormat_Object((1,3,6,1,4,1,1429,2,2,5,23,1,1),_TimeFormat_Type())
timeFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:timeFormat.setStatus(_B)
class _TimeDateFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('yyyymmdd',1),('ddmmyyyy',2),('mmddyyyy',3)))
_TimeDateFormat_Type.__name__=_A
_TimeDateFormat_Object=MibScalar
timeDateFormat=_TimeDateFormat_Object((1,3,6,1,4,1,1429,2,2,5,23,1,2),_TimeDateFormat_Type())
timeDateFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:timeDateFormat.setStatus(_B)
class _TimeGMTOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('minusTwelve',1),('minusEleven',2),('minusTen',3),('minusNine',4),('minusEight',5),('minusSeven',6),('minusSix',7),('minusFive',8),('minusFour',9),('minusThreeAndAHalf',10),('minusTwo',12),('minusOne',13),('zeroGMT',14),('plusOne',15),('plusTwo',16),('plusThree',17),('plusThreeAndAHalf',18),('plusFour',19),('plusFourAndAHalf',20),('plusFive',21),('plusFiveAndAHalf',22),('plusFiveAndThreeQuarter',23),('plusSix',24),('plusSixAndAHalf',25),('plusSeven',26),('plusEight',27),('plusNine',28),('plusNineAndAHalf',29),('plusTen',30),('plusEleven',31),('plusTwelve',32),('plusThirteen',33)))
_TimeGMTOffset_Type.__name__=_A
_TimeGMTOffset_Object=MibScalar
timeGMTOffset=_TimeGMTOffset_Object((1,3,6,1,4,1,1429,2,2,5,23,1,3),_TimeGMTOffset_Type())
timeGMTOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:timeGMTOffset.setStatus(_B)
class _TimeCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_TimeCurrent_Type.__name__=_D
_TimeCurrent_Object=MibScalar
timeCurrent=_TimeCurrent_Object((1,3,6,1,4,1,1429,2,2,5,23,1,4),_TimeCurrent_Type())
timeCurrent.setMaxAccess('read-only')
if mibBuilder.loadTexts:timeCurrent.setStatus(_B)
mibBuilder.exportSymbols('CISCO-DMN-DSG-TIME-MIB',**{'ciscoDSGTime':ciscoDSGTime,'timeInfo':timeInfo,'timeFormat':timeFormat,'timeDateFormat':timeDateFormat,'timeGMTOffset':timeGMTOffset,'timeCurrent':timeCurrent})