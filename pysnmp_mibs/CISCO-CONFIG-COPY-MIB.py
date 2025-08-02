_m='ccCopyGroupVpn'
_l='ccCopyGroup'
_k='ccCopyCompletion'
_j='ccCopyVrfName'
_i='ccCopyErrorDescription'
_h='ccCopyErrorDeviceWWN'
_g='ccCopyErrorDeviceIpAddress'
_f='ccCopyErrorDeviceIpAddressType'
_e='ccCopyServerAddressRev1'
_d='ccCopyServerAddressType'
_c='ccCopyErrorIndex'
_b='ConfigCopyProtocol'
_a='not-accessible'
_Z='TruthValue'
_Y='Unsigned32'
_X='OctetString'
_W='ccCopyErrorGroup'
_V='ccCopyEntryRowStatus'
_U='ccCopyNotificationOnCompletion'
_T='ccCopyUserPassword'
_S='ccCopyUserName'
_R='ccCopyServerAddress'
_Q='ccCopyDestFileType'
_P='ccCopySourceFileType'
_O='ccCopyProtocol'
_N='ccCopyIndex'
_M='DisplayString'
_L='ccCopyGroupRev1'
_K='ccCopyFailCause'
_J='ccCopyTimeCompleted'
_I='ccCopyTimeStarted'
_H='ccCopyState'
_G='ccCopyFileName'
_F='ccCopyNotificationsGroup'
_E='deprecated'
_D='read-only'
_C='read-create'
_B='current'
_A='CISCO-CONFIG-COPY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameIdOrZero,=mibBuilder.importSymbols('CISCO-ST-TC','FcNameIdOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Y,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_Z)
ciscoConfigCopyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,96))
if mibBuilder.loadTexts:ciscoConfigCopyMIB.setRevisions(('2009-02-27 00:00','2005-04-06 00:00','2004-03-17 00:00','2002-12-17 00:00','2002-05-30 00:00','2002-05-07 00:00','2002-03-28 00:00'))
class ConfigCopyProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('rcp',3),('scp',4),('sftp',5)))
class ConfigCopyState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('waiting',1),('running',2),('successful',3),('failed',4)))
class ConfigCopyFailCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('unknown',1),('badFileName',2),('timeout',3),('noMem',4),('noConfig',5),('unsupportedProtocol',6),('someConfigApplyFailed',7),('systemNotReady',8),('requestAborted',9)))
class ConfigFileType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('networkFile',1),('iosFile',2),('startupConfig',3),('runningConfig',4),('terminal',5),('fabricStartupConfig',6)))
_CiscoConfigCopyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoConfigCopyMIBObjects=_CiscoConfigCopyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,96,1))
_CcCopy_ObjectIdentity=ObjectIdentity
ccCopy=_CcCopy_ObjectIdentity((1,3,6,1,4,1,9,9,96,1,1))
_CcCopyTable_Object=MibTable
ccCopyTable=_CcCopyTable_Object((1,3,6,1,4,1,9,9,96,1,1,1))
if mibBuilder.loadTexts:ccCopyTable.setStatus(_B)
_CcCopyEntry_Object=MibTableRow
ccCopyEntry=_CcCopyEntry_Object((1,3,6,1,4,1,9,9,96,1,1,1,1))
ccCopyEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:ccCopyEntry.setStatus(_B)
class _CcCopyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CcCopyIndex_Type.__name__=_Y
_CcCopyIndex_Object=MibTableColumn
ccCopyIndex=_CcCopyIndex_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,1),_CcCopyIndex_Type())
ccCopyIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:ccCopyIndex.setStatus(_B)
class _CcCopyProtocol_Type(ConfigCopyProtocol):defaultValue=1
_CcCopyProtocol_Type.__name__=_b
_CcCopyProtocol_Object=MibTableColumn
ccCopyProtocol=_CcCopyProtocol_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,2),_CcCopyProtocol_Type())
ccCopyProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyProtocol.setStatus(_B)
_CcCopySourceFileType_Type=ConfigFileType
_CcCopySourceFileType_Object=MibTableColumn
ccCopySourceFileType=_CcCopySourceFileType_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,3),_CcCopySourceFileType_Type())
ccCopySourceFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopySourceFileType.setStatus(_B)
_CcCopyDestFileType_Type=ConfigFileType
_CcCopyDestFileType_Object=MibTableColumn
ccCopyDestFileType=_CcCopyDestFileType_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,4),_CcCopyDestFileType_Type())
ccCopyDestFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyDestFileType.setStatus(_B)
_CcCopyServerAddress_Type=IpAddress
_CcCopyServerAddress_Object=MibTableColumn
ccCopyServerAddress=_CcCopyServerAddress_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,5),_CcCopyServerAddress_Type())
ccCopyServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyServerAddress.setStatus(_E)
_CcCopyFileName_Type=DisplayString
_CcCopyFileName_Object=MibTableColumn
ccCopyFileName=_CcCopyFileName_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,6),_CcCopyFileName_Type())
ccCopyFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyFileName.setStatus(_B)
class _CcCopyUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_CcCopyUserName_Type.__name__=_M
_CcCopyUserName_Object=MibTableColumn
ccCopyUserName=_CcCopyUserName_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,7),_CcCopyUserName_Type())
ccCopyUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyUserName.setStatus(_B)
class _CcCopyUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_CcCopyUserPassword_Type.__name__=_M
_CcCopyUserPassword_Object=MibTableColumn
ccCopyUserPassword=_CcCopyUserPassword_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,8),_CcCopyUserPassword_Type())
ccCopyUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyUserPassword.setStatus(_B)
class _CcCopyNotificationOnCompletion_Type(TruthValue):defaultValue=2
_CcCopyNotificationOnCompletion_Type.__name__=_Z
_CcCopyNotificationOnCompletion_Object=MibTableColumn
ccCopyNotificationOnCompletion=_CcCopyNotificationOnCompletion_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,9),_CcCopyNotificationOnCompletion_Type())
ccCopyNotificationOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyNotificationOnCompletion.setStatus(_B)
_CcCopyState_Type=ConfigCopyState
_CcCopyState_Object=MibTableColumn
ccCopyState=_CcCopyState_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,10),_CcCopyState_Type())
ccCopyState.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyState.setStatus(_B)
_CcCopyTimeStarted_Type=TimeStamp
_CcCopyTimeStarted_Object=MibTableColumn
ccCopyTimeStarted=_CcCopyTimeStarted_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,11),_CcCopyTimeStarted_Type())
ccCopyTimeStarted.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyTimeStarted.setStatus(_B)
_CcCopyTimeCompleted_Type=TimeStamp
_CcCopyTimeCompleted_Object=MibTableColumn
ccCopyTimeCompleted=_CcCopyTimeCompleted_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,12),_CcCopyTimeCompleted_Type())
ccCopyTimeCompleted.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyTimeCompleted.setStatus(_B)
_CcCopyFailCause_Type=ConfigCopyFailCause
_CcCopyFailCause_Object=MibTableColumn
ccCopyFailCause=_CcCopyFailCause_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,13),_CcCopyFailCause_Type())
ccCopyFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyFailCause.setStatus(_B)
_CcCopyEntryRowStatus_Type=RowStatus
_CcCopyEntryRowStatus_Object=MibTableColumn
ccCopyEntryRowStatus=_CcCopyEntryRowStatus_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,14),_CcCopyEntryRowStatus_Type())
ccCopyEntryRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyEntryRowStatus.setStatus(_B)
_CcCopyServerAddressType_Type=InetAddressType
_CcCopyServerAddressType_Object=MibTableColumn
ccCopyServerAddressType=_CcCopyServerAddressType_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,15),_CcCopyServerAddressType_Type())
ccCopyServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyServerAddressType.setStatus(_B)
_CcCopyServerAddressRev1_Type=InetAddress
_CcCopyServerAddressRev1_Object=MibTableColumn
ccCopyServerAddressRev1=_CcCopyServerAddressRev1_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,16),_CcCopyServerAddressRev1_Type())
ccCopyServerAddressRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyServerAddressRev1.setStatus(_B)
class _CcCopyVrfName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CcCopyVrfName_Type.__name__=_X
_CcCopyVrfName_Object=MibTableColumn
ccCopyVrfName=_CcCopyVrfName_Object((1,3,6,1,4,1,9,9,96,1,1,1,1,17),_CcCopyVrfName_Type())
ccCopyVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCopyVrfName.setStatus(_B)
_CcCopyErrorTable_Object=MibTable
ccCopyErrorTable=_CcCopyErrorTable_Object((1,3,6,1,4,1,9,9,96,1,1,2))
if mibBuilder.loadTexts:ccCopyErrorTable.setStatus(_B)
_CcCopyErrorEntry_Object=MibTableRow
ccCopyErrorEntry=_CcCopyErrorEntry_Object((1,3,6,1,4,1,9,9,96,1,1,2,1))
ccCopyErrorEntry.setIndexNames((0,_A,_N),(0,_A,_c))
if mibBuilder.loadTexts:ccCopyErrorEntry.setStatus(_B)
_CcCopyErrorIndex_Type=Unsigned32
_CcCopyErrorIndex_Object=MibTableColumn
ccCopyErrorIndex=_CcCopyErrorIndex_Object((1,3,6,1,4,1,9,9,96,1,1,2,1,1),_CcCopyErrorIndex_Type())
ccCopyErrorIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:ccCopyErrorIndex.setStatus(_B)
_CcCopyErrorDeviceIpAddressType_Type=InetAddressType
_CcCopyErrorDeviceIpAddressType_Object=MibTableColumn
ccCopyErrorDeviceIpAddressType=_CcCopyErrorDeviceIpAddressType_Object((1,3,6,1,4,1,9,9,96,1,1,2,1,2),_CcCopyErrorDeviceIpAddressType_Type())
ccCopyErrorDeviceIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyErrorDeviceIpAddressType.setStatus(_B)
_CcCopyErrorDeviceIpAddress_Type=InetAddress
_CcCopyErrorDeviceIpAddress_Object=MibTableColumn
ccCopyErrorDeviceIpAddress=_CcCopyErrorDeviceIpAddress_Object((1,3,6,1,4,1,9,9,96,1,1,2,1,3),_CcCopyErrorDeviceIpAddress_Type())
ccCopyErrorDeviceIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyErrorDeviceIpAddress.setStatus(_B)
_CcCopyErrorDeviceWWN_Type=FcNameIdOrZero
_CcCopyErrorDeviceWWN_Object=MibTableColumn
ccCopyErrorDeviceWWN=_CcCopyErrorDeviceWWN_Object((1,3,6,1,4,1,9,9,96,1,1,2,1,4),_CcCopyErrorDeviceWWN_Type())
ccCopyErrorDeviceWWN.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyErrorDeviceWWN.setStatus(_B)
_CcCopyErrorDescription_Type=SnmpAdminString
_CcCopyErrorDescription_Object=MibTableColumn
ccCopyErrorDescription=_CcCopyErrorDescription_Object((1,3,6,1,4,1,9,9,96,1,1,2,1,5),_CcCopyErrorDescription_Type())
ccCopyErrorDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCopyErrorDescription.setStatus(_B)
_CiscoConfigCopyMIBTrapPrefix_ObjectIdentity=ObjectIdentity
ciscoConfigCopyMIBTrapPrefix=_CiscoConfigCopyMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,96,2))
_CcCopyMIBTraps_ObjectIdentity=ObjectIdentity
ccCopyMIBTraps=_CcCopyMIBTraps_ObjectIdentity((1,3,6,1,4,1,9,9,96,2,1))
_CiscoConfigCopyMIBConformance_ObjectIdentity=ObjectIdentity
ciscoConfigCopyMIBConformance=_CiscoConfigCopyMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,96,3))
_CcCopyMIBCompliances_ObjectIdentity=ObjectIdentity
ccCopyMIBCompliances=_CcCopyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,96,3,1))
_CcCopyMIBGroups_ObjectIdentity=ObjectIdentity
ccCopyMIBGroups=_CcCopyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,96,3,2))
ccCopyGroup=ObjectGroup((1,3,6,1,4,1,9,9,96,3,2,1))
ccCopyGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_G),(_A,_S),(_A,_T),(_A,_U),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_V)))
if mibBuilder.loadTexts:ccCopyGroup.setStatus(_E)
ccCopyGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,96,3,2,3))
ccCopyGroupRev1.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_d),(_A,_e),(_A,_G),(_A,_S),(_A,_T),(_A,_U),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_V)))
if mibBuilder.loadTexts:ccCopyGroupRev1.setStatus(_B)
ccCopyErrorGroup=ObjectGroup((1,3,6,1,4,1,9,9,96,3,2,4))
ccCopyErrorGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ccCopyErrorGroup.setStatus(_B)
ccCopyGroupVpn=ObjectGroup((1,3,6,1,4,1,9,9,96,3,2,5))
ccCopyGroupVpn.setObjects((_A,_j))
if mibBuilder.loadTexts:ccCopyGroupVpn.setStatus(_B)
ccCopyCompletion=NotificationType((1,3,6,1,4,1,9,9,96,2,1,1))
ccCopyCompletion.setObjects(*((_A,_R),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ccCopyCompletion.setStatus(_B)
ccCopyNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,96,3,2,2))
ccCopyNotificationsGroup.setObjects((_A,_k))
if mibBuilder.loadTexts:ccCopyNotificationsGroup.setStatus(_B)
ccCopyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,96,3,1,1))
ccCopyMIBCompliance.setObjects(*((_A,_l),(_A,_F)))
if mibBuilder.loadTexts:ccCopyMIBCompliance.setStatus(_E)
ccCopyMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,96,3,1,2))
ccCopyMIBComplianceRev1.setObjects(*((_A,_L),(_A,_F)))
if mibBuilder.loadTexts:ccCopyMIBComplianceRev1.setStatus(_E)
ccCopyMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,96,3,1,3))
ccCopyMIBComplianceRev2.setObjects(*((_A,_L),(_A,_F),(_A,_W)))
if mibBuilder.loadTexts:ccCopyMIBComplianceRev2.setStatus(_E)
ccCopyMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,96,3,1,4))
ccCopyMIBComplianceRev3.setObjects(*((_A,_L),(_A,_F),(_A,_m),(_A,_W)))
if mibBuilder.loadTexts:ccCopyMIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_b:ConfigCopyProtocol,'ConfigCopyState':ConfigCopyState,'ConfigCopyFailCause':ConfigCopyFailCause,'ConfigFileType':ConfigFileType,'ciscoConfigCopyMIB':ciscoConfigCopyMIB,'ciscoConfigCopyMIBObjects':ciscoConfigCopyMIBObjects,'ccCopy':ccCopy,'ccCopyTable':ccCopyTable,'ccCopyEntry':ccCopyEntry,_N:ccCopyIndex,_O:ccCopyProtocol,_P:ccCopySourceFileType,_Q:ccCopyDestFileType,_R:ccCopyServerAddress,_G:ccCopyFileName,_S:ccCopyUserName,_T:ccCopyUserPassword,_U:ccCopyNotificationOnCompletion,_H:ccCopyState,_I:ccCopyTimeStarted,_J:ccCopyTimeCompleted,_K:ccCopyFailCause,_V:ccCopyEntryRowStatus,_d:ccCopyServerAddressType,_e:ccCopyServerAddressRev1,_j:ccCopyVrfName,'ccCopyErrorTable':ccCopyErrorTable,'ccCopyErrorEntry':ccCopyErrorEntry,_c:ccCopyErrorIndex,_f:ccCopyErrorDeviceIpAddressType,_g:ccCopyErrorDeviceIpAddress,_h:ccCopyErrorDeviceWWN,_i:ccCopyErrorDescription,'ciscoConfigCopyMIBTrapPrefix':ciscoConfigCopyMIBTrapPrefix,'ccCopyMIBTraps':ccCopyMIBTraps,_k:ccCopyCompletion,'ciscoConfigCopyMIBConformance':ciscoConfigCopyMIBConformance,'ccCopyMIBCompliances':ccCopyMIBCompliances,'ccCopyMIBCompliance':ccCopyMIBCompliance,'ccCopyMIBComplianceRev1':ccCopyMIBComplianceRev1,'ccCopyMIBComplianceRev2':ccCopyMIBComplianceRev2,'ccCopyMIBComplianceRev3':ccCopyMIBComplianceRev3,'ccCopyMIBGroups':ccCopyMIBGroups,_l:ccCopyGroup,_F:ccCopyNotificationsGroup,_L:ccCopyGroupRev1,_W:ccCopyErrorGroup,_m:ccCopyGroupVpn})