_L='cerentIfExtGroup'
_K='cerentIfExtCurrentSoakTime'
_J='cerentIfExtConfiguredSoakTime'
_I='cerentIfExtPreServiceAlarmSuppression'
_H='minutes'
_G='read-write'
_F='TruthValue'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='CERENT-IF-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cerentGeneric,cerentModules,cerentRequirements=mibBuilder.importSymbols('CERENT-GLOBAL-REGISTRY','cerentGeneric','cerentModules','cerentRequirements')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
cerentIfExtMIB=ModuleIdentity((1,3,6,1,4,1,3607,1,10,140))
if mibBuilder.loadTexts:cerentIfExtMIB.setRevisions(('2005-11-14 00:00',))
_CerentIfExtMIBObjects_ObjectIdentity=ObjectIdentity
cerentIfExtMIBObjects=_CerentIfExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,3607,2,100))
_CerentIfExtTable_Object=MibTable
cerentIfExtTable=_CerentIfExtTable_Object((1,3,6,1,4,1,3607,2,100,10))
if mibBuilder.loadTexts:cerentIfExtTable.setStatus(_A)
_CerentIfExtEntry_Object=MibTableRow
cerentIfExtEntry=_CerentIfExtEntry_Object((1,3,6,1,4,1,3607,2,100,10,1))
cerentIfExtEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cerentIfExtEntry.setStatus(_A)
class _CerentIfExtPreServiceAlarmSuppression_Type(TruthValue):defaultValue=2
_CerentIfExtPreServiceAlarmSuppression_Type.__name__=_F
_CerentIfExtPreServiceAlarmSuppression_Object=MibTableColumn
cerentIfExtPreServiceAlarmSuppression=_CerentIfExtPreServiceAlarmSuppression_Object((1,3,6,1,4,1,3607,2,100,10,1,10),_CerentIfExtPreServiceAlarmSuppression_Type())
cerentIfExtPreServiceAlarmSuppression.setMaxAccess(_G)
if mibBuilder.loadTexts:cerentIfExtPreServiceAlarmSuppression.setStatus(_A)
class _CerentIfExtConfiguredSoakTime_Type(Integer32):defaultValue=480
_CerentIfExtConfiguredSoakTime_Type.__name__=_E
_CerentIfExtConfiguredSoakTime_Object=MibTableColumn
cerentIfExtConfiguredSoakTime=_CerentIfExtConfiguredSoakTime_Object((1,3,6,1,4,1,3607,2,100,10,1,20),_CerentIfExtConfiguredSoakTime_Type())
cerentIfExtConfiguredSoakTime.setMaxAccess(_G)
if mibBuilder.loadTexts:cerentIfExtConfiguredSoakTime.setStatus(_A)
if mibBuilder.loadTexts:cerentIfExtConfiguredSoakTime.setUnits(_H)
_CerentIfExtCurrentSoakTime_Type=Integer32
_CerentIfExtCurrentSoakTime_Object=MibTableColumn
cerentIfExtCurrentSoakTime=_CerentIfExtCurrentSoakTime_Object((1,3,6,1,4,1,3607,2,100,10,1,30),_CerentIfExtCurrentSoakTime_Type())
cerentIfExtCurrentSoakTime.setMaxAccess('read-only')
if mibBuilder.loadTexts:cerentIfExtCurrentSoakTime.setStatus(_A)
if mibBuilder.loadTexts:cerentIfExtCurrentSoakTime.setUnits(_H)
_CerentIfExtMIBConformance_ObjectIdentity=ObjectIdentity
cerentIfExtMIBConformance=_CerentIfExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,3607,5,90))
_CerentIfExtMIBCompliances_ObjectIdentity=ObjectIdentity
cerentIfExtMIBCompliances=_CerentIfExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3607,5,90,1))
_CerentIfExtMIBGroups_ObjectIdentity=ObjectIdentity
cerentIfExtMIBGroups=_CerentIfExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,3607,5,90,2))
cerentIfExtGroup=ObjectGroup((1,3,6,1,4,1,3607,5,90,2,10))
cerentIfExtGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cerentIfExtGroup.setStatus(_A)
cerentIfExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3607,5,90,1,1))
cerentIfExtMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:cerentIfExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cerentIfExtMIB':cerentIfExtMIB,'cerentIfExtMIBObjects':cerentIfExtMIBObjects,'cerentIfExtTable':cerentIfExtTable,'cerentIfExtEntry':cerentIfExtEntry,_I:cerentIfExtPreServiceAlarmSuppression,_J:cerentIfExtConfiguredSoakTime,_K:cerentIfExtCurrentSoakTime,'cerentIfExtMIBConformance':cerentIfExtMIBConformance,'cerentIfExtMIBCompliances':cerentIfExtMIBCompliances,'cerentIfExtMIBCompliance':cerentIfExtMIBCompliance,'cerentIfExtMIBGroups':cerentIfExtMIBGroups,_L:cerentIfExtGroup})