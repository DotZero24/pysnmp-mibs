_E='not-accessible'
_D='asTermCardIndex'
_C='IPE-TERM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class OffOnValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('invalid',0),('off',1),('on',2)))
class SeverityValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),('indetermine',2),('critical',3),('major',4),('minor',5),('warning',6)))
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
_AlarmStatusGroup_ObjectIdentity=ObjectIdentity
alarmStatusGroup=_AlarmStatusGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,3))
_AsTermCardGroup_ObjectIdentity=ObjectIdentity
asTermCardGroup=_AsTermCardGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,3,36))
_AsTermCardTable_Object=MibTable
asTermCardTable=_AsTermCardTable_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1))
if mibBuilder.loadTexts:asTermCardTable.setStatus(_A)
_AsTermCardEntry_Object=MibTableRow
asTermCardEntry=_AsTermCardEntry_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1))
asTermCardEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:asTermCardEntry.setStatus(_A)
_AsTermCardIndex_Type=Integer32
_AsTermCardIndex_Object=MibTableColumn
asTermCardIndex=_AsTermCardIndex_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1,1),_AsTermCardIndex_Type())
asTermCardIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:asTermCardIndex.setStatus(_A)
_AsTermCardNEAddress_Type=IpAddress
_AsTermCardNEAddress_Object=MibTableColumn
asTermCardNEAddress=_AsTermCardNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1,2),_AsTermCardNEAddress_Type())
asTermCardNEAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:asTermCardNEAddress.setStatus(_A)
_TermAlarm_Type=SeverityValue
_TermAlarm_Object=MibTableColumn
termAlarm=_TermAlarm_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1,3),_TermAlarm_Type())
termAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:termAlarm.setStatus(_A)
_TermComFailAlarm_Type=SeverityValue
_TermComFailAlarm_Object=MibTableColumn
termComFailAlarm=_TermComFailAlarm_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1,4),_TermComFailAlarm_Type())
termComFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:termComFailAlarm.setStatus(_A)
_TermUnequipped_Type=SeverityValue
_TermUnequipped_Object=MibTableColumn
termUnequipped=_TermUnequipped_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1,5),_TermUnequipped_Type())
termUnequipped.setMaxAccess(_B)
if mibBuilder.loadTexts:termUnequipped.setStatus(_A)
_TermTypeMismatch_Type=SeverityValue
_TermTypeMismatch_Object=MibTableColumn
termTypeMismatch=_TermTypeMismatch_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1,6),_TermTypeMismatch_Type())
termTypeMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:termTypeMismatch.setStatus(_A)
_TermCardChange_Type=OffOnValue
_TermCardChange_Object=MibTableColumn
termCardChange=_TermCardChange_Object((1,3,6,1,4,1,119,2,3,69,501,3,36,1,1,7),_TermCardChange_Type())
termCardChange.setMaxAccess(_B)
if mibBuilder.loadTexts:termCardChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'OffOnValue':OffOnValue,'SeverityValue':SeverityValue,'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'radioEquipment':radioEquipment,'pasoNeoIpe-common':pasoNeoIpe_common,'alarmStatusGroup':alarmStatusGroup,'asTermCardGroup':asTermCardGroup,'asTermCardTable':asTermCardTable,'asTermCardEntry':asTermCardEntry,_D:asTermCardIndex,'asTermCardNEAddress':asTermCardNEAddress,'termAlarm':termAlarm,'termComFailAlarm':termComFailAlarm,'termUnequipped':termUnequipped,'termTypeMismatch':termTypeMismatch,'termCardChange':termCardChange})