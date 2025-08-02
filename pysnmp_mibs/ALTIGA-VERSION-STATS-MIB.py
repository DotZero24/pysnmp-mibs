_K='altigaVersionStatsGroup'
_J='alVersionBoot'
_I='alVersionShort'
_H='alVersionLong'
_G='alVersionString'
_F='alVersionInt'
_E='alVersionMinor'
_D='alVersionMajor'
_C='read-only'
_B='ALTIGA-VERSION-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alVersionMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alVersionMibModule')
alStatsVersion,alVersionGroup=mibBuilder.importSymbols('ALTIGA-MIB','alStatsVersion','alVersionGroup')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaVersionStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,6,2))
if mibBuilder.loadTexts:altigaVersionStatsMibModule.setRevisions(('2002-09-05 13:00',))
_AltigaVersionStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaVersionStatsMibConformance=_AltigaVersionStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,6,2,1))
_AltigaVersionStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaVersionStatsMibCompliances=_AltigaVersionStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,6,2,1,1))
_AlStatsVersionGlobal_ObjectIdentity=ObjectIdentity
alStatsVersionGlobal=_AlStatsVersionGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,1,1))
_AlVersionMajor_Type=Unsigned32
_AlVersionMajor_Object=MibScalar
alVersionMajor=_AlVersionMajor_Object((1,3,6,1,4,1,3076,2,1,2,1,1,1),_AlVersionMajor_Type())
alVersionMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:alVersionMajor.setStatus(_A)
_AlVersionMinor_Type=Unsigned32
_AlVersionMinor_Object=MibScalar
alVersionMinor=_AlVersionMinor_Object((1,3,6,1,4,1,3076,2,1,2,1,1,2),_AlVersionMinor_Type())
alVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:alVersionMinor.setStatus(_A)
_AlVersionInt_Type=DisplayString
_AlVersionInt_Object=MibScalar
alVersionInt=_AlVersionInt_Object((1,3,6,1,4,1,3076,2,1,2,1,1,3),_AlVersionInt_Type())
alVersionInt.setMaxAccess(_C)
if mibBuilder.loadTexts:alVersionInt.setStatus(_A)
_AlVersionString_Type=DisplayString
_AlVersionString_Object=MibScalar
alVersionString=_AlVersionString_Object((1,3,6,1,4,1,3076,2,1,2,1,1,4),_AlVersionString_Type())
alVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:alVersionString.setStatus(_A)
_AlVersionLong_Type=DisplayString
_AlVersionLong_Object=MibScalar
alVersionLong=_AlVersionLong_Object((1,3,6,1,4,1,3076,2,1,2,1,1,5),_AlVersionLong_Type())
alVersionLong.setMaxAccess(_C)
if mibBuilder.loadTexts:alVersionLong.setStatus(_A)
_AlVersionShort_Type=DisplayString
_AlVersionShort_Object=MibScalar
alVersionShort=_AlVersionShort_Object((1,3,6,1,4,1,3076,2,1,2,1,1,6),_AlVersionShort_Type())
alVersionShort.setMaxAccess(_C)
if mibBuilder.loadTexts:alVersionShort.setStatus(_A)
_AlVersionBoot_Type=DisplayString
_AlVersionBoot_Object=MibScalar
alVersionBoot=_AlVersionBoot_Object((1,3,6,1,4,1,3076,2,1,2,1,1,7),_AlVersionBoot_Type())
alVersionBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:alVersionBoot.setStatus(_A)
altigaVersionStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,1,2))
altigaVersionStatsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:altigaVersionStatsGroup.setStatus(_A)
altigaVersionStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,6,2,1,1,1))
altigaVersionStatsMibCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:altigaVersionStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaVersionStatsMibModule':altigaVersionStatsMibModule,'altigaVersionStatsMibConformance':altigaVersionStatsMibConformance,'altigaVersionStatsMibCompliances':altigaVersionStatsMibCompliances,'altigaVersionStatsMibCompliance':altigaVersionStatsMibCompliance,_K:altigaVersionStatsGroup,'alStatsVersionGlobal':alStatsVersionGlobal,_D:alVersionMajor,_E:alVersionMinor,_F:alVersionInt,_G:alVersionString,_H:alVersionLong,_I:alVersionShort,_J:alVersionBoot})