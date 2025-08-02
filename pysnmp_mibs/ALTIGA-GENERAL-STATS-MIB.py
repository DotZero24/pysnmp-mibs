_J='altigaGeneralStatsGroup'
_I='alGeneralTimeZone'
_H='alGeneralGaugeThroughput'
_G='alGeneralGaugeActiveSessions'
_F='alGeneralGaugeCpuUtil'
_E='alGeneralTime'
_D='Gauge32'
_C='read-only'
_B='ALTIGA-GENERAL-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alGeneralMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alGeneralMibModule')
alGeneralGroup,alStatsGeneral=mibBuilder.importSymbols('ALTIGA-MIB','alGeneralGroup','alStatsGeneral')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_D,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaGeneralStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,30,2))
if mibBuilder.loadTexts:altigaGeneralStatsMibModule.setRevisions(('2002-09-11 13:00','2002-07-10 00:00'))
_AltigaGeneralStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaGeneralStatsMibConformance=_AltigaGeneralStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,30,2,1))
_AltigaGeneralStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaGeneralStatsMibCompliances=_AltigaGeneralStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,30,2,1,1))
_AlStatsGeneralGlobal_ObjectIdentity=ObjectIdentity
alStatsGeneralGlobal=_AlStatsGeneralGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,25,1))
_AlGeneralTime_Type=Counter32
_AlGeneralTime_Object=MibScalar
alGeneralTime=_AlGeneralTime_Object((1,3,6,1,4,1,3076,2,1,2,25,1,1),_AlGeneralTime_Type())
alGeneralTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alGeneralTime.setStatus(_A)
class _AlGeneralGaugeCpuUtil_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AlGeneralGaugeCpuUtil_Type.__name__=_D
_AlGeneralGaugeCpuUtil_Object=MibScalar
alGeneralGaugeCpuUtil=_AlGeneralGaugeCpuUtil_Object((1,3,6,1,4,1,3076,2,1,2,25,1,2),_AlGeneralGaugeCpuUtil_Type())
alGeneralGaugeCpuUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:alGeneralGaugeCpuUtil.setStatus(_A)
class _AlGeneralGaugeActiveSessions_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AlGeneralGaugeActiveSessions_Type.__name__=_D
_AlGeneralGaugeActiveSessions_Object=MibScalar
alGeneralGaugeActiveSessions=_AlGeneralGaugeActiveSessions_Object((1,3,6,1,4,1,3076,2,1,2,25,1,3),_AlGeneralGaugeActiveSessions_Type())
alGeneralGaugeActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:alGeneralGaugeActiveSessions.setStatus(_A)
class _AlGeneralGaugeThroughput_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AlGeneralGaugeThroughput_Type.__name__=_D
_AlGeneralGaugeThroughput_Object=MibScalar
alGeneralGaugeThroughput=_AlGeneralGaugeThroughput_Object((1,3,6,1,4,1,3076,2,1,2,25,1,4),_AlGeneralGaugeThroughput_Type())
alGeneralGaugeThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:alGeneralGaugeThroughput.setStatus(_A)
_AlGeneralTimeZone_Type=Integer32
_AlGeneralTimeZone_Object=MibScalar
alGeneralTimeZone=_AlGeneralTimeZone_Object((1,3,6,1,4,1,3076,2,1,2,25,1,5),_AlGeneralTimeZone_Type())
alGeneralTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:alGeneralTimeZone.setStatus(_A)
altigaGeneralStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,25,2))
altigaGeneralStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:altigaGeneralStatsGroup.setStatus(_A)
altigaGeneralStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,30,2,1,1,1))
altigaGeneralStatsMibCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:altigaGeneralStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaGeneralStatsMibModule':altigaGeneralStatsMibModule,'altigaGeneralStatsMibConformance':altigaGeneralStatsMibConformance,'altigaGeneralStatsMibCompliances':altigaGeneralStatsMibCompliances,'altigaGeneralStatsMibCompliance':altigaGeneralStatsMibCompliance,_J:altigaGeneralStatsGroup,'alStatsGeneralGlobal':alStatsGeneralGlobal,_E:alGeneralTime,_F:alGeneralGaugeCpuUtil,_G:alGeneralGaugeActiveSessions,_H:alGeneralGaugeThroughput,_I:alGeneralTimeZone})