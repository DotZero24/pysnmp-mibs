_F='read-only'
_E='not-accessible'
_D='maintFuncSummaryCategory'
_C='IPE-FUNC-SUMMARY-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_RadioEquipment_ObjectIdentity=ObjectIdentity
radioEquipment=_RadioEquipment_ObjectIdentity((1,3,6,1,4,1,119,2,3,69))
_PasoNeoIpe_common_ObjectIdentity=ObjectIdentity
pasoNeoIpe_common=_PasoNeoIpe_common_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501))
_SummaryGroup_ObjectIdentity=ObjectIdentity
summaryGroup=_SummaryGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,1))
_MaintSummaryGroup_ObjectIdentity=ObjectIdentity
maintSummaryGroup=_MaintSummaryGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,1,2))
_MaintFuncSummaryTable_Object=MibTable
maintFuncSummaryTable=_MaintFuncSummaryTable_Object((1,3,6,1,4,1,119,2,3,69,501,1,2,2))
if mibBuilder.loadTexts:maintFuncSummaryTable.setStatus(_A)
_MaintFuncSummaryEntry_Object=MibTableRow
maintFuncSummaryEntry=_MaintFuncSummaryEntry_Object((1,3,6,1,4,1,119,2,3,69,501,1,2,2,1))
maintFuncSummaryEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:maintFuncSummaryEntry.setStatus(_A)
class _MaintFuncSummaryCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17)));namedValues=NamedValues(*(('modemLb',1),('modemMaint',2),('modemSwgMaint',3),('e1Lb1',4),('e1Lb2',5),('stm1Lb1',6),('stm1Lb2',7),('sncpControl',8),('timingSourceControl',9),('laserShutdownControl',10),('fileUpdate',11),('etherring',12),('aps',13),('dot3ah',14),('modemL2Lb1',16),('modemL2Lb2',17)))
_MaintFuncSummaryCategory_Type.__name__=_B
_MaintFuncSummaryCategory_Object=MibTableColumn
maintFuncSummaryCategory=_MaintFuncSummaryCategory_Object((1,3,6,1,4,1,119,2,3,69,501,1,2,2,1,1),_MaintFuncSummaryCategory_Type())
maintFuncSummaryCategory.setMaxAccess(_E)
if mibBuilder.loadTexts:maintFuncSummaryCategory.setStatus(_A)
_MaintFuncSummaryNEAddress_Type=IpAddress
_MaintFuncSummaryNEAddress_Object=MibTableColumn
maintFuncSummaryNEAddress=_MaintFuncSummaryNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,1,2,2,1,2),_MaintFuncSummaryNEAddress_Type())
maintFuncSummaryNEAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:maintFuncSummaryNEAddress.setStatus(_A)
class _MaintFuncSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('invalid',0),('none',1),('executed',2)))
_MaintFuncSummary_Type.__name__=_B
_MaintFuncSummary_Object=MibTableColumn
maintFuncSummary=_MaintFuncSummary_Object((1,3,6,1,4,1,119,2,3,69,501,1,2,2,1,3),_MaintFuncSummary_Type())
maintFuncSummary.setMaxAccess(_F)
if mibBuilder.loadTexts:maintFuncSummary.setStatus(_A)
_MaintFuncSummaryLastUpdated_Type=DateAndTime
_MaintFuncSummaryLastUpdated_Object=MibTableColumn
maintFuncSummaryLastUpdated=_MaintFuncSummaryLastUpdated_Object((1,3,6,1,4,1,119,2,3,69,501,1,2,2,1,4),_MaintFuncSummaryLastUpdated_Type())
maintFuncSummaryLastUpdated.setMaxAccess(_F)
if mibBuilder.loadTexts:maintFuncSummaryLastUpdated.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'radioEquipment':radioEquipment,'pasoNeoIpe-common':pasoNeoIpe_common,'summaryGroup':summaryGroup,'maintSummaryGroup':maintSummaryGroup,'maintFuncSummaryTable':maintFuncSummaryTable,'maintFuncSummaryEntry':maintFuncSummaryEntry,_D:maintFuncSummaryCategory,'maintFuncSummaryNEAddress':maintFuncSummaryNEAddress,'maintFuncSummary':maintFuncSummary,'maintFuncSummaryLastUpdated':maintFuncSummaryLastUpdated})