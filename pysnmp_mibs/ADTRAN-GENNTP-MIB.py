_f='adGenNtpEntObjectsGroup2'
_e='adGenNtpAssocStatusDispersion'
_d='adGenNtpAssocStatusDelay'
_c='adGenNtpAssocStatusJitter'
_b='adGenNtpAssocStratum'
_a='adGenNtpAssocOffset'
_Z='adGenNtpEntStatusReferenceDateTime'
_Y='adGenNtpEntStatusMaxNumberOfRefSources'
_X='adGenNtpEntStatusOutPkts'
_W='adGenNtpEntStatusInPkts'
_V='adGenNtpEntStatusLeapSecDirection'
_U='adGenNtpEntStatusLeapSecond'
_T='adGenNtpEntStatusDispersion'
_S='adGenNtpEntStatusNumberOfRefSources'
_R='adGenNtpEntStatusActiveOffset'
_Q='adGenNtpEntStatusActiveRefSourceName'
_P='adGenNtpEntStatusActiveRefSourceId'
_O='adGenNtpEntStatusStratum'
_N='adGenNtpAssocPrefer'
_M='adGenNtpAssocVersion'
_L='adGenNtpAssocRowStatus'
_K='adGenNtpEntStatusEntityUptime'
_J='read-write'
_I='adGenNtpAssocAddress'
_H='Unsigned32'
_G='adGenNtpEntObjectsGroup1'
_F='read-create'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='ADTRAN-GENNTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenNtp,adGenNtpCompliance,adGenNtpID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenNtp','adGenNtpCompliance','adGenNtpID')
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TruthValue')
adGenNtpMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,5,1))
if mibBuilder.loadTexts:adGenNtpMIB.setRevisions(('2014-06-02 00:00','2008-09-17 00:00'))
_AdGenNtpMIBObjects_ObjectIdentity=ObjectIdentity
adGenNtpMIBObjects=_AdGenNtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,664,5,70,5,1))
_AdGenNtpEntStatus_ObjectIdentity=ObjectIdentity
adGenNtpEntStatus=_AdGenNtpEntStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,5,1,1))
class _AdGenNtpEntStatusCurrentMode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AdGenNtpEntStatusCurrentMode_Type.__name__=_D
_AdGenNtpEntStatusCurrentMode_Object=MibScalar
adGenNtpEntStatusCurrentMode=_AdGenNtpEntStatusCurrentMode_Object((1,3,6,1,4,1,664,5,70,5,1,1,1),_AdGenNtpEntStatusCurrentMode_Type())
adGenNtpEntStatusCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusCurrentMode.setStatus(_A)
class _AdGenNtpEntStatusCurrentModeVal_Type(Integer32):defaultValue=99;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,99)));namedValues=NamedValues(*(('notRunning',1),('notSynchronized',2),('noneConfigured',3),('syncToLocal',4),('syncToRefclock',5),('syncToRemoteServer',6),('unknown',99)))
_AdGenNtpEntStatusCurrentModeVal_Type.__name__=_E
_AdGenNtpEntStatusCurrentModeVal_Object=MibScalar
adGenNtpEntStatusCurrentModeVal=_AdGenNtpEntStatusCurrentModeVal_Object((1,3,6,1,4,1,664,5,70,5,1,1,2),_AdGenNtpEntStatusCurrentModeVal_Type())
adGenNtpEntStatusCurrentModeVal.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusCurrentModeVal.setStatus(_A)
class _AdGenNtpEntStatusStratum_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AdGenNtpEntStatusStratum_Type.__name__=_E
_AdGenNtpEntStatusStratum_Object=MibScalar
adGenNtpEntStatusStratum=_AdGenNtpEntStatusStratum_Object((1,3,6,1,4,1,664,5,70,5,1,1,3),_AdGenNtpEntStatusStratum_Type())
adGenNtpEntStatusStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusStratum.setStatus(_A)
class _AdGenNtpEntStatusActiveRefSourceId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99999))
_AdGenNtpEntStatusActiveRefSourceId_Type.__name__=_E
_AdGenNtpEntStatusActiveRefSourceId_Object=MibScalar
adGenNtpEntStatusActiveRefSourceId=_AdGenNtpEntStatusActiveRefSourceId_Object((1,3,6,1,4,1,664,5,70,5,1,1,4),_AdGenNtpEntStatusActiveRefSourceId_Type())
adGenNtpEntStatusActiveRefSourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusActiveRefSourceId.setStatus(_A)
class _AdGenNtpEntStatusActiveRefSourceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AdGenNtpEntStatusActiveRefSourceName_Type.__name__=_D
_AdGenNtpEntStatusActiveRefSourceName_Object=MibScalar
adGenNtpEntStatusActiveRefSourceName=_AdGenNtpEntStatusActiveRefSourceName_Object((1,3,6,1,4,1,664,5,70,5,1,1,5),_AdGenNtpEntStatusActiveRefSourceName_Type())
adGenNtpEntStatusActiveRefSourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusActiveRefSourceName.setStatus(_A)
class _AdGenNtpEntStatusActiveOffset_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_AdGenNtpEntStatusActiveOffset_Type.__name__=_D
_AdGenNtpEntStatusActiveOffset_Object=MibScalar
adGenNtpEntStatusActiveOffset=_AdGenNtpEntStatusActiveOffset_Object((1,3,6,1,4,1,664,5,70,5,1,1,6),_AdGenNtpEntStatusActiveOffset_Type())
adGenNtpEntStatusActiveOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusActiveOffset.setStatus(_A)
class _AdGenNtpEntStatusNumberOfRefSources_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AdGenNtpEntStatusNumberOfRefSources_Type.__name__=_E
_AdGenNtpEntStatusNumberOfRefSources_Object=MibScalar
adGenNtpEntStatusNumberOfRefSources=_AdGenNtpEntStatusNumberOfRefSources_Object((1,3,6,1,4,1,664,5,70,5,1,1,7),_AdGenNtpEntStatusNumberOfRefSources_Type())
adGenNtpEntStatusNumberOfRefSources.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusNumberOfRefSources.setStatus(_A)
class _AdGenNtpEntStatusDispersion_Type(DisplayString):defaultValue=OctetString('n/a');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_AdGenNtpEntStatusDispersion_Type.__name__=_D
_AdGenNtpEntStatusDispersion_Object=MibScalar
adGenNtpEntStatusDispersion=_AdGenNtpEntStatusDispersion_Object((1,3,6,1,4,1,664,5,70,5,1,1,8),_AdGenNtpEntStatusDispersion_Type())
adGenNtpEntStatusDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusDispersion.setStatus(_A)
class _AdGenNtpEntStatusEntityUptime_Type(Unsigned32):defaultValue=0
_AdGenNtpEntStatusEntityUptime_Type.__name__=_H
_AdGenNtpEntStatusEntityUptime_Object=MibScalar
adGenNtpEntStatusEntityUptime=_AdGenNtpEntStatusEntityUptime_Object((1,3,6,1,4,1,664,5,70,5,1,1,9),_AdGenNtpEntStatusEntityUptime_Type())
adGenNtpEntStatusEntityUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusEntityUptime.setStatus(_A)
class _AdGenNtpEntStatusReferenceNtpTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AdGenNtpEntStatusReferenceNtpTime_Type.__name__=_D
_AdGenNtpEntStatusReferenceNtpTime_Object=MibScalar
adGenNtpEntStatusReferenceNtpTime=_AdGenNtpEntStatusReferenceNtpTime_Object((1,3,6,1,4,1,664,5,70,5,1,1,10),_AdGenNtpEntStatusReferenceNtpTime_Type())
adGenNtpEntStatusReferenceNtpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusReferenceNtpTime.setStatus(_A)
class _AdGenNtpEntStatusLeapSecond_Type(Integer32):defaultValue=0
_AdGenNtpEntStatusLeapSecond_Type.__name__=_E
_AdGenNtpEntStatusLeapSecond_Object=MibScalar
adGenNtpEntStatusLeapSecond=_AdGenNtpEntStatusLeapSecond_Object((1,3,6,1,4,1,664,5,70,5,1,1,11),_AdGenNtpEntStatusLeapSecond_Type())
adGenNtpEntStatusLeapSecond.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusLeapSecond.setStatus(_A)
class _AdGenNtpEntStatusLeapSecDirection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1))
_AdGenNtpEntStatusLeapSecDirection_Type.__name__=_E
_AdGenNtpEntStatusLeapSecDirection_Object=MibScalar
adGenNtpEntStatusLeapSecDirection=_AdGenNtpEntStatusLeapSecDirection_Object((1,3,6,1,4,1,664,5,70,5,1,1,12),_AdGenNtpEntStatusLeapSecDirection_Type())
adGenNtpEntStatusLeapSecDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusLeapSecDirection.setStatus(_A)
_AdGenNtpEntStatusInPkts_Type=Counter32
_AdGenNtpEntStatusInPkts_Object=MibScalar
adGenNtpEntStatusInPkts=_AdGenNtpEntStatusInPkts_Object((1,3,6,1,4,1,664,5,70,5,1,1,13),_AdGenNtpEntStatusInPkts_Type())
adGenNtpEntStatusInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusInPkts.setStatus(_A)
_AdGenNtpEntStatusOutPkts_Type=Counter32
_AdGenNtpEntStatusOutPkts_Object=MibScalar
adGenNtpEntStatusOutPkts=_AdGenNtpEntStatusOutPkts_Object((1,3,6,1,4,1,664,5,70,5,1,1,14),_AdGenNtpEntStatusOutPkts_Type())
adGenNtpEntStatusOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusOutPkts.setStatus(_A)
class _AdGenNtpEntStatusMaxNumberOfRefSources_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AdGenNtpEntStatusMaxNumberOfRefSources_Type.__name__=_E
_AdGenNtpEntStatusMaxNumberOfRefSources_Object=MibScalar
adGenNtpEntStatusMaxNumberOfRefSources=_AdGenNtpEntStatusMaxNumberOfRefSources_Object((1,3,6,1,4,1,664,5,70,5,1,1,15),_AdGenNtpEntStatusMaxNumberOfRefSources_Type())
adGenNtpEntStatusMaxNumberOfRefSources.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusMaxNumberOfRefSources.setStatus(_A)
class _AdGenNtpEntStatusReferenceDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AdGenNtpEntStatusReferenceDateTime_Type.__name__=_D
_AdGenNtpEntStatusReferenceDateTime_Object=MibScalar
adGenNtpEntStatusReferenceDateTime=_AdGenNtpEntStatusReferenceDateTime_Object((1,3,6,1,4,1,664,5,70,5,1,1,16),_AdGenNtpEntStatusReferenceDateTime_Type())
adGenNtpEntStatusReferenceDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpEntStatusReferenceDateTime.setStatus(_A)
_AdGenNtpAssociation_ObjectIdentity=ObjectIdentity
adGenNtpAssociation=_AdGenNtpAssociation_ObjectIdentity((1,3,6,1,4,1,664,5,70,5,1,2))
_AdGenNtpAssociationTable_Object=MibTable
adGenNtpAssociationTable=_AdGenNtpAssociationTable_Object((1,3,6,1,4,1,664,5,70,5,1,2,1))
if mibBuilder.loadTexts:adGenNtpAssociationTable.setStatus(_A)
_AdGenNtpAssociationEntry_Object=MibTableRow
adGenNtpAssociationEntry=_AdGenNtpAssociationEntry_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1))
adGenNtpAssociationEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:adGenNtpAssociationEntry.setStatus(_A)
_AdGenNtpAssocRowStatus_Type=RowStatus
_AdGenNtpAssocRowStatus_Object=MibTableColumn
adGenNtpAssocRowStatus=_AdGenNtpAssocRowStatus_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,1),_AdGenNtpAssocRowStatus_Type())
adGenNtpAssocRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenNtpAssocRowStatus.setStatus(_A)
_AdGenNtpAssocAddress_Type=InetAddress
_AdGenNtpAssocAddress_Object=MibTableColumn
adGenNtpAssocAddress=_AdGenNtpAssocAddress_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,2),_AdGenNtpAssocAddress_Type())
adGenNtpAssocAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenNtpAssocAddress.setStatus(_A)
class _AdGenNtpAssocVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,4))
_AdGenNtpAssocVersion_Type.__name__=_E
_AdGenNtpAssocVersion_Object=MibTableColumn
adGenNtpAssocVersion=_AdGenNtpAssocVersion_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,3),_AdGenNtpAssocVersion_Type())
adGenNtpAssocVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenNtpAssocVersion.setStatus(_A)
_AdGenNtpAssocPrefer_Type=TruthValue
_AdGenNtpAssocPrefer_Object=MibTableColumn
adGenNtpAssocPrefer=_AdGenNtpAssocPrefer_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,4),_AdGenNtpAssocPrefer_Type())
adGenNtpAssocPrefer.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenNtpAssocPrefer.setStatus(_A)
class _AdGenNtpAssocRefId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AdGenNtpAssocRefId_Type.__name__=_D
_AdGenNtpAssocRefId_Object=MibTableColumn
adGenNtpAssocRefId=_AdGenNtpAssocRefId_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,5),_AdGenNtpAssocRefId_Type())
adGenNtpAssocRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpAssocRefId.setStatus(_A)
class _AdGenNtpAssocOffset_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_AdGenNtpAssocOffset_Type.__name__=_D
_AdGenNtpAssocOffset_Object=MibTableColumn
adGenNtpAssocOffset=_AdGenNtpAssocOffset_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,6),_AdGenNtpAssocOffset_Type())
adGenNtpAssocOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpAssocOffset.setStatus(_A)
class _AdGenNtpAssocStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AdGenNtpAssocStratum_Type.__name__=_E
_AdGenNtpAssocStratum_Object=MibTableColumn
adGenNtpAssocStratum=_AdGenNtpAssocStratum_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,7),_AdGenNtpAssocStratum_Type())
adGenNtpAssocStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpAssocStratum.setStatus(_A)
class _AdGenNtpAssocStatusJitter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_AdGenNtpAssocStatusJitter_Type.__name__=_D
_AdGenNtpAssocStatusJitter_Object=MibTableColumn
adGenNtpAssocStatusJitter=_AdGenNtpAssocStatusJitter_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,8),_AdGenNtpAssocStatusJitter_Type())
adGenNtpAssocStatusJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpAssocStatusJitter.setStatus(_A)
class _AdGenNtpAssocStatusDelay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_AdGenNtpAssocStatusDelay_Type.__name__=_D
_AdGenNtpAssocStatusDelay_Object=MibTableColumn
adGenNtpAssocStatusDelay=_AdGenNtpAssocStatusDelay_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,9),_AdGenNtpAssocStatusDelay_Type())
adGenNtpAssocStatusDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpAssocStatusDelay.setStatus(_A)
class _AdGenNtpAssocStatusDispersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_AdGenNtpAssocStatusDispersion_Type.__name__=_D
_AdGenNtpAssocStatusDispersion_Object=MibTableColumn
adGenNtpAssocStatusDispersion=_AdGenNtpAssocStatusDispersion_Object((1,3,6,1,4,1,664,5,70,5,1,2,1,1,10),_AdGenNtpAssocStatusDispersion_Type())
adGenNtpAssocStatusDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenNtpAssocStatusDispersion.setStatus(_A)
_AdGenNtpAssociationScalars_ObjectIdentity=ObjectIdentity
adGenNtpAssociationScalars=_AdGenNtpAssociationScalars_ObjectIdentity((1,3,6,1,4,1,664,5,70,5,1,2,2))
_AdGenNtpAssociationBroadcast_Type=TruthValue
_AdGenNtpAssociationBroadcast_Object=MibScalar
adGenNtpAssociationBroadcast=_AdGenNtpAssociationBroadcast_Object((1,3,6,1,4,1,664,5,70,5,1,2,2,1),_AdGenNtpAssociationBroadcast_Type())
adGenNtpAssociationBroadcast.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenNtpAssociationBroadcast.setStatus(_A)
_AdGenNtpAssociationPeriodicVolley_Type=Unsigned32
_AdGenNtpAssociationPeriodicVolley_Object=MibScalar
adGenNtpAssociationPeriodicVolley=_AdGenNtpAssociationPeriodicVolley_Object((1,3,6,1,4,1,664,5,70,5,1,2,2,2),_AdGenNtpAssociationPeriodicVolley_Type())
adGenNtpAssociationPeriodicVolley.setMaxAccess(_J)
if mibBuilder.loadTexts:adGenNtpAssociationPeriodicVolley.setStatus(_A)
_AdGenNtpEntConformance_ObjectIdentity=ObjectIdentity
adGenNtpEntConformance=_AdGenNtpEntConformance_ObjectIdentity((1,3,6,1,4,1,664,99,10000,70,5,1))
_AdGenNtpEntCompliances_ObjectIdentity=ObjectIdentity
adGenNtpEntCompliances=_AdGenNtpEntCompliances_ObjectIdentity((1,3,6,1,4,1,664,99,10000,70,5,1,1))
_AdGenNtpEntGroups_ObjectIdentity=ObjectIdentity
adGenNtpEntGroups=_AdGenNtpEntGroups_ObjectIdentity((1,3,6,1,4,1,664,99,10000,70,5,1,2))
adGenNtpEntObjectsGroup1=ObjectGroup((1,3,6,1,4,1,664,99,10000,70,5,1,2,1))
adGenNtpEntObjectsGroup1.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:adGenNtpEntObjectsGroup1.setStatus(_A)
adGenNtpEntObjectsGroup2=ObjectGroup((1,3,6,1,4,1,664,99,10000,70,5,1,2,2))
adGenNtpEntObjectsGroup2.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:adGenNtpEntObjectsGroup2.setStatus(_A)
adGenNtpEntNTPCompliance=ModuleCompliance((1,3,6,1,4,1,664,99,10000,70,5,1,1,1))
adGenNtpEntNTPCompliance.setObjects(*((_B,_G),(_B,_f)))
if mibBuilder.loadTexts:adGenNtpEntNTPCompliance.setStatus(_A)
adGenNtpEntSNTPCompliance=ModuleCompliance((1,3,6,1,4,1,664,99,10000,70,5,1,1,2))
adGenNtpEntSNTPCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:adGenNtpEntSNTPCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenNtpMIBObjects':adGenNtpMIBObjects,'adGenNtpEntStatus':adGenNtpEntStatus,'adGenNtpEntStatusCurrentMode':adGenNtpEntStatusCurrentMode,'adGenNtpEntStatusCurrentModeVal':adGenNtpEntStatusCurrentModeVal,_O:adGenNtpEntStatusStratum,_P:adGenNtpEntStatusActiveRefSourceId,_Q:adGenNtpEntStatusActiveRefSourceName,_R:adGenNtpEntStatusActiveOffset,_S:adGenNtpEntStatusNumberOfRefSources,_T:adGenNtpEntStatusDispersion,_K:adGenNtpEntStatusEntityUptime,'adGenNtpEntStatusReferenceNtpTime':adGenNtpEntStatusReferenceNtpTime,_U:adGenNtpEntStatusLeapSecond,_V:adGenNtpEntStatusLeapSecDirection,_W:adGenNtpEntStatusInPkts,_X:adGenNtpEntStatusOutPkts,_Y:adGenNtpEntStatusMaxNumberOfRefSources,_Z:adGenNtpEntStatusReferenceDateTime,'adGenNtpAssociation':adGenNtpAssociation,'adGenNtpAssociationTable':adGenNtpAssociationTable,'adGenNtpAssociationEntry':adGenNtpAssociationEntry,_L:adGenNtpAssocRowStatus,_I:adGenNtpAssocAddress,_M:adGenNtpAssocVersion,_N:adGenNtpAssocPrefer,'adGenNtpAssocRefId':adGenNtpAssocRefId,_a:adGenNtpAssocOffset,_b:adGenNtpAssocStratum,_c:adGenNtpAssocStatusJitter,_d:adGenNtpAssocStatusDelay,_e:adGenNtpAssocStatusDispersion,'adGenNtpAssociationScalars':adGenNtpAssociationScalars,'adGenNtpAssociationBroadcast':adGenNtpAssociationBroadcast,'adGenNtpAssociationPeriodicVolley':adGenNtpAssociationPeriodicVolley,'adGenNtpMIB':adGenNtpMIB,'adGenNtpEntConformance':adGenNtpEntConformance,'adGenNtpEntCompliances':adGenNtpEntCompliances,'adGenNtpEntNTPCompliance':adGenNtpEntNTPCompliance,'adGenNtpEntSNTPCompliance':adGenNtpEntSNTPCompliance,'adGenNtpEntGroups':adGenNtpEntGroups,_G:adGenNtpEntObjectsGroup1,_f:adGenNtpEntObjectsGroup2})