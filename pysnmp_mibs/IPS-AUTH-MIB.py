_g='ipsAuthIdentCredAttributesGroup'
_f='ipsAuthIdentAddrAttributesGroup'
_e='ipsAuthIdentNameAttributesGroup'
_d='ipsAuthIdentAttributesGroup'
_c='ipsAuthInstanceAttributesGroup'
_b='ipsAuthCredSrpRowStatus'
_a='ipsAuthCredSrpPassword'
_Z='ipsAuthCredSrpUserName'
_Y='ipsAuthCredChapRowStatus'
_X='ipsAuthCredChapPassword'
_W='ipsAuthCredChapUserName'
_V='ipsAuthCredRowStatus'
_U='ipsAuthCredAuthMethod'
_T='ipsAuthIdentAddrRowStatus'
_S='ipsAuthIdentAddrEnd'
_R='ipsAuthIdentAddrStart'
_Q='ipsAuthIdentAddrType'
_P='ipsAuthIdentNameRowStatus'
_O='ipsAuthIdentName'
_N='ipsAuthIdentRowStatus'
_M='ipsAuthIdentDescription'
_L='ipsAuthInstDescr'
_K='ipsAuthIdentAddrIndex'
_J='ipsAuthIdentNameIndex'
_I='ipsAuthCredIndex'
_H='not-accessible'
_G='Unsigned32'
_F='ipsAuthIdentIndex'
_E='ipsAuthInstIndex'
_D='OctetString'
_C='read-create'
_B='IPS-AUTH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ipsAuthModule=ModuleIdentity((1,3,6,1,3,99999))
if mibBuilder.loadTexts:ipsAuthModule.setRevisions(('2002-06-26 00:00',))
class IpsAuthAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthObjects_ObjectIdentity=ObjectIdentity
ipsAuthObjects=_IpsAuthObjects_ObjectIdentity((1,3,6,1,3,99999,1))
_IpsAuthDescriptors_ObjectIdentity=ObjectIdentity
ipsAuthDescriptors=_IpsAuthDescriptors_ObjectIdentity((1,3,6,1,3,99999,1,1))
_IpsAuthMethodTypes_ObjectIdentity=ObjectIdentity
ipsAuthMethodTypes=_IpsAuthMethodTypes_ObjectIdentity((1,3,6,1,3,99999,1,1,1))
_IpsAuthMethodNone_ObjectIdentity=ObjectIdentity
ipsAuthMethodNone=_IpsAuthMethodNone_ObjectIdentity((1,3,6,1,3,99999,1,1,1,1))
if mibBuilder.loadTexts:ipsAuthMethodNone.setStatus(_A)
_IpsAuthMethodSrp_ObjectIdentity=ObjectIdentity
ipsAuthMethodSrp=_IpsAuthMethodSrp_ObjectIdentity((1,3,6,1,3,99999,1,1,1,2))
if mibBuilder.loadTexts:ipsAuthMethodSrp.setStatus(_A)
_IpsAuthMethodChap_ObjectIdentity=ObjectIdentity
ipsAuthMethodChap=_IpsAuthMethodChap_ObjectIdentity((1,3,6,1,3,99999,1,1,1,3))
if mibBuilder.loadTexts:ipsAuthMethodChap.setStatus(_A)
_IpsAuthInstance_ObjectIdentity=ObjectIdentity
ipsAuthInstance=_IpsAuthInstance_ObjectIdentity((1,3,6,1,3,99999,1,2))
_IpsAuthInstanceAttributesTable_Object=MibTable
ipsAuthInstanceAttributesTable=_IpsAuthInstanceAttributesTable_Object((1,3,6,1,3,99999,1,2,2))
if mibBuilder.loadTexts:ipsAuthInstanceAttributesTable.setStatus(_A)
_IpsAuthInstanceAttributesEntry_Object=MibTableRow
ipsAuthInstanceAttributesEntry=_IpsAuthInstanceAttributesEntry_Object((1,3,6,1,3,99999,1,2,2,1))
ipsAuthInstanceAttributesEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ipsAuthInstanceAttributesEntry.setStatus(_A)
class _IpsAuthInstIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpsAuthInstIndex_Type.__name__=_G
_IpsAuthInstIndex_Object=MibTableColumn
ipsAuthInstIndex=_IpsAuthInstIndex_Object((1,3,6,1,3,99999,1,2,2,1,1),_IpsAuthInstIndex_Type())
ipsAuthInstIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipsAuthInstIndex.setStatus(_A)
class _IpsAuthInstDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthInstDescr_Type.__name__=_D
_IpsAuthInstDescr_Object=MibTableColumn
ipsAuthInstDescr=_IpsAuthInstDescr_Object((1,3,6,1,3,99999,1,2,2,1,2),_IpsAuthInstDescr_Type())
ipsAuthInstDescr.setMaxAccess('read-write')
if mibBuilder.loadTexts:ipsAuthInstDescr.setStatus(_A)
_IpsAuthIdentity_ObjectIdentity=ObjectIdentity
ipsAuthIdentity=_IpsAuthIdentity_ObjectIdentity((1,3,6,1,3,99999,1,3))
_IpsAuthIdentAttributesTable_Object=MibTable
ipsAuthIdentAttributesTable=_IpsAuthIdentAttributesTable_Object((1,3,6,1,3,99999,1,3,1))
if mibBuilder.loadTexts:ipsAuthIdentAttributesTable.setStatus(_A)
_IpsAuthIdentAttributesEntry_Object=MibTableRow
ipsAuthIdentAttributesEntry=_IpsAuthIdentAttributesEntry_Object((1,3,6,1,3,99999,1,3,1,1))
ipsAuthIdentAttributesEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:ipsAuthIdentAttributesEntry.setStatus(_A)
class _IpsAuthIdentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpsAuthIdentIndex_Type.__name__=_G
_IpsAuthIdentIndex_Object=MibTableColumn
ipsAuthIdentIndex=_IpsAuthIdentIndex_Object((1,3,6,1,3,99999,1,3,1,1,1),_IpsAuthIdentIndex_Type())
ipsAuthIdentIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipsAuthIdentIndex.setStatus(_A)
class _IpsAuthIdentDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthIdentDescription_Type.__name__=_D
_IpsAuthIdentDescription_Object=MibTableColumn
ipsAuthIdentDescription=_IpsAuthIdentDescription_Object((1,3,6,1,3,99999,1,3,1,1,2),_IpsAuthIdentDescription_Type())
ipsAuthIdentDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentDescription.setStatus(_A)
_IpsAuthIdentRowStatus_Type=RowStatus
_IpsAuthIdentRowStatus_Object=MibTableColumn
ipsAuthIdentRowStatus=_IpsAuthIdentRowStatus_Object((1,3,6,1,3,99999,1,3,1,1,3),_IpsAuthIdentRowStatus_Type())
ipsAuthIdentRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentRowStatus.setStatus(_A)
_IpsAuthIdentityName_ObjectIdentity=ObjectIdentity
ipsAuthIdentityName=_IpsAuthIdentityName_ObjectIdentity((1,3,6,1,3,99999,1,4))
_IpsAuthIdentNameAttributesTable_Object=MibTable
ipsAuthIdentNameAttributesTable=_IpsAuthIdentNameAttributesTable_Object((1,3,6,1,3,99999,1,4,1))
if mibBuilder.loadTexts:ipsAuthIdentNameAttributesTable.setStatus(_A)
_IpsAuthIdentNameAttributesEntry_Object=MibTableRow
ipsAuthIdentNameAttributesEntry=_IpsAuthIdentNameAttributesEntry_Object((1,3,6,1,3,99999,1,4,1,1))
ipsAuthIdentNameAttributesEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:ipsAuthIdentNameAttributesEntry.setStatus(_A)
class _IpsAuthIdentNameIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpsAuthIdentNameIndex_Type.__name__=_G
_IpsAuthIdentNameIndex_Object=MibTableColumn
ipsAuthIdentNameIndex=_IpsAuthIdentNameIndex_Object((1,3,6,1,3,99999,1,4,1,1,1),_IpsAuthIdentNameIndex_Type())
ipsAuthIdentNameIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipsAuthIdentNameIndex.setStatus(_A)
class _IpsAuthIdentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthIdentName_Type.__name__=_D
_IpsAuthIdentName_Object=MibTableColumn
ipsAuthIdentName=_IpsAuthIdentName_Object((1,3,6,1,3,99999,1,4,1,1,2),_IpsAuthIdentName_Type())
ipsAuthIdentName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentName.setStatus(_A)
_IpsAuthIdentNameRowStatus_Type=RowStatus
_IpsAuthIdentNameRowStatus_Object=MibTableColumn
ipsAuthIdentNameRowStatus=_IpsAuthIdentNameRowStatus_Object((1,3,6,1,3,99999,1,4,1,1,3),_IpsAuthIdentNameRowStatus_Type())
ipsAuthIdentNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentNameRowStatus.setStatus(_A)
_IpsAuthIdentityAddress_ObjectIdentity=ObjectIdentity
ipsAuthIdentityAddress=_IpsAuthIdentityAddress_ObjectIdentity((1,3,6,1,3,99999,1,5))
_IpsAuthIdentAddrAttributesTable_Object=MibTable
ipsAuthIdentAddrAttributesTable=_IpsAuthIdentAddrAttributesTable_Object((1,3,6,1,3,99999,1,5,1))
if mibBuilder.loadTexts:ipsAuthIdentAddrAttributesTable.setStatus(_A)
_IpsAuthIdentAddrAttributesEntry_Object=MibTableRow
ipsAuthIdentAddrAttributesEntry=_IpsAuthIdentAddrAttributesEntry_Object((1,3,6,1,3,99999,1,5,1,1))
ipsAuthIdentAddrAttributesEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:ipsAuthIdentAddrAttributesEntry.setStatus(_A)
class _IpsAuthIdentAddrIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpsAuthIdentAddrIndex_Type.__name__=_G
_IpsAuthIdentAddrIndex_Object=MibTableColumn
ipsAuthIdentAddrIndex=_IpsAuthIdentAddrIndex_Object((1,3,6,1,3,99999,1,5,1,1,1),_IpsAuthIdentAddrIndex_Type())
ipsAuthIdentAddrIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipsAuthIdentAddrIndex.setStatus(_A)
_IpsAuthIdentAddrType_Type=Integer32
_IpsAuthIdentAddrType_Object=MibTableColumn
ipsAuthIdentAddrType=_IpsAuthIdentAddrType_Object((1,3,6,1,3,99999,1,5,1,1,2),_IpsAuthIdentAddrType_Type())
ipsAuthIdentAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentAddrType.setStatus(_A)
_IpsAuthIdentAddrStart_Type=IpsAuthAddress
_IpsAuthIdentAddrStart_Object=MibTableColumn
ipsAuthIdentAddrStart=_IpsAuthIdentAddrStart_Object((1,3,6,1,3,99999,1,5,1,1,3),_IpsAuthIdentAddrStart_Type())
ipsAuthIdentAddrStart.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentAddrStart.setStatus(_A)
_IpsAuthIdentAddrEnd_Type=IpsAuthAddress
_IpsAuthIdentAddrEnd_Object=MibTableColumn
ipsAuthIdentAddrEnd=_IpsAuthIdentAddrEnd_Object((1,3,6,1,3,99999,1,5,1,1,4),_IpsAuthIdentAddrEnd_Type())
ipsAuthIdentAddrEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentAddrEnd.setStatus(_A)
_IpsAuthIdentAddrRowStatus_Type=RowStatus
_IpsAuthIdentAddrRowStatus_Object=MibTableColumn
ipsAuthIdentAddrRowStatus=_IpsAuthIdentAddrRowStatus_Object((1,3,6,1,3,99999,1,5,1,1,5),_IpsAuthIdentAddrRowStatus_Type())
ipsAuthIdentAddrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthIdentAddrRowStatus.setStatus(_A)
_IpsAuthCredential_ObjectIdentity=ObjectIdentity
ipsAuthCredential=_IpsAuthCredential_ObjectIdentity((1,3,6,1,3,99999,1,6))
_IpsAuthCredentialAttributesTable_Object=MibTable
ipsAuthCredentialAttributesTable=_IpsAuthCredentialAttributesTable_Object((1,3,6,1,3,99999,1,6,1))
if mibBuilder.loadTexts:ipsAuthCredentialAttributesTable.setStatus(_A)
_IpsAuthCredentialAttributesEntry_Object=MibTableRow
ipsAuthCredentialAttributesEntry=_IpsAuthCredentialAttributesEntry_Object((1,3,6,1,3,99999,1,6,1,1))
ipsAuthCredentialAttributesEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:ipsAuthCredentialAttributesEntry.setStatus(_A)
class _IpsAuthCredIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpsAuthCredIndex_Type.__name__=_G
_IpsAuthCredIndex_Object=MibTableColumn
ipsAuthCredIndex=_IpsAuthCredIndex_Object((1,3,6,1,3,99999,1,6,1,1,1),_IpsAuthCredIndex_Type())
ipsAuthCredIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipsAuthCredIndex.setStatus(_A)
_IpsAuthCredAuthMethod_Type=Integer32
_IpsAuthCredAuthMethod_Object=MibTableColumn
ipsAuthCredAuthMethod=_IpsAuthCredAuthMethod_Object((1,3,6,1,3,99999,1,6,1,1,2),_IpsAuthCredAuthMethod_Type())
ipsAuthCredAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredAuthMethod.setStatus(_A)
_IpsAuthCredRowStatus_Type=RowStatus
_IpsAuthCredRowStatus_Object=MibTableColumn
ipsAuthCredRowStatus=_IpsAuthCredRowStatus_Object((1,3,6,1,3,99999,1,6,1,1,3),_IpsAuthCredRowStatus_Type())
ipsAuthCredRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredRowStatus.setStatus(_A)
_IpsAuthCredChap_ObjectIdentity=ObjectIdentity
ipsAuthCredChap=_IpsAuthCredChap_ObjectIdentity((1,3,6,1,3,99999,1,7))
_IpsAuthCredChapAttributesTable_Object=MibTable
ipsAuthCredChapAttributesTable=_IpsAuthCredChapAttributesTable_Object((1,3,6,1,3,99999,1,7,1))
if mibBuilder.loadTexts:ipsAuthCredChapAttributesTable.setStatus(_A)
_IpsAuthCredChapAttributesEntry_Object=MibTableRow
ipsAuthCredChapAttributesEntry=_IpsAuthCredChapAttributesEntry_Object((1,3,6,1,3,99999,1,7,1,1))
ipsAuthCredChapAttributesEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:ipsAuthCredChapAttributesEntry.setStatus(_A)
class _IpsAuthCredChapUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthCredChapUserName_Type.__name__=_D
_IpsAuthCredChapUserName_Object=MibTableColumn
ipsAuthCredChapUserName=_IpsAuthCredChapUserName_Object((1,3,6,1,3,99999,1,7,1,1,1),_IpsAuthCredChapUserName_Type())
ipsAuthCredChapUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredChapUserName.setStatus(_A)
class _IpsAuthCredChapPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthCredChapPassword_Type.__name__=_D
_IpsAuthCredChapPassword_Object=MibTableColumn
ipsAuthCredChapPassword=_IpsAuthCredChapPassword_Object((1,3,6,1,3,99999,1,7,1,1,2),_IpsAuthCredChapPassword_Type())
ipsAuthCredChapPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredChapPassword.setStatus(_A)
_IpsAuthCredChapRowStatus_Type=RowStatus
_IpsAuthCredChapRowStatus_Object=MibTableColumn
ipsAuthCredChapRowStatus=_IpsAuthCredChapRowStatus_Object((1,3,6,1,3,99999,1,7,1,1,3),_IpsAuthCredChapRowStatus_Type())
ipsAuthCredChapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredChapRowStatus.setStatus(_A)
_IpsAuthCredSrp_ObjectIdentity=ObjectIdentity
ipsAuthCredSrp=_IpsAuthCredSrp_ObjectIdentity((1,3,6,1,3,99999,1,8))
_IpsAuthCredSrpAttributesTable_Object=MibTable
ipsAuthCredSrpAttributesTable=_IpsAuthCredSrpAttributesTable_Object((1,3,6,1,3,99999,1,8,1))
if mibBuilder.loadTexts:ipsAuthCredSrpAttributesTable.setStatus(_A)
_IpsAuthCredSrpAttributesEntry_Object=MibTableRow
ipsAuthCredSrpAttributesEntry=_IpsAuthCredSrpAttributesEntry_Object((1,3,6,1,3,99999,1,8,1,1))
ipsAuthCredSrpAttributesEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:ipsAuthCredSrpAttributesEntry.setStatus(_A)
class _IpsAuthCredSrpUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthCredSrpUserName_Type.__name__=_D
_IpsAuthCredSrpUserName_Object=MibTableColumn
ipsAuthCredSrpUserName=_IpsAuthCredSrpUserName_Object((1,3,6,1,3,99999,1,8,1,1,1),_IpsAuthCredSrpUserName_Type())
ipsAuthCredSrpUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredSrpUserName.setStatus(_A)
class _IpsAuthCredSrpPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IpsAuthCredSrpPassword_Type.__name__=_D
_IpsAuthCredSrpPassword_Object=MibTableColumn
ipsAuthCredSrpPassword=_IpsAuthCredSrpPassword_Object((1,3,6,1,3,99999,1,8,1,1,2),_IpsAuthCredSrpPassword_Type())
ipsAuthCredSrpPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredSrpPassword.setStatus(_A)
_IpsAuthCredSrpRowStatus_Type=RowStatus
_IpsAuthCredSrpRowStatus_Object=MibTableColumn
ipsAuthCredSrpRowStatus=_IpsAuthCredSrpRowStatus_Object((1,3,6,1,3,99999,1,8,1,1,3),_IpsAuthCredSrpRowStatus_Type())
ipsAuthCredSrpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsAuthCredSrpRowStatus.setStatus(_A)
_IpsAuthNotifications_ObjectIdentity=ObjectIdentity
ipsAuthNotifications=_IpsAuthNotifications_ObjectIdentity((1,3,6,1,3,99999,2))
_IpsAuthConformance_ObjectIdentity=ObjectIdentity
ipsAuthConformance=_IpsAuthConformance_ObjectIdentity((1,3,6,1,3,99999,3))
_IpsAuthGroups_ObjectIdentity=ObjectIdentity
ipsAuthGroups=_IpsAuthGroups_ObjectIdentity((1,3,6,1,3,99999,3,1))
_IpsAuthCompliances_ObjectIdentity=ObjectIdentity
ipsAuthCompliances=_IpsAuthCompliances_ObjectIdentity((1,3,6,1,3,99999,3,2))
ipsAuthInstanceAttributesGroup=ObjectGroup((1,3,6,1,3,99999,3,1,1))
ipsAuthInstanceAttributesGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:ipsAuthInstanceAttributesGroup.setStatus(_A)
ipsAuthIdentAttributesGroup=ObjectGroup((1,3,6,1,3,99999,3,1,2))
ipsAuthIdentAttributesGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ipsAuthIdentAttributesGroup.setStatus(_A)
ipsAuthIdentNameAttributesGroup=ObjectGroup((1,3,6,1,3,99999,3,1,3))
ipsAuthIdentNameAttributesGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ipsAuthIdentNameAttributesGroup.setStatus(_A)
ipsAuthIdentAddrAttributesGroup=ObjectGroup((1,3,6,1,3,99999,3,1,4))
ipsAuthIdentAddrAttributesGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ipsAuthIdentAddrAttributesGroup.setStatus(_A)
ipsAuthIdentCredAttributesGroup=ObjectGroup((1,3,6,1,3,99999,3,1,5))
ipsAuthIdentCredAttributesGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ipsAuthIdentCredAttributesGroup.setStatus(_A)
ipsAuthIdentChapAttrGroup=ObjectGroup((1,3,6,1,3,99999,3,1,6))
ipsAuthIdentChapAttrGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ipsAuthIdentChapAttrGroup.setStatus(_A)
ipsAuthIdentSrpAttrGroup=ObjectGroup((1,3,6,1,3,99999,3,1,7))
ipsAuthIdentSrpAttrGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ipsAuthIdentSrpAttrGroup.setStatus(_A)
ipsAuthComplianceV1=ModuleCompliance((1,3,6,1,3,99999,3,2,1))
ipsAuthComplianceV1.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ipsAuthComplianceV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IpsAuthAddress':IpsAuthAddress,'ipsAuthModule':ipsAuthModule,'ipsAuthObjects':ipsAuthObjects,'ipsAuthDescriptors':ipsAuthDescriptors,'ipsAuthMethodTypes':ipsAuthMethodTypes,'ipsAuthMethodNone':ipsAuthMethodNone,'ipsAuthMethodSrp':ipsAuthMethodSrp,'ipsAuthMethodChap':ipsAuthMethodChap,'ipsAuthInstance':ipsAuthInstance,'ipsAuthInstanceAttributesTable':ipsAuthInstanceAttributesTable,'ipsAuthInstanceAttributesEntry':ipsAuthInstanceAttributesEntry,_E:ipsAuthInstIndex,_L:ipsAuthInstDescr,'ipsAuthIdentity':ipsAuthIdentity,'ipsAuthIdentAttributesTable':ipsAuthIdentAttributesTable,'ipsAuthIdentAttributesEntry':ipsAuthIdentAttributesEntry,_F:ipsAuthIdentIndex,_M:ipsAuthIdentDescription,_N:ipsAuthIdentRowStatus,'ipsAuthIdentityName':ipsAuthIdentityName,'ipsAuthIdentNameAttributesTable':ipsAuthIdentNameAttributesTable,'ipsAuthIdentNameAttributesEntry':ipsAuthIdentNameAttributesEntry,_J:ipsAuthIdentNameIndex,_O:ipsAuthIdentName,_P:ipsAuthIdentNameRowStatus,'ipsAuthIdentityAddress':ipsAuthIdentityAddress,'ipsAuthIdentAddrAttributesTable':ipsAuthIdentAddrAttributesTable,'ipsAuthIdentAddrAttributesEntry':ipsAuthIdentAddrAttributesEntry,_K:ipsAuthIdentAddrIndex,_Q:ipsAuthIdentAddrType,_R:ipsAuthIdentAddrStart,_S:ipsAuthIdentAddrEnd,_T:ipsAuthIdentAddrRowStatus,'ipsAuthCredential':ipsAuthCredential,'ipsAuthCredentialAttributesTable':ipsAuthCredentialAttributesTable,'ipsAuthCredentialAttributesEntry':ipsAuthCredentialAttributesEntry,_I:ipsAuthCredIndex,_U:ipsAuthCredAuthMethod,_V:ipsAuthCredRowStatus,'ipsAuthCredChap':ipsAuthCredChap,'ipsAuthCredChapAttributesTable':ipsAuthCredChapAttributesTable,'ipsAuthCredChapAttributesEntry':ipsAuthCredChapAttributesEntry,_W:ipsAuthCredChapUserName,_X:ipsAuthCredChapPassword,_Y:ipsAuthCredChapRowStatus,'ipsAuthCredSrp':ipsAuthCredSrp,'ipsAuthCredSrpAttributesTable':ipsAuthCredSrpAttributesTable,'ipsAuthCredSrpAttributesEntry':ipsAuthCredSrpAttributesEntry,_Z:ipsAuthCredSrpUserName,_a:ipsAuthCredSrpPassword,_b:ipsAuthCredSrpRowStatus,'ipsAuthNotifications':ipsAuthNotifications,'ipsAuthConformance':ipsAuthConformance,'ipsAuthGroups':ipsAuthGroups,_c:ipsAuthInstanceAttributesGroup,_d:ipsAuthIdentAttributesGroup,_e:ipsAuthIdentNameAttributesGroup,_f:ipsAuthIdentAddrAttributesGroup,_g:ipsAuthIdentCredAttributesGroup,'ipsAuthIdentChapAttrGroup':ipsAuthIdentChapAttrGroup,'ipsAuthIdentSrpAttrGroup':ipsAuthIdentSrpAttrGroup,'ipsAuthCompliances':ipsAuthCompliances,'ipsAuthComplianceV1':ipsAuthComplianceV1})