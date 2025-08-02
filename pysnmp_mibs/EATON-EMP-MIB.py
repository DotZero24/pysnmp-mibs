_U='eatonEMPTableGroup'
_T='eatonEMPGroup'
_S='xupsContactDescr'
_R='xupsContactState'
_Q='xupsContactType'
_P='xupsEnvNumContacts'
_O='xupsEnvRemoteHumidityUpperLimit'
_N='xupsEnvRemoteHumidityLowerLimit'
_M='xupsEnvRemoteTempUpperLimit'
_L='xupsEnvRemoteTempLowerLimit'
_K='xupsEnvRemoteHumidity'
_J='xupsEnvRemoteTemp'
_I='DisplayString'
_H='xupsContactIndex'
_G='percent'
_F='degrees Centigrade'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='EATON-EMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
xupsEnvironment,=mibBuilder.importSymbols('EATON-OIDS','xupsEnvironment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
eatonEMPMIB=ModuleIdentity((1,3,6,1,4,1,534,1,6,0))
if mibBuilder.loadTexts:eatonEMPMIB.setRevisions(('2007-03-12 00:00',))
_EatonEMPConformance_ObjectIdentity=ObjectIdentity
eatonEMPConformance=_EatonEMPConformance_ObjectIdentity((1,3,6,1,4,1,534,1,6,0,2))
class _XupsEnvRemoteTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,200))
_XupsEnvRemoteTemp_Type.__name__=_C
_XupsEnvRemoteTemp_Object=MibScalar
xupsEnvRemoteTemp=_XupsEnvRemoteTemp_Object((1,3,6,1,4,1,534,1,6,5),_XupsEnvRemoteTemp_Type())
xupsEnvRemoteTemp.setMaxAccess(_E)
if mibBuilder.loadTexts:xupsEnvRemoteTemp.setStatus(_A)
if mibBuilder.loadTexts:xupsEnvRemoteTemp.setUnits(_F)
class _XupsEnvRemoteHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_XupsEnvRemoteHumidity_Type.__name__=_C
_XupsEnvRemoteHumidity_Object=MibScalar
xupsEnvRemoteHumidity=_XupsEnvRemoteHumidity_Object((1,3,6,1,4,1,534,1,6,6),_XupsEnvRemoteHumidity_Type())
xupsEnvRemoteHumidity.setMaxAccess(_E)
if mibBuilder.loadTexts:xupsEnvRemoteHumidity.setStatus(_A)
if mibBuilder.loadTexts:xupsEnvRemoteHumidity.setUnits(_G)
class _XupsEnvNumContacts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_XupsEnvNumContacts_Type.__name__=_C
_XupsEnvNumContacts_Object=MibScalar
xupsEnvNumContacts=_XupsEnvNumContacts_Object((1,3,6,1,4,1,534,1,6,7),_XupsEnvNumContacts_Type())
xupsEnvNumContacts.setMaxAccess(_E)
if mibBuilder.loadTexts:xupsEnvNumContacts.setStatus(_A)
_XupsContactSenseTable_Object=MibTable
xupsContactSenseTable=_XupsContactSenseTable_Object((1,3,6,1,4,1,534,1,6,8))
if mibBuilder.loadTexts:xupsContactSenseTable.setStatus(_A)
_XupsContactsTableEntry_Object=MibTableRow
xupsContactsTableEntry=_XupsContactsTableEntry_Object((1,3,6,1,4,1,534,1,6,8,1))
xupsContactsTableEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:xupsContactsTableEntry.setStatus(_A)
class _XupsContactIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_XupsContactIndex_Type.__name__=_C
_XupsContactIndex_Object=MibTableColumn
xupsContactIndex=_XupsContactIndex_Object((1,3,6,1,4,1,534,1,6,8,1,1),_XupsContactIndex_Type())
xupsContactIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:xupsContactIndex.setStatus(_A)
class _XupsContactType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normallyOpen',1),('normallyClosed',2),('anyChange',3),('notUsed',4)))
_XupsContactType_Type.__name__=_C
_XupsContactType_Object=MibTableColumn
xupsContactType=_XupsContactType_Object((1,3,6,1,4,1,534,1,6,8,1,2),_XupsContactType_Type())
xupsContactType.setMaxAccess(_D)
if mibBuilder.loadTexts:xupsContactType.setStatus(_A)
class _XupsContactState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('open',1),('closed',2),('openWithNotice',3),('closedWithNotice',4)))
_XupsContactState_Type.__name__=_C
_XupsContactState_Object=MibTableColumn
xupsContactState=_XupsContactState_Object((1,3,6,1,4,1,534,1,6,8,1,3),_XupsContactState_Type())
xupsContactState.setMaxAccess(_E)
if mibBuilder.loadTexts:xupsContactState.setStatus(_A)
class _XupsContactDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_XupsContactDescr_Type.__name__=_I
_XupsContactDescr_Object=MibTableColumn
xupsContactDescr=_XupsContactDescr_Object((1,3,6,1,4,1,534,1,6,8,1,4),_XupsContactDescr_Type())
xupsContactDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:xupsContactDescr.setStatus(_A)
class _XupsEnvRemoteTempLowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,200))
_XupsEnvRemoteTempLowerLimit_Type.__name__=_C
_XupsEnvRemoteTempLowerLimit_Object=MibScalar
xupsEnvRemoteTempLowerLimit=_XupsEnvRemoteTempLowerLimit_Object((1,3,6,1,4,1,534,1,6,9),_XupsEnvRemoteTempLowerLimit_Type())
xupsEnvRemoteTempLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:xupsEnvRemoteTempLowerLimit.setStatus(_A)
if mibBuilder.loadTexts:xupsEnvRemoteTempLowerLimit.setUnits(_F)
class _XupsEnvRemoteTempUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,200))
_XupsEnvRemoteTempUpperLimit_Type.__name__=_C
_XupsEnvRemoteTempUpperLimit_Object=MibScalar
xupsEnvRemoteTempUpperLimit=_XupsEnvRemoteTempUpperLimit_Object((1,3,6,1,4,1,534,1,6,10),_XupsEnvRemoteTempUpperLimit_Type())
xupsEnvRemoteTempUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:xupsEnvRemoteTempUpperLimit.setStatus(_A)
if mibBuilder.loadTexts:xupsEnvRemoteTempUpperLimit.setUnits(_F)
class _XupsEnvRemoteHumidityLowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_XupsEnvRemoteHumidityLowerLimit_Type.__name__=_C
_XupsEnvRemoteHumidityLowerLimit_Object=MibScalar
xupsEnvRemoteHumidityLowerLimit=_XupsEnvRemoteHumidityLowerLimit_Object((1,3,6,1,4,1,534,1,6,11),_XupsEnvRemoteHumidityLowerLimit_Type())
xupsEnvRemoteHumidityLowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:xupsEnvRemoteHumidityLowerLimit.setStatus(_A)
if mibBuilder.loadTexts:xupsEnvRemoteHumidityLowerLimit.setUnits(_G)
class _XupsEnvRemoteHumidityUpperLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_XupsEnvRemoteHumidityUpperLimit_Type.__name__=_C
_XupsEnvRemoteHumidityUpperLimit_Object=MibScalar
xupsEnvRemoteHumidityUpperLimit=_XupsEnvRemoteHumidityUpperLimit_Object((1,3,6,1,4,1,534,1,6,12),_XupsEnvRemoteHumidityUpperLimit_Type())
xupsEnvRemoteHumidityUpperLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:xupsEnvRemoteHumidityUpperLimit.setStatus(_A)
if mibBuilder.loadTexts:xupsEnvRemoteHumidityUpperLimit.setUnits(_G)
eatonEMPGroup=ObjectGroup((1,3,6,1,4,1,534,1,6,0,2,1))
eatonEMPGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:eatonEMPGroup.setStatus(_A)
eatonEMPTableGroup=ObjectGroup((1,3,6,1,4,1,534,1,6,0,2,2))
eatonEMPTableGroup.setObjects(*((_B,_P),(_B,_H),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:eatonEMPTableGroup.setStatus(_A)
eatonEMPSimpleCompliance=ModuleCompliance((1,3,6,1,4,1,534,1,6,0,2,4))
eatonEMPSimpleCompliance.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:eatonEMPSimpleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eatonEMPMIB':eatonEMPMIB,'eatonEMPConformance':eatonEMPConformance,_T:eatonEMPGroup,_U:eatonEMPTableGroup,'eatonEMPSimpleCompliance':eatonEMPSimpleCompliance,_J:xupsEnvRemoteTemp,_K:xupsEnvRemoteHumidity,_P:xupsEnvNumContacts,'xupsContactSenseTable':xupsContactSenseTable,'xupsContactsTableEntry':xupsContactsTableEntry,_H:xupsContactIndex,_Q:xupsContactType,_R:xupsContactState,_S:xupsContactDescr,_L:xupsEnvRemoteTempLowerLimit,_M:xupsEnvRemoteTempUpperLimit,_N:xupsEnvRemoteHumidityLowerLimit,_O:xupsEnvRemoteHumidityUpperLimit})