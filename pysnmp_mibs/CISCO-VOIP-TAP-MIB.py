_P='ciscoVoIpTapStreamGroup'
_O='cvoiptapStreamRowStatus'
_N='cvoiptapStreamCCMediationDevice'
_M='cvoiptapStreamMatchType'
_L='cvoiptapStreamMatch'
_K='cvoiptapStreamType'
_J='cvoiptapStreamId'
_I='cvoiptapStreamCapabilities'
_H='usernameOrNumber'
_G='cTap2StreamIndex'
_F='cTap2MediationContentId'
_E='Integer32'
_D='CISCO-TAP2-MIB'
_C='read-create'
_B='CISCO-VOIP-TAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cTap2MediationContentId,cTap2StreamIndex=mibBuilder.importSymbols(_D,_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoVoIpTapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,716))
if mibBuilder.loadTexts:ciscoVoIpTapMIB.setRevisions(('2009-10-01 00:00',))
class CvoipWarrantId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
class CvoipSubscriberId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CiscoVoIpTapMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVoIpTapMIBNotifs=_CiscoVoIpTapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,716,0))
_CiscoVoIpTapMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVoIpTapMIBObjects=_CiscoVoIpTapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,716,1))
_CvoiptapStreamEncodePacket_ObjectIdentity=ObjectIdentity
cvoiptapStreamEncodePacket=_CvoiptapStreamEncodePacket_ObjectIdentity((1,3,6,1,4,1,9,9,716,1,1))
class _CvoiptapStreamCapabilities_Type(Bits):namedValues=NamedValues(*(('tapEnable',0),(_H,1),('uri',2)))
_CvoiptapStreamCapabilities_Type.__name__='Bits'
_CvoiptapStreamCapabilities_Object=MibScalar
cvoiptapStreamCapabilities=_CvoiptapStreamCapabilities_Object((1,3,6,1,4,1,9,9,716,1,1,1),_CvoiptapStreamCapabilities_Type())
cvoiptapStreamCapabilities.setMaxAccess('read-only')
if mibBuilder.loadTexts:cvoiptapStreamCapabilities.setStatus(_A)
_CvoiptapStreamTable_Object=MibTable
cvoiptapStreamTable=_CvoiptapStreamTable_Object((1,3,6,1,4,1,9,9,716,1,1,2))
if mibBuilder.loadTexts:cvoiptapStreamTable.setStatus(_A)
_CvoiptapStreamEntry_Object=MibTableRow
cvoiptapStreamEntry=_CvoiptapStreamEntry_Object((1,3,6,1,4,1,9,9,716,1,1,2,1))
cvoiptapStreamEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:cvoiptapStreamEntry.setStatus(_A)
_CvoiptapStreamId_Type=CvoipWarrantId
_CvoiptapStreamId_Object=MibTableColumn
cvoiptapStreamId=_CvoiptapStreamId_Object((1,3,6,1,4,1,9,9,716,1,1,2,1,1),_CvoiptapStreamId_Type())
cvoiptapStreamId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvoiptapStreamId.setStatus(_A)
class _CvoiptapStreamType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pen',1),('trace',2),('penAndTrace',3),('intercept',4)))
_CvoiptapStreamType_Type.__name__=_E
_CvoiptapStreamType_Object=MibTableColumn
cvoiptapStreamType=_CvoiptapStreamType_Object((1,3,6,1,4,1,9,9,716,1,1,2,1,2),_CvoiptapStreamType_Type())
cvoiptapStreamType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvoiptapStreamType.setStatus(_A)
_CvoiptapStreamMatch_Type=CvoipSubscriberId
_CvoiptapStreamMatch_Object=MibTableColumn
cvoiptapStreamMatch=_CvoiptapStreamMatch_Object((1,3,6,1,4,1,9,9,716,1,1,2,1,3),_CvoiptapStreamMatch_Type())
cvoiptapStreamMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:cvoiptapStreamMatch.setStatus(_A)
class _CvoiptapStreamMatchType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('uri',2)))
_CvoiptapStreamMatchType_Type.__name__=_E
_CvoiptapStreamMatchType_Object=MibTableColumn
cvoiptapStreamMatchType=_CvoiptapStreamMatchType_Object((1,3,6,1,4,1,9,9,716,1,1,2,1,4),_CvoiptapStreamMatchType_Type())
cvoiptapStreamMatchType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvoiptapStreamMatchType.setStatus(_A)
_CvoiptapStreamCCMediationDevice_Type=Integer32
_CvoiptapStreamCCMediationDevice_Object=MibTableColumn
cvoiptapStreamCCMediationDevice=_CvoiptapStreamCCMediationDevice_Object((1,3,6,1,4,1,9,9,716,1,1,2,1,5),_CvoiptapStreamCCMediationDevice_Type())
cvoiptapStreamCCMediationDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:cvoiptapStreamCCMediationDevice.setStatus(_A)
_CvoiptapStreamRowStatus_Type=RowStatus
_CvoiptapStreamRowStatus_Object=MibTableColumn
cvoiptapStreamRowStatus=_CvoiptapStreamRowStatus_Object((1,3,6,1,4,1,9,9,716,1,1,2,1,6),_CvoiptapStreamRowStatus_Type())
cvoiptapStreamRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvoiptapStreamRowStatus.setStatus(_A)
_CiscoVoIpTapMIBConform_ObjectIdentity=ObjectIdentity
ciscoVoIpTapMIBConform=_CiscoVoIpTapMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,716,2))
_CiscoVoIpTapMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVoIpTapMIBCompliances=_CiscoVoIpTapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,716,2,1))
_CiscoVoIpTapMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVoIpTapMIBGroups=_CiscoVoIpTapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,716,2,2))
ciscoVoIpTapStreamGroup=ObjectGroup((1,3,6,1,4,1,9,9,716,2,2,1))
ciscoVoIpTapStreamGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoVoIpTapStreamGroup.setStatus(_A)
ciscoVoIpTapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,716,2,1,1))
ciscoVoIpTapMIBCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:ciscoVoIpTapMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CvoipWarrantId':CvoipWarrantId,'CvoipSubscriberId':CvoipSubscriberId,'ciscoVoIpTapMIB':ciscoVoIpTapMIB,'ciscoVoIpTapMIBNotifs':ciscoVoIpTapMIBNotifs,'ciscoVoIpTapMIBObjects':ciscoVoIpTapMIBObjects,'cvoiptapStreamEncodePacket':cvoiptapStreamEncodePacket,_I:cvoiptapStreamCapabilities,'cvoiptapStreamTable':cvoiptapStreamTable,'cvoiptapStreamEntry':cvoiptapStreamEntry,_J:cvoiptapStreamId,_K:cvoiptapStreamType,_L:cvoiptapStreamMatch,_M:cvoiptapStreamMatchType,_N:cvoiptapStreamCCMediationDevice,_O:cvoiptapStreamRowStatus,'ciscoVoIpTapMIBConform':ciscoVoIpTapMIBConform,'ciscoVoIpTapMIBCompliances':ciscoVoIpTapMIBCompliances,'ciscoVoIpTapMIBCompliance':ciscoVoIpTapMIBCompliance,'ciscoVoIpTapMIBGroups':ciscoVoIpTapMIBGroups,_P:ciscoVoIpTapStreamGroup})