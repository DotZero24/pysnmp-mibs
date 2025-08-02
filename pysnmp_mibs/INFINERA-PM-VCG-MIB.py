_Z='vCGPmRealGroup'
_Y='vCGPmRealDifferentialDelay20'
_X='vCGPmRealDifferentialDelay19'
_W='vCGPmRealDifferentialDelay18'
_V='vCGPmRealDifferentialDelay17'
_U='vCGPmRealDifferentialDelay16'
_T='vCGPmRealDifferentialDelay15'
_S='vCGPmRealDifferentialDelay14'
_R='vCGPmRealDifferentialDelay13'
_Q='vCGPmRealDifferentialDelay12'
_P='vCGPmRealDifferentialDelay11'
_O='vCGPmRealDifferentialDelay10'
_N='vCGPmRealDifferentialDelay9'
_M='vCGPmRealDifferentialDelay8'
_L='vCGPmRealDifferentialDelay7'
_K='vCGPmRealDifferentialDelay6'
_J='vCGPmRealDifferentialDelay5'
_I='vCGPmRealDifferentialDelay4'
_H='vCGPmRealDifferentialDelay3'
_G='vCGPmRealDifferentialDelay2'
_F='vCGPmRealDifferentialDelay1'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-VCG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vCGPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,16))
if mibBuilder.loadTexts:vCGPmMIB.setRevisions(('2008-10-20 00:00',))
_VCGPmRealTable_Object=MibTable
vCGPmRealTable=_VCGPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1))
if mibBuilder.loadTexts:vCGPmRealTable.setStatus(_A)
_VCGPmRealEntry_Object=MibTableRow
vCGPmRealEntry=_VCGPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1))
vCGPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:vCGPmRealEntry.setStatus(_A)
_VCGPmRealDifferentialDelay1_Type=FloatHundredths
_VCGPmRealDifferentialDelay1_Object=MibTableColumn
vCGPmRealDifferentialDelay1=_VCGPmRealDifferentialDelay1_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,1),_VCGPmRealDifferentialDelay1_Type())
vCGPmRealDifferentialDelay1.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay1.setStatus(_A)
_VCGPmRealDifferentialDelay2_Type=FloatHundredths
_VCGPmRealDifferentialDelay2_Object=MibTableColumn
vCGPmRealDifferentialDelay2=_VCGPmRealDifferentialDelay2_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,2),_VCGPmRealDifferentialDelay2_Type())
vCGPmRealDifferentialDelay2.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay2.setStatus(_A)
_VCGPmRealDifferentialDelay3_Type=FloatHundredths
_VCGPmRealDifferentialDelay3_Object=MibTableColumn
vCGPmRealDifferentialDelay3=_VCGPmRealDifferentialDelay3_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,3),_VCGPmRealDifferentialDelay3_Type())
vCGPmRealDifferentialDelay3.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay3.setStatus(_A)
_VCGPmRealDifferentialDelay4_Type=FloatHundredths
_VCGPmRealDifferentialDelay4_Object=MibTableColumn
vCGPmRealDifferentialDelay4=_VCGPmRealDifferentialDelay4_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,4),_VCGPmRealDifferentialDelay4_Type())
vCGPmRealDifferentialDelay4.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay4.setStatus(_A)
_VCGPmRealDifferentialDelay5_Type=FloatHundredths
_VCGPmRealDifferentialDelay5_Object=MibTableColumn
vCGPmRealDifferentialDelay5=_VCGPmRealDifferentialDelay5_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,5),_VCGPmRealDifferentialDelay5_Type())
vCGPmRealDifferentialDelay5.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay5.setStatus(_A)
_VCGPmRealDifferentialDelay6_Type=FloatHundredths
_VCGPmRealDifferentialDelay6_Object=MibTableColumn
vCGPmRealDifferentialDelay6=_VCGPmRealDifferentialDelay6_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,6),_VCGPmRealDifferentialDelay6_Type())
vCGPmRealDifferentialDelay6.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay6.setStatus(_A)
_VCGPmRealDifferentialDelay7_Type=FloatHundredths
_VCGPmRealDifferentialDelay7_Object=MibTableColumn
vCGPmRealDifferentialDelay7=_VCGPmRealDifferentialDelay7_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,7),_VCGPmRealDifferentialDelay7_Type())
vCGPmRealDifferentialDelay7.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay7.setStatus(_A)
_VCGPmRealDifferentialDelay8_Type=FloatHundredths
_VCGPmRealDifferentialDelay8_Object=MibTableColumn
vCGPmRealDifferentialDelay8=_VCGPmRealDifferentialDelay8_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,8),_VCGPmRealDifferentialDelay8_Type())
vCGPmRealDifferentialDelay8.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay8.setStatus(_A)
_VCGPmRealDifferentialDelay9_Type=FloatHundredths
_VCGPmRealDifferentialDelay9_Object=MibTableColumn
vCGPmRealDifferentialDelay9=_VCGPmRealDifferentialDelay9_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,9),_VCGPmRealDifferentialDelay9_Type())
vCGPmRealDifferentialDelay9.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay9.setStatus(_A)
_VCGPmRealDifferentialDelay10_Type=FloatHundredths
_VCGPmRealDifferentialDelay10_Object=MibTableColumn
vCGPmRealDifferentialDelay10=_VCGPmRealDifferentialDelay10_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,10),_VCGPmRealDifferentialDelay10_Type())
vCGPmRealDifferentialDelay10.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay10.setStatus(_A)
_VCGPmRealDifferentialDelay11_Type=FloatHundredths
_VCGPmRealDifferentialDelay11_Object=MibTableColumn
vCGPmRealDifferentialDelay11=_VCGPmRealDifferentialDelay11_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,11),_VCGPmRealDifferentialDelay11_Type())
vCGPmRealDifferentialDelay11.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay11.setStatus(_A)
_VCGPmRealDifferentialDelay12_Type=FloatHundredths
_VCGPmRealDifferentialDelay12_Object=MibTableColumn
vCGPmRealDifferentialDelay12=_VCGPmRealDifferentialDelay12_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,12),_VCGPmRealDifferentialDelay12_Type())
vCGPmRealDifferentialDelay12.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay12.setStatus(_A)
_VCGPmRealDifferentialDelay13_Type=FloatHundredths
_VCGPmRealDifferentialDelay13_Object=MibTableColumn
vCGPmRealDifferentialDelay13=_VCGPmRealDifferentialDelay13_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,13),_VCGPmRealDifferentialDelay13_Type())
vCGPmRealDifferentialDelay13.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay13.setStatus(_A)
_VCGPmRealDifferentialDelay14_Type=FloatHundredths
_VCGPmRealDifferentialDelay14_Object=MibTableColumn
vCGPmRealDifferentialDelay14=_VCGPmRealDifferentialDelay14_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,14),_VCGPmRealDifferentialDelay14_Type())
vCGPmRealDifferentialDelay14.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay14.setStatus(_A)
_VCGPmRealDifferentialDelay15_Type=FloatHundredths
_VCGPmRealDifferentialDelay15_Object=MibTableColumn
vCGPmRealDifferentialDelay15=_VCGPmRealDifferentialDelay15_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,15),_VCGPmRealDifferentialDelay15_Type())
vCGPmRealDifferentialDelay15.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay15.setStatus(_A)
_VCGPmRealDifferentialDelay16_Type=FloatHundredths
_VCGPmRealDifferentialDelay16_Object=MibTableColumn
vCGPmRealDifferentialDelay16=_VCGPmRealDifferentialDelay16_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,16),_VCGPmRealDifferentialDelay16_Type())
vCGPmRealDifferentialDelay16.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay16.setStatus(_A)
_VCGPmRealDifferentialDelay17_Type=FloatHundredths
_VCGPmRealDifferentialDelay17_Object=MibTableColumn
vCGPmRealDifferentialDelay17=_VCGPmRealDifferentialDelay17_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,17),_VCGPmRealDifferentialDelay17_Type())
vCGPmRealDifferentialDelay17.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay17.setStatus(_A)
_VCGPmRealDifferentialDelay18_Type=FloatHundredths
_VCGPmRealDifferentialDelay18_Object=MibTableColumn
vCGPmRealDifferentialDelay18=_VCGPmRealDifferentialDelay18_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,18),_VCGPmRealDifferentialDelay18_Type())
vCGPmRealDifferentialDelay18.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay18.setStatus(_A)
_VCGPmRealDifferentialDelay19_Type=FloatHundredths
_VCGPmRealDifferentialDelay19_Object=MibTableColumn
vCGPmRealDifferentialDelay19=_VCGPmRealDifferentialDelay19_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,19),_VCGPmRealDifferentialDelay19_Type())
vCGPmRealDifferentialDelay19.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay19.setStatus(_A)
_VCGPmRealDifferentialDelay20_Type=FloatHundredths
_VCGPmRealDifferentialDelay20_Object=MibTableColumn
vCGPmRealDifferentialDelay20=_VCGPmRealDifferentialDelay20_Object((1,3,6,1,4,1,21296,2,2,2,3,16,1,1,20),_VCGPmRealDifferentialDelay20_Type())
vCGPmRealDifferentialDelay20.setMaxAccess(_C)
if mibBuilder.loadTexts:vCGPmRealDifferentialDelay20.setStatus(_A)
_VCGPmConformance_ObjectIdentity=ObjectIdentity
vCGPmConformance=_VCGPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,16,3))
_VCGPmCompliances_ObjectIdentity=ObjectIdentity
vCGPmCompliances=_VCGPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,16,3,1))
_VCGPmGroups_ObjectIdentity=ObjectIdentity
vCGPmGroups=_VCGPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,16,3,2))
vCGPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,16,3,2,1))
vCGPmRealGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:vCGPmRealGroup.setStatus(_A)
vCGPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,16,3,1,1))
vCGPmRealCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:vCGPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vCGPmMIB':vCGPmMIB,'vCGPmRealTable':vCGPmRealTable,'vCGPmRealEntry':vCGPmRealEntry,_F:vCGPmRealDifferentialDelay1,_G:vCGPmRealDifferentialDelay2,_H:vCGPmRealDifferentialDelay3,_I:vCGPmRealDifferentialDelay4,_J:vCGPmRealDifferentialDelay5,_K:vCGPmRealDifferentialDelay6,_L:vCGPmRealDifferentialDelay7,_M:vCGPmRealDifferentialDelay8,_N:vCGPmRealDifferentialDelay9,_O:vCGPmRealDifferentialDelay10,_P:vCGPmRealDifferentialDelay11,_Q:vCGPmRealDifferentialDelay12,_R:vCGPmRealDifferentialDelay13,_S:vCGPmRealDifferentialDelay14,_T:vCGPmRealDifferentialDelay15,_U:vCGPmRealDifferentialDelay16,_V:vCGPmRealDifferentialDelay17,_W:vCGPmRealDifferentialDelay18,_X:vCGPmRealDifferentialDelay19,_Y:vCGPmRealDifferentialDelay20,'vCGPmConformance':vCGPmConformance,'vCGPmCompliances':vCGPmCompliances,'vCGPmRealCompliance':vCGPmRealCompliance,'vCGPmGroups':vCGPmGroups,_Z:vCGPmRealGroup})