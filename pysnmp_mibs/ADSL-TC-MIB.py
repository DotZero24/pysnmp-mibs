_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adsltcmib=ModuleIdentity((1,3,6,1,2,1,10,94,2))
if mibBuilder.loadTexts:adsltcmib.setRevisions(('1999-08-19 00:00',))
class AdslLineCodingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('dmt',2),('cap',3),('qam',4)))
class AdslPerfCurrDayCount(TextualConvention,Gauge32):status=_A
class AdslPerfPrevDayCount(TextualConvention,Gauge32):status=_A
class AdslPerfTimeElapsed(TextualConvention,Gauge32):status=_A
mibBuilder.exportSymbols('ADSL-TC-MIB',**{'AdslLineCodingType':AdslLineCodingType,'AdslPerfCurrDayCount':AdslPerfCurrDayCount,'AdslPerfPrevDayCount':AdslPerfPrevDayCount,'AdslPerfTimeElapsed':AdslPerfTimeElapsed,'adsltcmib':adsltcmib})