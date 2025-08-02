_Q='cyanMS64ObjectGroup'
_P='cyanMS64SecServState'
_O='cyanMS64OperStateQual'
_N='cyanMS64OperState'
_M='cyanMS64Inserted'
_L='cyanMS64ChannelId'
_K='cyanMS64AutoinserviceSoakTimeSec'
_J='cyanMS64AdminState'
_I='cyanMS64Accepted'
_H='cyanMS64MS64Id'
_G='cyanMS64ModuleId'
_F='cyanMS64ShelfId'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='CYAN-MS64-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyanEntityModules,=mibBuilder.importSymbols('CYAN-MIB','cyanEntityModules')
CyanAdminStateTc,CyanChannelIdTc,CyanOpStateQualTc,CyanOpStateTc,CyanSecServiceStateTc,CyanSsBitsTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanAdminStateTc','CyanChannelIdTc','CyanOpStateQualTc','CyanOpStateTc','CyanSecServiceStateTc','CyanSsBitsTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyanMS64Module=ModuleIdentity((1,3,6,1,4,1,28533,5,30,230))
if mibBuilder.loadTexts:cyanMS64Module.setRevisions(('2014-12-07 05:45',))
_CyanMS64MibObjects_ObjectIdentity=ObjectIdentity
cyanMS64MibObjects=_CyanMS64MibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,230,1))
_CyanMS64Table_Object=MibTable
cyanMS64Table=_CyanMS64Table_Object((1,3,6,1,4,1,28533,5,30,230,1,1))
if mibBuilder.loadTexts:cyanMS64Table.setStatus(_A)
_CyanMS64Entry_Object=MibTableRow
cyanMS64Entry=_CyanMS64Entry_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1))
cyanMS64Entry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cyanMS64Entry.setStatus(_A)
class _CyanMS64ShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanMS64ShelfId_Type.__name__=_E
_CyanMS64ShelfId_Object=MibTableColumn
cyanMS64ShelfId=_CyanMS64ShelfId_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,1),_CyanMS64ShelfId_Type())
cyanMS64ShelfId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanMS64ShelfId.setStatus(_A)
_CyanMS64ModuleId_Type=Unsigned32
_CyanMS64ModuleId_Object=MibTableColumn
cyanMS64ModuleId=_CyanMS64ModuleId_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,2),_CyanMS64ModuleId_Type())
cyanMS64ModuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanMS64ModuleId.setStatus(_A)
_CyanMS64MS64Id_Type=Unsigned32
_CyanMS64MS64Id_Object=MibTableColumn
cyanMS64MS64Id=_CyanMS64MS64Id_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,3),_CyanMS64MS64Id_Type())
cyanMS64MS64Id.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanMS64MS64Id.setStatus(_A)
_CyanMS64Accepted_Type=CyanSsBitsTc
_CyanMS64Accepted_Object=MibTableColumn
cyanMS64Accepted=_CyanMS64Accepted_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,4),_CyanMS64Accepted_Type())
cyanMS64Accepted.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64Accepted.setStatus(_A)
_CyanMS64AdminState_Type=CyanAdminStateTc
_CyanMS64AdminState_Object=MibTableColumn
cyanMS64AdminState=_CyanMS64AdminState_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,5),_CyanMS64AdminState_Type())
cyanMS64AdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64AdminState.setStatus(_A)
_CyanMS64AutoinserviceSoakTimeSec_Type=Integer32
_CyanMS64AutoinserviceSoakTimeSec_Object=MibTableColumn
cyanMS64AutoinserviceSoakTimeSec=_CyanMS64AutoinserviceSoakTimeSec_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,6),_CyanMS64AutoinserviceSoakTimeSec_Type())
cyanMS64AutoinserviceSoakTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64AutoinserviceSoakTimeSec.setStatus(_A)
_CyanMS64ChannelId_Type=CyanChannelIdTc
_CyanMS64ChannelId_Object=MibTableColumn
cyanMS64ChannelId=_CyanMS64ChannelId_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,7),_CyanMS64ChannelId_Type())
cyanMS64ChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64ChannelId.setStatus(_A)
_CyanMS64Inserted_Type=CyanSsBitsTc
_CyanMS64Inserted_Object=MibTableColumn
cyanMS64Inserted=_CyanMS64Inserted_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,8),_CyanMS64Inserted_Type())
cyanMS64Inserted.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64Inserted.setStatus(_A)
_CyanMS64OperState_Type=CyanOpStateTc
_CyanMS64OperState_Object=MibTableColumn
cyanMS64OperState=_CyanMS64OperState_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,9),_CyanMS64OperState_Type())
cyanMS64OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64OperState.setStatus(_A)
_CyanMS64OperStateQual_Type=CyanOpStateQualTc
_CyanMS64OperStateQual_Object=MibTableColumn
cyanMS64OperStateQual=_CyanMS64OperStateQual_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,10),_CyanMS64OperStateQual_Type())
cyanMS64OperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64OperStateQual.setStatus(_A)
_CyanMS64SecServState_Type=CyanSecServiceStateTc
_CyanMS64SecServState_Object=MibTableColumn
cyanMS64SecServState=_CyanMS64SecServState_Object((1,3,6,1,4,1,28533,5,30,230,1,1,1,11),_CyanMS64SecServState_Type())
cyanMS64SecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanMS64SecServState.setStatus(_A)
cyanMS64ObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,230,20))
cyanMS64ObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cyanMS64ObjectGroup.setStatus(_A)
cyanMS64Compliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,230,30))
cyanMS64Compliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:cyanMS64Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanMS64Module':cyanMS64Module,'cyanMS64MibObjects':cyanMS64MibObjects,'cyanMS64Table':cyanMS64Table,'cyanMS64Entry':cyanMS64Entry,_F:cyanMS64ShelfId,_G:cyanMS64ModuleId,_H:cyanMS64MS64Id,_I:cyanMS64Accepted,_J:cyanMS64AdminState,_K:cyanMS64AutoinserviceSoakTimeSec,_L:cyanMS64ChannelId,_M:cyanMS64Inserted,_N:cyanMS64OperState,_O:cyanMS64OperStateQual,_P:cyanMS64SecServState,_Q:cyanMS64ObjectGroup,'cyanMS64Compliance':cyanMS64Compliance})