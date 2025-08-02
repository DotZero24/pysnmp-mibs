_AB='apNotificationDot11ReasonCode'
_AA='apNotificationDot11RequestType'
_A9='apWMMApParamIndex'
_A8='apWMMBssParamIndex'
_A7='apEventLogIndex'
_A6='apSyslogServerIndex'
_A5='rogueApIndex'
_A4='apWStationSessionStationAddres'
_A3='apWStationSessionIfIndex'
_A2='apv8021xIndex'
_A1='ap8021xSuppIndex'
_A0='apAuthenticationServerIndex'
_z='apNativeVlanSsidNumber'
_y='apNativeVlanIfIndex'
_x='apvFilterControlIndex'
_w='enterpriseApFilterProtocolIndex'
_v='enterpriseApRadioAvChannelIndex'
_u='enterpriseApRadioAvAntennaIndex'
_t='enterpriseApRadioWEPKeysIndex'
_s='wdsPeerIndex'
_r='enterpriseApVapRadioIndex'
_q='fiftyFourMbps'
_p='thirtySixMbps'
_o='twentyFourMbps'
_n='eighteenMbps'
_m='twelveMbps'
_l='elevenMbps'
_k='nineMbps'
_j='sixMbps'
_i='fiveAndHalfMbps'
_h='twoMbps'
_g='oneMbps'
_f='alphanumeric'
_e='apRadioSecurityIndex'
_d='apSnmpTrapDestinationIndex'
_c='linkQualityStaIndex'
_b='linkQualityRadioIndex'
_a='apvMacFilterIndex'
_Z='denied'
_Y='macFilterIndex'
_X='OctetString'
_W='qosMACTypeIndex'
_V='read-create'
_U='create'
_T='valid'
_S='other'
_R='apNotificationDot11IpAddress'
_Q='required'
_P='supported'
_O='ifIndex'
_N='IF-MIB'
_M='enterpriseApRadioIndex'
_L='invalid'
_K='deprecated'
_J='apNotificationDot11Station'
_I='not-accessible'
_H='DisplayString'
_G='read-only'
_F='CTRON-AP3000-MIB'
_E='enabled'
_D='disabled'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_N,_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
ctronAP3000=ModuleIdentity((1,3,6,1,4,1,52,4,13))
if mibBuilder.loadTexts:ctronAP3000.setRevisions(('2007-10-30 18:45',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class DisplayString(OctetString):0
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,52,4))
_ComPortMgnt_ObjectIdentity=ObjectIdentity
comPortMgnt=_ComPortMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,1))
class _ComPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ComPortControl_Type.__name__=_B
_ComPortControl_Object=MibScalar
comPortControl=_ComPortControl_Object((1,3,6,1,4,1,52,4,13,1,1),_ComPortControl_Type())
comPortControl.setMaxAccess(_C)
if mibBuilder.loadTexts:comPortControl.setStatus(_A)
_MacFilterMgnt_ObjectIdentity=ObjectIdentity
macFilterMgnt=_MacFilterMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,2))
_MacFilterTable_Object=MibTable
macFilterTable=_MacFilterTable_Object((1,3,6,1,4,1,52,4,13,2,1))
if mibBuilder.loadTexts:macFilterTable.setStatus(_K)
_MacFilterEntry_Object=MibTableRow
macFilterEntry=_MacFilterEntry_Object((1,3,6,1,4,1,52,4,13,2,1,1))
macFilterEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:macFilterEntry.setStatus(_K)
class _MacFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MacFilterIndex_Type.__name__=_B
_MacFilterIndex_Object=MibTableColumn
macFilterIndex=_MacFilterIndex_Object((1,3,6,1,4,1,52,4,13,2,1,1,1),_MacFilterIndex_Type())
macFilterIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:macFilterIndex.setStatus(_K)
_MacFilterAddress_Type=MacAddress
_MacFilterAddress_Object=MibTableColumn
macFilterAddress=_MacFilterAddress_Object((1,3,6,1,4,1,52,4,13,2,1,1,2),_MacFilterAddress_Type())
macFilterAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:macFilterAddress.setStatus(_K)
class _MacFilterAllowedToGo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_MacFilterAllowedToGo_Type.__name__=_B
_MacFilterAllowedToGo_Object=MibTableColumn
macFilterAllowedToGo=_MacFilterAllowedToGo_Object((1,3,6,1,4,1,52,4,13,2,1,1,3),_MacFilterAllowedToGo_Type())
macFilterAllowedToGo.setMaxAccess(_C)
if mibBuilder.loadTexts:macFilterAllowedToGo.setStatus(_K)
class _MacFilterOpeStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),(_T,1),(_L,2),(_U,3)))
_MacFilterOpeStatus_Type.__name__=_B
_MacFilterOpeStatus_Object=MibTableColumn
macFilterOpeStatus=_MacFilterOpeStatus_Object((1,3,6,1,4,1,52,4,13,2,1,1,4),_MacFilterOpeStatus_Type())
macFilterOpeStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:macFilterOpeStatus.setStatus(_K)
class _ApMacFilterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApMacFilterControl_Type.__name__=_B
_ApMacFilterControl_Object=MibScalar
apMacFilterControl=_ApMacFilterControl_Object((1,3,6,1,4,1,52,4,13,2,2),_ApMacFilterControl_Type())
apMacFilterControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apMacFilterControl.setStatus(_K)
_ApvMacFilterOperateTable_Object=MibTable
apvMacFilterOperateTable=_ApvMacFilterOperateTable_Object((1,3,6,1,4,1,52,4,13,2,3))
if mibBuilder.loadTexts:apvMacFilterOperateTable.setStatus(_A)
_ApvMacFilterOperateEntry_Object=MibTableRow
apvMacFilterOperateEntry=_ApvMacFilterOperateEntry_Object((1,3,6,1,4,1,52,4,13,2,3,1))
apvMacFilterOperateEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:apvMacFilterOperateEntry.setStatus(_A)
class _ApvMacFilterPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allowed',1),(_Z,2)))
_ApvMacFilterPermission_Type.__name__=_B
_ApvMacFilterPermission_Object=MibTableColumn
apvMacFilterPermission=_ApvMacFilterPermission_Object((1,3,6,1,4,1,52,4,13,2,3,1,1),_ApvMacFilterPermission_Type())
apvMacFilterPermission.setMaxAccess(_C)
if mibBuilder.loadTexts:apvMacFilterPermission.setStatus(_A)
_ApvMacFilterAddressToAdd_Type=OctetString
_ApvMacFilterAddressToAdd_Object=MibTableColumn
apvMacFilterAddressToAdd=_ApvMacFilterAddressToAdd_Object((1,3,6,1,4,1,52,4,13,2,3,1,2),_ApvMacFilterAddressToAdd_Type())
apvMacFilterAddressToAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:apvMacFilterAddressToAdd.setStatus(_A)
_ApvMacFilterTable_Object=MibTable
apvMacFilterTable=_ApvMacFilterTable_Object((1,3,6,1,4,1,52,4,13,2,4))
if mibBuilder.loadTexts:apvMacFilterTable.setStatus(_A)
_ApvMacFilterEntry_Object=MibTableRow
apvMacFilterEntry=_ApvMacFilterEntry_Object((1,3,6,1,4,1,52,4,13,2,4,1))
apvMacFilterEntry.setIndexNames((0,_N,_O),(0,_F,_a))
if mibBuilder.loadTexts:apvMacFilterEntry.setStatus(_A)
class _ApvMacFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApvMacFilterIndex_Type.__name__=_B
_ApvMacFilterIndex_Object=MibTableColumn
apvMacFilterIndex=_ApvMacFilterIndex_Object((1,3,6,1,4,1,52,4,13,2,4,1,1),_ApvMacFilterIndex_Type())
apvMacFilterIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apvMacFilterIndex.setStatus(_A)
_ApvMacFilterAddress_Type=MacAddress
_ApvMacFilterAddress_Object=MibTableColumn
apvMacFilterAddress=_ApvMacFilterAddress_Object((1,3,6,1,4,1,52,4,13,2,4,1,2),_ApvMacFilterAddress_Type())
apvMacFilterAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:apvMacFilterAddress.setStatus(_A)
class _ApvMacFilterActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allow',1),(_Z,2),('deleteEntry',3)))
_ApvMacFilterActivity_Type.__name__=_B
_ApvMacFilterActivity_Object=MibTableColumn
apvMacFilterActivity=_ApvMacFilterActivity_Object((1,3,6,1,4,1,52,4,13,2,4,1,3),_ApvMacFilterActivity_Type())
apvMacFilterActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:apvMacFilterActivity.setStatus(_A)
_QosMgnt_ObjectIdentity=ObjectIdentity
qosMgnt=_QosMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,3))
class _QosModeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('qosoff',1),('qossa',2),('qosda',3),('qosether',4),('qos8021p',5)))
_QosModeControl_Type.__name__=_B
_QosModeControl_Object=MibScalar
qosModeControl=_QosModeControl_Object((1,3,6,1,4,1,52,4,13,3,1),_QosModeControl_Type())
qosModeControl.setMaxAccess(_C)
if mibBuilder.loadTexts:qosModeControl.setStatus(_A)
_QosMACTypeTable_Object=MibTable
qosMACTypeTable=_QosMACTypeTable_Object((1,3,6,1,4,1,52,4,13,3,2))
if mibBuilder.loadTexts:qosMACTypeTable.setStatus(_A)
_QosMACTypeEntry_Object=MibTableRow
qosMACTypeEntry=_QosMACTypeEntry_Object((1,3,6,1,4,1,52,4,13,3,2,1))
qosMACTypeEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:qosMACTypeEntry.setStatus(_A)
class _QosMACTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QosMACTypeIndex_Type.__name__=_B
_QosMACTypeIndex_Object=MibTableColumn
qosMACTypeIndex=_QosMACTypeIndex_Object((1,3,6,1,4,1,52,4,13,3,2,1,1),_QosMACTypeIndex_Type())
qosMACTypeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qosMACTypeIndex.setStatus(_A)
_QosMACTypeAddress_Type=MacAddress
_QosMACTypeAddress_Object=MibTableColumn
qosMACTypeAddress=_QosMACTypeAddress_Object((1,3,6,1,4,1,52,4,13,3,2,1,2),_QosMACTypeAddress_Type())
qosMACTypeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMACTypeAddress.setStatus(_A)
class _QosMACTypePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosMACTypePriority_Type.__name__=_B
_QosMACTypePriority_Object=MibTableColumn
qosMACTypePriority=_QosMACTypePriority_Object((1,3,6,1,4,1,52,4,13,3,2,1,3),_QosMACTypePriority_Type())
qosMACTypePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMACTypePriority.setStatus(_A)
class _QosMACTypeOpeStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),(_T,1),(_L,2),(_U,3)))
_QosMACTypeOpeStatus_Type.__name__=_B
_QosMACTypeOpeStatus_Object=MibTableColumn
qosMACTypeOpeStatus=_QosMACTypeOpeStatus_Object((1,3,6,1,4,1,52,4,13,3,2,1,4),_QosMACTypeOpeStatus_Type())
qosMACTypeOpeStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:qosMACTypeOpeStatus.setStatus(_A)
_QosEtherTypeTable_Object=MibTable
qosEtherTypeTable=_QosEtherTypeTable_Object((1,3,6,1,4,1,52,4,13,3,3))
if mibBuilder.loadTexts:qosEtherTypeTable.setStatus(_A)
_QosEtherTypeEntry_Object=MibTableRow
qosEtherTypeEntry=_QosEtherTypeEntry_Object((1,3,6,1,4,1,52,4,13,3,3,1))
qosEtherTypeEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:qosEtherTypeEntry.setStatus(_A)
_QosEtherTypeIndex_Type=Integer32
_QosEtherTypeIndex_Object=MibTableColumn
qosEtherTypeIndex=_QosEtherTypeIndex_Object((1,3,6,1,4,1,52,4,13,3,3,1,1),_QosEtherTypeIndex_Type())
qosEtherTypeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:qosEtherTypeIndex.setStatus(_A)
class _QosEtherTypeHexValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_QosEtherTypeHexValue_Type.__name__=_X
_QosEtherTypeHexValue_Object=MibTableColumn
qosEtherTypeHexValue=_QosEtherTypeHexValue_Object((1,3,6,1,4,1,52,4,13,3,3,1,2),_QosEtherTypeHexValue_Type())
qosEtherTypeHexValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qosEtherTypeHexValue.setStatus(_A)
class _QosEtherTypePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosEtherTypePriority_Type.__name__=_B
_QosEtherTypePriority_Object=MibTableColumn
qosEtherTypePriority=_QosEtherTypePriority_Object((1,3,6,1,4,1,52,4,13,3,3,1,3),_QosEtherTypePriority_Type())
qosEtherTypePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosEtherTypePriority.setStatus(_A)
class _QosEtherTypeOpeStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_S,0),(_T,1),(_L,2),(_U,3)))
_QosEtherTypeOpeStatus_Type.__name__=_B
_QosEtherTypeOpeStatus_Object=MibTableColumn
qosEtherTypeOpeStatus=_QosEtherTypeOpeStatus_Object((1,3,6,1,4,1,52,4,13,3,3,1,4),_QosEtherTypeOpeStatus_Type())
qosEtherTypeOpeStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:qosEtherTypeOpeStatus.setStatus(_A)
class _QosQueueingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('weighted-fair',1),('strict-priority',2)))
_QosQueueingMode_Type.__name__=_B
_QosQueueingMode_Object=MibScalar
qosQueueingMode=_QosQueueingMode_Object((1,3,6,1,4,1,52,4,13,3,4),_QosQueueingMode_Type())
qosQueueingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qosQueueingMode.setStatus(_A)
class _QosSVPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_QosSVPStatus_Type.__name__=_B
_QosSVPStatus_Object=MibScalar
qosSVPStatus=_QosSVPStatus_Object((1,3,6,1,4,1,52,4,13,3,5),_QosSVPStatus_Type())
qosSVPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosSVPStatus.setStatus(_A)
_LinkQualityMgnt_ObjectIdentity=ObjectIdentity
linkQualityMgnt=_LinkQualityMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,4))
_LinkQualityTable_Object=MibTable
linkQualityTable=_LinkQualityTable_Object((1,3,6,1,4,1,52,4,13,4,1))
if mibBuilder.loadTexts:linkQualityTable.setStatus(_A)
_LinkQualityEntry_Object=MibTableRow
linkQualityEntry=_LinkQualityEntry_Object((1,3,6,1,4,1,52,4,13,4,1,1))
linkQualityEntry.setIndexNames((0,_F,_b),(0,_F,_c))
if mibBuilder.loadTexts:linkQualityEntry.setStatus(_A)
class _LinkQualityRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LinkQualityRadioIndex_Type.__name__=_B
_LinkQualityRadioIndex_Object=MibTableColumn
linkQualityRadioIndex=_LinkQualityRadioIndex_Object((1,3,6,1,4,1,52,4,13,4,1,1,1),_LinkQualityRadioIndex_Type())
linkQualityRadioIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:linkQualityRadioIndex.setStatus(_A)
class _LinkQualityStaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LinkQualityStaIndex_Type.__name__=_B
_LinkQualityStaIndex_Object=MibTableColumn
linkQualityStaIndex=_LinkQualityStaIndex_Object((1,3,6,1,4,1,52,4,13,4,1,1,2),_LinkQualityStaIndex_Type())
linkQualityStaIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:linkQualityStaIndex.setStatus(_A)
_LinkQualityStaMacAddress_Type=MacAddress
_LinkQualityStaMacAddress_Object=MibTableColumn
linkQualityStaMacAddress=_LinkQualityStaMacAddress_Object((1,3,6,1,4,1,52,4,13,4,1,1,3),_LinkQualityStaMacAddress_Type())
linkQualityStaMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:linkQualityStaMacAddress.setStatus(_A)
class _LinkQualityStaRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LinkQualityStaRssi_Type.__name__=_B
_LinkQualityStaRssi_Object=MibTableColumn
linkQualityStaRssi=_LinkQualityStaRssi_Object((1,3,6,1,4,1,52,4,13,4,1,1,4),_LinkQualityStaRssi_Type())
linkQualityStaRssi.setMaxAccess(_G)
if mibBuilder.loadTexts:linkQualityStaRssi.setStatus(_A)
_ApSnmpMgnt_ObjectIdentity=ObjectIdentity
apSnmpMgnt=_ApSnmpMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,5))
class _TrapControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapControl_Type.__name__=_B
_TrapControl_Object=MibScalar
trapControl=_TrapControl_Object((1,3,6,1,4,1,52,4,13,5,1),_TrapControl_Type())
trapControl.setMaxAccess(_C)
if mibBuilder.loadTexts:trapControl.setStatus(_A)
_TrapConfiguration_ObjectIdentity=ObjectIdentity
trapConfiguration=_TrapConfiguration_ObjectIdentity((1,3,6,1,4,1,52,4,13,5,2))
class _TrapSysSystemUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapSysSystemUp_Type.__name__=_B
_TrapSysSystemUp_Object=MibScalar
trapSysSystemUp=_TrapSysSystemUp_Object((1,3,6,1,4,1,52,4,13,5,2,1),_TrapSysSystemUp_Type())
trapSysSystemUp.setMaxAccess(_C)
if mibBuilder.loadTexts:trapSysSystemUp.setStatus(_A)
class _TrapSysSystemDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapSysSystemDown_Type.__name__=_B
_TrapSysSystemDown_Object=MibScalar
trapSysSystemDown=_TrapSysSystemDown_Object((1,3,6,1,4,1,52,4,13,5,2,2),_TrapSysSystemDown_Type())
trapSysSystemDown.setMaxAccess(_C)
if mibBuilder.loadTexts:trapSysSystemDown.setStatus(_A)
class _TrapSysRadiusServerChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapSysRadiusServerChanged_Type.__name__=_B
_TrapSysRadiusServerChanged_Object=MibScalar
trapSysRadiusServerChanged=_TrapSysRadiusServerChanged_Object((1,3,6,1,4,1,52,4,13,5,2,3),_TrapSysRadiusServerChanged_Type())
trapSysRadiusServerChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:trapSysRadiusServerChanged.setStatus(_A)
class _TrapDot11StationAssociation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot11StationAssociation_Type.__name__=_B
_TrapDot11StationAssociation_Object=MibScalar
trapDot11StationAssociation=_TrapDot11StationAssociation_Object((1,3,6,1,4,1,52,4,13,5,2,4),_TrapDot11StationAssociation_Type())
trapDot11StationAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot11StationAssociation.setStatus(_A)
class _TrapDot11StationReAssociation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot11StationReAssociation_Type.__name__=_B
_TrapDot11StationReAssociation_Object=MibScalar
trapDot11StationReAssociation=_TrapDot11StationReAssociation_Object((1,3,6,1,4,1,52,4,13,5,2,5),_TrapDot11StationReAssociation_Type())
trapDot11StationReAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot11StationReAssociation.setStatus(_A)
class _TrapDot11StationAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot11StationAuthentication_Type.__name__=_B
_TrapDot11StationAuthentication_Object=MibScalar
trapDot11StationAuthentication=_TrapDot11StationAuthentication_Object((1,3,6,1,4,1,52,4,13,5,2,6),_TrapDot11StationAuthentication_Type())
trapDot11StationAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot11StationAuthentication.setStatus(_A)
class _TrapDot11StationRequestFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot11StationRequestFail_Type.__name__=_B
_TrapDot11StationRequestFail_Object=MibScalar
trapDot11StationRequestFail=_TrapDot11StationRequestFail_Object((1,3,6,1,4,1,52,4,13,5,2,7),_TrapDot11StationRequestFail_Type())
trapDot11StationRequestFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot11StationRequestFail.setStatus(_A)
class _TrapLocalMacAddrAuthFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapLocalMacAddrAuthFail_Type.__name__=_B
_TrapLocalMacAddrAuthFail_Object=MibScalar
trapLocalMacAddrAuthFail=_TrapLocalMacAddrAuthFail_Object((1,3,6,1,4,1,52,4,13,5,2,9),_TrapLocalMacAddrAuthFail_Type())
trapLocalMacAddrAuthFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapLocalMacAddrAuthFail.setStatus(_A)
class _TrapLocalMacAddrAuthSuccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapLocalMacAddrAuthSuccess_Type.__name__=_B
_TrapLocalMacAddrAuthSuccess_Object=MibScalar
trapLocalMacAddrAuthSuccess=_TrapLocalMacAddrAuthSuccess_Object((1,3,6,1,4,1,52,4,13,5,2,10),_TrapLocalMacAddrAuthSuccess_Type())
trapLocalMacAddrAuthSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:trapLocalMacAddrAuthSuccess.setStatus(_A)
class _TrapDot1xAuthNotInitiated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot1xAuthNotInitiated_Type.__name__=_B
_TrapDot1xAuthNotInitiated_Object=MibScalar
trapDot1xAuthNotInitiated=_TrapDot1xAuthNotInitiated_Object((1,3,6,1,4,1,52,4,13,5,2,11),_TrapDot1xAuthNotInitiated_Type())
trapDot1xAuthNotInitiated.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot1xAuthNotInitiated.setStatus(_A)
class _TrapDot1xAuthSuccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot1xAuthSuccess_Type.__name__=_B
_TrapDot1xAuthSuccess_Object=MibScalar
trapDot1xAuthSuccess=_TrapDot1xAuthSuccess_Object((1,3,6,1,4,1,52,4,13,5,2,12),_TrapDot1xAuthSuccess_Type())
trapDot1xAuthSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot1xAuthSuccess.setStatus(_A)
class _TrapDot1xAuthFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot1xAuthFail_Type.__name__=_B
_TrapDot1xAuthFail_Object=MibScalar
trapDot1xAuthFail=_TrapDot1xAuthFail_Object((1,3,6,1,4,1,52,4,13,5,2,13),_TrapDot1xAuthFail_Type())
trapDot1xAuthFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot1xAuthFail.setStatus(_A)
class _TrapDot1xMacAddrAuthSuccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot1xMacAddrAuthSuccess_Type.__name__=_B
_TrapDot1xMacAddrAuthSuccess_Object=MibScalar
trapDot1xMacAddrAuthSuccess=_TrapDot1xMacAddrAuthSuccess_Object((1,3,6,1,4,1,52,4,13,5,2,14),_TrapDot1xMacAddrAuthSuccess_Type())
trapDot1xMacAddrAuthSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot1xMacAddrAuthSuccess.setStatus(_A)
class _TrapDot1xMacAddrAuthFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot1xMacAddrAuthFail_Type.__name__=_B
_TrapDot1xMacAddrAuthFail_Object=MibScalar
trapDot1xMacAddrAuthFail=_TrapDot1xMacAddrAuthFail_Object((1,3,6,1,4,1,52,4,13,5,2,15),_TrapDot1xMacAddrAuthFail_Type())
trapDot1xMacAddrAuthFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot1xMacAddrAuthFail.setStatus(_A)
class _TrapPppLogonFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapPppLogonFail_Type.__name__=_B
_TrapPppLogonFail_Object=MibScalar
trapPppLogonFail=_TrapPppLogonFail_Object((1,3,6,1,4,1,52,4,13,5,2,16),_TrapPppLogonFail_Type())
trapPppLogonFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapPppLogonFail.setStatus(_A)
class _TrapIappStationRoamedFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapIappStationRoamedFrom_Type.__name__=_B
_TrapIappStationRoamedFrom_Object=MibScalar
trapIappStationRoamedFrom=_TrapIappStationRoamedFrom_Object((1,3,6,1,4,1,52,4,13,5,2,17),_TrapIappStationRoamedFrom_Type())
trapIappStationRoamedFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:trapIappStationRoamedFrom.setStatus(_A)
class _TrapIappStationRoamedTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapIappStationRoamedTo_Type.__name__=_B
_TrapIappStationRoamedTo_Object=MibScalar
trapIappStationRoamedTo=_TrapIappStationRoamedTo_Object((1,3,6,1,4,1,52,4,13,5,2,18),_TrapIappStationRoamedTo_Type())
trapIappStationRoamedTo.setMaxAccess(_C)
if mibBuilder.loadTexts:trapIappStationRoamedTo.setStatus(_A)
class _TrapIappContextDataSent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapIappContextDataSent_Type.__name__=_B
_TrapIappContextDataSent_Object=MibScalar
trapIappContextDataSent=_TrapIappContextDataSent_Object((1,3,6,1,4,1,52,4,13,5,2,19),_TrapIappContextDataSent_Type())
trapIappContextDataSent.setMaxAccess(_C)
if mibBuilder.loadTexts:trapIappContextDataSent.setStatus(_A)
class _TrapSntpServerFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapSntpServerFail_Type.__name__=_B
_TrapSntpServerFail_Object=MibScalar
trapSntpServerFail=_TrapSntpServerFail_Object((1,3,6,1,4,1,52,4,13,5,2,20),_TrapSntpServerFail_Type())
trapSntpServerFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapSntpServerFail.setStatus(_A)
class _TrapDot11InterfaceAFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot11InterfaceAFail_Type.__name__=_B
_TrapDot11InterfaceAFail_Object=MibScalar
trapDot11InterfaceAFail=_TrapDot11InterfaceAFail_Object((1,3,6,1,4,1,52,4,13,5,2,21),_TrapDot11InterfaceAFail_Type())
trapDot11InterfaceAFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot11InterfaceAFail.setStatus(_A)
class _TrapDot11InterfaceGFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot11InterfaceGFail_Type.__name__=_B
_TrapDot11InterfaceGFail_Object=MibScalar
trapDot11InterfaceGFail=_TrapDot11InterfaceGFail_Object((1,3,6,1,4,1,52,4,13,5,2,22),_TrapDot11InterfaceGFail_Type())
trapDot11InterfaceGFail.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot11InterfaceGFail.setStatus(_A)
class _TrapDot11WirelessSTPDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_TrapDot11WirelessSTPDetection_Type.__name__=_B
_TrapDot11WirelessSTPDetection_Object=MibScalar
trapDot11WirelessSTPDetection=_TrapDot11WirelessSTPDetection_Object((1,3,6,1,4,1,52,4,13,5,2,23),_TrapDot11WirelessSTPDetection_Type())
trapDot11WirelessSTPDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:trapDot11WirelessSTPDetection.setStatus(_A)
_ApSnmpTrapDestinationTable_Object=MibTable
apSnmpTrapDestinationTable=_ApSnmpTrapDestinationTable_Object((1,3,6,1,4,1,52,4,13,5,3))
if mibBuilder.loadTexts:apSnmpTrapDestinationTable.setStatus(_A)
_ApSnmpTrapDestinationEntry_Object=MibTableRow
apSnmpTrapDestinationEntry=_ApSnmpTrapDestinationEntry_Object((1,3,6,1,4,1,52,4,13,5,3,1))
apSnmpTrapDestinationEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:apSnmpTrapDestinationEntry.setStatus(_A)
class _ApSnmpTrapDestinationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ApSnmpTrapDestinationIndex_Type.__name__=_B
_ApSnmpTrapDestinationIndex_Object=MibTableColumn
apSnmpTrapDestinationIndex=_ApSnmpTrapDestinationIndex_Object((1,3,6,1,4,1,52,4,13,5,3,1,1),_ApSnmpTrapDestinationIndex_Type())
apSnmpTrapDestinationIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apSnmpTrapDestinationIndex.setStatus(_A)
class _ApSnmpTrapDestinationCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ApSnmpTrapDestinationCommunity_Type.__name__=_H
_ApSnmpTrapDestinationCommunity_Object=MibTableColumn
apSnmpTrapDestinationCommunity=_ApSnmpTrapDestinationCommunity_Object((1,3,6,1,4,1,52,4,13,5,3,1,2),_ApSnmpTrapDestinationCommunity_Type())
apSnmpTrapDestinationCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:apSnmpTrapDestinationCommunity.setStatus(_A)
_ApSnmpTrapDestinationIP_Type=IpAddress
_ApSnmpTrapDestinationIP_Object=MibTableColumn
apSnmpTrapDestinationIP=_ApSnmpTrapDestinationIP_Object((1,3,6,1,4,1,52,4,13,5,3,1,3),_ApSnmpTrapDestinationIP_Type())
apSnmpTrapDestinationIP.setMaxAccess(_C)
if mibBuilder.loadTexts:apSnmpTrapDestinationIP.setStatus(_A)
class _ApSnmpTrapDestinationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApSnmpTrapDestinationState_Type.__name__=_B
_ApSnmpTrapDestinationState_Object=MibTableColumn
apSnmpTrapDestinationState=_ApSnmpTrapDestinationState_Object((1,3,6,1,4,1,52,4,13,5,3,1,4),_ApSnmpTrapDestinationState_Type())
apSnmpTrapDestinationState.setMaxAccess(_C)
if mibBuilder.loadTexts:apSnmpTrapDestinationState.setStatus(_A)
class _ApSnmpCommunityReadOnly_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ApSnmpCommunityReadOnly_Type.__name__=_H
_ApSnmpCommunityReadOnly_Object=MibScalar
apSnmpCommunityReadOnly=_ApSnmpCommunityReadOnly_Object((1,3,6,1,4,1,52,4,13,5,4),_ApSnmpCommunityReadOnly_Type())
apSnmpCommunityReadOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:apSnmpCommunityReadOnly.setStatus(_A)
class _ApSnmpCommunityReadWrite_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ApSnmpCommunityReadWrite_Type.__name__=_H
_ApSnmpCommunityReadWrite_Object=MibScalar
apSnmpCommunityReadWrite=_ApSnmpCommunityReadWrite_Object((1,3,6,1,4,1,52,4,13,5,5),_ApSnmpCommunityReadWrite_Type())
apSnmpCommunityReadWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:apSnmpCommunityReadWrite.setStatus(_A)
class _ApSnmpVersionFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableSNMPv1SNMPv2c',1),('disableSNMPv1SNMPv2c',2)))
_ApSnmpVersionFilter_Type.__name__=_B
_ApSnmpVersionFilter_Object=MibScalar
apSnmpVersionFilter=_ApSnmpVersionFilter_Object((1,3,6,1,4,1,52,4,13,5,6),_ApSnmpVersionFilter_Type())
apSnmpVersionFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:apSnmpVersionFilter.setStatus(_A)
_SysEntity_ObjectIdentity=ObjectIdentity
sysEntity=_SysEntity_ObjectIdentity((1,3,6,1,4,1,52,4,13,6))
class _SwHardwareVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwHardwareVer_Type.__name__=_H
_SwHardwareVer_Object=MibScalar
swHardwareVer=_SwHardwareVer_Object((1,3,6,1,4,1,52,4,13,6,1),_SwHardwareVer_Type())
swHardwareVer.setMaxAccess(_G)
if mibBuilder.loadTexts:swHardwareVer.setStatus(_A)
class _SwBootRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwBootRomVer_Type.__name__=_H
_SwBootRomVer_Object=MibScalar
swBootRomVer=_SwBootRomVer_Object((1,3,6,1,4,1,52,4,13,6,2),_SwBootRomVer_Type())
swBootRomVer.setMaxAccess(_G)
if mibBuilder.loadTexts:swBootRomVer.setStatus(_A)
class _SwOpCodeVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwOpCodeVer_Type.__name__=_H
_SwOpCodeVer_Object=MibScalar
swOpCodeVer=_SwOpCodeVer_Object((1,3,6,1,4,1,52,4,13,6,3),_SwOpCodeVer_Type())
swOpCodeVer.setMaxAccess(_G)
if mibBuilder.loadTexts:swOpCodeVer.setStatus(_A)
class _SwSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwSerialNumber_Type.__name__=_H
_SwSerialNumber_Object=MibScalar
swSerialNumber=_SwSerialNumber_Object((1,3,6,1,4,1,52,4,13,6,4),_SwSerialNumber_Type())
swSerialNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:swSerialNumber.setStatus(_A)
class _SwProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SwProductName_Type.__name__=_H
_SwProductName_Object=MibScalar
swProductName=_SwProductName_Object((1,3,6,1,4,1,52,4,13,6,5),_SwProductName_Type())
swProductName.setMaxAccess(_G)
if mibBuilder.loadTexts:swProductName.setStatus(_A)
class _SwCountrySetting_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwCountrySetting_Type.__name__=_H
_SwCountrySetting_Object=MibScalar
swCountrySetting=_SwCountrySetting_Object((1,3,6,1,4,1,52,4,13,6,6),_SwCountrySetting_Type())
swCountrySetting.setMaxAccess(_G)
if mibBuilder.loadTexts:swCountrySetting.setStatus(_A)
_ApSecurityMgnt_ObjectIdentity=ObjectIdentity
apSecurityMgnt=_ApSecurityMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,7))
_ApRadioSecurityTable_Object=MibTable
apRadioSecurityTable=_ApRadioSecurityTable_Object((1,3,6,1,4,1,52,4,13,7,1))
if mibBuilder.loadTexts:apRadioSecurityTable.setStatus(_A)
_ApRadioSecurityEntry_Object=MibTableRow
apRadioSecurityEntry=_ApRadioSecurityEntry_Object((1,3,6,1,4,1,52,4,13,7,1,1))
apRadioSecurityEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:apRadioSecurityEntry.setStatus(_A)
class _ApRadioSecurityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApRadioSecurityIndex_Type.__name__=_B
_ApRadioSecurityIndex_Object=MibTableColumn
apRadioSecurityIndex=_ApRadioSecurityIndex_Object((1,3,6,1,4,1,52,4,13,7,1,1,1),_ApRadioSecurityIndex_Type())
apRadioSecurityIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apRadioSecurityIndex.setStatus(_A)
class _ApRadioSecurityWEPAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('opensystem',0),('sharedkey',1),('wpa',2),('wpapsk',3),('wpawpa2mixed',4),('wpawpa2pskmixed',5),('wpa2',6),('wpa2psk',7)))
_ApRadioSecurityWEPAuthType_Type.__name__=_B
_ApRadioSecurityWEPAuthType_Object=MibTableColumn
apRadioSecurityWEPAuthType=_ApRadioSecurityWEPAuthType_Object((1,3,6,1,4,1,52,4,13,7,1,1,2),_ApRadioSecurityWEPAuthType_Type())
apRadioSecurityWEPAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWEPAuthType.setStatus(_A)
class _ApRadioSecuritySharedKeyLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('sixtyFour',1),('oneHundredTwentyEight',2),('oneHundredFiftyTwo',3)))
_ApRadioSecuritySharedKeyLen_Type.__name__=_B
_ApRadioSecuritySharedKeyLen_Object=MibTableColumn
apRadioSecuritySharedKeyLen=_ApRadioSecuritySharedKeyLen_Object((1,3,6,1,4,1,52,4,13,7,1,1,3),_ApRadioSecuritySharedKeyLen_Type())
apRadioSecuritySharedKeyLen.setMaxAccess(_G)
if mibBuilder.loadTexts:apRadioSecuritySharedKeyLen.setStatus(_A)
class _ApRadioSecurityWPAMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_Q,1),('notSupported',2)))
_ApRadioSecurityWPAMode_Type.__name__=_B
_ApRadioSecurityWPAMode_Object=MibTableColumn
apRadioSecurityWPAMode=_ApRadioSecurityWPAMode_Object((1,3,6,1,4,1,52,4,13,7,1,1,4),_ApRadioSecurityWPAMode_Type())
apRadioSecurityWPAMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWPAMode.setStatus(_A)
class _ApRadioSecurityWPAKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dot1x',0),('presharedkey',1)))
_ApRadioSecurityWPAKeyType_Type.__name__=_B
_ApRadioSecurityWPAKeyType_Object=MibTableColumn
apRadioSecurityWPAKeyType=_ApRadioSecurityWPAKeyType_Object((1,3,6,1,4,1,52,4,13,7,1,1,5),_ApRadioSecurityWPAKeyType_Type())
apRadioSecurityWPAKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWPAKeyType.setStatus(_A)
class _ApRadioSecurityWPACipher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('wep',0),('tkip',1),('aes',2)))
_ApRadioSecurityWPACipher_Type.__name__=_B
_ApRadioSecurityWPACipher_Object=MibTableColumn
apRadioSecurityWPACipher=_ApRadioSecurityWPACipher_Object((1,3,6,1,4,1,52,4,13,7,1,1,6),_ApRadioSecurityWPACipher_Type())
apRadioSecurityWPACipher.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWPACipher.setStatus('obsolete')
class _ApRadioSecurityWPAPSKType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hex',0),(_f,1)))
_ApRadioSecurityWPAPSKType_Type.__name__=_B
_ApRadioSecurityWPAPSKType_Object=MibTableColumn
apRadioSecurityWPAPSKType=_ApRadioSecurityWPAPSKType_Object((1,3,6,1,4,1,52,4,13,7,1,1,7),_ApRadioSecurityWPAPSKType_Type())
apRadioSecurityWPAPSKType.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWPAPSKType.setStatus(_A)
class _ApRadioSecurityWPAPSK_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ApRadioSecurityWPAPSK_Type.__name__=_H
_ApRadioSecurityWPAPSK_Object=MibTableColumn
apRadioSecurityWPAPSK=_ApRadioSecurityWPAPSK_Object((1,3,6,1,4,1,52,4,13,7,1,1,8),_ApRadioSecurityWPAPSK_Type())
apRadioSecurityWPAPSK.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWPAPSK.setStatus(_A)
class _ApRadioSecurityWEPKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hexadecimal',0),(_f,1)))
_ApRadioSecurityWEPKeyType_Type.__name__=_B
_ApRadioSecurityWEPKeyType_Object=MibTableColumn
apRadioSecurityWEPKeyType=_ApRadioSecurityWEPKeyType_Object((1,3,6,1,4,1,52,4,13,7,1,1,9),_ApRadioSecurityWEPKeyType_Type())
apRadioSecurityWEPKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWEPKeyType.setStatus(_A)
_ApRadioSecurityWEPEnabled_Type=TruthValue
_ApRadioSecurityWEPEnabled_Object=MibTableColumn
apRadioSecurityWEPEnabled=_ApRadioSecurityWEPEnabled_Object((1,3,6,1,4,1,52,4,13,7,1,1,10),_ApRadioSecurityWEPEnabled_Type())
apRadioSecurityWEPEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWEPEnabled.setStatus(_A)
class _ApRadioSecurityWPACipherSuite_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('aesccmp',0),('tkip',1),('wep',2)))
_ApRadioSecurityWPACipherSuite_Type.__name__=_B
_ApRadioSecurityWPACipherSuite_Object=MibTableColumn
apRadioSecurityWPACipherSuite=_ApRadioSecurityWPACipherSuite_Object((1,3,6,1,4,1,52,4,13,7,1,1,11),_ApRadioSecurityWPACipherSuite_Type())
apRadioSecurityWPACipherSuite.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioSecurityWPACipherSuite.setStatus(_A)
class _ApRadioApSecurityWPAPreAuthentication_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApRadioApSecurityWPAPreAuthentication_Type.__name__=_B
_ApRadioApSecurityWPAPreAuthentication_Object=MibTableColumn
apRadioApSecurityWPAPreAuthentication=_ApRadioApSecurityWPAPreAuthentication_Object((1,3,6,1,4,1,52,4,13,7,1,1,12),_ApRadioApSecurityWPAPreAuthentication_Type())
apRadioApSecurityWPAPreAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioApSecurityWPAPreAuthentication.setStatus(_A)
class _ApRadioApSecurityWPAPmksaLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14400))
_ApRadioApSecurityWPAPmksaLifetime_Type.__name__=_B
_ApRadioApSecurityWPAPmksaLifetime_Object=MibTableColumn
apRadioApSecurityWPAPmksaLifetime=_ApRadioApSecurityWPAPmksaLifetime_Object((1,3,6,1,4,1,52,4,13,7,1,1,13),_ApRadioApSecurityWPAPmksaLifetime_Type())
apRadioApSecurityWPAPmksaLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadioApSecurityWPAPmksaLifetime.setStatus(_A)
_ApSecuritySsh_ObjectIdentity=ObjectIdentity
apSecuritySsh=_ApSecuritySsh_ObjectIdentity((1,3,6,1,4,1,52,4,13,7,2))
_ApSecuritySshServerEnabled_Type=TruthValue
_ApSecuritySshServerEnabled_Object=MibScalar
apSecuritySshServerEnabled=_ApSecuritySshServerEnabled_Object((1,3,6,1,4,1,52,4,13,7,2,1),_ApSecuritySshServerEnabled_Type())
apSecuritySshServerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apSecuritySshServerEnabled.setStatus(_A)
class _ApSecuritySshServerPort_Type(Integer32):defaultValue=22
_ApSecuritySshServerPort_Type.__name__=_B
_ApSecuritySshServerPort_Object=MibScalar
apSecuritySshServerPort=_ApSecuritySshServerPort_Object((1,3,6,1,4,1,52,4,13,7,2,2),_ApSecuritySshServerPort_Type())
apSecuritySshServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apSecuritySshServerPort.setStatus(_A)
_ApSecuritySshTelnetServerEnabled_Type=TruthValue
_ApSecuritySshTelnetServerEnabled_Object=MibScalar
apSecuritySshTelnetServerEnabled=_ApSecuritySshTelnetServerEnabled_Object((1,3,6,1,4,1,52,4,13,7,2,3),_ApSecuritySshTelnetServerEnabled_Type())
apSecuritySshTelnetServerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apSecuritySshTelnetServerEnabled.setStatus(_A)
_ApRadioInterfaceMgnt_ObjectIdentity=ObjectIdentity
apRadioInterfaceMgnt=_ApRadioInterfaceMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,8))
_EnterpriseApRadioTable_Object=MibTable
enterpriseApRadioTable=_EnterpriseApRadioTable_Object((1,3,6,1,4,1,52,4,13,8,2))
if mibBuilder.loadTexts:enterpriseApRadioTable.setStatus(_A)
_EnterpriseApRadioEntry_Object=MibTableRow
enterpriseApRadioEntry=_EnterpriseApRadioEntry_Object((1,3,6,1,4,1,52,4,13,8,2,1))
enterpriseApRadioEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:enterpriseApRadioEntry.setStatus(_A)
class _EnterpriseApRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EnterpriseApRadioIndex_Type.__name__=_B
_EnterpriseApRadioIndex_Object=MibTableColumn
enterpriseApRadioIndex=_EnterpriseApRadioIndex_Object((1,3,6,1,4,1,52,4,13,8,2,1,1),_EnterpriseApRadioIndex_Type())
enterpriseApRadioIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:enterpriseApRadioIndex.setStatus(_A)
class _EnterpriseApRadioAutoChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioAutoChannel_Type.__name__=_B
_EnterpriseApRadioAutoChannel_Object=MibTableColumn
enterpriseApRadioAutoChannel=_EnterpriseApRadioAutoChannel_Object((1,3,6,1,4,1,52,4,13,8,2,1,2),_EnterpriseApRadioAutoChannel_Type())
enterpriseApRadioAutoChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioAutoChannel.setStatus(_A)
class _EnterpriseApRadioTransmitPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('full',1),('half',2),('quarter',3),('eighth',4),('min',5)))
_EnterpriseApRadioTransmitPower_Type.__name__=_B
_EnterpriseApRadioTransmitPower_Object=MibTableColumn
enterpriseApRadioTransmitPower=_EnterpriseApRadioTransmitPower_Object((1,3,6,1,4,1,52,4,13,8,2,1,3),_EnterpriseApRadioTransmitPower_Type())
enterpriseApRadioTransmitPower.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioTransmitPower.setStatus(_A)
class _EnterpriseApRadioTurboMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_D,2),(_L,3)))
_EnterpriseApRadioTurboMode_Type.__name__=_B
_EnterpriseApRadioTurboMode_Object=MibTableColumn
enterpriseApRadioTurboMode=_EnterpriseApRadioTurboMode_Object((1,3,6,1,4,1,52,4,13,8,2,1,4),_EnterpriseApRadioTurboMode_Type())
enterpriseApRadioTurboMode.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioTurboMode.setStatus(_A)
class _EnterpriseApRadioDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,9,11,12,18,24,36,48,54,255)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,5),(_j,6),(_k,9),(_l,11),(_m,12),(_n,18),(_o,24),(_p,36),('fourtyEightMbps',48),(_q,54),('auto',255)))
_EnterpriseApRadioDataRate_Type.__name__=_B
_EnterpriseApRadioDataRate_Object=MibTableColumn
enterpriseApRadioDataRate=_EnterpriseApRadioDataRate_Object((1,3,6,1,4,1,52,4,13,8,2,1,5),_EnterpriseApRadioDataRate_Type())
enterpriseApRadioDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioDataRate.setStatus(_A)
class _EnterpriseApRadioGMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bOnly',1),('gOnly',2),('bg',3),(_L,4)))
_EnterpriseApRadioGMode_Type.__name__=_B
_EnterpriseApRadioGMode_Object=MibTableColumn
enterpriseApRadioGMode=_EnterpriseApRadioGMode_Object((1,3,6,1,4,1,52,4,13,8,2,1,6),_EnterpriseApRadioGMode_Type())
enterpriseApRadioGMode.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioGMode.setStatus(_A)
class _EnterpriseApRadioAntennaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('both',1),('left',2),('right',3),(_L,4)))
_EnterpriseApRadioAntennaMode_Type.__name__=_B
_EnterpriseApRadioAntennaMode_Object=MibTableColumn
enterpriseApRadioAntennaMode=_EnterpriseApRadioAntennaMode_Object((1,3,6,1,4,1,52,4,13,8,2,1,7),_EnterpriseApRadioAntennaMode_Type())
enterpriseApRadioAntennaMode.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioAntennaMode.setStatus(_A)
class _RogueApState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_RogueApState_Type.__name__=_B
_RogueApState_Object=MibTableColumn
rogueApState=_RogueApState_Object((1,3,6,1,4,1,52,4,13,8,2,1,8),_RogueApState_Type())
rogueApState.setMaxAccess(_C)
if mibBuilder.loadTexts:rogueApState.setStatus(_A)
class _RogueApInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RogueApInterval_Type.__name__=_B
_RogueApInterval_Object=MibTableColumn
rogueApInterval=_RogueApInterval_Object((1,3,6,1,4,1,52,4,13,8,2,1,9),_RogueApInterval_Type())
rogueApInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rogueApInterval.setStatus(_A)
class _RogueApDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_RogueApDuration_Type.__name__=_B
_RogueApDuration_Object=MibTableColumn
rogueApDuration=_RogueApDuration_Object((1,3,6,1,4,1,52,4,13,8,2,1,10),_RogueApDuration_Type())
rogueApDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:rogueApDuration.setStatus(_A)
class _RogueApScanNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_RogueApScanNow_Type.__name__=_B
_RogueApScanNow_Object=MibTableColumn
rogueApScanNow=_RogueApScanNow_Object((1,3,6,1,4,1,52,4,13,8,2,1,11),_RogueApScanNow_Type())
rogueApScanNow.setMaxAccess(_C)
if mibBuilder.loadTexts:rogueApScanNow.setStatus(_A)
class _EnterpriseApRadioAntennaModeControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('external',2)))
_EnterpriseApRadioAntennaModeControl_Type.__name__=_B
_EnterpriseApRadioAntennaModeControl_Object=MibTableColumn
enterpriseApRadioAntennaModeControl=_EnterpriseApRadioAntennaModeControl_Object((1,3,6,1,4,1,52,4,13,8,2,1,12),_EnterpriseApRadioAntennaModeControl_Type())
enterpriseApRadioAntennaModeControl.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApRadioAntennaModeControl.setStatus(_A)
class _EnterpriseApRadioFixedAntennaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('diversity',1),('left',2),('right',3)))
_EnterpriseApRadioFixedAntennaType_Type.__name__=_B
_EnterpriseApRadioFixedAntennaType_Object=MibTableColumn
enterpriseApRadioFixedAntennaType=_EnterpriseApRadioFixedAntennaType_Object((1,3,6,1,4,1,52,4,13,8,2,1,13),_EnterpriseApRadioFixedAntennaType_Type())
enterpriseApRadioFixedAntennaType.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioFixedAntennaType.setStatus(_A)
_EnterpriseApRadioAntennaID_Type=Integer32
_EnterpriseApRadioAntennaID_Object=MibTableColumn
enterpriseApRadioAntennaID=_EnterpriseApRadioAntennaID_Object((1,3,6,1,4,1,52,4,13,8,2,1,14),_EnterpriseApRadioAntennaID_Type())
enterpriseApRadioAntennaID.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioAntennaID.setStatus(_A)
class _EnterpriseApRadioMulticastDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,9,11,12,18,24,36,48,54)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,5),(_j,6),(_k,9),(_l,11),(_m,12),(_n,18),(_o,24),(_p,36),('fortyEightMbps',48),(_q,54)))
_EnterpriseApRadioMulticastDataRate_Type.__name__=_B
_EnterpriseApRadioMulticastDataRate_Object=MibTableColumn
enterpriseApRadioMulticastDataRate=_EnterpriseApRadioMulticastDataRate_Object((1,3,6,1,4,1,52,4,13,8,2,1,15),_EnterpriseApRadioMulticastDataRate_Type())
enterpriseApRadioMulticastDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioMulticastDataRate.setStatus(_A)
class _EnterpriseApRadioAutoDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioAutoDataRate_Type.__name__=_B
_EnterpriseApRadioAutoDataRate_Object=MibTableColumn
enterpriseApRadioAutoDataRate=_EnterpriseApRadioAutoDataRate_Object((1,3,6,1,4,1,52,4,13,8,2,1,16),_EnterpriseApRadioAutoDataRate_Type())
enterpriseApRadioAutoDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioAutoDataRate.setStatus(_A)
class _EnterpriseApRadioPreamble_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('long',1),('short',2),(_L,3)))
_EnterpriseApRadioPreamble_Type.__name__=_B
_EnterpriseApRadioPreamble_Object=MibTableColumn
enterpriseApRadioPreamble=_EnterpriseApRadioPreamble_Object((1,3,6,1,4,1,52,4,13,8,2,1,17),_EnterpriseApRadioPreamble_Type())
enterpriseApRadioPreamble.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioPreamble.setStatus(_A)
class _EnterpriseApRadioSWRetryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApRadioSWRetryMode_Type.__name__=_B
_EnterpriseApRadioSWRetryMode_Object=MibTableColumn
enterpriseApRadioSWRetryMode=_EnterpriseApRadioSWRetryMode_Object((1,3,6,1,4,1,52,4,13,8,2,1,18),_EnterpriseApRadioSWRetryMode_Type())
enterpriseApRadioSWRetryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApRadioSWRetryMode.setStatus(_A)
_EnterpriseApVapRadioTable_Object=MibTable
enterpriseApVapRadioTable=_EnterpriseApVapRadioTable_Object((1,3,6,1,4,1,52,4,13,8,3))
if mibBuilder.loadTexts:enterpriseApVapRadioTable.setStatus(_A)
_EnterpriseApVapRadioEntry_Object=MibTableRow
enterpriseApVapRadioEntry=_EnterpriseApVapRadioEntry_Object((1,3,6,1,4,1,52,4,13,8,3,1))
enterpriseApVapRadioEntry.setIndexNames((0,_F,_r))
if mibBuilder.loadTexts:enterpriseApVapRadioEntry.setStatus(_A)
class _EnterpriseApVapRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EnterpriseApVapRadioIndex_Type.__name__=_B
_EnterpriseApVapRadioIndex_Object=MibTableColumn
enterpriseApVapRadioIndex=_EnterpriseApVapRadioIndex_Object((1,3,6,1,4,1,52,4,13,8,3,1,1),_EnterpriseApVapRadioIndex_Type())
enterpriseApVapRadioIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:enterpriseApVapRadioIndex.setStatus(_A)
class _EnterpriseApVapRadioState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApVapRadioState_Type.__name__=_B
_EnterpriseApVapRadioState_Object=MibTableColumn
enterpriseApVapRadioState=_EnterpriseApVapRadioState_Object((1,3,6,1,4,1,52,4,13,8,3,1,2),_EnterpriseApVapRadioState_Type())
enterpriseApVapRadioState.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApVapRadioState.setStatus(_A)
class _EnterpriseApVapRadioSecureAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApVapRadioSecureAccess_Type.__name__=_B
_EnterpriseApVapRadioSecureAccess_Object=MibTableColumn
enterpriseApVapRadioSecureAccess=_EnterpriseApVapRadioSecureAccess_Object((1,3,6,1,4,1,52,4,13,8,3,1,3),_EnterpriseApVapRadioSecureAccess_Type())
enterpriseApVapRadioSecureAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApVapRadioSecureAccess.setStatus(_A)
class _EnterpriseApVapRadioMaxAssoc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EnterpriseApVapRadioMaxAssoc_Type.__name__=_B
_EnterpriseApVapRadioMaxAssoc_Object=MibTableColumn
enterpriseApVapRadioMaxAssoc=_EnterpriseApVapRadioMaxAssoc_Object((1,3,6,1,4,1,52,4,13,8,3,1,4),_EnterpriseApVapRadioMaxAssoc_Type())
enterpriseApVapRadioMaxAssoc.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApVapRadioMaxAssoc.setStatus(_A)
class _EnterpriseApVapRadioTransmitKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EnterpriseApVapRadioTransmitKey_Type.__name__=_B
_EnterpriseApVapRadioTransmitKey_Object=MibTableColumn
enterpriseApVapRadioTransmitKey=_EnterpriseApVapRadioTransmitKey_Object((1,3,6,1,4,1,52,4,13,8,3,1,5),_EnterpriseApVapRadioTransmitKey_Type())
enterpriseApVapRadioTransmitKey.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApVapRadioTransmitKey.setStatus(_A)
class _EnterpriseApVapRadioDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EnterpriseApVapRadioDescription_Type.__name__=_H
_EnterpriseApVapRadioDescription_Object=MibTableColumn
enterpriseApVapRadioDescription=_EnterpriseApVapRadioDescription_Object((1,3,6,1,4,1,52,4,13,8,3,1,6),_EnterpriseApVapRadioDescription_Type())
enterpriseApVapRadioDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApVapRadioDescription.setStatus(_A)
class _EnterpriseApVapRadioDefefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EnterpriseApVapRadioDefefaultPriority_Type.__name__=_B
_EnterpriseApVapRadioDefefaultPriority_Object=MibTableColumn
enterpriseApVapRadioDefefaultPriority=_EnterpriseApVapRadioDefefaultPriority_Object((1,3,6,1,4,1,52,4,13,8,3,1,7),_EnterpriseApVapRadioDefefaultPriority_Type())
enterpriseApVapRadioDefefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApVapRadioDefefaultPriority.setStatus(_A)
_EnterpriseApRadioWdsTable_Object=MibTable
enterpriseApRadioWdsTable=_EnterpriseApRadioWdsTable_Object((1,3,6,1,4,1,52,4,13,8,4))
if mibBuilder.loadTexts:enterpriseApRadioWdsTable.setStatus(_A)
_EnterpriseApRadioWdsEntry_Object=MibTableRow
enterpriseApRadioWdsEntry=_EnterpriseApRadioWdsEntry_Object((1,3,6,1,4,1,52,4,13,8,4,1))
enterpriseApRadioWdsEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:enterpriseApRadioWdsEntry.setStatus(_A)
class _WdsApRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('roleAp',1),('roleBridgeMaster',2),('roleBridge',3)))
_WdsApRole_Type.__name__=_B
_WdsApRole_Object=MibTableColumn
wdsApRole=_WdsApRole_Object((1,3,6,1,4,1,52,4,13,8,4,1,1),_WdsApRole_Type())
wdsApRole.setMaxAccess(_C)
if mibBuilder.loadTexts:wdsApRole.setStatus(_A)
_WdsApAckTimeout_Type=Integer32
_WdsApAckTimeout_Object=MibTableColumn
wdsApAckTimeout=_WdsApAckTimeout_Object((1,3,6,1,4,1,52,4,13,8,4,1,2),_WdsApAckTimeout_Type())
wdsApAckTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:wdsApAckTimeout.setStatus(_A)
_EnterpriseApRadioWdsPeerTable_Object=MibTable
enterpriseApRadioWdsPeerTable=_EnterpriseApRadioWdsPeerTable_Object((1,3,6,1,4,1,52,4,13,8,5))
if mibBuilder.loadTexts:enterpriseApRadioWdsPeerTable.setStatus(_A)
_EnterpriseApRadioWdsPeerEntry_Object=MibTableRow
enterpriseApRadioWdsPeerEntry=_EnterpriseApRadioWdsPeerEntry_Object((1,3,6,1,4,1,52,4,13,8,5,1))
enterpriseApRadioWdsPeerEntry.setIndexNames((0,_F,_M),(0,_F,_s))
if mibBuilder.loadTexts:enterpriseApRadioWdsPeerEntry.setStatus(_A)
class _WdsPeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WdsPeerIndex_Type.__name__=_B
_WdsPeerIndex_Object=MibTableColumn
wdsPeerIndex=_WdsPeerIndex_Object((1,3,6,1,4,1,52,4,13,8,5,1,1),_WdsPeerIndex_Type())
wdsPeerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wdsPeerIndex.setStatus(_A)
class _WdsPeerBssid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_WdsPeerBssid_Type.__name__=_H
_WdsPeerBssid_Object=MibTableColumn
wdsPeerBssid=_WdsPeerBssid_Object((1,3,6,1,4,1,52,4,13,8,5,1,2),_WdsPeerBssid_Type())
wdsPeerBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:wdsPeerBssid.setStatus(_A)
_WdsPeerRSSI_Type=Integer32
_WdsPeerRSSI_Object=MibTableColumn
wdsPeerRSSI=_WdsPeerRSSI_Object((1,3,6,1,4,1,52,4,13,8,5,1,3),_WdsPeerRSSI_Type())
wdsPeerRSSI.setMaxAccess(_G)
if mibBuilder.loadTexts:wdsPeerRSSI.setStatus(_A)
_EnterpriseApRadioWEPKeysTable_Object=MibTable
enterpriseApRadioWEPKeysTable=_EnterpriseApRadioWEPKeysTable_Object((1,3,6,1,4,1,52,4,13,8,6))
if mibBuilder.loadTexts:enterpriseApRadioWEPKeysTable.setStatus(_A)
_EnterpriseApRadioWEPKeysEntry_Object=MibTableRow
enterpriseApRadioWEPKeysEntry=_EnterpriseApRadioWEPKeysEntry_Object((1,3,6,1,4,1,52,4,13,8,6,1))
enterpriseApRadioWEPKeysEntry.setIndexNames((0,_F,_M),(0,_F,_t))
if mibBuilder.loadTexts:enterpriseApRadioWEPKeysEntry.setStatus(_A)
class _EnterpriseApRadioWEPKeysIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_EnterpriseApRadioWEPKeysIndex_Type.__name__=_B
_EnterpriseApRadioWEPKeysIndex_Object=MibTableColumn
enterpriseApRadioWEPKeysIndex=_EnterpriseApRadioWEPKeysIndex_Object((1,3,6,1,4,1,52,4,13,8,6,1,1),_EnterpriseApRadioWEPKeysIndex_Type())
enterpriseApRadioWEPKeysIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:enterpriseApRadioWEPKeysIndex.setStatus(_A)
class _EnterpriseApRadioWEPKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hexadecimalKey',1),('alphanumericKey',2),('otherKey',3)))
_EnterpriseApRadioWEPKeyType_Type.__name__=_B
_EnterpriseApRadioWEPKeyType_Object=MibTableColumn
enterpriseApRadioWEPKeyType=_EnterpriseApRadioWEPKeyType_Object((1,3,6,1,4,1,52,4,13,8,6,1,2),_EnterpriseApRadioWEPKeyType_Type())
enterpriseApRadioWEPKeyType.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApRadioWEPKeyType.setStatus(_A)
class _EnterpriseApRadioWEPKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('keyLength64Bit',1),('keyLength128Bit',2),('keyLength152Bit',3),('keyLengthOther',4)))
_EnterpriseApRadioWEPKeyLength_Type.__name__=_B
_EnterpriseApRadioWEPKeyLength_Object=MibTableColumn
enterpriseApRadioWEPKeyLength=_EnterpriseApRadioWEPKeyLength_Object((1,3,6,1,4,1,52,4,13,8,6,1,3),_EnterpriseApRadioWEPKeyLength_Type())
enterpriseApRadioWEPKeyLength.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApRadioWEPKeyLength.setStatus(_A)
_EnterpriseApRadioAvAntennaListTable_Object=MibTable
enterpriseApRadioAvAntennaListTable=_EnterpriseApRadioAvAntennaListTable_Object((1,3,6,1,4,1,52,4,13,8,7))
if mibBuilder.loadTexts:enterpriseApRadioAvAntennaListTable.setStatus(_A)
_EnterpriseApRadioAvAntennaListEntry_Object=MibTableRow
enterpriseApRadioAvAntennaListEntry=_EnterpriseApRadioAvAntennaListEntry_Object((1,3,6,1,4,1,52,4,13,8,7,1))
enterpriseApRadioAvAntennaListEntry.setIndexNames((0,_F,_M),(0,_F,_u))
if mibBuilder.loadTexts:enterpriseApRadioAvAntennaListEntry.setStatus(_A)
class _EnterpriseApRadioAvAntennaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EnterpriseApRadioAvAntennaIndex_Type.__name__=_B
_EnterpriseApRadioAvAntennaIndex_Object=MibTableColumn
enterpriseApRadioAvAntennaIndex=_EnterpriseApRadioAvAntennaIndex_Object((1,3,6,1,4,1,52,4,13,8,7,1,1),_EnterpriseApRadioAvAntennaIndex_Type())
enterpriseApRadioAvAntennaIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:enterpriseApRadioAvAntennaIndex.setStatus(_A)
_EnterpriseApRadioAvAntennaId_Type=Integer32
_EnterpriseApRadioAvAntennaId_Object=MibTableColumn
enterpriseApRadioAvAntennaId=_EnterpriseApRadioAvAntennaId_Object((1,3,6,1,4,1,52,4,13,8,7,1,2),_EnterpriseApRadioAvAntennaId_Type())
enterpriseApRadioAvAntennaId.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApRadioAvAntennaId.setStatus(_A)
class _EnterpriseApRadioAvAntennaDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EnterpriseApRadioAvAntennaDesc_Type.__name__=_H
_EnterpriseApRadioAvAntennaDesc_Object=MibTableColumn
enterpriseApRadioAvAntennaDesc=_EnterpriseApRadioAvAntennaDesc_Object((1,3,6,1,4,1,52,4,13,8,7,1,3),_EnterpriseApRadioAvAntennaDesc_Type())
enterpriseApRadioAvAntennaDesc.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApRadioAvAntennaDesc.setStatus(_A)
_EnterpriseApRadioAvChannelListTable_Object=MibTable
enterpriseApRadioAvChannelListTable=_EnterpriseApRadioAvChannelListTable_Object((1,3,6,1,4,1,52,4,13,8,8))
if mibBuilder.loadTexts:enterpriseApRadioAvChannelListTable.setStatus(_A)
_EnterpriseApRadioAvChannelListEntry_Object=MibTableRow
enterpriseApRadioAvChannelListEntry=_EnterpriseApRadioAvChannelListEntry_Object((1,3,6,1,4,1,52,4,13,8,8,1))
enterpriseApRadioAvChannelListEntry.setIndexNames((0,_F,_M),(0,_F,_v))
if mibBuilder.loadTexts:enterpriseApRadioAvChannelListEntry.setStatus(_A)
class _EnterpriseApRadioAvChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EnterpriseApRadioAvChannelIndex_Type.__name__=_B
_EnterpriseApRadioAvChannelIndex_Object=MibTableColumn
enterpriseApRadioAvChannelIndex=_EnterpriseApRadioAvChannelIndex_Object((1,3,6,1,4,1,52,4,13,8,8,1,1),_EnterpriseApRadioAvChannelIndex_Type())
enterpriseApRadioAvChannelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:enterpriseApRadioAvChannelIndex.setStatus(_A)
_EnterpriseApRadioAvChannelNo_Type=Integer32
_EnterpriseApRadioAvChannelNo_Object=MibTableColumn
enterpriseApRadioAvChannelNo=_EnterpriseApRadioAvChannelNo_Object((1,3,6,1,4,1,52,4,13,8,8,1,2),_EnterpriseApRadioAvChannelNo_Type())
enterpriseApRadioAvChannelNo.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApRadioAvChannelNo.setStatus(_A)
_ApEtherInterfaceMgnt_ObjectIdentity=ObjectIdentity
apEtherInterfaceMgnt=_ApEtherInterfaceMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,9))
_ApEtherNetConfig_ObjectIdentity=ObjectIdentity
apEtherNetConfig=_ApEtherNetConfig_ObjectIdentity((1,3,6,1,4,1,52,4,13,9,1))
_NetConfigIPAddress_Type=IpAddress
_NetConfigIPAddress_Object=MibScalar
netConfigIPAddress=_NetConfigIPAddress_Object((1,3,6,1,4,1,52,4,13,9,1,1),_NetConfigIPAddress_Type())
netConfigIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigIPAddress.setStatus(_A)
_NetConfigSubnetMask_Type=IpAddress
_NetConfigSubnetMask_Object=MibScalar
netConfigSubnetMask=_NetConfigSubnetMask_Object((1,3,6,1,4,1,52,4,13,9,1,2),_NetConfigSubnetMask_Type())
netConfigSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigSubnetMask.setStatus(_A)
_NetConfigDefaultGateway_Type=IpAddress
_NetConfigDefaultGateway_Object=MibScalar
netConfigDefaultGateway=_NetConfigDefaultGateway_Object((1,3,6,1,4,1,52,4,13,9,1,3),_NetConfigDefaultGateway_Type())
netConfigDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigDefaultGateway.setStatus(_A)
class _NetConfigHttpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_NetConfigHttpState_Type.__name__=_B
_NetConfigHttpState_Object=MibScalar
netConfigHttpState=_NetConfigHttpState_Object((1,3,6,1,4,1,52,4,13,9,1,4),_NetConfigHttpState_Type())
netConfigHttpState.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigHttpState.setStatus(_A)
class _NetConfigHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(514,65535))
_NetConfigHttpPort_Type.__name__=_B
_NetConfigHttpPort_Object=MibScalar
netConfigHttpPort=_NetConfigHttpPort_Object((1,3,6,1,4,1,52,4,13,9,1,5),_NetConfigHttpPort_Type())
netConfigHttpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigHttpPort.setStatus(_A)
class _NetConfigHttpsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_NetConfigHttpsState_Type.__name__=_B
_NetConfigHttpsState_Object=MibScalar
netConfigHttpsState=_NetConfigHttpsState_Object((1,3,6,1,4,1,52,4,13,9,1,6),_NetConfigHttpsState_Type())
netConfigHttpsState.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigHttpsState.setStatus(_A)
class _NetConfigHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(514,65535))
_NetConfigHttpsPort_Type.__name__=_B
_NetConfigHttpsPort_Object=MibScalar
netConfigHttpsPort=_NetConfigHttpsPort_Object((1,3,6,1,4,1,52,4,13,9,1,7),_NetConfigHttpsPort_Type())
netConfigHttpsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigHttpsPort.setStatus(_A)
class _NetConfigDHCPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_NetConfigDHCPState_Type.__name__=_B
_NetConfigDHCPState_Object=MibScalar
netConfigDHCPState=_NetConfigDHCPState_Object((1,3,6,1,4,1,52,4,13,9,1,8),_NetConfigDHCPState_Type())
netConfigDHCPState.setMaxAccess(_C)
if mibBuilder.loadTexts:netConfigDHCPState.setStatus(_A)
_ApFilterControlMgnt_ObjectIdentity=ObjectIdentity
apFilterControlMgnt=_ApFilterControlMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,10))
class _ApFilterControlBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApFilterControlBridge_Type.__name__=_B
_ApFilterControlBridge_Object=MibScalar
apFilterControlBridge=_ApFilterControlBridge_Object((1,3,6,1,4,1,52,4,13,10,1),_ApFilterControlBridge_Type())
apFilterControlBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:apFilterControlBridge.setStatus(_A)
class _EnterpriseApFilterControlAPManage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApFilterControlAPManage_Type.__name__=_B
_EnterpriseApFilterControlAPManage_Object=MibScalar
enterpriseApFilterControlAPManage=_EnterpriseApFilterControlAPManage_Object((1,3,6,1,4,1,52,4,13,10,2),_EnterpriseApFilterControlAPManage_Type())
enterpriseApFilterControlAPManage.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApFilterControlAPManage.setStatus(_A)
class _EnterpriseApFilterControlEthernet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApFilterControlEthernet_Type.__name__=_B
_EnterpriseApFilterControlEthernet_Object=MibScalar
enterpriseApFilterControlEthernet=_EnterpriseApFilterControlEthernet_Object((1,3,6,1,4,1,52,4,13,10,3),_EnterpriseApFilterControlEthernet_Type())
enterpriseApFilterControlEthernet.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApFilterControlEthernet.setStatus(_A)
_EnterpriseApFilterProtocolTable_Object=MibTable
enterpriseApFilterProtocolTable=_EnterpriseApFilterProtocolTable_Object((1,3,6,1,4,1,52,4,13,10,4))
if mibBuilder.loadTexts:enterpriseApFilterProtocolTable.setStatus(_A)
_EnterpriseApFilterProtocolEntry_Object=MibTableRow
enterpriseApFilterProtocolEntry=_EnterpriseApFilterProtocolEntry_Object((1,3,6,1,4,1,52,4,13,10,4,1))
enterpriseApFilterProtocolEntry.setIndexNames((0,_F,_w))
if mibBuilder.loadTexts:enterpriseApFilterProtocolEntry.setStatus(_A)
class _EnterpriseApFilterProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EnterpriseApFilterProtocolIndex_Type.__name__=_B
_EnterpriseApFilterProtocolIndex_Object=MibTableColumn
enterpriseApFilterProtocolIndex=_EnterpriseApFilterProtocolIndex_Object((1,3,6,1,4,1,52,4,13,10,4,1,1),_EnterpriseApFilterProtocolIndex_Type())
enterpriseApFilterProtocolIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:enterpriseApFilterProtocolIndex.setStatus(_A)
_EnterpriseApFilterProtocolName_Type=DisplayString
_EnterpriseApFilterProtocolName_Object=MibTableColumn
enterpriseApFilterProtocolName=_EnterpriseApFilterProtocolName_Object((1,3,6,1,4,1,52,4,13,10,4,1,2),_EnterpriseApFilterProtocolName_Type())
enterpriseApFilterProtocolName.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApFilterProtocolName.setStatus(_A)
_EnterpriseApFilterProtocolISODesignator_Type=DisplayString
_EnterpriseApFilterProtocolISODesignator_Object=MibTableColumn
enterpriseApFilterProtocolISODesignator=_EnterpriseApFilterProtocolISODesignator_Object((1,3,6,1,4,1,52,4,13,10,4,1,3),_EnterpriseApFilterProtocolISODesignator_Type())
enterpriseApFilterProtocolISODesignator.setMaxAccess(_G)
if mibBuilder.loadTexts:enterpriseApFilterProtocolISODesignator.setStatus(_A)
class _EnterpriseApFilterProtocolState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_EnterpriseApFilterProtocolState_Type.__name__=_B
_EnterpriseApFilterProtocolState_Object=MibTableColumn
enterpriseApFilterProtocolState=_EnterpriseApFilterProtocolState_Object((1,3,6,1,4,1,52,4,13,10,4,1,4),_EnterpriseApFilterProtocolState_Type())
enterpriseApFilterProtocolState.setMaxAccess(_C)
if mibBuilder.loadTexts:enterpriseApFilterProtocolState.setStatus(_A)
class _ApvGlobalIBSSRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('perVapModeEnable',1),('allVapModeEnable',2)))
_ApvGlobalIBSSRelayMode_Type.__name__=_B
_ApvGlobalIBSSRelayMode_Object=MibScalar
apvGlobalIBSSRelayMode=_ApvGlobalIBSSRelayMode_Object((1,3,6,1,4,1,52,4,13,10,5),_ApvGlobalIBSSRelayMode_Type())
apvGlobalIBSSRelayMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apvGlobalIBSSRelayMode.setStatus(_A)
_ApvFilterControlTable_Object=MibTable
apvFilterControlTable=_ApvFilterControlTable_Object((1,3,6,1,4,1,52,4,13,10,6))
if mibBuilder.loadTexts:apvFilterControlTable.setStatus(_A)
_ApvFilterControlEntry_Object=MibTableRow
apvFilterControlEntry=_ApvFilterControlEntry_Object((1,3,6,1,4,1,52,4,13,10,6,1))
apvFilterControlEntry.setIndexNames((0,_F,_x))
if mibBuilder.loadTexts:apvFilterControlEntry.setStatus(_A)
class _ApvFilterControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApvFilterControlIndex_Type.__name__=_B
_ApvFilterControlIndex_Object=MibTableColumn
apvFilterControlIndex=_ApvFilterControlIndex_Object((1,3,6,1,4,1,52,4,13,10,6,1,1),_ApvFilterControlIndex_Type())
apvFilterControlIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apvFilterControlIndex.setStatus(_A)
class _ApvIBSSFilterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApvIBSSFilterControl_Type.__name__=_B
_ApvIBSSFilterControl_Object=MibTableColumn
apvIBSSFilterControl=_ApvIBSSFilterControl_Object((1,3,6,1,4,1,52,4,13,10,6,1,2),_ApvIBSSFilterControl_Type())
apvIBSSFilterControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apvIBSSFilterControl.setStatus(_A)
class _ApvAPManageFilterControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApvAPManageFilterControl_Type.__name__=_B
_ApvAPManageFilterControl_Object=MibTableColumn
apvAPManageFilterControl=_ApvAPManageFilterControl_Object((1,3,6,1,4,1,52,4,13,10,6,1,3),_ApvAPManageFilterControl_Type())
apvAPManageFilterControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apvAPManageFilterControl.setStatus(_A)
_ApVLANMgnt_ObjectIdentity=ObjectIdentity
apVLANMgnt=_ApVLANMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,11))
_ApVLANMgntNativeId_Type=Integer32
_ApVLANMgntNativeId_Object=MibScalar
apVLANMgntNativeId=_ApVLANMgntNativeId_Object((1,3,6,1,4,1,52,4,13,11,1),_ApVLANMgntNativeId_Type())
apVLANMgntNativeId.setMaxAccess(_C)
if mibBuilder.loadTexts:apVLANMgntNativeId.setStatus(_A)
class _ApVLANMgntState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApVLANMgntState_Type.__name__=_B
_ApVLANMgntState_Object=MibScalar
apVLANMgntState=_ApVLANMgntState_Object((1,3,6,1,4,1,52,4,13,11,2),_ApVLANMgntState_Type())
apVLANMgntState.setMaxAccess(_G)
if mibBuilder.loadTexts:apVLANMgntState.setStatus(_A)
class _ApVLANMgntStateNextBoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApVLANMgntStateNextBoot_Type.__name__=_B
_ApVLANMgntStateNextBoot_Object=MibScalar
apVLANMgntStateNextBoot=_ApVLANMgntStateNextBoot_Object((1,3,6,1,4,1,52,4,13,11,3),_ApVLANMgntStateNextBoot_Type())
apVLANMgntStateNextBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:apVLANMgntStateNextBoot.setStatus(_A)
_ApNativeVlanTable_Object=MibTable
apNativeVlanTable=_ApNativeVlanTable_Object((1,3,6,1,4,1,52,4,13,11,6))
if mibBuilder.loadTexts:apNativeVlanTable.setStatus(_A)
_ApNativeVlanEntry_Object=MibTableRow
apNativeVlanEntry=_ApNativeVlanEntry_Object((1,3,6,1,4,1,52,4,13,11,6,1))
apNativeVlanEntry.setIndexNames((0,_F,_y),(0,_F,_z))
if mibBuilder.loadTexts:apNativeVlanEntry.setStatus(_A)
class _ApNativeVlanIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApNativeVlanIfIndex_Type.__name__=_B
_ApNativeVlanIfIndex_Object=MibTableColumn
apNativeVlanIfIndex=_ApNativeVlanIfIndex_Object((1,3,6,1,4,1,52,4,13,11,6,1,1),_ApNativeVlanIfIndex_Type())
apNativeVlanIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apNativeVlanIfIndex.setStatus(_A)
class _ApNativeVlanSsidNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApNativeVlanSsidNumber_Type.__name__=_B
_ApNativeVlanSsidNumber_Object=MibTableColumn
apNativeVlanSsidNumber=_ApNativeVlanSsidNumber_Object((1,3,6,1,4,1,52,4,13,11,6,1,2),_ApNativeVlanSsidNumber_Type())
apNativeVlanSsidNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:apNativeVlanSsidNumber.setStatus(_A)
_ApNativeVlanVlanId_Type=Integer32
_ApNativeVlanVlanId_Object=MibTableColumn
apNativeVlanVlanId=_ApNativeVlanVlanId_Object((1,3,6,1,4,1,52,4,13,11,6,1,3),_ApNativeVlanVlanId_Type())
apNativeVlanVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:apNativeVlanVlanId.setStatus(_A)
class _ApNativeVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApNativeVlanState_Type.__name__=_B
_ApNativeVlanState_Object=MibTableColumn
apNativeVlanState=_ApNativeVlanState_Object((1,3,6,1,4,1,52,4,13,11,6,1,4),_ApNativeVlanState_Type())
apNativeVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:apNativeVlanState.setStatus(_A)
_ApVLANMgntEtherUntaggedVlanId_Type=Integer32
_ApVLANMgntEtherUntaggedVlanId_Object=MibScalar
apVLANMgntEtherUntaggedVlanId=_ApVLANMgntEtherUntaggedVlanId_Object((1,3,6,1,4,1,52,4,13,11,7),_ApVLANMgntEtherUntaggedVlanId_Type())
apVLANMgntEtherUntaggedVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:apVLANMgntEtherUntaggedVlanId.setStatus(_A)
_ApAuthenticationMgnt_ObjectIdentity=ObjectIdentity
apAuthenticationMgnt=_ApAuthenticationMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,12))
_ApAuthenticationSetupEntry_ObjectIdentity=ObjectIdentity
apAuthenticationSetupEntry=_ApAuthenticationSetupEntry_ObjectIdentity((1,3,6,1,4,1,52,4,13,12,1))
class _Ap8021xState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_P,1),(_Q,2)))
_Ap8021xState_Type.__name__=_B
_Ap8021xState_Object=MibScalar
ap8021xState=_Ap8021xState_Object((1,3,6,1,4,1,52,4,13,12,1,1),_Ap8021xState_Type())
ap8021xState.setMaxAccess(_C)
if mibBuilder.loadTexts:ap8021xState.setStatus(_A)
class _Ap8021xBroadcastKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Ap8021xBroadcastKeyRefreshRate_Type.__name__=_B
_Ap8021xBroadcastKeyRefreshRate_Object=MibScalar
ap8021xBroadcastKeyRefreshRate=_Ap8021xBroadcastKeyRefreshRate_Object((1,3,6,1,4,1,52,4,13,12,1,2),_Ap8021xBroadcastKeyRefreshRate_Type())
ap8021xBroadcastKeyRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ap8021xBroadcastKeyRefreshRate.setStatus(_A)
class _Ap8021xSessionKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Ap8021xSessionKeyRefreshRate_Type.__name__=_B
_Ap8021xSessionKeyRefreshRate_Object=MibScalar
ap8021xSessionKeyRefreshRate=_Ap8021xSessionKeyRefreshRate_Object((1,3,6,1,4,1,52,4,13,12,1,3),_Ap8021xSessionKeyRefreshRate_Type())
ap8021xSessionKeyRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ap8021xSessionKeyRefreshRate.setStatus(_A)
class _Ap8021xReauthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Ap8021xReauthenticationTimeout_Type.__name__=_B
_Ap8021xReauthenticationTimeout_Object=MibScalar
ap8021xReauthenticationTimeout=_Ap8021xReauthenticationTimeout_Object((1,3,6,1,4,1,52,4,13,12,1,4),_Ap8021xReauthenticationTimeout_Type())
ap8021xReauthenticationTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ap8021xReauthenticationTimeout.setStatus(_A)
class _ApAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('local',1),('radius',2)))
_ApAuthenticationMode_Type.__name__=_B
_ApAuthenticationMode_Object=MibScalar
apAuthenticationMode=_ApAuthenticationMode_Object((1,3,6,1,4,1,52,4,13,12,1,5),_ApAuthenticationMode_Type())
apAuthenticationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationMode.setStatus(_A)
_ApAuthenticationServerTable_Object=MibTable
apAuthenticationServerTable=_ApAuthenticationServerTable_Object((1,3,6,1,4,1,52,4,13,12,2))
if mibBuilder.loadTexts:apAuthenticationServerTable.setStatus(_A)
_ApAuthenticationServerEntry_Object=MibTableRow
apAuthenticationServerEntry=_ApAuthenticationServerEntry_Object((1,3,6,1,4,1,52,4,13,12,2,1))
apAuthenticationServerEntry.setIndexNames((0,_F,_A0))
if mibBuilder.loadTexts:apAuthenticationServerEntry.setStatus(_A)
class _ApAuthenticationServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApAuthenticationServerIndex_Type.__name__=_B
_ApAuthenticationServerIndex_Object=MibTableColumn
apAuthenticationServerIndex=_ApAuthenticationServerIndex_Object((1,3,6,1,4,1,52,4,13,12,2,1,1),_ApAuthenticationServerIndex_Type())
apAuthenticationServerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apAuthenticationServerIndex.setStatus(_A)
class _ApAuthenticationServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ApAuthenticationServer_Type.__name__=_H
_ApAuthenticationServer_Object=MibTableColumn
apAuthenticationServer=_ApAuthenticationServer_Object((1,3,6,1,4,1,52,4,13,12,2,1,2),_ApAuthenticationServer_Type())
apAuthenticationServer.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationServer.setStatus(_A)
class _ApAuthenticationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_ApAuthenticationPort_Type.__name__=_B
_ApAuthenticationPort_Object=MibTableColumn
apAuthenticationPort=_ApAuthenticationPort_Object((1,3,6,1,4,1,52,4,13,12,2,1,3),_ApAuthenticationPort_Type())
apAuthenticationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationPort.setStatus(_A)
class _ApAuthenticationKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ApAuthenticationKey_Type.__name__=_H
_ApAuthenticationKey_Object=MibTableColumn
apAuthenticationKey=_ApAuthenticationKey_Object((1,3,6,1,4,1,52,4,13,12,2,1,4),_ApAuthenticationKey_Type())
apAuthenticationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationKey.setStatus(_A)
class _ApAuthenticationRetransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ApAuthenticationRetransmit_Type.__name__=_B
_ApAuthenticationRetransmit_Object=MibTableColumn
apAuthenticationRetransmit=_ApAuthenticationRetransmit_Object((1,3,6,1,4,1,52,4,13,12,2,1,5),_ApAuthenticationRetransmit_Type())
apAuthenticationRetransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationRetransmit.setStatus(_A)
class _ApAuthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ApAuthenticationTimeout_Type.__name__=_B
_ApAuthenticationTimeout_Object=MibTableColumn
apAuthenticationTimeout=_ApAuthenticationTimeout_Object((1,3,6,1,4,1,52,4,13,12,2,1,6),_ApAuthenticationTimeout_Type())
apAuthenticationTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationTimeout.setStatus(_A)
class _ApAuthenticationAcctPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ApAuthenticationAcctPort_Type.__name__=_B
_ApAuthenticationAcctPort_Object=MibTableColumn
apAuthenticationAcctPort=_ApAuthenticationAcctPort_Object((1,3,6,1,4,1,52,4,13,12,2,1,7),_ApAuthenticationAcctPort_Type())
apAuthenticationAcctPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationAcctPort.setStatus(_A)
class _ApAuthenticationAcctInterimUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_ApAuthenticationAcctInterimUpdate_Type.__name__=_B
_ApAuthenticationAcctInterimUpdate_Object=MibTableColumn
apAuthenticationAcctInterimUpdate=_ApAuthenticationAcctInterimUpdate_Object((1,3,6,1,4,1,52,4,13,12,2,1,8),_ApAuthenticationAcctInterimUpdate_Type())
apAuthenticationAcctInterimUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationAcctInterimUpdate.setStatus(_A)
class _ApAuthenticationAcctState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApAuthenticationAcctState_Type.__name__=_B
_ApAuthenticationAcctState_Object=MibTableColumn
apAuthenticationAcctState=_ApAuthenticationAcctState_Object((1,3,6,1,4,1,52,4,13,12,2,1,9),_ApAuthenticationAcctState_Type())
apAuthenticationAcctState.setMaxAccess(_C)
if mibBuilder.loadTexts:apAuthenticationAcctState.setStatus(_A)
_ApAuthenticationSupplicantTable_Object=MibTable
apAuthenticationSupplicantTable=_ApAuthenticationSupplicantTable_Object((1,3,6,1,4,1,52,4,13,12,3))
if mibBuilder.loadTexts:apAuthenticationSupplicantTable.setStatus(_A)
_ApAuthenticationSupplicantEntry_Object=MibTableRow
apAuthenticationSupplicantEntry=_ApAuthenticationSupplicantEntry_Object((1,3,6,1,4,1,52,4,13,12,3,1))
apAuthenticationSupplicantEntry.setIndexNames((0,_F,_A1))
if mibBuilder.loadTexts:apAuthenticationSupplicantEntry.setStatus(_A)
class _Ap8021xSuppIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Ap8021xSuppIndex_Type.__name__=_B
_Ap8021xSuppIndex_Object=MibTableColumn
ap8021xSuppIndex=_Ap8021xSuppIndex_Object((1,3,6,1,4,1,52,4,13,12,3,1,1),_Ap8021xSuppIndex_Type())
ap8021xSuppIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ap8021xSuppIndex.setStatus(_A)
class _Ap8021xSuppState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_Ap8021xSuppState_Type.__name__=_B
_Ap8021xSuppState_Object=MibTableColumn
ap8021xSuppState=_Ap8021xSuppState_Object((1,3,6,1,4,1,52,4,13,12,3,1,2),_Ap8021xSuppState_Type())
ap8021xSuppState.setMaxAccess(_C)
if mibBuilder.loadTexts:ap8021xSuppState.setStatus(_A)
class _Ap8021xSuppUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Ap8021xSuppUser_Type.__name__=_H
_Ap8021xSuppUser_Object=MibTableColumn
ap8021xSuppUser=_Ap8021xSuppUser_Object((1,3,6,1,4,1,52,4,13,12,3,1,3),_Ap8021xSuppUser_Type())
ap8021xSuppUser.setMaxAccess(_C)
if mibBuilder.loadTexts:ap8021xSuppUser.setStatus(_A)
class _Ap8021xSuppPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Ap8021xSuppPasswd_Type.__name__=_H
_Ap8021xSuppPasswd_Object=MibTableColumn
ap8021xSuppPasswd=_Ap8021xSuppPasswd_Object((1,3,6,1,4,1,52,4,13,12,3,1,4),_Ap8021xSuppPasswd_Type())
ap8021xSuppPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:ap8021xSuppPasswd.setStatus(_A)
_ApvAuthenticationSetupTable_Object=MibTable
apvAuthenticationSetupTable=_ApvAuthenticationSetupTable_Object((1,3,6,1,4,1,52,4,13,12,4))
if mibBuilder.loadTexts:apvAuthenticationSetupTable.setStatus(_A)
_ApvAuthenticationSetupEntry_Object=MibTableRow
apvAuthenticationSetupEntry=_ApvAuthenticationSetupEntry_Object((1,3,6,1,4,1,52,4,13,12,4,1))
apvAuthenticationSetupEntry.setIndexNames((0,_F,_A2))
if mibBuilder.loadTexts:apvAuthenticationSetupEntry.setStatus(_A)
class _Apv8021xIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Apv8021xIndex_Type.__name__=_B
_Apv8021xIndex_Object=MibTableColumn
apv8021xIndex=_Apv8021xIndex_Object((1,3,6,1,4,1,52,4,13,12,4,1,1),_Apv8021xIndex_Type())
apv8021xIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apv8021xIndex.setStatus(_A)
class _Apv8021xState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_P,1),(_Q,2)))
_Apv8021xState_Type.__name__=_B
_Apv8021xState_Object=MibTableColumn
apv8021xState=_Apv8021xState_Object((1,3,6,1,4,1,52,4,13,12,4,1,2),_Apv8021xState_Type())
apv8021xState.setMaxAccess(_C)
if mibBuilder.loadTexts:apv8021xState.setStatus(_A)
class _Apv8021xBroadcastKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Apv8021xBroadcastKeyRefreshRate_Type.__name__=_B
_Apv8021xBroadcastKeyRefreshRate_Object=MibTableColumn
apv8021xBroadcastKeyRefreshRate=_Apv8021xBroadcastKeyRefreshRate_Object((1,3,6,1,4,1,52,4,13,12,4,1,3),_Apv8021xBroadcastKeyRefreshRate_Type())
apv8021xBroadcastKeyRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:apv8021xBroadcastKeyRefreshRate.setStatus(_A)
class _Apv8021xSessionKeyRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_Apv8021xSessionKeyRefreshRate_Type.__name__=_B
_Apv8021xSessionKeyRefreshRate_Object=MibTableColumn
apv8021xSessionKeyRefreshRate=_Apv8021xSessionKeyRefreshRate_Object((1,3,6,1,4,1,52,4,13,12,4,1,4),_Apv8021xSessionKeyRefreshRate_Type())
apv8021xSessionKeyRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:apv8021xSessionKeyRefreshRate.setStatus(_A)
class _Apv8021xReauthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Apv8021xReauthenticationTimeout_Type.__name__=_B
_Apv8021xReauthenticationTimeout_Object=MibTableColumn
apv8021xReauthenticationTimeout=_Apv8021xReauthenticationTimeout_Object((1,3,6,1,4,1,52,4,13,12,4,1,5),_Apv8021xReauthenticationTimeout_Type())
apv8021xReauthenticationTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:apv8021xReauthenticationTimeout.setStatus(_A)
class _ApvMACAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('local',1),('remote',2)))
_ApvMACAuthenticationMode_Type.__name__=_B
_ApvMACAuthenticationMode_Object=MibTableColumn
apvMACAuthenticationMode=_ApvMACAuthenticationMode_Object((1,3,6,1,4,1,52,4,13,12,4,1,6),_ApvMACAuthenticationMode_Type())
apvMACAuthenticationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apvMACAuthenticationMode.setStatus(_A)
class _ApvMACAuthenticationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ApvMACAuthenticationTimeout_Type.__name__=_B
_ApvMACAuthenticationTimeout_Object=MibTableColumn
apvMACAuthenticationTimeout=_ApvMACAuthenticationTimeout_Object((1,3,6,1,4,1,52,4,13,12,4,1,7),_ApvMACAuthenticationTimeout_Type())
apvMACAuthenticationTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:apvMACAuthenticationTimeout.setStatus(_A)
class _ApvMACAuthenticationPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ApvMACAuthenticationPasswd_Type.__name__=_H
_ApvMACAuthenticationPasswd_Object=MibTableColumn
apvMACAuthenticationPasswd=_ApvMACAuthenticationPasswd_Object((1,3,6,1,4,1,52,4,13,12,4,1,8),_ApvMACAuthenticationPasswd_Type())
apvMACAuthenticationPasswd.setMaxAccess(_C)
if mibBuilder.loadTexts:apvMACAuthenticationPasswd.setStatus(_A)
_ApWStationSessionMgnt_ObjectIdentity=ObjectIdentity
apWStationSessionMgnt=_ApWStationSessionMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,13))
_ApWStationSessionTable_Object=MibTable
apWStationSessionTable=_ApWStationSessionTable_Object((1,3,6,1,4,1,52,4,13,13,1))
if mibBuilder.loadTexts:apWStationSessionTable.setStatus(_A)
_ApWStationSessionEntry_Object=MibTableRow
apWStationSessionEntry=_ApWStationSessionEntry_Object((1,3,6,1,4,1,52,4,13,13,1,1))
apWStationSessionEntry.setIndexNames((0,_F,_A3),(0,_F,_A4))
if mibBuilder.loadTexts:apWStationSessionEntry.setStatus(_A)
class _ApWStationSessionIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApWStationSessionIfIndex_Type.__name__=_B
_ApWStationSessionIfIndex_Object=MibTableColumn
apWStationSessionIfIndex=_ApWStationSessionIfIndex_Object((1,3,6,1,4,1,52,4,13,13,1,1,1),_ApWStationSessionIfIndex_Type())
apWStationSessionIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apWStationSessionIfIndex.setStatus(_A)
_ApWStationSessionStationAddres_Type=MacAddress
_ApWStationSessionStationAddres_Object=MibTableColumn
apWStationSessionStationAddres=_ApWStationSessionStationAddres_Object((1,3,6,1,4,1,52,4,13,13,1,1,2),_ApWStationSessionStationAddres_Type())
apWStationSessionStationAddres.setMaxAccess(_I)
if mibBuilder.loadTexts:apWStationSessionStationAddres.setStatus(_A)
_ApWStationSessionAuthenticated_Type=TruthValue
_ApWStationSessionAuthenticated_Object=MibTableColumn
apWStationSessionAuthenticated=_ApWStationSessionAuthenticated_Object((1,3,6,1,4,1,52,4,13,13,1,1,3),_ApWStationSessionAuthenticated_Type())
apWStationSessionAuthenticated.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionAuthenticated.setStatus(_A)
_ApWStationSessionAssociated_Type=TruthValue
_ApWStationSessionAssociated_Object=MibTableColumn
apWStationSessionAssociated=_ApWStationSessionAssociated_Object((1,3,6,1,4,1,52,4,13,13,1,1,4),_ApWStationSessionAssociated_Type())
apWStationSessionAssociated.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionAssociated.setStatus(_A)
_ApWStationSessionIsForwarding_Type=TruthValue
_ApWStationSessionIsForwarding_Object=MibTableColumn
apWStationSessionIsForwarding=_ApWStationSessionIsForwarding_Object((1,3,6,1,4,1,52,4,13,13,1,1,5),_ApWStationSessionIsForwarding_Type())
apWStationSessionIsForwarding.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionIsForwarding.setStatus(_A)
class _ApWStationSessionKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('staticWep',2),('dynamicWep',3),('wpaWep',4),('wpaTkip',5),('wpaAes',6)))
_ApWStationSessionKeyType_Type.__name__=_B
_ApWStationSessionKeyType_Object=MibTableColumn
apWStationSessionKeyType=_ApWStationSessionKeyType_Object((1,3,6,1,4,1,52,4,13,13,1,1,6),_ApWStationSessionKeyType_Type())
apWStationSessionKeyType.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionKeyType.setStatus(_A)
_ApWStationSessionAssociationId_Type=Integer32
_ApWStationSessionAssociationId_Object=MibTableColumn
apWStationSessionAssociationId=_ApWStationSessionAssociationId_Object((1,3,6,1,4,1,52,4,13,13,1,1,7),_ApWStationSessionAssociationId_Type())
apWStationSessionAssociationId.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionAssociationId.setStatus(_A)
_ApWStationSessionLastAuthenticatedTime_Type=TimeTicks
_ApWStationSessionLastAuthenticatedTime_Object=MibTableColumn
apWStationSessionLastAuthenticatedTime=_ApWStationSessionLastAuthenticatedTime_Object((1,3,6,1,4,1,52,4,13,13,1,1,8),_ApWStationSessionLastAuthenticatedTime_Type())
apWStationSessionLastAuthenticatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionLastAuthenticatedTime.setStatus(_A)
_ApWStationSessionAssociatedTime_Type=TimeTicks
_ApWStationSessionAssociatedTime_Object=MibTableColumn
apWStationSessionAssociatedTime=_ApWStationSessionAssociatedTime_Object((1,3,6,1,4,1,52,4,13,13,1,1,9),_ApWStationSessionAssociatedTime_Type())
apWStationSessionAssociatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionAssociatedTime.setStatus(_A)
_ApWStationSessionLastAssociatedTime_Type=TimeTicks
_ApWStationSessionLastAssociatedTime_Object=MibTableColumn
apWStationSessionLastAssociatedTime=_ApWStationSessionLastAssociatedTime_Object((1,3,6,1,4,1,52,4,13,13,1,1,10),_ApWStationSessionLastAssociatedTime_Type())
apWStationSessionLastAssociatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionLastAssociatedTime.setStatus(_A)
_ApWStationSessionLastDisassociatedTime_Type=TimeTicks
_ApWStationSessionLastDisassociatedTime_Object=MibTableColumn
apWStationSessionLastDisassociatedTime=_ApWStationSessionLastDisassociatedTime_Object((1,3,6,1,4,1,52,4,13,13,1,1,11),_ApWStationSessionLastDisassociatedTime_Type())
apWStationSessionLastDisassociatedTime.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionLastDisassociatedTime.setStatus(_A)
_ApWStationSessionTxPacketCount_Type=Counter32
_ApWStationSessionTxPacketCount_Object=MibTableColumn
apWStationSessionTxPacketCount=_ApWStationSessionTxPacketCount_Object((1,3,6,1,4,1,52,4,13,13,1,1,12),_ApWStationSessionTxPacketCount_Type())
apWStationSessionTxPacketCount.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionTxPacketCount.setStatus(_A)
_ApWStationSessionRxPacketCount_Type=Counter32
_ApWStationSessionRxPacketCount_Object=MibTableColumn
apWStationSessionRxPacketCount=_ApWStationSessionRxPacketCount_Object((1,3,6,1,4,1,52,4,13,13,1,1,13),_ApWStationSessionRxPacketCount_Type())
apWStationSessionRxPacketCount.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionRxPacketCount.setStatus(_A)
_ApWStationSessionTxByteCount_Type=Counter32
_ApWStationSessionTxByteCount_Object=MibTableColumn
apWStationSessionTxByteCount=_ApWStationSessionTxByteCount_Object((1,3,6,1,4,1,52,4,13,13,1,1,14),_ApWStationSessionTxByteCount_Type())
apWStationSessionTxByteCount.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionTxByteCount.setStatus(_A)
_ApWStationSessionRxByteCount_Type=Counter32
_ApWStationSessionRxByteCount_Object=MibTableColumn
apWStationSessionRxByteCount=_ApWStationSessionRxByteCount_Object((1,3,6,1,4,1,52,4,13,13,1,1,15),_ApWStationSessionRxByteCount_Type())
apWStationSessionRxByteCount.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionRxByteCount.setStatus(_A)
_ApWStationSessionVlanID_Type=Integer32
_ApWStationSessionVlanID_Object=MibTableColumn
apWStationSessionVlanID=_ApWStationSessionVlanID_Object((1,3,6,1,4,1,52,4,13,13,1,1,16),_ApWStationSessionVlanID_Type())
apWStationSessionVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:apWStationSessionVlanID.setStatus(_A)
_ApRogueApMgnt_ObjectIdentity=ObjectIdentity
apRogueApMgnt=_ApRogueApMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,14))
_RogueApDetectionTable_Object=MibTable
rogueApDetectionTable=_RogueApDetectionTable_Object((1,3,6,1,4,1,52,4,13,14,1))
if mibBuilder.loadTexts:rogueApDetectionTable.setStatus(_A)
_RogueApDetectionEntry_Object=MibTableRow
rogueApDetectionEntry=_RogueApDetectionEntry_Object((1,3,6,1,4,1,52,4,13,14,1,1))
rogueApDetectionEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:rogueApDetectionEntry.setStatus(_A)
class _RogueApIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_RogueApIndex_Type.__name__=_B
_RogueApIndex_Object=MibTableColumn
rogueApIndex=_RogueApIndex_Object((1,3,6,1,4,1,52,4,13,14,1,1,1),_RogueApIndex_Type())
rogueApIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:rogueApIndex.setStatus(_A)
class _RogueApBssid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_RogueApBssid_Type.__name__=_H
_RogueApBssid_Object=MibTableColumn
rogueApBssid=_RogueApBssid_Object((1,3,6,1,4,1,52,4,13,14,1,1,2),_RogueApBssid_Type())
rogueApBssid.setMaxAccess(_G)
if mibBuilder.loadTexts:rogueApBssid.setStatus(_A)
class _RogueApSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RogueApSsid_Type.__name__=_H
_RogueApSsid_Object=MibTableColumn
rogueApSsid=_RogueApSsid_Object((1,3,6,1,4,1,52,4,13,14,1,1,3),_RogueApSsid_Type())
rogueApSsid.setMaxAccess(_G)
if mibBuilder.loadTexts:rogueApSsid.setStatus(_A)
_RogueApPortNumber_Type=Integer32
_RogueApPortNumber_Object=MibTableColumn
rogueApPortNumber=_RogueApPortNumber_Object((1,3,6,1,4,1,52,4,13,14,1,1,4),_RogueApPortNumber_Type())
rogueApPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:rogueApPortNumber.setStatus(_A)
_RogueApChannelNumber_Type=Integer32
_RogueApChannelNumber_Object=MibTableColumn
rogueApChannelNumber=_RogueApChannelNumber_Object((1,3,6,1,4,1,52,4,13,14,1,1,5),_RogueApChannelNumber_Type())
rogueApChannelNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:rogueApChannelNumber.setStatus(_A)
_RogueApRSSIValue_Type=Integer32
_RogueApRSSIValue_Object=MibTableColumn
rogueApRSSIValue=_RogueApRSSIValue_Object((1,3,6,1,4,1,52,4,13,14,1,1,6),_RogueApRSSIValue_Type())
rogueApRSSIValue.setMaxAccess(_G)
if mibBuilder.loadTexts:rogueApRSSIValue.setStatus(_A)
_ApRougeApControl_ObjectIdentity=ObjectIdentity
apRougeApControl=_ApRougeApControl_ObjectIdentity((1,3,6,1,4,1,52,4,13,14,2))
class _RogueApRADIUSAuthenticate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_RogueApRADIUSAuthenticate_Type.__name__=_B
_RogueApRADIUSAuthenticate_Object=MibScalar
rogueApRADIUSAuthenticate=_RogueApRADIUSAuthenticate_Object((1,3,6,1,4,1,52,4,13,14,2,1),_RogueApRADIUSAuthenticate_Type())
rogueApRADIUSAuthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:rogueApRADIUSAuthenticate.setStatus(_A)
class _RogueApClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_RogueApClear_Type.__name__=_B
_RogueApClear_Object=MibScalar
rogueApClear=_RogueApClear_Object((1,3,6,1,4,1,52,4,13,14,2,2),_RogueApClear_Type())
rogueApClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rogueApClear.setStatus(_A)
_ApAdminMgnt_ObjectIdentity=ObjectIdentity
apAdminMgnt=_ApAdminMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,15))
class _ApAdminUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ApAdminUsername_Type.__name__=_H
_ApAdminUsername_Object=MibScalar
apAdminUsername=_ApAdminUsername_Object((1,3,6,1,4,1,52,4,13,15,1),_ApAdminUsername_Type())
apAdminUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:apAdminUsername.setStatus(_A)
class _AppAdminPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AppAdminPassword_Type.__name__=_H
_AppAdminPassword_Object=MibScalar
appAdminPassword=_AppAdminPassword_Object((1,3,6,1,4,1,52,4,13,15,2),_AppAdminPassword_Type())
appAdminPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:appAdminPassword.setStatus(_A)
_ApResetMgt_ObjectIdentity=ObjectIdentity
apResetMgt=_ApResetMgt_ObjectIdentity((1,3,6,1,4,1,52,4,13,16))
class _ApRestartOpCodeFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_ApRestartOpCodeFile_Type.__name__=_H
_ApRestartOpCodeFile_Object=MibScalar
apRestartOpCodeFile=_ApRestartOpCodeFile_Object((1,3,6,1,4,1,52,4,13,16,1),_ApRestartOpCodeFile_Type())
apRestartOpCodeFile.setMaxAccess(_C)
if mibBuilder.loadTexts:apRestartOpCodeFile.setStatus(_A)
class _ApRestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('warmBoot',2),('coldBoot',3)))
_ApRestartControl_Type.__name__=_B
_ApRestartControl_Object=MibScalar
apRestartControl=_ApRestartControl_Object((1,3,6,1,4,1,52,4,13,16,2),_ApRestartControl_Type())
apRestartControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apRestartControl.setStatus(_A)
_ApSNTPMgnt_ObjectIdentity=ObjectIdentity
apSNTPMgnt=_ApSNTPMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,17))
class _ApSNTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApSNTPState_Type.__name__=_B
_ApSNTPState_Object=MibScalar
apSNTPState=_ApSNTPState_Object((1,3,6,1,4,1,52,4,13,17,1),_ApSNTPState_Type())
apSNTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPState.setStatus(_A)
_ApSNTPPrimaryServer_Type=IpAddress
_ApSNTPPrimaryServer_Object=MibScalar
apSNTPPrimaryServer=_ApSNTPPrimaryServer_Object((1,3,6,1,4,1,52,4,13,17,2),_ApSNTPPrimaryServer_Type())
apSNTPPrimaryServer.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPPrimaryServer.setStatus(_A)
_ApSNTPSecondaryServer_Type=IpAddress
_ApSNTPSecondaryServer_Object=MibScalar
apSNTPSecondaryServer=_ApSNTPSecondaryServer_Object((1,3,6,1,4,1,52,4,13,17,3),_ApSNTPSecondaryServer_Type())
apSNTPSecondaryServer.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPSecondaryServer.setStatus(_A)
class _ApSNTPTimezone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53)));namedValues=NamedValues(*(('enewetakKwajalein',0),('midwayIsland',1),('hawaii',2),('alaska',3),('pacific',4),('arizona',5),('mountain',6),('central',7),('mexicoCity',8),('saskatchewan',9),('bogota',10),('eastern',11),('indiana',12),('atlantic',13),('caracas',14),('santiago',15),('newfoundland',16),('brasilia',17),('buenos',18),('midAtlantic',19),('azores',20),('casablanca',21),('greenwichMeanTimeDublin',22),('greenwichMeanTimeLisbon',23),('amsterdam',24),('stockholm',25),('bratislava',26),('prague',27),('paris',28),('sofija',29),('athens',30),('bucharest',31),('cairo',32),('harare',33),('helsinki',34),('israel',35),('baghdad',36),('moscow',37),('tehran',38),('abuDhabi',39),('vogograd',40),('islamabad',41),('almaty',42),('bangkok',43),('beijing',44),('taipei',45),('tokyo',46),('brisbane',47),('canberra',48),('guam',49),('hobart',50),('magadan',51),('fiji',52),('wellington',53)))
_ApSNTPTimezone_Type.__name__=_B
_ApSNTPTimezone_Object=MibScalar
apSNTPTimezone=_ApSNTPTimezone_Object((1,3,6,1,4,1,52,4,13,17,4),_ApSNTPTimezone_Type())
apSNTPTimezone.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPTimezone.setStatus(_A)
class _ApSNTPDST_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApSNTPDST_Type.__name__=_B
_ApSNTPDST_Object=MibScalar
apSNTPDST=_ApSNTPDST_Object((1,3,6,1,4,1,52,4,13,17,5),_ApSNTPDST_Type())
apSNTPDST.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPDST.setStatus(_A)
class _ApSNTPDSTStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ApSNTPDSTStartMonth_Type.__name__=_B
_ApSNTPDSTStartMonth_Object=MibScalar
apSNTPDSTStartMonth=_ApSNTPDSTStartMonth_Object((1,3,6,1,4,1,52,4,13,17,6),_ApSNTPDSTStartMonth_Type())
apSNTPDSTStartMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPDSTStartMonth.setStatus(_A)
class _ApSNTPDSTStartDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_ApSNTPDSTStartDay_Type.__name__=_B
_ApSNTPDSTStartDay_Object=MibScalar
apSNTPDSTStartDay=_ApSNTPDSTStartDay_Object((1,3,6,1,4,1,52,4,13,17,7),_ApSNTPDSTStartDay_Type())
apSNTPDSTStartDay.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPDSTStartDay.setStatus(_A)
class _ApSNTPDSTEndMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ApSNTPDSTEndMonth_Type.__name__=_B
_ApSNTPDSTEndMonth_Object=MibScalar
apSNTPDSTEndMonth=_ApSNTPDSTEndMonth_Object((1,3,6,1,4,1,52,4,13,17,8),_ApSNTPDSTEndMonth_Type())
apSNTPDSTEndMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPDSTEndMonth.setStatus(_A)
class _ApSNTPDSTEndDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_ApSNTPDSTEndDay_Type.__name__=_B
_ApSNTPDSTEndDay_Object=MibScalar
apSNTPDSTEndDay=_ApSNTPDSTEndDay_Object((1,3,6,1,4,1,52,4,13,17,9),_ApSNTPDSTEndDay_Type())
apSNTPDSTEndDay.setMaxAccess(_C)
if mibBuilder.loadTexts:apSNTPDSTEndDay.setStatus(_A)
_ApDNSMgnt_ObjectIdentity=ObjectIdentity
apDNSMgnt=_ApDNSMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,18))
_ApDNSPrimaryServer_Type=IpAddress
_ApDNSPrimaryServer_Object=MibScalar
apDNSPrimaryServer=_ApDNSPrimaryServer_Object((1,3,6,1,4,1,52,4,13,18,1),_ApDNSPrimaryServer_Type())
apDNSPrimaryServer.setMaxAccess(_C)
if mibBuilder.loadTexts:apDNSPrimaryServer.setStatus(_A)
_ApDNSSecondaryServer_Type=IpAddress
_ApDNSSecondaryServer_Object=MibScalar
apDNSSecondaryServer=_ApDNSSecondaryServer_Object((1,3,6,1,4,1,52,4,13,18,2),_ApDNSSecondaryServer_Type())
apDNSSecondaryServer.setMaxAccess(_C)
if mibBuilder.loadTexts:apDNSSecondaryServer.setStatus(_A)
_ApIappMgnt_ObjectIdentity=ObjectIdentity
apIappMgnt=_ApIappMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,19))
class _ApIappEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApIappEnabled_Type.__name__=_B
_ApIappEnabled_Object=MibScalar
apIappEnabled=_ApIappEnabled_Object((1,3,6,1,4,1,52,4,13,19,1),_ApIappEnabled_Type())
apIappEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:apIappEnabled.setStatus(_A)
_ApSyslogConfigMgnt_ObjectIdentity=ObjectIdentity
apSyslogConfigMgnt=_ApSyslogConfigMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,20))
class _ApLogConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApLogConfigState_Type.__name__=_B
_ApLogConfigState_Object=MibScalar
apLogConfigState=_ApLogConfigState_Object((1,3,6,1,4,1,52,4,13,20,1),_ApLogConfigState_Type())
apLogConfigState.setMaxAccess(_C)
if mibBuilder.loadTexts:apLogConfigState.setStatus(_A)
class _ApSyslogConsoleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApSyslogConsoleState_Type.__name__=_B
_ApSyslogConsoleState_Object=MibScalar
apSyslogConsoleState=_ApSyslogConsoleState_Object((1,3,6,1,4,1,52,4,13,20,2),_ApSyslogConsoleState_Type())
apSyslogConsoleState.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogConsoleState.setStatus(_A)
class _ApSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_ApSyslogLevel_Type.__name__=_B
_ApSyslogLevel_Object=MibScalar
apSyslogLevel=_ApSyslogLevel_Object((1,3,6,1,4,1,52,4,13,20,3),_ApSyslogLevel_Type())
apSyslogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogLevel.setStatus(_A)
_ApSyslogServerTable_Object=MibTable
apSyslogServerTable=_ApSyslogServerTable_Object((1,3,6,1,4,1,52,4,13,20,4))
if mibBuilder.loadTexts:apSyslogServerTable.setStatus(_A)
_ApSyslogServerEntry_Object=MibTableRow
apSyslogServerEntry=_ApSyslogServerEntry_Object((1,3,6,1,4,1,52,4,13,20,4,1))
apSyslogServerEntry.setIndexNames((0,_F,_A6))
if mibBuilder.loadTexts:apSyslogServerEntry.setStatus(_A)
class _ApSyslogServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ApSyslogServerIndex_Type.__name__=_B
_ApSyslogServerIndex_Object=MibTableColumn
apSyslogServerIndex=_ApSyslogServerIndex_Object((1,3,6,1,4,1,52,4,13,20,4,1,1),_ApSyslogServerIndex_Type())
apSyslogServerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apSyslogServerIndex.setStatus(_A)
class _ApSyslogServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApSyslogServerState_Type.__name__=_B
_ApSyslogServerState_Object=MibTableColumn
apSyslogServerState=_ApSyslogServerState_Object((1,3,6,1,4,1,52,4,13,20,4,1,2),_ApSyslogServerState_Type())
apSyslogServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogServerState.setStatus(_A)
class _ApSyslogServerIPAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApSyslogServerIPAddress_Type.__name__=_H
_ApSyslogServerIPAddress_Object=MibTableColumn
apSyslogServerIPAddress=_ApSyslogServerIPAddress_Object((1,3,6,1,4,1,52,4,13,20,4,1,3),_ApSyslogServerIPAddress_Type())
apSyslogServerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogServerIPAddress.setStatus(_A)
class _ApSyslogServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_ApSyslogServerPort_Type.__name__=_B
_ApSyslogServerPort_Object=MibTableColumn
apSyslogServerPort=_ApSyslogServerPort_Object((1,3,6,1,4,1,52,4,13,20,4,1,4),_ApSyslogServerPort_Type())
apSyslogServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apSyslogServerPort.setStatus(_A)
_ApEventLogMgnt_ObjectIdentity=ObjectIdentity
apEventLogMgnt=_ApEventLogMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,21))
_ApEventLogTable_Object=MibTable
apEventLogTable=_ApEventLogTable_Object((1,3,6,1,4,1,52,4,13,21,1))
if mibBuilder.loadTexts:apEventLogTable.setStatus(_A)
_ApEventLogEntry_Object=MibTableRow
apEventLogEntry=_ApEventLogEntry_Object((1,3,6,1,4,1,52,4,13,21,1,1))
apEventLogEntry.setIndexNames((0,_F,_A7))
if mibBuilder.loadTexts:apEventLogEntry.setStatus(_A)
class _ApEventLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_ApEventLogIndex_Type.__name__=_B
_ApEventLogIndex_Object=MibTableColumn
apEventLogIndex=_ApEventLogIndex_Object((1,3,6,1,4,1,52,4,13,21,1,1,1),_ApEventLogIndex_Type())
apEventLogIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apEventLogIndex.setStatus(_A)
class _ApEventLogMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ApEventLogMessage_Type.__name__=_H
_ApEventLogMessage_Object=MibTableColumn
apEventLogMessage=_ApEventLogMessage_Object((1,3,6,1,4,1,52,4,13,21,1,1,2),_ApEventLogMessage_Type())
apEventLogMessage.setMaxAccess(_G)
if mibBuilder.loadTexts:apEventLogMessage.setStatus(_A)
class _ApEventLogClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearLog',1))
_ApEventLogClear_Type.__name__=_B
_ApEventLogClear_Object=MibScalar
apEventLogClear=_ApEventLogClear_Object((1,3,6,1,4,1,52,4,13,21,2),_ApEventLogClear_Type())
apEventLogClear.setMaxAccess(_C)
if mibBuilder.loadTexts:apEventLogClear.setStatus(_A)
_ApWSLSupportMgnt_ObjectIdentity=ObjectIdentity
apWSLSupportMgnt=_ApWSLSupportMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,22))
class _ApWSLSupportControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApWSLSupportControl_Type.__name__=_B
_ApWSLSupportControl_Object=MibScalar
apWSLSupportControl=_ApWSLSupportControl_Object((1,3,6,1,4,1,52,4,13,22,1),_ApWSLSupportControl_Type())
apWSLSupportControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apWSLSupportControl.setStatus(_A)
class _ApWSLSupportMasterAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApWSLSupportMasterAddress_Type.__name__=_H
_ApWSLSupportMasterAddress_Object=MibScalar
apWSLSupportMasterAddress=_ApWSLSupportMasterAddress_Object((1,3,6,1,4,1,52,4,13,22,2),_ApWSLSupportMasterAddress_Type())
apWSLSupportMasterAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apWSLSupportMasterAddress.setStatus(_A)
class _ApWSLSupportSecondaryAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApWSLSupportSecondaryAddress_Type.__name__=_H
_ApWSLSupportSecondaryAddress_Object=MibScalar
apWSLSupportSecondaryAddress=_ApWSLSupportSecondaryAddress_Object((1,3,6,1,4,1,52,4,13,22,3),_ApWSLSupportSecondaryAddress_Type())
apWSLSupportSecondaryAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apWSLSupportSecondaryAddress.setStatus(_A)
class _ApWSLSupportPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_ApWSLSupportPort_Type.__name__=_B
_ApWSLSupportPort_Object=MibScalar
apWSLSupportPort=_ApWSLSupportPort_Object((1,3,6,1,4,1,52,4,13,22,4),_ApWSLSupportPort_Type())
apWSLSupportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:apWSLSupportPort.setStatus(_A)
class _ApWSLSupportHeartbeatInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ApWSLSupportHeartbeatInterval_Type.__name__=_B
_ApWSLSupportHeartbeatInterval_Object=MibScalar
apWSLSupportHeartbeatInterval=_ApWSLSupportHeartbeatInterval_Object((1,3,6,1,4,1,52,4,13,22,5),_ApWSLSupportHeartbeatInterval_Type())
apWSLSupportHeartbeatInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:apWSLSupportHeartbeatInterval.setStatus(_A)
class _ApWSLSupportHeartbeatLastChange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ApWSLSupportHeartbeatLastChange_Type.__name__=_H
_ApWSLSupportHeartbeatLastChange_Object=MibScalar
apWSLSupportHeartbeatLastChange=_ApWSLSupportHeartbeatLastChange_Object((1,3,6,1,4,1,52,4,13,22,6),_ApWSLSupportHeartbeatLastChange_Type())
apWSLSupportHeartbeatLastChange.setMaxAccess(_G)
if mibBuilder.loadTexts:apWSLSupportHeartbeatLastChange.setStatus(_A)
class _ApWSLSupportOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('standalone',0),('associated',1)))
_ApWSLSupportOperationMode_Type.__name__=_B
_ApWSLSupportOperationMode_Object=MibScalar
apWSLSupportOperationMode=_ApWSLSupportOperationMode_Object((1,3,6,1,4,1,52,4,13,22,7),_ApWSLSupportOperationMode_Type())
apWSLSupportOperationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apWSLSupportOperationMode.setStatus(_A)
class _ApWSLSupportRxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_ApWSLSupportRxThreshold_Type.__name__=_B
_ApWSLSupportRxThreshold_Object=MibScalar
apWSLSupportRxThreshold=_ApWSLSupportRxThreshold_Object((1,3,6,1,4,1,52,4,13,22,8),_ApWSLSupportRxThreshold_Type())
apWSLSupportRxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apWSLSupportRxThreshold.setStatus(_A)
class _ApWSLSupportControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApWSLSupportControlStatus_Type.__name__=_B
_ApWSLSupportControlStatus_Object=MibScalar
apWSLSupportControlStatus=_ApWSLSupportControlStatus_Object((1,3,6,1,4,1,52,4,13,22,9),_ApWSLSupportControlStatus_Type())
apWSLSupportControlStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:apWSLSupportControlStatus.setStatus(_A)
class _ApWSLRFAreaPollControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApWSLRFAreaPollControl_Type.__name__=_B
_ApWSLRFAreaPollControl_Object=MibScalar
apWSLRFAreaPollControl=_ApWSLRFAreaPollControl_Object((1,3,6,1,4,1,52,4,13,22,10),_ApWSLRFAreaPollControl_Type())
apWSLRFAreaPollControl.setMaxAccess(_G)
if mibBuilder.loadTexts:apWSLRFAreaPollControl.setStatus(_A)
class _ApWSLRFAreaPollControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_ApWSLRFAreaPollControlStatus_Type.__name__=_B
_ApWSLRFAreaPollControlStatus_Object=MibScalar
apWSLRFAreaPollControlStatus=_ApWSLRFAreaPollControlStatus_Object((1,3,6,1,4,1,52,4,13,22,11),_ApWSLRFAreaPollControlStatus_Type())
apWSLRFAreaPollControlStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:apWSLRFAreaPollControlStatus.setStatus(_A)
_ApWMMMgnt_ObjectIdentity=ObjectIdentity
apWMMMgnt=_ApWMMMgnt_ObjectIdentity((1,3,6,1,4,1,52,4,13,23))
_ApWMMControlTable_Object=MibTable
apWMMControlTable=_ApWMMControlTable_Object((1,3,6,1,4,1,52,4,13,23,1))
if mibBuilder.loadTexts:apWMMControlTable.setStatus(_A)
_ApWMMControlEntry_Object=MibTableRow
apWMMControlEntry=_ApWMMControlEntry_Object((1,3,6,1,4,1,52,4,13,23,1,1))
apWMMControlEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:apWMMControlEntry.setStatus(_A)
class _ApWMMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_Q,1),(_P,2)))
_ApWMMState_Type.__name__=_B
_ApWMMState_Object=MibTableColumn
apWMMState=_ApWMMState_Object((1,3,6,1,4,1,52,4,13,23,1,1,1),_ApWMMState_Type())
apWMMState.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMState.setStatus(_A)
_ApWMMBssParamTable_Object=MibTable
apWMMBssParamTable=_ApWMMBssParamTable_Object((1,3,6,1,4,1,52,4,13,23,2))
if mibBuilder.loadTexts:apWMMBssParamTable.setStatus(_A)
_ApWMMBssParamEntry_Object=MibTableRow
apWMMBssParamEntry=_ApWMMBssParamEntry_Object((1,3,6,1,4,1,52,4,13,23,2,1))
apWMMBssParamEntry.setIndexNames((0,_N,_O),(0,_F,_A8))
if mibBuilder.loadTexts:apWMMBssParamEntry.setStatus(_A)
class _ApWMMBssParamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ApWMMBssParamIndex_Type.__name__=_B
_ApWMMBssParamIndex_Object=MibTableColumn
apWMMBssParamIndex=_ApWMMBssParamIndex_Object((1,3,6,1,4,1,52,4,13,23,2,1,1),_ApWMMBssParamIndex_Type())
apWMMBssParamIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apWMMBssParamIndex.setStatus(_A)
class _ApWMMBssParamCWmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ApWMMBssParamCWmin_Type.__name__=_B
_ApWMMBssParamCWmin_Object=MibTableColumn
apWMMBssParamCWmin=_ApWMMBssParamCWmin_Object((1,3,6,1,4,1,52,4,13,23,2,1,2),_ApWMMBssParamCWmin_Type())
apWMMBssParamCWmin.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMBssParamCWmin.setStatus(_A)
class _ApWMMBssParamCWmax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ApWMMBssParamCWmax_Type.__name__=_B
_ApWMMBssParamCWmax_Object=MibTableColumn
apWMMBssParamCWmax=_ApWMMBssParamCWmax_Object((1,3,6,1,4,1,52,4,13,23,2,1,3),_ApWMMBssParamCWmax_Type())
apWMMBssParamCWmax.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMBssParamCWmax.setStatus(_A)
class _ApWMMBssParamAIFSN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ApWMMBssParamAIFSN_Type.__name__=_B
_ApWMMBssParamAIFSN_Object=MibTableColumn
apWMMBssParamAIFSN=_ApWMMBssParamAIFSN_Object((1,3,6,1,4,1,52,4,13,23,2,1,4),_ApWMMBssParamAIFSN_Type())
apWMMBssParamAIFSN.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMBssParamAIFSN.setStatus(_A)
class _ApWMMBssParamTXOPLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ApWMMBssParamTXOPLimit_Type.__name__=_B
_ApWMMBssParamTXOPLimit_Object=MibTableColumn
apWMMBssParamTXOPLimit=_ApWMMBssParamTXOPLimit_Object((1,3,6,1,4,1,52,4,13,23,2,1,5),_ApWMMBssParamTXOPLimit_Type())
apWMMBssParamTXOPLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMBssParamTXOPLimit.setStatus(_A)
_ApWMMBssParamAdmissionControl_Type=TruthValue
_ApWMMBssParamAdmissionControl_Object=MibTableColumn
apWMMBssParamAdmissionControl=_ApWMMBssParamAdmissionControl_Object((1,3,6,1,4,1,52,4,13,23,2,1,6),_ApWMMBssParamAdmissionControl_Type())
apWMMBssParamAdmissionControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMBssParamAdmissionControl.setStatus(_A)
_ApWMMApParamTable_Object=MibTable
apWMMApParamTable=_ApWMMApParamTable_Object((1,3,6,1,4,1,52,4,13,23,3))
if mibBuilder.loadTexts:apWMMApParamTable.setStatus(_A)
_ApWMMApParamEntry_Object=MibTableRow
apWMMApParamEntry=_ApWMMApParamEntry_Object((1,3,6,1,4,1,52,4,13,23,3,1))
apWMMApParamEntry.setIndexNames((0,_N,_O),(0,_F,_A9))
if mibBuilder.loadTexts:apWMMApParamEntry.setStatus(_A)
class _ApWMMApParamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ApWMMApParamIndex_Type.__name__=_B
_ApWMMApParamIndex_Object=MibTableColumn
apWMMApParamIndex=_ApWMMApParamIndex_Object((1,3,6,1,4,1,52,4,13,23,3,1,1),_ApWMMApParamIndex_Type())
apWMMApParamIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:apWMMApParamIndex.setStatus(_A)
class _ApWMMApParamCWmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ApWMMApParamCWmin_Type.__name__=_B
_ApWMMApParamCWmin_Object=MibTableColumn
apWMMApParamCWmin=_ApWMMApParamCWmin_Object((1,3,6,1,4,1,52,4,13,23,3,1,2),_ApWMMApParamCWmin_Type())
apWMMApParamCWmin.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMApParamCWmin.setStatus(_A)
class _ApWMMApParamCWmax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ApWMMApParamCWmax_Type.__name__=_B
_ApWMMApParamCWmax_Object=MibTableColumn
apWMMApParamCWmax=_ApWMMApParamCWmax_Object((1,3,6,1,4,1,52,4,13,23,3,1,3),_ApWMMApParamCWmax_Type())
apWMMApParamCWmax.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMApParamCWmax.setStatus(_A)
class _ApWMMApParamAIFSN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ApWMMApParamAIFSN_Type.__name__=_B
_ApWMMApParamAIFSN_Object=MibTableColumn
apWMMApParamAIFSN=_ApWMMApParamAIFSN_Object((1,3,6,1,4,1,52,4,13,23,3,1,4),_ApWMMApParamAIFSN_Type())
apWMMApParamAIFSN.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMApParamAIFSN.setStatus(_A)
class _ApWMMApParamTXOPLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ApWMMApParamTXOPLimit_Type.__name__=_B
_ApWMMApParamTXOPLimit_Object=MibTableColumn
apWMMApParamTXOPLimit=_ApWMMApParamTXOPLimit_Object((1,3,6,1,4,1,52,4,13,23,3,1,5),_ApWMMApParamTXOPLimit_Type())
apWMMApParamTXOPLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMApParamTXOPLimit.setStatus(_A)
_ApWMMApParamAdmissionControl_Type=TruthValue
_ApWMMApParamAdmissionControl_Object=MibTableColumn
apWMMApParamAdmissionControl=_ApWMMApParamAdmissionControl_Object((1,3,6,1,4,1,52,4,13,23,3,1,6),_ApWMMApParamAdmissionControl_Type())
apWMMApParamAdmissionControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apWMMApParamAdmissionControl.setStatus(_A)
_ApNotificationTrapTree_ObjectIdentity=ObjectIdentity
apNotificationTrapTree=_ApNotificationTrapTree_ObjectIdentity((1,3,6,1,4,1,52,4,13,100))
_ApNotificationObjects_ObjectIdentity=ObjectIdentity
apNotificationObjects=_ApNotificationObjects_ObjectIdentity((1,3,6,1,4,1,52,4,13,100,1))
_ApNotificationDot11MacAddr_Type=MacAddress
_ApNotificationDot11MacAddr_Object=MibScalar
apNotificationDot11MacAddr=_ApNotificationDot11MacAddr_Object((1,3,6,1,4,1,52,4,13,100,1,1),_ApNotificationDot11MacAddr_Type())
apNotificationDot11MacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:apNotificationDot11MacAddr.setStatus(_A)
_ApNotificationDot11Station_Type=MacAddress
_ApNotificationDot11Station_Object=MibScalar
apNotificationDot11Station=_ApNotificationDot11Station_Object((1,3,6,1,4,1,52,4,13,100,1,2),_ApNotificationDot11Station_Type())
apNotificationDot11Station.setMaxAccess(_G)
if mibBuilder.loadTexts:apNotificationDot11Station.setStatus(_A)
class _ApNotificationDot11RequestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('association',2),('reAssociation',3),('authentication',4)))
_ApNotificationDot11RequestType_Type.__name__=_B
_ApNotificationDot11RequestType_Object=MibScalar
apNotificationDot11RequestType=_ApNotificationDot11RequestType_Object((1,3,6,1,4,1,52,4,13,100,1,3),_ApNotificationDot11RequestType_Type())
apNotificationDot11RequestType.setMaxAccess(_G)
if mibBuilder.loadTexts:apNotificationDot11RequestType.setStatus(_A)
class _ApNotificationDot11ReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('invalidModeOrState',1),('unAuthenticatedStation',2),('internalError',3),('outOfSequenceFrame',4),('unsupportedAlgorithm',5),('invalidFrameLngth',6),('wepRequiredOnAP',7),('wepNotAllowed',8),('challengeTextMismatch',9)))
_ApNotificationDot11ReasonCode_Type.__name__=_B
_ApNotificationDot11ReasonCode_Object=MibScalar
apNotificationDot11ReasonCode=_ApNotificationDot11ReasonCode_Object((1,3,6,1,4,1,52,4,13,100,1,4),_ApNotificationDot11ReasonCode_Type())
apNotificationDot11ReasonCode.setMaxAccess(_G)
if mibBuilder.loadTexts:apNotificationDot11ReasonCode.setStatus(_A)
_ApNotificationDot11IpAddress_Type=IpAddress
_ApNotificationDot11IpAddress_Object=MibScalar
apNotificationDot11IpAddress=_ApNotificationDot11IpAddress_Object((1,3,6,1,4,1,52,4,13,100,1,5),_ApNotificationDot11IpAddress_Type())
apNotificationDot11IpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:apNotificationDot11IpAddress.setStatus(_A)
_ApNotificationDot11AuthenticatorMacAddr_Type=MacAddress
_ApNotificationDot11AuthenticatorMacAddr_Object=MibScalar
apNotificationDot11AuthenticatorMacAddr=_ApNotificationDot11AuthenticatorMacAddr_Object((1,3,6,1,4,1,52,4,13,100,1,6),_ApNotificationDot11AuthenticatorMacAddr_Type())
apNotificationDot11AuthenticatorMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:apNotificationDot11AuthenticatorMacAddr.setStatus(_A)
_ApNotificationTrapObjects_ObjectIdentity=ObjectIdentity
apNotificationTrapObjects=_ApNotificationTrapObjects_ObjectIdentity((1,3,6,1,4,1,52,4,13,100,2))
sysSystemUp=NotificationType((1,3,6,1,4,1,52,4,13,100,2,1))
if mibBuilder.loadTexts:sysSystemUp.setStatus(_A)
sysSystemDown=NotificationType((1,3,6,1,4,1,52,4,13,100,2,2))
if mibBuilder.loadTexts:sysSystemDown.setStatus(_A)
sysRadiusServerChanged=NotificationType((1,3,6,1,4,1,52,4,13,100,2,3))
if mibBuilder.loadTexts:sysRadiusServerChanged.setStatus(_A)
dot11StationAssociation=NotificationType((1,3,6,1,4,1,52,4,13,100,2,4))
dot11StationAssociation.setObjects((_F,_J))
if mibBuilder.loadTexts:dot11StationAssociation.setStatus(_A)
dot11StationReAssociation=NotificationType((1,3,6,1,4,1,52,4,13,100,2,5))
dot11StationReAssociation.setObjects((_F,_J))
if mibBuilder.loadTexts:dot11StationReAssociation.setStatus(_A)
dot11StationAuthentication=NotificationType((1,3,6,1,4,1,52,4,13,100,2,6))
dot11StationAuthentication.setObjects((_F,_J))
if mibBuilder.loadTexts:dot11StationAuthentication.setStatus(_A)
dot11StationRequestFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,7))
dot11StationRequestFail.setObjects(*((_F,_J),(_F,_AA),(_F,_AB)))
if mibBuilder.loadTexts:dot11StationRequestFail.setStatus(_A)
dot1xMacAddrAuthSuccess=NotificationType((1,3,6,1,4,1,52,4,13,100,2,9))
dot1xMacAddrAuthSuccess.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xMacAddrAuthSuccess.setStatus(_A)
dot1xMacAddrAuthFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,10))
dot1xMacAddrAuthFail.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xMacAddrAuthFail.setStatus(_A)
dot1xAuthNotInitiated=NotificationType((1,3,6,1,4,1,52,4,13,100,2,11))
dot1xAuthNotInitiated.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xAuthNotInitiated.setStatus(_A)
dot1xAuthSuccess=NotificationType((1,3,6,1,4,1,52,4,13,100,2,12))
dot1xAuthSuccess.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xAuthSuccess.setStatus(_A)
dot1xAuthFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,13))
dot1xAuthFail.setObjects((_F,_J))
if mibBuilder.loadTexts:dot1xAuthFail.setStatus(_A)
localMacAddrAuthSuccess=NotificationType((1,3,6,1,4,1,52,4,13,100,2,14))
localMacAddrAuthSuccess.setObjects((_F,_J))
if mibBuilder.loadTexts:localMacAddrAuthSuccess.setStatus(_A)
localMacAddrAuthFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,15))
localMacAddrAuthFail.setObjects((_F,_J))
if mibBuilder.loadTexts:localMacAddrAuthFail.setStatus(_A)
pppLogonFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,16))
if mibBuilder.loadTexts:pppLogonFail.setStatus(_A)
iappStationRoamedFrom=NotificationType((1,3,6,1,4,1,52,4,13,100,2,17))
iappStationRoamedFrom.setObjects(*((_F,_J),(_F,_R)))
if mibBuilder.loadTexts:iappStationRoamedFrom.setStatus(_A)
iappStationRoamedTo=NotificationType((1,3,6,1,4,1,52,4,13,100,2,18))
iappStationRoamedTo.setObjects(*((_F,_J),(_F,_R)))
if mibBuilder.loadTexts:iappStationRoamedTo.setStatus(_A)
iappContextDataSent=NotificationType((1,3,6,1,4,1,52,4,13,100,2,19))
iappContextDataSent.setObjects(*((_F,_J),(_F,_R)))
if mibBuilder.loadTexts:iappContextDataSent.setStatus(_A)
sntpServerFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,20))
if mibBuilder.loadTexts:sntpServerFail.setStatus(_A)
dot11InterfaceAFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,21))
if mibBuilder.loadTexts:dot11InterfaceAFail.setStatus(_A)
dot11InterfaceGFail=NotificationType((1,3,6,1,4,1,52,4,13,100,2,22))
if mibBuilder.loadTexts:dot11InterfaceGFail.setStatus(_A)
dot11WirelessSTPDetection=NotificationType((1,3,6,1,4,1,52,4,13,100,2,23))
if mibBuilder.loadTexts:dot11WirelessSTPDetection.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'MacAddress':MacAddress,_H:DisplayString,'TruthValue':TruthValue,'cabletron':cabletron,'mibs':mibs,'ctronAP3000':ctronAP3000,'comPortMgnt':comPortMgnt,'comPortControl':comPortControl,'macFilterMgnt':macFilterMgnt,'macFilterTable':macFilterTable,'macFilterEntry':macFilterEntry,_Y:macFilterIndex,'macFilterAddress':macFilterAddress,'macFilterAllowedToGo':macFilterAllowedToGo,'macFilterOpeStatus':macFilterOpeStatus,'apMacFilterControl':apMacFilterControl,'apvMacFilterOperateTable':apvMacFilterOperateTable,'apvMacFilterOperateEntry':apvMacFilterOperateEntry,'apvMacFilterPermission':apvMacFilterPermission,'apvMacFilterAddressToAdd':apvMacFilterAddressToAdd,'apvMacFilterTable':apvMacFilterTable,'apvMacFilterEntry':apvMacFilterEntry,_a:apvMacFilterIndex,'apvMacFilterAddress':apvMacFilterAddress,'apvMacFilterActivity':apvMacFilterActivity,'qosMgnt':qosMgnt,'qosModeControl':qosModeControl,'qosMACTypeTable':qosMACTypeTable,'qosMACTypeEntry':qosMACTypeEntry,_W:qosMACTypeIndex,'qosMACTypeAddress':qosMACTypeAddress,'qosMACTypePriority':qosMACTypePriority,'qosMACTypeOpeStatus':qosMACTypeOpeStatus,'qosEtherTypeTable':qosEtherTypeTable,'qosEtherTypeEntry':qosEtherTypeEntry,'qosEtherTypeIndex':qosEtherTypeIndex,'qosEtherTypeHexValue':qosEtherTypeHexValue,'qosEtherTypePriority':qosEtherTypePriority,'qosEtherTypeOpeStatus':qosEtherTypeOpeStatus,'qosQueueingMode':qosQueueingMode,'qosSVPStatus':qosSVPStatus,'linkQualityMgnt':linkQualityMgnt,'linkQualityTable':linkQualityTable,'linkQualityEntry':linkQualityEntry,_b:linkQualityRadioIndex,_c:linkQualityStaIndex,'linkQualityStaMacAddress':linkQualityStaMacAddress,'linkQualityStaRssi':linkQualityStaRssi,'apSnmpMgnt':apSnmpMgnt,'trapControl':trapControl,'trapConfiguration':trapConfiguration,'trapSysSystemUp':trapSysSystemUp,'trapSysSystemDown':trapSysSystemDown,'trapSysRadiusServerChanged':trapSysRadiusServerChanged,'trapDot11StationAssociation':trapDot11StationAssociation,'trapDot11StationReAssociation':trapDot11StationReAssociation,'trapDot11StationAuthentication':trapDot11StationAuthentication,'trapDot11StationRequestFail':trapDot11StationRequestFail,'trapLocalMacAddrAuthFail':trapLocalMacAddrAuthFail,'trapLocalMacAddrAuthSuccess':trapLocalMacAddrAuthSuccess,'trapDot1xAuthNotInitiated':trapDot1xAuthNotInitiated,'trapDot1xAuthSuccess':trapDot1xAuthSuccess,'trapDot1xAuthFail':trapDot1xAuthFail,'trapDot1xMacAddrAuthSuccess':trapDot1xMacAddrAuthSuccess,'trapDot1xMacAddrAuthFail':trapDot1xMacAddrAuthFail,'trapPppLogonFail':trapPppLogonFail,'trapIappStationRoamedFrom':trapIappStationRoamedFrom,'trapIappStationRoamedTo':trapIappStationRoamedTo,'trapIappContextDataSent':trapIappContextDataSent,'trapSntpServerFail':trapSntpServerFail,'trapDot11InterfaceAFail':trapDot11InterfaceAFail,'trapDot11InterfaceGFail':trapDot11InterfaceGFail,'trapDot11WirelessSTPDetection':trapDot11WirelessSTPDetection,'apSnmpTrapDestinationTable':apSnmpTrapDestinationTable,'apSnmpTrapDestinationEntry':apSnmpTrapDestinationEntry,_d:apSnmpTrapDestinationIndex,'apSnmpTrapDestinationCommunity':apSnmpTrapDestinationCommunity,'apSnmpTrapDestinationIP':apSnmpTrapDestinationIP,'apSnmpTrapDestinationState':apSnmpTrapDestinationState,'apSnmpCommunityReadOnly':apSnmpCommunityReadOnly,'apSnmpCommunityReadWrite':apSnmpCommunityReadWrite,'apSnmpVersionFilter':apSnmpVersionFilter,'sysEntity':sysEntity,'swHardwareVer':swHardwareVer,'swBootRomVer':swBootRomVer,'swOpCodeVer':swOpCodeVer,'swSerialNumber':swSerialNumber,'swProductName':swProductName,'swCountrySetting':swCountrySetting,'apSecurityMgnt':apSecurityMgnt,'apRadioSecurityTable':apRadioSecurityTable,'apRadioSecurityEntry':apRadioSecurityEntry,_e:apRadioSecurityIndex,'apRadioSecurityWEPAuthType':apRadioSecurityWEPAuthType,'apRadioSecuritySharedKeyLen':apRadioSecuritySharedKeyLen,'apRadioSecurityWPAMode':apRadioSecurityWPAMode,'apRadioSecurityWPAKeyType':apRadioSecurityWPAKeyType,'apRadioSecurityWPACipher':apRadioSecurityWPACipher,'apRadioSecurityWPAPSKType':apRadioSecurityWPAPSKType,'apRadioSecurityWPAPSK':apRadioSecurityWPAPSK,'apRadioSecurityWEPKeyType':apRadioSecurityWEPKeyType,'apRadioSecurityWEPEnabled':apRadioSecurityWEPEnabled,'apRadioSecurityWPACipherSuite':apRadioSecurityWPACipherSuite,'apRadioApSecurityWPAPreAuthentication':apRadioApSecurityWPAPreAuthentication,'apRadioApSecurityWPAPmksaLifetime':apRadioApSecurityWPAPmksaLifetime,'apSecuritySsh':apSecuritySsh,'apSecuritySshServerEnabled':apSecuritySshServerEnabled,'apSecuritySshServerPort':apSecuritySshServerPort,'apSecuritySshTelnetServerEnabled':apSecuritySshTelnetServerEnabled,'apRadioInterfaceMgnt':apRadioInterfaceMgnt,'enterpriseApRadioTable':enterpriseApRadioTable,'enterpriseApRadioEntry':enterpriseApRadioEntry,_M:enterpriseApRadioIndex,'enterpriseApRadioAutoChannel':enterpriseApRadioAutoChannel,'enterpriseApRadioTransmitPower':enterpriseApRadioTransmitPower,'enterpriseApRadioTurboMode':enterpriseApRadioTurboMode,'enterpriseApRadioDataRate':enterpriseApRadioDataRate,'enterpriseApRadioGMode':enterpriseApRadioGMode,'enterpriseApRadioAntennaMode':enterpriseApRadioAntennaMode,'rogueApState':rogueApState,'rogueApInterval':rogueApInterval,'rogueApDuration':rogueApDuration,'rogueApScanNow':rogueApScanNow,'enterpriseApRadioAntennaModeControl':enterpriseApRadioAntennaModeControl,'enterpriseApRadioFixedAntennaType':enterpriseApRadioFixedAntennaType,'enterpriseApRadioAntennaID':enterpriseApRadioAntennaID,'enterpriseApRadioMulticastDataRate':enterpriseApRadioMulticastDataRate,'enterpriseApRadioAutoDataRate':enterpriseApRadioAutoDataRate,'enterpriseApRadioPreamble':enterpriseApRadioPreamble,'enterpriseApRadioSWRetryMode':enterpriseApRadioSWRetryMode,'enterpriseApVapRadioTable':enterpriseApVapRadioTable,'enterpriseApVapRadioEntry':enterpriseApVapRadioEntry,_r:enterpriseApVapRadioIndex,'enterpriseApVapRadioState':enterpriseApVapRadioState,'enterpriseApVapRadioSecureAccess':enterpriseApVapRadioSecureAccess,'enterpriseApVapRadioMaxAssoc':enterpriseApVapRadioMaxAssoc,'enterpriseApVapRadioTransmitKey':enterpriseApVapRadioTransmitKey,'enterpriseApVapRadioDescription':enterpriseApVapRadioDescription,'enterpriseApVapRadioDefefaultPriority':enterpriseApVapRadioDefefaultPriority,'enterpriseApRadioWdsTable':enterpriseApRadioWdsTable,'enterpriseApRadioWdsEntry':enterpriseApRadioWdsEntry,'wdsApRole':wdsApRole,'wdsApAckTimeout':wdsApAckTimeout,'enterpriseApRadioWdsPeerTable':enterpriseApRadioWdsPeerTable,'enterpriseApRadioWdsPeerEntry':enterpriseApRadioWdsPeerEntry,_s:wdsPeerIndex,'wdsPeerBssid':wdsPeerBssid,'wdsPeerRSSI':wdsPeerRSSI,'enterpriseApRadioWEPKeysTable':enterpriseApRadioWEPKeysTable,'enterpriseApRadioWEPKeysEntry':enterpriseApRadioWEPKeysEntry,_t:enterpriseApRadioWEPKeysIndex,'enterpriseApRadioWEPKeyType':enterpriseApRadioWEPKeyType,'enterpriseApRadioWEPKeyLength':enterpriseApRadioWEPKeyLength,'enterpriseApRadioAvAntennaListTable':enterpriseApRadioAvAntennaListTable,'enterpriseApRadioAvAntennaListEntry':enterpriseApRadioAvAntennaListEntry,_u:enterpriseApRadioAvAntennaIndex,'enterpriseApRadioAvAntennaId':enterpriseApRadioAvAntennaId,'enterpriseApRadioAvAntennaDesc':enterpriseApRadioAvAntennaDesc,'enterpriseApRadioAvChannelListTable':enterpriseApRadioAvChannelListTable,'enterpriseApRadioAvChannelListEntry':enterpriseApRadioAvChannelListEntry,_v:enterpriseApRadioAvChannelIndex,'enterpriseApRadioAvChannelNo':enterpriseApRadioAvChannelNo,'apEtherInterfaceMgnt':apEtherInterfaceMgnt,'apEtherNetConfig':apEtherNetConfig,'netConfigIPAddress':netConfigIPAddress,'netConfigSubnetMask':netConfigSubnetMask,'netConfigDefaultGateway':netConfigDefaultGateway,'netConfigHttpState':netConfigHttpState,'netConfigHttpPort':netConfigHttpPort,'netConfigHttpsState':netConfigHttpsState,'netConfigHttpsPort':netConfigHttpsPort,'netConfigDHCPState':netConfigDHCPState,'apFilterControlMgnt':apFilterControlMgnt,'apFilterControlBridge':apFilterControlBridge,'enterpriseApFilterControlAPManage':enterpriseApFilterControlAPManage,'enterpriseApFilterControlEthernet':enterpriseApFilterControlEthernet,'enterpriseApFilterProtocolTable':enterpriseApFilterProtocolTable,'enterpriseApFilterProtocolEntry':enterpriseApFilterProtocolEntry,_w:enterpriseApFilterProtocolIndex,'enterpriseApFilterProtocolName':enterpriseApFilterProtocolName,'enterpriseApFilterProtocolISODesignator':enterpriseApFilterProtocolISODesignator,'enterpriseApFilterProtocolState':enterpriseApFilterProtocolState,'apvGlobalIBSSRelayMode':apvGlobalIBSSRelayMode,'apvFilterControlTable':apvFilterControlTable,'apvFilterControlEntry':apvFilterControlEntry,_x:apvFilterControlIndex,'apvIBSSFilterControl':apvIBSSFilterControl,'apvAPManageFilterControl':apvAPManageFilterControl,'apVLANMgnt':apVLANMgnt,'apVLANMgntNativeId':apVLANMgntNativeId,'apVLANMgntState':apVLANMgntState,'apVLANMgntStateNextBoot':apVLANMgntStateNextBoot,'apNativeVlanTable':apNativeVlanTable,'apNativeVlanEntry':apNativeVlanEntry,_y:apNativeVlanIfIndex,_z:apNativeVlanSsidNumber,'apNativeVlanVlanId':apNativeVlanVlanId,'apNativeVlanState':apNativeVlanState,'apVLANMgntEtherUntaggedVlanId':apVLANMgntEtherUntaggedVlanId,'apAuthenticationMgnt':apAuthenticationMgnt,'apAuthenticationSetupEntry':apAuthenticationSetupEntry,'ap8021xState':ap8021xState,'ap8021xBroadcastKeyRefreshRate':ap8021xBroadcastKeyRefreshRate,'ap8021xSessionKeyRefreshRate':ap8021xSessionKeyRefreshRate,'ap8021xReauthenticationTimeout':ap8021xReauthenticationTimeout,'apAuthenticationMode':apAuthenticationMode,'apAuthenticationServerTable':apAuthenticationServerTable,'apAuthenticationServerEntry':apAuthenticationServerEntry,_A0:apAuthenticationServerIndex,'apAuthenticationServer':apAuthenticationServer,'apAuthenticationPort':apAuthenticationPort,'apAuthenticationKey':apAuthenticationKey,'apAuthenticationRetransmit':apAuthenticationRetransmit,'apAuthenticationTimeout':apAuthenticationTimeout,'apAuthenticationAcctPort':apAuthenticationAcctPort,'apAuthenticationAcctInterimUpdate':apAuthenticationAcctInterimUpdate,'apAuthenticationAcctState':apAuthenticationAcctState,'apAuthenticationSupplicantTable':apAuthenticationSupplicantTable,'apAuthenticationSupplicantEntry':apAuthenticationSupplicantEntry,_A1:ap8021xSuppIndex,'ap8021xSuppState':ap8021xSuppState,'ap8021xSuppUser':ap8021xSuppUser,'ap8021xSuppPasswd':ap8021xSuppPasswd,'apvAuthenticationSetupTable':apvAuthenticationSetupTable,'apvAuthenticationSetupEntry':apvAuthenticationSetupEntry,_A2:apv8021xIndex,'apv8021xState':apv8021xState,'apv8021xBroadcastKeyRefreshRate':apv8021xBroadcastKeyRefreshRate,'apv8021xSessionKeyRefreshRate':apv8021xSessionKeyRefreshRate,'apv8021xReauthenticationTimeout':apv8021xReauthenticationTimeout,'apvMACAuthenticationMode':apvMACAuthenticationMode,'apvMACAuthenticationTimeout':apvMACAuthenticationTimeout,'apvMACAuthenticationPasswd':apvMACAuthenticationPasswd,'apWStationSessionMgnt':apWStationSessionMgnt,'apWStationSessionTable':apWStationSessionTable,'apWStationSessionEntry':apWStationSessionEntry,_A3:apWStationSessionIfIndex,_A4:apWStationSessionStationAddres,'apWStationSessionAuthenticated':apWStationSessionAuthenticated,'apWStationSessionAssociated':apWStationSessionAssociated,'apWStationSessionIsForwarding':apWStationSessionIsForwarding,'apWStationSessionKeyType':apWStationSessionKeyType,'apWStationSessionAssociationId':apWStationSessionAssociationId,'apWStationSessionLastAuthenticatedTime':apWStationSessionLastAuthenticatedTime,'apWStationSessionAssociatedTime':apWStationSessionAssociatedTime,'apWStationSessionLastAssociatedTime':apWStationSessionLastAssociatedTime,'apWStationSessionLastDisassociatedTime':apWStationSessionLastDisassociatedTime,'apWStationSessionTxPacketCount':apWStationSessionTxPacketCount,'apWStationSessionRxPacketCount':apWStationSessionRxPacketCount,'apWStationSessionTxByteCount':apWStationSessionTxByteCount,'apWStationSessionRxByteCount':apWStationSessionRxByteCount,'apWStationSessionVlanID':apWStationSessionVlanID,'apRogueApMgnt':apRogueApMgnt,'rogueApDetectionTable':rogueApDetectionTable,'rogueApDetectionEntry':rogueApDetectionEntry,_A5:rogueApIndex,'rogueApBssid':rogueApBssid,'rogueApSsid':rogueApSsid,'rogueApPortNumber':rogueApPortNumber,'rogueApChannelNumber':rogueApChannelNumber,'rogueApRSSIValue':rogueApRSSIValue,'apRougeApControl':apRougeApControl,'rogueApRADIUSAuthenticate':rogueApRADIUSAuthenticate,'rogueApClear':rogueApClear,'apAdminMgnt':apAdminMgnt,'apAdminUsername':apAdminUsername,'appAdminPassword':appAdminPassword,'apResetMgt':apResetMgt,'apRestartOpCodeFile':apRestartOpCodeFile,'apRestartControl':apRestartControl,'apSNTPMgnt':apSNTPMgnt,'apSNTPState':apSNTPState,'apSNTPPrimaryServer':apSNTPPrimaryServer,'apSNTPSecondaryServer':apSNTPSecondaryServer,'apSNTPTimezone':apSNTPTimezone,'apSNTPDST':apSNTPDST,'apSNTPDSTStartMonth':apSNTPDSTStartMonth,'apSNTPDSTStartDay':apSNTPDSTStartDay,'apSNTPDSTEndMonth':apSNTPDSTEndMonth,'apSNTPDSTEndDay':apSNTPDSTEndDay,'apDNSMgnt':apDNSMgnt,'apDNSPrimaryServer':apDNSPrimaryServer,'apDNSSecondaryServer':apDNSSecondaryServer,'apIappMgnt':apIappMgnt,'apIappEnabled':apIappEnabled,'apSyslogConfigMgnt':apSyslogConfigMgnt,'apLogConfigState':apLogConfigState,'apSyslogConsoleState':apSyslogConsoleState,'apSyslogLevel':apSyslogLevel,'apSyslogServerTable':apSyslogServerTable,'apSyslogServerEntry':apSyslogServerEntry,_A6:apSyslogServerIndex,'apSyslogServerState':apSyslogServerState,'apSyslogServerIPAddress':apSyslogServerIPAddress,'apSyslogServerPort':apSyslogServerPort,'apEventLogMgnt':apEventLogMgnt,'apEventLogTable':apEventLogTable,'apEventLogEntry':apEventLogEntry,_A7:apEventLogIndex,'apEventLogMessage':apEventLogMessage,'apEventLogClear':apEventLogClear,'apWSLSupportMgnt':apWSLSupportMgnt,'apWSLSupportControl':apWSLSupportControl,'apWSLSupportMasterAddress':apWSLSupportMasterAddress,'apWSLSupportSecondaryAddress':apWSLSupportSecondaryAddress,'apWSLSupportPort':apWSLSupportPort,'apWSLSupportHeartbeatInterval':apWSLSupportHeartbeatInterval,'apWSLSupportHeartbeatLastChange':apWSLSupportHeartbeatLastChange,'apWSLSupportOperationMode':apWSLSupportOperationMode,'apWSLSupportRxThreshold':apWSLSupportRxThreshold,'apWSLSupportControlStatus':apWSLSupportControlStatus,'apWSLRFAreaPollControl':apWSLRFAreaPollControl,'apWSLRFAreaPollControlStatus':apWSLRFAreaPollControlStatus,'apWMMMgnt':apWMMMgnt,'apWMMControlTable':apWMMControlTable,'apWMMControlEntry':apWMMControlEntry,'apWMMState':apWMMState,'apWMMBssParamTable':apWMMBssParamTable,'apWMMBssParamEntry':apWMMBssParamEntry,_A8:apWMMBssParamIndex,'apWMMBssParamCWmin':apWMMBssParamCWmin,'apWMMBssParamCWmax':apWMMBssParamCWmax,'apWMMBssParamAIFSN':apWMMBssParamAIFSN,'apWMMBssParamTXOPLimit':apWMMBssParamTXOPLimit,'apWMMBssParamAdmissionControl':apWMMBssParamAdmissionControl,'apWMMApParamTable':apWMMApParamTable,'apWMMApParamEntry':apWMMApParamEntry,_A9:apWMMApParamIndex,'apWMMApParamCWmin':apWMMApParamCWmin,'apWMMApParamCWmax':apWMMApParamCWmax,'apWMMApParamAIFSN':apWMMApParamAIFSN,'apWMMApParamTXOPLimit':apWMMApParamTXOPLimit,'apWMMApParamAdmissionControl':apWMMApParamAdmissionControl,'apNotificationTrapTree':apNotificationTrapTree,'apNotificationObjects':apNotificationObjects,'apNotificationDot11MacAddr':apNotificationDot11MacAddr,_J:apNotificationDot11Station,_AA:apNotificationDot11RequestType,_AB:apNotificationDot11ReasonCode,_R:apNotificationDot11IpAddress,'apNotificationDot11AuthenticatorMacAddr':apNotificationDot11AuthenticatorMacAddr,'apNotificationTrapObjects':apNotificationTrapObjects,'sysSystemUp':sysSystemUp,'sysSystemDown':sysSystemDown,'sysRadiusServerChanged':sysRadiusServerChanged,'dot11StationAssociation':dot11StationAssociation,'dot11StationReAssociation':dot11StationReAssociation,'dot11StationAuthentication':dot11StationAuthentication,'dot11StationRequestFail':dot11StationRequestFail,'dot1xMacAddrAuthSuccess':dot1xMacAddrAuthSuccess,'dot1xMacAddrAuthFail':dot1xMacAddrAuthFail,'dot1xAuthNotInitiated':dot1xAuthNotInitiated,'dot1xAuthSuccess':dot1xAuthSuccess,'dot1xAuthFail':dot1xAuthFail,'localMacAddrAuthSuccess':localMacAddrAuthSuccess,'localMacAddrAuthFail':localMacAddrAuthFail,'pppLogonFail':pppLogonFail,'iappStationRoamedFrom':iappStationRoamedFrom,'iappStationRoamedTo':iappStationRoamedTo,'iappContextDataSent':iappContextDataSent,'sntpServerFail':sntpServerFail,'dot11InterfaceAFail':dot11InterfaceAFail,'dot11InterfaceGFail':dot11InterfaceGFail,'dot11WirelessSTPDetection':dot11WirelessSTPDetection})