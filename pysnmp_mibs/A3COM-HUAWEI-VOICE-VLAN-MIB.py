_H='h3cVoiceVlanPortifIndex'
_G='manual'
_F='h3cVoiceVlanOuiAddress'
_E='OctetString'
_D='A3COM-HUAWEI-VOICE-VLAN-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cVoiceVlan=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,9))
if mibBuilder.loadTexts:h3cVoiceVlan.setRevisions(('2009-05-15 00:00','2002-07-01 00:00'))
class PortList(TextualConvention,OctetString):status=_A
_H3cvoiceVlanOuiTable_Object=MibTable
h3cvoiceVlanOuiTable=_H3cvoiceVlanOuiTable_Object((1,3,6,1,4,1,43,45,1,10,2,9,1))
if mibBuilder.loadTexts:h3cvoiceVlanOuiTable.setStatus(_A)
_H3cvoiceVlanOuiEntry_Object=MibTableRow
h3cvoiceVlanOuiEntry=_H3cvoiceVlanOuiEntry_Object((1,3,6,1,4,1,43,45,1,10,2,9,1,1))
h3cvoiceVlanOuiEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cvoiceVlanOuiEntry.setStatus(_A)
_H3cVoiceVlanOuiAddress_Type=MacAddress
_H3cVoiceVlanOuiAddress_Object=MibTableColumn
h3cVoiceVlanOuiAddress=_H3cVoiceVlanOuiAddress_Object((1,3,6,1,4,1,43,45,1,10,2,9,1,1,1),_H3cVoiceVlanOuiAddress_Type())
h3cVoiceVlanOuiAddress.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cVoiceVlanOuiAddress.setStatus(_A)
_H3cVoiceVlanOuiMask_Type=MacAddress
_H3cVoiceVlanOuiMask_Object=MibTableColumn
h3cVoiceVlanOuiMask=_H3cVoiceVlanOuiMask_Object((1,3,6,1,4,1,43,45,1,10,2,9,1,1,2),_H3cVoiceVlanOuiMask_Type())
h3cVoiceVlanOuiMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanOuiMask.setStatus(_A)
class _H3cVoiceVlanOuiDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_H3cVoiceVlanOuiDescription_Type.__name__=_E
_H3cVoiceVlanOuiDescription_Object=MibTableColumn
h3cVoiceVlanOuiDescription=_H3cVoiceVlanOuiDescription_Object((1,3,6,1,4,1,43,45,1,10,2,9,1,1,3),_H3cVoiceVlanOuiDescription_Type())
h3cVoiceVlanOuiDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanOuiDescription.setStatus(_A)
_H3cVoiceVlanOuiRowStatus_Type=RowStatus
_H3cVoiceVlanOuiRowStatus_Object=MibTableColumn
h3cVoiceVlanOuiRowStatus=_H3cVoiceVlanOuiRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,9,1,1,4),_H3cVoiceVlanOuiRowStatus_Type())
h3cVoiceVlanOuiRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:h3cVoiceVlanOuiRowStatus.setStatus(_A)
_H3cVoiceVlanEnabledId_Type=Integer32
_H3cVoiceVlanEnabledId_Object=MibScalar
h3cVoiceVlanEnabledId=_H3cVoiceVlanEnabledId_Object((1,3,6,1,4,1,43,45,1,10,2,9,2),_H3cVoiceVlanEnabledId_Type())
h3cVoiceVlanEnabledId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanEnabledId.setStatus(_A)
_H3cVoiceVlanPortEnableList_Type=PortList
_H3cVoiceVlanPortEnableList_Object=MibScalar
h3cVoiceVlanPortEnableList=_H3cVoiceVlanPortEnableList_Object((1,3,6,1,4,1,43,45,1,10,2,9,3),_H3cVoiceVlanPortEnableList_Type())
h3cVoiceVlanPortEnableList.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanPortEnableList.setStatus(_A)
class _H3cVoiceVlanAgingTime_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,43200))
_H3cVoiceVlanAgingTime_Type.__name__=_C
_H3cVoiceVlanAgingTime_Object=MibScalar
h3cVoiceVlanAgingTime=_H3cVoiceVlanAgingTime_Object((1,3,6,1,4,1,43,45,1,10,2,9,4),_H3cVoiceVlanAgingTime_Type())
h3cVoiceVlanAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanAgingTime.setStatus(_A)
class _H3cVoiceVlanConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_G,2)))
_H3cVoiceVlanConfigState_Type.__name__=_C
_H3cVoiceVlanConfigState_Object=MibScalar
h3cVoiceVlanConfigState=_H3cVoiceVlanConfigState_Object((1,3,6,1,4,1,43,45,1,10,2,9,5),_H3cVoiceVlanConfigState_Type())
h3cVoiceVlanConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanConfigState.setStatus(_A)
class _H3cVoiceVlanSecurityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('security',1),('normal',2)))
_H3cVoiceVlanSecurityState_Type.__name__=_C
_H3cVoiceVlanSecurityState_Object=MibScalar
h3cVoiceVlanSecurityState=_H3cVoiceVlanSecurityState_Object((1,3,6,1,4,1,43,45,1,10,2,9,6),_H3cVoiceVlanSecurityState_Type())
h3cVoiceVlanSecurityState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanSecurityState.setStatus(_A)
_H3cvoiceVlanPortTable_Object=MibTable
h3cvoiceVlanPortTable=_H3cvoiceVlanPortTable_Object((1,3,6,1,4,1,43,45,1,10,2,9,7))
if mibBuilder.loadTexts:h3cvoiceVlanPortTable.setStatus(_A)
_H3cvoiceVlanPortEntry_Object=MibTableRow
h3cvoiceVlanPortEntry=_H3cvoiceVlanPortEntry_Object((1,3,6,1,4,1,43,45,1,10,2,9,7,1))
h3cvoiceVlanPortEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:h3cvoiceVlanPortEntry.setStatus(_A)
class _H3cVoiceVlanPortifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoiceVlanPortifIndex_Type.__name__=_C
_H3cVoiceVlanPortifIndex_Object=MibTableColumn
h3cVoiceVlanPortifIndex=_H3cVoiceVlanPortifIndex_Object((1,3,6,1,4,1,43,45,1,10,2,9,7,1,1),_H3cVoiceVlanPortifIndex_Type())
h3cVoiceVlanPortifIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cVoiceVlanPortifIndex.setStatus(_A)
class _H3cVoiceVlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_G,2)))
_H3cVoiceVlanPortMode_Type.__name__=_C
_H3cVoiceVlanPortMode_Object=MibTableColumn
h3cVoiceVlanPortMode=_H3cVoiceVlanPortMode_Object((1,3,6,1,4,1,43,45,1,10,2,9,7,1,2),_H3cVoiceVlanPortMode_Type())
h3cVoiceVlanPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanPortMode.setStatus(_A)
_H3cVoiceVlanPortLegacy_Type=TruthValue
_H3cVoiceVlanPortLegacy_Object=MibTableColumn
h3cVoiceVlanPortLegacy=_H3cVoiceVlanPortLegacy_Object((1,3,6,1,4,1,43,45,1,10,2,9,7,1,3),_H3cVoiceVlanPortLegacy_Type())
h3cVoiceVlanPortLegacy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanPortLegacy.setStatus(_A)
_H3cVoiceVlanPortQosTrust_Type=TruthValue
_H3cVoiceVlanPortQosTrust_Object=MibTableColumn
h3cVoiceVlanPortQosTrust=_H3cVoiceVlanPortQosTrust_Object((1,3,6,1,4,1,43,45,1,10,2,9,7,1,4),_H3cVoiceVlanPortQosTrust_Type())
h3cVoiceVlanPortQosTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoiceVlanPortQosTrust.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PortList':PortList,'h3cVoiceVlan':h3cVoiceVlan,'h3cvoiceVlanOuiTable':h3cvoiceVlanOuiTable,'h3cvoiceVlanOuiEntry':h3cvoiceVlanOuiEntry,_F:h3cVoiceVlanOuiAddress,'h3cVoiceVlanOuiMask':h3cVoiceVlanOuiMask,'h3cVoiceVlanOuiDescription':h3cVoiceVlanOuiDescription,'h3cVoiceVlanOuiRowStatus':h3cVoiceVlanOuiRowStatus,'h3cVoiceVlanEnabledId':h3cVoiceVlanEnabledId,'h3cVoiceVlanPortEnableList':h3cVoiceVlanPortEnableList,'h3cVoiceVlanAgingTime':h3cVoiceVlanAgingTime,'h3cVoiceVlanConfigState':h3cVoiceVlanConfigState,'h3cVoiceVlanSecurityState':h3cVoiceVlanSecurityState,'h3cvoiceVlanPortTable':h3cvoiceVlanPortTable,'h3cvoiceVlanPortEntry':h3cvoiceVlanPortEntry,_H:h3cVoiceVlanPortifIndex,'h3cVoiceVlanPortMode':h3cVoiceVlanPortMode,'h3cVoiceVlanPortLegacy':h3cVoiceVlanPortLegacy,'h3cVoiceVlanPortQosTrust':h3cVoiceVlanPortQosTrust})