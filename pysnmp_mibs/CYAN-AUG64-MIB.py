_Q='cyanAUG64ObjectGroup'
_P='cyanAUG64StsaugStructure'
_O='cyanAUG64SecServState'
_N='cyanAUG64OperStateQual'
_M='cyanAUG64OperState'
_L='cyanAUG64Description'
_K='cyanAUG64AutoinserviceSoakTimeSec'
_J='cyanAUG64AdminState'
_I='cyanAUG64AUG64Id'
_H='cyanAUG64ModuleId'
_G='cyanAUG64ShelfId'
_F='DisplayString'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='CYAN-AUG64-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyanEntityModules,=mibBuilder.importSymbols('CYAN-MIB','cyanEntityModules')
CyanAdminStateTc,CyanAugStructureTc,CyanOpStateQualTc,CyanOpStateTc,CyanSecServiceStateTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanAdminStateTc','CyanAugStructureTc','CyanOpStateQualTc','CyanOpStateTc','CyanSecServiceStateTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
cyanAUG64Module=ModuleIdentity((1,3,6,1,4,1,28533,5,30,240))
if mibBuilder.loadTexts:cyanAUG64Module.setRevisions(('2014-12-07 05:45',))
_CyanAUG64MibObjects_ObjectIdentity=ObjectIdentity
cyanAUG64MibObjects=_CyanAUG64MibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,240,1))
_CyanAUG64Table_Object=MibTable
cyanAUG64Table=_CyanAUG64Table_Object((1,3,6,1,4,1,28533,5,30,240,1,1))
if mibBuilder.loadTexts:cyanAUG64Table.setStatus(_A)
_CyanAUG64Entry_Object=MibTableRow
cyanAUG64Entry=_CyanAUG64Entry_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1))
cyanAUG64Entry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cyanAUG64Entry.setStatus(_A)
class _CyanAUG64ShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanAUG64ShelfId_Type.__name__=_E
_CyanAUG64ShelfId_Object=MibTableColumn
cyanAUG64ShelfId=_CyanAUG64ShelfId_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,1),_CyanAUG64ShelfId_Type())
cyanAUG64ShelfId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanAUG64ShelfId.setStatus(_A)
_CyanAUG64ModuleId_Type=Unsigned32
_CyanAUG64ModuleId_Object=MibTableColumn
cyanAUG64ModuleId=_CyanAUG64ModuleId_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,2),_CyanAUG64ModuleId_Type())
cyanAUG64ModuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanAUG64ModuleId.setStatus(_A)
_CyanAUG64AUG64Id_Type=Unsigned32
_CyanAUG64AUG64Id_Object=MibTableColumn
cyanAUG64AUG64Id=_CyanAUG64AUG64Id_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,3),_CyanAUG64AUG64Id_Type())
cyanAUG64AUG64Id.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanAUG64AUG64Id.setStatus(_A)
_CyanAUG64AdminState_Type=CyanAdminStateTc
_CyanAUG64AdminState_Object=MibTableColumn
cyanAUG64AdminState=_CyanAUG64AdminState_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,4),_CyanAUG64AdminState_Type())
cyanAUG64AdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanAUG64AdminState.setStatus(_A)
_CyanAUG64AutoinserviceSoakTimeSec_Type=Integer32
_CyanAUG64AutoinserviceSoakTimeSec_Object=MibTableColumn
cyanAUG64AutoinserviceSoakTimeSec=_CyanAUG64AutoinserviceSoakTimeSec_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,5),_CyanAUG64AutoinserviceSoakTimeSec_Type())
cyanAUG64AutoinserviceSoakTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanAUG64AutoinserviceSoakTimeSec.setStatus(_A)
class _CyanAUG64Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CyanAUG64Description_Type.__name__=_F
_CyanAUG64Description_Object=MibTableColumn
cyanAUG64Description=_CyanAUG64Description_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,6),_CyanAUG64Description_Type())
cyanAUG64Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanAUG64Description.setStatus(_A)
_CyanAUG64OperState_Type=CyanOpStateTc
_CyanAUG64OperState_Object=MibTableColumn
cyanAUG64OperState=_CyanAUG64OperState_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,7),_CyanAUG64OperState_Type())
cyanAUG64OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanAUG64OperState.setStatus(_A)
_CyanAUG64OperStateQual_Type=CyanOpStateQualTc
_CyanAUG64OperStateQual_Object=MibTableColumn
cyanAUG64OperStateQual=_CyanAUG64OperStateQual_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,8),_CyanAUG64OperStateQual_Type())
cyanAUG64OperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanAUG64OperStateQual.setStatus(_A)
_CyanAUG64SecServState_Type=CyanSecServiceStateTc
_CyanAUG64SecServState_Object=MibTableColumn
cyanAUG64SecServState=_CyanAUG64SecServState_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,9),_CyanAUG64SecServState_Type())
cyanAUG64SecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanAUG64SecServState.setStatus(_A)
_CyanAUG64StsaugStructure_Type=CyanAugStructureTc
_CyanAUG64StsaugStructure_Object=MibTableColumn
cyanAUG64StsaugStructure=_CyanAUG64StsaugStructure_Object((1,3,6,1,4,1,28533,5,30,240,1,1,1,10),_CyanAUG64StsaugStructure_Type())
cyanAUG64StsaugStructure.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanAUG64StsaugStructure.setStatus(_A)
cyanAUG64ObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,240,20))
cyanAUG64ObjectGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cyanAUG64ObjectGroup.setStatus(_A)
cyanAUG64Compliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,240,30))
cyanAUG64Compliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:cyanAUG64Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanAUG64Module':cyanAUG64Module,'cyanAUG64MibObjects':cyanAUG64MibObjects,'cyanAUG64Table':cyanAUG64Table,'cyanAUG64Entry':cyanAUG64Entry,_G:cyanAUG64ShelfId,_H:cyanAUG64ModuleId,_I:cyanAUG64AUG64Id,_J:cyanAUG64AdminState,_K:cyanAUG64AutoinserviceSoakTimeSec,_L:cyanAUG64Description,_M:cyanAUG64OperState,_N:cyanAUG64OperStateQual,_O:cyanAUG64SecServState,_P:cyanAUG64StsaugStructure,_Q:cyanAUG64ObjectGroup,'cyanAUG64Compliance':cyanAUG64Compliance})