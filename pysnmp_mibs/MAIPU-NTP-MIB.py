_L='ntpServerVRF'
_K='ntpServerAddr'
_J='ntpTrustKeyNum'
_I='ntpAuthKeyNum'
_H='read-only'
_G='read-write'
_F='not-accessible'
_E='DisplayString'
_D='Integer32'
_C='MAIPU-NTP-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ntpMib=ModuleIdentity((1,3,6,1,4,1,5651,3,97))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_NtpAuthenticationCntl_Type=EnabledStatus
_NtpAuthenticationCntl_Object=MibScalar
ntpAuthenticationCntl=_NtpAuthenticationCntl_Object((1,3,6,1,4,1,5651,3,97,1),_NtpAuthenticationCntl_Type())
ntpAuthenticationCntl.setMaxAccess(_G)
if mibBuilder.loadTexts:ntpAuthenticationCntl.setStatus(_A)
_NtpMasterCntl_Type=EnabledStatus
_NtpMasterCntl_Object=MibScalar
ntpMasterCntl=_NtpMasterCntl_Object((1,3,6,1,4,1,5651,3,97,2),_NtpMasterCntl_Type())
ntpMasterCntl.setMaxAccess(_G)
if mibBuilder.loadTexts:ntpMasterCntl.setStatus(_A)
class _NtpMasterStratum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,15))
_NtpMasterStratum_Type.__name__=_D
_NtpMasterStratum_Object=MibScalar
ntpMasterStratum=_NtpMasterStratum_Object((1,3,6,1,4,1,5651,3,97,3),_NtpMasterStratum_Type())
ntpMasterStratum.setMaxAccess(_G)
if mibBuilder.loadTexts:ntpMasterStratum.setStatus(_A)
class _NtpSynStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('synchronized',1),('unsynchronized',2)))
_NtpSynStatus_Type.__name__=_D
_NtpSynStatus_Object=MibScalar
ntpSynStatus=_NtpSynStatus_Object((1,3,6,1,4,1,5651,3,97,4),_NtpSynStatus_Type())
ntpSynStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ntpSynStatus.setStatus(_A)
class _NtpSynTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtpSynTime_Type.__name__=_E
_NtpSynTime_Object=MibScalar
ntpSynTime=_NtpSynTime_Object((1,3,6,1,4,1,5651,3,97,5),_NtpSynTime_Type())
ntpSynTime.setMaxAccess(_H)
if mibBuilder.loadTexts:ntpSynTime.setStatus(_A)
_NtpAuthenticationKeyTable_Object=MibTable
ntpAuthenticationKeyTable=_NtpAuthenticationKeyTable_Object((1,3,6,1,4,1,5651,3,97,20))
if mibBuilder.loadTexts:ntpAuthenticationKeyTable.setStatus(_A)
_NtpAuthenticationKeyEntry_Object=MibTableRow
ntpAuthenticationKeyEntry=_NtpAuthenticationKeyEntry_Object((1,3,6,1,4,1,5651,3,97,20,1))
ntpAuthenticationKeyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:ntpAuthenticationKeyEntry.setStatus(_A)
_NtpAuthKeyNum_Type=Unsigned32
_NtpAuthKeyNum_Object=MibTableColumn
ntpAuthKeyNum=_NtpAuthKeyNum_Object((1,3,6,1,4,1,5651,3,97,20,1,1),_NtpAuthKeyNum_Type())
ntpAuthKeyNum.setMaxAccess(_F)
if mibBuilder.loadTexts:ntpAuthKeyNum.setStatus(_A)
class _NtpAuthStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtpAuthStr_Type.__name__=_E
_NtpAuthStr_Object=MibTableColumn
ntpAuthStr=_NtpAuthStr_Object((1,3,6,1,4,1,5651,3,97,20,1,2),_NtpAuthStr_Type())
ntpAuthStr.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpAuthStr.setStatus(_A)
_NtpAuthKeyRowStatus_Type=RowStatus
_NtpAuthKeyRowStatus_Object=MibTableColumn
ntpAuthKeyRowStatus=_NtpAuthKeyRowStatus_Object((1,3,6,1,4,1,5651,3,97,20,1,3),_NtpAuthKeyRowStatus_Type())
ntpAuthKeyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpAuthKeyRowStatus.setStatus(_A)
_NtpTrustKeyTable_Object=MibTable
ntpTrustKeyTable=_NtpTrustKeyTable_Object((1,3,6,1,4,1,5651,3,97,21))
if mibBuilder.loadTexts:ntpTrustKeyTable.setStatus(_A)
_NtpTrustKeyEntry_Object=MibTableRow
ntpTrustKeyEntry=_NtpTrustKeyEntry_Object((1,3,6,1,4,1,5651,3,97,21,1))
ntpTrustKeyEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:ntpTrustKeyEntry.setStatus(_A)
_NtpTrustKeyNum_Type=Unsigned32
_NtpTrustKeyNum_Object=MibTableColumn
ntpTrustKeyNum=_NtpTrustKeyNum_Object((1,3,6,1,4,1,5651,3,97,21,1,1),_NtpTrustKeyNum_Type())
ntpTrustKeyNum.setMaxAccess(_F)
if mibBuilder.loadTexts:ntpTrustKeyNum.setStatus(_A)
_NtpTrustkeyRowStatus_Type=RowStatus
_NtpTrustkeyRowStatus_Object=MibTableColumn
ntpTrustkeyRowStatus=_NtpTrustkeyRowStatus_Object((1,3,6,1,4,1,5651,3,97,21,1,2),_NtpTrustkeyRowStatus_Type())
ntpTrustkeyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpTrustkeyRowStatus.setStatus(_A)
_NtpServerTable_Object=MibTable
ntpServerTable=_NtpServerTable_Object((1,3,6,1,4,1,5651,3,97,22))
if mibBuilder.loadTexts:ntpServerTable.setStatus(_A)
_NtpServerEntry_Object=MibTableRow
ntpServerEntry=_NtpServerEntry_Object((1,3,6,1,4,1,5651,3,97,22,1))
ntpServerEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:ntpServerEntry.setStatus(_A)
_NtpServerAddr_Type=IpAddress
_NtpServerAddr_Object=MibTableColumn
ntpServerAddr=_NtpServerAddr_Object((1,3,6,1,4,1,5651,3,97,22,1,1),_NtpServerAddr_Type())
ntpServerAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:ntpServerAddr.setStatus(_A)
class _NtpServerVRF_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_NtpServerVRF_Type.__name__=_E
_NtpServerVRF_Object=MibTableColumn
ntpServerVRF=_NtpServerVRF_Object((1,3,6,1,4,1,5651,3,97,22,1,2),_NtpServerVRF_Type())
ntpServerVRF.setMaxAccess(_F)
if mibBuilder.loadTexts:ntpServerVRF.setStatus(_A)
_NtpServerKeyNum_Type=Unsigned32
_NtpServerKeyNum_Object=MibTableColumn
ntpServerKeyNum=_NtpServerKeyNum_Object((1,3,6,1,4,1,5651,3,97,22,1,3),_NtpServerKeyNum_Type())
ntpServerKeyNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpServerKeyNum.setStatus(_A)
class _NtpServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ver1',1),('ver2',2),('ver3',3),('ver4',4)))
_NtpServerVersion_Type.__name__=_D
_NtpServerVersion_Object=MibTableColumn
ntpServerVersion=_NtpServerVersion_Object((1,3,6,1,4,1,5651,3,97,22,1,4),_NtpServerVersion_Type())
ntpServerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpServerVersion.setStatus(_A)
_NtpServerRowStatus_Type=RowStatus
_NtpServerRowStatus_Object=MibTableColumn
ntpServerRowStatus=_NtpServerRowStatus_Object((1,3,6,1,4,1,5651,3,97,22,1,5),_NtpServerRowStatus_Type())
ntpServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpServerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EnabledStatus':EnabledStatus,'ntpMib':ntpMib,'ntpAuthenticationCntl':ntpAuthenticationCntl,'ntpMasterCntl':ntpMasterCntl,'ntpMasterStratum':ntpMasterStratum,'ntpSynStatus':ntpSynStatus,'ntpSynTime':ntpSynTime,'ntpAuthenticationKeyTable':ntpAuthenticationKeyTable,'ntpAuthenticationKeyEntry':ntpAuthenticationKeyEntry,_I:ntpAuthKeyNum,'ntpAuthStr':ntpAuthStr,'ntpAuthKeyRowStatus':ntpAuthKeyRowStatus,'ntpTrustKeyTable':ntpTrustKeyTable,'ntpTrustKeyEntry':ntpTrustKeyEntry,_J:ntpTrustKeyNum,'ntpTrustkeyRowStatus':ntpTrustkeyRowStatus,'ntpServerTable':ntpServerTable,'ntpServerEntry':ntpServerEntry,_K:ntpServerAddr,_L:ntpServerVRF,'ntpServerKeyNum':ntpServerKeyNum,'ntpServerVersion':ntpServerVersion,'ntpServerRowStatus':ntpServerRowStatus})