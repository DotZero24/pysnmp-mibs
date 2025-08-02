_P='hpicfFanScalarsGroup'
_O='hpicfFanAirflowDirection'
_N='hpicfFanNumFailures'
_M='hpicfFanRecovering'
_L='hpicfFanState'
_K='hpicfFanType'
_J='hpicfFanTray'
_I='hpicfFanUserPrefAirflowDir'
_H='hpicfFanIndex'
_G='powerToPort'
_F='portToPower'
_E='Integer32'
_D='hpicfFanGroup'
_C='read-only'
_B='FAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfFanMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,54))
if mibBuilder.loadTexts:hpicfFanMIB.setRevisions(('2008-08-27 10:30',))
class HpicfDcFanIndex(TextualConvention,Unsigned32):status=_A;displayHint='d'
class HpicfDcFanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',0),('mm',1),('fm',2),('im',3),('ps',4),('rollup',5),('maxtype',6)))
class HpicfDcFanAirflowDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
class HpicfDcFanState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('failed',0),('removed',1),('off',2),('underspeed',3),('overspeed',4),('ok',5),('maxstate',6)))
_HpicfFanScalars_ObjectIdentity=ObjectIdentity
hpicfFanScalars=_HpicfFanScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,54,1))
class _HpicfFanUserPrefAirflowDir_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpicfFanUserPrefAirflowDir_Type.__name__=_E
_HpicfFanUserPrefAirflowDir_Object=MibScalar
hpicfFanUserPrefAirflowDir=_HpicfFanUserPrefAirflowDir_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,1,1),_HpicfFanUserPrefAirflowDir_Type())
hpicfFanUserPrefAirflowDir.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfFanUserPrefAirflowDir.setStatus(_A)
_HpicfEntityFan_ObjectIdentity=ObjectIdentity
hpicfEntityFan=_HpicfEntityFan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,54,2))
_HpicfFanTable_Object=MibTable
hpicfFanTable=_HpicfFanTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1))
if mibBuilder.loadTexts:hpicfFanTable.setStatus(_A)
_HpicfFanEntry_Object=MibTableRow
hpicfFanEntry=_HpicfFanEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1))
hpicfFanEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpicfFanEntry.setStatus(_A)
_HpicfFanIndex_Type=HpicfDcFanIndex
_HpicfFanIndex_Object=MibTableColumn
hpicfFanIndex=_HpicfFanIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1,1),_HpicfFanIndex_Type())
hpicfFanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfFanIndex.setStatus(_A)
_HpicfFanTray_Type=Integer32
_HpicfFanTray_Object=MibTableColumn
hpicfFanTray=_HpicfFanTray_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1,2),_HpicfFanTray_Type())
hpicfFanTray.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFanTray.setStatus(_A)
_HpicfFanType_Type=HpicfDcFanType
_HpicfFanType_Object=MibTableColumn
hpicfFanType=_HpicfFanType_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1,3),_HpicfFanType_Type())
hpicfFanType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFanType.setStatus(_A)
_HpicfFanState_Type=HpicfDcFanState
_HpicfFanState_Object=MibTableColumn
hpicfFanState=_HpicfFanState_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1,4),_HpicfFanState_Type())
hpicfFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFanState.setStatus(_A)
_HpicfFanRecovering_Type=Integer32
_HpicfFanRecovering_Object=MibTableColumn
hpicfFanRecovering=_HpicfFanRecovering_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1,5),_HpicfFanRecovering_Type())
hpicfFanRecovering.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFanRecovering.setStatus(_A)
_HpicfFanNumFailures_Type=Counter32
_HpicfFanNumFailures_Object=MibTableColumn
hpicfFanNumFailures=_HpicfFanNumFailures_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1,6),_HpicfFanNumFailures_Type())
hpicfFanNumFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFanNumFailures.setStatus(_A)
_HpicfFanAirflowDirection_Type=HpicfDcFanAirflowDirection
_HpicfFanAirflowDirection_Object=MibTableColumn
hpicfFanAirflowDirection=_HpicfFanAirflowDirection_Object((1,3,6,1,4,1,11,2,14,11,5,1,54,2,1,1,7),_HpicfFanAirflowDirection_Type())
hpicfFanAirflowDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfFanAirflowDirection.setStatus(_A)
_HpicfFanConformance_ObjectIdentity=ObjectIdentity
hpicfFanConformance=_HpicfFanConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,54,3))
_HpicfFanCompliance_ObjectIdentity=ObjectIdentity
hpicfFanCompliance=_HpicfFanCompliance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,54,3,1))
_HpicfFanGroups_ObjectIdentity=ObjectIdentity
hpicfFanGroups=_HpicfFanGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,54,3,2))
hpicfFanScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,54,3,2,1))
hpicfFanScalarsGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:hpicfFanScalarsGroup.setStatus(_A)
hpicfFanGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,54,3,2,2))
hpicfFanGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:hpicfFanGroup.setStatus(_A)
hpicfDcFanCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,54,3,1,1))
hpicfDcFanCompliance.setObjects(*((_B,_P),(_B,_D),(_B,_D)))
if mibBuilder.loadTexts:hpicfDcFanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpicfDcFanIndex':HpicfDcFanIndex,'HpicfDcFanType':HpicfDcFanType,'HpicfDcFanAirflowDirection':HpicfDcFanAirflowDirection,'HpicfDcFanState':HpicfDcFanState,'hpicfFanMIB':hpicfFanMIB,'hpicfFanScalars':hpicfFanScalars,_I:hpicfFanUserPrefAirflowDir,'hpicfEntityFan':hpicfEntityFan,'hpicfFanTable':hpicfFanTable,'hpicfFanEntry':hpicfFanEntry,_H:hpicfFanIndex,_J:hpicfFanTray,_K:hpicfFanType,_L:hpicfFanState,_M:hpicfFanRecovering,_N:hpicfFanNumFailures,_O:hpicfFanAirflowDirection,'hpicfFanConformance':hpicfFanConformance,'hpicfFanCompliance':hpicfFanCompliance,'hpicfDcFanCompliance':hpicfDcFanCompliance,'hpicfFanGroups':hpicfFanGroups,_P:hpicfFanScalarsGroup,_D:hpicfFanGroup})