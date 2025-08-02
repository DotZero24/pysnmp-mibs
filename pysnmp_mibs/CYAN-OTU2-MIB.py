_R='cyanOTU2ObjectGroup'
_Q='cyanOTU2SupportedRates'
_P='cyanOTU2SecServState'
_O='cyanOTU2RxFecErrorCorrection'
_N='cyanOTU2OperStateQual'
_M='cyanOTU2OperState'
_L='cyanOTU2ForwardErrorCoding'
_K='cyanOTU2FecCorrectableBitErrorsCurrSec'
_J='cyanOTU2AutoinserviceSoakTimeSec'
_I='cyanOTU2AdminState'
_H='cyanOTU2OTU2Id'
_G='cyanOTU2ModuleId'
_F='cyanOTU2ShelfId'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='CYAN-OTU2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyanEntityModules,=mibBuilder.importSymbols('CYAN-MIB','cyanEntityModules')
CyanAdminStateTc,CyanEnDisabledTc,CyanFecModeTc,CyanLayerRateTc,CyanOpStateQualTc,CyanOpStateTc,CyanSecServiceStateTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanAdminStateTc','CyanEnDisabledTc','CyanFecModeTc','CyanLayerRateTc','CyanOpStateQualTc','CyanOpStateTc','CyanSecServiceStateTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyanOTU2Module=ModuleIdentity((1,3,6,1,4,1,28533,5,30,190))
if mibBuilder.loadTexts:cyanOTU2Module.setRevisions(('2014-12-07 05:45',))
_CyanOTU2MibObjects_ObjectIdentity=ObjectIdentity
cyanOTU2MibObjects=_CyanOTU2MibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,190,1))
_CyanOTU2Table_Object=MibTable
cyanOTU2Table=_CyanOTU2Table_Object((1,3,6,1,4,1,28533,5,30,190,1,1))
if mibBuilder.loadTexts:cyanOTU2Table.setStatus(_A)
_CyanOTU2Entry_Object=MibTableRow
cyanOTU2Entry=_CyanOTU2Entry_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1))
cyanOTU2Entry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cyanOTU2Entry.setStatus(_A)
class _CyanOTU2ShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanOTU2ShelfId_Type.__name__=_E
_CyanOTU2ShelfId_Object=MibTableColumn
cyanOTU2ShelfId=_CyanOTU2ShelfId_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,1),_CyanOTU2ShelfId_Type())
cyanOTU2ShelfId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanOTU2ShelfId.setStatus(_A)
_CyanOTU2ModuleId_Type=Unsigned32
_CyanOTU2ModuleId_Object=MibTableColumn
cyanOTU2ModuleId=_CyanOTU2ModuleId_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,2),_CyanOTU2ModuleId_Type())
cyanOTU2ModuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanOTU2ModuleId.setStatus(_A)
_CyanOTU2OTU2Id_Type=Unsigned32
_CyanOTU2OTU2Id_Object=MibTableColumn
cyanOTU2OTU2Id=_CyanOTU2OTU2Id_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,3),_CyanOTU2OTU2Id_Type())
cyanOTU2OTU2Id.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanOTU2OTU2Id.setStatus(_A)
_CyanOTU2AdminState_Type=CyanAdminStateTc
_CyanOTU2AdminState_Object=MibTableColumn
cyanOTU2AdminState=_CyanOTU2AdminState_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,4),_CyanOTU2AdminState_Type())
cyanOTU2AdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2AdminState.setStatus(_A)
_CyanOTU2AutoinserviceSoakTimeSec_Type=Integer32
_CyanOTU2AutoinserviceSoakTimeSec_Object=MibTableColumn
cyanOTU2AutoinserviceSoakTimeSec=_CyanOTU2AutoinserviceSoakTimeSec_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,5),_CyanOTU2AutoinserviceSoakTimeSec_Type())
cyanOTU2AutoinserviceSoakTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2AutoinserviceSoakTimeSec.setStatus(_A)
_CyanOTU2FecCorrectableBitErrorsCurrSec_Type=Unsigned32
_CyanOTU2FecCorrectableBitErrorsCurrSec_Object=MibTableColumn
cyanOTU2FecCorrectableBitErrorsCurrSec=_CyanOTU2FecCorrectableBitErrorsCurrSec_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,6),_CyanOTU2FecCorrectableBitErrorsCurrSec_Type())
cyanOTU2FecCorrectableBitErrorsCurrSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2FecCorrectableBitErrorsCurrSec.setStatus(_A)
_CyanOTU2ForwardErrorCoding_Type=CyanFecModeTc
_CyanOTU2ForwardErrorCoding_Object=MibTableColumn
cyanOTU2ForwardErrorCoding=_CyanOTU2ForwardErrorCoding_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,7),_CyanOTU2ForwardErrorCoding_Type())
cyanOTU2ForwardErrorCoding.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2ForwardErrorCoding.setStatus(_A)
_CyanOTU2OperState_Type=CyanOpStateTc
_CyanOTU2OperState_Object=MibTableColumn
cyanOTU2OperState=_CyanOTU2OperState_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,8),_CyanOTU2OperState_Type())
cyanOTU2OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2OperState.setStatus(_A)
_CyanOTU2OperStateQual_Type=CyanOpStateQualTc
_CyanOTU2OperStateQual_Object=MibTableColumn
cyanOTU2OperStateQual=_CyanOTU2OperStateQual_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,9),_CyanOTU2OperStateQual_Type())
cyanOTU2OperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2OperStateQual.setStatus(_A)
_CyanOTU2RxFecErrorCorrection_Type=CyanEnDisabledTc
_CyanOTU2RxFecErrorCorrection_Object=MibTableColumn
cyanOTU2RxFecErrorCorrection=_CyanOTU2RxFecErrorCorrection_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,10),_CyanOTU2RxFecErrorCorrection_Type())
cyanOTU2RxFecErrorCorrection.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2RxFecErrorCorrection.setStatus(_A)
_CyanOTU2SecServState_Type=CyanSecServiceStateTc
_CyanOTU2SecServState_Object=MibTableColumn
cyanOTU2SecServState=_CyanOTU2SecServState_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,11),_CyanOTU2SecServState_Type())
cyanOTU2SecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2SecServState.setStatus(_A)
_CyanOTU2SupportedRates_Type=CyanLayerRateTc
_CyanOTU2SupportedRates_Object=MibTableColumn
cyanOTU2SupportedRates=_CyanOTU2SupportedRates_Object((1,3,6,1,4,1,28533,5,30,190,1,1,1,12),_CyanOTU2SupportedRates_Type())
cyanOTU2SupportedRates.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanOTU2SupportedRates.setStatus(_A)
cyanOTU2ObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,190,20))
cyanOTU2ObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cyanOTU2ObjectGroup.setStatus(_A)
cyanOTU2Compliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,190,30))
cyanOTU2Compliance.setObjects((_B,_R))
if mibBuilder.loadTexts:cyanOTU2Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanOTU2Module':cyanOTU2Module,'cyanOTU2MibObjects':cyanOTU2MibObjects,'cyanOTU2Table':cyanOTU2Table,'cyanOTU2Entry':cyanOTU2Entry,_F:cyanOTU2ShelfId,_G:cyanOTU2ModuleId,_H:cyanOTU2OTU2Id,_I:cyanOTU2AdminState,_J:cyanOTU2AutoinserviceSoakTimeSec,_K:cyanOTU2FecCorrectableBitErrorsCurrSec,_L:cyanOTU2ForwardErrorCoding,_M:cyanOTU2OperState,_N:cyanOTU2OperStateQual,_O:cyanOTU2RxFecErrorCorrection,_P:cyanOTU2SecServState,_Q:cyanOTU2SupportedRates,_R:cyanOTU2ObjectGroup,'cyanOTU2Compliance':cyanOTU2Compliance})