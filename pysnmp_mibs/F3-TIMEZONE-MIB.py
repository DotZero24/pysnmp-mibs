_M='f3TimeZoneConfigGroup'
_L='f3TimeZoneDstEndTime'
_K='f3TimeZoneDstEndDay'
_J='f3TimeZoneDstEndMonth'
_I='f3TimeZoneDstStartTime'
_H='f3TimeZoneDstStartDay'
_G='f3TimeZoneDstStartMonth'
_F='f3TimeZoneDstUtcOffset'
_E='f3TimeZoneDstControlEnabled'
_D='f3TimeZoneUtcOffset'
_C='read-write'
_B='F3-TIMEZONE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
f3TimeZoneMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,32))
if mibBuilder.loadTexts:f3TimeZoneMIB.setRevisions(('2014-06-05 00:00',))
class MonthOfYear(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('january',1),('february',2),('march',3),('april',4),('may',5),('june',6),('july',7),('august',8),('september',9),('october',10),('november',11),('december',12)))
_F3TimeZoneConfigObjects_ObjectIdentity=ObjectIdentity
f3TimeZoneConfigObjects=_F3TimeZoneConfigObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,32,1))
_F3TimeZoneUtcOffset_Type=DisplayString
_F3TimeZoneUtcOffset_Object=MibScalar
f3TimeZoneUtcOffset=_F3TimeZoneUtcOffset_Object((1,3,6,1,4,1,2544,1,12,32,1,1),_F3TimeZoneUtcOffset_Type())
f3TimeZoneUtcOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneUtcOffset.setStatus(_A)
_F3TimeZoneDstControlEnabled_Type=TruthValue
_F3TimeZoneDstControlEnabled_Object=MibScalar
f3TimeZoneDstControlEnabled=_F3TimeZoneDstControlEnabled_Object((1,3,6,1,4,1,2544,1,12,32,1,2),_F3TimeZoneDstControlEnabled_Type())
f3TimeZoneDstControlEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstControlEnabled.setStatus(_A)
_F3TimeZoneDstUtcOffset_Type=DisplayString
_F3TimeZoneDstUtcOffset_Object=MibScalar
f3TimeZoneDstUtcOffset=_F3TimeZoneDstUtcOffset_Object((1,3,6,1,4,1,2544,1,12,32,1,3),_F3TimeZoneDstUtcOffset_Type())
f3TimeZoneDstUtcOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstUtcOffset.setStatus(_A)
_F3TimeZoneDstStartMonth_Type=MonthOfYear
_F3TimeZoneDstStartMonth_Object=MibScalar
f3TimeZoneDstStartMonth=_F3TimeZoneDstStartMonth_Object((1,3,6,1,4,1,2544,1,12,32,1,4),_F3TimeZoneDstStartMonth_Type())
f3TimeZoneDstStartMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstStartMonth.setStatus(_A)
_F3TimeZoneDstStartDay_Type=DisplayString
_F3TimeZoneDstStartDay_Object=MibScalar
f3TimeZoneDstStartDay=_F3TimeZoneDstStartDay_Object((1,3,6,1,4,1,2544,1,12,32,1,5),_F3TimeZoneDstStartDay_Type())
f3TimeZoneDstStartDay.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstStartDay.setStatus(_A)
_F3TimeZoneDstStartTime_Type=DisplayString
_F3TimeZoneDstStartTime_Object=MibScalar
f3TimeZoneDstStartTime=_F3TimeZoneDstStartTime_Object((1,3,6,1,4,1,2544,1,12,32,1,6),_F3TimeZoneDstStartTime_Type())
f3TimeZoneDstStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstStartTime.setStatus(_A)
_F3TimeZoneDstEndMonth_Type=MonthOfYear
_F3TimeZoneDstEndMonth_Object=MibScalar
f3TimeZoneDstEndMonth=_F3TimeZoneDstEndMonth_Object((1,3,6,1,4,1,2544,1,12,32,1,7),_F3TimeZoneDstEndMonth_Type())
f3TimeZoneDstEndMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstEndMonth.setStatus(_A)
_F3TimeZoneDstEndDay_Type=DisplayString
_F3TimeZoneDstEndDay_Object=MibScalar
f3TimeZoneDstEndDay=_F3TimeZoneDstEndDay_Object((1,3,6,1,4,1,2544,1,12,32,1,8),_F3TimeZoneDstEndDay_Type())
f3TimeZoneDstEndDay.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstEndDay.setStatus(_A)
_F3TimeZoneDstEndTime_Type=DisplayString
_F3TimeZoneDstEndTime_Object=MibScalar
f3TimeZoneDstEndTime=_F3TimeZoneDstEndTime_Object((1,3,6,1,4,1,2544,1,12,32,1,9),_F3TimeZoneDstEndTime_Type())
f3TimeZoneDstEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeZoneDstEndTime.setStatus(_A)
_F3TimeZoneConformance_ObjectIdentity=ObjectIdentity
f3TimeZoneConformance=_F3TimeZoneConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,32,2))
_F3TimeZoneCompliances_ObjectIdentity=ObjectIdentity
f3TimeZoneCompliances=_F3TimeZoneCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,32,2,1))
_F3TimeZoneGroups_ObjectIdentity=ObjectIdentity
f3TimeZoneGroups=_F3TimeZoneGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,32,2,2))
f3TimeZoneConfigGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,32,2,2,1))
f3TimeZoneConfigGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:f3TimeZoneConfigGroup.setStatus(_A)
f3TimeZoneCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,32,2,1,1))
f3TimeZoneCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:f3TimeZoneCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MonthOfYear':MonthOfYear,'f3TimeZoneMIB':f3TimeZoneMIB,'f3TimeZoneConfigObjects':f3TimeZoneConfigObjects,_D:f3TimeZoneUtcOffset,_E:f3TimeZoneDstControlEnabled,_F:f3TimeZoneDstUtcOffset,_G:f3TimeZoneDstStartMonth,_H:f3TimeZoneDstStartDay,_I:f3TimeZoneDstStartTime,_J:f3TimeZoneDstEndMonth,_K:f3TimeZoneDstEndDay,_L:f3TimeZoneDstEndTime,'f3TimeZoneConformance':f3TimeZoneConformance,'f3TimeZoneCompliances':f3TimeZoneCompliances,'f3TimeZoneCompliance':f3TimeZoneCompliance,'f3TimeZoneGroups':f3TimeZoneGroups,_M:f3TimeZoneConfigGroup})