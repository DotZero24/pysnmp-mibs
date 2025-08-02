_H='hpnicfVoiceVlanPortifIndex'
_G='manual'
_F='hpnicfVoiceVlanOuiAddress'
_E='OctetString'
_D='HPN-ICF-VOICE-VLAN-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfVoiceVlan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,9))
if mibBuilder.loadTexts:hpnicfVoiceVlan.setRevisions(('2009-05-15 00:00','2002-07-01 00:00'))
class PortList(TextualConvention,OctetString):status=_A
_HpnicfvoiceVlanOuiTable_Object=MibTable
hpnicfvoiceVlanOuiTable=_HpnicfvoiceVlanOuiTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,1))
if mibBuilder.loadTexts:hpnicfvoiceVlanOuiTable.setStatus(_A)
_HpnicfvoiceVlanOuiEntry_Object=MibTableRow
hpnicfvoiceVlanOuiEntry=_HpnicfvoiceVlanOuiEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,1,1))
hpnicfvoiceVlanOuiEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfvoiceVlanOuiEntry.setStatus(_A)
_HpnicfVoiceVlanOuiAddress_Type=MacAddress
_HpnicfVoiceVlanOuiAddress_Object=MibTableColumn
hpnicfVoiceVlanOuiAddress=_HpnicfVoiceVlanOuiAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,1,1,1),_HpnicfVoiceVlanOuiAddress_Type())
hpnicfVoiceVlanOuiAddress.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfVoiceVlanOuiAddress.setStatus(_A)
_HpnicfVoiceVlanOuiMask_Type=MacAddress
_HpnicfVoiceVlanOuiMask_Object=MibTableColumn
hpnicfVoiceVlanOuiMask=_HpnicfVoiceVlanOuiMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,1,1,2),_HpnicfVoiceVlanOuiMask_Type())
hpnicfVoiceVlanOuiMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanOuiMask.setStatus(_A)
class _HpnicfVoiceVlanOuiDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_HpnicfVoiceVlanOuiDescription_Type.__name__=_E
_HpnicfVoiceVlanOuiDescription_Object=MibTableColumn
hpnicfVoiceVlanOuiDescription=_HpnicfVoiceVlanOuiDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,1,1,3),_HpnicfVoiceVlanOuiDescription_Type())
hpnicfVoiceVlanOuiDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanOuiDescription.setStatus(_A)
_HpnicfVoiceVlanOuiRowStatus_Type=RowStatus
_HpnicfVoiceVlanOuiRowStatus_Object=MibTableColumn
hpnicfVoiceVlanOuiRowStatus=_HpnicfVoiceVlanOuiRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,1,1,4),_HpnicfVoiceVlanOuiRowStatus_Type())
hpnicfVoiceVlanOuiRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfVoiceVlanOuiRowStatus.setStatus(_A)
_HpnicfVoiceVlanEnabledId_Type=Integer32
_HpnicfVoiceVlanEnabledId_Object=MibScalar
hpnicfVoiceVlanEnabledId=_HpnicfVoiceVlanEnabledId_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,2),_HpnicfVoiceVlanEnabledId_Type())
hpnicfVoiceVlanEnabledId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanEnabledId.setStatus(_A)
_HpnicfVoiceVlanPortEnableList_Type=PortList
_HpnicfVoiceVlanPortEnableList_Object=MibScalar
hpnicfVoiceVlanPortEnableList=_HpnicfVoiceVlanPortEnableList_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,3),_HpnicfVoiceVlanPortEnableList_Type())
hpnicfVoiceVlanPortEnableList.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanPortEnableList.setStatus(_A)
class _HpnicfVoiceVlanAgingTime_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,43200))
_HpnicfVoiceVlanAgingTime_Type.__name__=_C
_HpnicfVoiceVlanAgingTime_Object=MibScalar
hpnicfVoiceVlanAgingTime=_HpnicfVoiceVlanAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,4),_HpnicfVoiceVlanAgingTime_Type())
hpnicfVoiceVlanAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanAgingTime.setStatus(_A)
class _HpnicfVoiceVlanConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_G,2)))
_HpnicfVoiceVlanConfigState_Type.__name__=_C
_HpnicfVoiceVlanConfigState_Object=MibScalar
hpnicfVoiceVlanConfigState=_HpnicfVoiceVlanConfigState_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,5),_HpnicfVoiceVlanConfigState_Type())
hpnicfVoiceVlanConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanConfigState.setStatus(_A)
class _HpnicfVoiceVlanSecurityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('security',1),('normal',2)))
_HpnicfVoiceVlanSecurityState_Type.__name__=_C
_HpnicfVoiceVlanSecurityState_Object=MibScalar
hpnicfVoiceVlanSecurityState=_HpnicfVoiceVlanSecurityState_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,6),_HpnicfVoiceVlanSecurityState_Type())
hpnicfVoiceVlanSecurityState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanSecurityState.setStatus(_A)
_HpnicfvoiceVlanPortTable_Object=MibTable
hpnicfvoiceVlanPortTable=_HpnicfvoiceVlanPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,7))
if mibBuilder.loadTexts:hpnicfvoiceVlanPortTable.setStatus(_A)
_HpnicfvoiceVlanPortEntry_Object=MibTableRow
hpnicfvoiceVlanPortEntry=_HpnicfvoiceVlanPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,7,1))
hpnicfvoiceVlanPortEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hpnicfvoiceVlanPortEntry.setStatus(_A)
class _HpnicfVoiceVlanPortifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfVoiceVlanPortifIndex_Type.__name__=_C
_HpnicfVoiceVlanPortifIndex_Object=MibTableColumn
hpnicfVoiceVlanPortifIndex=_HpnicfVoiceVlanPortifIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,7,1,1),_HpnicfVoiceVlanPortifIndex_Type())
hpnicfVoiceVlanPortifIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfVoiceVlanPortifIndex.setStatus(_A)
class _HpnicfVoiceVlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_G,2)))
_HpnicfVoiceVlanPortMode_Type.__name__=_C
_HpnicfVoiceVlanPortMode_Object=MibTableColumn
hpnicfVoiceVlanPortMode=_HpnicfVoiceVlanPortMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,7,1,2),_HpnicfVoiceVlanPortMode_Type())
hpnicfVoiceVlanPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanPortMode.setStatus(_A)
_HpnicfVoiceVlanPortLegacy_Type=TruthValue
_HpnicfVoiceVlanPortLegacy_Object=MibTableColumn
hpnicfVoiceVlanPortLegacy=_HpnicfVoiceVlanPortLegacy_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,7,1,3),_HpnicfVoiceVlanPortLegacy_Type())
hpnicfVoiceVlanPortLegacy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanPortLegacy.setStatus(_A)
_HpnicfVoiceVlanPortQosTrust_Type=TruthValue
_HpnicfVoiceVlanPortQosTrust_Object=MibTableColumn
hpnicfVoiceVlanPortQosTrust=_HpnicfVoiceVlanPortQosTrust_Object((1,3,6,1,4,1,11,2,14,11,15,2,9,7,1,4),_HpnicfVoiceVlanPortQosTrust_Type())
hpnicfVoiceVlanPortQosTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVoiceVlanPortQosTrust.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PortList':PortList,'hpnicfVoiceVlan':hpnicfVoiceVlan,'hpnicfvoiceVlanOuiTable':hpnicfvoiceVlanOuiTable,'hpnicfvoiceVlanOuiEntry':hpnicfvoiceVlanOuiEntry,_F:hpnicfVoiceVlanOuiAddress,'hpnicfVoiceVlanOuiMask':hpnicfVoiceVlanOuiMask,'hpnicfVoiceVlanOuiDescription':hpnicfVoiceVlanOuiDescription,'hpnicfVoiceVlanOuiRowStatus':hpnicfVoiceVlanOuiRowStatus,'hpnicfVoiceVlanEnabledId':hpnicfVoiceVlanEnabledId,'hpnicfVoiceVlanPortEnableList':hpnicfVoiceVlanPortEnableList,'hpnicfVoiceVlanAgingTime':hpnicfVoiceVlanAgingTime,'hpnicfVoiceVlanConfigState':hpnicfVoiceVlanConfigState,'hpnicfVoiceVlanSecurityState':hpnicfVoiceVlanSecurityState,'hpnicfvoiceVlanPortTable':hpnicfvoiceVlanPortTable,'hpnicfvoiceVlanPortEntry':hpnicfvoiceVlanPortEntry,_H:hpnicfVoiceVlanPortifIndex,'hpnicfVoiceVlanPortMode':hpnicfVoiceVlanPortMode,'hpnicfVoiceVlanPortLegacy':hpnicfVoiceVlanPortLegacy,'hpnicfVoiceVlanPortQosTrust':hpnicfVoiceVlanPortQosTrust})