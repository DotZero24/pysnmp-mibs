_b='cienaWsLicenseGroup'
_a='cwsLicenseServerNumLicenseServers'
_Z='cwsLicenseServerHostAddress'
_Y='cwsLicenseLicenseslistNotice'
_X='cwsLicenseLicenseslistExpiryDate'
_W='cwsLicenseLicenseslistCheckedOutCount'
_V='cwsLicenseLicenseslistCount'
_U='cwsLicenseLicenseslistHostId'
_T='cwsLicenseLicenseslistType'
_S='cwsLicenseLicenseslistIssuedDate'
_R='cwsLicenseLicenseslistIssuerName'
_Q='cwsLicenseLicenseslistSource'
_P='cwsLicenseLicenseslistStatus'
_O='cwsLicenseLicenseslistVersion'
_N='cwsLicenseLicenseslistDescription'
_M='cwsLicenseLicenseslistName'
_L='cwsLicenseClientStateComplianceState'
_K='cwsLicenseClientIdRegistrationId'
_J='cwsLicenseServerTableSnmpKey'
_I='cwsLicenseLicenseslistLicenseIndex'
_H='cwsLicenseClientStateTableSnmpKey'
_G='cwsLicenseClientIdTableSnmpKey'
_F='OctetString'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-LICENSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
StringMaxl128,StringMaxl16,StringMaxl32,StringMaxl64=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','StringMaxl128','StringMaxl16','StringMaxl32','StringMaxl64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaWsLicenseMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,25))
if mibBuilder.loadTexts:cienaWsLicenseMIB.setRevisions(('2017-07-07 00:00',))
class LicenseComplianceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notCompliant',0),('compliant',1)))
class LicenseSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('preInstall',0),('local',1)))
class LicenseStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('valid',0),('invalid',1),('expired',2)))
class LicenseType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('trial',0),('served',1)))
_CienaWsLicenseObjects_ObjectIdentity=ObjectIdentity
cienaWsLicenseObjects=_CienaWsLicenseObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,25,1))
_CienaWsLicenseConformance_ObjectIdentity=ObjectIdentity
cienaWsLicenseConformance=_CienaWsLicenseConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,25,2))
_CienaWsLicenseGroups_ObjectIdentity=ObjectIdentity
cienaWsLicenseGroups=_CienaWsLicenseGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,25,2,1))
_CienaWsLicenseCompliances_ObjectIdentity=ObjectIdentity
cienaWsLicenseCompliances=_CienaWsLicenseCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,25,2,2))
_CwsLicenseClientIdTable_Object=MibTable
cwsLicenseClientIdTable=_CwsLicenseClientIdTable_Object((1,3,6,1,4,1,1271,3,4,25,4))
if mibBuilder.loadTexts:cwsLicenseClientIdTable.setStatus(_A)
_CwsLicenseClientIdEntry_Object=MibTableRow
cwsLicenseClientIdEntry=_CwsLicenseClientIdEntry_Object((1,3,6,1,4,1,1271,3,4,25,4,1))
cwsLicenseClientIdEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cwsLicenseClientIdEntry.setStatus(_A)
class _CwsLicenseClientIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLicenseClientIdTableSnmpKey_Type.__name__=_D
_CwsLicenseClientIdTableSnmpKey_Object=MibTableColumn
cwsLicenseClientIdTableSnmpKey=_CwsLicenseClientIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,25,4,1,1),_CwsLicenseClientIdTableSnmpKey_Type())
cwsLicenseClientIdTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsLicenseClientIdTableSnmpKey.setStatus(_A)
_CwsLicenseClientIdRegistrationId_Type=StringMaxl64
_CwsLicenseClientIdRegistrationId_Object=MibTableColumn
cwsLicenseClientIdRegistrationId=_CwsLicenseClientIdRegistrationId_Object((1,3,6,1,4,1,1271,3,4,25,4,1,2),_CwsLicenseClientIdRegistrationId_Type())
cwsLicenseClientIdRegistrationId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseClientIdRegistrationId.setStatus(_A)
_CwsLicenseClientStateTable_Object=MibTable
cwsLicenseClientStateTable=_CwsLicenseClientStateTable_Object((1,3,6,1,4,1,1271,3,4,25,5))
if mibBuilder.loadTexts:cwsLicenseClientStateTable.setStatus(_A)
_CwsLicenseClientStateEntry_Object=MibTableRow
cwsLicenseClientStateEntry=_CwsLicenseClientStateEntry_Object((1,3,6,1,4,1,1271,3,4,25,5,1))
cwsLicenseClientStateEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwsLicenseClientStateEntry.setStatus(_A)
class _CwsLicenseClientStateTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLicenseClientStateTableSnmpKey_Type.__name__=_D
_CwsLicenseClientStateTableSnmpKey_Object=MibTableColumn
cwsLicenseClientStateTableSnmpKey=_CwsLicenseClientStateTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,25,5,1,1),_CwsLicenseClientStateTableSnmpKey_Type())
cwsLicenseClientStateTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsLicenseClientStateTableSnmpKey.setStatus(_A)
_CwsLicenseClientStateComplianceState_Type=LicenseComplianceState
_CwsLicenseClientStateComplianceState_Object=MibTableColumn
cwsLicenseClientStateComplianceState=_CwsLicenseClientStateComplianceState_Object((1,3,6,1,4,1,1271,3,4,25,5,1,2),_CwsLicenseClientStateComplianceState_Type())
cwsLicenseClientStateComplianceState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseClientStateComplianceState.setStatus(_A)
_CwsLicenseLicenseslistTable_Object=MibTable
cwsLicenseLicenseslistTable=_CwsLicenseLicenseslistTable_Object((1,3,6,1,4,1,1271,3,4,25,7))
if mibBuilder.loadTexts:cwsLicenseLicenseslistTable.setStatus(_A)
_CwsLicenseLicenseslistEntry_Object=MibTableRow
cwsLicenseLicenseslistEntry=_CwsLicenseLicenseslistEntry_Object((1,3,6,1,4,1,1271,3,4,25,7,1))
cwsLicenseLicenseslistEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cwsLicenseLicenseslistEntry.setStatus(_A)
class _CwsLicenseLicenseslistLicenseIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLicenseLicenseslistLicenseIndex_Type.__name__=_D
_CwsLicenseLicenseslistLicenseIndex_Object=MibTableColumn
cwsLicenseLicenseslistLicenseIndex=_CwsLicenseLicenseslistLicenseIndex_Object((1,3,6,1,4,1,1271,3,4,25,7,1,1),_CwsLicenseLicenseslistLicenseIndex_Type())
cwsLicenseLicenseslistLicenseIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsLicenseLicenseslistLicenseIndex.setStatus(_A)
_CwsLicenseLicenseslistName_Type=StringMaxl128
_CwsLicenseLicenseslistName_Object=MibTableColumn
cwsLicenseLicenseslistName=_CwsLicenseLicenseslistName_Object((1,3,6,1,4,1,1271,3,4,25,7,1,2),_CwsLicenseLicenseslistName_Type())
cwsLicenseLicenseslistName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistName.setStatus(_A)
_CwsLicenseLicenseslistDescription_Type=StringMaxl128
_CwsLicenseLicenseslistDescription_Object=MibTableColumn
cwsLicenseLicenseslistDescription=_CwsLicenseLicenseslistDescription_Object((1,3,6,1,4,1,1271,3,4,25,7,1,3),_CwsLicenseLicenseslistDescription_Type())
cwsLicenseLicenseslistDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistDescription.setStatus(_A)
_CwsLicenseLicenseslistVersion_Type=StringMaxl16
_CwsLicenseLicenseslistVersion_Object=MibTableColumn
cwsLicenseLicenseslistVersion=_CwsLicenseLicenseslistVersion_Object((1,3,6,1,4,1,1271,3,4,25,7,1,4),_CwsLicenseLicenseslistVersion_Type())
cwsLicenseLicenseslistVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistVersion.setStatus(_A)
_CwsLicenseLicenseslistStatus_Type=LicenseStatus
_CwsLicenseLicenseslistStatus_Object=MibTableColumn
cwsLicenseLicenseslistStatus=_CwsLicenseLicenseslistStatus_Object((1,3,6,1,4,1,1271,3,4,25,7,1,5),_CwsLicenseLicenseslistStatus_Type())
cwsLicenseLicenseslistStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistStatus.setStatus(_A)
_CwsLicenseLicenseslistSource_Type=LicenseSource
_CwsLicenseLicenseslistSource_Object=MibTableColumn
cwsLicenseLicenseslistSource=_CwsLicenseLicenseslistSource_Object((1,3,6,1,4,1,1271,3,4,25,7,1,6),_CwsLicenseLicenseslistSource_Type())
cwsLicenseLicenseslistSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistSource.setStatus(_A)
_CwsLicenseLicenseslistIssuerName_Type=StringMaxl128
_CwsLicenseLicenseslistIssuerName_Object=MibTableColumn
cwsLicenseLicenseslistIssuerName=_CwsLicenseLicenseslistIssuerName_Object((1,3,6,1,4,1,1271,3,4,25,7,1,7),_CwsLicenseLicenseslistIssuerName_Type())
cwsLicenseLicenseslistIssuerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistIssuerName.setStatus(_A)
_CwsLicenseLicenseslistIssuedDate_Type=StringMaxl128
_CwsLicenseLicenseslistIssuedDate_Object=MibTableColumn
cwsLicenseLicenseslistIssuedDate=_CwsLicenseLicenseslistIssuedDate_Object((1,3,6,1,4,1,1271,3,4,25,7,1,8),_CwsLicenseLicenseslistIssuedDate_Type())
cwsLicenseLicenseslistIssuedDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistIssuedDate.setStatus(_A)
_CwsLicenseLicenseslistType_Type=LicenseType
_CwsLicenseLicenseslistType_Object=MibTableColumn
cwsLicenseLicenseslistType=_CwsLicenseLicenseslistType_Object((1,3,6,1,4,1,1271,3,4,25,7,1,9),_CwsLicenseLicenseslistType_Type())
cwsLicenseLicenseslistType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistType.setStatus(_A)
_CwsLicenseLicenseslistHostId_Type=StringMaxl128
_CwsLicenseLicenseslistHostId_Object=MibTableColumn
cwsLicenseLicenseslistHostId=_CwsLicenseLicenseslistHostId_Object((1,3,6,1,4,1,1271,3,4,25,7,1,10),_CwsLicenseLicenseslistHostId_Type())
cwsLicenseLicenseslistHostId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistHostId.setStatus(_A)
_CwsLicenseLicenseslistCount_Type=StringMaxl16
_CwsLicenseLicenseslistCount_Object=MibTableColumn
cwsLicenseLicenseslistCount=_CwsLicenseLicenseslistCount_Object((1,3,6,1,4,1,1271,3,4,25,7,1,11),_CwsLicenseLicenseslistCount_Type())
cwsLicenseLicenseslistCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistCount.setStatus(_A)
_CwsLicenseLicenseslistCheckedOutCount_Type=StringMaxl16
_CwsLicenseLicenseslistCheckedOutCount_Object=MibTableColumn
cwsLicenseLicenseslistCheckedOutCount=_CwsLicenseLicenseslistCheckedOutCount_Object((1,3,6,1,4,1,1271,3,4,25,7,1,12),_CwsLicenseLicenseslistCheckedOutCount_Type())
cwsLicenseLicenseslistCheckedOutCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistCheckedOutCount.setStatus(_A)
_CwsLicenseLicenseslistExpiryDate_Type=StringMaxl32
_CwsLicenseLicenseslistExpiryDate_Object=MibTableColumn
cwsLicenseLicenseslistExpiryDate=_CwsLicenseLicenseslistExpiryDate_Object((1,3,6,1,4,1,1271,3,4,25,7,1,13),_CwsLicenseLicenseslistExpiryDate_Type())
cwsLicenseLicenseslistExpiryDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistExpiryDate.setStatus(_A)
_CwsLicenseLicenseslistNotice_Type=StringMaxl128
_CwsLicenseLicenseslistNotice_Object=MibTableColumn
cwsLicenseLicenseslistNotice=_CwsLicenseLicenseslistNotice_Object((1,3,6,1,4,1,1271,3,4,25,7,1,14),_CwsLicenseLicenseslistNotice_Type())
cwsLicenseLicenseslistNotice.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseLicenseslistNotice.setStatus(_A)
_CwsLicenseServerTable_Object=MibTable
cwsLicenseServerTable=_CwsLicenseServerTable_Object((1,3,6,1,4,1,1271,3,4,25,8))
if mibBuilder.loadTexts:cwsLicenseServerTable.setStatus(_A)
_CwsLicenseServerEntry_Object=MibTableRow
cwsLicenseServerEntry=_CwsLicenseServerEntry_Object((1,3,6,1,4,1,1271,3,4,25,8,1))
cwsLicenseServerEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cwsLicenseServerEntry.setStatus(_A)
class _CwsLicenseServerTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsLicenseServerTableSnmpKey_Type.__name__=_D
_CwsLicenseServerTableSnmpKey_Object=MibTableColumn
cwsLicenseServerTableSnmpKey=_CwsLicenseServerTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,25,8,1,1),_CwsLicenseServerTableSnmpKey_Type())
cwsLicenseServerTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsLicenseServerTableSnmpKey.setStatus(_A)
class _CwsLicenseServerHostAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CwsLicenseServerHostAddress_Type.__name__=_F
_CwsLicenseServerHostAddress_Object=MibTableColumn
cwsLicenseServerHostAddress=_CwsLicenseServerHostAddress_Object((1,3,6,1,4,1,1271,3,4,25,8,1,2),_CwsLicenseServerHostAddress_Type())
cwsLicenseServerHostAddress.setMaxAccess('read-write')
if mibBuilder.loadTexts:cwsLicenseServerHostAddress.setStatus(_A)
_CwsLicenseServerNumLicenseServers_Type=Unsigned32
_CwsLicenseServerNumLicenseServers_Object=MibTableColumn
cwsLicenseServerNumLicenseServers=_CwsLicenseServerNumLicenseServers_Object((1,3,6,1,4,1,1271,3,4,25,8,1,3),_CwsLicenseServerNumLicenseServers_Type())
cwsLicenseServerNumLicenseServers.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsLicenseServerNumLicenseServers.setStatus(_A)
cienaWsLicenseGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,25,2,1,1))
cienaWsLicenseGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cienaWsLicenseGroup.setStatus(_A)
cienaWsLicenseCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,25,2,2,1))
cienaWsLicenseCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:cienaWsLicenseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LicenseComplianceState':LicenseComplianceState,'LicenseSource':LicenseSource,'LicenseStatus':LicenseStatus,'LicenseType':LicenseType,'cienaWsLicenseMIB':cienaWsLicenseMIB,'cienaWsLicenseObjects':cienaWsLicenseObjects,'cienaWsLicenseConformance':cienaWsLicenseConformance,'cienaWsLicenseGroups':cienaWsLicenseGroups,_b:cienaWsLicenseGroup,'cienaWsLicenseCompliances':cienaWsLicenseCompliances,'cienaWsLicenseCompliance':cienaWsLicenseCompliance,'cwsLicenseClientIdTable':cwsLicenseClientIdTable,'cwsLicenseClientIdEntry':cwsLicenseClientIdEntry,_G:cwsLicenseClientIdTableSnmpKey,_K:cwsLicenseClientIdRegistrationId,'cwsLicenseClientStateTable':cwsLicenseClientStateTable,'cwsLicenseClientStateEntry':cwsLicenseClientStateEntry,_H:cwsLicenseClientStateTableSnmpKey,_L:cwsLicenseClientStateComplianceState,'cwsLicenseLicenseslistTable':cwsLicenseLicenseslistTable,'cwsLicenseLicenseslistEntry':cwsLicenseLicenseslistEntry,_I:cwsLicenseLicenseslistLicenseIndex,_M:cwsLicenseLicenseslistName,_N:cwsLicenseLicenseslistDescription,_O:cwsLicenseLicenseslistVersion,_P:cwsLicenseLicenseslistStatus,_Q:cwsLicenseLicenseslistSource,_R:cwsLicenseLicenseslistIssuerName,_S:cwsLicenseLicenseslistIssuedDate,_T:cwsLicenseLicenseslistType,_U:cwsLicenseLicenseslistHostId,_V:cwsLicenseLicenseslistCount,_W:cwsLicenseLicenseslistCheckedOutCount,_X:cwsLicenseLicenseslistExpiryDate,_Y:cwsLicenseLicenseslistNotice,'cwsLicenseServerTable':cwsLicenseServerTable,'cwsLicenseServerEntry':cwsLicenseServerEntry,_J:cwsLicenseServerTableSnmpKey,_Z:cwsLicenseServerHostAddress,_a:cwsLicenseServerNumLicenseServers})