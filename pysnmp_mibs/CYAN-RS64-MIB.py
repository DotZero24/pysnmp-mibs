_N='cyanRS64ObjectGroup'
_M='cyanRS64SecServState'
_L='cyanRS64OperStateQual'
_K='cyanRS64OperState'
_J='cyanRS64AutoinserviceSoakTimeSec'
_I='cyanRS64AdminState'
_H='cyanRS64RS64Id'
_G='cyanRS64ModuleId'
_F='cyanRS64ShelfId'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='CYAN-RS64-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyanEntityModules,=mibBuilder.importSymbols('CYAN-MIB','cyanEntityModules')
CyanAdminStateTc,CyanOpStateQualTc,CyanOpStateTc,CyanSecServiceStateTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanAdminStateTc','CyanOpStateQualTc','CyanOpStateTc','CyanSecServiceStateTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyanRS64Module=ModuleIdentity((1,3,6,1,4,1,28533,5,30,220))
if mibBuilder.loadTexts:cyanRS64Module.setRevisions(('2014-12-07 05:45',))
_CyanRS64MibObjects_ObjectIdentity=ObjectIdentity
cyanRS64MibObjects=_CyanRS64MibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,220,1))
_CyanRS64Table_Object=MibTable
cyanRS64Table=_CyanRS64Table_Object((1,3,6,1,4,1,28533,5,30,220,1,1))
if mibBuilder.loadTexts:cyanRS64Table.setStatus(_A)
_CyanRS64Entry_Object=MibTableRow
cyanRS64Entry=_CyanRS64Entry_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1))
cyanRS64Entry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cyanRS64Entry.setStatus(_A)
class _CyanRS64ShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanRS64ShelfId_Type.__name__=_E
_CyanRS64ShelfId_Object=MibTableColumn
cyanRS64ShelfId=_CyanRS64ShelfId_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,1),_CyanRS64ShelfId_Type())
cyanRS64ShelfId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanRS64ShelfId.setStatus(_A)
_CyanRS64ModuleId_Type=Unsigned32
_CyanRS64ModuleId_Object=MibTableColumn
cyanRS64ModuleId=_CyanRS64ModuleId_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,2),_CyanRS64ModuleId_Type())
cyanRS64ModuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanRS64ModuleId.setStatus(_A)
_CyanRS64RS64Id_Type=Unsigned32
_CyanRS64RS64Id_Object=MibTableColumn
cyanRS64RS64Id=_CyanRS64RS64Id_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,3),_CyanRS64RS64Id_Type())
cyanRS64RS64Id.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanRS64RS64Id.setStatus(_A)
_CyanRS64AdminState_Type=CyanAdminStateTc
_CyanRS64AdminState_Object=MibTableColumn
cyanRS64AdminState=_CyanRS64AdminState_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,4),_CyanRS64AdminState_Type())
cyanRS64AdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanRS64AdminState.setStatus(_A)
_CyanRS64AutoinserviceSoakTimeSec_Type=Integer32
_CyanRS64AutoinserviceSoakTimeSec_Object=MibTableColumn
cyanRS64AutoinserviceSoakTimeSec=_CyanRS64AutoinserviceSoakTimeSec_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,5),_CyanRS64AutoinserviceSoakTimeSec_Type())
cyanRS64AutoinserviceSoakTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanRS64AutoinserviceSoakTimeSec.setStatus(_A)
_CyanRS64OperState_Type=CyanOpStateTc
_CyanRS64OperState_Object=MibTableColumn
cyanRS64OperState=_CyanRS64OperState_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,6),_CyanRS64OperState_Type())
cyanRS64OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanRS64OperState.setStatus(_A)
_CyanRS64OperStateQual_Type=CyanOpStateQualTc
_CyanRS64OperStateQual_Object=MibTableColumn
cyanRS64OperStateQual=_CyanRS64OperStateQual_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,7),_CyanRS64OperStateQual_Type())
cyanRS64OperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanRS64OperStateQual.setStatus(_A)
_CyanRS64SecServState_Type=CyanSecServiceStateTc
_CyanRS64SecServState_Object=MibTableColumn
cyanRS64SecServState=_CyanRS64SecServState_Object((1,3,6,1,4,1,28533,5,30,220,1,1,1,8),_CyanRS64SecServState_Type())
cyanRS64SecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanRS64SecServState.setStatus(_A)
cyanRS64ObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,220,20))
cyanRS64ObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cyanRS64ObjectGroup.setStatus(_A)
cyanRS64Compliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,220,30))
cyanRS64Compliance.setObjects((_B,_N))
if mibBuilder.loadTexts:cyanRS64Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanRS64Module':cyanRS64Module,'cyanRS64MibObjects':cyanRS64MibObjects,'cyanRS64Table':cyanRS64Table,'cyanRS64Entry':cyanRS64Entry,_F:cyanRS64ShelfId,_G:cyanRS64ModuleId,_H:cyanRS64RS64Id,_I:cyanRS64AdminState,_J:cyanRS64AutoinserviceSoakTimeSec,_K:cyanRS64OperState,_L:cyanRS64OperStateQual,_M:cyanRS64SecServState,_N:cyanRS64ObjectGroup,'cyanRS64Compliance':cyanRS64Compliance})