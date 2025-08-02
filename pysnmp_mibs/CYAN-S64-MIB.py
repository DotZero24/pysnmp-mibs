_T='cyanS64ObjectGroup'
_S='cyanS64SecServState'
_R='cyanS64OperStateQual'
_Q='cyanS64OperState'
_P='cyanS64Monitorterminate'
_O='cyanS64Inserted'
_N='cyanS64Expected'
_M='cyanS64Description'
_L='cyanS64AutoinserviceSoakTimeSec'
_K='cyanS64AdminState'
_J='cyanS64Accepted'
_I='cyanS64S64Id'
_H='cyanS64ModuleId'
_G='cyanS64ShelfId'
_F='DisplayString'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='CYAN-S64-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyanEntityModules,=mibBuilder.importSymbols('CYAN-MIB','cyanEntityModules')
CyanAdminStateTc,CyanNimTc,CyanOpStateQualTc,CyanOpStateTc,CyanSdhSnSignalLabelTc,CyanSecServiceStateTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanAdminStateTc','CyanNimTc','CyanOpStateQualTc','CyanOpStateTc','CyanSdhSnSignalLabelTc','CyanSecServiceStateTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
cyanS64Module=ModuleIdentity((1,3,6,1,4,1,28533,5,30,250))
if mibBuilder.loadTexts:cyanS64Module.setRevisions(('2014-12-07 05:45',))
_CyanS64MibObjects_ObjectIdentity=ObjectIdentity
cyanS64MibObjects=_CyanS64MibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,250,1))
_CyanS64Table_Object=MibTable
cyanS64Table=_CyanS64Table_Object((1,3,6,1,4,1,28533,5,30,250,1,1))
if mibBuilder.loadTexts:cyanS64Table.setStatus(_A)
_CyanS64Entry_Object=MibTableRow
cyanS64Entry=_CyanS64Entry_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1))
cyanS64Entry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cyanS64Entry.setStatus(_A)
class _CyanS64ShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanS64ShelfId_Type.__name__=_E
_CyanS64ShelfId_Object=MibTableColumn
cyanS64ShelfId=_CyanS64ShelfId_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,1),_CyanS64ShelfId_Type())
cyanS64ShelfId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanS64ShelfId.setStatus(_A)
_CyanS64ModuleId_Type=Unsigned32
_CyanS64ModuleId_Object=MibTableColumn
cyanS64ModuleId=_CyanS64ModuleId_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,2),_CyanS64ModuleId_Type())
cyanS64ModuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanS64ModuleId.setStatus(_A)
_CyanS64S64Id_Type=Unsigned32
_CyanS64S64Id_Object=MibTableColumn
cyanS64S64Id=_CyanS64S64Id_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,3),_CyanS64S64Id_Type())
cyanS64S64Id.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanS64S64Id.setStatus(_A)
_CyanS64Accepted_Type=CyanSdhSnSignalLabelTc
_CyanS64Accepted_Object=MibTableColumn
cyanS64Accepted=_CyanS64Accepted_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,4),_CyanS64Accepted_Type())
cyanS64Accepted.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64Accepted.setStatus(_A)
_CyanS64AdminState_Type=CyanAdminStateTc
_CyanS64AdminState_Object=MibTableColumn
cyanS64AdminState=_CyanS64AdminState_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,5),_CyanS64AdminState_Type())
cyanS64AdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64AdminState.setStatus(_A)
_CyanS64AutoinserviceSoakTimeSec_Type=Integer32
_CyanS64AutoinserviceSoakTimeSec_Object=MibTableColumn
cyanS64AutoinserviceSoakTimeSec=_CyanS64AutoinserviceSoakTimeSec_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,6),_CyanS64AutoinserviceSoakTimeSec_Type())
cyanS64AutoinserviceSoakTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64AutoinserviceSoakTimeSec.setStatus(_A)
class _CyanS64Description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CyanS64Description_Type.__name__=_F
_CyanS64Description_Object=MibTableColumn
cyanS64Description=_CyanS64Description_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,7),_CyanS64Description_Type())
cyanS64Description.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64Description.setStatus(_A)
_CyanS64Expected_Type=CyanSdhSnSignalLabelTc
_CyanS64Expected_Object=MibTableColumn
cyanS64Expected=_CyanS64Expected_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,8),_CyanS64Expected_Type())
cyanS64Expected.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64Expected.setStatus(_A)
_CyanS64Inserted_Type=CyanSdhSnSignalLabelTc
_CyanS64Inserted_Object=MibTableColumn
cyanS64Inserted=_CyanS64Inserted_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,9),_CyanS64Inserted_Type())
cyanS64Inserted.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64Inserted.setStatus(_A)
_CyanS64Monitorterminate_Type=CyanNimTc
_CyanS64Monitorterminate_Object=MibTableColumn
cyanS64Monitorterminate=_CyanS64Monitorterminate_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,10),_CyanS64Monitorterminate_Type())
cyanS64Monitorterminate.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64Monitorterminate.setStatus(_A)
_CyanS64OperState_Type=CyanOpStateTc
_CyanS64OperState_Object=MibTableColumn
cyanS64OperState=_CyanS64OperState_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,11),_CyanS64OperState_Type())
cyanS64OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64OperState.setStatus(_A)
_CyanS64OperStateQual_Type=CyanOpStateQualTc
_CyanS64OperStateQual_Object=MibTableColumn
cyanS64OperStateQual=_CyanS64OperStateQual_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,12),_CyanS64OperStateQual_Type())
cyanS64OperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64OperStateQual.setStatus(_A)
_CyanS64SecServState_Type=CyanSecServiceStateTc
_CyanS64SecServState_Object=MibTableColumn
cyanS64SecServState=_CyanS64SecServState_Object((1,3,6,1,4,1,28533,5,30,250,1,1,1,13),_CyanS64SecServState_Type())
cyanS64SecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanS64SecServState.setStatus(_A)
cyanS64ObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,250,20))
cyanS64ObjectGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cyanS64ObjectGroup.setStatus(_A)
cyanS64Compliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,250,30))
cyanS64Compliance.setObjects((_B,_T))
if mibBuilder.loadTexts:cyanS64Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanS64Module':cyanS64Module,'cyanS64MibObjects':cyanS64MibObjects,'cyanS64Table':cyanS64Table,'cyanS64Entry':cyanS64Entry,_G:cyanS64ShelfId,_H:cyanS64ModuleId,_I:cyanS64S64Id,_J:cyanS64Accepted,_K:cyanS64AdminState,_L:cyanS64AutoinserviceSoakTimeSec,_M:cyanS64Description,_N:cyanS64Expected,_O:cyanS64Inserted,_P:cyanS64Monitorterminate,_Q:cyanS64OperState,_R:cyanS64OperStateQual,_S:cyanS64SecServState,_T:cyanS64ObjectGroup,'cyanS64Compliance':cyanS64Compliance})