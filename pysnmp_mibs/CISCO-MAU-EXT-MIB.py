_O='cmExtIfMauTrafficGroup'
_N='deprecated'
_M='cmExtIfMauTrafficType'
_L='cmExtIfAutoMdixEnabled'
_K='cmExtJackState'
_J='cmExtJackConfigEntry'
_I='read-write'
_H='cmExtIfAutoMdixConfigGroup'
_G='Integer32'
_F='ifMauIndex'
_E='ifMauIfIndex'
_D='cmExtJackConfigGroup'
_C='MAU-MIB'
_B='CISCO-MAU-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifJackEntry,ifMauIfIndex,ifMauIndex=mibBuilder.importSymbols(_C,'ifJackEntry',_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoMauExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,398))
if mibBuilder.loadTexts:ciscoMauExtMIB.setRevisions(('2008-03-05 00:00','2004-04-21 00:00'))
_CmExtMIBNotifs_ObjectIdentity=ObjectIdentity
cmExtMIBNotifs=_CmExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,398,0))
_CmExtMIBObjects_ObjectIdentity=ObjectIdentity
cmExtMIBObjects=_CmExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,398,1))
_CmExtMauConfig_ObjectIdentity=ObjectIdentity
cmExtMauConfig=_CmExtMauConfig_ObjectIdentity((1,3,6,1,4,1,9,9,398,1,1))
_CmExtJackConfigTable_Object=MibTable
cmExtJackConfigTable=_CmExtJackConfigTable_Object((1,3,6,1,4,1,9,9,398,1,1,1))
if mibBuilder.loadTexts:cmExtJackConfigTable.setStatus(_A)
_CmExtJackConfigEntry_Object=MibTableRow
cmExtJackConfigEntry=_CmExtJackConfigEntry_Object((1,3,6,1,4,1,9,9,398,1,1,1,1))
if mibBuilder.loadTexts:cmExtJackConfigEntry.setStatus(_A)
class _CmExtJackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_CmExtJackState_Type.__name__=_G
_CmExtJackState_Object=MibTableColumn
cmExtJackState=_CmExtJackState_Object((1,3,6,1,4,1,9,9,398,1,1,1,1,1),_CmExtJackState_Type())
cmExtJackState.setMaxAccess(_I)
if mibBuilder.loadTexts:cmExtJackState.setStatus(_A)
_CmExtAutoMdixConfig_ObjectIdentity=ObjectIdentity
cmExtAutoMdixConfig=_CmExtAutoMdixConfig_ObjectIdentity((1,3,6,1,4,1,9,9,398,1,2))
_CmExtIfAutoMdixConfigTable_Object=MibTable
cmExtIfAutoMdixConfigTable=_CmExtIfAutoMdixConfigTable_Object((1,3,6,1,4,1,9,9,398,1,2,1))
if mibBuilder.loadTexts:cmExtIfAutoMdixConfigTable.setStatus(_A)
_CmExtIfAutoMdixConfigEntry_Object=MibTableRow
cmExtIfAutoMdixConfigEntry=_CmExtIfAutoMdixConfigEntry_Object((1,3,6,1,4,1,9,9,398,1,2,1,1))
cmExtIfAutoMdixConfigEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:cmExtIfAutoMdixConfigEntry.setStatus(_A)
_CmExtIfAutoMdixEnabled_Type=TruthValue
_CmExtIfAutoMdixEnabled_Object=MibTableColumn
cmExtIfAutoMdixEnabled=_CmExtIfAutoMdixEnabled_Object((1,3,6,1,4,1,9,9,398,1,2,1,1,1),_CmExtIfAutoMdixEnabled_Type())
cmExtIfAutoMdixEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:cmExtIfAutoMdixEnabled.setStatus(_A)
_CmExtIfMau_ObjectIdentity=ObjectIdentity
cmExtIfMau=_CmExtIfMau_ObjectIdentity((1,3,6,1,4,1,9,9,398,1,3))
_CmExtIfMauTrafficTable_Object=MibTable
cmExtIfMauTrafficTable=_CmExtIfMauTrafficTable_Object((1,3,6,1,4,1,9,9,398,1,3,1))
if mibBuilder.loadTexts:cmExtIfMauTrafficTable.setStatus(_A)
_CmExtIfMauTrafficEntry_Object=MibTableRow
cmExtIfMauTrafficEntry=_CmExtIfMauTrafficEntry_Object((1,3,6,1,4,1,9,9,398,1,3,1,1))
cmExtIfMauTrafficEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:cmExtIfMauTrafficEntry.setStatus(_A)
class _CmExtIfMauTrafficType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('adminControl',2),('user',3)))
_CmExtIfMauTrafficType_Type.__name__=_G
_CmExtIfMauTrafficType_Object=MibTableColumn
cmExtIfMauTrafficType=_CmExtIfMauTrafficType_Object((1,3,6,1,4,1,9,9,398,1,3,1,1,1),_CmExtIfMauTrafficType_Type())
cmExtIfMauTrafficType.setMaxAccess('read-only')
if mibBuilder.loadTexts:cmExtIfMauTrafficType.setStatus(_A)
_CmExtMIBConformance_ObjectIdentity=ObjectIdentity
cmExtMIBConformance=_CmExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,398,2))
_CmExtMIBCompliances_ObjectIdentity=ObjectIdentity
cmExtMIBCompliances=_CmExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,398,2,1))
_CmExtMIBGroups_ObjectIdentity=ObjectIdentity
cmExtMIBGroups=_CmExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,398,2,2))
ifJackEntry.registerAugmentions((_B,_J))
cmExtJackConfigEntry.setIndexNames(*ifJackEntry.getIndexNames())
cmExtJackConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,398,2,2,1))
cmExtJackConfigGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:cmExtJackConfigGroup.setStatus(_A)
cmExtIfAutoMdixConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,398,2,2,2))
cmExtIfAutoMdixConfigGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:cmExtIfAutoMdixConfigGroup.setStatus(_A)
cmExtIfMauTrafficGroup=ObjectGroup((1,3,6,1,4,1,9,9,398,2,2,3))
cmExtIfMauTrafficGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:cmExtIfMauTrafficGroup.setStatus(_A)
cmExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,398,2,1,1))
cmExtMIBCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:cmExtMIBCompliance.setStatus(_N)
cmExtMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,398,2,1,2))
cmExtMIBCompliance2.setObjects(*((_B,_D),(_B,_H)))
if mibBuilder.loadTexts:cmExtMIBCompliance2.setStatus(_N)
cmExtMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,398,2,1,3))
cmExtMIBCompliance3.setObjects(*((_B,_D),(_B,_H),(_B,_O)))
if mibBuilder.loadTexts:cmExtMIBCompliance3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoMauExtMIB':ciscoMauExtMIB,'cmExtMIBNotifs':cmExtMIBNotifs,'cmExtMIBObjects':cmExtMIBObjects,'cmExtMauConfig':cmExtMauConfig,'cmExtJackConfigTable':cmExtJackConfigTable,_J:cmExtJackConfigEntry,_K:cmExtJackState,'cmExtAutoMdixConfig':cmExtAutoMdixConfig,'cmExtIfAutoMdixConfigTable':cmExtIfAutoMdixConfigTable,'cmExtIfAutoMdixConfigEntry':cmExtIfAutoMdixConfigEntry,_L:cmExtIfAutoMdixEnabled,'cmExtIfMau':cmExtIfMau,'cmExtIfMauTrafficTable':cmExtIfMauTrafficTable,'cmExtIfMauTrafficEntry':cmExtIfMauTrafficEntry,_M:cmExtIfMauTrafficType,'cmExtMIBConformance':cmExtMIBConformance,'cmExtMIBCompliances':cmExtMIBCompliances,'cmExtMIBCompliance':cmExtMIBCompliance,'cmExtMIBCompliance2':cmExtMIBCompliance2,'cmExtMIBCompliance3':cmExtMIBCompliance3,'cmExtMIBGroups':cmExtMIBGroups,_D:cmExtJackConfigGroup,_H:cmExtIfAutoMdixConfigGroup,_O:cmExtIfMauTrafficGroup})