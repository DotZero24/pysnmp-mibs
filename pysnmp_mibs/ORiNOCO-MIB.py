_B8='oriUnitTemp'
_B7='oriTrapVarDefaultRouterIPAddress'
_B6='oriTrapVarSubnetMask'
_B5='oriTrapVarIPAddress'
_B4='oriTrapVarDHCPServerIPAddress'
_B3='oriSystemReboot'
_B2='oriTrapVarUnAuthorizedManagerCount'
_B1='oriTrapVarUnauthorizedManagerIPaddress'
_B0='oriTrapVarFailedAuthenticationType'
_A_='oriTrapVarBatchCLILineNumber'
_Az='oriTFTPAutoConfigServerIPAddress'
_Ay='oriTFTPAutoConfigFilename'
_Ax='oriVLANIDTableIdentifier'
_Aw='oriWirelessIfNetworkName'
_Av='oriDMZHostTableIndex'
_Au='oriVLANIDTableIndex'
_At='oriNATStaticPortBindTableIndex'
_As='oriNATStaticIPBindTableIndex'
_Ar='oriConfigFileTableIndex'
_Aq='oriPPPoEMACtoSessionTableIndex'
_Ap='oriPPPoESessionTableIndex'
_Ao='oriSecurityProfileTableSecModeIndex'
_An='oriSecurityProfileTableIndex'
_Am='oriRogueScanResultsTableIndex'
_Al='oriRADScanResultsTableIndex'
_Ak='oriWDSSetupTablePortIndex'
_Aj='oriHTTPWebSitenameTableIndex'
_Ai='oriDHCPRelayDHCPServerTableIndex'
_Ah='oriDHCPServerIPPoolTableIndex'
_Ag='oriQoSDot1DToIPDSCPPriority'
_Af='oriQoSDot1DToIPDSCPMappingTableIndex'
_Ae='oriQoSDot1dPriority'
_Ad='oriQoSDot1DToDot1pMappingTableIndex'
_Ac='oriQoSPolicyTableSecIndex'
_Ab='oriQoSPolicyTableIndex'
_Aa='oriLinkIntTableIndex'
_AZ='oriLinkTestDataRateTableIndex'
_AY='oriIAPPMACIPTableIndex'
_AX='oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex'
_AW='oriRADIUSAcctClientStatTableIndex'
_AV='oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex'
_AU='oriRADIUSAuthClientStatTableIndex'
_AT='oriRADIUSSvrTablePrimaryOrSecondaryIndex'
_AS='oriRADIUSSvrTableProfileIndex'
_AR='noDelimiter'
_AQ='singleDashDelimited'
_AP='colonDelimited'
_AO='dashDelimited'
_AN='oriRADIUSAcctServerTableIndex'
_AM='authAndAcct'
_AL='accounting'
_AK='authentication'
_AJ='oriRADIUSAuthServerTableIndex'
_AI='oriIntraCellBlockingGroupTableIndex'
_AH='oriIntraCellBlockingMACTableIndex'
_AG='oriBroadcastFilteringTableIndex'
_AF='oriPortFilterTableEntryIndex'
_AE='oriStaticMACAddressFilterTableIndex'
_AD='oriAccessControlTableIndex'
_AC='oriProtocolFilterTableIndex'
_AB='oriSNMPTrapHostTableIndex'
_AA='oriSNMPAccessTableIndex'
_A9='oriNetworkIPConfigTableIndex'
_A8='oriWORPIfSiteSurveyTableIndex'
_A7='oriWORPIfSatConfigTableIndex'
_A6='oriEthernetIfConfigTableIndex'
_A5='oriWirelessIfSSIDTableIndex'
_A4='oriWirelessIfSecurityIndex'
_A3='oriWirelessIfPropertiesIndex'
_A2='oriTempLogMessage'
_A1='oriSyslogHostTableIndex'
_A0='spectralink'
_z='oriSystemEventLogMessage'
_y='oriSystemInvMgmtInterfaceTableIndex'
_x='IpAddress'
_w='oriTrapVarInterface'
_v='oriTrapVarTaskSuspended'
_u='oriTrapVarUnauthorizedClientMACAddress'
_t='oriTrapVarBatchCLIMessage'
_s='unknown'
_r='oriLinkTestTableIndex'
_q='name'
_p='ipAddress'
_o='both'
_n='oriStationStatTableIndex'
_m='oneHundredFiftyTwoBits'
_l='oriSystemFeatureTableCode'
_k='oriSystemInvMgmtTableComponentIndex'
_j='oriTrapVarTFTPOperation'
_i='oriTrapVarTFTPFilename'
_h='oriTrapVarTFTPIPAddress'
_g='oriTrapVarBatchCLIFilename'
_f='block'
_e='passthru'
_d='oneHundredTwentyEightBits'
_c='sixtyFourBits'
_b='dot1x'
_a='VlanId'
_Z='wep'
_Y='down'
_X='up'
_W='disabled'
_V='OctetString'
_U='public'
_T='ifIndex'
_S='IF-MIB'
_R='oriTrapVarMACAddress'
_Q='none'
_P='oriTrapVarWirelessCard'
_O='DisplayString'
_N='ObjStatusActive'
_M='create'
_L='delete'
_K='oriGenericTrapVariable'
_J='ObjStatus'
_I='read-create'
_H='deprecated'
_G='disable'
_F='enable'
_E='ORiNOCO-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_S,_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_x,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_O,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
orinoco=ModuleIdentity((1,3,6,1,4,1,11898,2))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4094))
class InterfaceBitmask(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ObjStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
class WEPKeyType(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class ObjStatusActive(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('deleted',3)))
class DisplayString80(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
class DisplayString55(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,55))
class DisplayString32(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Agere_ObjectIdentity=ObjectIdentity
agere=_Agere_ObjectIdentity((1,3,6,1,4,1,11898))
_OrinocoObjects_ObjectIdentity=ObjectIdentity
orinocoObjects=_OrinocoObjects_ObjectIdentity((1,3,6,1,4,1,11898,2,1))
_OrinocoSys_ObjectIdentity=ObjectIdentity
orinocoSys=_OrinocoSys_ObjectIdentity((1,3,6,1,4,1,11898,2,1,1))
_OrinocoSysInvMgmt_ObjectIdentity=ObjectIdentity
orinocoSysInvMgmt=_OrinocoSysInvMgmt_ObjectIdentity((1,3,6,1,4,1,11898,2,1,1,1))
_OriSystemInvMgmtComponentTable_Object=MibTable
oriSystemInvMgmtComponentTable=_OriSystemInvMgmtComponentTable_Object((1,3,6,1,4,1,11898,2,1,1,1,1))
if mibBuilder.loadTexts:oriSystemInvMgmtComponentTable.setStatus(_A)
_OriSystemInvMgmtComponentTableEntry_Object=MibTableRow
oriSystemInvMgmtComponentTableEntry=_OriSystemInvMgmtComponentTableEntry_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1))
oriSystemInvMgmtComponentTableEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:oriSystemInvMgmtComponentTableEntry.setStatus(_A)
_OriSystemInvMgmtTableComponentIndex_Type=Integer32
_OriSystemInvMgmtTableComponentIndex_Object=MibTableColumn
oriSystemInvMgmtTableComponentIndex=_OriSystemInvMgmtTableComponentIndex_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,1),_OriSystemInvMgmtTableComponentIndex_Type())
oriSystemInvMgmtTableComponentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentIndex.setStatus(_A)
_OriSystemInvMgmtTableComponentSerialNumber_Type=DisplayString
_OriSystemInvMgmtTableComponentSerialNumber_Object=MibTableColumn
oriSystemInvMgmtTableComponentSerialNumber=_OriSystemInvMgmtTableComponentSerialNumber_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,2),_OriSystemInvMgmtTableComponentSerialNumber_Type())
oriSystemInvMgmtTableComponentSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentSerialNumber.setStatus(_A)
_OriSystemInvMgmtTableComponentName_Type=DisplayString
_OriSystemInvMgmtTableComponentName_Object=MibTableColumn
oriSystemInvMgmtTableComponentName=_OriSystemInvMgmtTableComponentName_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,3),_OriSystemInvMgmtTableComponentName_Type())
oriSystemInvMgmtTableComponentName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentName.setStatus(_A)
_OriSystemInvMgmtTableComponentId_Type=Integer32
_OriSystemInvMgmtTableComponentId_Object=MibTableColumn
oriSystemInvMgmtTableComponentId=_OriSystemInvMgmtTableComponentId_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,4),_OriSystemInvMgmtTableComponentId_Type())
oriSystemInvMgmtTableComponentId.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentId.setStatus(_A)
_OriSystemInvMgmtTableComponentVariant_Type=Integer32
_OriSystemInvMgmtTableComponentVariant_Object=MibTableColumn
oriSystemInvMgmtTableComponentVariant=_OriSystemInvMgmtTableComponentVariant_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,5),_OriSystemInvMgmtTableComponentVariant_Type())
oriSystemInvMgmtTableComponentVariant.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentVariant.setStatus(_A)
_OriSystemInvMgmtTableComponentReleaseVersion_Type=Integer32
_OriSystemInvMgmtTableComponentReleaseVersion_Object=MibTableColumn
oriSystemInvMgmtTableComponentReleaseVersion=_OriSystemInvMgmtTableComponentReleaseVersion_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,6),_OriSystemInvMgmtTableComponentReleaseVersion_Type())
oriSystemInvMgmtTableComponentReleaseVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentReleaseVersion.setStatus(_A)
_OriSystemInvMgmtTableComponentMajorVersion_Type=Integer32
_OriSystemInvMgmtTableComponentMajorVersion_Object=MibTableColumn
oriSystemInvMgmtTableComponentMajorVersion=_OriSystemInvMgmtTableComponentMajorVersion_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,7),_OriSystemInvMgmtTableComponentMajorVersion_Type())
oriSystemInvMgmtTableComponentMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentMajorVersion.setStatus(_A)
_OriSystemInvMgmtTableComponentMinorVersion_Type=Integer32
_OriSystemInvMgmtTableComponentMinorVersion_Object=MibTableColumn
oriSystemInvMgmtTableComponentMinorVersion=_OriSystemInvMgmtTableComponentMinorVersion_Object((1,3,6,1,4,1,11898,2,1,1,1,1,1,8),_OriSystemInvMgmtTableComponentMinorVersion_Type())
oriSystemInvMgmtTableComponentMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentMinorVersion.setStatus(_A)
_OriSystemInvMgmtTableComponentIfTable_Object=MibTable
oriSystemInvMgmtTableComponentIfTable=_OriSystemInvMgmtTableComponentIfTable_Object((1,3,6,1,4,1,11898,2,1,1,1,2))
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentIfTable.setStatus(_H)
_OriSystemInvMgmtTableComponentIfTableEntry_Object=MibTableRow
oriSystemInvMgmtTableComponentIfTableEntry=_OriSystemInvMgmtTableComponentIfTableEntry_Object((1,3,6,1,4,1,11898,2,1,1,1,2,1))
oriSystemInvMgmtTableComponentIfTableEntry.setIndexNames((0,_E,_k),(0,_E,_y))
if mibBuilder.loadTexts:oriSystemInvMgmtTableComponentIfTableEntry.setStatus(_H)
_OriSystemInvMgmtInterfaceTableIndex_Type=Integer32
_OriSystemInvMgmtInterfaceTableIndex_Object=MibTableColumn
oriSystemInvMgmtInterfaceTableIndex=_OriSystemInvMgmtInterfaceTableIndex_Object((1,3,6,1,4,1,11898,2,1,1,1,2,1,1),_OriSystemInvMgmtInterfaceTableIndex_Type())
oriSystemInvMgmtInterfaceTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtInterfaceTableIndex.setStatus(_H)
_OriSystemInvMgmtInterfaceId_Type=Integer32
_OriSystemInvMgmtInterfaceId_Object=MibTableColumn
oriSystemInvMgmtInterfaceId=_OriSystemInvMgmtInterfaceId_Object((1,3,6,1,4,1,11898,2,1,1,1,2,1,2),_OriSystemInvMgmtInterfaceId_Type())
oriSystemInvMgmtInterfaceId.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtInterfaceId.setStatus(_H)
class _OriSystemInvMgmtInterfaceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('actor',1),('supplier',2)))
_OriSystemInvMgmtInterfaceRole_Type.__name__=_D
_OriSystemInvMgmtInterfaceRole_Object=MibTableColumn
oriSystemInvMgmtInterfaceRole=_OriSystemInvMgmtInterfaceRole_Object((1,3,6,1,4,1,11898,2,1,1,1,2,1,3),_OriSystemInvMgmtInterfaceRole_Type())
oriSystemInvMgmtInterfaceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtInterfaceRole.setStatus(_H)
_OriSystemInvMgmtInterfaceVariant_Type=Integer32
_OriSystemInvMgmtInterfaceVariant_Object=MibTableColumn
oriSystemInvMgmtInterfaceVariant=_OriSystemInvMgmtInterfaceVariant_Object((1,3,6,1,4,1,11898,2,1,1,1,2,1,4),_OriSystemInvMgmtInterfaceVariant_Type())
oriSystemInvMgmtInterfaceVariant.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtInterfaceVariant.setStatus(_H)
_OriSystemInvMgmtInterfaceBottomNumber_Type=Integer32
_OriSystemInvMgmtInterfaceBottomNumber_Object=MibTableColumn
oriSystemInvMgmtInterfaceBottomNumber=_OriSystemInvMgmtInterfaceBottomNumber_Object((1,3,6,1,4,1,11898,2,1,1,1,2,1,5),_OriSystemInvMgmtInterfaceBottomNumber_Type())
oriSystemInvMgmtInterfaceBottomNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtInterfaceBottomNumber.setStatus(_H)
_OriSystemInvMgmtInterfaceTopNumber_Type=Integer32
_OriSystemInvMgmtInterfaceTopNumber_Object=MibTableColumn
oriSystemInvMgmtInterfaceTopNumber=_OriSystemInvMgmtInterfaceTopNumber_Object((1,3,6,1,4,1,11898,2,1,1,1,2,1,6),_OriSystemInvMgmtInterfaceTopNumber_Type())
oriSystemInvMgmtInterfaceTopNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemInvMgmtInterfaceTopNumber.setStatus(_H)
_OriSystemReboot_Type=Integer32
_OriSystemReboot_Object=MibScalar
oriSystemReboot=_OriSystemReboot_Object((1,3,6,1,4,1,11898,2,1,1,4),_OriSystemReboot_Type())
oriSystemReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemReboot.setStatus(_A)
_OriSystemContactEmail_Type=DisplayString
_OriSystemContactEmail_Object=MibScalar
oriSystemContactEmail=_OriSystemContactEmail_Object((1,3,6,1,4,1,11898,2,1,1,5),_OriSystemContactEmail_Type())
oriSystemContactEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemContactEmail.setStatus(_A)
_OriSystemContactPhoneNumber_Type=DisplayString
_OriSystemContactPhoneNumber_Object=MibScalar
oriSystemContactPhoneNumber=_OriSystemContactPhoneNumber_Object((1,3,6,1,4,1,11898,2,1,1,6),_OriSystemContactPhoneNumber_Type())
oriSystemContactPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemContactPhoneNumber.setStatus(_A)
_OriSystemFlashUpdate_Type=Integer32
_OriSystemFlashUpdate_Object=MibScalar
oriSystemFlashUpdate=_OriSystemFlashUpdate_Object((1,3,6,1,4,1,11898,2,1,1,7),_OriSystemFlashUpdate_Type())
oriSystemFlashUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemFlashUpdate.setStatus(_A)
_OriSystemFlashBackupInterval_Type=Integer32
_OriSystemFlashBackupInterval_Object=MibScalar
oriSystemFlashBackupInterval=_OriSystemFlashBackupInterval_Object((1,3,6,1,4,1,11898,2,1,1,8),_OriSystemFlashBackupInterval_Type())
oriSystemFlashBackupInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemFlashBackupInterval.setStatus(_A)
class _OriSystemEmergencyResetToDefault_Type(Integer32):defaultValue=0
_OriSystemEmergencyResetToDefault_Type.__name__=_D
_OriSystemEmergencyResetToDefault_Object=MibScalar
oriSystemEmergencyResetToDefault=_OriSystemEmergencyResetToDefault_Object((1,3,6,1,4,1,11898,2,1,1,9),_OriSystemEmergencyResetToDefault_Type())
oriSystemEmergencyResetToDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemEmergencyResetToDefault.setStatus(_A)
class _OriSystemMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('gateway',2)))
_OriSystemMode_Type.__name__=_D
_OriSystemMode_Object=MibScalar
oriSystemMode=_OriSystemMode_Object((1,3,6,1,4,1,11898,2,1,1,10),_OriSystemMode_Type())
oriSystemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemMode.setStatus(_A)
_OriSystemEventLogTable_Object=MibTable
oriSystemEventLogTable=_OriSystemEventLogTable_Object((1,3,6,1,4,1,11898,2,1,1,11))
if mibBuilder.loadTexts:oriSystemEventLogTable.setStatus(_A)
_OriSystemEventLogTableEntry_Object=MibTableRow
oriSystemEventLogTableEntry=_OriSystemEventLogTableEntry_Object((1,3,6,1,4,1,11898,2,1,1,11,1))
oriSystemEventLogTableEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:oriSystemEventLogTableEntry.setStatus(_A)
_OriSystemEventLogMessage_Type=DisplayString
_OriSystemEventLogMessage_Object=MibTableColumn
oriSystemEventLogMessage=_OriSystemEventLogMessage_Object((1,3,6,1,4,1,11898,2,1,1,11,1,1),_OriSystemEventLogMessage_Type())
oriSystemEventLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemEventLogMessage.setStatus(_A)
class _OriSystemEventLogTableReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_OriSystemEventLogTableReset_Type.__name__=_D
_OriSystemEventLogTableReset_Object=MibScalar
oriSystemEventLogTableReset=_OriSystemEventLogTableReset_Object((1,3,6,1,4,1,11898,2,1,1,12),_OriSystemEventLogTableReset_Type())
oriSystemEventLogTableReset.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemEventLogTableReset.setStatus(_A)
_OriSystemEventLogMask_Type=Integer32
_OriSystemEventLogMask_Object=MibScalar
oriSystemEventLogMask=_OriSystemEventLogMask_Object((1,3,6,1,4,1,11898,2,1,1,13),_OriSystemEventLogMask_Type())
oriSystemEventLogMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemEventLogMask.setStatus(_A)
_OriSystemAccessUserName_Type=DisplayString
_OriSystemAccessUserName_Object=MibScalar
oriSystemAccessUserName=_OriSystemAccessUserName_Object((1,3,6,1,4,1,11898,2,1,1,14),_OriSystemAccessUserName_Type())
oriSystemAccessUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemAccessUserName.setStatus(_A)
_OriSystemAccessPassword_Type=DisplayString
_OriSystemAccessPassword_Object=MibScalar
oriSystemAccessPassword=_OriSystemAccessPassword_Object((1,3,6,1,4,1,11898,2,1,1,15),_OriSystemAccessPassword_Type())
oriSystemAccessPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemAccessPassword.setStatus(_A)
class _OriSystemAccessLoginTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_OriSystemAccessLoginTimeout_Type.__name__=_D
_OriSystemAccessLoginTimeout_Object=MibScalar
oriSystemAccessLoginTimeout=_OriSystemAccessLoginTimeout_Object((1,3,6,1,4,1,11898,2,1,1,16),_OriSystemAccessLoginTimeout_Type())
oriSystemAccessLoginTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemAccessLoginTimeout.setStatus(_A)
class _OriSystemAccessIdleTimeout_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,36000))
_OriSystemAccessIdleTimeout_Type.__name__=_D
_OriSystemAccessIdleTimeout_Object=MibScalar
oriSystemAccessIdleTimeout=_OriSystemAccessIdleTimeout_Object((1,3,6,1,4,1,11898,2,1,1,17),_OriSystemAccessIdleTimeout_Type())
oriSystemAccessIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemAccessIdleTimeout.setStatus(_A)
_OriSystemEventLogNumberOfMessages_Type=Integer32
_OriSystemEventLogNumberOfMessages_Object=MibScalar
oriSystemEventLogNumberOfMessages=_OriSystemEventLogNumberOfMessages_Object((1,3,6,1,4,1,11898,2,1,1,18),_OriSystemEventLogNumberOfMessages_Type())
oriSystemEventLogNumberOfMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemEventLogNumberOfMessages.setStatus(_A)
_OrinocoSysFeature_ObjectIdentity=ObjectIdentity
orinocoSysFeature=_OrinocoSysFeature_ObjectIdentity((1,3,6,1,4,1,11898,2,1,1,19))
_OriSystemFeatureTable_Object=MibTable
oriSystemFeatureTable=_OriSystemFeatureTable_Object((1,3,6,1,4,1,11898,2,1,1,19,1))
if mibBuilder.loadTexts:oriSystemFeatureTable.setStatus(_A)
_OriSystemFeatureTableEntry_Object=MibTableRow
oriSystemFeatureTableEntry=_OriSystemFeatureTableEntry_Object((1,3,6,1,4,1,11898,2,1,1,19,1,1))
oriSystemFeatureTableEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:oriSystemFeatureTableEntry.setStatus(_A)
class _OriSystemFeatureTableCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)));namedValues=NamedValues(*(('bandwidthWiFi',1),('bandwidthWDS',2),('bandwidthWORPUp',3),('bandwidthTurboCell',4),('bandwidthADSL',5),('bandwidthCable',6),('bandwidthPhone',7),('maxStationsWiFi',8),('maxLinksWDS',9),('maxStationsWORP',10),('maxStationsTurboCell',11),('maxPPPoESessions',12),('managementHTTP',13),('remoteLinkTest',14),('routingStatic',15),('routingRIP',16),('routingOSPF',17),('spanningTreeProtocol',18),('linkIntegrity',19),('dHCPServer',20),('dHCPRelayAgent',21),('proxyARP',22),('filteringStatic',23),('authRADIUS',24),('acctRADIUS',25),('throttlingRADIUS',26),('filterIP',27),('ieee802dot1x',28),('nse',29),('iAPP',30),('dNSRedirect',31),('aOLNATGateway',32),('hereUare',33),(_A0,34),('vLANTagging',35),('satMaxUsers',36),('bandwidthWORPDown',37),('disableSecWifiIf',38),('initialProductType',39)))
_OriSystemFeatureTableCode_Type.__name__=_D
_OriSystemFeatureTableCode_Object=MibTableColumn
oriSystemFeatureTableCode=_OriSystemFeatureTableCode_Object((1,3,6,1,4,1,11898,2,1,1,19,1,1,1),_OriSystemFeatureTableCode_Type())
oriSystemFeatureTableCode.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemFeatureTableCode.setStatus(_A)
_OriSystemFeatureTableSupported_Type=Integer32
_OriSystemFeatureTableSupported_Object=MibTableColumn
oriSystemFeatureTableSupported=_OriSystemFeatureTableSupported_Object((1,3,6,1,4,1,11898,2,1,1,19,1,1,2),_OriSystemFeatureTableSupported_Type())
oriSystemFeatureTableSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemFeatureTableSupported.setStatus(_A)
_OriSystemFeatureTableLicensed_Type=Integer32
_OriSystemFeatureTableLicensed_Object=MibTableColumn
oriSystemFeatureTableLicensed=_OriSystemFeatureTableLicensed_Object((1,3,6,1,4,1,11898,2,1,1,19,1,1,3),_OriSystemFeatureTableLicensed_Type())
oriSystemFeatureTableLicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemFeatureTableLicensed.setStatus(_A)
_OriSystemFeatureTableDescription_Type=DisplayString
_OriSystemFeatureTableDescription_Object=MibTableColumn
oriSystemFeatureTableDescription=_OriSystemFeatureTableDescription_Object((1,3,6,1,4,1,11898,2,1,1,19,1,1,4),_OriSystemFeatureTableDescription_Type())
oriSystemFeatureTableDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemFeatureTableDescription.setStatus(_A)
class _OriSystemAccessMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_OriSystemAccessMaxSessions_Type.__name__=_D
_OriSystemAccessMaxSessions_Object=MibScalar
oriSystemAccessMaxSessions=_OriSystemAccessMaxSessions_Object((1,3,6,1,4,1,11898,2,1,1,20),_OriSystemAccessMaxSessions_Type())
oriSystemAccessMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemAccessMaxSessions.setStatus(_A)
_OrinocoSyslog_ObjectIdentity=ObjectIdentity
orinocoSyslog=_OrinocoSyslog_ObjectIdentity((1,3,6,1,4,1,11898,2,1,1,21))
class _OriSyslogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriSyslogStatus_Type.__name__=_D
_OriSyslogStatus_Object=MibScalar
oriSyslogStatus=_OriSyslogStatus_Object((1,3,6,1,4,1,11898,2,1,1,21,1),_OriSyslogStatus_Type())
oriSyslogStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSyslogStatus.setStatus(_A)
_OriSyslogPort_Type=Integer32
_OriSyslogPort_Object=MibScalar
oriSyslogPort=_OriSyslogPort_Object((1,3,6,1,4,1,11898,2,1,1,21,2),_OriSyslogPort_Type())
oriSyslogPort.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSyslogPort.setStatus(_A)
class _OriSyslogPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_OriSyslogPriority_Type.__name__=_D
_OriSyslogPriority_Object=MibScalar
oriSyslogPriority=_OriSyslogPriority_Object((1,3,6,1,4,1,11898,2,1,1,21,3),_OriSyslogPriority_Type())
oriSyslogPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSyslogPriority.setStatus(_A)
class _OriSyslogHeartbeatStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriSyslogHeartbeatStatus_Type.__name__=_D
_OriSyslogHeartbeatStatus_Object=MibScalar
oriSyslogHeartbeatStatus=_OriSyslogHeartbeatStatus_Object((1,3,6,1,4,1,11898,2,1,1,21,4),_OriSyslogHeartbeatStatus_Type())
oriSyslogHeartbeatStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSyslogHeartbeatStatus.setStatus(_A)
class _OriSyslogHeartbeatInterval_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_OriSyslogHeartbeatInterval_Type.__name__=_D
_OriSyslogHeartbeatInterval_Object=MibScalar
oriSyslogHeartbeatInterval=_OriSyslogHeartbeatInterval_Object((1,3,6,1,4,1,11898,2,1,1,21,5),_OriSyslogHeartbeatInterval_Type())
oriSyslogHeartbeatInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSyslogHeartbeatInterval.setStatus(_A)
_OriSyslogHostTable_Object=MibTable
oriSyslogHostTable=_OriSyslogHostTable_Object((1,3,6,1,4,1,11898,2,1,1,21,6))
if mibBuilder.loadTexts:oriSyslogHostTable.setStatus(_A)
_OriSyslogHostTableEntry_Object=MibTableRow
oriSyslogHostTableEntry=_OriSyslogHostTableEntry_Object((1,3,6,1,4,1,11898,2,1,1,21,6,1))
oriSyslogHostTableEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:oriSyslogHostTableEntry.setStatus(_A)
class _OriSyslogHostTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_OriSyslogHostTableIndex_Type.__name__=_D
_OriSyslogHostTableIndex_Object=MibTableColumn
oriSyslogHostTableIndex=_OriSyslogHostTableIndex_Object((1,3,6,1,4,1,11898,2,1,1,21,6,1,1),_OriSyslogHostTableIndex_Type())
oriSyslogHostTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSyslogHostTableIndex.setStatus(_A)
_OriSyslogHostIPAddress_Type=IpAddress
_OriSyslogHostIPAddress_Object=MibTableColumn
oriSyslogHostIPAddress=_OriSyslogHostIPAddress_Object((1,3,6,1,4,1,11898,2,1,1,21,6,1,2),_OriSyslogHostIPAddress_Type())
oriSyslogHostIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSyslogHostIPAddress.setStatus(_A)
_OriSyslogHostComment_Type=DisplayString
_OriSyslogHostComment_Object=MibTableColumn
oriSyslogHostComment=_OriSyslogHostComment_Object((1,3,6,1,4,1,11898,2,1,1,21,6,1,3),_OriSyslogHostComment_Type())
oriSyslogHostComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSyslogHostComment.setStatus(_A)
class _OriSyslogHostTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriSyslogHostTableEntryStatus_Type.__name__=_D
_OriSyslogHostTableEntryStatus_Object=MibTableColumn
oriSyslogHostTableEntryStatus=_OriSyslogHostTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,1,21,6,1,4),_OriSyslogHostTableEntryStatus_Type())
oriSyslogHostTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSyslogHostTableEntryStatus.setStatus(_A)
_OriSystemCountryCode_Type=DisplayString
_OriSystemCountryCode_Object=MibScalar
oriSystemCountryCode=_OriSystemCountryCode_Object((1,3,6,1,4,1,11898,2,1,1,22),_OriSystemCountryCode_Type())
oriSystemCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSystemCountryCode.setStatus(_A)
_OrinocoTempLog_ObjectIdentity=ObjectIdentity
orinocoTempLog=_OrinocoTempLog_ObjectIdentity((1,3,6,1,4,1,11898,2,1,1,23))
class _OriUnitTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-30,60))
_OriUnitTemp_Type.__name__=_D
_OriUnitTemp_Object=MibScalar
oriUnitTemp=_OriUnitTemp_Object((1,3,6,1,4,1,11898,2,1,1,23,1),_OriUnitTemp_Type())
oriUnitTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:oriUnitTemp.setStatus(_A)
class _OriTempLoggingInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_OriTempLoggingInterval_Type.__name__=_D
_OriTempLoggingInterval_Object=MibScalar
oriTempLoggingInterval=_OriTempLoggingInterval_Object((1,3,6,1,4,1,11898,2,1,1,23,2),_OriTempLoggingInterval_Type())
oriTempLoggingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTempLoggingInterval.setStatus(_A)
_OriTempLogTable_Object=MibTable
oriTempLogTable=_OriTempLogTable_Object((1,3,6,1,4,1,11898,2,1,1,23,3))
if mibBuilder.loadTexts:oriTempLogTable.setStatus(_A)
_OriTempLogTableEntry_Object=MibTableRow
oriTempLogTableEntry=_OriTempLogTableEntry_Object((1,3,6,1,4,1,11898,2,1,1,23,3,1))
oriTempLogTableEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:oriTempLogTableEntry.setStatus(_A)
_OriTempLogMessage_Type=DisplayString55
_OriTempLogMessage_Object=MibTableColumn
oriTempLogMessage=_OriTempLogMessage_Object((1,3,6,1,4,1,11898,2,1,1,23,3,1,1),_OriTempLogMessage_Type())
oriTempLogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTempLogMessage.setStatus(_A)
class _OriTempLogTableReset_Type(Integer32):defaultValue=0
_OriTempLogTableReset_Type.__name__=_D
_OriTempLogTableReset_Object=MibScalar
oriTempLogTableReset=_OriTempLogTableReset_Object((1,3,6,1,4,1,11898,2,1,1,23,4),_OriTempLogTableReset_Type())
oriTempLogTableReset.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTempLogTableReset.setStatus(_A)
class _OriSystemHwType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('indoor',1),('outdoor',2)))
_OriSystemHwType_Type.__name__=_D
_OriSystemHwType_Object=MibScalar
oriSystemHwType=_OriSystemHwType_Object((1,3,6,1,4,1,11898,2,1,1,24),_OriSystemHwType_Type())
oriSystemHwType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSystemHwType.setStatus(_A)
_OrinocoIf_ObjectIdentity=ObjectIdentity
orinocoIf=_OrinocoIf_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2))
_OrinocoWirelessIf_ObjectIdentity=ObjectIdentity
orinocoWirelessIf=_OrinocoWirelessIf_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,1))
_OriWirelessIfPropertiesTable_Object=MibTable
oriWirelessIfPropertiesTable=_OriWirelessIfPropertiesTable_Object((1,3,6,1,4,1,11898,2,1,2,1,1))
if mibBuilder.loadTexts:oriWirelessIfPropertiesTable.setStatus(_A)
_OriWirelessIfPropertiesEntry_Object=MibTableRow
oriWirelessIfPropertiesEntry=_OriWirelessIfPropertiesEntry_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1))
oriWirelessIfPropertiesEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:oriWirelessIfPropertiesEntry.setStatus(_A)
_OriWirelessIfPropertiesIndex_Type=Integer32
_OriWirelessIfPropertiesIndex_Object=MibTableColumn
oriWirelessIfPropertiesIndex=_OriWirelessIfPropertiesIndex_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,1),_OriWirelessIfPropertiesIndex_Type())
oriWirelessIfPropertiesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfPropertiesIndex.setStatus(_A)
class _OriWirelessIfNetworkName_Type(DisplayString):defaultValue=OctetString('My Wireless Network');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OriWirelessIfNetworkName_Type.__name__=_O
_OriWirelessIfNetworkName_Object=MibTableColumn
oriWirelessIfNetworkName=_OriWirelessIfNetworkName_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,2),_OriWirelessIfNetworkName_Type())
oriWirelessIfNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfNetworkName.setStatus(_A)
class _OriWirelessIfMediumReservation_Type(Integer32):defaultValue=2347;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_OriWirelessIfMediumReservation_Type.__name__=_D
_OriWirelessIfMediumReservation_Object=MibTableColumn
oriWirelessIfMediumReservation=_OriWirelessIfMediumReservation_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,3),_OriWirelessIfMediumReservation_Type())
oriWirelessIfMediumReservation.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfMediumReservation.setStatus(_A)
class _OriWirelessIfInterferenceRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfInterferenceRobustness_Type.__name__=_D
_OriWirelessIfInterferenceRobustness_Object=MibTableColumn
oriWirelessIfInterferenceRobustness=_OriWirelessIfInterferenceRobustness_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,4),_OriWirelessIfInterferenceRobustness_Type())
oriWirelessIfInterferenceRobustness.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfInterferenceRobustness.setStatus(_A)
class _OriWirelessIfDTIMPeriod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OriWirelessIfDTIMPeriod_Type.__name__=_D
_OriWirelessIfDTIMPeriod_Object=MibTableColumn
oriWirelessIfDTIMPeriod=_OriWirelessIfDTIMPeriod_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,5),_OriWirelessIfDTIMPeriod_Type())
oriWirelessIfDTIMPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfDTIMPeriod.setStatus(_A)
class _OriWirelessIfChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_OriWirelessIfChannel_Type.__name__=_D
_OriWirelessIfChannel_Object=MibTableColumn
oriWirelessIfChannel=_OriWirelessIfChannel_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,6),_OriWirelessIfChannel_Type())
oriWirelessIfChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfChannel.setStatus(_A)
class _OriWirelessIfDistancebetweenAPs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('large',1),('medium',2),('small',3),('minicell',4),('microcell',5)))
_OriWirelessIfDistancebetweenAPs_Type.__name__=_D
_OriWirelessIfDistancebetweenAPs_Object=MibTableColumn
oriWirelessIfDistancebetweenAPs=_OriWirelessIfDistancebetweenAPs_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,7),_OriWirelessIfDistancebetweenAPs_Type())
oriWirelessIfDistancebetweenAPs.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfDistancebetweenAPs.setStatus(_A)
class _OriWirelessIfMulticastRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OriWirelessIfMulticastRate_Type.__name__=_D
_OriWirelessIfMulticastRate_Object=MibTableColumn
oriWirelessIfMulticastRate=_OriWirelessIfMulticastRate_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,8),_OriWirelessIfMulticastRate_Type())
oriWirelessIfMulticastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfMulticastRate.setStatus(_A)
class _OriWirelessIfClosedSystem_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfClosedSystem_Type.__name__=_D
_OriWirelessIfClosedSystem_Object=MibTableColumn
oriWirelessIfClosedSystem=_OriWirelessIfClosedSystem_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,9),_OriWirelessIfClosedSystem_Type())
oriWirelessIfClosedSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfClosedSystem.setStatus(_A)
_OriWirelessIfAllowedSupportedDataRates_Type=OctetString
_OriWirelessIfAllowedSupportedDataRates_Object=MibTableColumn
oriWirelessIfAllowedSupportedDataRates=_OriWirelessIfAllowedSupportedDataRates_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,10),_OriWirelessIfAllowedSupportedDataRates_Type())
oriWirelessIfAllowedSupportedDataRates.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfAllowedSupportedDataRates.setStatus(_A)
_OriWirelessIfRegulatoryDomainList_Type=OctetString
_OriWirelessIfRegulatoryDomainList_Object=MibTableColumn
oriWirelessIfRegulatoryDomainList=_OriWirelessIfRegulatoryDomainList_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,11),_OriWirelessIfRegulatoryDomainList_Type())
oriWirelessIfRegulatoryDomainList.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfRegulatoryDomainList.setStatus(_A)
_OriWirelessIfAllowedChannels_Type=OctetString
_OriWirelessIfAllowedChannels_Object=MibTableColumn
oriWirelessIfAllowedChannels=_OriWirelessIfAllowedChannels_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,12),_OriWirelessIfAllowedChannels_Type())
oriWirelessIfAllowedChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfAllowedChannels.setStatus(_A)
_OriWirelessIfMACAddress_Type=PhysAddress
_OriWirelessIfMACAddress_Object=MibTableColumn
oriWirelessIfMACAddress=_OriWirelessIfMACAddress_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,13),_OriWirelessIfMACAddress_Type())
oriWirelessIfMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfMACAddress.setStatus(_H)
class _OriWirelessIfLoadBalancing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfLoadBalancing_Type.__name__=_D
_OriWirelessIfLoadBalancing_Object=MibTableColumn
oriWirelessIfLoadBalancing=_OriWirelessIfLoadBalancing_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,14),_OriWirelessIfLoadBalancing_Type())
oriWirelessIfLoadBalancing.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfLoadBalancing.setStatus(_A)
class _OriWirelessIfMediumDensityDistribution_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfMediumDensityDistribution_Type.__name__=_D
_OriWirelessIfMediumDensityDistribution_Object=MibTableColumn
oriWirelessIfMediumDensityDistribution=_OriWirelessIfMediumDensityDistribution_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,15),_OriWirelessIfMediumDensityDistribution_Type())
oriWirelessIfMediumDensityDistribution.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfMediumDensityDistribution.setStatus(_A)
class _OriWirelessIfTxRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OriWirelessIfTxRate_Type.__name__=_D
_OriWirelessIfTxRate_Object=MibTableColumn
oriWirelessIfTxRate=_OriWirelessIfTxRate_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,16),_OriWirelessIfTxRate_Type())
oriWirelessIfTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfTxRate.setStatus(_A)
class _OriWirelessIfAutoChannelSelectStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfAutoChannelSelectStatus_Type.__name__=_D
_OriWirelessIfAutoChannelSelectStatus_Object=MibTableColumn
oriWirelessIfAutoChannelSelectStatus=_OriWirelessIfAutoChannelSelectStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,17),_OriWirelessIfAutoChannelSelectStatus_Type())
oriWirelessIfAutoChannelSelectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfAutoChannelSelectStatus.setStatus(_A)
_OriWirelessIfBandwidthLimitIn_Type=Gauge32
_OriWirelessIfBandwidthLimitIn_Object=MibTableColumn
oriWirelessIfBandwidthLimitIn=_OriWirelessIfBandwidthLimitIn_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,18),_OriWirelessIfBandwidthLimitIn_Type())
oriWirelessIfBandwidthLimitIn.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfBandwidthLimitIn.setStatus(_A)
_OriWirelessIfBandwidthLimitOut_Type=Gauge32
_OriWirelessIfBandwidthLimitOut_Object=MibTableColumn
oriWirelessIfBandwidthLimitOut=_OriWirelessIfBandwidthLimitOut_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,19),_OriWirelessIfBandwidthLimitOut_Type())
oriWirelessIfBandwidthLimitOut.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfBandwidthLimitOut.setStatus(_A)
_OriWirelessIfTurboModeStatus_Type=ObjStatus
_OriWirelessIfTurboModeStatus_Object=MibTableColumn
oriWirelessIfTurboModeStatus=_OriWirelessIfTurboModeStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,20),_OriWirelessIfTurboModeStatus_Type())
oriWirelessIfTurboModeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfTurboModeStatus.setStatus(_A)
_OriWirelessIfSupportedOperationalModes_Type=DisplayString
_OriWirelessIfSupportedOperationalModes_Object=MibTableColumn
oriWirelessIfSupportedOperationalModes=_OriWirelessIfSupportedOperationalModes_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,21),_OriWirelessIfSupportedOperationalModes_Type())
oriWirelessIfSupportedOperationalModes.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfSupportedOperationalModes.setStatus(_A)
class _OriWirelessIfOperationalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('dot11b-only',1),('dot11g-only',2),('dot11bg',3),('dot11a-only',4),('dot11g-wifi',5)))
_OriWirelessIfOperationalMode_Type.__name__=_D
_OriWirelessIfOperationalMode_Object=MibTableColumn
oriWirelessIfOperationalMode=_OriWirelessIfOperationalMode_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,22),_OriWirelessIfOperationalMode_Type())
oriWirelessIfOperationalMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfOperationalMode.setStatus(_A)
_OriWirelessIfPreambleType_Type=DisplayString
_OriWirelessIfPreambleType_Object=MibTableColumn
oriWirelessIfPreambleType=_OriWirelessIfPreambleType_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,23),_OriWirelessIfPreambleType_Type())
oriWirelessIfPreambleType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfPreambleType.setStatus(_A)
_OriWirelessIfProtectionMechanismStatus_Type=ObjStatus
_OriWirelessIfProtectionMechanismStatus_Object=MibTableColumn
oriWirelessIfProtectionMechanismStatus=_OriWirelessIfProtectionMechanismStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,24),_OriWirelessIfProtectionMechanismStatus_Type())
oriWirelessIfProtectionMechanismStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfProtectionMechanismStatus.setStatus(_A)
_OriWirelessIfSupportedMulticastRates_Type=DisplayString
_OriWirelessIfSupportedMulticastRates_Object=MibTableColumn
oriWirelessIfSupportedMulticastRates=_OriWirelessIfSupportedMulticastRates_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,25),_OriWirelessIfSupportedMulticastRates_Type())
oriWirelessIfSupportedMulticastRates.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfSupportedMulticastRates.setStatus(_A)
class _OriWirelessIfCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_OriWirelessIfCapabilities_Type.__name__=_V
_OriWirelessIfCapabilities_Object=MibTableColumn
oriWirelessIfCapabilities=_OriWirelessIfCapabilities_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,26),_OriWirelessIfCapabilities_Type())
oriWirelessIfCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfCapabilities.setStatus(_A)
class _OriWirelessIfLBTxTimeThreshold_Type(Integer32):defaultValue=1000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_OriWirelessIfLBTxTimeThreshold_Type.__name__=_D
_OriWirelessIfLBTxTimeThreshold_Object=MibTableColumn
oriWirelessIfLBTxTimeThreshold=_OriWirelessIfLBTxTimeThreshold_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,27),_OriWirelessIfLBTxTimeThreshold_Type())
oriWirelessIfLBTxTimeThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfLBTxTimeThreshold.setStatus(_A)
class _OriWirelessIfLBAdjAPTimeDiffThreshold_Type(Integer32):defaultValue=1000000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_OriWirelessIfLBAdjAPTimeDiffThreshold_Type.__name__=_D
_OriWirelessIfLBAdjAPTimeDiffThreshold_Object=MibTableColumn
oriWirelessIfLBAdjAPTimeDiffThreshold=_OriWirelessIfLBAdjAPTimeDiffThreshold_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,28),_OriWirelessIfLBAdjAPTimeDiffThreshold_Type())
oriWirelessIfLBAdjAPTimeDiffThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfLBAdjAPTimeDiffThreshold.setStatus(_A)
class _OriWirelessIfACSFrequencyBandScan_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OriWirelessIfACSFrequencyBandScan_Type.__name__=_D
_OriWirelessIfACSFrequencyBandScan_Object=MibTableColumn
oriWirelessIfACSFrequencyBandScan=_OriWirelessIfACSFrequencyBandScan_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,29),_OriWirelessIfACSFrequencyBandScan_Type())
oriWirelessIfACSFrequencyBandScan.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfACSFrequencyBandScan.setStatus(_A)
class _OriWirelessIfSecurityPerSSIDStatus_Type(ObjStatus):defaultValue=2
_OriWirelessIfSecurityPerSSIDStatus_Type.__name__=_J
_OriWirelessIfSecurityPerSSIDStatus_Object=MibTableColumn
oriWirelessIfSecurityPerSSIDStatus=_OriWirelessIfSecurityPerSSIDStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,30),_OriWirelessIfSecurityPerSSIDStatus_Type())
oriWirelessIfSecurityPerSSIDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfSecurityPerSSIDStatus.setStatus(_A)
class _OriWirelessIfDFSStatus_Type(ObjStatus):defaultValue=2
_OriWirelessIfDFSStatus_Type.__name__=_J
_OriWirelessIfDFSStatus_Object=MibTableColumn
oriWirelessIfDFSStatus=_OriWirelessIfDFSStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,31),_OriWirelessIfDFSStatus_Type())
oriWirelessIfDFSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfDFSStatus.setStatus(_A)
class _OriWirelessIfAntenna_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('external',1),('internal',2),('controllable',3),(_W,4)))
_OriWirelessIfAntenna_Type.__name__=_D
_OriWirelessIfAntenna_Object=MibTableColumn
oriWirelessIfAntenna=_OriWirelessIfAntenna_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,32),_OriWirelessIfAntenna_Type())
oriWirelessIfAntenna.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfAntenna.setStatus(_H)
class _OriWirelessIfTPCMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,3),ValueRangeConstraint(6,6),ValueRangeConstraint(9,9),ValueRangeConstraint(12,12),ValueRangeConstraint(15,15),ValueRangeConstraint(18,18))
_OriWirelessIfTPCMode_Type.__name__=_D
_OriWirelessIfTPCMode_Object=MibTableColumn
oriWirelessIfTPCMode=_OriWirelessIfTPCMode_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,33),_OriWirelessIfTPCMode_Type())
oriWirelessIfTPCMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfTPCMode.setStatus(_A)
class _OriWirelessIfSuperModeStatus_Type(ObjStatus):defaultValue=2
_OriWirelessIfSuperModeStatus_Type.__name__=_J
_OriWirelessIfSuperModeStatus_Object=MibTableColumn
oriWirelessIfSuperModeStatus=_OriWirelessIfSuperModeStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,34),_OriWirelessIfSuperModeStatus_Type())
oriWirelessIfSuperModeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfSuperModeStatus.setStatus(_A)
class _OriWirelessIfWSSStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_OriWirelessIfWSSStatus_Type.__name__=_D
_OriWirelessIfWSSStatus_Object=MibTableColumn
oriWirelessIfWSSStatus=_OriWirelessIfWSSStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,35),_OriWirelessIfWSSStatus_Type())
oriWirelessIfWSSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfWSSStatus.setStatus(_A)
_OriWirelessIfSupportedAuthenticationModes_Type=DisplayString
_OriWirelessIfSupportedAuthenticationModes_Object=MibTableColumn
oriWirelessIfSupportedAuthenticationModes=_OriWirelessIfSupportedAuthenticationModes_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,36),_OriWirelessIfSupportedAuthenticationModes_Type())
oriWirelessIfSupportedAuthenticationModes.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfSupportedAuthenticationModes.setStatus(_A)
_OriWirelessIfSupportedCipherModes_Type=DisplayString
_OriWirelessIfSupportedCipherModes_Object=MibTableColumn
oriWirelessIfSupportedCipherModes=_OriWirelessIfSupportedCipherModes_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,37),_OriWirelessIfSupportedCipherModes_Type())
oriWirelessIfSupportedCipherModes.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfSupportedCipherModes.setStatus(_A)
class _OriWirelessIfQoSStatus_Type(ObjStatus):defaultValue=2
_OriWirelessIfQoSStatus_Type.__name__=_J
_OriWirelessIfQoSStatus_Object=MibTableColumn
oriWirelessIfQoSStatus=_OriWirelessIfQoSStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,38),_OriWirelessIfQoSStatus_Type())
oriWirelessIfQoSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfQoSStatus.setStatus(_A)
class _OriWirelessIfQoSMaxMediumThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,90))
_OriWirelessIfQoSMaxMediumThreshold_Type.__name__=_D
_OriWirelessIfQoSMaxMediumThreshold_Object=MibTableColumn
oriWirelessIfQoSMaxMediumThreshold=_OriWirelessIfQoSMaxMediumThreshold_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,39),_OriWirelessIfQoSMaxMediumThreshold_Type())
oriWirelessIfQoSMaxMediumThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfQoSMaxMediumThreshold.setStatus(_A)
class _OriWirelessIfAntennaGain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,35))
_OriWirelessIfAntennaGain_Type.__name__=_D
_OriWirelessIfAntennaGain_Object=MibTableColumn
oriWirelessIfAntennaGain=_OriWirelessIfAntennaGain_Object((1,3,6,1,4,1,11898,2,1,2,1,1,1,40),_OriWirelessIfAntennaGain_Type())
oriWirelessIfAntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfAntennaGain.setStatus(_A)
_OriWirelessIfSecurityTable_Object=MibTable
oriWirelessIfSecurityTable=_OriWirelessIfSecurityTable_Object((1,3,6,1,4,1,11898,2,1,2,1,2))
if mibBuilder.loadTexts:oriWirelessIfSecurityTable.setStatus(_A)
_OriWirelessIfSecurityEntry_Object=MibTableRow
oriWirelessIfSecurityEntry=_OriWirelessIfSecurityEntry_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1))
oriWirelessIfSecurityEntry.setIndexNames((0,_E,_A4))
if mibBuilder.loadTexts:oriWirelessIfSecurityEntry.setStatus(_A)
_OriWirelessIfSecurityIndex_Type=Integer32
_OriWirelessIfSecurityIndex_Object=MibTableColumn
oriWirelessIfSecurityIndex=_OriWirelessIfSecurityIndex_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,1),_OriWirelessIfSecurityIndex_Type())
oriWirelessIfSecurityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfSecurityIndex.setStatus(_A)
class _OriWirelessIfEncryptionOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_Z,2),('rcFour128',3),('aes',4)))
_OriWirelessIfEncryptionOptions_Type.__name__=_D
_OriWirelessIfEncryptionOptions_Object=MibTableColumn
oriWirelessIfEncryptionOptions=_OriWirelessIfEncryptionOptions_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,2),_OriWirelessIfEncryptionOptions_Type())
oriWirelessIfEncryptionOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfEncryptionOptions.setStatus(_A)
class _OriWirelessIfEncryptionStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfEncryptionStatus_Type.__name__=_D
_OriWirelessIfEncryptionStatus_Object=MibTableColumn
oriWirelessIfEncryptionStatus=_OriWirelessIfEncryptionStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,3),_OriWirelessIfEncryptionStatus_Type())
oriWirelessIfEncryptionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfEncryptionStatus.setStatus(_H)
_OriWirelessIfEncryptionKey1_Type=DisplayString
_OriWirelessIfEncryptionKey1_Object=MibTableColumn
oriWirelessIfEncryptionKey1=_OriWirelessIfEncryptionKey1_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,4),_OriWirelessIfEncryptionKey1_Type())
oriWirelessIfEncryptionKey1.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfEncryptionKey1.setStatus(_A)
_OriWirelessIfEncryptionKey2_Type=DisplayString
_OriWirelessIfEncryptionKey2_Object=MibTableColumn
oriWirelessIfEncryptionKey2=_OriWirelessIfEncryptionKey2_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,5),_OriWirelessIfEncryptionKey2_Type())
oriWirelessIfEncryptionKey2.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfEncryptionKey2.setStatus(_A)
_OriWirelessIfEncryptionKey3_Type=DisplayString
_OriWirelessIfEncryptionKey3_Object=MibTableColumn
oriWirelessIfEncryptionKey3=_OriWirelessIfEncryptionKey3_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,6),_OriWirelessIfEncryptionKey3_Type())
oriWirelessIfEncryptionKey3.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfEncryptionKey3.setStatus(_A)
_OriWirelessIfEncryptionKey4_Type=DisplayString
_OriWirelessIfEncryptionKey4_Object=MibTableColumn
oriWirelessIfEncryptionKey4=_OriWirelessIfEncryptionKey4_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,7),_OriWirelessIfEncryptionKey4_Type())
oriWirelessIfEncryptionKey4.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfEncryptionKey4.setStatus(_A)
class _OriWirelessIfEncryptionTxKey_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_OriWirelessIfEncryptionTxKey_Type.__name__=_D
_OriWirelessIfEncryptionTxKey_Object=MibTableColumn
oriWirelessIfEncryptionTxKey=_OriWirelessIfEncryptionTxKey_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,8),_OriWirelessIfEncryptionTxKey_Type())
oriWirelessIfEncryptionTxKey.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfEncryptionTxKey.setStatus(_A)
class _OriWirelessIfDenyNonEncryptedData_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfDenyNonEncryptedData_Type.__name__=_D
_OriWirelessIfDenyNonEncryptedData_Object=MibTableColumn
oriWirelessIfDenyNonEncryptedData=_OriWirelessIfDenyNonEncryptedData_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,9),_OriWirelessIfDenyNonEncryptedData_Type())
oriWirelessIfDenyNonEncryptedData.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfDenyNonEncryptedData.setStatus(_A)
_OriWirelessIfProfileCode_Type=Integer32
_OriWirelessIfProfileCode_Object=MibTableColumn
oriWirelessIfProfileCode=_OriWirelessIfProfileCode_Object((1,3,6,1,4,1,11898,2,1,2,1,2,1,10),_OriWirelessIfProfileCode_Type())
oriWirelessIfProfileCode.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfProfileCode.setStatus(_A)
_OriWirelessIfSSIDTable_Object=MibTable
oriWirelessIfSSIDTable=_OriWirelessIfSSIDTable_Object((1,3,6,1,4,1,11898,2,1,2,1,3))
if mibBuilder.loadTexts:oriWirelessIfSSIDTable.setStatus(_A)
_OriWirelessIfSSIDTableEntry_Object=MibTableRow
oriWirelessIfSSIDTableEntry=_OriWirelessIfSSIDTableEntry_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1))
oriWirelessIfSSIDTableEntry.setIndexNames((0,_S,_T),(0,_E,_A5))
if mibBuilder.loadTexts:oriWirelessIfSSIDTableEntry.setStatus(_A)
class _OriWirelessIfSSIDTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_OriWirelessIfSSIDTableIndex_Type.__name__=_D
_OriWirelessIfSSIDTableIndex_Object=MibTableColumn
oriWirelessIfSSIDTableIndex=_OriWirelessIfSSIDTableIndex_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,1),_OriWirelessIfSSIDTableIndex_Type())
oriWirelessIfSSIDTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableIndex.setStatus(_A)
class _OriWirelessIfSSIDTableSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OriWirelessIfSSIDTableSSID_Type.__name__=_O
_OriWirelessIfSSIDTableSSID_Object=MibTableColumn
oriWirelessIfSSIDTableSSID=_OriWirelessIfSSIDTableSSID_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,2),_OriWirelessIfSSIDTableSSID_Type())
oriWirelessIfSSIDTableSSID.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableSSID.setStatus(_A)
class _OriWirelessIfSSIDTableVLANID_Type(VlanId):defaultValue=-1
_OriWirelessIfSSIDTableVLANID_Type.__name__=_a
_OriWirelessIfSSIDTableVLANID_Object=MibTableColumn
oriWirelessIfSSIDTableVLANID=_OriWirelessIfSSIDTableVLANID_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,3),_OriWirelessIfSSIDTableVLANID_Type())
oriWirelessIfSSIDTableVLANID.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableVLANID.setStatus(_A)
_OriWirelessIfSSIDTableStatus_Type=RowStatus
_OriWirelessIfSSIDTableStatus_Object=MibTableColumn
oriWirelessIfSSIDTableStatus=_OriWirelessIfSSIDTableStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,4),_OriWirelessIfSSIDTableStatus_Type())
oriWirelessIfSSIDTableStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableStatus.setStatus(_A)
class _OriWirelessIfSSIDTableSecurityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_b,2),('mixed',3),('wpa',4),('wpa-psk',5),(_Z,6)))
_OriWirelessIfSSIDTableSecurityMode_Type.__name__=_D
_OriWirelessIfSSIDTableSecurityMode_Object=MibTableColumn
oriWirelessIfSSIDTableSecurityMode=_OriWirelessIfSSIDTableSecurityMode_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,5),_OriWirelessIfSSIDTableSecurityMode_Type())
oriWirelessIfSSIDTableSecurityMode.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableSecurityMode.setStatus(_H)
class _OriWirelessIfSSIDTableBroadcastSSID_Type(ObjStatus):defaultValue=2
_OriWirelessIfSSIDTableBroadcastSSID_Type.__name__=_J
_OriWirelessIfSSIDTableBroadcastSSID_Object=MibTableColumn
oriWirelessIfSSIDTableBroadcastSSID=_OriWirelessIfSSIDTableBroadcastSSID_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,6),_OriWirelessIfSSIDTableBroadcastSSID_Type())
oriWirelessIfSSIDTableBroadcastSSID.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableBroadcastSSID.setStatus(_A)
class _OriWirelessIfSSIDTableClosedSystem_Type(ObjStatus):defaultValue=1
_OriWirelessIfSSIDTableClosedSystem_Type.__name__=_J
_OriWirelessIfSSIDTableClosedSystem_Object=MibTableColumn
oriWirelessIfSSIDTableClosedSystem=_OriWirelessIfSSIDTableClosedSystem_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,7),_OriWirelessIfSSIDTableClosedSystem_Type())
oriWirelessIfSSIDTableClosedSystem.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableClosedSystem.setStatus(_A)
_OriWirelessIfSSIDTableSupportedSecurityModes_Type=DisplayString
_OriWirelessIfSSIDTableSupportedSecurityModes_Object=MibTableColumn
oriWirelessIfSSIDTableSupportedSecurityModes=_OriWirelessIfSSIDTableSupportedSecurityModes_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,8),_OriWirelessIfSSIDTableSupportedSecurityModes_Type())
oriWirelessIfSSIDTableSupportedSecurityModes.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableSupportedSecurityModes.setStatus(_H)
_OriWirelessIfSSIDTableEncryptionKey0_Type=WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey0_Object=MibTableColumn
oriWirelessIfSSIDTableEncryptionKey0=_OriWirelessIfSSIDTableEncryptionKey0_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,9),_OriWirelessIfSSIDTableEncryptionKey0_Type())
oriWirelessIfSSIDTableEncryptionKey0.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableEncryptionKey0.setStatus(_H)
_OriWirelessIfSSIDTableEncryptionKey1_Type=WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey1_Object=MibTableColumn
oriWirelessIfSSIDTableEncryptionKey1=_OriWirelessIfSSIDTableEncryptionKey1_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,10),_OriWirelessIfSSIDTableEncryptionKey1_Type())
oriWirelessIfSSIDTableEncryptionKey1.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableEncryptionKey1.setStatus(_H)
_OriWirelessIfSSIDTableEncryptionKey2_Type=WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey2_Object=MibTableColumn
oriWirelessIfSSIDTableEncryptionKey2=_OriWirelessIfSSIDTableEncryptionKey2_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,11),_OriWirelessIfSSIDTableEncryptionKey2_Type())
oriWirelessIfSSIDTableEncryptionKey2.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableEncryptionKey2.setStatus(_H)
_OriWirelessIfSSIDTableEncryptionKey3_Type=WEPKeyType
_OriWirelessIfSSIDTableEncryptionKey3_Object=MibTableColumn
oriWirelessIfSSIDTableEncryptionKey3=_OriWirelessIfSSIDTableEncryptionKey3_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,12),_OriWirelessIfSSIDTableEncryptionKey3_Type())
oriWirelessIfSSIDTableEncryptionKey3.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableEncryptionKey3.setStatus(_H)
class _OriWirelessIfSSIDTableEncryptionTxKey_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_OriWirelessIfSSIDTableEncryptionTxKey_Type.__name__=_D
_OriWirelessIfSSIDTableEncryptionTxKey_Object=MibTableColumn
oriWirelessIfSSIDTableEncryptionTxKey=_OriWirelessIfSSIDTableEncryptionTxKey_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,13),_OriWirelessIfSSIDTableEncryptionTxKey_Type())
oriWirelessIfSSIDTableEncryptionTxKey.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableEncryptionTxKey.setStatus(_H)
class _OriWirelessIfSSIDTableEncryptionKeyLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),(_m,3)))
_OriWirelessIfSSIDTableEncryptionKeyLength_Type.__name__=_D
_OriWirelessIfSSIDTableEncryptionKeyLength_Object=MibTableColumn
oriWirelessIfSSIDTableEncryptionKeyLength=_OriWirelessIfSSIDTableEncryptionKeyLength_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,14),_OriWirelessIfSSIDTableEncryptionKeyLength_Type())
oriWirelessIfSSIDTableEncryptionKeyLength.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableEncryptionKeyLength.setStatus(_H)
class _OriWirelessIfSSIDTableRekeyingInterval_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(300,65535))
_OriWirelessIfSSIDTableRekeyingInterval_Type.__name__=_D
_OriWirelessIfSSIDTableRekeyingInterval_Object=MibTableColumn
oriWirelessIfSSIDTableRekeyingInterval=_OriWirelessIfSSIDTableRekeyingInterval_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,15),_OriWirelessIfSSIDTableRekeyingInterval_Type())
oriWirelessIfSSIDTableRekeyingInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableRekeyingInterval.setStatus(_A)
class _OriWirelessIfSSIDTablePSKValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_OriWirelessIfSSIDTablePSKValue_Type.__name__=_V
_OriWirelessIfSSIDTablePSKValue_Object=MibTableColumn
oriWirelessIfSSIDTablePSKValue=_OriWirelessIfSSIDTablePSKValue_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,16),_OriWirelessIfSSIDTablePSKValue_Type())
oriWirelessIfSSIDTablePSKValue.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTablePSKValue.setStatus(_H)
_OriWirelessIfSSIDTablePSKPassPhrase_Type=DisplayString
_OriWirelessIfSSIDTablePSKPassPhrase_Object=MibTableColumn
oriWirelessIfSSIDTablePSKPassPhrase=_OriWirelessIfSSIDTablePSKPassPhrase_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,17),_OriWirelessIfSSIDTablePSKPassPhrase_Type())
oriWirelessIfSSIDTablePSKPassPhrase.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTablePSKPassPhrase.setStatus(_H)
class _OriWirelessIfSSIDTableDenyNonEncryptedData_Type(ObjStatus):defaultValue=1
_OriWirelessIfSSIDTableDenyNonEncryptedData_Type.__name__=_J
_OriWirelessIfSSIDTableDenyNonEncryptedData_Object=MibTableColumn
oriWirelessIfSSIDTableDenyNonEncryptedData=_OriWirelessIfSSIDTableDenyNonEncryptedData_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,18),_OriWirelessIfSSIDTableDenyNonEncryptedData_Type())
oriWirelessIfSSIDTableDenyNonEncryptedData.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableDenyNonEncryptedData.setStatus(_H)
class _OriWirelessIfSSIDTableSSIDAuthorizationStatus_Type(ObjStatus):defaultValue=2
_OriWirelessIfSSIDTableSSIDAuthorizationStatus_Type.__name__=_J
_OriWirelessIfSSIDTableSSIDAuthorizationStatus_Object=MibTableColumn
oriWirelessIfSSIDTableSSIDAuthorizationStatus=_OriWirelessIfSSIDTableSSIDAuthorizationStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,19),_OriWirelessIfSSIDTableSSIDAuthorizationStatus_Type())
oriWirelessIfSSIDTableSSIDAuthorizationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableSSIDAuthorizationStatus.setStatus(_A)
class _OriWirelessIfSSIDTableMACAccessControl_Type(ObjStatus):defaultValue=2
_OriWirelessIfSSIDTableMACAccessControl_Type.__name__=_J
_OriWirelessIfSSIDTableMACAccessControl_Object=MibTableColumn
oriWirelessIfSSIDTableMACAccessControl=_OriWirelessIfSSIDTableMACAccessControl_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,20),_OriWirelessIfSSIDTableMACAccessControl_Type())
oriWirelessIfSSIDTableMACAccessControl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableMACAccessControl.setStatus(_A)
class _OriWirelessIfSSIDTableRADIUSMACAccessControl_Type(ObjStatus):defaultValue=2
_OriWirelessIfSSIDTableRADIUSMACAccessControl_Type.__name__=_J
_OriWirelessIfSSIDTableRADIUSMACAccessControl_Object=MibTableColumn
oriWirelessIfSSIDTableRADIUSMACAccessControl=_OriWirelessIfSSIDTableRADIUSMACAccessControl_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,21),_OriWirelessIfSSIDTableRADIUSMACAccessControl_Type())
oriWirelessIfSSIDTableRADIUSMACAccessControl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableRADIUSMACAccessControl.setStatus(_A)
_OriWirelessIfSSIDTableSecurityProfile_Type=Integer32
_OriWirelessIfSSIDTableSecurityProfile_Object=MibTableColumn
oriWirelessIfSSIDTableSecurityProfile=_OriWirelessIfSSIDTableSecurityProfile_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,22),_OriWirelessIfSSIDTableSecurityProfile_Type())
oriWirelessIfSSIDTableSecurityProfile.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableSecurityProfile.setStatus(_A)
_OriWirelessIfSSIDTableRADIUSDot1xProfile_Type=DisplayString
_OriWirelessIfSSIDTableRADIUSDot1xProfile_Object=MibTableColumn
oriWirelessIfSSIDTableRADIUSDot1xProfile=_OriWirelessIfSSIDTableRADIUSDot1xProfile_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,23),_OriWirelessIfSSIDTableRADIUSDot1xProfile_Type())
oriWirelessIfSSIDTableRADIUSDot1xProfile.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableRADIUSDot1xProfile.setStatus(_A)
_OriWirelessIfSSIDTableRADIUSMACAuthProfile_Type=DisplayString
_OriWirelessIfSSIDTableRADIUSMACAuthProfile_Object=MibTableColumn
oriWirelessIfSSIDTableRADIUSMACAuthProfile=_OriWirelessIfSSIDTableRADIUSMACAuthProfile_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,24),_OriWirelessIfSSIDTableRADIUSMACAuthProfile_Type())
oriWirelessIfSSIDTableRADIUSMACAuthProfile.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableRADIUSMACAuthProfile.setStatus(_A)
class _OriWirelessIfSSIDTableRADIUSAccountingStatus_Type(ObjStatus):defaultValue=2
_OriWirelessIfSSIDTableRADIUSAccountingStatus_Type.__name__=_J
_OriWirelessIfSSIDTableRADIUSAccountingStatus_Object=MibTableColumn
oriWirelessIfSSIDTableRADIUSAccountingStatus=_OriWirelessIfSSIDTableRADIUSAccountingStatus_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,25),_OriWirelessIfSSIDTableRADIUSAccountingStatus_Type())
oriWirelessIfSSIDTableRADIUSAccountingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableRADIUSAccountingStatus.setStatus(_A)
_OriWirelessIfSSIDTableRADIUSAccountingProfile_Type=DisplayString
_OriWirelessIfSSIDTableRADIUSAccountingProfile_Object=MibTableColumn
oriWirelessIfSSIDTableRADIUSAccountingProfile=_OriWirelessIfSSIDTableRADIUSAccountingProfile_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,26),_OriWirelessIfSSIDTableRADIUSAccountingProfile_Type())
oriWirelessIfSSIDTableRADIUSAccountingProfile.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableRADIUSAccountingProfile.setStatus(_A)
_OriWirelessIfSSIDTableQoSPolicy_Type=Integer32
_OriWirelessIfSSIDTableQoSPolicy_Object=MibTableColumn
oriWirelessIfSSIDTableQoSPolicy=_OriWirelessIfSSIDTableQoSPolicy_Object((1,3,6,1,4,1,11898,2,1,2,1,3,1,27),_OriWirelessIfSSIDTableQoSPolicy_Type())
oriWirelessIfSSIDTableQoSPolicy.setMaxAccess(_I)
if mibBuilder.loadTexts:oriWirelessIfSSIDTableQoSPolicy.setStatus(_A)
class _OriWirelessIfTxPowerControl_Type(ObjStatus):defaultValue=2
_OriWirelessIfTxPowerControl_Type.__name__=_J
_OriWirelessIfTxPowerControl_Object=MibScalar
oriWirelessIfTxPowerControl=_OriWirelessIfTxPowerControl_Object((1,3,6,1,4,1,11898,2,1,2,1,4),_OriWirelessIfTxPowerControl_Type())
oriWirelessIfTxPowerControl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfTxPowerControl.setStatus(_A)
_OrinocoEthernetIf_ObjectIdentity=ObjectIdentity
orinocoEthernetIf=_OrinocoEthernetIf_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,2))
_OriEthernetIfConfigTable_Object=MibTable
oriEthernetIfConfigTable=_OriEthernetIfConfigTable_Object((1,3,6,1,4,1,11898,2,1,2,2,1))
if mibBuilder.loadTexts:oriEthernetIfConfigTable.setStatus(_A)
_OriEthernetIfConfigTableEntry_Object=MibTableRow
oriEthernetIfConfigTableEntry=_OriEthernetIfConfigTableEntry_Object((1,3,6,1,4,1,11898,2,1,2,2,1,1))
oriEthernetIfConfigTableEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:oriEthernetIfConfigTableEntry.setStatus(_A)
_OriEthernetIfConfigTableIndex_Type=Integer32
_OriEthernetIfConfigTableIndex_Object=MibTableColumn
oriEthernetIfConfigTableIndex=_OriEthernetIfConfigTableIndex_Object((1,3,6,1,4,1,11898,2,1,2,2,1,1,1),_OriEthernetIfConfigTableIndex_Type())
oriEthernetIfConfigTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriEthernetIfConfigTableIndex.setStatus(_A)
class _OriEthernetIfConfigSettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('tenMegabitPerSecHalfDuplex',1),('tenMegabitPerSecFullDuplex',2),('tenMegabitPerSecAutoDuplex',3),('onehundredMegabitPerSecHalfDuplex',4),('onehundredMegabitPerSecFullDuplex',5),('autoSpeedHalfDuplex',6),('autoSpeedAutoDuplex',7),('onehundredMegabitPerSecAutoDuplex',8)))
_OriEthernetIfConfigSettings_Type.__name__=_D
_OriEthernetIfConfigSettings_Object=MibTableColumn
oriEthernetIfConfigSettings=_OriEthernetIfConfigSettings_Object((1,3,6,1,4,1,11898,2,1,2,2,1,1,2),_OriEthernetIfConfigSettings_Type())
oriEthernetIfConfigSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:oriEthernetIfConfigSettings.setStatus(_A)
_OriEthernetIfConfigBandwidthLimitIn_Type=Gauge32
_OriEthernetIfConfigBandwidthLimitIn_Object=MibTableColumn
oriEthernetIfConfigBandwidthLimitIn=_OriEthernetIfConfigBandwidthLimitIn_Object((1,3,6,1,4,1,11898,2,1,2,2,1,1,3),_OriEthernetIfConfigBandwidthLimitIn_Type())
oriEthernetIfConfigBandwidthLimitIn.setMaxAccess(_B)
if mibBuilder.loadTexts:oriEthernetIfConfigBandwidthLimitIn.setStatus(_A)
_OriEthernetIfConfigBandwidthLimitOut_Type=Gauge32
_OriEthernetIfConfigBandwidthLimitOut_Object=MibTableColumn
oriEthernetIfConfigBandwidthLimitOut=_OriEthernetIfConfigBandwidthLimitOut_Object((1,3,6,1,4,1,11898,2,1,2,2,1,1,4),_OriEthernetIfConfigBandwidthLimitOut_Type())
oriEthernetIfConfigBandwidthLimitOut.setMaxAccess(_B)
if mibBuilder.loadTexts:oriEthernetIfConfigBandwidthLimitOut.setStatus(_A)
_OriIfWANInterfaceMACAddress_Type=PhysAddress
_OriIfWANInterfaceMACAddress_Object=MibScalar
oriIfWANInterfaceMACAddress=_OriIfWANInterfaceMACAddress_Object((1,3,6,1,4,1,11898,2,1,2,4),_OriIfWANInterfaceMACAddress_Type())
oriIfWANInterfaceMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIfWANInterfaceMACAddress.setStatus(_A)
_OrinocoWORPIf_ObjectIdentity=ObjectIdentity
orinocoWORPIf=_OrinocoWORPIf_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5))
_OriWORPIfConfigTable_Object=MibTable
oriWORPIfConfigTable=_OriWORPIfConfigTable_Object((1,3,6,1,4,1,11898,2,1,2,5,1))
if mibBuilder.loadTexts:oriWORPIfConfigTable.setStatus(_A)
_OriWORPIfConfigTableEntry_Object=MibTableRow
oriWORPIfConfigTableEntry=_OriWORPIfConfigTableEntry_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1))
oriWORPIfConfigTableEntry.setIndexNames((0,_S,_T))
if mibBuilder.loadTexts:oriWORPIfConfigTableEntry.setStatus(_A)
class _OriWORPIfConfigTableMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),('ap',2),('base',3),('satellite',4)))
_OriWORPIfConfigTableMode_Type.__name__=_D
_OriWORPIfConfigTableMode_Object=MibTableColumn
oriWORPIfConfigTableMode=_OriWORPIfConfigTableMode_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1,1),_OriWORPIfConfigTableMode_Type())
oriWORPIfConfigTableMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfConfigTableMode.setStatus(_A)
_OriWORPIfConfigTableBaseStationName_Type=DisplayString
_OriWORPIfConfigTableBaseStationName_Object=MibTableColumn
oriWORPIfConfigTableBaseStationName=_OriWORPIfConfigTableBaseStationName_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1,2),_OriWORPIfConfigTableBaseStationName_Type())
oriWORPIfConfigTableBaseStationName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfConfigTableBaseStationName.setStatus(_A)
_OriWORPIfConfigTableMaxSatellites_Type=Integer32
_OriWORPIfConfigTableMaxSatellites_Object=MibTableColumn
oriWORPIfConfigTableMaxSatellites=_OriWORPIfConfigTableMaxSatellites_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1,3),_OriWORPIfConfigTableMaxSatellites_Type())
oriWORPIfConfigTableMaxSatellites.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfConfigTableMaxSatellites.setStatus(_A)
class _OriWORPIfConfigTableRegistrationTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_OriWORPIfConfigTableRegistrationTimeout_Type.__name__=_D
_OriWORPIfConfigTableRegistrationTimeout_Object=MibTableColumn
oriWORPIfConfigTableRegistrationTimeout=_OriWORPIfConfigTableRegistrationTimeout_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1,4),_OriWORPIfConfigTableRegistrationTimeout_Type())
oriWORPIfConfigTableRegistrationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfConfigTableRegistrationTimeout.setStatus(_A)
class _OriWORPIfConfigTableRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_OriWORPIfConfigTableRetries_Type.__name__=_D
_OriWORPIfConfigTableRetries_Object=MibTableColumn
oriWORPIfConfigTableRetries=_OriWORPIfConfigTableRetries_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1,5),_OriWORPIfConfigTableRetries_Type())
oriWORPIfConfigTableRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfConfigTableRetries.setStatus(_A)
_OriWORPIfConfigTableNetworkSecret_Type=DisplayString
_OriWORPIfConfigTableNetworkSecret_Object=MibTableColumn
oriWORPIfConfigTableNetworkSecret=_OriWORPIfConfigTableNetworkSecret_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1,6),_OriWORPIfConfigTableNetworkSecret_Type())
oriWORPIfConfigTableNetworkSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfConfigTableNetworkSecret.setStatus(_A)
class _OriWORPIfConfigTableNoSleepMode_Type(ObjStatus):defaultValue=2
_OriWORPIfConfigTableNoSleepMode_Type.__name__=_J
_OriWORPIfConfigTableNoSleepMode_Object=MibTableColumn
oriWORPIfConfigTableNoSleepMode=_OriWORPIfConfigTableNoSleepMode_Object((1,3,6,1,4,1,11898,2,1,2,5,1,1,7),_OriWORPIfConfigTableNoSleepMode_Type())
oriWORPIfConfigTableNoSleepMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfConfigTableNoSleepMode.setStatus(_A)
_OriWORPIfStatTable_Object=MibTable
oriWORPIfStatTable=_OriWORPIfStatTable_Object((1,3,6,1,4,1,11898,2,1,2,5,2))
if mibBuilder.loadTexts:oriWORPIfStatTable.setStatus(_A)
_OriWORPIfStatTableEntry_Object=MibTableRow
oriWORPIfStatTableEntry=_OriWORPIfStatTableEntry_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1))
oriWORPIfStatTableEntry.setIndexNames((0,_S,_T))
if mibBuilder.loadTexts:oriWORPIfStatTableEntry.setStatus(_A)
_OriWORPIfStatTableRemotePartners_Type=Counter32
_OriWORPIfStatTableRemotePartners_Object=MibTableColumn
oriWORPIfStatTableRemotePartners=_OriWORPIfStatTableRemotePartners_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,1),_OriWORPIfStatTableRemotePartners_Type())
oriWORPIfStatTableRemotePartners.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRemotePartners.setStatus(_A)
class _OriWORPIfStatTableAverageLocalSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfStatTableAverageLocalSignal_Type.__name__=_D
_OriWORPIfStatTableAverageLocalSignal_Object=MibTableColumn
oriWORPIfStatTableAverageLocalSignal=_OriWORPIfStatTableAverageLocalSignal_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,2),_OriWORPIfStatTableAverageLocalSignal_Type())
oriWORPIfStatTableAverageLocalSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableAverageLocalSignal.setStatus(_A)
class _OriWORPIfStatTableAverageLocalNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfStatTableAverageLocalNoise_Type.__name__=_D
_OriWORPIfStatTableAverageLocalNoise_Object=MibTableColumn
oriWORPIfStatTableAverageLocalNoise=_OriWORPIfStatTableAverageLocalNoise_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,3),_OriWORPIfStatTableAverageLocalNoise_Type())
oriWORPIfStatTableAverageLocalNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableAverageLocalNoise.setStatus(_A)
class _OriWORPIfStatTableAverageRemoteSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfStatTableAverageRemoteSignal_Type.__name__=_D
_OriWORPIfStatTableAverageRemoteSignal_Object=MibTableColumn
oriWORPIfStatTableAverageRemoteSignal=_OriWORPIfStatTableAverageRemoteSignal_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,4),_OriWORPIfStatTableAverageRemoteSignal_Type())
oriWORPIfStatTableAverageRemoteSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableAverageRemoteSignal.setStatus(_A)
class _OriWORPIfStatTableAverageRemoteNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfStatTableAverageRemoteNoise_Type.__name__=_D
_OriWORPIfStatTableAverageRemoteNoise_Object=MibTableColumn
oriWORPIfStatTableAverageRemoteNoise=_OriWORPIfStatTableAverageRemoteNoise_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,5),_OriWORPIfStatTableAverageRemoteNoise_Type())
oriWORPIfStatTableAverageRemoteNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableAverageRemoteNoise.setStatus(_A)
_OriWORPIfStatTableBaseStationAnnounces_Type=Counter32
_OriWORPIfStatTableBaseStationAnnounces_Object=MibTableColumn
oriWORPIfStatTableBaseStationAnnounces=_OriWORPIfStatTableBaseStationAnnounces_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,6),_OriWORPIfStatTableBaseStationAnnounces_Type())
oriWORPIfStatTableBaseStationAnnounces.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableBaseStationAnnounces.setStatus(_A)
_OriWORPIfStatTableRegistrationRequests_Type=Counter32
_OriWORPIfStatTableRegistrationRequests_Object=MibTableColumn
oriWORPIfStatTableRegistrationRequests=_OriWORPIfStatTableRegistrationRequests_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,7),_OriWORPIfStatTableRegistrationRequests_Type())
oriWORPIfStatTableRegistrationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRegistrationRequests.setStatus(_A)
_OriWORPIfStatTableRegistrationRejects_Type=Counter32
_OriWORPIfStatTableRegistrationRejects_Object=MibTableColumn
oriWORPIfStatTableRegistrationRejects=_OriWORPIfStatTableRegistrationRejects_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,8),_OriWORPIfStatTableRegistrationRejects_Type())
oriWORPIfStatTableRegistrationRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRegistrationRejects.setStatus(_A)
_OriWORPIfStatTableAuthenticationRequests_Type=Counter32
_OriWORPIfStatTableAuthenticationRequests_Object=MibTableColumn
oriWORPIfStatTableAuthenticationRequests=_OriWORPIfStatTableAuthenticationRequests_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,9),_OriWORPIfStatTableAuthenticationRequests_Type())
oriWORPIfStatTableAuthenticationRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableAuthenticationRequests.setStatus(_A)
_OriWORPIfStatTableAuthenticationConfirms_Type=Counter32
_OriWORPIfStatTableAuthenticationConfirms_Object=MibTableColumn
oriWORPIfStatTableAuthenticationConfirms=_OriWORPIfStatTableAuthenticationConfirms_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,10),_OriWORPIfStatTableAuthenticationConfirms_Type())
oriWORPIfStatTableAuthenticationConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableAuthenticationConfirms.setStatus(_A)
_OriWORPIfStatTableRegistrationAttempts_Type=Counter32
_OriWORPIfStatTableRegistrationAttempts_Object=MibTableColumn
oriWORPIfStatTableRegistrationAttempts=_OriWORPIfStatTableRegistrationAttempts_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,11),_OriWORPIfStatTableRegistrationAttempts_Type())
oriWORPIfStatTableRegistrationAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRegistrationAttempts.setStatus(_A)
_OriWORPIfStatTableRegistrationIncompletes_Type=Counter32
_OriWORPIfStatTableRegistrationIncompletes_Object=MibTableColumn
oriWORPIfStatTableRegistrationIncompletes=_OriWORPIfStatTableRegistrationIncompletes_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,12),_OriWORPIfStatTableRegistrationIncompletes_Type())
oriWORPIfStatTableRegistrationIncompletes.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRegistrationIncompletes.setStatus(_A)
_OriWORPIfStatTableRegistrationTimeouts_Type=Counter32
_OriWORPIfStatTableRegistrationTimeouts_Object=MibTableColumn
oriWORPIfStatTableRegistrationTimeouts=_OriWORPIfStatTableRegistrationTimeouts_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,13),_OriWORPIfStatTableRegistrationTimeouts_Type())
oriWORPIfStatTableRegistrationTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRegistrationTimeouts.setStatus(_A)
class _OriWORPIfStatTableRegistrationLastReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),('noMoreAllowed',2),('incorrectParameter',3),('roaming',4),('timeout',5),('lowQuality',6)))
_OriWORPIfStatTableRegistrationLastReason_Type.__name__=_D
_OriWORPIfStatTableRegistrationLastReason_Object=MibTableColumn
oriWORPIfStatTableRegistrationLastReason=_OriWORPIfStatTableRegistrationLastReason_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,14),_OriWORPIfStatTableRegistrationLastReason_Type())
oriWORPIfStatTableRegistrationLastReason.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRegistrationLastReason.setStatus(_A)
_OriWORPIfStatTablePollData_Type=Counter32
_OriWORPIfStatTablePollData_Object=MibTableColumn
oriWORPIfStatTablePollData=_OriWORPIfStatTablePollData_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,15),_OriWORPIfStatTablePollData_Type())
oriWORPIfStatTablePollData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTablePollData.setStatus(_A)
_OriWORPIfStatTablePollNoData_Type=Counter32
_OriWORPIfStatTablePollNoData_Object=MibTableColumn
oriWORPIfStatTablePollNoData=_OriWORPIfStatTablePollNoData_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,16),_OriWORPIfStatTablePollNoData_Type())
oriWORPIfStatTablePollNoData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTablePollNoData.setStatus(_A)
_OriWORPIfStatTableReplyData_Type=Counter32
_OriWORPIfStatTableReplyData_Object=MibTableColumn
oriWORPIfStatTableReplyData=_OriWORPIfStatTableReplyData_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,17),_OriWORPIfStatTableReplyData_Type())
oriWORPIfStatTableReplyData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableReplyData.setStatus(_A)
_OriWORPIfStatTableReplyMoreData_Type=Counter32
_OriWORPIfStatTableReplyMoreData_Object=MibTableColumn
oriWORPIfStatTableReplyMoreData=_OriWORPIfStatTableReplyMoreData_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,18),_OriWORPIfStatTableReplyMoreData_Type())
oriWORPIfStatTableReplyMoreData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableReplyMoreData.setStatus(_A)
_OriWORPIfStatTableReplyNoData_Type=Counter32
_OriWORPIfStatTableReplyNoData_Object=MibTableColumn
oriWORPIfStatTableReplyNoData=_OriWORPIfStatTableReplyNoData_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,19),_OriWORPIfStatTableReplyNoData_Type())
oriWORPIfStatTableReplyNoData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableReplyNoData.setStatus(_A)
_OriWORPIfStatTableRequestForService_Type=Counter32
_OriWORPIfStatTableRequestForService_Object=MibTableColumn
oriWORPIfStatTableRequestForService=_OriWORPIfStatTableRequestForService_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,20),_OriWORPIfStatTableRequestForService_Type())
oriWORPIfStatTableRequestForService.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableRequestForService.setStatus(_A)
_OriWORPIfStatTableSendSuccess_Type=Counter32
_OriWORPIfStatTableSendSuccess_Object=MibTableColumn
oriWORPIfStatTableSendSuccess=_OriWORPIfStatTableSendSuccess_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,21),_OriWORPIfStatTableSendSuccess_Type())
oriWORPIfStatTableSendSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableSendSuccess.setStatus(_A)
_OriWORPIfStatTableSendRetries_Type=Counter32
_OriWORPIfStatTableSendRetries_Object=MibTableColumn
oriWORPIfStatTableSendRetries=_OriWORPIfStatTableSendRetries_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,22),_OriWORPIfStatTableSendRetries_Type())
oriWORPIfStatTableSendRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableSendRetries.setStatus(_A)
_OriWORPIfStatTableSendFailures_Type=Counter32
_OriWORPIfStatTableSendFailures_Object=MibTableColumn
oriWORPIfStatTableSendFailures=_OriWORPIfStatTableSendFailures_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,23),_OriWORPIfStatTableSendFailures_Type())
oriWORPIfStatTableSendFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableSendFailures.setStatus(_A)
_OriWORPIfStatTableReceiveSuccess_Type=Counter32
_OriWORPIfStatTableReceiveSuccess_Object=MibTableColumn
oriWORPIfStatTableReceiveSuccess=_OriWORPIfStatTableReceiveSuccess_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,24),_OriWORPIfStatTableReceiveSuccess_Type())
oriWORPIfStatTableReceiveSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableReceiveSuccess.setStatus(_A)
_OriWORPIfStatTableReceiveRetries_Type=Counter32
_OriWORPIfStatTableReceiveRetries_Object=MibTableColumn
oriWORPIfStatTableReceiveRetries=_OriWORPIfStatTableReceiveRetries_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,25),_OriWORPIfStatTableReceiveRetries_Type())
oriWORPIfStatTableReceiveRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableReceiveRetries.setStatus(_A)
_OriWORPIfStatTableReceiveFailures_Type=Counter32
_OriWORPIfStatTableReceiveFailures_Object=MibTableColumn
oriWORPIfStatTableReceiveFailures=_OriWORPIfStatTableReceiveFailures_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,26),_OriWORPIfStatTableReceiveFailures_Type())
oriWORPIfStatTableReceiveFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTableReceiveFailures.setStatus(_A)
_OriWORPIfStatTablePollNoReplies_Type=Counter32
_OriWORPIfStatTablePollNoReplies_Object=MibTableColumn
oriWORPIfStatTablePollNoReplies=_OriWORPIfStatTablePollNoReplies_Object((1,3,6,1,4,1,11898,2,1,2,5,2,1,27),_OriWORPIfStatTablePollNoReplies_Type())
oriWORPIfStatTablePollNoReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfStatTablePollNoReplies.setStatus(_A)
_OrinocoWORPIfSat_ObjectIdentity=ObjectIdentity
orinocoWORPIfSat=_OrinocoWORPIfSat_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,3))
_OrinocoWORPIfSatConfig_ObjectIdentity=ObjectIdentity
orinocoWORPIfSatConfig=_OrinocoWORPIfSatConfig_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,3,1))
class _OriWORPIfSatConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_W,2)))
_OriWORPIfSatConfigStatus_Type.__name__=_D
_OriWORPIfSatConfigStatus_Object=MibScalar
oriWORPIfSatConfigStatus=_OriWORPIfSatConfigStatus_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,1),_OriWORPIfSatConfigStatus_Type())
oriWORPIfSatConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigStatus.setStatus(_A)
_OriWORPIfSatConfigTable_Object=MibTable
oriWORPIfSatConfigTable=_OriWORPIfSatConfigTable_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2))
if mibBuilder.loadTexts:oriWORPIfSatConfigTable.setStatus(_A)
_OriWORPIfSatConfigTableEntry_Object=MibTableRow
oriWORPIfSatConfigTableEntry=_OriWORPIfSatConfigTableEntry_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1))
oriWORPIfSatConfigTableEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:oriWORPIfSatConfigTableEntry.setStatus(_A)
_OriWORPIfSatConfigTableIndex_Type=Integer32
_OriWORPIfSatConfigTableIndex_Object=MibTableColumn
oriWORPIfSatConfigTableIndex=_OriWORPIfSatConfigTableIndex_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,1),_OriWORPIfSatConfigTableIndex_Type())
oriWORPIfSatConfigTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableIndex.setStatus(_A)
class _OriWORPIfSatConfigTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriWORPIfSatConfigTableEntryStatus_Type.__name__=_D
_OriWORPIfSatConfigTableEntryStatus_Object=MibTableColumn
oriWORPIfSatConfigTableEntryStatus=_OriWORPIfSatConfigTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,2),_OriWORPIfSatConfigTableEntryStatus_Type())
oriWORPIfSatConfigTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableEntryStatus.setStatus(_A)
_OriWORPIfSatConfigTableMacAddress_Type=MacAddress
_OriWORPIfSatConfigTableMacAddress_Object=MibTableColumn
oriWORPIfSatConfigTableMacAddress=_OriWORPIfSatConfigTableMacAddress_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,3),_OriWORPIfSatConfigTableMacAddress_Type())
oriWORPIfSatConfigTableMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableMacAddress.setStatus(_A)
_OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Type=Gauge32
_OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Object=MibTableColumn
oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink=_OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,4),_OriWORPIfSatConfigTableMinimumBandwidthLimitDownlink_Type())
oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink.setStatus(_A)
_OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Type=Gauge32
_OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Object=MibTableColumn
oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink=_OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,5),_OriWORPIfSatConfigTableMaximumBandwidthLimitDownlink_Type())
oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink.setStatus(_A)
_OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Type=Gauge32
_OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Object=MibTableColumn
oriWORPIfSatConfigTableMinimumBandwidthLimitUplink=_OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,6),_OriWORPIfSatConfigTableMinimumBandwidthLimitUplink_Type())
oriWORPIfSatConfigTableMinimumBandwidthLimitUplink.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableMinimumBandwidthLimitUplink.setStatus(_A)
_OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Type=Gauge32
_OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Object=MibTableColumn
oriWORPIfSatConfigTableMaximumBandwidthLimitUplink=_OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,7),_OriWORPIfSatConfigTableMaximumBandwidthLimitUplink_Type())
oriWORPIfSatConfigTableMaximumBandwidthLimitUplink.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableMaximumBandwidthLimitUplink.setStatus(_A)
_OriWORPIfSatConfigTableComment_Type=DisplayString
_OriWORPIfSatConfigTableComment_Object=MibTableColumn
oriWORPIfSatConfigTableComment=_OriWORPIfSatConfigTableComment_Object((1,3,6,1,4,1,11898,2,1,2,5,3,1,2,1,8),_OriWORPIfSatConfigTableComment_Type())
oriWORPIfSatConfigTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSatConfigTableComment.setStatus(_A)
_OrinocoWORPIfSatStat_ObjectIdentity=ObjectIdentity
orinocoWORPIfSatStat=_OrinocoWORPIfSatStat_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,3,2))
_OriWORPIfSatStatTable_Object=MibTable
oriWORPIfSatStatTable=_OriWORPIfSatStatTable_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1))
if mibBuilder.loadTexts:oriWORPIfSatStatTable.setStatus(_A)
_OriWORPIfSatStatTableEntry_Object=MibTableRow
oriWORPIfSatStatTableEntry=_OriWORPIfSatStatTableEntry_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1))
oriWORPIfSatStatTableEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:oriWORPIfSatStatTableEntry.setStatus(_A)
_OriWORPIfSatStatTableIndex_Type=Integer32
_OriWORPIfSatStatTableIndex_Object=MibTableColumn
oriWORPIfSatStatTableIndex=_OriWORPIfSatStatTableIndex_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,1),_OriWORPIfSatStatTableIndex_Type())
oriWORPIfSatStatTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableIndex.setStatus(_A)
_OriWORPIfSatStatTableMacAddress_Type=MacAddress
_OriWORPIfSatStatTableMacAddress_Object=MibTableColumn
oriWORPIfSatStatTableMacAddress=_OriWORPIfSatStatTableMacAddress_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,2),_OriWORPIfSatStatTableMacAddress_Type())
oriWORPIfSatStatTableMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableMacAddress.setStatus(_A)
class _OriWORPIfSatStatTableAverageLocalSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfSatStatTableAverageLocalSignal_Type.__name__=_D
_OriWORPIfSatStatTableAverageLocalSignal_Object=MibTableColumn
oriWORPIfSatStatTableAverageLocalSignal=_OriWORPIfSatStatTableAverageLocalSignal_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,3),_OriWORPIfSatStatTableAverageLocalSignal_Type())
oriWORPIfSatStatTableAverageLocalSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableAverageLocalSignal.setStatus(_A)
class _OriWORPIfSatStatTableAverageLocalNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfSatStatTableAverageLocalNoise_Type.__name__=_D
_OriWORPIfSatStatTableAverageLocalNoise_Object=MibTableColumn
oriWORPIfSatStatTableAverageLocalNoise=_OriWORPIfSatStatTableAverageLocalNoise_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,4),_OriWORPIfSatStatTableAverageLocalNoise_Type())
oriWORPIfSatStatTableAverageLocalNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableAverageLocalNoise.setStatus(_A)
class _OriWORPIfSatStatTableAverageRemoteSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfSatStatTableAverageRemoteSignal_Type.__name__=_D
_OriWORPIfSatStatTableAverageRemoteSignal_Object=MibTableColumn
oriWORPIfSatStatTableAverageRemoteSignal=_OriWORPIfSatStatTableAverageRemoteSignal_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,5),_OriWORPIfSatStatTableAverageRemoteSignal_Type())
oriWORPIfSatStatTableAverageRemoteSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableAverageRemoteSignal.setStatus(_A)
class _OriWORPIfSatStatTableAverageRemoteNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriWORPIfSatStatTableAverageRemoteNoise_Type.__name__=_D
_OriWORPIfSatStatTableAverageRemoteNoise_Object=MibTableColumn
oriWORPIfSatStatTableAverageRemoteNoise=_OriWORPIfSatStatTableAverageRemoteNoise_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,6),_OriWORPIfSatStatTableAverageRemoteNoise_Type())
oriWORPIfSatStatTableAverageRemoteNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableAverageRemoteNoise.setStatus(_A)
_OriWORPIfSatStatTablePollData_Type=Counter32
_OriWORPIfSatStatTablePollData_Object=MibTableColumn
oriWORPIfSatStatTablePollData=_OriWORPIfSatStatTablePollData_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,7),_OriWORPIfSatStatTablePollData_Type())
oriWORPIfSatStatTablePollData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTablePollData.setStatus(_A)
_OriWORPIfSatStatTablePollNoData_Type=Counter32
_OriWORPIfSatStatTablePollNoData_Object=MibTableColumn
oriWORPIfSatStatTablePollNoData=_OriWORPIfSatStatTablePollNoData_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,8),_OriWORPIfSatStatTablePollNoData_Type())
oriWORPIfSatStatTablePollNoData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTablePollNoData.setStatus(_A)
_OriWORPIfSatStatTableReplyData_Type=Counter32
_OriWORPIfSatStatTableReplyData_Object=MibTableColumn
oriWORPIfSatStatTableReplyData=_OriWORPIfSatStatTableReplyData_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,9),_OriWORPIfSatStatTableReplyData_Type())
oriWORPIfSatStatTableReplyData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableReplyData.setStatus(_A)
_OriWORPIfSatStatTableReplyNoData_Type=Counter32
_OriWORPIfSatStatTableReplyNoData_Object=MibTableColumn
oriWORPIfSatStatTableReplyNoData=_OriWORPIfSatStatTableReplyNoData_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,10),_OriWORPIfSatStatTableReplyNoData_Type())
oriWORPIfSatStatTableReplyNoData.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableReplyNoData.setStatus(_A)
_OriWORPIfSatStatTableRequestForService_Type=Counter32
_OriWORPIfSatStatTableRequestForService_Object=MibTableColumn
oriWORPIfSatStatTableRequestForService=_OriWORPIfSatStatTableRequestForService_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,11),_OriWORPIfSatStatTableRequestForService_Type())
oriWORPIfSatStatTableRequestForService.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableRequestForService.setStatus(_A)
_OriWORPIfSatStatTableSendSuccess_Type=Counter32
_OriWORPIfSatStatTableSendSuccess_Object=MibTableColumn
oriWORPIfSatStatTableSendSuccess=_OriWORPIfSatStatTableSendSuccess_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,12),_OriWORPIfSatStatTableSendSuccess_Type())
oriWORPIfSatStatTableSendSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableSendSuccess.setStatus(_A)
_OriWORPIfSatStatTableSendRetries_Type=Counter32
_OriWORPIfSatStatTableSendRetries_Object=MibTableColumn
oriWORPIfSatStatTableSendRetries=_OriWORPIfSatStatTableSendRetries_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,13),_OriWORPIfSatStatTableSendRetries_Type())
oriWORPIfSatStatTableSendRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableSendRetries.setStatus(_A)
_OriWORPIfSatStatTableSendFailures_Type=Counter32
_OriWORPIfSatStatTableSendFailures_Object=MibTableColumn
oriWORPIfSatStatTableSendFailures=_OriWORPIfSatStatTableSendFailures_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,14),_OriWORPIfSatStatTableSendFailures_Type())
oriWORPIfSatStatTableSendFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableSendFailures.setStatus(_A)
_OriWORPIfSatStatTableReceiveSuccess_Type=Counter32
_OriWORPIfSatStatTableReceiveSuccess_Object=MibTableColumn
oriWORPIfSatStatTableReceiveSuccess=_OriWORPIfSatStatTableReceiveSuccess_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,15),_OriWORPIfSatStatTableReceiveSuccess_Type())
oriWORPIfSatStatTableReceiveSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableReceiveSuccess.setStatus(_A)
_OriWORPIfSatStatTableReceiveRetries_Type=Counter32
_OriWORPIfSatStatTableReceiveRetries_Object=MibTableColumn
oriWORPIfSatStatTableReceiveRetries=_OriWORPIfSatStatTableReceiveRetries_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,16),_OriWORPIfSatStatTableReceiveRetries_Type())
oriWORPIfSatStatTableReceiveRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableReceiveRetries.setStatus(_A)
_OriWORPIfSatStatTableReceiveFailures_Type=Counter32
_OriWORPIfSatStatTableReceiveFailures_Object=MibTableColumn
oriWORPIfSatStatTableReceiveFailures=_OriWORPIfSatStatTableReceiveFailures_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,17),_OriWORPIfSatStatTableReceiveFailures_Type())
oriWORPIfSatStatTableReceiveFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableReceiveFailures.setStatus(_A)
_OriWORPIfSatStatTablePollNoReplies_Type=Counter32
_OriWORPIfSatStatTablePollNoReplies_Object=MibTableColumn
oriWORPIfSatStatTablePollNoReplies=_OriWORPIfSatStatTablePollNoReplies_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,18),_OriWORPIfSatStatTablePollNoReplies_Type())
oriWORPIfSatStatTablePollNoReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTablePollNoReplies.setStatus(_A)
_OriWORPIfSatStatTableLocalTxRate_Type=Integer32
_OriWORPIfSatStatTableLocalTxRate_Object=MibTableColumn
oriWORPIfSatStatTableLocalTxRate=_OriWORPIfSatStatTableLocalTxRate_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,19),_OriWORPIfSatStatTableLocalTxRate_Type())
oriWORPIfSatStatTableLocalTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableLocalTxRate.setStatus(_A)
_OriWORPIfSatStatTableRemoteTxRate_Type=Integer32
_OriWORPIfSatStatTableRemoteTxRate_Object=MibTableColumn
oriWORPIfSatStatTableRemoteTxRate=_OriWORPIfSatStatTableRemoteTxRate_Object((1,3,6,1,4,1,11898,2,1,2,5,3,2,1,1,20),_OriWORPIfSatStatTableRemoteTxRate_Type())
oriWORPIfSatStatTableRemoteTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSatStatTableRemoteTxRate.setStatus(_A)
_OrinocoWORPIfSiteSurvey_ObjectIdentity=ObjectIdentity
orinocoWORPIfSiteSurvey=_OrinocoWORPIfSiteSurvey_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,4))
class _OriWORPIfSiteSurveyOperation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),(_W,2),('test',3)))
_OriWORPIfSiteSurveyOperation_Type.__name__=_D
_OriWORPIfSiteSurveyOperation_Object=MibScalar
oriWORPIfSiteSurveyOperation=_OriWORPIfSiteSurveyOperation_Object((1,3,6,1,4,1,11898,2,1,2,5,4,1),_OriWORPIfSiteSurveyOperation_Type())
oriWORPIfSiteSurveyOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyOperation.setStatus(_A)
_OriWORPIfSiteSurveyTable_Object=MibTable
oriWORPIfSiteSurveyTable=_OriWORPIfSiteSurveyTable_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2))
if mibBuilder.loadTexts:oriWORPIfSiteSurveyTable.setStatus(_A)
_OriWORPIfSiteSurveySignalQualityTableEntry_Object=MibTableRow
oriWORPIfSiteSurveySignalQualityTableEntry=_OriWORPIfSiteSurveySignalQualityTableEntry_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1))
oriWORPIfSiteSurveySignalQualityTableEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:oriWORPIfSiteSurveySignalQualityTableEntry.setStatus(_A)
_OriWORPIfSiteSurveyTableIndex_Type=Integer32
_OriWORPIfSiteSurveyTableIndex_Object=MibTableColumn
oriWORPIfSiteSurveyTableIndex=_OriWORPIfSiteSurveyTableIndex_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,1),_OriWORPIfSiteSurveyTableIndex_Type())
oriWORPIfSiteSurveyTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyTableIndex.setStatus(_A)
_OriWORPIfSiteSurveyBaseMACAddress_Type=PhysAddress
_OriWORPIfSiteSurveyBaseMACAddress_Object=MibTableColumn
oriWORPIfSiteSurveyBaseMACAddress=_OriWORPIfSiteSurveyBaseMACAddress_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,2),_OriWORPIfSiteSurveyBaseMACAddress_Type())
oriWORPIfSiteSurveyBaseMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyBaseMACAddress.setStatus(_A)
_OriWORPIfSiteSurveyBaseName_Type=DisplayString
_OriWORPIfSiteSurveyBaseName_Object=MibTableColumn
oriWORPIfSiteSurveyBaseName=_OriWORPIfSiteSurveyBaseName_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,3),_OriWORPIfSiteSurveyBaseName_Type())
oriWORPIfSiteSurveyBaseName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyBaseName.setStatus(_A)
_OriWORPIfSiteSurveyMaxSatAllowed_Type=Integer32
_OriWORPIfSiteSurveyMaxSatAllowed_Object=MibTableColumn
oriWORPIfSiteSurveyMaxSatAllowed=_OriWORPIfSiteSurveyMaxSatAllowed_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,4),_OriWORPIfSiteSurveyMaxSatAllowed_Type())
oriWORPIfSiteSurveyMaxSatAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyMaxSatAllowed.setStatus(_A)
_OriWORPIfSiteSurveyNumSatRegistered_Type=Integer32
_OriWORPIfSiteSurveyNumSatRegistered_Object=MibTableColumn
oriWORPIfSiteSurveyNumSatRegistered=_OriWORPIfSiteSurveyNumSatRegistered_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,5),_OriWORPIfSiteSurveyNumSatRegistered_Type())
oriWORPIfSiteSurveyNumSatRegistered.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyNumSatRegistered.setStatus(_A)
_OriWORPIfSiteSurveyCurrentSatRegistered_Type=Integer32
_OriWORPIfSiteSurveyCurrentSatRegistered_Object=MibTableColumn
oriWORPIfSiteSurveyCurrentSatRegistered=_OriWORPIfSiteSurveyCurrentSatRegistered_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,6),_OriWORPIfSiteSurveyCurrentSatRegistered_Type())
oriWORPIfSiteSurveyCurrentSatRegistered.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyCurrentSatRegistered.setStatus(_A)
_OriWORPIfSiteSurveyLocalSignalLevel_Type=Integer32
_OriWORPIfSiteSurveyLocalSignalLevel_Object=MibTableColumn
oriWORPIfSiteSurveyLocalSignalLevel=_OriWORPIfSiteSurveyLocalSignalLevel_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,7),_OriWORPIfSiteSurveyLocalSignalLevel_Type())
oriWORPIfSiteSurveyLocalSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyLocalSignalLevel.setStatus(_A)
_OriWORPIfSiteSurveyLocalNoiseLevel_Type=Integer32
_OriWORPIfSiteSurveyLocalNoiseLevel_Object=MibTableColumn
oriWORPIfSiteSurveyLocalNoiseLevel=_OriWORPIfSiteSurveyLocalNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,8),_OriWORPIfSiteSurveyLocalNoiseLevel_Type())
oriWORPIfSiteSurveyLocalNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyLocalNoiseLevel.setStatus(_A)
_OriWORPIfSiteSurveyLocalSNR_Type=Integer32
_OriWORPIfSiteSurveyLocalSNR_Object=MibTableColumn
oriWORPIfSiteSurveyLocalSNR=_OriWORPIfSiteSurveyLocalSNR_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,9),_OriWORPIfSiteSurveyLocalSNR_Type())
oriWORPIfSiteSurveyLocalSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyLocalSNR.setStatus(_A)
_OriWORPIfSiteSurveyRemoteSignalLevel_Type=Integer32
_OriWORPIfSiteSurveyRemoteSignalLevel_Object=MibTableColumn
oriWORPIfSiteSurveyRemoteSignalLevel=_OriWORPIfSiteSurveyRemoteSignalLevel_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,10),_OriWORPIfSiteSurveyRemoteSignalLevel_Type())
oriWORPIfSiteSurveyRemoteSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyRemoteSignalLevel.setStatus(_A)
_OriWORPIfSiteSurveyRemoteNoiseLevel_Type=Integer32
_OriWORPIfSiteSurveyRemoteNoiseLevel_Object=MibTableColumn
oriWORPIfSiteSurveyRemoteNoiseLevel=_OriWORPIfSiteSurveyRemoteNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,11),_OriWORPIfSiteSurveyRemoteNoiseLevel_Type())
oriWORPIfSiteSurveyRemoteNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyRemoteNoiseLevel.setStatus(_A)
_OriWORPIfSiteSurveyRemoteSNR_Type=Integer32
_OriWORPIfSiteSurveyRemoteSNR_Object=MibTableColumn
oriWORPIfSiteSurveyRemoteSNR=_OriWORPIfSiteSurveyRemoteSNR_Object((1,3,6,1,4,1,11898,2,1,2,5,4,2,1,12),_OriWORPIfSiteSurveyRemoteSNR_Type())
oriWORPIfSiteSurveyRemoteSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWORPIfSiteSurveyRemoteSNR.setStatus(_A)
_OrinocoWORPIfRoaming_ObjectIdentity=ObjectIdentity
orinocoWORPIfRoaming=_OrinocoWORPIfRoaming_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,5))
_OriWORPIfRoamingStatus_Type=ObjStatus
_OriWORPIfRoamingStatus_Object=MibScalar
oriWORPIfRoamingStatus=_OriWORPIfRoamingStatus_Object((1,3,6,1,4,1,11898,2,1,2,5,5,1),_OriWORPIfRoamingStatus_Type())
oriWORPIfRoamingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfRoamingStatus.setStatus(_A)
class _OriWORPIfRoamingSlowScanThreshold_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_OriWORPIfRoamingSlowScanThreshold_Type.__name__=_D
_OriWORPIfRoamingSlowScanThreshold_Object=MibScalar
oriWORPIfRoamingSlowScanThreshold=_OriWORPIfRoamingSlowScanThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,5,2),_OriWORPIfRoamingSlowScanThreshold_Type())
oriWORPIfRoamingSlowScanThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfRoamingSlowScanThreshold.setStatus(_A)
class _OriWORPIfRoamingFastScanThreshold_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_OriWORPIfRoamingFastScanThreshold_Type.__name__=_D
_OriWORPIfRoamingFastScanThreshold_Object=MibScalar
oriWORPIfRoamingFastScanThreshold=_OriWORPIfRoamingFastScanThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,5,3),_OriWORPIfRoamingFastScanThreshold_Type())
oriWORPIfRoamingFastScanThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfRoamingFastScanThreshold.setStatus(_A)
class _OriWORPIfRoamingThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_OriWORPIfRoamingThreshold_Type.__name__=_D
_OriWORPIfRoamingThreshold_Object=MibScalar
oriWORPIfRoamingThreshold=_OriWORPIfRoamingThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,5,4),_OriWORPIfRoamingThreshold_Type())
oriWORPIfRoamingThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfRoamingThreshold.setStatus(_A)
class _OriWORPIfRoamingSlowScanPercentThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OriWORPIfRoamingSlowScanPercentThreshold_Type.__name__=_D
_OriWORPIfRoamingSlowScanPercentThreshold_Object=MibScalar
oriWORPIfRoamingSlowScanPercentThreshold=_OriWORPIfRoamingSlowScanPercentThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,5,5),_OriWORPIfRoamingSlowScanPercentThreshold_Type())
oriWORPIfRoamingSlowScanPercentThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfRoamingSlowScanPercentThreshold.setStatus(_A)
class _OriWORPIfRoamingFastScanPercentThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OriWORPIfRoamingFastScanPercentThreshold_Type.__name__=_D
_OriWORPIfRoamingFastScanPercentThreshold_Object=MibScalar
oriWORPIfRoamingFastScanPercentThreshold=_OriWORPIfRoamingFastScanPercentThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,5,6),_OriWORPIfRoamingFastScanPercentThreshold_Type())
oriWORPIfRoamingFastScanPercentThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfRoamingFastScanPercentThreshold.setStatus(_A)
_OrinocoWORPIfDDRS_ObjectIdentity=ObjectIdentity
orinocoWORPIfDDRS=_OrinocoWORPIfDDRS_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,6))
class _OriWORPIfDDRSStatus_Type(ObjStatus):defaultValue=2
_OriWORPIfDDRSStatus_Type.__name__=_J
_OriWORPIfDDRSStatus_Object=MibScalar
oriWORPIfDDRSStatus=_OriWORPIfDDRSStatus_Object((1,3,6,1,4,1,11898,2,1,2,5,6,1),_OriWORPIfDDRSStatus_Type())
oriWORPIfDDRSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSStatus.setStatus(_A)
class _OriWORPIfDDRSDefDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,108))
_OriWORPIfDDRSDefDataRate_Type.__name__=_D
_OriWORPIfDDRSDefDataRate_Object=MibScalar
oriWORPIfDDRSDefDataRate=_OriWORPIfDDRSDefDataRate_Object((1,3,6,1,4,1,11898,2,1,2,5,6,2),_OriWORPIfDDRSDefDataRate_Type())
oriWORPIfDDRSDefDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSDefDataRate.setStatus(_A)
class _OriWORPIfDDRSMaxDataRate_Type(Integer32):defaultValue=36;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,108))
_OriWORPIfDDRSMaxDataRate_Type.__name__=_D
_OriWORPIfDDRSMaxDataRate_Object=MibScalar
oriWORPIfDDRSMaxDataRate=_OriWORPIfDDRSMaxDataRate_Object((1,3,6,1,4,1,11898,2,1,2,5,6,3),_OriWORPIfDDRSMaxDataRate_Type())
oriWORPIfDDRSMaxDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMaxDataRate.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an6Mbps_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an6Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an6Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an6Mbps=_OriWORPIfDDRSMinReqSNRdot11an6Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,4),_OriWORPIfDDRSMinReqSNRdot11an6Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an6Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an9Mbps_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an9Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an9Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an9Mbps=_OriWORPIfDDRSMinReqSNRdot11an9Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,5),_OriWORPIfDDRSMinReqSNRdot11an9Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an9Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an9Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an12Mbps_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an12Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an12Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an12Mbps=_OriWORPIfDDRSMinReqSNRdot11an12Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,6),_OriWORPIfDDRSMinReqSNRdot11an12Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an12Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an18Mbps_Type(Integer32):defaultValue=11;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an18Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an18Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an18Mbps=_OriWORPIfDDRSMinReqSNRdot11an18Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,7),_OriWORPIfDDRSMinReqSNRdot11an18Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an18Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an24Mbps_Type(Integer32):defaultValue=14;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an24Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an24Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an24Mbps=_OriWORPIfDDRSMinReqSNRdot11an24Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,8),_OriWORPIfDDRSMinReqSNRdot11an24Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an24Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an36Mbps_Type(Integer32):defaultValue=18;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an36Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an36Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an36Mbps=_OriWORPIfDDRSMinReqSNRdot11an36Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,9),_OriWORPIfDDRSMinReqSNRdot11an36Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an36Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an48Mbps_Type(Integer32):defaultValue=22;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an48Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an48Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an48Mbps=_OriWORPIfDDRSMinReqSNRdot11an48Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,10),_OriWORPIfDDRSMinReqSNRdot11an48Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an48Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11an54Mbps_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11an54Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11an54Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11an54Mbps=_OriWORPIfDDRSMinReqSNRdot11an54Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,11),_OriWORPIfDDRSMinReqSNRdot11an54Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11an54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11an54Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at12Mbps_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at12Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at12Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at12Mbps=_OriWORPIfDDRSMinReqSNRdot11at12Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,12),_OriWORPIfDDRSMinReqSNRdot11at12Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at12Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at18Mbps_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at18Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at18Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at18Mbps=_OriWORPIfDDRSMinReqSNRdot11at18Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,13),_OriWORPIfDDRSMinReqSNRdot11at18Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at18Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at24Mbps_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at24Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at24Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at24Mbps=_OriWORPIfDDRSMinReqSNRdot11at24Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,14),_OriWORPIfDDRSMinReqSNRdot11at24Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at24Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at36Mbps_Type(Integer32):defaultValue=11;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at36Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at36Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at36Mbps=_OriWORPIfDDRSMinReqSNRdot11at36Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,15),_OriWORPIfDDRSMinReqSNRdot11at36Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at36Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at48Mbps_Type(Integer32):defaultValue=14;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at48Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at48Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at48Mbps=_OriWORPIfDDRSMinReqSNRdot11at48Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,16),_OriWORPIfDDRSMinReqSNRdot11at48Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at48Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at72Mbps_Type(Integer32):defaultValue=18;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at72Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at72Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at72Mbps=_OriWORPIfDDRSMinReqSNRdot11at72Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,17),_OriWORPIfDDRSMinReqSNRdot11at72Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at72Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at72Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at96Mbps_Type(Integer32):defaultValue=22;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at96Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at96Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at96Mbps=_OriWORPIfDDRSMinReqSNRdot11at96Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,18),_OriWORPIfDDRSMinReqSNRdot11at96Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at96Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at96Mbps.setStatus(_A)
class _OriWORPIfDDRSMinReqSNRdot11at108Mbps_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSMinReqSNRdot11at108Mbps_Type.__name__=_D
_OriWORPIfDDRSMinReqSNRdot11at108Mbps_Object=MibScalar
oriWORPIfDDRSMinReqSNRdot11at108Mbps=_OriWORPIfDDRSMinReqSNRdot11at108Mbps_Object((1,3,6,1,4,1,11898,2,1,2,5,6,19),_OriWORPIfDDRSMinReqSNRdot11at108Mbps_Type())
oriWORPIfDDRSMinReqSNRdot11at108Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSMinReqSNRdot11at108Mbps.setStatus(_A)
class _OriWORPIfDDRSDataRateIncAvgSNRThreshold_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSDataRateIncAvgSNRThreshold_Type.__name__=_D
_OriWORPIfDDRSDataRateIncAvgSNRThreshold_Object=MibScalar
oriWORPIfDDRSDataRateIncAvgSNRThreshold=_OriWORPIfDDRSDataRateIncAvgSNRThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,6,20),_OriWORPIfDDRSDataRateIncAvgSNRThreshold_Type())
oriWORPIfDDRSDataRateIncAvgSNRThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSDataRateIncAvgSNRThreshold.setStatus(_A)
class _OriWORPIfDDRSDataRateIncReqSNRThreshold_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSDataRateIncReqSNRThreshold_Type.__name__=_D
_OriWORPIfDDRSDataRateIncReqSNRThreshold_Object=MibScalar
oriWORPIfDDRSDataRateIncReqSNRThreshold=_OriWORPIfDDRSDataRateIncReqSNRThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,6,21),_OriWORPIfDDRSDataRateIncReqSNRThreshold_Type())
oriWORPIfDDRSDataRateIncReqSNRThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSDataRateIncReqSNRThreshold.setStatus(_A)
class _OriWORPIfDDRSDataRateDecReqSNRThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_OriWORPIfDDRSDataRateDecReqSNRThreshold_Type.__name__=_D
_OriWORPIfDDRSDataRateDecReqSNRThreshold_Object=MibScalar
oriWORPIfDDRSDataRateDecReqSNRThreshold=_OriWORPIfDDRSDataRateDecReqSNRThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,6,22),_OriWORPIfDDRSDataRateDecReqSNRThreshold_Type())
oriWORPIfDDRSDataRateDecReqSNRThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSDataRateDecReqSNRThreshold.setStatus(_A)
class _OriWORPIfDDRSDataRateIncPercentThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OriWORPIfDDRSDataRateIncPercentThreshold_Type.__name__=_D
_OriWORPIfDDRSDataRateIncPercentThreshold_Object=MibScalar
oriWORPIfDDRSDataRateIncPercentThreshold=_OriWORPIfDDRSDataRateIncPercentThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,6,23),_OriWORPIfDDRSDataRateIncPercentThreshold_Type())
oriWORPIfDDRSDataRateIncPercentThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSDataRateIncPercentThreshold.setStatus(_A)
class _OriWORPIfDDRSDataRateDecPercentThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OriWORPIfDDRSDataRateDecPercentThreshold_Type.__name__=_D
_OriWORPIfDDRSDataRateDecPercentThreshold_Object=MibScalar
oriWORPIfDDRSDataRateDecPercentThreshold=_OriWORPIfDDRSDataRateDecPercentThreshold_Object((1,3,6,1,4,1,11898,2,1,2,5,6,24),_OriWORPIfDDRSDataRateDecPercentThreshold_Type())
oriWORPIfDDRSDataRateDecPercentThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPIfDDRSDataRateDecPercentThreshold.setStatus(_A)
_OrinocoWORPIfBSU_ObjectIdentity=ObjectIdentity
orinocoWORPIfBSU=_OrinocoWORPIfBSU_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,7))
_OrinocoWORPIfBSUStat_ObjectIdentity=ObjectIdentity
orinocoWORPIfBSUStat=_OrinocoWORPIfBSUStat_ObjectIdentity((1,3,6,1,4,1,11898,2,1,2,5,7,1))
_OrinocoWORPIfBSUStatMACAddress_Type=MacAddress
_OrinocoWORPIfBSUStatMACAddress_Object=MibScalar
orinocoWORPIfBSUStatMACAddress=_OrinocoWORPIfBSUStatMACAddress_Object((1,3,6,1,4,1,11898,2,1,2,5,7,1,1),_OrinocoWORPIfBSUStatMACAddress_Type())
orinocoWORPIfBSUStatMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:orinocoWORPIfBSUStatMACAddress.setStatus(_A)
_OrinocoWORPIfBSUStatLocalTxRate_Type=Integer32
_OrinocoWORPIfBSUStatLocalTxRate_Object=MibScalar
orinocoWORPIfBSUStatLocalTxRate=_OrinocoWORPIfBSUStatLocalTxRate_Object((1,3,6,1,4,1,11898,2,1,2,5,7,1,2),_OrinocoWORPIfBSUStatLocalTxRate_Type())
orinocoWORPIfBSUStatLocalTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:orinocoWORPIfBSUStatLocalTxRate.setStatus(_A)
_OrinocoWORPIfBSUStatRemoteTxRate_Type=Integer32
_OrinocoWORPIfBSUStatRemoteTxRate_Object=MibScalar
orinocoWORPIfBSUStatRemoteTxRate=_OrinocoWORPIfBSUStatRemoteTxRate_Object((1,3,6,1,4,1,11898,2,1,2,5,7,1,3),_OrinocoWORPIfBSUStatRemoteTxRate_Type())
orinocoWORPIfBSUStatRemoteTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:orinocoWORPIfBSUStatRemoteTxRate.setStatus(_A)
class _OrinocoWORPIfBSUStatAverageLocalSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OrinocoWORPIfBSUStatAverageLocalSignal_Type.__name__=_D
_OrinocoWORPIfBSUStatAverageLocalSignal_Object=MibScalar
orinocoWORPIfBSUStatAverageLocalSignal=_OrinocoWORPIfBSUStatAverageLocalSignal_Object((1,3,6,1,4,1,11898,2,1,2,5,7,1,4),_OrinocoWORPIfBSUStatAverageLocalSignal_Type())
orinocoWORPIfBSUStatAverageLocalSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:orinocoWORPIfBSUStatAverageLocalSignal.setStatus(_A)
class _OrinocoWORPIfBSUStatAverageLocalNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OrinocoWORPIfBSUStatAverageLocalNoise_Type.__name__=_D
_OrinocoWORPIfBSUStatAverageLocalNoise_Object=MibScalar
orinocoWORPIfBSUStatAverageLocalNoise=_OrinocoWORPIfBSUStatAverageLocalNoise_Object((1,3,6,1,4,1,11898,2,1,2,5,7,1,5),_OrinocoWORPIfBSUStatAverageLocalNoise_Type())
orinocoWORPIfBSUStatAverageLocalNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:orinocoWORPIfBSUStatAverageLocalNoise.setStatus(_A)
class _OrinocoWORPIfBSUStatAverageRemoteSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OrinocoWORPIfBSUStatAverageRemoteSignal_Type.__name__=_D
_OrinocoWORPIfBSUStatAverageRemoteSignal_Object=MibScalar
orinocoWORPIfBSUStatAverageRemoteSignal=_OrinocoWORPIfBSUStatAverageRemoteSignal_Object((1,3,6,1,4,1,11898,2,1,2,5,7,1,6),_OrinocoWORPIfBSUStatAverageRemoteSignal_Type())
orinocoWORPIfBSUStatAverageRemoteSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:orinocoWORPIfBSUStatAverageRemoteSignal.setStatus(_A)
class _OrinocoWORPIfBSUStatAverageRemoteNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OrinocoWORPIfBSUStatAverageRemoteNoise_Type.__name__=_D
_OrinocoWORPIfBSUStatAverageRemoteNoise_Object=MibScalar
orinocoWORPIfBSUStatAverageRemoteNoise=_OrinocoWORPIfBSUStatAverageRemoteNoise_Object((1,3,6,1,4,1,11898,2,1,2,5,7,1,7),_OrinocoWORPIfBSUStatAverageRemoteNoise_Type())
orinocoWORPIfBSUStatAverageRemoteNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:orinocoWORPIfBSUStatAverageRemoteNoise.setStatus(_A)
_OrinocoNet_ObjectIdentity=ObjectIdentity
orinocoNet=_OrinocoNet_ObjectIdentity((1,3,6,1,4,1,11898,2,1,3))
_OrinocoNetIP_ObjectIdentity=ObjectIdentity
orinocoNetIP=_OrinocoNetIP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,3,1))
_OriNetworkIPConfigTable_Object=MibTable
oriNetworkIPConfigTable=_OriNetworkIPConfigTable_Object((1,3,6,1,4,1,11898,2,1,3,1,1))
if mibBuilder.loadTexts:oriNetworkIPConfigTable.setStatus(_A)
_OriNetworkIPConfigTableEntry_Object=MibTableRow
oriNetworkIPConfigTableEntry=_OriNetworkIPConfigTableEntry_Object((1,3,6,1,4,1,11898,2,1,3,1,1,1))
oriNetworkIPConfigTableEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:oriNetworkIPConfigTableEntry.setStatus(_A)
_OriNetworkIPConfigTableIndex_Type=Integer32
_OriNetworkIPConfigTableIndex_Object=MibTableColumn
oriNetworkIPConfigTableIndex=_OriNetworkIPConfigTableIndex_Object((1,3,6,1,4,1,11898,2,1,3,1,1,1,1),_OriNetworkIPConfigTableIndex_Type())
oriNetworkIPConfigTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriNetworkIPConfigTableIndex.setStatus(_A)
_OriNetworkIPConfigIPAddress_Type=IpAddress
_OriNetworkIPConfigIPAddress_Object=MibTableColumn
oriNetworkIPConfigIPAddress=_OriNetworkIPConfigIPAddress_Object((1,3,6,1,4,1,11898,2,1,3,1,1,1,2),_OriNetworkIPConfigIPAddress_Type())
oriNetworkIPConfigIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNetworkIPConfigIPAddress.setStatus(_A)
_OriNetworkIPConfigSubnetMask_Type=IpAddress
_OriNetworkIPConfigSubnetMask_Object=MibTableColumn
oriNetworkIPConfigSubnetMask=_OriNetworkIPConfigSubnetMask_Object((1,3,6,1,4,1,11898,2,1,3,1,1,1,3),_OriNetworkIPConfigSubnetMask_Type())
oriNetworkIPConfigSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNetworkIPConfigSubnetMask.setStatus(_A)
_OriNetworkIPDefaultRouterIPAddress_Type=IpAddress
_OriNetworkIPDefaultRouterIPAddress_Object=MibScalar
oriNetworkIPDefaultRouterIPAddress=_OriNetworkIPDefaultRouterIPAddress_Object((1,3,6,1,4,1,11898,2,1,3,1,3),_OriNetworkIPDefaultRouterIPAddress_Type())
oriNetworkIPDefaultRouterIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNetworkIPDefaultRouterIPAddress.setStatus(_A)
class _OriNetworkIPDefaultTTL_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OriNetworkIPDefaultTTL_Type.__name__=_D
_OriNetworkIPDefaultTTL_Object=MibScalar
oriNetworkIPDefaultTTL=_OriNetworkIPDefaultTTL_Object((1,3,6,1,4,1,11898,2,1,3,1,4),_OriNetworkIPDefaultTTL_Type())
oriNetworkIPDefaultTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNetworkIPDefaultTTL.setStatus(_A)
class _OriNetworkIPAddressType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_OriNetworkIPAddressType_Type.__name__=_D
_OriNetworkIPAddressType_Object=MibScalar
oriNetworkIPAddressType=_OriNetworkIPAddressType_Object((1,3,6,1,4,1,11898,2,1,3,1,5),_OriNetworkIPAddressType_Type())
oriNetworkIPAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNetworkIPAddressType.setStatus(_A)
_OrinocoSNMP_ObjectIdentity=ObjectIdentity
orinocoSNMP=_OrinocoSNMP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,4))
class _OriSNMPReadPassword_Type(DisplayString):defaultValue=OctetString(_U)
_OriSNMPReadPassword_Type.__name__=_O
_OriSNMPReadPassword_Object=MibScalar
oriSNMPReadPassword=_OriSNMPReadPassword_Object((1,3,6,1,4,1,11898,2,1,4,1),_OriSNMPReadPassword_Type())
oriSNMPReadPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPReadPassword.setStatus(_A)
class _OriSNMPReadWritePassword_Type(DisplayString):defaultValue=OctetString(_U)
_OriSNMPReadWritePassword_Type.__name__=_O
_OriSNMPReadWritePassword_Object=MibScalar
oriSNMPReadWritePassword=_OriSNMPReadWritePassword_Object((1,3,6,1,4,1,11898,2,1,4,2),_OriSNMPReadWritePassword_Type())
oriSNMPReadWritePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPReadWritePassword.setStatus(_A)
_OriSNMPAuthorizedManagerCount_Type=Counter32
_OriSNMPAuthorizedManagerCount_Object=MibScalar
oriSNMPAuthorizedManagerCount=_OriSNMPAuthorizedManagerCount_Object((1,3,6,1,4,1,11898,2,1,4,3),_OriSNMPAuthorizedManagerCount_Type())
oriSNMPAuthorizedManagerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSNMPAuthorizedManagerCount.setStatus(_A)
_OriSNMPAccessTable_Object=MibTable
oriSNMPAccessTable=_OriSNMPAccessTable_Object((1,3,6,1,4,1,11898,2,1,4,4))
if mibBuilder.loadTexts:oriSNMPAccessTable.setStatus(_A)
_OriSNMPAccessTableEntry_Object=MibTableRow
oriSNMPAccessTableEntry=_OriSNMPAccessTableEntry_Object((1,3,6,1,4,1,11898,2,1,4,4,1))
oriSNMPAccessTableEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:oriSNMPAccessTableEntry.setStatus(_A)
class _OriSNMPAccessTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_OriSNMPAccessTableIndex_Type.__name__=_D
_OriSNMPAccessTableIndex_Object=MibTableColumn
oriSNMPAccessTableIndex=_OriSNMPAccessTableIndex_Object((1,3,6,1,4,1,11898,2,1,4,4,1,1),_OriSNMPAccessTableIndex_Type())
oriSNMPAccessTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSNMPAccessTableIndex.setStatus(_A)
_OriSNMPAccessTableIPAddress_Type=IpAddress
_OriSNMPAccessTableIPAddress_Object=MibTableColumn
oriSNMPAccessTableIPAddress=_OriSNMPAccessTableIPAddress_Object((1,3,6,1,4,1,11898,2,1,4,4,1,2),_OriSNMPAccessTableIPAddress_Type())
oriSNMPAccessTableIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPAccessTableIPAddress.setStatus(_A)
_OriSNMPAccessTableIPMask_Type=IpAddress
_OriSNMPAccessTableIPMask_Object=MibTableColumn
oriSNMPAccessTableIPMask=_OriSNMPAccessTableIPMask_Object((1,3,6,1,4,1,11898,2,1,4,4,1,3),_OriSNMPAccessTableIPMask_Type())
oriSNMPAccessTableIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPAccessTableIPMask.setStatus(_A)
_OriSNMPAccessTableInterfaceBitmask_Type=InterfaceBitmask
_OriSNMPAccessTableInterfaceBitmask_Object=MibTableColumn
oriSNMPAccessTableInterfaceBitmask=_OriSNMPAccessTableInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,4,4,1,4),_OriSNMPAccessTableInterfaceBitmask_Type())
oriSNMPAccessTableInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPAccessTableInterfaceBitmask.setStatus(_A)
_OriSNMPAccessTableComment_Type=DisplayString
_OriSNMPAccessTableComment_Object=MibTableColumn
oriSNMPAccessTableComment=_OriSNMPAccessTableComment_Object((1,3,6,1,4,1,11898,2,1,4,4,1,5),_OriSNMPAccessTableComment_Type())
oriSNMPAccessTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPAccessTableComment.setStatus(_A)
class _OriSNMPAccessTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriSNMPAccessTableEntryStatus_Type.__name__=_D
_OriSNMPAccessTableEntryStatus_Object=MibTableColumn
oriSNMPAccessTableEntryStatus=_OriSNMPAccessTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,4,4,1,6),_OriSNMPAccessTableEntryStatus_Type())
oriSNMPAccessTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPAccessTableEntryStatus.setStatus(_A)
_OriSNMPTrapHostTable_Object=MibTable
oriSNMPTrapHostTable=_OriSNMPTrapHostTable_Object((1,3,6,1,4,1,11898,2,1,4,5))
if mibBuilder.loadTexts:oriSNMPTrapHostTable.setStatus(_A)
_OriSNMPTrapHostTableEntry_Object=MibTableRow
oriSNMPTrapHostTableEntry=_OriSNMPTrapHostTableEntry_Object((1,3,6,1,4,1,11898,2,1,4,5,1))
oriSNMPTrapHostTableEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:oriSNMPTrapHostTableEntry.setStatus(_A)
class _OriSNMPTrapHostTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_OriSNMPTrapHostTableIndex_Type.__name__=_D
_OriSNMPTrapHostTableIndex_Object=MibTableColumn
oriSNMPTrapHostTableIndex=_OriSNMPTrapHostTableIndex_Object((1,3,6,1,4,1,11898,2,1,4,5,1,1),_OriSNMPTrapHostTableIndex_Type())
oriSNMPTrapHostTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSNMPTrapHostTableIndex.setStatus(_A)
_OriSNMPTrapHostTableIPAddress_Type=IpAddress
_OriSNMPTrapHostTableIPAddress_Object=MibTableColumn
oriSNMPTrapHostTableIPAddress=_OriSNMPTrapHostTableIPAddress_Object((1,3,6,1,4,1,11898,2,1,4,5,1,2),_OriSNMPTrapHostTableIPAddress_Type())
oriSNMPTrapHostTableIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPTrapHostTableIPAddress.setStatus(_A)
_OriSNMPTrapHostTablePassword_Type=DisplayString
_OriSNMPTrapHostTablePassword_Object=MibTableColumn
oriSNMPTrapHostTablePassword=_OriSNMPTrapHostTablePassword_Object((1,3,6,1,4,1,11898,2,1,4,5,1,3),_OriSNMPTrapHostTablePassword_Type())
oriSNMPTrapHostTablePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPTrapHostTablePassword.setStatus(_A)
_OriSNMPTrapHostTableComment_Type=DisplayString
_OriSNMPTrapHostTableComment_Object=MibTableColumn
oriSNMPTrapHostTableComment=_OriSNMPTrapHostTableComment_Object((1,3,6,1,4,1,11898,2,1,4,5,1,4),_OriSNMPTrapHostTableComment_Type())
oriSNMPTrapHostTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPTrapHostTableComment.setStatus(_A)
class _OriSNMPTrapHostTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriSNMPTrapHostTableEntryStatus_Type.__name__=_D
_OriSNMPTrapHostTableEntryStatus_Object=MibTableColumn
oriSNMPTrapHostTableEntryStatus=_OriSNMPTrapHostTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,4,5,1,5),_OriSNMPTrapHostTableEntryStatus_Type())
oriSNMPTrapHostTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPTrapHostTableEntryStatus.setStatus(_A)
_OriSNMPInterfaceBitmask_Type=InterfaceBitmask
_OriSNMPInterfaceBitmask_Object=MibScalar
oriSNMPInterfaceBitmask=_OriSNMPInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,4,7),_OriSNMPInterfaceBitmask_Type())
oriSNMPInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPInterfaceBitmask.setStatus(_A)
_OriSNMPErrorMessage_Type=DisplayString
_OriSNMPErrorMessage_Object=MibScalar
oriSNMPErrorMessage=_OriSNMPErrorMessage_Object((1,3,6,1,4,1,11898,2,1,4,8),_OriSNMPErrorMessage_Type())
oriSNMPErrorMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSNMPErrorMessage.setStatus(_A)
class _OriSNMPAccessTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriSNMPAccessTableStatus_Type.__name__=_D
_OriSNMPAccessTableStatus_Object=MibScalar
oriSNMPAccessTableStatus=_OriSNMPAccessTableStatus_Object((1,3,6,1,4,1,11898,2,1,4,9),_OriSNMPAccessTableStatus_Type())
oriSNMPAccessTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPAccessTableStatus.setStatus(_A)
class _OriSNMPTrapType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('snmp-v1',1),('snmp-v2c',2)))
_OriSNMPTrapType_Type.__name__=_D
_OriSNMPTrapType_Object=MibScalar
oriSNMPTrapType=_OriSNMPTrapType_Object((1,3,6,1,4,1,11898,2,1,4,10),_OriSNMPTrapType_Type())
oriSNMPTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPTrapType.setStatus(_A)
class _OriSNMPSecureManagementStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriSNMPSecureManagementStatus_Type.__name__=_D
_OriSNMPSecureManagementStatus_Object=MibScalar
oriSNMPSecureManagementStatus=_OriSNMPSecureManagementStatus_Object((1,3,6,1,4,1,11898,2,1,4,11),_OriSNMPSecureManagementStatus_Type())
oriSNMPSecureManagementStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPSecureManagementStatus.setStatus(_A)
class _OriSNMPV3AuthPassword_Type(DisplayString):defaultValue=OctetString(_U);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,32))
_OriSNMPV3AuthPassword_Type.__name__=_O
_OriSNMPV3AuthPassword_Object=MibScalar
oriSNMPV3AuthPassword=_OriSNMPV3AuthPassword_Object((1,3,6,1,4,1,11898,2,1,4,12),_OriSNMPV3AuthPassword_Type())
oriSNMPV3AuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPV3AuthPassword.setStatus(_A)
class _OriSNMPV3PrivPassword_Type(DisplayString):defaultValue=OctetString(_U);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,32))
_OriSNMPV3PrivPassword_Type.__name__=_O
_OriSNMPV3PrivPassword_Object=MibScalar
oriSNMPV3PrivPassword=_OriSNMPV3PrivPassword_Object((1,3,6,1,4,1,11898,2,1,4,13),_OriSNMPV3PrivPassword_Type())
oriSNMPV3PrivPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNMPV3PrivPassword.setStatus(_A)
_OrinocoFiltering_ObjectIdentity=ObjectIdentity
orinocoFiltering=_OrinocoFiltering_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5))
_OrinocoProtocolFilter_ObjectIdentity=ObjectIdentity
orinocoProtocolFilter=_OrinocoProtocolFilter_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,1))
class _OriProtocolFilterOperationType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_OriProtocolFilterOperationType_Type.__name__=_D
_OriProtocolFilterOperationType_Object=MibScalar
oriProtocolFilterOperationType=_OriProtocolFilterOperationType_Object((1,3,6,1,4,1,11898,2,1,5,1,1),_OriProtocolFilterOperationType_Type())
oriProtocolFilterOperationType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProtocolFilterOperationType.setStatus(_A)
_OriProtocolFilterTable_Object=MibTable
oriProtocolFilterTable=_OriProtocolFilterTable_Object((1,3,6,1,4,1,11898,2,1,5,1,2))
if mibBuilder.loadTexts:oriProtocolFilterTable.setStatus(_A)
_OriProtocolFilterTableEntry_Object=MibTableRow
oriProtocolFilterTableEntry=_OriProtocolFilterTableEntry_Object((1,3,6,1,4,1,11898,2,1,5,1,2,1))
oriProtocolFilterTableEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:oriProtocolFilterTableEntry.setStatus(_A)
class _OriProtocolFilterTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_OriProtocolFilterTableIndex_Type.__name__=_D
_OriProtocolFilterTableIndex_Object=MibTableColumn
oriProtocolFilterTableIndex=_OriProtocolFilterTableIndex_Object((1,3,6,1,4,1,11898,2,1,5,1,2,1,1),_OriProtocolFilterTableIndex_Type())
oriProtocolFilterTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriProtocolFilterTableIndex.setStatus(_A)
class _OriProtocolFilterProtocol_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_OriProtocolFilterProtocol_Type.__name__=_V
_OriProtocolFilterProtocol_Object=MibTableColumn
oriProtocolFilterProtocol=_OriProtocolFilterProtocol_Object((1,3,6,1,4,1,11898,2,1,5,1,2,1,2),_OriProtocolFilterProtocol_Type())
oriProtocolFilterProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProtocolFilterProtocol.setStatus(_A)
_OriProtocolFilterProtocolComment_Type=DisplayString
_OriProtocolFilterProtocolComment_Object=MibTableColumn
oriProtocolFilterProtocolComment=_OriProtocolFilterProtocolComment_Object((1,3,6,1,4,1,11898,2,1,5,1,2,1,3),_OriProtocolFilterProtocolComment_Type())
oriProtocolFilterProtocolComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProtocolFilterProtocolComment.setStatus(_A)
class _OriProtocolFilterTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriProtocolFilterTableEntryStatus_Type.__name__=_D
_OriProtocolFilterTableEntryStatus_Object=MibTableColumn
oriProtocolFilterTableEntryStatus=_OriProtocolFilterTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,5,1,2,1,4),_OriProtocolFilterTableEntryStatus_Type())
oriProtocolFilterTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProtocolFilterTableEntryStatus.setStatus(_A)
_OriProtocolFilterTableInterfaceBitmask_Type=InterfaceBitmask
_OriProtocolFilterTableInterfaceBitmask_Object=MibTableColumn
oriProtocolFilterTableInterfaceBitmask=_OriProtocolFilterTableInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,5,1,2,1,5),_OriProtocolFilterTableInterfaceBitmask_Type())
oriProtocolFilterTableInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProtocolFilterTableInterfaceBitmask.setStatus(_A)
_OriProtocolFilterProtocolString_Type=DisplayString
_OriProtocolFilterProtocolString_Object=MibTableColumn
oriProtocolFilterProtocolString=_OriProtocolFilterProtocolString_Object((1,3,6,1,4,1,11898,2,1,5,1,2,1,6),_OriProtocolFilterProtocolString_Type())
oriProtocolFilterProtocolString.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProtocolFilterProtocolString.setStatus(_A)
_OriProtocolFilterInterfaceBitmask_Type=InterfaceBitmask
_OriProtocolFilterInterfaceBitmask_Object=MibScalar
oriProtocolFilterInterfaceBitmask=_OriProtocolFilterInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,5,1,3),_OriProtocolFilterInterfaceBitmask_Type())
oriProtocolFilterInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProtocolFilterInterfaceBitmask.setStatus(_A)
_OrinocoAccessControl_ObjectIdentity=ObjectIdentity
orinocoAccessControl=_OrinocoAccessControl_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,2))
class _OriAccessControlStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriAccessControlStatus_Type.__name__=_D
_OriAccessControlStatus_Object=MibScalar
oriAccessControlStatus=_OriAccessControlStatus_Object((1,3,6,1,4,1,11898,2,1,5,2,1),_OriAccessControlStatus_Type())
oriAccessControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriAccessControlStatus.setStatus(_A)
class _OriAccessControlOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_OriAccessControlOperationType_Type.__name__=_D
_OriAccessControlOperationType_Object=MibScalar
oriAccessControlOperationType=_OriAccessControlOperationType_Object((1,3,6,1,4,1,11898,2,1,5,2,2),_OriAccessControlOperationType_Type())
oriAccessControlOperationType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriAccessControlOperationType.setStatus(_A)
_OriAccessControlTable_Object=MibTable
oriAccessControlTable=_OriAccessControlTable_Object((1,3,6,1,4,1,11898,2,1,5,2,3))
if mibBuilder.loadTexts:oriAccessControlTable.setStatus(_A)
_OriAccessControlEntry_Object=MibTableRow
oriAccessControlEntry=_OriAccessControlEntry_Object((1,3,6,1,4,1,11898,2,1,5,2,3,1))
oriAccessControlEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:oriAccessControlEntry.setStatus(_A)
class _OriAccessControlTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_OriAccessControlTableIndex_Type.__name__=_D
_OriAccessControlTableIndex_Object=MibTableColumn
oriAccessControlTableIndex=_OriAccessControlTableIndex_Object((1,3,6,1,4,1,11898,2,1,5,2,3,1,1),_OriAccessControlTableIndex_Type())
oriAccessControlTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriAccessControlTableIndex.setStatus(_A)
_OriAccessControlTableMACAddress_Type=PhysAddress
_OriAccessControlTableMACAddress_Object=MibTableColumn
oriAccessControlTableMACAddress=_OriAccessControlTableMACAddress_Object((1,3,6,1,4,1,11898,2,1,5,2,3,1,2),_OriAccessControlTableMACAddress_Type())
oriAccessControlTableMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriAccessControlTableMACAddress.setStatus(_A)
_OriAccessControlTableComment_Type=DisplayString
_OriAccessControlTableComment_Object=MibTableColumn
oriAccessControlTableComment=_OriAccessControlTableComment_Object((1,3,6,1,4,1,11898,2,1,5,2,3,1,3),_OriAccessControlTableComment_Type())
oriAccessControlTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriAccessControlTableComment.setStatus(_A)
class _OriAccessControlTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriAccessControlTableEntryStatus_Type.__name__=_D
_OriAccessControlTableEntryStatus_Object=MibTableColumn
oriAccessControlTableEntryStatus=_OriAccessControlTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,5,2,3,1,4),_OriAccessControlTableEntryStatus_Type())
oriAccessControlTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriAccessControlTableEntryStatus.setStatus(_A)
_OrinocoStaticMACAddressFilter_ObjectIdentity=ObjectIdentity
orinocoStaticMACAddressFilter=_OrinocoStaticMACAddressFilter_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,3))
_OriStaticMACAddressFilterTable_Object=MibTable
oriStaticMACAddressFilterTable=_OriStaticMACAddressFilterTable_Object((1,3,6,1,4,1,11898,2,1,5,3,1))
if mibBuilder.loadTexts:oriStaticMACAddressFilterTable.setStatus(_A)
_OriStaticMACAddressFilterEntry_Object=MibTableRow
oriStaticMACAddressFilterEntry=_OriStaticMACAddressFilterEntry_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1))
oriStaticMACAddressFilterEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:oriStaticMACAddressFilterEntry.setStatus(_A)
class _OriStaticMACAddressFilterTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_OriStaticMACAddressFilterTableIndex_Type.__name__=_D
_OriStaticMACAddressFilterTableIndex_Object=MibTableColumn
oriStaticMACAddressFilterTableIndex=_OriStaticMACAddressFilterTableIndex_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1,1),_OriStaticMACAddressFilterTableIndex_Type())
oriStaticMACAddressFilterTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStaticMACAddressFilterTableIndex.setStatus(_A)
_OriStaticMACAddressFilterWiredAddress_Type=PhysAddress
_OriStaticMACAddressFilterWiredAddress_Object=MibTableColumn
oriStaticMACAddressFilterWiredAddress=_OriStaticMACAddressFilterWiredAddress_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1,2),_OriStaticMACAddressFilterWiredAddress_Type())
oriStaticMACAddressFilterWiredAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStaticMACAddressFilterWiredAddress.setStatus(_A)
_OriStaticMACAddressFilterWiredMask_Type=PhysAddress
_OriStaticMACAddressFilterWiredMask_Object=MibTableColumn
oriStaticMACAddressFilterWiredMask=_OriStaticMACAddressFilterWiredMask_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1,3),_OriStaticMACAddressFilterWiredMask_Type())
oriStaticMACAddressFilterWiredMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStaticMACAddressFilterWiredMask.setStatus(_A)
_OriStaticMACAddressFilterWirelessAddress_Type=PhysAddress
_OriStaticMACAddressFilterWirelessAddress_Object=MibTableColumn
oriStaticMACAddressFilterWirelessAddress=_OriStaticMACAddressFilterWirelessAddress_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1,4),_OriStaticMACAddressFilterWirelessAddress_Type())
oriStaticMACAddressFilterWirelessAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStaticMACAddressFilterWirelessAddress.setStatus(_A)
_OriStaticMACAddressFilterWirelessMask_Type=PhysAddress
_OriStaticMACAddressFilterWirelessMask_Object=MibTableColumn
oriStaticMACAddressFilterWirelessMask=_OriStaticMACAddressFilterWirelessMask_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1,5),_OriStaticMACAddressFilterWirelessMask_Type())
oriStaticMACAddressFilterWirelessMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStaticMACAddressFilterWirelessMask.setStatus(_A)
class _OriStaticMACAddressFilterTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriStaticMACAddressFilterTableEntryStatus_Type.__name__=_D
_OriStaticMACAddressFilterTableEntryStatus_Object=MibTableColumn
oriStaticMACAddressFilterTableEntryStatus=_OriStaticMACAddressFilterTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1,6),_OriStaticMACAddressFilterTableEntryStatus_Type())
oriStaticMACAddressFilterTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStaticMACAddressFilterTableEntryStatus.setStatus(_A)
_OriStaticMACAddressFilterComment_Type=DisplayString
_OriStaticMACAddressFilterComment_Object=MibTableColumn
oriStaticMACAddressFilterComment=_OriStaticMACAddressFilterComment_Object((1,3,6,1,4,1,11898,2,1,5,3,1,1,7),_OriStaticMACAddressFilterComment_Type())
oriStaticMACAddressFilterComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStaticMACAddressFilterComment.setStatus(_A)
_OrinocoStormThreshold_ObjectIdentity=ObjectIdentity
orinocoStormThreshold=_OrinocoStormThreshold_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,4))
class _OriBroadcastAddressThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OriBroadcastAddressThreshold_Type.__name__=_D
_OriBroadcastAddressThreshold_Object=MibScalar
oriBroadcastAddressThreshold=_OriBroadcastAddressThreshold_Object((1,3,6,1,4,1,11898,2,1,5,4,1),_OriBroadcastAddressThreshold_Type())
oriBroadcastAddressThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriBroadcastAddressThreshold.setStatus(_A)
class _OriMulticastAddressThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OriMulticastAddressThreshold_Type.__name__=_D
_OriMulticastAddressThreshold_Object=MibScalar
oriMulticastAddressThreshold=_OriMulticastAddressThreshold_Object((1,3,6,1,4,1,11898,2,1,5,4,2),_OriMulticastAddressThreshold_Type())
oriMulticastAddressThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:oriMulticastAddressThreshold.setStatus(_A)
_OriStormThresholdTable_Object=MibTable
oriStormThresholdTable=_OriStormThresholdTable_Object((1,3,6,1,4,1,11898,2,1,5,4,3))
if mibBuilder.loadTexts:oriStormThresholdTable.setStatus(_A)
_OriStormThresholdTableEntry_Object=MibTableRow
oriStormThresholdTableEntry=_OriStormThresholdTableEntry_Object((1,3,6,1,4,1,11898,2,1,5,4,3,1))
oriStormThresholdTableEntry.setIndexNames((0,_S,_T))
if mibBuilder.loadTexts:oriStormThresholdTableEntry.setStatus(_A)
class _OriStormThresholdIfBroadcast_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_OriStormThresholdIfBroadcast_Type.__name__=_D
_OriStormThresholdIfBroadcast_Object=MibTableColumn
oriStormThresholdIfBroadcast=_OriStormThresholdIfBroadcast_Object((1,3,6,1,4,1,11898,2,1,5,4,3,1,1),_OriStormThresholdIfBroadcast_Type())
oriStormThresholdIfBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStormThresholdIfBroadcast.setStatus(_A)
class _OriStormThresholdIfMulticast_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_OriStormThresholdIfMulticast_Type.__name__=_D
_OriStormThresholdIfMulticast_Object=MibTableColumn
oriStormThresholdIfMulticast=_OriStormThresholdIfMulticast_Object((1,3,6,1,4,1,11898,2,1,5,4,3,1,2),_OriStormThresholdIfMulticast_Type())
oriStormThresholdIfMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStormThresholdIfMulticast.setStatus(_A)
_OrinocoPortFilter_ObjectIdentity=ObjectIdentity
orinocoPortFilter=_OrinocoPortFilter_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,5))
class _OriPortFilterStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriPortFilterStatus_Type.__name__=_D
_OriPortFilterStatus_Object=MibScalar
oriPortFilterStatus=_OriPortFilterStatus_Object((1,3,6,1,4,1,11898,2,1,5,5,1),_OriPortFilterStatus_Type())
oriPortFilterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPortFilterStatus.setStatus(_A)
class _OriPortFilterOperationType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_OriPortFilterOperationType_Type.__name__=_D
_OriPortFilterOperationType_Object=MibScalar
oriPortFilterOperationType=_OriPortFilterOperationType_Object((1,3,6,1,4,1,11898,2,1,5,5,2),_OriPortFilterOperationType_Type())
oriPortFilterOperationType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPortFilterOperationType.setStatus(_A)
_OriPortFilterTable_Object=MibTable
oriPortFilterTable=_OriPortFilterTable_Object((1,3,6,1,4,1,11898,2,1,5,5,3))
if mibBuilder.loadTexts:oriPortFilterTable.setStatus(_A)
_OriPortFilterTableEntry_Object=MibTableRow
oriPortFilterTableEntry=_OriPortFilterTableEntry_Object((1,3,6,1,4,1,11898,2,1,5,5,3,1))
oriPortFilterTableEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:oriPortFilterTableEntry.setStatus(_A)
class _OriPortFilterTableEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_OriPortFilterTableEntryIndex_Type.__name__=_D
_OriPortFilterTableEntryIndex_Object=MibTableColumn
oriPortFilterTableEntryIndex=_OriPortFilterTableEntryIndex_Object((1,3,6,1,4,1,11898,2,1,5,5,3,1,1),_OriPortFilterTableEntryIndex_Type())
oriPortFilterTableEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPortFilterTableEntryIndex.setStatus(_A)
_OriPortFilterTableEntryPort_Type=Integer32
_OriPortFilterTableEntryPort_Object=MibTableColumn
oriPortFilterTableEntryPort=_OriPortFilterTableEntryPort_Object((1,3,6,1,4,1,11898,2,1,5,5,3,1,2),_OriPortFilterTableEntryPort_Type())
oriPortFilterTableEntryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPortFilterTableEntryPort.setStatus(_A)
class _OriPortFilterTableEntryPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('udp',2),(_o,3)))
_OriPortFilterTableEntryPortType_Type.__name__=_D
_OriPortFilterTableEntryPortType_Object=MibTableColumn
oriPortFilterTableEntryPortType=_OriPortFilterTableEntryPortType_Object((1,3,6,1,4,1,11898,2,1,5,5,3,1,3),_OriPortFilterTableEntryPortType_Type())
oriPortFilterTableEntryPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPortFilterTableEntryPortType.setStatus(_A)
_OriPortFilterTableEntryInterfaceBitmask_Type=InterfaceBitmask
_OriPortFilterTableEntryInterfaceBitmask_Object=MibTableColumn
oriPortFilterTableEntryInterfaceBitmask=_OriPortFilterTableEntryInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,5,5,3,1,4),_OriPortFilterTableEntryInterfaceBitmask_Type())
oriPortFilterTableEntryInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPortFilterTableEntryInterfaceBitmask.setStatus(_A)
_OriPortFilterTableEntryComment_Type=DisplayString
_OriPortFilterTableEntryComment_Object=MibTableColumn
oriPortFilterTableEntryComment=_OriPortFilterTableEntryComment_Object((1,3,6,1,4,1,11898,2,1,5,5,3,1,5),_OriPortFilterTableEntryComment_Type())
oriPortFilterTableEntryComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPortFilterTableEntryComment.setStatus(_A)
class _OriPortFilterTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriPortFilterTableEntryStatus_Type.__name__=_D
_OriPortFilterTableEntryStatus_Object=MibTableColumn
oriPortFilterTableEntryStatus=_OriPortFilterTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,5,5,3,1,6),_OriPortFilterTableEntryStatus_Type())
oriPortFilterTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPortFilterTableEntryStatus.setStatus(_A)
_OrinocoAdvancedFiltering_ObjectIdentity=ObjectIdentity
orinocoAdvancedFiltering=_OrinocoAdvancedFiltering_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,6))
_OriBroadcastFilteringTable_Object=MibTable
oriBroadcastFilteringTable=_OriBroadcastFilteringTable_Object((1,3,6,1,4,1,11898,2,1,5,6,1))
if mibBuilder.loadTexts:oriBroadcastFilteringTable.setStatus(_A)
_OriBroadcastFilteringTableEntry_Object=MibTableRow
oriBroadcastFilteringTableEntry=_OriBroadcastFilteringTableEntry_Object((1,3,6,1,4,1,11898,2,1,5,6,1,1))
oriBroadcastFilteringTableEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:oriBroadcastFilteringTableEntry.setStatus(_A)
class _OriBroadcastFilteringTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_OriBroadcastFilteringTableIndex_Type.__name__=_D
_OriBroadcastFilteringTableIndex_Object=MibTableColumn
oriBroadcastFilteringTableIndex=_OriBroadcastFilteringTableIndex_Object((1,3,6,1,4,1,11898,2,1,5,6,1,1,1),_OriBroadcastFilteringTableIndex_Type())
oriBroadcastFilteringTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriBroadcastFilteringTableIndex.setStatus(_A)
_OriBroadcastFilteringProtocolName_Type=DisplayString
_OriBroadcastFilteringProtocolName_Object=MibTableColumn
oriBroadcastFilteringProtocolName=_OriBroadcastFilteringProtocolName_Object((1,3,6,1,4,1,11898,2,1,5,6,1,1,2),_OriBroadcastFilteringProtocolName_Type())
oriBroadcastFilteringProtocolName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriBroadcastFilteringProtocolName.setStatus(_A)
class _OriBroadcastFilteringDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ethernetToWireless',1),('wirelessToEthernet',2),(_o,3)))
_OriBroadcastFilteringDirection_Type.__name__=_D
_OriBroadcastFilteringDirection_Object=MibTableColumn
oriBroadcastFilteringDirection=_OriBroadcastFilteringDirection_Object((1,3,6,1,4,1,11898,2,1,5,6,1,1,3),_OriBroadcastFilteringDirection_Type())
oriBroadcastFilteringDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:oriBroadcastFilteringDirection.setStatus(_A)
class _OriBroadcastFilteringTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriBroadcastFilteringTableEntryStatus_Type.__name__=_D
_OriBroadcastFilteringTableEntryStatus_Object=MibTableColumn
oriBroadcastFilteringTableEntryStatus=_OriBroadcastFilteringTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,5,6,1,1,4),_OriBroadcastFilteringTableEntryStatus_Type())
oriBroadcastFilteringTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriBroadcastFilteringTableEntryStatus.setStatus(_A)
_OrinocoPacketForwarding_ObjectIdentity=ObjectIdentity
orinocoPacketForwarding=_OrinocoPacketForwarding_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,7))
class _OriPacketForwardingStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriPacketForwardingStatus_Type.__name__=_D
_OriPacketForwardingStatus_Object=MibScalar
oriPacketForwardingStatus=_OriPacketForwardingStatus_Object((1,3,6,1,4,1,11898,2,1,5,7,1),_OriPacketForwardingStatus_Type())
oriPacketForwardingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPacketForwardingStatus.setStatus(_A)
_OriPacketForwardingMACAddress_Type=MacAddress
_OriPacketForwardingMACAddress_Object=MibScalar
oriPacketForwardingMACAddress=_OriPacketForwardingMACAddress_Object((1,3,6,1,4,1,11898,2,1,5,7,2),_OriPacketForwardingMACAddress_Type())
oriPacketForwardingMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPacketForwardingMACAddress.setStatus(_A)
class _OriPacketForwardingInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_OriPacketForwardingInterface_Type.__name__=_D
_OriPacketForwardingInterface_Object=MibScalar
oriPacketForwardingInterface=_OriPacketForwardingInterface_Object((1,3,6,1,4,1,11898,2,1,5,7,3),_OriPacketForwardingInterface_Type())
oriPacketForwardingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPacketForwardingInterface.setStatus(_A)
_OrinocoIBSSTraffic_ObjectIdentity=ObjectIdentity
orinocoIBSSTraffic=_OrinocoIBSSTraffic_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,8))
class _OriIBSSTrafficOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_OriIBSSTrafficOperation_Type.__name__=_D
_OriIBSSTrafficOperation_Object=MibScalar
oriIBSSTrafficOperation=_OriIBSSTrafficOperation_Object((1,3,6,1,4,1,11898,2,1,5,8,1),_OriIBSSTrafficOperation_Type())
oriIBSSTrafficOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIBSSTrafficOperation.setStatus(_A)
_OrinocoIntraCellBlocking_ObjectIdentity=ObjectIdentity
orinocoIntraCellBlocking=_OrinocoIntraCellBlocking_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,9))
class _OriIntraCellBlockingStatus_Type(ObjStatus):defaultValue=2
_OriIntraCellBlockingStatus_Type.__name__=_J
_OriIntraCellBlockingStatus_Object=MibScalar
oriIntraCellBlockingStatus=_OriIntraCellBlockingStatus_Object((1,3,6,1,4,1,11898,2,1,5,9,1),_OriIntraCellBlockingStatus_Type())
oriIntraCellBlockingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingStatus.setStatus(_A)
_OriIntraCellBlockingMACTable_Object=MibTable
oriIntraCellBlockingMACTable=_OriIntraCellBlockingMACTable_Object((1,3,6,1,4,1,11898,2,1,5,9,2))
if mibBuilder.loadTexts:oriIntraCellBlockingMACTable.setStatus(_A)
_OriIntraCellBlockingMACTableEntry_Object=MibTableRow
oriIntraCellBlockingMACTableEntry=_OriIntraCellBlockingMACTableEntry_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1))
oriIntraCellBlockingMACTableEntry.setIndexNames((0,_E,_AH))
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableEntry.setStatus(_A)
class _OriIntraCellBlockingMACTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_OriIntraCellBlockingMACTableIndex_Type.__name__=_D
_OriIntraCellBlockingMACTableIndex_Object=MibTableColumn
oriIntraCellBlockingMACTableIndex=_OriIntraCellBlockingMACTableIndex_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,1),_OriIntraCellBlockingMACTableIndex_Type())
oriIntraCellBlockingMACTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableIndex.setStatus(_A)
_OriIntraCellBlockingMACTableMACAddress_Type=PhysAddress
_OriIntraCellBlockingMACTableMACAddress_Object=MibTableColumn
oriIntraCellBlockingMACTableMACAddress=_OriIntraCellBlockingMACTableMACAddress_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,2),_OriIntraCellBlockingMACTableMACAddress_Type())
oriIntraCellBlockingMACTableMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableMACAddress.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID1_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID1_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID1_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID1=_OriIntraCellBlockingMACTableGroupID1_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,3),_OriIntraCellBlockingMACTableGroupID1_Type())
oriIntraCellBlockingMACTableGroupID1.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID1.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID2_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID2_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID2_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID2=_OriIntraCellBlockingMACTableGroupID2_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,4),_OriIntraCellBlockingMACTableGroupID2_Type())
oriIntraCellBlockingMACTableGroupID2.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID2.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID3_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID3_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID3_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID3=_OriIntraCellBlockingMACTableGroupID3_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,5),_OriIntraCellBlockingMACTableGroupID3_Type())
oriIntraCellBlockingMACTableGroupID3.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID3.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID4_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID4_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID4_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID4=_OriIntraCellBlockingMACTableGroupID4_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,6),_OriIntraCellBlockingMACTableGroupID4_Type())
oriIntraCellBlockingMACTableGroupID4.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID4.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID5_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID5_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID5_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID5=_OriIntraCellBlockingMACTableGroupID5_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,7),_OriIntraCellBlockingMACTableGroupID5_Type())
oriIntraCellBlockingMACTableGroupID5.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID5.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID6_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID6_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID6_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID6=_OriIntraCellBlockingMACTableGroupID6_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,8),_OriIntraCellBlockingMACTableGroupID6_Type())
oriIntraCellBlockingMACTableGroupID6.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID6.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID7_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID7_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID7_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID7=_OriIntraCellBlockingMACTableGroupID7_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,9),_OriIntraCellBlockingMACTableGroupID7_Type())
oriIntraCellBlockingMACTableGroupID7.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID7.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID8_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID8_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID8_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID8=_OriIntraCellBlockingMACTableGroupID8_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,10),_OriIntraCellBlockingMACTableGroupID8_Type())
oriIntraCellBlockingMACTableGroupID8.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID8.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID9_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID9_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID9_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID9=_OriIntraCellBlockingMACTableGroupID9_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,11),_OriIntraCellBlockingMACTableGroupID9_Type())
oriIntraCellBlockingMACTableGroupID9.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID9.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID10_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID10_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID10_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID10=_OriIntraCellBlockingMACTableGroupID10_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,12),_OriIntraCellBlockingMACTableGroupID10_Type())
oriIntraCellBlockingMACTableGroupID10.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID10.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID11_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID11_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID11_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID11=_OriIntraCellBlockingMACTableGroupID11_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,13),_OriIntraCellBlockingMACTableGroupID11_Type())
oriIntraCellBlockingMACTableGroupID11.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID11.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID12_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID12_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID12_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID12=_OriIntraCellBlockingMACTableGroupID12_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,14),_OriIntraCellBlockingMACTableGroupID12_Type())
oriIntraCellBlockingMACTableGroupID12.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID12.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID13_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID13_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID13_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID13=_OriIntraCellBlockingMACTableGroupID13_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,15),_OriIntraCellBlockingMACTableGroupID13_Type())
oriIntraCellBlockingMACTableGroupID13.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID13.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID14_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID14_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID14_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID14=_OriIntraCellBlockingMACTableGroupID14_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,16),_OriIntraCellBlockingMACTableGroupID14_Type())
oriIntraCellBlockingMACTableGroupID14.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID14.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID15_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID15_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID15_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID15=_OriIntraCellBlockingMACTableGroupID15_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,17),_OriIntraCellBlockingMACTableGroupID15_Type())
oriIntraCellBlockingMACTableGroupID15.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID15.setStatus(_A)
class _OriIntraCellBlockingMACTableGroupID16_Type(ObjStatusActive):defaultValue=2
_OriIntraCellBlockingMACTableGroupID16_Type.__name__=_N
_OriIntraCellBlockingMACTableGroupID16_Object=MibTableColumn
oriIntraCellBlockingMACTableGroupID16=_OriIntraCellBlockingMACTableGroupID16_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,18),_OriIntraCellBlockingMACTableGroupID16_Type())
oriIntraCellBlockingMACTableGroupID16.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableGroupID16.setStatus(_A)
class _OriIntraCellBlockingMACTableEntryStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriIntraCellBlockingMACTableEntryStatus_Type.__name__=_D
_OriIntraCellBlockingMACTableEntryStatus_Object=MibTableColumn
oriIntraCellBlockingMACTableEntryStatus=_OriIntraCellBlockingMACTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,5,9,2,1,19),_OriIntraCellBlockingMACTableEntryStatus_Type())
oriIntraCellBlockingMACTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingMACTableEntryStatus.setStatus(_A)
_OriIntraCellBlockingGroupTable_Object=MibTable
oriIntraCellBlockingGroupTable=_OriIntraCellBlockingGroupTable_Object((1,3,6,1,4,1,11898,2,1,5,9,3))
if mibBuilder.loadTexts:oriIntraCellBlockingGroupTable.setStatus(_A)
_OriIntraCellBlockingGroupTableEntry_Object=MibTableRow
oriIntraCellBlockingGroupTableEntry=_OriIntraCellBlockingGroupTableEntry_Object((1,3,6,1,4,1,11898,2,1,5,9,3,1))
oriIntraCellBlockingGroupTableEntry.setIndexNames((0,_E,_AI))
if mibBuilder.loadTexts:oriIntraCellBlockingGroupTableEntry.setStatus(_A)
class _OriIntraCellBlockingGroupTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_OriIntraCellBlockingGroupTableIndex_Type.__name__=_D
_OriIntraCellBlockingGroupTableIndex_Object=MibTableColumn
oriIntraCellBlockingGroupTableIndex=_OriIntraCellBlockingGroupTableIndex_Object((1,3,6,1,4,1,11898,2,1,5,9,3,1,1),_OriIntraCellBlockingGroupTableIndex_Type())
oriIntraCellBlockingGroupTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIntraCellBlockingGroupTableIndex.setStatus(_A)
_OriIntraCellBlockingGroupTableName_Type=DisplayString
_OriIntraCellBlockingGroupTableName_Object=MibTableColumn
oriIntraCellBlockingGroupTableName=_OriIntraCellBlockingGroupTableName_Object((1,3,6,1,4,1,11898,2,1,5,9,3,1,2),_OriIntraCellBlockingGroupTableName_Type())
oriIntraCellBlockingGroupTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingGroupTableName.setStatus(_A)
class _OriIntraCellBlockingGroupTableEntryStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriIntraCellBlockingGroupTableEntryStatus_Type.__name__=_D
_OriIntraCellBlockingGroupTableEntryStatus_Object=MibTableColumn
oriIntraCellBlockingGroupTableEntryStatus=_OriIntraCellBlockingGroupTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,5,9,3,1,3),_OriIntraCellBlockingGroupTableEntryStatus_Type())
oriIntraCellBlockingGroupTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIntraCellBlockingGroupTableEntryStatus.setStatus(_A)
_OrinocoSecurityGw_ObjectIdentity=ObjectIdentity
orinocoSecurityGw=_OrinocoSecurityGw_ObjectIdentity((1,3,6,1,4,1,11898,2,1,5,10))
class _OriSecurityGwStatus_Type(ObjStatus):defaultValue=2
_OriSecurityGwStatus_Type.__name__=_J
_OriSecurityGwStatus_Object=MibScalar
oriSecurityGwStatus=_OriSecurityGwStatus_Object((1,3,6,1,4,1,11898,2,1,5,10,1),_OriSecurityGwStatus_Type())
oriSecurityGwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityGwStatus.setStatus(_A)
_OriSecurityGwMac_Type=MacAddress
_OriSecurityGwMac_Object=MibScalar
oriSecurityGwMac=_OriSecurityGwMac_Object((1,3,6,1,4,1,11898,2,1,5,10,2),_OriSecurityGwMac_Type())
oriSecurityGwMac.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityGwMac.setStatus(_A)
_OrinocoRADIUS_ObjectIdentity=ObjectIdentity
orinocoRADIUS=_OrinocoRADIUS_ObjectIdentity((1,3,6,1,4,1,11898,2,1,6))
_OrinocoRADIUSAuth_ObjectIdentity=ObjectIdentity
orinocoRADIUSAuth=_OrinocoRADIUSAuth_ObjectIdentity((1,3,6,1,4,1,11898,2,1,6,1))
_OriRADIUSAuthServerTable_Object=MibTable
oriRADIUSAuthServerTable=_OriRADIUSAuthServerTable_Object((1,3,6,1,4,1,11898,2,1,6,1,1))
if mibBuilder.loadTexts:oriRADIUSAuthServerTable.setStatus(_A)
_OriRADIUSAuthServerTableEntry_Object=MibTableRow
oriRADIUSAuthServerTableEntry=_OriRADIUSAuthServerTableEntry_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1))
oriRADIUSAuthServerTableEntry.setIndexNames((0,_E,_AJ))
if mibBuilder.loadTexts:oriRADIUSAuthServerTableEntry.setStatus(_A)
class _OriRADIUSAuthServerTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_OriRADIUSAuthServerTableIndex_Type.__name__=_D
_OriRADIUSAuthServerTableIndex_Object=MibTableColumn
oriRADIUSAuthServerTableIndex=_OriRADIUSAuthServerTableIndex_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,1),_OriRADIUSAuthServerTableIndex_Type())
oriRADIUSAuthServerTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthServerTableIndex.setStatus(_A)
class _OriRADIUSAuthServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AK,1),(_AL,2),(_AM,3),('authdot1x',4)))
_OriRADIUSAuthServerType_Type.__name__=_D
_OriRADIUSAuthServerType_Object=MibTableColumn
oriRADIUSAuthServerType=_OriRADIUSAuthServerType_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,2),_OriRADIUSAuthServerType_Type())
oriRADIUSAuthServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthServerType.setStatus(_A)
class _OriRADIUSAuthServerTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriRADIUSAuthServerTableEntryStatus_Type.__name__=_D
_OriRADIUSAuthServerTableEntryStatus_Object=MibTableColumn
oriRADIUSAuthServerTableEntryStatus=_OriRADIUSAuthServerTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,3),_OriRADIUSAuthServerTableEntryStatus_Type())
oriRADIUSAuthServerTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerTableEntryStatus.setStatus(_A)
_OriRADIUSAuthServerIPAddress_Type=IpAddress
_OriRADIUSAuthServerIPAddress_Object=MibTableColumn
oriRADIUSAuthServerIPAddress=_OriRADIUSAuthServerIPAddress_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,4),_OriRADIUSAuthServerIPAddress_Type())
oriRADIUSAuthServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerIPAddress.setStatus(_H)
class _OriRADIUSAuthServerDestPort_Type(Integer32):defaultValue=1812
_OriRADIUSAuthServerDestPort_Type.__name__=_D
_OriRADIUSAuthServerDestPort_Object=MibTableColumn
oriRADIUSAuthServerDestPort=_OriRADIUSAuthServerDestPort_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,5),_OriRADIUSAuthServerDestPort_Type())
oriRADIUSAuthServerDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerDestPort.setStatus(_A)
_OriRADIUSAuthServerSharedSecret_Type=DisplayString
_OriRADIUSAuthServerSharedSecret_Object=MibTableColumn
oriRADIUSAuthServerSharedSecret=_OriRADIUSAuthServerSharedSecret_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,6),_OriRADIUSAuthServerSharedSecret_Type())
oriRADIUSAuthServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerSharedSecret.setStatus(_A)
class _OriRADIUSAuthServerResponseTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_OriRADIUSAuthServerResponseTime_Type.__name__=_D
_OriRADIUSAuthServerResponseTime_Object=MibTableColumn
oriRADIUSAuthServerResponseTime=_OriRADIUSAuthServerResponseTime_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,7),_OriRADIUSAuthServerResponseTime_Type())
oriRADIUSAuthServerResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerResponseTime.setStatus(_A)
class _OriRADIUSAuthServerMaximumRetransmission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_OriRADIUSAuthServerMaximumRetransmission_Type.__name__=_D
_OriRADIUSAuthServerMaximumRetransmission_Object=MibTableColumn
oriRADIUSAuthServerMaximumRetransmission=_OriRADIUSAuthServerMaximumRetransmission_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,8),_OriRADIUSAuthServerMaximumRetransmission_Type())
oriRADIUSAuthServerMaximumRetransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerMaximumRetransmission.setStatus(_A)
_OriRADIUSAuthClientAccessRequests_Type=Counter32
_OriRADIUSAuthClientAccessRequests_Object=MibTableColumn
oriRADIUSAuthClientAccessRequests=_OriRADIUSAuthClientAccessRequests_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,9),_OriRADIUSAuthClientAccessRequests_Type())
oriRADIUSAuthClientAccessRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientAccessRequests.setStatus(_A)
_OriRADIUSAuthClientAccessRetransmissions_Type=Counter32
_OriRADIUSAuthClientAccessRetransmissions_Object=MibTableColumn
oriRADIUSAuthClientAccessRetransmissions=_OriRADIUSAuthClientAccessRetransmissions_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,10),_OriRADIUSAuthClientAccessRetransmissions_Type())
oriRADIUSAuthClientAccessRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientAccessRetransmissions.setStatus(_A)
_OriRADIUSAuthClientAccessAccepts_Type=Counter32
_OriRADIUSAuthClientAccessAccepts_Object=MibTableColumn
oriRADIUSAuthClientAccessAccepts=_OriRADIUSAuthClientAccessAccepts_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,11),_OriRADIUSAuthClientAccessAccepts_Type())
oriRADIUSAuthClientAccessAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientAccessAccepts.setStatus(_A)
_OriRADIUSAuthClientAccessChallenges_Type=Counter32
_OriRADIUSAuthClientAccessChallenges_Object=MibTableColumn
oriRADIUSAuthClientAccessChallenges=_OriRADIUSAuthClientAccessChallenges_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,12),_OriRADIUSAuthClientAccessChallenges_Type())
oriRADIUSAuthClientAccessChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientAccessChallenges.setStatus(_A)
_OriRADIUSAuthClientAccessRejects_Type=Counter32
_OriRADIUSAuthClientAccessRejects_Object=MibTableColumn
oriRADIUSAuthClientAccessRejects=_OriRADIUSAuthClientAccessRejects_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,13),_OriRADIUSAuthClientAccessRejects_Type())
oriRADIUSAuthClientAccessRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientAccessRejects.setStatus(_A)
_OriRADIUSAuthClientMalformedAccessResponses_Type=Counter32
_OriRADIUSAuthClientMalformedAccessResponses_Object=MibTableColumn
oriRADIUSAuthClientMalformedAccessResponses=_OriRADIUSAuthClientMalformedAccessResponses_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,14),_OriRADIUSAuthClientMalformedAccessResponses_Type())
oriRADIUSAuthClientMalformedAccessResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientMalformedAccessResponses.setStatus(_A)
_OriRADIUSAuthClientAuthInvalidAuthenticators_Type=Counter32
_OriRADIUSAuthClientAuthInvalidAuthenticators_Object=MibTableColumn
oriRADIUSAuthClientAuthInvalidAuthenticators=_OriRADIUSAuthClientAuthInvalidAuthenticators_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,15),_OriRADIUSAuthClientAuthInvalidAuthenticators_Type())
oriRADIUSAuthClientAuthInvalidAuthenticators.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientAuthInvalidAuthenticators.setStatus(_A)
_OriRADIUSAuthClientTimeouts_Type=Counter32
_OriRADIUSAuthClientTimeouts_Object=MibTableColumn
oriRADIUSAuthClientTimeouts=_OriRADIUSAuthClientTimeouts_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,16),_OriRADIUSAuthClientTimeouts_Type())
oriRADIUSAuthClientTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientTimeouts.setStatus(_A)
_OriRADIUSAuthServerNameOrIPAddress_Type=DisplayString
_OriRADIUSAuthServerNameOrIPAddress_Object=MibTableColumn
oriRADIUSAuthServerNameOrIPAddress=_OriRADIUSAuthServerNameOrIPAddress_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,17),_OriRADIUSAuthServerNameOrIPAddress_Type())
oriRADIUSAuthServerNameOrIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerNameOrIPAddress.setStatus(_A)
class _OriRADIUSAuthServerAddressingFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_OriRADIUSAuthServerAddressingFormat_Type.__name__=_D
_OriRADIUSAuthServerAddressingFormat_Object=MibTableColumn
oriRADIUSAuthServerAddressingFormat=_OriRADIUSAuthServerAddressingFormat_Object((1,3,6,1,4,1,11898,2,1,6,1,1,1,18),_OriRADIUSAuthServerAddressingFormat_Type())
oriRADIUSAuthServerAddressingFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthServerAddressingFormat.setStatus(_A)
_OrinocoRADIUSAcct_ObjectIdentity=ObjectIdentity
orinocoRADIUSAcct=_OrinocoRADIUSAcct_ObjectIdentity((1,3,6,1,4,1,11898,2,1,6,2))
class _OriRADIUSAcctStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriRADIUSAcctStatus_Type.__name__=_D
_OriRADIUSAcctStatus_Object=MibScalar
oriRADIUSAcctStatus=_OriRADIUSAcctStatus_Object((1,3,6,1,4,1,11898,2,1,6,2,1),_OriRADIUSAcctStatus_Type())
oriRADIUSAcctStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctStatus.setStatus(_H)
class _OriRADIUSAcctInactivityTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_OriRADIUSAcctInactivityTimer_Type.__name__=_D
_OriRADIUSAcctInactivityTimer_Object=MibScalar
oriRADIUSAcctInactivityTimer=_OriRADIUSAcctInactivityTimer_Object((1,3,6,1,4,1,11898,2,1,6,2,2),_OriRADIUSAcctInactivityTimer_Type())
oriRADIUSAcctInactivityTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctInactivityTimer.setStatus(_H)
_OriRADIUSAcctServerTable_Object=MibTable
oriRADIUSAcctServerTable=_OriRADIUSAcctServerTable_Object((1,3,6,1,4,1,11898,2,1,6,2,3))
if mibBuilder.loadTexts:oriRADIUSAcctServerTable.setStatus(_H)
_OriRADIUSAcctServerTableEntry_Object=MibTableRow
oriRADIUSAcctServerTableEntry=_OriRADIUSAcctServerTableEntry_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1))
oriRADIUSAcctServerTableEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:oriRADIUSAcctServerTableEntry.setStatus(_H)
class _OriRADIUSAcctServerTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OriRADIUSAcctServerTableIndex_Type.__name__=_D
_OriRADIUSAcctServerTableIndex_Object=MibTableColumn
oriRADIUSAcctServerTableIndex=_OriRADIUSAcctServerTableIndex_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,1),_OriRADIUSAcctServerTableIndex_Type())
oriRADIUSAcctServerTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctServerTableIndex.setStatus(_H)
class _OriRADIUSAcctServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AK,1),(_AL,2),(_AM,3)))
_OriRADIUSAcctServerType_Type.__name__=_D
_OriRADIUSAcctServerType_Object=MibTableColumn
oriRADIUSAcctServerType=_OriRADIUSAcctServerType_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,2),_OriRADIUSAcctServerType_Type())
oriRADIUSAcctServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctServerType.setStatus(_H)
class _OriRADIUSAcctServerTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriRADIUSAcctServerTableEntryStatus_Type.__name__=_D
_OriRADIUSAcctServerTableEntryStatus_Object=MibTableColumn
oriRADIUSAcctServerTableEntryStatus=_OriRADIUSAcctServerTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,3),_OriRADIUSAcctServerTableEntryStatus_Type())
oriRADIUSAcctServerTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerTableEntryStatus.setStatus(_H)
_OriRADIUSAcctServerIPAddress_Type=IpAddress
_OriRADIUSAcctServerIPAddress_Object=MibTableColumn
oriRADIUSAcctServerIPAddress=_OriRADIUSAcctServerIPAddress_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,4),_OriRADIUSAcctServerIPAddress_Type())
oriRADIUSAcctServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerIPAddress.setStatus(_H)
class _OriRADIUSAcctServerDestPort_Type(Integer32):defaultValue=1813
_OriRADIUSAcctServerDestPort_Type.__name__=_D
_OriRADIUSAcctServerDestPort_Object=MibTableColumn
oriRADIUSAcctServerDestPort=_OriRADIUSAcctServerDestPort_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,5),_OriRADIUSAcctServerDestPort_Type())
oriRADIUSAcctServerDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerDestPort.setStatus(_H)
_OriRADIUSAcctServerSharedSecret_Type=DisplayString
_OriRADIUSAcctServerSharedSecret_Object=MibTableColumn
oriRADIUSAcctServerSharedSecret=_OriRADIUSAcctServerSharedSecret_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,6),_OriRADIUSAcctServerSharedSecret_Type())
oriRADIUSAcctServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerSharedSecret.setStatus(_H)
class _OriRADIUSAcctServerResponseTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_OriRADIUSAcctServerResponseTime_Type.__name__=_D
_OriRADIUSAcctServerResponseTime_Object=MibTableColumn
oriRADIUSAcctServerResponseTime=_OriRADIUSAcctServerResponseTime_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,7),_OriRADIUSAcctServerResponseTime_Type())
oriRADIUSAcctServerResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerResponseTime.setStatus(_H)
class _OriRADIUSAcctServerMaximumRetransmission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_OriRADIUSAcctServerMaximumRetransmission_Type.__name__=_D
_OriRADIUSAcctServerMaximumRetransmission_Object=MibTableColumn
oriRADIUSAcctServerMaximumRetransmission=_OriRADIUSAcctServerMaximumRetransmission_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,8),_OriRADIUSAcctServerMaximumRetransmission_Type())
oriRADIUSAcctServerMaximumRetransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerMaximumRetransmission.setStatus(_H)
_OriRADIUSAcctClientAccountingRequests_Type=Counter32
_OriRADIUSAcctClientAccountingRequests_Object=MibTableColumn
oriRADIUSAcctClientAccountingRequests=_OriRADIUSAcctClientAccountingRequests_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,9),_OriRADIUSAcctClientAccountingRequests_Type())
oriRADIUSAcctClientAccountingRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientAccountingRequests.setStatus(_H)
_OriRADIUSAcctClientAccountingRetransmissions_Type=Counter32
_OriRADIUSAcctClientAccountingRetransmissions_Object=MibTableColumn
oriRADIUSAcctClientAccountingRetransmissions=_OriRADIUSAcctClientAccountingRetransmissions_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,10),_OriRADIUSAcctClientAccountingRetransmissions_Type())
oriRADIUSAcctClientAccountingRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientAccountingRetransmissions.setStatus(_H)
_OriRADIUSAcctClientAccountingResponses_Type=Counter32
_OriRADIUSAcctClientAccountingResponses_Object=MibTableColumn
oriRADIUSAcctClientAccountingResponses=_OriRADIUSAcctClientAccountingResponses_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,11),_OriRADIUSAcctClientAccountingResponses_Type())
oriRADIUSAcctClientAccountingResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientAccountingResponses.setStatus(_H)
_OriRADIUSAcctClientAcctInvalidAuthenticators_Type=Counter32
_OriRADIUSAcctClientAcctInvalidAuthenticators_Object=MibTableColumn
oriRADIUSAcctClientAcctInvalidAuthenticators=_OriRADIUSAcctClientAcctInvalidAuthenticators_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,12),_OriRADIUSAcctClientAcctInvalidAuthenticators_Type())
oriRADIUSAcctClientAcctInvalidAuthenticators.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientAcctInvalidAuthenticators.setStatus(_H)
_OriRADIUSAcctServerNameOrIPAddress_Type=DisplayString
_OriRADIUSAcctServerNameOrIPAddress_Object=MibTableColumn
oriRADIUSAcctServerNameOrIPAddress=_OriRADIUSAcctServerNameOrIPAddress_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,13),_OriRADIUSAcctServerNameOrIPAddress_Type())
oriRADIUSAcctServerNameOrIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerNameOrIPAddress.setStatus(_H)
class _OriRADIUSAcctServerAddressingFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_OriRADIUSAcctServerAddressingFormat_Type.__name__=_D
_OriRADIUSAcctServerAddressingFormat_Object=MibTableColumn
oriRADIUSAcctServerAddressingFormat=_OriRADIUSAcctServerAddressingFormat_Object((1,3,6,1,4,1,11898,2,1,6,2,3,1,14),_OriRADIUSAcctServerAddressingFormat_Type())
oriRADIUSAcctServerAddressingFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctServerAddressingFormat.setStatus(_H)
class _OriRADIUSAcctUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_OriRADIUSAcctUpdateInterval_Type.__name__=_D
_OriRADIUSAcctUpdateInterval_Object=MibScalar
oriRADIUSAcctUpdateInterval=_OriRADIUSAcctUpdateInterval_Object((1,3,6,1,4,1,11898,2,1,6,2,4),_OriRADIUSAcctUpdateInterval_Type())
oriRADIUSAcctUpdateInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAcctUpdateInterval.setStatus(_H)
_OriRADIUSClientInvalidServerAddress_Type=Counter32
_OriRADIUSClientInvalidServerAddress_Object=MibScalar
oriRADIUSClientInvalidServerAddress=_OriRADIUSClientInvalidServerAddress_Object((1,3,6,1,4,1,11898,2,1,6,3),_OriRADIUSClientInvalidServerAddress_Type())
oriRADIUSClientInvalidServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSClientInvalidServerAddress.setStatus(_A)
class _OriRADIUSMACAccessControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriRADIUSMACAccessControl_Type.__name__=_D
_OriRADIUSMACAccessControl_Object=MibScalar
oriRADIUSMACAccessControl=_OriRADIUSMACAccessControl_Object((1,3,6,1,4,1,11898,2,1,6,4),_OriRADIUSMACAccessControl_Type())
oriRADIUSMACAccessControl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSMACAccessControl.setStatus(_A)
class _OriRADIUSAuthorizationLifeTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(7200,43200))
_OriRADIUSAuthorizationLifeTime_Type.__name__=_D
_OriRADIUSAuthorizationLifeTime_Object=MibScalar
oriRADIUSAuthorizationLifeTime=_OriRADIUSAuthorizationLifeTime_Object((1,3,6,1,4,1,11898,2,1,6,5),_OriRADIUSAuthorizationLifeTime_Type())
oriRADIUSAuthorizationLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSAuthorizationLifeTime.setStatus(_A)
class _OriRADIUSMACAddressFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AO,1),(_AP,2),(_AQ,3),(_AR,4)))
_OriRADIUSMACAddressFormat_Type.__name__=_D
_OriRADIUSMACAddressFormat_Object=MibScalar
oriRADIUSMACAddressFormat=_OriRADIUSMACAddressFormat_Object((1,3,6,1,4,1,11898,2,1,6,6),_OriRADIUSMACAddressFormat_Type())
oriRADIUSMACAddressFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSMACAddressFormat.setStatus(_A)
class _OriRADIUSLocalUserStatus_Type(ObjStatus):defaultValue=2
_OriRADIUSLocalUserStatus_Type.__name__=_J
_OriRADIUSLocalUserStatus_Object=MibScalar
oriRADIUSLocalUserStatus=_OriRADIUSLocalUserStatus_Object((1,3,6,1,4,1,11898,2,1,6,7),_OriRADIUSLocalUserStatus_Type())
oriRADIUSLocalUserStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSLocalUserStatus.setStatus(_A)
class _OriRADIUSLocalUserPassword_Type(DisplayString):defaultValue=OctetString(_U);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,32))
_OriRADIUSLocalUserPassword_Type.__name__=_O
_OriRADIUSLocalUserPassword_Object=MibScalar
oriRADIUSLocalUserPassword=_OriRADIUSLocalUserPassword_Object((1,3,6,1,4,1,11898,2,1,6,8),_OriRADIUSLocalUserPassword_Type())
oriRADIUSLocalUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSLocalUserPassword.setStatus(_A)
_OriRADIUSbasedManagementAccessProfile_Type=DisplayString
_OriRADIUSbasedManagementAccessProfile_Object=MibScalar
oriRADIUSbasedManagementAccessProfile=_OriRADIUSbasedManagementAccessProfile_Object((1,3,6,1,4,1,11898,2,1,6,9),_OriRADIUSbasedManagementAccessProfile_Type())
oriRADIUSbasedManagementAccessProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSbasedManagementAccessProfile.setStatus(_A)
_OrinocoRADIUSSvrProfiles_ObjectIdentity=ObjectIdentity
orinocoRADIUSSvrProfiles=_OrinocoRADIUSSvrProfiles_ObjectIdentity((1,3,6,1,4,1,11898,2,1,6,10))
_OriRADIUSSvrTable_Object=MibTable
oriRADIUSSvrTable=_OriRADIUSSvrTable_Object((1,3,6,1,4,1,11898,2,1,6,10,1))
if mibBuilder.loadTexts:oriRADIUSSvrTable.setStatus(_A)
_OriRADIUSSvrTableEntry_Object=MibTableRow
oriRADIUSSvrTableEntry=_OriRADIUSSvrTableEntry_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1))
oriRADIUSSvrTableEntry.setIndexNames((0,_E,_AS),(0,_E,_AT))
if mibBuilder.loadTexts:oriRADIUSSvrTableEntry.setStatus(_A)
_OriRADIUSSvrTableProfileIndex_Type=Integer32
_OriRADIUSSvrTableProfileIndex_Object=MibTableColumn
oriRADIUSSvrTableProfileIndex=_OriRADIUSSvrTableProfileIndex_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,1),_OriRADIUSSvrTableProfileIndex_Type())
oriRADIUSSvrTableProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSSvrTableProfileIndex.setStatus(_A)
class _OriRADIUSSvrTablePrimaryOrSecondaryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_OriRADIUSSvrTablePrimaryOrSecondaryIndex_Type.__name__=_D
_OriRADIUSSvrTablePrimaryOrSecondaryIndex_Object=MibTableColumn
oriRADIUSSvrTablePrimaryOrSecondaryIndex=_OriRADIUSSvrTablePrimaryOrSecondaryIndex_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,2),_OriRADIUSSvrTablePrimaryOrSecondaryIndex_Type())
oriRADIUSSvrTablePrimaryOrSecondaryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSSvrTablePrimaryOrSecondaryIndex.setStatus(_A)
_OriRADIUSSvrTableProfileName_Type=DisplayString
_OriRADIUSSvrTableProfileName_Object=MibTableColumn
oriRADIUSSvrTableProfileName=_OriRADIUSSvrTableProfileName_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,3),_OriRADIUSSvrTableProfileName_Type())
oriRADIUSSvrTableProfileName.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableProfileName.setStatus(_A)
class _OriRADIUSSvrTableAddressingFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_OriRADIUSSvrTableAddressingFormat_Type.__name__=_D
_OriRADIUSSvrTableAddressingFormat_Object=MibTableColumn
oriRADIUSSvrTableAddressingFormat=_OriRADIUSSvrTableAddressingFormat_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,4),_OriRADIUSSvrTableAddressingFormat_Type())
oriRADIUSSvrTableAddressingFormat.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableAddressingFormat.setStatus(_A)
_OriRADIUSSvrTableNameOrIPAddress_Type=DisplayString
_OriRADIUSSvrTableNameOrIPAddress_Object=MibTableColumn
oriRADIUSSvrTableNameOrIPAddress=_OriRADIUSSvrTableNameOrIPAddress_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,5),_OriRADIUSSvrTableNameOrIPAddress_Type())
oriRADIUSSvrTableNameOrIPAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableNameOrIPAddress.setStatus(_A)
class _OriRADIUSSvrTableDestPort_Type(Integer32):defaultValue=1812
_OriRADIUSSvrTableDestPort_Type.__name__=_D
_OriRADIUSSvrTableDestPort_Object=MibTableColumn
oriRADIUSSvrTableDestPort=_OriRADIUSSvrTableDestPort_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,6),_OriRADIUSSvrTableDestPort_Type())
oriRADIUSSvrTableDestPort.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableDestPort.setStatus(_A)
_OriRADIUSSvrTableSharedSecret_Type=DisplayString
_OriRADIUSSvrTableSharedSecret_Object=MibTableColumn
oriRADIUSSvrTableSharedSecret=_OriRADIUSSvrTableSharedSecret_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,7),_OriRADIUSSvrTableSharedSecret_Type())
oriRADIUSSvrTableSharedSecret.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableSharedSecret.setStatus(_A)
class _OriRADIUSSvrTableResponseTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_OriRADIUSSvrTableResponseTime_Type.__name__=_D
_OriRADIUSSvrTableResponseTime_Object=MibTableColumn
oriRADIUSSvrTableResponseTime=_OriRADIUSSvrTableResponseTime_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,8),_OriRADIUSSvrTableResponseTime_Type())
oriRADIUSSvrTableResponseTime.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableResponseTime.setStatus(_A)
class _OriRADIUSSvrTableMaximumRetransmission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_OriRADIUSSvrTableMaximumRetransmission_Type.__name__=_D
_OriRADIUSSvrTableMaximumRetransmission_Object=MibTableColumn
oriRADIUSSvrTableMaximumRetransmission=_OriRADIUSSvrTableMaximumRetransmission_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,9),_OriRADIUSSvrTableMaximumRetransmission_Type())
oriRADIUSSvrTableMaximumRetransmission.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableMaximumRetransmission.setStatus(_A)
_OriRADIUSSvrTableVLANID_Type=VlanId
_OriRADIUSSvrTableVLANID_Object=MibTableColumn
oriRADIUSSvrTableVLANID=_OriRADIUSSvrTableVLANID_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,10),_OriRADIUSSvrTableVLANID_Type())
oriRADIUSSvrTableVLANID.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableVLANID.setStatus(_A)
class _OriRADIUSSvrTableMACAddressFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AO,1),(_AP,2),(_AQ,3),(_AR,4)))
_OriRADIUSSvrTableMACAddressFormat_Type.__name__=_D
_OriRADIUSSvrTableMACAddressFormat_Object=MibTableColumn
oriRADIUSSvrTableMACAddressFormat=_OriRADIUSSvrTableMACAddressFormat_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,11),_OriRADIUSSvrTableMACAddressFormat_Type())
oriRADIUSSvrTableMACAddressFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSSvrTableMACAddressFormat.setStatus(_A)
class _OriRADIUSSvrTableAuthorizationLifeTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(900,43200))
_OriRADIUSSvrTableAuthorizationLifeTime_Type.__name__=_D
_OriRADIUSSvrTableAuthorizationLifeTime_Object=MibTableColumn
oriRADIUSSvrTableAuthorizationLifeTime=_OriRADIUSSvrTableAuthorizationLifeTime_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,12),_OriRADIUSSvrTableAuthorizationLifeTime_Type())
oriRADIUSSvrTableAuthorizationLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSSvrTableAuthorizationLifeTime.setStatus(_A)
class _OriRADIUSSvrTableAccountingInactivityTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_OriRADIUSSvrTableAccountingInactivityTimer_Type.__name__=_D
_OriRADIUSSvrTableAccountingInactivityTimer_Object=MibTableColumn
oriRADIUSSvrTableAccountingInactivityTimer=_OriRADIUSSvrTableAccountingInactivityTimer_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,13),_OriRADIUSSvrTableAccountingInactivityTimer_Type())
oriRADIUSSvrTableAccountingInactivityTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSSvrTableAccountingInactivityTimer.setStatus(_A)
class _OriRADIUSSvrTableAccountingUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,10080))
_OriRADIUSSvrTableAccountingUpdateInterval_Type.__name__=_D
_OriRADIUSSvrTableAccountingUpdateInterval_Object=MibTableColumn
oriRADIUSSvrTableAccountingUpdateInterval=_OriRADIUSSvrTableAccountingUpdateInterval_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,14),_OriRADIUSSvrTableAccountingUpdateInterval_Type())
oriRADIUSSvrTableAccountingUpdateInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADIUSSvrTableAccountingUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:oriRADIUSSvrTableAccountingUpdateInterval.setUnits('minutes')
_OriRADIUSSvrTableRowStatus_Type=RowStatus
_OriRADIUSSvrTableRowStatus_Object=MibTableColumn
oriRADIUSSvrTableRowStatus=_OriRADIUSSvrTableRowStatus_Object((1,3,6,1,4,1,11898,2,1,6,10,1,1,15),_OriRADIUSSvrTableRowStatus_Type())
oriRADIUSSvrTableRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRADIUSSvrTableRowStatus.setStatus(_A)
_OriRADIUSClientInvalidSvrAddress_Type=Counter32
_OriRADIUSClientInvalidSvrAddress_Object=MibScalar
oriRADIUSClientInvalidSvrAddress=_OriRADIUSClientInvalidSvrAddress_Object((1,3,6,1,4,1,11898,2,1,6,10,2),_OriRADIUSClientInvalidSvrAddress_Type())
oriRADIUSClientInvalidSvrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSClientInvalidSvrAddress.setStatus(_A)
_OriRADIUSAuthClientStatTable_Object=MibTable
oriRADIUSAuthClientStatTable=_OriRADIUSAuthClientStatTable_Object((1,3,6,1,4,1,11898,2,1,6,10,3))
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTable.setStatus(_A)
_OriRADIUSAuthClientStatTableEntry_Object=MibTableRow
oriRADIUSAuthClientStatTableEntry=_OriRADIUSAuthClientStatTableEntry_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1))
oriRADIUSAuthClientStatTableEntry.setIndexNames((0,_E,_AU),(0,_E,_AV))
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableEntry.setStatus(_A)
_OriRADIUSAuthClientStatTableIndex_Type=Integer32
_OriRADIUSAuthClientStatTableIndex_Object=MibTableColumn
oriRADIUSAuthClientStatTableIndex=_OriRADIUSAuthClientStatTableIndex_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,1),_OriRADIUSAuthClientStatTableIndex_Type())
oriRADIUSAuthClientStatTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableIndex.setStatus(_A)
class _OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Type.__name__=_D
_OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Object=MibTableColumn
oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex=_OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,2),_OriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex_Type())
oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex.setStatus(_A)
_OriRADIUSAuthClientStatTableAccessRequests_Type=Counter32
_OriRADIUSAuthClientStatTableAccessRequests_Object=MibTableColumn
oriRADIUSAuthClientStatTableAccessRequests=_OriRADIUSAuthClientStatTableAccessRequests_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,3),_OriRADIUSAuthClientStatTableAccessRequests_Type())
oriRADIUSAuthClientStatTableAccessRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableAccessRequests.setStatus(_A)
_OriRADIUSAuthClientStatTableAccessRetransmissions_Type=Counter32
_OriRADIUSAuthClientStatTableAccessRetransmissions_Object=MibTableColumn
oriRADIUSAuthClientStatTableAccessRetransmissions=_OriRADIUSAuthClientStatTableAccessRetransmissions_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,4),_OriRADIUSAuthClientStatTableAccessRetransmissions_Type())
oriRADIUSAuthClientStatTableAccessRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableAccessRetransmissions.setStatus(_A)
_OriRADIUSAuthClientStatTableAccessAccepts_Type=Counter32
_OriRADIUSAuthClientStatTableAccessAccepts_Object=MibTableColumn
oriRADIUSAuthClientStatTableAccessAccepts=_OriRADIUSAuthClientStatTableAccessAccepts_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,5),_OriRADIUSAuthClientStatTableAccessAccepts_Type())
oriRADIUSAuthClientStatTableAccessAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableAccessAccepts.setStatus(_A)
_OriRADIUSAuthClientStatTableAccessChallenges_Type=Counter32
_OriRADIUSAuthClientStatTableAccessChallenges_Object=MibTableColumn
oriRADIUSAuthClientStatTableAccessChallenges=_OriRADIUSAuthClientStatTableAccessChallenges_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,6),_OriRADIUSAuthClientStatTableAccessChallenges_Type())
oriRADIUSAuthClientStatTableAccessChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableAccessChallenges.setStatus(_A)
_OriRADIUSAuthClientStatTableAccessRejects_Type=Counter32
_OriRADIUSAuthClientStatTableAccessRejects_Object=MibTableColumn
oriRADIUSAuthClientStatTableAccessRejects=_OriRADIUSAuthClientStatTableAccessRejects_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,7),_OriRADIUSAuthClientStatTableAccessRejects_Type())
oriRADIUSAuthClientStatTableAccessRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableAccessRejects.setStatus(_A)
_OriRADIUSAuthClientStatTableMalformedAccessResponses_Type=Counter32
_OriRADIUSAuthClientStatTableMalformedAccessResponses_Object=MibTableColumn
oriRADIUSAuthClientStatTableMalformedAccessResponses=_OriRADIUSAuthClientStatTableMalformedAccessResponses_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,8),_OriRADIUSAuthClientStatTableMalformedAccessResponses_Type())
oriRADIUSAuthClientStatTableMalformedAccessResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableMalformedAccessResponses.setStatus(_A)
_OriRADIUSAuthClientStatTableBadAuthenticators_Type=Counter32
_OriRADIUSAuthClientStatTableBadAuthenticators_Object=MibTableColumn
oriRADIUSAuthClientStatTableBadAuthenticators=_OriRADIUSAuthClientStatTableBadAuthenticators_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,9),_OriRADIUSAuthClientStatTableBadAuthenticators_Type())
oriRADIUSAuthClientStatTableBadAuthenticators.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableBadAuthenticators.setStatus(_A)
_OriRADIUSAuthClientStatTableTimeouts_Type=Counter32
_OriRADIUSAuthClientStatTableTimeouts_Object=MibTableColumn
oriRADIUSAuthClientStatTableTimeouts=_OriRADIUSAuthClientStatTableTimeouts_Object((1,3,6,1,4,1,11898,2,1,6,10,3,1,10),_OriRADIUSAuthClientStatTableTimeouts_Type())
oriRADIUSAuthClientStatTableTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAuthClientStatTableTimeouts.setStatus(_A)
_OriRADIUSAcctClientStatTable_Object=MibTable
oriRADIUSAcctClientStatTable=_OriRADIUSAcctClientStatTable_Object((1,3,6,1,4,1,11898,2,1,6,10,4))
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTable.setStatus(_A)
_OriRADIUSAcctClientStatTableEntry_Object=MibTableRow
oriRADIUSAcctClientStatTableEntry=_OriRADIUSAcctClientStatTableEntry_Object((1,3,6,1,4,1,11898,2,1,6,10,4,1))
oriRADIUSAcctClientStatTableEntry.setIndexNames((0,_E,_AW),(0,_E,_AX))
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTableEntry.setStatus(_A)
_OriRADIUSAcctClientStatTableIndex_Type=Integer32
_OriRADIUSAcctClientStatTableIndex_Object=MibTableColumn
oriRADIUSAcctClientStatTableIndex=_OriRADIUSAcctClientStatTableIndex_Object((1,3,6,1,4,1,11898,2,1,6,10,4,1,1),_OriRADIUSAcctClientStatTableIndex_Type())
oriRADIUSAcctClientStatTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTableIndex.setStatus(_A)
class _OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Type.__name__=_D
_OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Object=MibTableColumn
oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex=_OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Object((1,3,6,1,4,1,11898,2,1,6,10,4,1,2),_OriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex_Type())
oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex.setStatus(_A)
_OriRADIUSAcctClientStatTableAccountingRequests_Type=Counter32
_OriRADIUSAcctClientStatTableAccountingRequests_Object=MibTableColumn
oriRADIUSAcctClientStatTableAccountingRequests=_OriRADIUSAcctClientStatTableAccountingRequests_Object((1,3,6,1,4,1,11898,2,1,6,10,4,1,3),_OriRADIUSAcctClientStatTableAccountingRequests_Type())
oriRADIUSAcctClientStatTableAccountingRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTableAccountingRequests.setStatus(_A)
_OriRADIUSAcctClientStatTableAccountingRetransmissions_Type=Counter32
_OriRADIUSAcctClientStatTableAccountingRetransmissions_Object=MibTableColumn
oriRADIUSAcctClientStatTableAccountingRetransmissions=_OriRADIUSAcctClientStatTableAccountingRetransmissions_Object((1,3,6,1,4,1,11898,2,1,6,10,4,1,4),_OriRADIUSAcctClientStatTableAccountingRetransmissions_Type())
oriRADIUSAcctClientStatTableAccountingRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTableAccountingRetransmissions.setStatus(_A)
_OriRADIUSAcctClientStatTableAccountingResponses_Type=Counter32
_OriRADIUSAcctClientStatTableAccountingResponses_Object=MibTableColumn
oriRADIUSAcctClientStatTableAccountingResponses=_OriRADIUSAcctClientStatTableAccountingResponses_Object((1,3,6,1,4,1,11898,2,1,6,10,4,1,5),_OriRADIUSAcctClientStatTableAccountingResponses_Type())
oriRADIUSAcctClientStatTableAccountingResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTableAccountingResponses.setStatus(_A)
_OriRADIUSAcctClientStatTableBadAuthenticators_Type=Counter32
_OriRADIUSAcctClientStatTableBadAuthenticators_Object=MibTableColumn
oriRADIUSAcctClientStatTableBadAuthenticators=_OriRADIUSAcctClientStatTableBadAuthenticators_Object((1,3,6,1,4,1,11898,2,1,6,10,4,1,6),_OriRADIUSAcctClientStatTableBadAuthenticators_Type())
oriRADIUSAcctClientStatTableBadAuthenticators.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADIUSAcctClientStatTableBadAuthenticators.setStatus(_A)
_OrinocoTelnet_ObjectIdentity=ObjectIdentity
orinocoTelnet=_OrinocoTelnet_ObjectIdentity((1,3,6,1,4,1,11898,2,1,7))
class _OriTelnetSessions_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_OriTelnetSessions_Type.__name__=_D
_OriTelnetSessions_Object=MibScalar
oriTelnetSessions=_OriTelnetSessions_Object((1,3,6,1,4,1,11898,2,1,7,1),_OriTelnetSessions_Type())
oriTelnetSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetSessions.setStatus(_H)
class _OriTelnetPassword_Type(DisplayString):defaultValue=OctetString(_U)
_OriTelnetPassword_Type.__name__=_O
_OriTelnetPassword_Object=MibScalar
oriTelnetPassword=_OriTelnetPassword_Object((1,3,6,1,4,1,11898,2,1,7,2),_OriTelnetPassword_Type())
oriTelnetPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetPassword.setStatus(_A)
class _OriTelnetPort_Type(Integer32):defaultValue=23
_OriTelnetPort_Type.__name__=_D
_OriTelnetPort_Object=MibScalar
oriTelnetPort=_OriTelnetPort_Object((1,3,6,1,4,1,11898,2,1,7,3),_OriTelnetPort_Type())
oriTelnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetPort.setStatus(_A)
class _OriTelnetLoginTimeout_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,300))
_OriTelnetLoginTimeout_Type.__name__=_D
_OriTelnetLoginTimeout_Object=MibScalar
oriTelnetLoginTimeout=_OriTelnetLoginTimeout_Object((1,3,6,1,4,1,11898,2,1,7,4),_OriTelnetLoginTimeout_Type())
oriTelnetLoginTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetLoginTimeout.setStatus(_A)
class _OriTelnetIdleTimeout_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,36000))
_OriTelnetIdleTimeout_Type.__name__=_D
_OriTelnetIdleTimeout_Object=MibScalar
oriTelnetIdleTimeout=_OriTelnetIdleTimeout_Object((1,3,6,1,4,1,11898,2,1,7,5),_OriTelnetIdleTimeout_Type())
oriTelnetIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetIdleTimeout.setStatus(_A)
_OriTelnetInterfaceBitmask_Type=InterfaceBitmask
_OriTelnetInterfaceBitmask_Object=MibScalar
oriTelnetInterfaceBitmask=_OriTelnetInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,7,6),_OriTelnetInterfaceBitmask_Type())
oriTelnetInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetInterfaceBitmask.setStatus(_A)
class _OriTelnetSSHStatus_Type(ObjStatus):defaultValue=2
_OriTelnetSSHStatus_Type.__name__=_J
_OriTelnetSSHStatus_Object=MibScalar
oriTelnetSSHStatus=_OriTelnetSSHStatus_Object((1,3,6,1,4,1,11898,2,1,7,7),_OriTelnetSSHStatus_Type())
oriTelnetSSHStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetSSHStatus.setStatus(_A)
class _OriTelnetSSHHostKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_L,2)))
_OriTelnetSSHHostKeyStatus_Type.__name__=_D
_OriTelnetSSHHostKeyStatus_Object=MibScalar
oriTelnetSSHHostKeyStatus=_OriTelnetSSHHostKeyStatus_Object((1,3,6,1,4,1,11898,2,1,7,8),_OriTelnetSSHHostKeyStatus_Type())
oriTelnetSSHHostKeyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetSSHHostKeyStatus.setStatus(_A)
_OriTelnetSSHFingerPrint_Type=DisplayString
_OriTelnetSSHFingerPrint_Object=MibScalar
oriTelnetSSHFingerPrint=_OriTelnetSSHFingerPrint_Object((1,3,6,1,4,1,11898,2,1,7,9),_OriTelnetSSHFingerPrint_Type())
oriTelnetSSHFingerPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTelnetSSHFingerPrint.setStatus(_A)
class _OriTelnetRADIUSAccessControl_Type(ObjStatus):defaultValue=2
_OriTelnetRADIUSAccessControl_Type.__name__=_J
_OriTelnetRADIUSAccessControl_Object=MibScalar
oriTelnetRADIUSAccessControl=_OriTelnetRADIUSAccessControl_Object((1,3,6,1,4,1,11898,2,1,7,10),_OriTelnetRADIUSAccessControl_Type())
oriTelnetRADIUSAccessControl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTelnetRADIUSAccessControl.setStatus(_A)
_OrinocoTFTP_ObjectIdentity=ObjectIdentity
orinocoTFTP=_OrinocoTFTP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,8))
class _OriTFTPServerIPAddress_Type(IpAddress):defaultHexValue='0a000002'
_OriTFTPServerIPAddress_Type.__name__=_x
_OriTFTPServerIPAddress_Object=MibScalar
oriTFTPServerIPAddress=_OriTFTPServerIPAddress_Object((1,3,6,1,4,1,11898,2,1,8,1),_OriTFTPServerIPAddress_Type())
oriTFTPServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPServerIPAddress.setStatus(_A)
class _OriTFTPFileName_Type(DisplayString):defaultValue=OctetString('Filename')
_OriTFTPFileName_Type.__name__=_O
_OriTFTPFileName_Object=MibScalar
oriTFTPFileName=_OriTFTPFileName_Object((1,3,6,1,4,1,11898,2,1,8,2),_OriTFTPFileName_Type())
oriTFTPFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPFileName.setStatus(_A)
class _OriTFTPFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('config',1),('image',2),('bootloader',3),('license',4),('certificate',5),('privatekey',6),('sshHostPublicKey',7),('sshHostPrivateKey',8),('cliBatchFile',9),('cliBatchLog',10),('templog',11),('eventlog',12)))
_OriTFTPFileType_Type.__name__=_D
_OriTFTPFileType_Object=MibScalar
oriTFTPFileType=_OriTFTPFileType_Object((1,3,6,1,4,1,11898,2,1,8,3),_OriTFTPFileType_Type())
oriTFTPFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPFileType.setStatus(_A)
class _OriTFTPOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('upload',1),('download',2),('downloadAndReboot',3)))
_OriTFTPOperation_Type.__name__=_D
_OriTFTPOperation_Object=MibScalar
oriTFTPOperation=_OriTFTPOperation_Object((1,3,6,1,4,1,11898,2,1,8,4),_OriTFTPOperation_Type())
oriTFTPOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPOperation.setStatus(_A)
class _OriTFTPFileMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ascii',1),('bin',2)))
_OriTFTPFileMode_Type.__name__=_D
_OriTFTPFileMode_Object=MibScalar
oriTFTPFileMode=_OriTFTPFileMode_Object((1,3,6,1,4,1,11898,2,1,8,5),_OriTFTPFileMode_Type())
oriTFTPFileMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPFileMode.setStatus(_A)
class _OriTFTPOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('inProgress',2),('successful',3),('failure',4)))
_OriTFTPOperationStatus_Type.__name__=_D
_OriTFTPOperationStatus_Object=MibScalar
oriTFTPOperationStatus=_OriTFTPOperationStatus_Object((1,3,6,1,4,1,11898,2,1,8,6),_OriTFTPOperationStatus_Type())
oriTFTPOperationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTFTPOperationStatus.setStatus(_A)
_OriTFTPAutoConfigStatus_Type=ObjStatus
_OriTFTPAutoConfigStatus_Object=MibScalar
oriTFTPAutoConfigStatus=_OriTFTPAutoConfigStatus_Object((1,3,6,1,4,1,11898,2,1,8,7),_OriTFTPAutoConfigStatus_Type())
oriTFTPAutoConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPAutoConfigStatus.setStatus(_A)
_OriTFTPAutoConfigFilename_Type=DisplayString
_OriTFTPAutoConfigFilename_Object=MibScalar
oriTFTPAutoConfigFilename=_OriTFTPAutoConfigFilename_Object((1,3,6,1,4,1,11898,2,1,8,8),_OriTFTPAutoConfigFilename_Type())
oriTFTPAutoConfigFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPAutoConfigFilename.setStatus(_A)
_OriTFTPAutoConfigServerIPAddress_Type=IpAddress
_OriTFTPAutoConfigServerIPAddress_Object=MibScalar
oriTFTPAutoConfigServerIPAddress=_OriTFTPAutoConfigServerIPAddress_Object((1,3,6,1,4,1,11898,2,1,8,9),_OriTFTPAutoConfigServerIPAddress_Type())
oriTFTPAutoConfigServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPAutoConfigServerIPAddress.setStatus(_A)
class _OriTFTPDowngrade_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('rel201',2)))
_OriTFTPDowngrade_Type.__name__=_D
_OriTFTPDowngrade_Object=MibScalar
oriTFTPDowngrade=_OriTFTPDowngrade_Object((1,3,6,1,4,1,11898,2,1,8,10),_OriTFTPDowngrade_Type())
oriTFTPDowngrade.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPDowngrade.setStatus(_A)
_OrinocoSerial_ObjectIdentity=ObjectIdentity
orinocoSerial=_OrinocoSerial_ObjectIdentity((1,3,6,1,4,1,11898,2,1,9))
class _OriSerialBaudRate_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('baud2400',1),('baud4800',2),('baud9600',3),('baud19200',4),('baud38400',5),('baud57600',6)))
_OriSerialBaudRate_Type.__name__=_D
_OriSerialBaudRate_Object=MibScalar
oriSerialBaudRate=_OriSerialBaudRate_Object((1,3,6,1,4,1,11898,2,1,9,1),_OriSerialBaudRate_Type())
oriSerialBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSerialBaudRate.setStatus(_A)
class _OriSerialDataBits_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,8))
_OriSerialDataBits_Type.__name__=_D
_OriSerialDataBits_Object=MibScalar
oriSerialDataBits=_OriSerialDataBits_Object((1,3,6,1,4,1,11898,2,1,9,2),_OriSerialDataBits_Type())
oriSerialDataBits.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSerialDataBits.setStatus(_A)
class _OriSerialParity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('even',1),('odd',2),(_Q,3),('mark',4),('space',5)))
_OriSerialParity_Type.__name__=_D
_OriSerialParity_Object=MibScalar
oriSerialParity=_OriSerialParity_Object((1,3,6,1,4,1,11898,2,1,9,3),_OriSerialParity_Type())
oriSerialParity.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSerialParity.setStatus(_A)
class _OriSerialStopBits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bit1',1),('bit1dot5',2),('bit2',3)))
_OriSerialStopBits_Type.__name__=_D
_OriSerialStopBits_Object=MibScalar
oriSerialStopBits=_OriSerialStopBits_Object((1,3,6,1,4,1,11898,2,1,9,4),_OriSerialStopBits_Type())
oriSerialStopBits.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSerialStopBits.setStatus(_A)
class _OriSerialFlowControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('xonxoff',1),(_Q,2)))
_OriSerialFlowControl_Type.__name__=_D
_OriSerialFlowControl_Object=MibScalar
oriSerialFlowControl=_OriSerialFlowControl_Object((1,3,6,1,4,1,11898,2,1,9,5),_OriSerialFlowControl_Type())
oriSerialFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSerialFlowControl.setStatus(_A)
_OrinocoIAPP_ObjectIdentity=ObjectIdentity
orinocoIAPP=_OrinocoIAPP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,10))
class _OriIAPPStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriIAPPStatus_Type.__name__=_D
_OriIAPPStatus_Object=MibScalar
oriIAPPStatus=_OriIAPPStatus_Object((1,3,6,1,4,1,11898,2,1,10,1),_OriIAPPStatus_Type())
oriIAPPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIAPPStatus.setStatus(_A)
class _OriIAPPPeriodicAnnounceInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(80,120,160,200)));namedValues=NamedValues(*(('eighty',80),('oneHundredTwenty',120),('oneHundredSixty',160),('twoHundred',200)))
_OriIAPPPeriodicAnnounceInterval_Type.__name__=_D
_OriIAPPPeriodicAnnounceInterval_Object=MibScalar
oriIAPPPeriodicAnnounceInterval=_OriIAPPPeriodicAnnounceInterval_Object((1,3,6,1,4,1,11898,2,1,10,2),_OriIAPPPeriodicAnnounceInterval_Type())
oriIAPPPeriodicAnnounceInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIAPPPeriodicAnnounceInterval.setStatus(_A)
_OriIAPPAnnounceResponseTime_Type=Integer32
_OriIAPPAnnounceResponseTime_Object=MibScalar
oriIAPPAnnounceResponseTime=_OriIAPPAnnounceResponseTime_Object((1,3,6,1,4,1,11898,2,1,10,3),_OriIAPPAnnounceResponseTime_Type())
oriIAPPAnnounceResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPAnnounceResponseTime.setStatus(_A)
class _OriIAPPHandoverTimeout_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(410,512,614,717,819)));namedValues=NamedValues(*(('fourHundredTen',410),('fiveHundredTwelve',512),('sixHundredFourteen',614),('sevenHundredSeventeen',717),('eightHundredNineteen',819)))
_OriIAPPHandoverTimeout_Type.__name__=_D
_OriIAPPHandoverTimeout_Object=MibScalar
oriIAPPHandoverTimeout=_OriIAPPHandoverTimeout_Object((1,3,6,1,4,1,11898,2,1,10,4),_OriIAPPHandoverTimeout_Type())
oriIAPPHandoverTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIAPPHandoverTimeout.setStatus(_A)
class _OriIAPPMaximumHandoverRetransmissions_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_OriIAPPMaximumHandoverRetransmissions_Type.__name__=_D
_OriIAPPMaximumHandoverRetransmissions_Object=MibScalar
oriIAPPMaximumHandoverRetransmissions=_OriIAPPMaximumHandoverRetransmissions_Object((1,3,6,1,4,1,11898,2,1,10,5),_OriIAPPMaximumHandoverRetransmissions_Type())
oriIAPPMaximumHandoverRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIAPPMaximumHandoverRetransmissions.setStatus(_A)
_OriIAPPAnnounceRequestSent_Type=Counter32
_OriIAPPAnnounceRequestSent_Object=MibScalar
oriIAPPAnnounceRequestSent=_OriIAPPAnnounceRequestSent_Object((1,3,6,1,4,1,11898,2,1,10,6),_OriIAPPAnnounceRequestSent_Type())
oriIAPPAnnounceRequestSent.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPAnnounceRequestSent.setStatus(_A)
_OriIAPPAnnounceRequestReceived_Type=Counter32
_OriIAPPAnnounceRequestReceived_Object=MibScalar
oriIAPPAnnounceRequestReceived=_OriIAPPAnnounceRequestReceived_Object((1,3,6,1,4,1,11898,2,1,10,7),_OriIAPPAnnounceRequestReceived_Type())
oriIAPPAnnounceRequestReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPAnnounceRequestReceived.setStatus(_A)
_OriIAPPAnnounceResponseSent_Type=Counter32
_OriIAPPAnnounceResponseSent_Object=MibScalar
oriIAPPAnnounceResponseSent=_OriIAPPAnnounceResponseSent_Object((1,3,6,1,4,1,11898,2,1,10,8),_OriIAPPAnnounceResponseSent_Type())
oriIAPPAnnounceResponseSent.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPAnnounceResponseSent.setStatus(_A)
_OriIAPPAnnounceResponseReceived_Type=Counter32
_OriIAPPAnnounceResponseReceived_Object=MibScalar
oriIAPPAnnounceResponseReceived=_OriIAPPAnnounceResponseReceived_Object((1,3,6,1,4,1,11898,2,1,10,9),_OriIAPPAnnounceResponseReceived_Type())
oriIAPPAnnounceResponseReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPAnnounceResponseReceived.setStatus(_A)
_OriIAPPHandoverRequestSent_Type=Counter32
_OriIAPPHandoverRequestSent_Object=MibScalar
oriIAPPHandoverRequestSent=_OriIAPPHandoverRequestSent_Object((1,3,6,1,4,1,11898,2,1,10,10),_OriIAPPHandoverRequestSent_Type())
oriIAPPHandoverRequestSent.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPHandoverRequestSent.setStatus(_A)
_OriIAPPHandoverRequestReceived_Type=Counter32
_OriIAPPHandoverRequestReceived_Object=MibScalar
oriIAPPHandoverRequestReceived=_OriIAPPHandoverRequestReceived_Object((1,3,6,1,4,1,11898,2,1,10,11),_OriIAPPHandoverRequestReceived_Type())
oriIAPPHandoverRequestReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPHandoverRequestReceived.setStatus(_A)
_OriIAPPHandoverRequestRetransmissions_Type=Counter32
_OriIAPPHandoverRequestRetransmissions_Object=MibScalar
oriIAPPHandoverRequestRetransmissions=_OriIAPPHandoverRequestRetransmissions_Object((1,3,6,1,4,1,11898,2,1,10,12),_OriIAPPHandoverRequestRetransmissions_Type())
oriIAPPHandoverRequestRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPHandoverRequestRetransmissions.setStatus(_A)
_OriIAPPHandoverResponseSent_Type=Counter32
_OriIAPPHandoverResponseSent_Object=MibScalar
oriIAPPHandoverResponseSent=_OriIAPPHandoverResponseSent_Object((1,3,6,1,4,1,11898,2,1,10,13),_OriIAPPHandoverResponseSent_Type())
oriIAPPHandoverResponseSent.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPHandoverResponseSent.setStatus(_A)
_OriIAPPHandoverResponseReceived_Type=Counter32
_OriIAPPHandoverResponseReceived_Object=MibScalar
oriIAPPHandoverResponseReceived=_OriIAPPHandoverResponseReceived_Object((1,3,6,1,4,1,11898,2,1,10,14),_OriIAPPHandoverResponseReceived_Type())
oriIAPPHandoverResponseReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPHandoverResponseReceived.setStatus(_A)
_OriIAPPPDUsDropped_Type=Counter32
_OriIAPPPDUsDropped_Object=MibScalar
oriIAPPPDUsDropped=_OriIAPPPDUsDropped_Object((1,3,6,1,4,1,11898,2,1,10,15),_OriIAPPPDUsDropped_Type())
oriIAPPPDUsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPPDUsDropped.setStatus(_A)
_OriIAPPRoamingClients_Type=Counter32
_OriIAPPRoamingClients_Object=MibScalar
oriIAPPRoamingClients=_OriIAPPRoamingClients_Object((1,3,6,1,4,1,11898,2,1,10,16),_OriIAPPRoamingClients_Type())
oriIAPPRoamingClients.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPRoamingClients.setStatus(_A)
_OriIAPPMACIPTable_Object=MibTable
oriIAPPMACIPTable=_OriIAPPMACIPTable_Object((1,3,6,1,4,1,11898,2,1,10,21))
if mibBuilder.loadTexts:oriIAPPMACIPTable.setStatus(_A)
_OriIAPPMACIPTableEntry_Object=MibTableRow
oriIAPPMACIPTableEntry=_OriIAPPMACIPTableEntry_Object((1,3,6,1,4,1,11898,2,1,10,21,1))
oriIAPPMACIPTableEntry.setIndexNames((0,_E,_AY))
if mibBuilder.loadTexts:oriIAPPMACIPTableEntry.setStatus(_A)
_OriIAPPMACIPTableIndex_Type=Integer32
_OriIAPPMACIPTableIndex_Object=MibTableColumn
oriIAPPMACIPTableIndex=_OriIAPPMACIPTableIndex_Object((1,3,6,1,4,1,11898,2,1,10,21,1,1),_OriIAPPMACIPTableIndex_Type())
oriIAPPMACIPTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPMACIPTableIndex.setStatus(_A)
_OriIAPPMACIPTableSystemName_Type=DisplayString
_OriIAPPMACIPTableSystemName_Object=MibTableColumn
oriIAPPMACIPTableSystemName=_OriIAPPMACIPTableSystemName_Object((1,3,6,1,4,1,11898,2,1,10,21,1,2),_OriIAPPMACIPTableSystemName_Type())
oriIAPPMACIPTableSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPMACIPTableSystemName.setStatus(_A)
_OriIAPPMACIPTableIPAddress_Type=IpAddress
_OriIAPPMACIPTableIPAddress_Object=MibTableColumn
oriIAPPMACIPTableIPAddress=_OriIAPPMACIPTableIPAddress_Object((1,3,6,1,4,1,11898,2,1,10,21,1,3),_OriIAPPMACIPTableIPAddress_Type())
oriIAPPMACIPTableIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPMACIPTableIPAddress.setStatus(_A)
_OriIAPPMACIPTableBSSID_Type=PhysAddress
_OriIAPPMACIPTableBSSID_Object=MibTableColumn
oriIAPPMACIPTableBSSID=_OriIAPPMACIPTableBSSID_Object((1,3,6,1,4,1,11898,2,1,10,21,1,4),_OriIAPPMACIPTableBSSID_Type())
oriIAPPMACIPTableBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPMACIPTableBSSID.setStatus(_A)
_OriIAPPMACIPTableESSID_Type=DisplayString
_OriIAPPMACIPTableESSID_Object=MibTableColumn
oriIAPPMACIPTableESSID=_OriIAPPMACIPTableESSID_Object((1,3,6,1,4,1,11898,2,1,10,21,1,5),_OriIAPPMACIPTableESSID_Type())
oriIAPPMACIPTableESSID.setMaxAccess(_C)
if mibBuilder.loadTexts:oriIAPPMACIPTableESSID.setStatus(_A)
class _OriIAPPSendAnnounceRequestOnStart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriIAPPSendAnnounceRequestOnStart_Type.__name__=_D
_OriIAPPSendAnnounceRequestOnStart_Object=MibScalar
oriIAPPSendAnnounceRequestOnStart=_OriIAPPSendAnnounceRequestOnStart_Object((1,3,6,1,4,1,11898,2,1,10,22),_OriIAPPSendAnnounceRequestOnStart_Type())
oriIAPPSendAnnounceRequestOnStart.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIAPPSendAnnounceRequestOnStart.setStatus(_A)
_OrinocoLinkTest_ObjectIdentity=ObjectIdentity
orinocoLinkTest=_OrinocoLinkTest_ObjectIdentity((1,3,6,1,4,1,11898,2,1,11))
class _OriLinkTestTimeOut_Type(Integer32):defaultValue=300
_OriLinkTestTimeOut_Type.__name__=_D
_OriLinkTestTimeOut_Object=MibScalar
oriLinkTestTimeOut=_OriLinkTestTimeOut_Object((1,3,6,1,4,1,11898,2,1,11,1),_OriLinkTestTimeOut_Type())
oriLinkTestTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkTestTimeOut.setStatus(_A)
class _OriLinkTestInterval_Type(Integer32):defaultValue=200
_OriLinkTestInterval_Type.__name__=_D
_OriLinkTestInterval_Object=MibScalar
oriLinkTestInterval=_OriLinkTestInterval_Object((1,3,6,1,4,1,11898,2,1,11,3),_OriLinkTestInterval_Type())
oriLinkTestInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkTestInterval.setStatus(_A)
class _OriLinkTestExplore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tableTimedOut',1),('exploring',2),('exploreResultsAvailable',3)))
_OriLinkTestExplore_Type.__name__=_D
_OriLinkTestExplore_Object=MibScalar
oriLinkTestExplore=_OriLinkTestExplore_Object((1,3,6,1,4,1,11898,2,1,11,4),_OriLinkTestExplore_Type())
oriLinkTestExplore.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkTestExplore.setStatus(_A)
_OriLinkTestTable_Object=MibTable
oriLinkTestTable=_OriLinkTestTable_Object((1,3,6,1,4,1,11898,2,1,11,5))
if mibBuilder.loadTexts:oriLinkTestTable.setStatus(_A)
_OriLinkTestTableEntry_Object=MibTableRow
oriLinkTestTableEntry=_OriLinkTestTableEntry_Object((1,3,6,1,4,1,11898,2,1,11,5,1))
oriLinkTestTableEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:oriLinkTestTableEntry.setStatus(_A)
class _OriLinkTestTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_OriLinkTestTableIndex_Type.__name__=_D
_OriLinkTestTableIndex_Object=MibTableColumn
oriLinkTestTableIndex=_OriLinkTestTableIndex_Object((1,3,6,1,4,1,11898,2,1,11,5,1,1),_OriLinkTestTableIndex_Type())
oriLinkTestTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestTableIndex.setStatus(_A)
class _OriLinkTestInProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLinkTestInProgress',1),('linkTestIinProgress',2)))
_OriLinkTestInProgress_Type.__name__=_D
_OriLinkTestInProgress_Object=MibTableColumn
oriLinkTestInProgress=_OriLinkTestInProgress_Object((1,3,6,1,4,1,11898,2,1,11,5,1,2),_OriLinkTestInProgress_Type())
oriLinkTestInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkTestInProgress.setStatus(_A)
_OriLinkTestStationName_Type=DisplayString
_OriLinkTestStationName_Object=MibTableColumn
oriLinkTestStationName=_OriLinkTestStationName_Object((1,3,6,1,4,1,11898,2,1,11,5,1,3),_OriLinkTestStationName_Type())
oriLinkTestStationName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestStationName.setStatus(_A)
_OriLinkTestMACAddress_Type=PhysAddress
_OriLinkTestMACAddress_Object=MibTableColumn
oriLinkTestMACAddress=_OriLinkTestMACAddress_Object((1,3,6,1,4,1,11898,2,1,11,5,1,4),_OriLinkTestMACAddress_Type())
oriLinkTestMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestMACAddress.setStatus(_A)
_OriLinkTestStationProfile_Type=Integer32
_OriLinkTestStationProfile_Object=MibTableColumn
oriLinkTestStationProfile=_OriLinkTestStationProfile_Object((1,3,6,1,4,1,11898,2,1,11,5,1,5),_OriLinkTestStationProfile_Type())
oriLinkTestStationProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestStationProfile.setStatus(_A)
_OriLinkTestOurCurSignalLevel_Type=Integer32
_OriLinkTestOurCurSignalLevel_Object=MibTableColumn
oriLinkTestOurCurSignalLevel=_OriLinkTestOurCurSignalLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,6),_OriLinkTestOurCurSignalLevel_Type())
oriLinkTestOurCurSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurCurSignalLevel.setStatus(_A)
_OriLinkTestOurCurNoiseLevel_Type=Integer32
_OriLinkTestOurCurNoiseLevel_Object=MibTableColumn
oriLinkTestOurCurNoiseLevel=_OriLinkTestOurCurNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,7),_OriLinkTestOurCurNoiseLevel_Type())
oriLinkTestOurCurNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurCurNoiseLevel.setStatus(_A)
_OriLinkTestOurCurSNR_Type=Integer32
_OriLinkTestOurCurSNR_Object=MibTableColumn
oriLinkTestOurCurSNR=_OriLinkTestOurCurSNR_Object((1,3,6,1,4,1,11898,2,1,11,5,1,8),_OriLinkTestOurCurSNR_Type())
oriLinkTestOurCurSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurCurSNR.setStatus(_A)
_OriLinkTestOurMinSignalLevel_Type=Integer32
_OriLinkTestOurMinSignalLevel_Object=MibTableColumn
oriLinkTestOurMinSignalLevel=_OriLinkTestOurMinSignalLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,9),_OriLinkTestOurMinSignalLevel_Type())
oriLinkTestOurMinSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurMinSignalLevel.setStatus(_A)
_OriLinkTestOurMinNoiseLevel_Type=Integer32
_OriLinkTestOurMinNoiseLevel_Object=MibTableColumn
oriLinkTestOurMinNoiseLevel=_OriLinkTestOurMinNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,10),_OriLinkTestOurMinNoiseLevel_Type())
oriLinkTestOurMinNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurMinNoiseLevel.setStatus(_A)
_OriLinkTestOurMinSNR_Type=Integer32
_OriLinkTestOurMinSNR_Object=MibTableColumn
oriLinkTestOurMinSNR=_OriLinkTestOurMinSNR_Object((1,3,6,1,4,1,11898,2,1,11,5,1,11),_OriLinkTestOurMinSNR_Type())
oriLinkTestOurMinSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurMinSNR.setStatus(_A)
_OriLinkTestOurMaxSignalLevel_Type=Integer32
_OriLinkTestOurMaxSignalLevel_Object=MibTableColumn
oriLinkTestOurMaxSignalLevel=_OriLinkTestOurMaxSignalLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,12),_OriLinkTestOurMaxSignalLevel_Type())
oriLinkTestOurMaxSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurMaxSignalLevel.setStatus(_A)
_OriLinkTestOurMaxNoiseLevel_Type=Integer32
_OriLinkTestOurMaxNoiseLevel_Object=MibTableColumn
oriLinkTestOurMaxNoiseLevel=_OriLinkTestOurMaxNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,13),_OriLinkTestOurMaxNoiseLevel_Type())
oriLinkTestOurMaxNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurMaxNoiseLevel.setStatus(_A)
_OriLinkTestOurMaxSNR_Type=Integer32
_OriLinkTestOurMaxSNR_Object=MibTableColumn
oriLinkTestOurMaxSNR=_OriLinkTestOurMaxSNR_Object((1,3,6,1,4,1,11898,2,1,11,5,1,14),_OriLinkTestOurMaxSNR_Type())
oriLinkTestOurMaxSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurMaxSNR.setStatus(_A)
_OriLinkTestOurLowFrameCount_Type=Integer32
_OriLinkTestOurLowFrameCount_Object=MibTableColumn
oriLinkTestOurLowFrameCount=_OriLinkTestOurLowFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,15),_OriLinkTestOurLowFrameCount_Type())
oriLinkTestOurLowFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurLowFrameCount.setStatus(_A)
_OriLinkTestOurStandardFrameCount_Type=Integer32
_OriLinkTestOurStandardFrameCount_Object=MibTableColumn
oriLinkTestOurStandardFrameCount=_OriLinkTestOurStandardFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,16),_OriLinkTestOurStandardFrameCount_Type())
oriLinkTestOurStandardFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurStandardFrameCount.setStatus(_A)
_OriLinkTestOurMediumFrameCount_Type=Integer32
_OriLinkTestOurMediumFrameCount_Object=MibTableColumn
oriLinkTestOurMediumFrameCount=_OriLinkTestOurMediumFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,17),_OriLinkTestOurMediumFrameCount_Type())
oriLinkTestOurMediumFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurMediumFrameCount.setStatus(_A)
_OriLinkTestOurHighFrameCount_Type=Integer32
_OriLinkTestOurHighFrameCount_Object=MibTableColumn
oriLinkTestOurHighFrameCount=_OriLinkTestOurHighFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,18),_OriLinkTestOurHighFrameCount_Type())
oriLinkTestOurHighFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestOurHighFrameCount.setStatus(_A)
_OriLinkTestHisCurSignalLevel_Type=Integer32
_OriLinkTestHisCurSignalLevel_Object=MibTableColumn
oriLinkTestHisCurSignalLevel=_OriLinkTestHisCurSignalLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,19),_OriLinkTestHisCurSignalLevel_Type())
oriLinkTestHisCurSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisCurSignalLevel.setStatus(_A)
_OriLinkTestHisCurNoiseLevel_Type=Integer32
_OriLinkTestHisCurNoiseLevel_Object=MibTableColumn
oriLinkTestHisCurNoiseLevel=_OriLinkTestHisCurNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,20),_OriLinkTestHisCurNoiseLevel_Type())
oriLinkTestHisCurNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisCurNoiseLevel.setStatus(_A)
_OriLinkTestHisCurSNR_Type=Integer32
_OriLinkTestHisCurSNR_Object=MibTableColumn
oriLinkTestHisCurSNR=_OriLinkTestHisCurSNR_Object((1,3,6,1,4,1,11898,2,1,11,5,1,21),_OriLinkTestHisCurSNR_Type())
oriLinkTestHisCurSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisCurSNR.setStatus(_A)
_OriLinkTestHisMinSignalLevel_Type=Integer32
_OriLinkTestHisMinSignalLevel_Object=MibTableColumn
oriLinkTestHisMinSignalLevel=_OriLinkTestHisMinSignalLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,22),_OriLinkTestHisMinSignalLevel_Type())
oriLinkTestHisMinSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisMinSignalLevel.setStatus(_A)
_OriLinkTestHisMinNoiseLevel_Type=Integer32
_OriLinkTestHisMinNoiseLevel_Object=MibTableColumn
oriLinkTestHisMinNoiseLevel=_OriLinkTestHisMinNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,23),_OriLinkTestHisMinNoiseLevel_Type())
oriLinkTestHisMinNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisMinNoiseLevel.setStatus(_A)
_OriLinkTestHisMinSNR_Type=Integer32
_OriLinkTestHisMinSNR_Object=MibTableColumn
oriLinkTestHisMinSNR=_OriLinkTestHisMinSNR_Object((1,3,6,1,4,1,11898,2,1,11,5,1,24),_OriLinkTestHisMinSNR_Type())
oriLinkTestHisMinSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisMinSNR.setStatus(_A)
_OriLinkTestHisMaxSignalLevel_Type=Integer32
_OriLinkTestHisMaxSignalLevel_Object=MibTableColumn
oriLinkTestHisMaxSignalLevel=_OriLinkTestHisMaxSignalLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,25),_OriLinkTestHisMaxSignalLevel_Type())
oriLinkTestHisMaxSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisMaxSignalLevel.setStatus(_A)
_OriLinkTestHisMaxNoiseLevel_Type=Integer32
_OriLinkTestHisMaxNoiseLevel_Object=MibTableColumn
oriLinkTestHisMaxNoiseLevel=_OriLinkTestHisMaxNoiseLevel_Object((1,3,6,1,4,1,11898,2,1,11,5,1,26),_OriLinkTestHisMaxNoiseLevel_Type())
oriLinkTestHisMaxNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisMaxNoiseLevel.setStatus(_A)
_OriLinkTestHisMaxSNR_Type=Integer32
_OriLinkTestHisMaxSNR_Object=MibTableColumn
oriLinkTestHisMaxSNR=_OriLinkTestHisMaxSNR_Object((1,3,6,1,4,1,11898,2,1,11,5,1,27),_OriLinkTestHisMaxSNR_Type())
oriLinkTestHisMaxSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisMaxSNR.setStatus(_A)
_OriLinkTestHisLowFrameCount_Type=Integer32
_OriLinkTestHisLowFrameCount_Object=MibTableColumn
oriLinkTestHisLowFrameCount=_OriLinkTestHisLowFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,28),_OriLinkTestHisLowFrameCount_Type())
oriLinkTestHisLowFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisLowFrameCount.setStatus(_A)
_OriLinkTestHisStandardFrameCount_Type=Integer32
_OriLinkTestHisStandardFrameCount_Object=MibTableColumn
oriLinkTestHisStandardFrameCount=_OriLinkTestHisStandardFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,29),_OriLinkTestHisStandardFrameCount_Type())
oriLinkTestHisStandardFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisStandardFrameCount.setStatus(_A)
_OriLinkTestHisMediumFrameCount_Type=Integer32
_OriLinkTestHisMediumFrameCount_Object=MibTableColumn
oriLinkTestHisMediumFrameCount=_OriLinkTestHisMediumFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,30),_OriLinkTestHisMediumFrameCount_Type())
oriLinkTestHisMediumFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisMediumFrameCount.setStatus(_A)
_OriLinkTestHisHighFrameCount_Type=Integer32
_OriLinkTestHisHighFrameCount_Object=MibTableColumn
oriLinkTestHisHighFrameCount=_OriLinkTestHisHighFrameCount_Object((1,3,6,1,4,1,11898,2,1,11,5,1,31),_OriLinkTestHisHighFrameCount_Type())
oriLinkTestHisHighFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestHisHighFrameCount.setStatus(_A)
_OriLinkTestInterface_Type=DisplayString
_OriLinkTestInterface_Object=MibTableColumn
oriLinkTestInterface=_OriLinkTestInterface_Object((1,3,6,1,4,1,11898,2,1,11,5,1,32),_OriLinkTestInterface_Type())
oriLinkTestInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestInterface.setStatus(_A)
_OriLinkTestRadioType_Type=DisplayString
_OriLinkTestRadioType_Object=MibTableColumn
oriLinkTestRadioType=_OriLinkTestRadioType_Object((1,3,6,1,4,1,11898,2,1,11,5,1,33),_OriLinkTestRadioType_Type())
oriLinkTestRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestRadioType.setStatus(_A)
_OriLinkTestDataRateTable_Object=MibTable
oriLinkTestDataRateTable=_OriLinkTestDataRateTable_Object((1,3,6,1,4,1,11898,2,1,11,6))
if mibBuilder.loadTexts:oriLinkTestDataRateTable.setStatus(_A)
_OriLinkTestDataRateTableEntry_Object=MibTableRow
oriLinkTestDataRateTableEntry=_OriLinkTestDataRateTableEntry_Object((1,3,6,1,4,1,11898,2,1,11,6,1))
oriLinkTestDataRateTableEntry.setIndexNames((0,_E,_r),(0,_E,_AZ))
if mibBuilder.loadTexts:oriLinkTestDataRateTableEntry.setStatus(_A)
_OriLinkTestDataRateTableIndex_Type=Integer32
_OriLinkTestDataRateTableIndex_Object=MibTableColumn
oriLinkTestDataRateTableIndex=_OriLinkTestDataRateTableIndex_Object((1,3,6,1,4,1,11898,2,1,11,6,1,1),_OriLinkTestDataRateTableIndex_Type())
oriLinkTestDataRateTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestDataRateTableIndex.setStatus(_A)
_OriLinkTestDataRateTableRemoteCount_Type=Counter32
_OriLinkTestDataRateTableRemoteCount_Object=MibTableColumn
oriLinkTestDataRateTableRemoteCount=_OriLinkTestDataRateTableRemoteCount_Object((1,3,6,1,4,1,11898,2,1,11,6,1,2),_OriLinkTestDataRateTableRemoteCount_Type())
oriLinkTestDataRateTableRemoteCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestDataRateTableRemoteCount.setStatus(_A)
_OriLinkTestDataRateTableLocalCount_Type=Counter32
_OriLinkTestDataRateTableLocalCount_Object=MibTableColumn
oriLinkTestDataRateTableLocalCount=_OriLinkTestDataRateTableLocalCount_Object((1,3,6,1,4,1,11898,2,1,11,6,1,3),_OriLinkTestDataRateTableLocalCount_Type())
oriLinkTestDataRateTableLocalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkTestDataRateTableLocalCount.setStatus(_A)
_OrinocoLinkInt_ObjectIdentity=ObjectIdentity
orinocoLinkInt=_OrinocoLinkInt_ObjectIdentity((1,3,6,1,4,1,11898,2,1,12))
class _OriLinkIntStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriLinkIntStatus_Type.__name__=_D
_OriLinkIntStatus_Object=MibScalar
oriLinkIntStatus=_OriLinkIntStatus_Object((1,3,6,1,4,1,11898,2,1,12,1),_OriLinkIntStatus_Type())
oriLinkIntStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkIntStatus.setStatus(_A)
class _OriLinkIntPollInterval_Type(Integer32):defaultValue=500
_OriLinkIntPollInterval_Type.__name__=_D
_OriLinkIntPollInterval_Object=MibScalar
oriLinkIntPollInterval=_OriLinkIntPollInterval_Object((1,3,6,1,4,1,11898,2,1,12,2),_OriLinkIntPollInterval_Type())
oriLinkIntPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkIntPollInterval.setStatus(_A)
_OriLinkIntPollRetransmissions_Type=Integer32
_OriLinkIntPollRetransmissions_Object=MibScalar
oriLinkIntPollRetransmissions=_OriLinkIntPollRetransmissions_Object((1,3,6,1,4,1,11898,2,1,12,3),_OriLinkIntPollRetransmissions_Type())
oriLinkIntPollRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkIntPollRetransmissions.setStatus(_A)
_OriLinkIntTable_Object=MibTable
oriLinkIntTable=_OriLinkIntTable_Object((1,3,6,1,4,1,11898,2,1,12,4))
if mibBuilder.loadTexts:oriLinkIntTable.setStatus(_A)
_OriLinkIntTableEntry_Object=MibTableRow
oriLinkIntTableEntry=_OriLinkIntTableEntry_Object((1,3,6,1,4,1,11898,2,1,12,4,1))
oriLinkIntTableEntry.setIndexNames((0,_E,_Aa))
if mibBuilder.loadTexts:oriLinkIntTableEntry.setStatus(_A)
class _OriLinkIntTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_OriLinkIntTableIndex_Type.__name__=_D
_OriLinkIntTableIndex_Object=MibTableColumn
oriLinkIntTableIndex=_OriLinkIntTableIndex_Object((1,3,6,1,4,1,11898,2,1,12,4,1,1),_OriLinkIntTableIndex_Type())
oriLinkIntTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriLinkIntTableIndex.setStatus(_A)
_OriLinkIntTableTargetIPAddress_Type=IpAddress
_OriLinkIntTableTargetIPAddress_Object=MibTableColumn
oriLinkIntTableTargetIPAddress=_OriLinkIntTableTargetIPAddress_Object((1,3,6,1,4,1,11898,2,1,12,4,1,2),_OriLinkIntTableTargetIPAddress_Type())
oriLinkIntTableTargetIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkIntTableTargetIPAddress.setStatus(_A)
_OriLinkIntTableComment_Type=DisplayString
_OriLinkIntTableComment_Object=MibTableColumn
oriLinkIntTableComment=_OriLinkIntTableComment_Object((1,3,6,1,4,1,11898,2,1,12,4,1,3),_OriLinkIntTableComment_Type())
oriLinkIntTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkIntTableComment.setStatus(_A)
class _OriLinkIntTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3)))
_OriLinkIntTableEntryStatus_Type.__name__=_D
_OriLinkIntTableEntryStatus_Object=MibTableColumn
oriLinkIntTableEntryStatus=_OriLinkIntTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,12,4,1,4),_OriLinkIntTableEntryStatus_Type())
oriLinkIntTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriLinkIntTableEntryStatus.setStatus(_A)
_OrinocoUPSD_ObjectIdentity=ObjectIdentity
orinocoUPSD=_OrinocoUPSD_ObjectIdentity((1,3,6,1,4,1,11898,2,1,13))
class _OriUPSDGPRInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_OriUPSDGPRInterval_Type.__name__=_D
_OriUPSDGPRInterval_Object=MibScalar
oriUPSDGPRInterval=_OriUPSDGPRInterval_Object((1,3,6,1,4,1,11898,2,1,13,1),_OriUPSDGPRInterval_Type())
oriUPSDGPRInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriUPSDGPRInterval.setStatus(_A)
class _OriUPSDMaxActiveSU_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_OriUPSDMaxActiveSU_Type.__name__=_D
_OriUPSDMaxActiveSU_Object=MibScalar
oriUPSDMaxActiveSU=_OriUPSDMaxActiveSU_Object((1,3,6,1,4,1,11898,2,1,13,2),_OriUPSDMaxActiveSU_Type())
oriUPSDMaxActiveSU.setMaxAccess(_B)
if mibBuilder.loadTexts:oriUPSDMaxActiveSU.setStatus(_A)
class _OriUPSDE911Reserved_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_OriUPSDE911Reserved_Type.__name__=_D
_OriUPSDE911Reserved_Object=MibScalar
oriUPSDE911Reserved=_OriUPSDE911Reserved_Object((1,3,6,1,4,1,11898,2,1,13,3),_OriUPSDE911Reserved_Type())
oriUPSDE911Reserved.setMaxAccess(_B)
if mibBuilder.loadTexts:oriUPSDE911Reserved.setStatus(_A)
class _OriUPSDRoamingReserved_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_OriUPSDRoamingReserved_Type.__name__=_D
_OriUPSDRoamingReserved_Object=MibScalar
oriUPSDRoamingReserved=_OriUPSDRoamingReserved_Object((1,3,6,1,4,1,11898,2,1,13,4),_OriUPSDRoamingReserved_Type())
oriUPSDRoamingReserved.setMaxAccess(_B)
if mibBuilder.loadTexts:oriUPSDRoamingReserved.setStatus(_A)
_OrinocoQoS_ObjectIdentity=ObjectIdentity
orinocoQoS=_OrinocoQoS_ObjectIdentity((1,3,6,1,4,1,11898,2,1,14))
_OriQoSPolicyTable_Object=MibTable
oriQoSPolicyTable=_OriQoSPolicyTable_Object((1,3,6,1,4,1,11898,2,1,14,1))
if mibBuilder.loadTexts:oriQoSPolicyTable.setStatus(_A)
_OriQoSPolicyTableEntry_Object=MibTableRow
oriQoSPolicyTableEntry=_OriQoSPolicyTableEntry_Object((1,3,6,1,4,1,11898,2,1,14,1,1))
oriQoSPolicyTableEntry.setIndexNames((0,_E,_Ab),(0,_E,_Ac))
if mibBuilder.loadTexts:oriQoSPolicyTableEntry.setStatus(_A)
_OriQoSPolicyTableIndex_Type=Integer32
_OriQoSPolicyTableIndex_Object=MibTableColumn
oriQoSPolicyTableIndex=_OriQoSPolicyTableIndex_Object((1,3,6,1,4,1,11898,2,1,14,1,1,1),_OriQoSPolicyTableIndex_Type())
oriQoSPolicyTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriQoSPolicyTableIndex.setStatus(_A)
_OriQoSPolicyTableSecIndex_Type=Integer32
_OriQoSPolicyTableSecIndex_Object=MibTableColumn
oriQoSPolicyTableSecIndex=_OriQoSPolicyTableSecIndex_Object((1,3,6,1,4,1,11898,2,1,14,1,1,2),_OriQoSPolicyTableSecIndex_Type())
oriQoSPolicyTableSecIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriQoSPolicyTableSecIndex.setStatus(_A)
_OriQoSPolicyName_Type=DisplayString32
_OriQoSPolicyName_Object=MibTableColumn
oriQoSPolicyName=_OriQoSPolicyName_Object((1,3,6,1,4,1,11898,2,1,14,1,1,3),_OriQoSPolicyName_Type())
oriQoSPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSPolicyName.setStatus(_A)
class _OriQoSPolicyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inboundLayer2',1),('inboundLayer3',2),('outboundLayer2',3),('outboundLayer3',4),(_A0,5)))
_OriQoSPolicyType_Type.__name__=_D
_OriQoSPolicyType_Object=MibTableColumn
oriQoSPolicyType=_OriQoSPolicyType_Object((1,3,6,1,4,1,11898,2,1,14,1,1,4),_OriQoSPolicyType_Type())
oriQoSPolicyType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriQoSPolicyType.setStatus(_A)
_OriQoSPolicyPriorityMapping_Type=Integer32
_OriQoSPolicyPriorityMapping_Object=MibTableColumn
oriQoSPolicyPriorityMapping=_OriQoSPolicyPriorityMapping_Object((1,3,6,1,4,1,11898,2,1,14,1,1,5),_OriQoSPolicyPriorityMapping_Type())
oriQoSPolicyPriorityMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSPolicyPriorityMapping.setStatus(_A)
_OriQoSPolicyMarkingStatus_Type=ObjStatus
_OriQoSPolicyMarkingStatus_Object=MibTableColumn
oriQoSPolicyMarkingStatus=_OriQoSPolicyMarkingStatus_Object((1,3,6,1,4,1,11898,2,1,14,1,1,6),_OriQoSPolicyMarkingStatus_Type())
oriQoSPolicyMarkingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSPolicyMarkingStatus.setStatus(_A)
_OriQoSPolicyTableRowStatus_Type=RowStatus
_OriQoSPolicyTableRowStatus_Object=MibTableColumn
oriQoSPolicyTableRowStatus=_OriQoSPolicyTableRowStatus_Object((1,3,6,1,4,1,11898,2,1,14,1,1,7),_OriQoSPolicyTableRowStatus_Type())
oriQoSPolicyTableRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSPolicyTableRowStatus.setStatus(_A)
_OriQoSDot1DToDot1pMappingTable_Object=MibTable
oriQoSDot1DToDot1pMappingTable=_OriQoSDot1DToDot1pMappingTable_Object((1,3,6,1,4,1,11898,2,1,14,2))
if mibBuilder.loadTexts:oriQoSDot1DToDot1pMappingTable.setStatus(_A)
_OriQoSDot1DToDot1pMappingTableEntry_Object=MibTableRow
oriQoSDot1DToDot1pMappingTableEntry=_OriQoSDot1DToDot1pMappingTableEntry_Object((1,3,6,1,4,1,11898,2,1,14,2,1))
oriQoSDot1DToDot1pMappingTableEntry.setIndexNames((0,_E,_Ad),(0,_E,_Ae))
if mibBuilder.loadTexts:oriQoSDot1DToDot1pMappingTableEntry.setStatus(_A)
_OriQoSDot1DToDot1pMappingTableIndex_Type=Integer32
_OriQoSDot1DToDot1pMappingTableIndex_Object=MibTableColumn
oriQoSDot1DToDot1pMappingTableIndex=_OriQoSDot1DToDot1pMappingTableIndex_Object((1,3,6,1,4,1,11898,2,1,14,2,1,1),_OriQoSDot1DToDot1pMappingTableIndex_Type())
oriQoSDot1DToDot1pMappingTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriQoSDot1DToDot1pMappingTableIndex.setStatus(_A)
class _OriQoSDot1dPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OriQoSDot1dPriority_Type.__name__=_D
_OriQoSDot1dPriority_Object=MibTableColumn
oriQoSDot1dPriority=_OriQoSDot1dPriority_Object((1,3,6,1,4,1,11898,2,1,14,2,1,2),_OriQoSDot1dPriority_Type())
oriQoSDot1dPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:oriQoSDot1dPriority.setStatus(_A)
class _OriQoSDot1pPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OriQoSDot1pPriority_Type.__name__=_D
_OriQoSDot1pPriority_Object=MibTableColumn
oriQoSDot1pPriority=_OriQoSDot1pPriority_Object((1,3,6,1,4,1,11898,2,1,14,2,1,3),_OriQoSDot1pPriority_Type())
oriQoSDot1pPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSDot1pPriority.setStatus(_A)
_OriQoSDot1DToDot1pMappingTableRowStatus_Type=RowStatus
_OriQoSDot1DToDot1pMappingTableRowStatus_Object=MibTableColumn
oriQoSDot1DToDot1pMappingTableRowStatus=_OriQoSDot1DToDot1pMappingTableRowStatus_Object((1,3,6,1,4,1,11898,2,1,14,2,1,4),_OriQoSDot1DToDot1pMappingTableRowStatus_Type())
oriQoSDot1DToDot1pMappingTableRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSDot1DToDot1pMappingTableRowStatus.setStatus(_A)
_OriQoSDot1DToIPDSCPMappingTable_Object=MibTable
oriQoSDot1DToIPDSCPMappingTable=_OriQoSDot1DToIPDSCPMappingTable_Object((1,3,6,1,4,1,11898,2,1,14,3))
if mibBuilder.loadTexts:oriQoSDot1DToIPDSCPMappingTable.setStatus(_A)
_OriQoSDot1DToIPDSCPMappingTableEntry_Object=MibTableRow
oriQoSDot1DToIPDSCPMappingTableEntry=_OriQoSDot1DToIPDSCPMappingTableEntry_Object((1,3,6,1,4,1,11898,2,1,14,3,1))
oriQoSDot1DToIPDSCPMappingTableEntry.setIndexNames((0,_E,_Af),(0,_E,_Ag))
if mibBuilder.loadTexts:oriQoSDot1DToIPDSCPMappingTableEntry.setStatus(_A)
_OriQoSDot1DToIPDSCPMappingTableIndex_Type=Integer32
_OriQoSDot1DToIPDSCPMappingTableIndex_Object=MibTableColumn
oriQoSDot1DToIPDSCPMappingTableIndex=_OriQoSDot1DToIPDSCPMappingTableIndex_Object((1,3,6,1,4,1,11898,2,1,14,3,1,1),_OriQoSDot1DToIPDSCPMappingTableIndex_Type())
oriQoSDot1DToIPDSCPMappingTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriQoSDot1DToIPDSCPMappingTableIndex.setStatus(_A)
class _OriQoSDot1DToIPDSCPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OriQoSDot1DToIPDSCPPriority_Type.__name__=_D
_OriQoSDot1DToIPDSCPPriority_Object=MibTableColumn
oriQoSDot1DToIPDSCPPriority=_OriQoSDot1DToIPDSCPPriority_Object((1,3,6,1,4,1,11898,2,1,14,3,1,2),_OriQoSDot1DToIPDSCPPriority_Type())
oriQoSDot1DToIPDSCPPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:oriQoSDot1DToIPDSCPPriority.setStatus(_A)
class _OriQoSIPDSCPLowerLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62))
_OriQoSIPDSCPLowerLimit_Type.__name__=_D
_OriQoSIPDSCPLowerLimit_Object=MibTableColumn
oriQoSIPDSCPLowerLimit=_OriQoSIPDSCPLowerLimit_Object((1,3,6,1,4,1,11898,2,1,14,3,1,3),_OriQoSIPDSCPLowerLimit_Type())
oriQoSIPDSCPLowerLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSIPDSCPLowerLimit.setStatus(_A)
class _OriQoSIPDSCPUpperLimit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_OriQoSIPDSCPUpperLimit_Type.__name__=_D
_OriQoSIPDSCPUpperLimit_Object=MibTableColumn
oriQoSIPDSCPUpperLimit=_OriQoSIPDSCPUpperLimit_Object((1,3,6,1,4,1,11898,2,1,14,3,1,4),_OriQoSIPDSCPUpperLimit_Type())
oriQoSIPDSCPUpperLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSIPDSCPUpperLimit.setStatus(_A)
_OriQoSDot1DToIPDSCPMappingTableRowStatus_Type=RowStatus
_OriQoSDot1DToIPDSCPMappingTableRowStatus_Object=MibTableColumn
oriQoSDot1DToIPDSCPMappingTableRowStatus=_OriQoSDot1DToIPDSCPMappingTableRowStatus_Object((1,3,6,1,4,1,11898,2,1,14,3,1,5),_OriQoSDot1DToIPDSCPMappingTableRowStatus_Type())
oriQoSDot1DToIPDSCPMappingTableRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriQoSDot1DToIPDSCPMappingTableRowStatus.setStatus(_A)
_OrinocoDHCP_ObjectIdentity=ObjectIdentity
orinocoDHCP=_OrinocoDHCP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,15))
_OrinocoDHCPServer_ObjectIdentity=ObjectIdentity
orinocoDHCPServer=_OrinocoDHCPServer_ObjectIdentity((1,3,6,1,4,1,11898,2,1,15,1))
class _OriDHCPServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriDHCPServerStatus_Type.__name__=_D
_OriDHCPServerStatus_Object=MibScalar
oriDHCPServerStatus=_OriDHCPServerStatus_Object((1,3,6,1,4,1,11898,2,1,15,1,1),_OriDHCPServerStatus_Type())
oriDHCPServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerStatus.setStatus(_A)
_OriDHCPServerIPPoolTable_Object=MibTable
oriDHCPServerIPPoolTable=_OriDHCPServerIPPoolTable_Object((1,3,6,1,4,1,11898,2,1,15,1,2))
if mibBuilder.loadTexts:oriDHCPServerIPPoolTable.setStatus(_A)
_OriDHCPServerIPPoolTableEntry_Object=MibTableRow
oriDHCPServerIPPoolTableEntry=_OriDHCPServerIPPoolTableEntry_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1))
oriDHCPServerIPPoolTableEntry.setIndexNames((0,_E,_Ah))
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableEntry.setStatus(_A)
class _OriDHCPServerIPPoolTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OriDHCPServerIPPoolTableIndex_Type.__name__=_D
_OriDHCPServerIPPoolTableIndex_Object=MibTableColumn
oriDHCPServerIPPoolTableIndex=_OriDHCPServerIPPoolTableIndex_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,1),_OriDHCPServerIPPoolTableIndex_Type())
oriDHCPServerIPPoolTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableIndex.setStatus(_A)
_OriDHCPServerIPPoolTableStartIPAddress_Type=IpAddress
_OriDHCPServerIPPoolTableStartIPAddress_Object=MibTableColumn
oriDHCPServerIPPoolTableStartIPAddress=_OriDHCPServerIPPoolTableStartIPAddress_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,2),_OriDHCPServerIPPoolTableStartIPAddress_Type())
oriDHCPServerIPPoolTableStartIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableStartIPAddress.setStatus(_A)
_OriDHCPServerIPPoolTableEndIPAddress_Type=IpAddress
_OriDHCPServerIPPoolTableEndIPAddress_Object=MibTableColumn
oriDHCPServerIPPoolTableEndIPAddress=_OriDHCPServerIPPoolTableEndIPAddress_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,3),_OriDHCPServerIPPoolTableEndIPAddress_Type())
oriDHCPServerIPPoolTableEndIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableEndIPAddress.setStatus(_A)
_OriDHCPServerIPPoolTableWidth_Type=Integer32
_OriDHCPServerIPPoolTableWidth_Object=MibTableColumn
oriDHCPServerIPPoolTableWidth=_OriDHCPServerIPPoolTableWidth_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,4),_OriDHCPServerIPPoolTableWidth_Type())
oriDHCPServerIPPoolTableWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableWidth.setStatus(_A)
class _OriDHCPServerIPPoolTableDefaultLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,86400))
_OriDHCPServerIPPoolTableDefaultLeaseTime_Type.__name__=_D
_OriDHCPServerIPPoolTableDefaultLeaseTime_Object=MibTableColumn
oriDHCPServerIPPoolTableDefaultLeaseTime=_OriDHCPServerIPPoolTableDefaultLeaseTime_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,5),_OriDHCPServerIPPoolTableDefaultLeaseTime_Type())
oriDHCPServerIPPoolTableDefaultLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableDefaultLeaseTime.setStatus(_A)
class _OriDHCPServerIPPoolTableMaximumLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,86400))
_OriDHCPServerIPPoolTableMaximumLeaseTime_Type.__name__=_D
_OriDHCPServerIPPoolTableMaximumLeaseTime_Object=MibTableColumn
oriDHCPServerIPPoolTableMaximumLeaseTime=_OriDHCPServerIPPoolTableMaximumLeaseTime_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,6),_OriDHCPServerIPPoolTableMaximumLeaseTime_Type())
oriDHCPServerIPPoolTableMaximumLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableMaximumLeaseTime.setStatus(_A)
_OriDHCPServerIPPoolTableComment_Type=DisplayString
_OriDHCPServerIPPoolTableComment_Object=MibTableColumn
oriDHCPServerIPPoolTableComment=_OriDHCPServerIPPoolTableComment_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,7),_OriDHCPServerIPPoolTableComment_Type())
oriDHCPServerIPPoolTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableComment.setStatus(_A)
class _OriDHCPServerIPPoolTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriDHCPServerIPPoolTableEntryStatus_Type.__name__=_D
_OriDHCPServerIPPoolTableEntryStatus_Object=MibTableColumn
oriDHCPServerIPPoolTableEntryStatus=_OriDHCPServerIPPoolTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,15,1,2,1,8),_OriDHCPServerIPPoolTableEntryStatus_Type())
oriDHCPServerIPPoolTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerIPPoolTableEntryStatus.setStatus(_A)
_OriDHCPServerDefaultGatewayIPAddress_Type=IpAddress
_OriDHCPServerDefaultGatewayIPAddress_Object=MibScalar
oriDHCPServerDefaultGatewayIPAddress=_OriDHCPServerDefaultGatewayIPAddress_Object((1,3,6,1,4,1,11898,2,1,15,1,3),_OriDHCPServerDefaultGatewayIPAddress_Type())
oriDHCPServerDefaultGatewayIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerDefaultGatewayIPAddress.setStatus(_A)
_OriDHCPServerSubnetMask_Type=IpAddress
_OriDHCPServerSubnetMask_Object=MibScalar
oriDHCPServerSubnetMask=_OriDHCPServerSubnetMask_Object((1,3,6,1,4,1,11898,2,1,15,1,4),_OriDHCPServerSubnetMask_Type())
oriDHCPServerSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:oriDHCPServerSubnetMask.setStatus(_A)
_OriDHCPServerNumIPPoolTableEntries_Type=Integer32
_OriDHCPServerNumIPPoolTableEntries_Object=MibScalar
oriDHCPServerNumIPPoolTableEntries=_OriDHCPServerNumIPPoolTableEntries_Object((1,3,6,1,4,1,11898,2,1,15,1,5),_OriDHCPServerNumIPPoolTableEntries_Type())
oriDHCPServerNumIPPoolTableEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:oriDHCPServerNumIPPoolTableEntries.setStatus(_A)
_OriDHCPServerPrimaryDNSIPAddress_Type=IpAddress
_OriDHCPServerPrimaryDNSIPAddress_Object=MibScalar
oriDHCPServerPrimaryDNSIPAddress=_OriDHCPServerPrimaryDNSIPAddress_Object((1,3,6,1,4,1,11898,2,1,15,1,6),_OriDHCPServerPrimaryDNSIPAddress_Type())
oriDHCPServerPrimaryDNSIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerPrimaryDNSIPAddress.setStatus(_A)
_OriDHCPServerSecondaryDNSIPAddress_Type=IpAddress
_OriDHCPServerSecondaryDNSIPAddress_Object=MibScalar
oriDHCPServerSecondaryDNSIPAddress=_OriDHCPServerSecondaryDNSIPAddress_Object((1,3,6,1,4,1,11898,2,1,15,1,7),_OriDHCPServerSecondaryDNSIPAddress_Type())
oriDHCPServerSecondaryDNSIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPServerSecondaryDNSIPAddress.setStatus(_A)
_OrinocoDHCPClient_ObjectIdentity=ObjectIdentity
orinocoDHCPClient=_OrinocoDHCPClient_ObjectIdentity((1,3,6,1,4,1,11898,2,1,15,2))
_OriDHCPClientID_Type=DisplayString
_OriDHCPClientID_Object=MibScalar
oriDHCPClientID=_OriDHCPClientID_Object((1,3,6,1,4,1,11898,2,1,15,2,1),_OriDHCPClientID_Type())
oriDHCPClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPClientID.setStatus(_A)
_OriDHCPClientInterfaceBitmask_Type=InterfaceBitmask
_OriDHCPClientInterfaceBitmask_Object=MibScalar
oriDHCPClientInterfaceBitmask=_OriDHCPClientInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,15,2,2),_OriDHCPClientInterfaceBitmask_Type())
oriDHCPClientInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPClientInterfaceBitmask.setStatus(_A)
_OrinocoDHCPRelay_ObjectIdentity=ObjectIdentity
orinocoDHCPRelay=_OrinocoDHCPRelay_ObjectIdentity((1,3,6,1,4,1,11898,2,1,15,3))
class _OriDHCPRelayStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriDHCPRelayStatus_Type.__name__=_D
_OriDHCPRelayStatus_Object=MibScalar
oriDHCPRelayStatus=_OriDHCPRelayStatus_Object((1,3,6,1,4,1,11898,2,1,15,3,1),_OriDHCPRelayStatus_Type())
oriDHCPRelayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPRelayStatus.setStatus(_A)
_OriDHCPRelayDHCPServerTable_Object=MibTable
oriDHCPRelayDHCPServerTable=_OriDHCPRelayDHCPServerTable_Object((1,3,6,1,4,1,11898,2,1,15,3,2))
if mibBuilder.loadTexts:oriDHCPRelayDHCPServerTable.setStatus(_A)
_OriDHCPRelayDHCPServerTableEntry_Object=MibTableRow
oriDHCPRelayDHCPServerTableEntry=_OriDHCPRelayDHCPServerTableEntry_Object((1,3,6,1,4,1,11898,2,1,15,3,2,1))
oriDHCPRelayDHCPServerTableEntry.setIndexNames((0,_E,_Ai))
if mibBuilder.loadTexts:oriDHCPRelayDHCPServerTableEntry.setStatus(_A)
class _OriDHCPRelayDHCPServerTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_OriDHCPRelayDHCPServerTableIndex_Type.__name__=_D
_OriDHCPRelayDHCPServerTableIndex_Object=MibTableColumn
oriDHCPRelayDHCPServerTableIndex=_OriDHCPRelayDHCPServerTableIndex_Object((1,3,6,1,4,1,11898,2,1,15,3,2,1,1),_OriDHCPRelayDHCPServerTableIndex_Type())
oriDHCPRelayDHCPServerTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriDHCPRelayDHCPServerTableIndex.setStatus(_A)
_OriDHCPRelayDHCPServerTableIpAddress_Type=IpAddress
_OriDHCPRelayDHCPServerTableIpAddress_Object=MibTableColumn
oriDHCPRelayDHCPServerTableIpAddress=_OriDHCPRelayDHCPServerTableIpAddress_Object((1,3,6,1,4,1,11898,2,1,15,3,2,1,2),_OriDHCPRelayDHCPServerTableIpAddress_Type())
oriDHCPRelayDHCPServerTableIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPRelayDHCPServerTableIpAddress.setStatus(_A)
_OriDHCPRelayDHCPServerTableComment_Type=DisplayString
_OriDHCPRelayDHCPServerTableComment_Object=MibTableColumn
oriDHCPRelayDHCPServerTableComment=_OriDHCPRelayDHCPServerTableComment_Object((1,3,6,1,4,1,11898,2,1,15,3,2,1,3),_OriDHCPRelayDHCPServerTableComment_Type())
oriDHCPRelayDHCPServerTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPRelayDHCPServerTableComment.setStatus(_A)
class _OriDHCPRelayDHCPServerTableEntryStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriDHCPRelayDHCPServerTableEntryStatus_Type.__name__=_D
_OriDHCPRelayDHCPServerTableEntryStatus_Object=MibTableColumn
oriDHCPRelayDHCPServerTableEntryStatus=_OriDHCPRelayDHCPServerTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,15,3,2,1,4),_OriDHCPRelayDHCPServerTableEntryStatus_Type())
oriDHCPRelayDHCPServerTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDHCPRelayDHCPServerTableEntryStatus.setStatus(_A)
_OrinocoHTTP_ObjectIdentity=ObjectIdentity
orinocoHTTP=_OrinocoHTTP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,16))
_OriHTTPInterfaceBitmask_Type=InterfaceBitmask
_OriHTTPInterfaceBitmask_Object=MibScalar
oriHTTPInterfaceBitmask=_OriHTTPInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,16,1),_OriHTTPInterfaceBitmask_Type())
oriHTTPInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPInterfaceBitmask.setStatus(_A)
_OriHTTPPassword_Type=DisplayString
_OriHTTPPassword_Object=MibScalar
oriHTTPPassword=_OriHTTPPassword_Object((1,3,6,1,4,1,11898,2,1,16,2),_OriHTTPPassword_Type())
oriHTTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPPassword.setStatus(_A)
_OriHTTPPort_Type=Integer32
_OriHTTPPort_Object=MibScalar
oriHTTPPort=_OriHTTPPort_Object((1,3,6,1,4,1,11898,2,1,16,3),_OriHTTPPort_Type())
oriHTTPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPPort.setStatus(_A)
_OriHTTPWebSitenameTable_Object=MibTable
oriHTTPWebSitenameTable=_OriHTTPWebSitenameTable_Object((1,3,6,1,4,1,11898,2,1,16,4))
if mibBuilder.loadTexts:oriHTTPWebSitenameTable.setStatus(_A)
_OriHTTPWebSitenameTableEntry_Object=MibTableRow
oriHTTPWebSitenameTableEntry=_OriHTTPWebSitenameTableEntry_Object((1,3,6,1,4,1,11898,2,1,16,4,1))
oriHTTPWebSitenameTableEntry.setIndexNames((0,_E,_Aj))
if mibBuilder.loadTexts:oriHTTPWebSitenameTableEntry.setStatus(_A)
_OriHTTPWebSitenameTableIndex_Type=Integer32
_OriHTTPWebSitenameTableIndex_Object=MibTableColumn
oriHTTPWebSitenameTableIndex=_OriHTTPWebSitenameTableIndex_Object((1,3,6,1,4,1,11898,2,1,16,4,1,1),_OriHTTPWebSitenameTableIndex_Type())
oriHTTPWebSitenameTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriHTTPWebSitenameTableIndex.setStatus(_A)
_OriHTTPWebSiteFilename_Type=DisplayString
_OriHTTPWebSiteFilename_Object=MibTableColumn
oriHTTPWebSiteFilename=_OriHTTPWebSiteFilename_Object((1,3,6,1,4,1,11898,2,1,16,4,1,2),_OriHTTPWebSiteFilename_Type())
oriHTTPWebSiteFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:oriHTTPWebSiteFilename.setStatus(_A)
_OriHTTPWebSiteLanguage_Type=DisplayString
_OriHTTPWebSiteLanguage_Object=MibTableColumn
oriHTTPWebSiteLanguage=_OriHTTPWebSiteLanguage_Object((1,3,6,1,4,1,11898,2,1,16,4,1,3),_OriHTTPWebSiteLanguage_Type())
oriHTTPWebSiteLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:oriHTTPWebSiteLanguage.setStatus(_A)
_OriHTTPWebSiteDescription_Type=DisplayString
_OriHTTPWebSiteDescription_Object=MibTableColumn
oriHTTPWebSiteDescription=_OriHTTPWebSiteDescription_Object((1,3,6,1,4,1,11898,2,1,16,4,1,4),_OriHTTPWebSiteDescription_Type())
oriHTTPWebSiteDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:oriHTTPWebSiteDescription.setStatus(_A)
class _OriHTTPWebSitenameTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3)))
_OriHTTPWebSitenameTableStatus_Type.__name__=_D
_OriHTTPWebSitenameTableStatus_Object=MibTableColumn
oriHTTPWebSitenameTableStatus=_OriHTTPWebSitenameTableStatus_Object((1,3,6,1,4,1,11898,2,1,16,4,1,5),_OriHTTPWebSitenameTableStatus_Type())
oriHTTPWebSitenameTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPWebSitenameTableStatus.setStatus(_A)
_OriHTTPRefreshDelay_Type=Integer32
_OriHTTPRefreshDelay_Object=MibScalar
oriHTTPRefreshDelay=_OriHTTPRefreshDelay_Object((1,3,6,1,4,1,11898,2,1,16,5),_OriHTTPRefreshDelay_Type())
oriHTTPRefreshDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPRefreshDelay.setStatus(_A)
_OriHTTPHelpInformationLink_Type=DisplayString
_OriHTTPHelpInformationLink_Object=MibScalar
oriHTTPHelpInformationLink=_OriHTTPHelpInformationLink_Object((1,3,6,1,4,1,11898,2,1,16,6),_OriHTTPHelpInformationLink_Type())
oriHTTPHelpInformationLink.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPHelpInformationLink.setStatus(_A)
class _OriHTTPSSLStatus_Type(ObjStatus):defaultValue=2
_OriHTTPSSLStatus_Type.__name__=_J
_OriHTTPSSLStatus_Object=MibScalar
oriHTTPSSLStatus=_OriHTTPSSLStatus_Object((1,3,6,1,4,1,11898,2,1,16,7),_OriHTTPSSLStatus_Type())
oriHTTPSSLStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPSSLStatus.setStatus(_A)
_OriHTTPSSLPassphrase_Type=DisplayString
_OriHTTPSSLPassphrase_Object=MibScalar
oriHTTPSSLPassphrase=_OriHTTPSSLPassphrase_Object((1,3,6,1,4,1,11898,2,1,16,8),_OriHTTPSSLPassphrase_Type())
oriHTTPSSLPassphrase.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPSSLPassphrase.setStatus(_A)
class _OriHTTPSetupWizardStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriHTTPSetupWizardStatus_Type.__name__=_D
_OriHTTPSetupWizardStatus_Object=MibScalar
oriHTTPSetupWizardStatus=_OriHTTPSetupWizardStatus_Object((1,3,6,1,4,1,11898,2,1,16,9),_OriHTTPSetupWizardStatus_Type())
oriHTTPSetupWizardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPSetupWizardStatus.setStatus(_A)
class _OriHTTPRADIUSAccessControl_Type(ObjStatus):defaultValue=2
_OriHTTPRADIUSAccessControl_Type.__name__=_J
_OriHTTPRADIUSAccessControl_Object=MibScalar
oriHTTPRADIUSAccessControl=_OriHTTPRADIUSAccessControl_Object((1,3,6,1,4,1,11898,2,1,16,10),_OriHTTPRADIUSAccessControl_Type())
oriHTTPRADIUSAccessControl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriHTTPRADIUSAccessControl.setStatus(_A)
_OrinocoWDS_ObjectIdentity=ObjectIdentity
orinocoWDS=_OrinocoWDS_ObjectIdentity((1,3,6,1,4,1,11898,2,1,17))
_OriWDSSetupTable_Object=MibTable
oriWDSSetupTable=_OriWDSSetupTable_Object((1,3,6,1,4,1,11898,2,1,17,1))
if mibBuilder.loadTexts:oriWDSSetupTable.setStatus(_A)
_OriWDSSetupTableEntry_Object=MibTableRow
oriWDSSetupTableEntry=_OriWDSSetupTableEntry_Object((1,3,6,1,4,1,11898,2,1,17,1,1))
oriWDSSetupTableEntry.setIndexNames((0,_S,_T),(0,_E,_Ak))
if mibBuilder.loadTexts:oriWDSSetupTableEntry.setStatus(_A)
class _OriWDSSetupTablePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_OriWDSSetupTablePortIndex_Type.__name__=_D
_OriWDSSetupTablePortIndex_Object=MibTableColumn
oriWDSSetupTablePortIndex=_OriWDSSetupTablePortIndex_Object((1,3,6,1,4,1,11898,2,1,17,1,1,1),_OriWDSSetupTablePortIndex_Type())
oriWDSSetupTablePortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriWDSSetupTablePortIndex.setStatus(_A)
class _OriWDSSetupTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWDSSetupTableEntryStatus_Type.__name__=_D
_OriWDSSetupTableEntryStatus_Object=MibTableColumn
oriWDSSetupTableEntryStatus=_OriWDSSetupTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,17,1,1,2),_OriWDSSetupTableEntryStatus_Type())
oriWDSSetupTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWDSSetupTableEntryStatus.setStatus(_A)
_OriWDSSetupTablePartnerMACAddress_Type=PhysAddress
_OriWDSSetupTablePartnerMACAddress_Object=MibTableColumn
oriWDSSetupTablePartnerMACAddress=_OriWDSSetupTablePartnerMACAddress_Object((1,3,6,1,4,1,11898,2,1,17,1,1,3),_OriWDSSetupTablePartnerMACAddress_Type())
oriWDSSetupTablePartnerMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWDSSetupTablePartnerMACAddress.setStatus(_A)
_OriWDSSecurityTable_Object=MibTable
oriWDSSecurityTable=_OriWDSSecurityTable_Object((1,3,6,1,4,1,11898,2,1,17,2))
if mibBuilder.loadTexts:oriWDSSecurityTable.setStatus(_A)
_OriWDSSecurityTableEntry_Object=MibTableRow
oriWDSSecurityTableEntry=_OriWDSSecurityTableEntry_Object((1,3,6,1,4,1,11898,2,1,17,2,1))
oriWDSSecurityTableEntry.setIndexNames((0,_S,_T))
if mibBuilder.loadTexts:oriWDSSecurityTableEntry.setStatus(_A)
class _OriWDSSecurityTableSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6)));namedValues=NamedValues(*((_Q,1),(_Z,6)))
_OriWDSSecurityTableSecurityMode_Type.__name__=_D
_OriWDSSecurityTableSecurityMode_Object=MibTableColumn
oriWDSSecurityTableSecurityMode=_OriWDSSecurityTableSecurityMode_Object((1,3,6,1,4,1,11898,2,1,17,2,1,1),_OriWDSSecurityTableSecurityMode_Type())
oriWDSSecurityTableSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWDSSecurityTableSecurityMode.setStatus(_A)
_OriWDSSecurityTableEncryptionKey0_Type=WEPKeyType
_OriWDSSecurityTableEncryptionKey0_Object=MibTableColumn
oriWDSSecurityTableEncryptionKey0=_OriWDSSecurityTableEncryptionKey0_Object((1,3,6,1,4,1,11898,2,1,17,2,1,2),_OriWDSSecurityTableEncryptionKey0_Type())
oriWDSSecurityTableEncryptionKey0.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWDSSecurityTableEncryptionKey0.setStatus(_A)
_OrinocoTrap_ObjectIdentity=ObjectIdentity
orinocoTrap=_OrinocoTrap_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18))
_OriTrapVariable_ObjectIdentity=ObjectIdentity
oriTrapVariable=_OriTrapVariable_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,1))
_OriGenericTrapVariable_Type=DisplayString
_OriGenericTrapVariable_Object=MibScalar
oriGenericTrapVariable=_OriGenericTrapVariable_Object((1,3,6,1,4,1,11898,2,1,18,1,1),_OriGenericTrapVariable_Type())
oriGenericTrapVariable.setMaxAccess(_C)
if mibBuilder.loadTexts:oriGenericTrapVariable.setStatus(_A)
_OriTrapVarMACAddress_Type=PhysAddress
_OriTrapVarMACAddress_Object=MibScalar
oriTrapVarMACAddress=_OriTrapVarMACAddress_Object((1,3,6,1,4,1,11898,2,1,18,1,2),_OriTrapVarMACAddress_Type())
oriTrapVarMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarMACAddress.setStatus(_A)
_OriTrapVarTFTPIPAddress_Type=IpAddress
_OriTrapVarTFTPIPAddress_Object=MibScalar
oriTrapVarTFTPIPAddress=_OriTrapVarTFTPIPAddress_Object((1,3,6,1,4,1,11898,2,1,18,1,3),_OriTrapVarTFTPIPAddress_Type())
oriTrapVarTFTPIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarTFTPIPAddress.setStatus(_A)
_OriTrapVarTFTPFilename_Type=DisplayString
_OriTrapVarTFTPFilename_Object=MibScalar
oriTrapVarTFTPFilename=_OriTrapVarTFTPFilename_Object((1,3,6,1,4,1,11898,2,1,18,1,4),_OriTrapVarTFTPFilename_Type())
oriTrapVarTFTPFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarTFTPFilename.setStatus(_A)
class _OriTrapVarTFTPOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upload',1),('download',2)))
_OriTrapVarTFTPOperation_Type.__name__=_D
_OriTrapVarTFTPOperation_Object=MibScalar
oriTrapVarTFTPOperation=_OriTrapVarTFTPOperation_Object((1,3,6,1,4,1,11898,2,1,18,1,5),_OriTrapVarTFTPOperation_Type())
oriTrapVarTFTPOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarTFTPOperation.setStatus(_A)
_OriTrapVarUnauthorizedManagerIPaddress_Type=IpAddress
_OriTrapVarUnauthorizedManagerIPaddress_Object=MibScalar
oriTrapVarUnauthorizedManagerIPaddress=_OriTrapVarUnauthorizedManagerIPaddress_Object((1,3,6,1,4,1,11898,2,1,18,1,6),_OriTrapVarUnauthorizedManagerIPaddress_Type())
oriTrapVarUnauthorizedManagerIPaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarUnauthorizedManagerIPaddress.setStatus(_A)
_OriTrapVarFailedAuthenticationType_Type=DisplayString
_OriTrapVarFailedAuthenticationType_Object=MibScalar
oriTrapVarFailedAuthenticationType=_OriTrapVarFailedAuthenticationType_Object((1,3,6,1,4,1,11898,2,1,18,1,7),_OriTrapVarFailedAuthenticationType_Type())
oriTrapVarFailedAuthenticationType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarFailedAuthenticationType.setStatus(_A)
_OriTrapVarUnAuthorizedManagerCount_Type=Counter32
_OriTrapVarUnAuthorizedManagerCount_Object=MibScalar
oriTrapVarUnAuthorizedManagerCount=_OriTrapVarUnAuthorizedManagerCount_Object((1,3,6,1,4,1,11898,2,1,18,1,8),_OriTrapVarUnAuthorizedManagerCount_Type())
oriTrapVarUnAuthorizedManagerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarUnAuthorizedManagerCount.setStatus(_A)
_OriTrapVarTaskSuspended_Type=DisplayString
_OriTrapVarTaskSuspended_Object=MibScalar
oriTrapVarTaskSuspended=_OriTrapVarTaskSuspended_Object((1,3,6,1,4,1,11898,2,1,18,1,9),_OriTrapVarTaskSuspended_Type())
oriTrapVarTaskSuspended.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarTaskSuspended.setStatus(_A)
class _OriConfigurationTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriConfigurationTrapsStatus_Type.__name__=_D
_OriConfigurationTrapsStatus_Object=MibScalar
oriConfigurationTrapsStatus=_OriConfigurationTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,10),_OriConfigurationTrapsStatus_Type())
oriConfigurationTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriConfigurationTrapsStatus.setStatus(_A)
class _OriSecurityTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriSecurityTrapsStatus_Type.__name__=_D
_OriSecurityTrapsStatus_Object=MibScalar
oriSecurityTrapsStatus=_OriSecurityTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,11),_OriSecurityTrapsStatus_Type())
oriSecurityTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityTrapsStatus.setStatus(_A)
class _OriWirelessIfTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWirelessIfTrapsStatus_Type.__name__=_D
_OriWirelessIfTrapsStatus_Object=MibScalar
oriWirelessIfTrapsStatus=_OriWirelessIfTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,12),_OriWirelessIfTrapsStatus_Type())
oriWirelessIfTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWirelessIfTrapsStatus.setStatus(_A)
class _OriOperationalTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriOperationalTrapsStatus_Type.__name__=_D
_OriOperationalTrapsStatus_Object=MibScalar
oriOperationalTrapsStatus=_OriOperationalTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,13),_OriOperationalTrapsStatus_Type())
oriOperationalTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriOperationalTrapsStatus.setStatus(_A)
class _OriFlashMemoryTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriFlashMemoryTrapsStatus_Type.__name__=_D
_OriFlashMemoryTrapsStatus_Object=MibScalar
oriFlashMemoryTrapsStatus=_OriFlashMemoryTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,14),_OriFlashMemoryTrapsStatus_Type())
oriFlashMemoryTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriFlashMemoryTrapsStatus.setStatus(_A)
class _OriTFTPTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriTFTPTrapsStatus_Type.__name__=_D
_OriTFTPTrapsStatus_Object=MibScalar
oriTFTPTrapsStatus=_OriTFTPTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,15),_OriTFTPTrapsStatus_Type())
oriTFTPTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTFTPTrapsStatus.setStatus(_A)
class _OriTrapsImageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriTrapsImageStatus_Type.__name__=_D
_OriTrapsImageStatus_Object=MibScalar
oriTrapsImageStatus=_OriTrapsImageStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,16),_OriTrapsImageStatus_Type())
oriTrapsImageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriTrapsImageStatus.setStatus(_A)
_OriTrapVarUnauthorizedClientMACAddress_Type=PhysAddress
_OriTrapVarUnauthorizedClientMACAddress_Object=MibScalar
oriTrapVarUnauthorizedClientMACAddress=_OriTrapVarUnauthorizedClientMACAddress_Object((1,3,6,1,4,1,11898,2,1,18,1,17),_OriTrapVarUnauthorizedClientMACAddress_Type())
oriTrapVarUnauthorizedClientMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarUnauthorizedClientMACAddress.setStatus(_A)
class _OriTrapVarWirelessCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pcCardA',1),('pcCardB',2)))
_OriTrapVarWirelessCard_Type.__name__=_D
_OriTrapVarWirelessCard_Object=MibScalar
oriTrapVarWirelessCard=_OriTrapVarWirelessCard_Object((1,3,6,1,4,1,11898,2,1,18,1,18),_OriTrapVarWirelessCard_Type())
oriTrapVarWirelessCard.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarWirelessCard.setStatus(_A)
class _OriADSLIfTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriADSLIfTrapsStatus_Type.__name__=_D
_OriADSLIfTrapsStatus_Object=MibScalar
oriADSLIfTrapsStatus=_OriADSLIfTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,19),_OriADSLIfTrapsStatus_Type())
oriADSLIfTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriADSLIfTrapsStatus.setStatus(_A)
class _OriWORPTrapsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriWORPTrapsStatus_Type.__name__=_D
_OriWORPTrapsStatus_Object=MibScalar
oriWORPTrapsStatus=_OriWORPTrapsStatus_Object((1,3,6,1,4,1,11898,2,1,18,1,20),_OriWORPTrapsStatus_Type())
oriWORPTrapsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriWORPTrapsStatus.setStatus(_A)
_OriTrapVarInterface_Type=Integer32
_OriTrapVarInterface_Object=MibScalar
oriTrapVarInterface=_OriTrapVarInterface_Object((1,3,6,1,4,1,11898,2,1,18,1,21),_OriTrapVarInterface_Type())
oriTrapVarInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarInterface.setStatus(_A)
_OriTrapVarBatchCLIFilename_Type=DisplayString
_OriTrapVarBatchCLIFilename_Object=MibScalar
oriTrapVarBatchCLIFilename=_OriTrapVarBatchCLIFilename_Object((1,3,6,1,4,1,11898,2,1,18,1,22),_OriTrapVarBatchCLIFilename_Type())
oriTrapVarBatchCLIFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarBatchCLIFilename.setStatus(_A)
_OriTrapVarBatchCLIMessage_Type=DisplayString
_OriTrapVarBatchCLIMessage_Object=MibScalar
oriTrapVarBatchCLIMessage=_OriTrapVarBatchCLIMessage_Object((1,3,6,1,4,1,11898,2,1,18,1,23),_OriTrapVarBatchCLIMessage_Type())
oriTrapVarBatchCLIMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarBatchCLIMessage.setStatus(_A)
_OriTrapVarBatchCLILineNumber_Type=Integer32
_OriTrapVarBatchCLILineNumber_Object=MibScalar
oriTrapVarBatchCLILineNumber=_OriTrapVarBatchCLILineNumber_Object((1,3,6,1,4,1,11898,2,1,18,1,24),_OriTrapVarBatchCLILineNumber_Type())
oriTrapVarBatchCLILineNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarBatchCLILineNumber.setStatus(_A)
_OriTrapVarDHCPServerIPAddress_Type=IpAddress
_OriTrapVarDHCPServerIPAddress_Object=MibScalar
oriTrapVarDHCPServerIPAddress=_OriTrapVarDHCPServerIPAddress_Object((1,3,6,1,4,1,11898,2,1,18,1,25),_OriTrapVarDHCPServerIPAddress_Type())
oriTrapVarDHCPServerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarDHCPServerIPAddress.setStatus(_A)
_OriTrapVarIPAddress_Type=IpAddress
_OriTrapVarIPAddress_Object=MibScalar
oriTrapVarIPAddress=_OriTrapVarIPAddress_Object((1,3,6,1,4,1,11898,2,1,18,1,26),_OriTrapVarIPAddress_Type())
oriTrapVarIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarIPAddress.setStatus(_A)
_OriTrapVarSubnetMask_Type=IpAddress
_OriTrapVarSubnetMask_Object=MibScalar
oriTrapVarSubnetMask=_OriTrapVarSubnetMask_Object((1,3,6,1,4,1,11898,2,1,18,1,27),_OriTrapVarSubnetMask_Type())
oriTrapVarSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarSubnetMask.setStatus(_A)
_OriTrapVarDefaultRouterIPAddress_Type=IpAddress
_OriTrapVarDefaultRouterIPAddress_Object=MibScalar
oriTrapVarDefaultRouterIPAddress=_OriTrapVarDefaultRouterIPAddress_Object((1,3,6,1,4,1,11898,2,1,18,1,28),_OriTrapVarDefaultRouterIPAddress_Type())
oriTrapVarDefaultRouterIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriTrapVarDefaultRouterIPAddress.setStatus(_A)
_OriConfigurationTraps_ObjectIdentity=ObjectIdentity
oriConfigurationTraps=_OriConfigurationTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,2))
if mibBuilder.loadTexts:oriConfigurationTraps.setStatus(_A)
_OriSecurityTraps_ObjectIdentity=ObjectIdentity
oriSecurityTraps=_OriSecurityTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,3))
if mibBuilder.loadTexts:oriSecurityTraps.setStatus(_A)
_OriWirelessIfTraps_ObjectIdentity=ObjectIdentity
oriWirelessIfTraps=_OriWirelessIfTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,4))
if mibBuilder.loadTexts:oriWirelessIfTraps.setStatus(_A)
_OriOperationalTraps_ObjectIdentity=ObjectIdentity
oriOperationalTraps=_OriOperationalTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,5))
if mibBuilder.loadTexts:oriOperationalTraps.setStatus(_A)
_OriFlashTraps_ObjectIdentity=ObjectIdentity
oriFlashTraps=_OriFlashTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,6))
if mibBuilder.loadTexts:oriFlashTraps.setStatus(_A)
_OriTFTPTraps_ObjectIdentity=ObjectIdentity
oriTFTPTraps=_OriTFTPTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,7))
if mibBuilder.loadTexts:oriTFTPTraps.setStatus(_A)
_OriMiscTraps_ObjectIdentity=ObjectIdentity
oriMiscTraps=_OriMiscTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,8))
if mibBuilder.loadTexts:oriMiscTraps.setStatus(_A)
_OriImageTraps_ObjectIdentity=ObjectIdentity
oriImageTraps=_OriImageTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,9))
if mibBuilder.loadTexts:oriImageTraps.setStatus(_A)
_OriWORPTraps_ObjectIdentity=ObjectIdentity
oriWORPTraps=_OriWORPTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,11))
if mibBuilder.loadTexts:oriWORPTraps.setStatus(_A)
_OriSysFeatureTraps_ObjectIdentity=ObjectIdentity
oriSysFeatureTraps=_OriSysFeatureTraps_ObjectIdentity((1,3,6,1,4,1,11898,2,1,18,12))
if mibBuilder.loadTexts:oriSysFeatureTraps.setStatus(_A)
_OrinocoIPARP_ObjectIdentity=ObjectIdentity
orinocoIPARP=_OrinocoIPARP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,19))
class _OriProxyARPStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriProxyARPStatus_Type.__name__=_D
_OriProxyARPStatus_Object=MibScalar
oriProxyARPStatus=_OriProxyARPStatus_Object((1,3,6,1,4,1,11898,2,1,19,1),_OriProxyARPStatus_Type())
oriProxyARPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriProxyARPStatus.setStatus(_A)
class _OriIPARPFilteringStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriIPARPFilteringStatus_Type.__name__=_D
_OriIPARPFilteringStatus_Object=MibScalar
oriIPARPFilteringStatus=_OriIPARPFilteringStatus_Object((1,3,6,1,4,1,11898,2,1,19,2),_OriIPARPFilteringStatus_Type())
oriIPARPFilteringStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIPARPFilteringStatus.setStatus(_A)
_OriIPARPFilteringIPAddress_Type=IpAddress
_OriIPARPFilteringIPAddress_Object=MibScalar
oriIPARPFilteringIPAddress=_OriIPARPFilteringIPAddress_Object((1,3,6,1,4,1,11898,2,1,19,3),_OriIPARPFilteringIPAddress_Type())
oriIPARPFilteringIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIPARPFilteringIPAddress.setStatus(_A)
_OriIPARPFilteringSubnetMask_Type=IpAddress
_OriIPARPFilteringSubnetMask_Object=MibScalar
oriIPARPFilteringSubnetMask=_OriIPARPFilteringSubnetMask_Object((1,3,6,1,4,1,11898,2,1,19,4),_OriIPARPFilteringSubnetMask_Type())
oriIPARPFilteringSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriIPARPFilteringSubnetMask.setStatus(_A)
_OrinocoSpanningTree_ObjectIdentity=ObjectIdentity
orinocoSpanningTree=_OrinocoSpanningTree_ObjectIdentity((1,3,6,1,4,1,11898,2,1,20))
class _OriSpanningTreeStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriSpanningTreeStatus_Type.__name__=_D
_OriSpanningTreeStatus_Object=MibScalar
oriSpanningTreeStatus=_OriSpanningTreeStatus_Object((1,3,6,1,4,1,11898,2,1,20,1),_OriSpanningTreeStatus_Type())
oriSpanningTreeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSpanningTreeStatus.setStatus(_A)
_OrinocoSecurity_ObjectIdentity=ObjectIdentity
orinocoSecurity=_OrinocoSecurity_ObjectIdentity((1,3,6,1,4,1,11898,2,1,21))
class _OriSecurityConfiguration_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_b,2),('mixedWepAnddot1x',3)))
_OriSecurityConfiguration_Type.__name__=_D
_OriSecurityConfiguration_Object=MibScalar
oriSecurityConfiguration=_OriSecurityConfiguration_Object((1,3,6,1,4,1,11898,2,1,21,1),_OriSecurityConfiguration_Type())
oriSecurityConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityConfiguration.setStatus(_H)
_OriSecurityEncryptionKeyLengthTable_Object=MibTable
oriSecurityEncryptionKeyLengthTable=_OriSecurityEncryptionKeyLengthTable_Object((1,3,6,1,4,1,11898,2,1,21,2))
if mibBuilder.loadTexts:oriSecurityEncryptionKeyLengthTable.setStatus(_H)
_OriSecurityEncryptionKeyLengthTableEntry_Object=MibTableRow
oriSecurityEncryptionKeyLengthTableEntry=_OriSecurityEncryptionKeyLengthTableEntry_Object((1,3,6,1,4,1,11898,2,1,21,2,1))
oriSecurityEncryptionKeyLengthTableEntry.setIndexNames((0,_S,_T))
if mibBuilder.loadTexts:oriSecurityEncryptionKeyLengthTableEntry.setStatus(_H)
class _OriSecurityEncryptionKeyLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_OriSecurityEncryptionKeyLength_Type.__name__=_D
_OriSecurityEncryptionKeyLength_Object=MibTableColumn
oriSecurityEncryptionKeyLength=_OriSecurityEncryptionKeyLength_Object((1,3,6,1,4,1,11898,2,1,21,2,1,1),_OriSecurityEncryptionKeyLength_Type())
oriSecurityEncryptionKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityEncryptionKeyLength.setStatus(_H)
class _OriSecurityRekeyingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,65535))
_OriSecurityRekeyingInterval_Type.__name__=_D
_OriSecurityRekeyingInterval_Object=MibScalar
oriSecurityRekeyingInterval=_OriSecurityRekeyingInterval_Object((1,3,6,1,4,1,11898,2,1,21,3),_OriSecurityRekeyingInterval_Type())
oriSecurityRekeyingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityRekeyingInterval.setStatus(_H)
_OrinocoRAD_ObjectIdentity=ObjectIdentity
orinocoRAD=_OrinocoRAD_ObjectIdentity((1,3,6,1,4,1,11898,2,1,21,4))
class _OriRADStatus_Type(ObjStatus):defaultValue=2
_OriRADStatus_Type.__name__=_J
_OriRADStatus_Object=MibScalar
oriRADStatus=_OriRADStatus_Object((1,3,6,1,4,1,11898,2,1,21,4,1),_OriRADStatus_Type())
oriRADStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADStatus.setStatus(_A)
class _OriRADInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,1440))
_OriRADInterval_Type.__name__=_D
_OriRADInterval_Object=MibScalar
oriRADInterval=_OriRADInterval_Object((1,3,6,1,4,1,11898,2,1,21,4,2),_OriRADInterval_Type())
oriRADInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADInterval.setStatus(_A)
if mibBuilder.loadTexts:oriRADInterval.setUnits('seconds')
_OriRADInterfaceBitmask_Type=InterfaceBitmask
_OriRADInterfaceBitmask_Object=MibScalar
oriRADInterfaceBitmask=_OriRADInterfaceBitmask_Object((1,3,6,1,4,1,11898,2,1,21,4,3),_OriRADInterfaceBitmask_Type())
oriRADInterfaceBitmask.setMaxAccess(_B)
if mibBuilder.loadTexts:oriRADInterfaceBitmask.setStatus(_A)
_OriRADLastSuccessfulScanTime_Type=TimeTicks
_OriRADLastSuccessfulScanTime_Object=MibScalar
oriRADLastSuccessfulScanTime=_OriRADLastSuccessfulScanTime_Object((1,3,6,1,4,1,11898,2,1,21,4,4),_OriRADLastSuccessfulScanTime_Type())
oriRADLastSuccessfulScanTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADLastSuccessfulScanTime.setStatus(_A)
_OriRADAccessPointCount_Type=Counter32
_OriRADAccessPointCount_Object=MibScalar
oriRADAccessPointCount=_OriRADAccessPointCount_Object((1,3,6,1,4,1,11898,2,1,21,4,5),_OriRADAccessPointCount_Type())
oriRADAccessPointCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADAccessPointCount.setStatus(_A)
_OriRADScanResultsTable_Object=MibTable
oriRADScanResultsTable=_OriRADScanResultsTable_Object((1,3,6,1,4,1,11898,2,1,21,4,6))
if mibBuilder.loadTexts:oriRADScanResultsTable.setStatus(_A)
_OriRADScanResultsTableEntry_Object=MibTableRow
oriRADScanResultsTableEntry=_OriRADScanResultsTableEntry_Object((1,3,6,1,4,1,11898,2,1,21,4,6,1))
oriRADScanResultsTableEntry.setIndexNames((0,_E,_Al))
if mibBuilder.loadTexts:oriRADScanResultsTableEntry.setStatus(_A)
_OriRADScanResultsTableIndex_Type=Integer32
_OriRADScanResultsTableIndex_Object=MibTableColumn
oriRADScanResultsTableIndex=_OriRADScanResultsTableIndex_Object((1,3,6,1,4,1,11898,2,1,21,4,6,1,1),_OriRADScanResultsTableIndex_Type())
oriRADScanResultsTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADScanResultsTableIndex.setStatus(_A)
_OriRADScanResultsMACAddress_Type=PhysAddress
_OriRADScanResultsMACAddress_Object=MibTableColumn
oriRADScanResultsMACAddress=_OriRADScanResultsMACAddress_Object((1,3,6,1,4,1,11898,2,1,21,4,6,1,2),_OriRADScanResultsMACAddress_Type())
oriRADScanResultsMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADScanResultsMACAddress.setStatus(_A)
_OriRADScanResultsFrequencyChannel_Type=Integer32
_OriRADScanResultsFrequencyChannel_Object=MibTableColumn
oriRADScanResultsFrequencyChannel=_OriRADScanResultsFrequencyChannel_Object((1,3,6,1,4,1,11898,2,1,21,4,6,1,3),_OriRADScanResultsFrequencyChannel_Type())
oriRADScanResultsFrequencyChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRADScanResultsFrequencyChannel.setStatus(_A)
_OriSecurityConfigTable_Object=MibTable
oriSecurityConfigTable=_OriSecurityConfigTable_Object((1,3,6,1,4,1,11898,2,1,21,5))
if mibBuilder.loadTexts:oriSecurityConfigTable.setStatus(_H)
_OriSecurityConfigTableEntry_Object=MibTableRow
oriSecurityConfigTableEntry=_OriSecurityConfigTableEntry_Object((1,3,6,1,4,1,11898,2,1,21,5,1))
oriSecurityConfigTableEntry.setIndexNames((0,_S,_T))
if mibBuilder.loadTexts:oriSecurityConfigTableEntry.setStatus(_H)
_OriSecurityConfigTableSupportedSecurityModes_Type=DisplayString
_OriSecurityConfigTableSupportedSecurityModes_Object=MibTableColumn
oriSecurityConfigTableSupportedSecurityModes=_OriSecurityConfigTableSupportedSecurityModes_Object((1,3,6,1,4,1,11898,2,1,21,5,1,1),_OriSecurityConfigTableSupportedSecurityModes_Type())
oriSecurityConfigTableSupportedSecurityModes.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSecurityConfigTableSupportedSecurityModes.setStatus(_H)
class _OriSecurityConfigTableSecurityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_b,2),('mixed',3),('wpa',4),('wpa-psk',5)))
_OriSecurityConfigTableSecurityMode_Type.__name__=_D
_OriSecurityConfigTableSecurityMode_Object=MibTableColumn
oriSecurityConfigTableSecurityMode=_OriSecurityConfigTableSecurityMode_Object((1,3,6,1,4,1,11898,2,1,21,5,1,2),_OriSecurityConfigTableSecurityMode_Type())
oriSecurityConfigTableSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityConfigTableSecurityMode.setStatus(_H)
class _OriSecurityConfigTableRekeyingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,65535))
_OriSecurityConfigTableRekeyingInterval_Type.__name__=_D
_OriSecurityConfigTableRekeyingInterval_Object=MibTableColumn
oriSecurityConfigTableRekeyingInterval=_OriSecurityConfigTableRekeyingInterval_Object((1,3,6,1,4,1,11898,2,1,21,5,1,3),_OriSecurityConfigTableRekeyingInterval_Type())
oriSecurityConfigTableRekeyingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityConfigTableRekeyingInterval.setStatus(_H)
if mibBuilder.loadTexts:oriSecurityConfigTableRekeyingInterval.setUnits('seconds')
class _OriSecurityConfigTableEncryptionKeyLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),(_m,3)))
_OriSecurityConfigTableEncryptionKeyLength_Type.__name__=_D
_OriSecurityConfigTableEncryptionKeyLength_Object=MibTableColumn
oriSecurityConfigTableEncryptionKeyLength=_OriSecurityConfigTableEncryptionKeyLength_Object((1,3,6,1,4,1,11898,2,1,21,5,1,4),_OriSecurityConfigTableEncryptionKeyLength_Type())
oriSecurityConfigTableEncryptionKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityConfigTableEncryptionKeyLength.setStatus(_H)
class _OriSecurityHwConfigResetStatus_Type(ObjStatus):defaultValue=1
_OriSecurityHwConfigResetStatus_Type.__name__=_J
_OriSecurityHwConfigResetStatus_Object=MibScalar
oriSecurityHwConfigResetStatus=_OriSecurityHwConfigResetStatus_Object((1,3,6,1,4,1,11898,2,1,21,6),_OriSecurityHwConfigResetStatus_Type())
oriSecurityHwConfigResetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityHwConfigResetStatus.setStatus(_A)
class _OriSecurityHwConfigResetPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,32))
_OriSecurityHwConfigResetPassword_Type.__name__=_O
_OriSecurityHwConfigResetPassword_Object=MibScalar
oriSecurityHwConfigResetPassword=_OriSecurityHwConfigResetPassword_Object((1,3,6,1,4,1,11898,2,1,21,7),_OriSecurityHwConfigResetPassword_Type())
oriSecurityHwConfigResetPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityHwConfigResetPassword.setStatus(_A)
_OrinocoRogueScan_ObjectIdentity=ObjectIdentity
orinocoRogueScan=_OrinocoRogueScan_ObjectIdentity((1,3,6,1,4,1,11898,2,1,21,8))
_OriRogueScanConfigTable_Object=MibTable
oriRogueScanConfigTable=_OriRogueScanConfigTable_Object((1,3,6,1,4,1,11898,2,1,21,8,1))
if mibBuilder.loadTexts:oriRogueScanConfigTable.setStatus(_A)
_OriRogueScanConfigTableEntry_Object=MibTableRow
oriRogueScanConfigTableEntry=_OriRogueScanConfigTableEntry_Object((1,3,6,1,4,1,11898,2,1,21,8,1,1))
oriRogueScanConfigTableEntry.setIndexNames((0,_S,_T))
if mibBuilder.loadTexts:oriRogueScanConfigTableEntry.setStatus(_A)
class _OriRogueScanConfigTableScanMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bkScanMode',1),('contScanMode',2)))
_OriRogueScanConfigTableScanMode_Type.__name__=_D
_OriRogueScanConfigTableScanMode_Object=MibTableColumn
oriRogueScanConfigTableScanMode=_OriRogueScanConfigTableScanMode_Object((1,3,6,1,4,1,11898,2,1,21,8,1,1,1),_OriRogueScanConfigTableScanMode_Type())
oriRogueScanConfigTableScanMode.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRogueScanConfigTableScanMode.setStatus(_A)
class _OriRogueScanConfigTableScanCycleTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_OriRogueScanConfigTableScanCycleTime_Type.__name__=_D
_OriRogueScanConfigTableScanCycleTime_Object=MibTableColumn
oriRogueScanConfigTableScanCycleTime=_OriRogueScanConfigTableScanCycleTime_Object((1,3,6,1,4,1,11898,2,1,21,8,1,1,2),_OriRogueScanConfigTableScanCycleTime_Type())
oriRogueScanConfigTableScanCycleTime.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRogueScanConfigTableScanCycleTime.setStatus(_A)
_OriRogueScanConfigTableScanStatus_Type=ObjStatus
_OriRogueScanConfigTableScanStatus_Object=MibTableColumn
oriRogueScanConfigTableScanStatus=_OriRogueScanConfigTableScanStatus_Object((1,3,6,1,4,1,11898,2,1,21,8,1,1,3),_OriRogueScanConfigTableScanStatus_Type())
oriRogueScanConfigTableScanStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRogueScanConfigTableScanStatus.setStatus(_A)
_OriRogueScanStationCountWirelessCardA_Type=Counter32
_OriRogueScanStationCountWirelessCardA_Object=MibScalar
oriRogueScanStationCountWirelessCardA=_OriRogueScanStationCountWirelessCardA_Object((1,3,6,1,4,1,11898,2,1,21,8,2),_OriRogueScanStationCountWirelessCardA_Type())
oriRogueScanStationCountWirelessCardA.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanStationCountWirelessCardA.setStatus(_A)
_OriRogueScanStationCountWirelessCardB_Type=Counter32
_OriRogueScanStationCountWirelessCardB_Object=MibScalar
oriRogueScanStationCountWirelessCardB=_OriRogueScanStationCountWirelessCardB_Object((1,3,6,1,4,1,11898,2,1,21,8,3),_OriRogueScanStationCountWirelessCardB_Type())
oriRogueScanStationCountWirelessCardB.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanStationCountWirelessCardB.setStatus(_A)
class _OriRogueScanResultsTableAgingTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,7200))
_OriRogueScanResultsTableAgingTime_Type.__name__=_D
_OriRogueScanResultsTableAgingTime_Object=MibScalar
oriRogueScanResultsTableAgingTime=_OriRogueScanResultsTableAgingTime_Object((1,3,6,1,4,1,11898,2,1,21,8,4),_OriRogueScanResultsTableAgingTime_Type())
oriRogueScanResultsTableAgingTime.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRogueScanResultsTableAgingTime.setStatus(_A)
_OriRogueScanResultsTableClearEntries_Type=Integer32
_OriRogueScanResultsTableClearEntries_Object=MibScalar
oriRogueScanResultsTableClearEntries=_OriRogueScanResultsTableClearEntries_Object((1,3,6,1,4,1,11898,2,1,21,8,5),_OriRogueScanResultsTableClearEntries_Type())
oriRogueScanResultsTableClearEntries.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRogueScanResultsTableClearEntries.setStatus(_A)
class _OriRogueScanResultsNotificationMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noNotification',1),('notifyAP',2),('notifyClient',3),('notifyAll',4)))
_OriRogueScanResultsNotificationMode_Type.__name__=_D
_OriRogueScanResultsNotificationMode_Object=MibScalar
oriRogueScanResultsNotificationMode=_OriRogueScanResultsNotificationMode_Object((1,3,6,1,4,1,11898,2,1,21,8,6),_OriRogueScanResultsNotificationMode_Type())
oriRogueScanResultsNotificationMode.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRogueScanResultsNotificationMode.setStatus(_A)
class _OriRogueScanResultsTrapReportType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reportSinceLastScan',1),('reportSinceStartOfScan',2)))
_OriRogueScanResultsTrapReportType_Type.__name__=_D
_OriRogueScanResultsTrapReportType_Object=MibScalar
oriRogueScanResultsTrapReportType=_OriRogueScanResultsTrapReportType_Object((1,3,6,1,4,1,11898,2,1,21,8,7),_OriRogueScanResultsTrapReportType_Type())
oriRogueScanResultsTrapReportType.setMaxAccess(_I)
if mibBuilder.loadTexts:oriRogueScanResultsTrapReportType.setStatus(_A)
_OriRogueScanResultsTable_Object=MibTable
oriRogueScanResultsTable=_OriRogueScanResultsTable_Object((1,3,6,1,4,1,11898,2,1,21,8,8))
if mibBuilder.loadTexts:oriRogueScanResultsTable.setStatus(_A)
_OriRogueScanResultsTableEntry_Object=MibTableRow
oriRogueScanResultsTableEntry=_OriRogueScanResultsTableEntry_Object((1,3,6,1,4,1,11898,2,1,21,8,8,1))
oriRogueScanResultsTableEntry.setIndexNames((0,_E,_Am))
if mibBuilder.loadTexts:oriRogueScanResultsTableEntry.setStatus(_A)
_OriRogueScanResultsTableIndex_Type=Integer32
_OriRogueScanResultsTableIndex_Object=MibTableColumn
oriRogueScanResultsTableIndex=_OriRogueScanResultsTableIndex_Object((1,3,6,1,4,1,11898,2,1,21,8,8,1,1),_OriRogueScanResultsTableIndex_Type())
oriRogueScanResultsTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanResultsTableIndex.setStatus(_A)
class _OriRogueScanResultsStationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_s,1),('infrastructureClient',2),('accessPoint',3),('ibssClient',4)))
_OriRogueScanResultsStationType_Type.__name__=_D
_OriRogueScanResultsStationType_Object=MibTableColumn
oriRogueScanResultsStationType=_OriRogueScanResultsStationType_Object((1,3,6,1,4,1,11898,2,1,21,8,8,1,2),_OriRogueScanResultsStationType_Type())
oriRogueScanResultsStationType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanResultsStationType.setStatus(_A)
_OriRogueScanResultsMACAddress_Type=PhysAddress
_OriRogueScanResultsMACAddress_Object=MibTableColumn
oriRogueScanResultsMACAddress=_OriRogueScanResultsMACAddress_Object((1,3,6,1,4,1,11898,2,1,21,8,8,1,3),_OriRogueScanResultsMACAddress_Type())
oriRogueScanResultsMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanResultsMACAddress.setStatus(_A)
class _OriRogueScanResultsFrequencyChannel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_OriRogueScanResultsFrequencyChannel_Type.__name__=_O
_OriRogueScanResultsFrequencyChannel_Object=MibTableColumn
oriRogueScanResultsFrequencyChannel=_OriRogueScanResultsFrequencyChannel_Object((1,3,6,1,4,1,11898,2,1,21,8,8,1,5),_OriRogueScanResultsFrequencyChannel_Type())
oriRogueScanResultsFrequencyChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanResultsFrequencyChannel.setStatus(_A)
_OriRogueScanResultsSNR_Type=Integer32
_OriRogueScanResultsSNR_Object=MibTableColumn
oriRogueScanResultsSNR=_OriRogueScanResultsSNR_Object((1,3,6,1,4,1,11898,2,1,21,8,8,1,6),_OriRogueScanResultsSNR_Type())
oriRogueScanResultsSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanResultsSNR.setStatus(_A)
_OriRogueScanResultsBSSID_Type=MacAddress
_OriRogueScanResultsBSSID_Object=MibTableColumn
oriRogueScanResultsBSSID=_OriRogueScanResultsBSSID_Object((1,3,6,1,4,1,11898,2,1,21,8,8,1,7),_OriRogueScanResultsBSSID_Type())
oriRogueScanResultsBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:oriRogueScanResultsBSSID.setStatus(_A)
_OriSecurityProfileTable_Object=MibTable
oriSecurityProfileTable=_OriSecurityProfileTable_Object((1,3,6,1,4,1,11898,2,1,21,9))
if mibBuilder.loadTexts:oriSecurityProfileTable.setStatus(_A)
_OriSecurityProfileTableEntry_Object=MibTableRow
oriSecurityProfileTableEntry=_OriSecurityProfileTableEntry_Object((1,3,6,1,4,1,11898,2,1,21,9,1))
oriSecurityProfileTableEntry.setIndexNames((0,_E,_An),(0,_E,_Ao))
if mibBuilder.loadTexts:oriSecurityProfileTableEntry.setStatus(_A)
_OriSecurityProfileTableIndex_Type=Integer32
_OriSecurityProfileTableIndex_Object=MibTableColumn
oriSecurityProfileTableIndex=_OriSecurityProfileTableIndex_Object((1,3,6,1,4,1,11898,2,1,21,9,1,1),_OriSecurityProfileTableIndex_Type())
oriSecurityProfileTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSecurityProfileTableIndex.setStatus(_A)
_OriSecurityProfileTableSecModeIndex_Type=Integer32
_OriSecurityProfileTableSecModeIndex_Object=MibTableColumn
oriSecurityProfileTableSecModeIndex=_OriSecurityProfileTableSecModeIndex_Object((1,3,6,1,4,1,11898,2,1,21,9,1,2),_OriSecurityProfileTableSecModeIndex_Type())
oriSecurityProfileTableSecModeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSecurityProfileTableSecModeIndex.setStatus(_A)
class _OriSecurityProfileTableAuthenticationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_b,2),('psk',3)))
_OriSecurityProfileTableAuthenticationMode_Type.__name__=_D
_OriSecurityProfileTableAuthenticationMode_Object=MibTableColumn
oriSecurityProfileTableAuthenticationMode=_OriSecurityProfileTableAuthenticationMode_Object((1,3,6,1,4,1,11898,2,1,21,9,1,3),_OriSecurityProfileTableAuthenticationMode_Type())
oriSecurityProfileTableAuthenticationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSecurityProfileTableAuthenticationMode.setStatus(_A)
class _OriSecurityProfileTableCipherMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_Z,2),('tkip',3),('aes',4)))
_OriSecurityProfileTableCipherMode_Type.__name__=_D
_OriSecurityProfileTableCipherMode_Object=MibTableColumn
oriSecurityProfileTableCipherMode=_OriSecurityProfileTableCipherMode_Object((1,3,6,1,4,1,11898,2,1,21,9,1,4),_OriSecurityProfileTableCipherMode_Type())
oriSecurityProfileTableCipherMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSecurityProfileTableCipherMode.setStatus(_A)
_OriSecurityProfileTableEncryptionKey0_Type=WEPKeyType
_OriSecurityProfileTableEncryptionKey0_Object=MibTableColumn
oriSecurityProfileTableEncryptionKey0=_OriSecurityProfileTableEncryptionKey0_Object((1,3,6,1,4,1,11898,2,1,21,9,1,5),_OriSecurityProfileTableEncryptionKey0_Type())
oriSecurityProfileTableEncryptionKey0.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTableEncryptionKey0.setStatus(_A)
_OriSecurityProfileTableEncryptionKey1_Type=WEPKeyType
_OriSecurityProfileTableEncryptionKey1_Object=MibTableColumn
oriSecurityProfileTableEncryptionKey1=_OriSecurityProfileTableEncryptionKey1_Object((1,3,6,1,4,1,11898,2,1,21,9,1,6),_OriSecurityProfileTableEncryptionKey1_Type())
oriSecurityProfileTableEncryptionKey1.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTableEncryptionKey1.setStatus(_A)
_OriSecurityProfileTableEncryptionKey2_Type=WEPKeyType
_OriSecurityProfileTableEncryptionKey2_Object=MibTableColumn
oriSecurityProfileTableEncryptionKey2=_OriSecurityProfileTableEncryptionKey2_Object((1,3,6,1,4,1,11898,2,1,21,9,1,7),_OriSecurityProfileTableEncryptionKey2_Type())
oriSecurityProfileTableEncryptionKey2.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTableEncryptionKey2.setStatus(_A)
_OriSecurityProfileTableEncryptionKey3_Type=WEPKeyType
_OriSecurityProfileTableEncryptionKey3_Object=MibTableColumn
oriSecurityProfileTableEncryptionKey3=_OriSecurityProfileTableEncryptionKey3_Object((1,3,6,1,4,1,11898,2,1,21,9,1,8),_OriSecurityProfileTableEncryptionKey3_Type())
oriSecurityProfileTableEncryptionKey3.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTableEncryptionKey3.setStatus(_A)
class _OriSecurityProfileTableEncryptionTxKey_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_OriSecurityProfileTableEncryptionTxKey_Type.__name__=_D
_OriSecurityProfileTableEncryptionTxKey_Object=MibTableColumn
oriSecurityProfileTableEncryptionTxKey=_OriSecurityProfileTableEncryptionTxKey_Object((1,3,6,1,4,1,11898,2,1,21,9,1,9),_OriSecurityProfileTableEncryptionTxKey_Type())
oriSecurityProfileTableEncryptionTxKey.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTableEncryptionTxKey.setStatus(_A)
class _OriSecurityProfileTableEncryptionKeyLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),(_m,3)))
_OriSecurityProfileTableEncryptionKeyLength_Type.__name__=_D
_OriSecurityProfileTableEncryptionKeyLength_Object=MibTableColumn
oriSecurityProfileTableEncryptionKeyLength=_OriSecurityProfileTableEncryptionKeyLength_Object((1,3,6,1,4,1,11898,2,1,21,9,1,10),_OriSecurityProfileTableEncryptionKeyLength_Type())
oriSecurityProfileTableEncryptionKeyLength.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTableEncryptionKeyLength.setStatus(_A)
class _OriSecurityProfileTablePSKValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_OriSecurityProfileTablePSKValue_Type.__name__=_V
_OriSecurityProfileTablePSKValue_Object=MibTableColumn
oriSecurityProfileTablePSKValue=_OriSecurityProfileTablePSKValue_Object((1,3,6,1,4,1,11898,2,1,21,9,1,11),_OriSecurityProfileTablePSKValue_Type())
oriSecurityProfileTablePSKValue.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTablePSKValue.setStatus(_A)
class _OriSecurityProfileTablePSKPassPhrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,63))
_OriSecurityProfileTablePSKPassPhrase_Type.__name__=_O
_OriSecurityProfileTablePSKPassPhrase_Object=MibTableColumn
oriSecurityProfileTablePSKPassPhrase=_OriSecurityProfileTablePSKPassPhrase_Object((1,3,6,1,4,1,11898,2,1,21,9,1,12),_OriSecurityProfileTablePSKPassPhrase_Type())
oriSecurityProfileTablePSKPassPhrase.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTablePSKPassPhrase.setStatus(_A)
_OriSecurityProfileTableStatus_Type=RowStatus
_OriSecurityProfileTableStatus_Object=MibTableColumn
oriSecurityProfileTableStatus=_OriSecurityProfileTableStatus_Object((1,3,6,1,4,1,11898,2,1,21,9,1,14),_OriSecurityProfileTableStatus_Type())
oriSecurityProfileTableStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:oriSecurityProfileTableStatus.setStatus(_A)
_OriSecurityProfileFourWEPKeySupport_Type=Integer32
_OriSecurityProfileFourWEPKeySupport_Object=MibScalar
oriSecurityProfileFourWEPKeySupport=_OriSecurityProfileFourWEPKeySupport_Object((1,3,6,1,4,1,11898,2,1,21,10),_OriSecurityProfileFourWEPKeySupport_Type())
oriSecurityProfileFourWEPKeySupport.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSecurityProfileFourWEPKeySupport.setStatus(_A)
_OrinocoPPPoE_ObjectIdentity=ObjectIdentity
orinocoPPPoE=_OrinocoPPPoE_ObjectIdentity((1,3,6,1,4,1,11898,2,1,22))
class _OriPPPoEStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriPPPoEStatus_Type.__name__=_D
_OriPPPoEStatus_Object=MibScalar
oriPPPoEStatus=_OriPPPoEStatus_Object((1,3,6,1,4,1,11898,2,1,22,1),_OriPPPoEStatus_Type())
oriPPPoEStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoEStatus.setStatus(_A)
class _OriPPPoEMaximumNumberOfSessions_Type(Integer32):defaultValue=10
_OriPPPoEMaximumNumberOfSessions_Type.__name__=_D
_OriPPPoEMaximumNumberOfSessions_Object=MibScalar
oriPPPoEMaximumNumberOfSessions=_OriPPPoEMaximumNumberOfSessions_Object((1,3,6,1,4,1,11898,2,1,22,2),_OriPPPoEMaximumNumberOfSessions_Type())
oriPPPoEMaximumNumberOfSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoEMaximumNumberOfSessions.setStatus(_A)
_OriPPPoENumberOfActiveSessions_Type=Counter32
_OriPPPoENumberOfActiveSessions_Object=MibScalar
oriPPPoENumberOfActiveSessions=_OriPPPoENumberOfActiveSessions_Object((1,3,6,1,4,1,11898,2,1,22,3),_OriPPPoENumberOfActiveSessions_Type())
oriPPPoENumberOfActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoENumberOfActiveSessions.setStatus(_A)
_OriPPPoESessionTable_Object=MibTable
oriPPPoESessionTable=_OriPPPoESessionTable_Object((1,3,6,1,4,1,11898,2,1,22,4))
if mibBuilder.loadTexts:oriPPPoESessionTable.setStatus(_A)
_OriPPPoESessionTableEntry_Object=MibTableRow
oriPPPoESessionTableEntry=_OriPPPoESessionTableEntry_Object((1,3,6,1,4,1,11898,2,1,22,4,1))
oriPPPoESessionTableEntry.setIndexNames((0,_E,_Ap))
if mibBuilder.loadTexts:oriPPPoESessionTableEntry.setStatus(_A)
_OriPPPoESessionTableIndex_Type=Integer32
_OriPPPoESessionTableIndex_Object=MibTableColumn
oriPPPoESessionTableIndex=_OriPPPoESessionTableIndex_Object((1,3,6,1,4,1,11898,2,1,22,4,1,1),_OriPPPoESessionTableIndex_Type())
oriPPPoESessionTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionTableIndex.setStatus(_A)
class _OriPPPoESessionWANConnectMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('alwaysOn',1),('onDemand',2),('manual',3)))
_OriPPPoESessionWANConnectMode_Type.__name__=_D
_OriPPPoESessionWANConnectMode_Object=MibTableColumn
oriPPPoESessionWANConnectMode=_OriPPPoESessionWANConnectMode_Object((1,3,6,1,4,1,11898,2,1,22,4,1,2),_OriPPPoESessionWANConnectMode_Type())
oriPPPoESessionWANConnectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionWANConnectMode.setStatus(_A)
_OriPPPoESessionIdleTimeOut_Type=Integer32
_OriPPPoESessionIdleTimeOut_Object=MibTableColumn
oriPPPoESessionIdleTimeOut=_OriPPPoESessionIdleTimeOut_Object((1,3,6,1,4,1,11898,2,1,22,4,1,3),_OriPPPoESessionIdleTimeOut_Type())
oriPPPoESessionIdleTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionIdleTimeOut.setStatus(_A)
_OriPPPoESessionConnectTime_Type=Counter32
_OriPPPoESessionConnectTime_Object=MibTableColumn
oriPPPoESessionConnectTime=_OriPPPoESessionConnectTime_Object((1,3,6,1,4,1,11898,2,1,22,4,1,4),_OriPPPoESessionConnectTime_Type())
oriPPPoESessionConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionConnectTime.setStatus(_A)
class _OriPPPoESessionConnectTimeLimitation_Type(Integer32):defaultValue=0
_OriPPPoESessionConnectTimeLimitation_Type.__name__=_D
_OriPPPoESessionConnectTimeLimitation_Object=MibTableColumn
oriPPPoESessionConnectTimeLimitation=_OriPPPoESessionConnectTimeLimitation_Object((1,3,6,1,4,1,11898,2,1,22,4,1,5),_OriPPPoESessionConnectTimeLimitation_Type())
oriPPPoESessionConnectTimeLimitation.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionConnectTimeLimitation.setStatus(_A)
_OriPPPoESessionConfigPADITxInterval_Type=Integer32
_OriPPPoESessionConfigPADITxInterval_Object=MibTableColumn
oriPPPoESessionConfigPADITxInterval=_OriPPPoESessionConfigPADITxInterval_Object((1,3,6,1,4,1,11898,2,1,22,4,1,6),_OriPPPoESessionConfigPADITxInterval_Type())
oriPPPoESessionConfigPADITxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionConfigPADITxInterval.setStatus(_A)
_OriPPPoESessionConfigPADIMaxNumberOfRetries_Type=Integer32
_OriPPPoESessionConfigPADIMaxNumberOfRetries_Object=MibTableColumn
oriPPPoESessionConfigPADIMaxNumberOfRetries=_OriPPPoESessionConfigPADIMaxNumberOfRetries_Object((1,3,6,1,4,1,11898,2,1,22,4,1,7),_OriPPPoESessionConfigPADIMaxNumberOfRetries_Type())
oriPPPoESessionConfigPADIMaxNumberOfRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionConfigPADIMaxNumberOfRetries.setStatus(_A)
_OriPPPoESessionBindingsNumberPADITx_Type=Counter32
_OriPPPoESessionBindingsNumberPADITx_Object=MibTableColumn
oriPPPoESessionBindingsNumberPADITx=_OriPPPoESessionBindingsNumberPADITx_Object((1,3,6,1,4,1,11898,2,1,22,4,1,8),_OriPPPoESessionBindingsNumberPADITx_Type())
oriPPPoESessionBindingsNumberPADITx.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberPADITx.setStatus(_A)
_OriPPPoESessionBindingsNumberPADTTx_Type=Counter32
_OriPPPoESessionBindingsNumberPADTTx_Object=MibTableColumn
oriPPPoESessionBindingsNumberPADTTx=_OriPPPoESessionBindingsNumberPADTTx_Object((1,3,6,1,4,1,11898,2,1,22,4,1,9),_OriPPPoESessionBindingsNumberPADTTx_Type())
oriPPPoESessionBindingsNumberPADTTx.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberPADTTx.setStatus(_A)
_OriPPPoESessionBindingsNumberServiceNameErrors_Type=Counter32
_OriPPPoESessionBindingsNumberServiceNameErrors_Object=MibTableColumn
oriPPPoESessionBindingsNumberServiceNameErrors=_OriPPPoESessionBindingsNumberServiceNameErrors_Object((1,3,6,1,4,1,11898,2,1,22,4,1,10),_OriPPPoESessionBindingsNumberServiceNameErrors_Type())
oriPPPoESessionBindingsNumberServiceNameErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberServiceNameErrors.setStatus(_A)
_OriPPPoESessionBindingsNumberACSystemErrors_Type=Counter32
_OriPPPoESessionBindingsNumberACSystemErrors_Object=MibTableColumn
oriPPPoESessionBindingsNumberACSystemErrors=_OriPPPoESessionBindingsNumberACSystemErrors_Object((1,3,6,1,4,1,11898,2,1,22,4,1,11),_OriPPPoESessionBindingsNumberACSystemErrors_Type())
oriPPPoESessionBindingsNumberACSystemErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberACSystemErrors.setStatus(_A)
_OriPPPoESessionBindingsNumberGenericErrorsRx_Type=Counter32
_OriPPPoESessionBindingsNumberGenericErrorsRx_Object=MibTableColumn
oriPPPoESessionBindingsNumberGenericErrorsRx=_OriPPPoESessionBindingsNumberGenericErrorsRx_Object((1,3,6,1,4,1,11898,2,1,22,4,1,12),_OriPPPoESessionBindingsNumberGenericErrorsRx_Type())
oriPPPoESessionBindingsNumberGenericErrorsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberGenericErrorsRx.setStatus(_A)
_OriPPPoESessionBindingsNumberGenericErrorsTx_Type=Counter32
_OriPPPoESessionBindingsNumberGenericErrorsTx_Object=MibTableColumn
oriPPPoESessionBindingsNumberGenericErrorsTx=_OriPPPoESessionBindingsNumberGenericErrorsTx_Object((1,3,6,1,4,1,11898,2,1,22,4,1,13),_OriPPPoESessionBindingsNumberGenericErrorsTx_Type())
oriPPPoESessionBindingsNumberGenericErrorsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberGenericErrorsTx.setStatus(_A)
_OriPPPoESessionBindingsNumberMalformedPackets_Type=Counter32
_OriPPPoESessionBindingsNumberMalformedPackets_Object=MibTableColumn
oriPPPoESessionBindingsNumberMalformedPackets=_OriPPPoESessionBindingsNumberMalformedPackets_Object((1,3,6,1,4,1,11898,2,1,22,4,1,14),_OriPPPoESessionBindingsNumberMalformedPackets_Type())
oriPPPoESessionBindingsNumberMalformedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberMalformedPackets.setStatus(_A)
_OriPPPoESessionBindingsNumberMultiplePADORx_Type=Counter32
_OriPPPoESessionBindingsNumberMultiplePADORx_Object=MibTableColumn
oriPPPoESessionBindingsNumberMultiplePADORx=_OriPPPoESessionBindingsNumberMultiplePADORx_Object((1,3,6,1,4,1,11898,2,1,22,4,1,15),_OriPPPoESessionBindingsNumberMultiplePADORx_Type())
oriPPPoESessionBindingsNumberMultiplePADORx.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionBindingsNumberMultiplePADORx.setStatus(_A)
_OriPPPoESessionUserName_Type=DisplayString
_OriPPPoESessionUserName_Object=MibTableColumn
oriPPPoESessionUserName=_OriPPPoESessionUserName_Object((1,3,6,1,4,1,11898,2,1,22,4,1,16),_OriPPPoESessionUserName_Type())
oriPPPoESessionUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionUserName.setStatus(_A)
_OriPPPoESessionUserNamePassword_Type=DisplayString
_OriPPPoESessionUserNamePassword_Object=MibTableColumn
oriPPPoESessionUserNamePassword=_OriPPPoESessionUserNamePassword_Object((1,3,6,1,4,1,11898,2,1,22,4,1,17),_OriPPPoESessionUserNamePassword_Type())
oriPPPoESessionUserNamePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionUserNamePassword.setStatus(_A)
_OriPPPoESessionServiceName_Type=DisplayString
_OriPPPoESessionServiceName_Object=MibTableColumn
oriPPPoESessionServiceName=_OriPPPoESessionServiceName_Object((1,3,6,1,4,1,11898,2,1,22,4,1,18),_OriPPPoESessionServiceName_Type())
oriPPPoESessionServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionServiceName.setStatus(_A)
_OriPPPoESessionISPName_Type=DisplayString
_OriPPPoESessionISPName_Object=MibTableColumn
oriPPPoESessionISPName=_OriPPPoESessionISPName_Object((1,3,6,1,4,1,11898,2,1,22,4,1,19),_OriPPPoESessionISPName_Type())
oriPPPoESessionISPName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionISPName.setStatus(_A)
class _OriPPPoESessionTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriPPPoESessionTableStatus_Type.__name__=_D
_OriPPPoESessionTableStatus_Object=MibTableColumn
oriPPPoESessionTableStatus=_OriPPPoESessionTableStatus_Object((1,3,6,1,4,1,11898,2,1,22,4,1,20),_OriPPPoESessionTableStatus_Type())
oriPPPoESessionTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionTableStatus.setStatus(_A)
class _OriPPPoESessionWANManualConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriPPPoESessionWANManualConnect_Type.__name__=_D
_OriPPPoESessionWANManualConnect_Object=MibTableColumn
oriPPPoESessionWANManualConnect=_OriPPPoESessionWANManualConnect_Object((1,3,6,1,4,1,11898,2,1,22,4,1,21),_OriPPPoESessionWANManualConnect_Type())
oriPPPoESessionWANManualConnect.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoESessionWANManualConnect.setStatus(_A)
class _OriPPPoESessionWANConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('null',1),('start',2),('addingStack',3),('stackAdded',4),('stackAddError',5),('connectFailed',6),('authFailed',7),(_X,8),(_Y,9),('suspended',10),(_s,11)))
_OriPPPoESessionWANConnectionStatus_Type.__name__=_D
_OriPPPoESessionWANConnectionStatus_Object=MibTableColumn
oriPPPoESessionWANConnectionStatus=_OriPPPoESessionWANConnectionStatus_Object((1,3,6,1,4,1,11898,2,1,22,4,1,22),_OriPPPoESessionWANConnectionStatus_Type())
oriPPPoESessionWANConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoESessionWANConnectionStatus.setStatus(_A)
_OriPPPoEMACtoSessionTable_Object=MibTable
oriPPPoEMACtoSessionTable=_OriPPPoEMACtoSessionTable_Object((1,3,6,1,4,1,11898,2,1,22,5))
if mibBuilder.loadTexts:oriPPPoEMACtoSessionTable.setStatus(_A)
_OriPPPoEMACtoSessionTableEntry_Object=MibTableRow
oriPPPoEMACtoSessionTableEntry=_OriPPPoEMACtoSessionTableEntry_Object((1,3,6,1,4,1,11898,2,1,22,5,1))
oriPPPoEMACtoSessionTableEntry.setIndexNames((0,_E,_Aq))
if mibBuilder.loadTexts:oriPPPoEMACtoSessionTableEntry.setStatus(_A)
_OriPPPoEMACtoSessionTableIndex_Type=Integer32
_OriPPPoEMACtoSessionTableIndex_Object=MibTableColumn
oriPPPoEMACtoSessionTableIndex=_OriPPPoEMACtoSessionTableIndex_Object((1,3,6,1,4,1,11898,2,1,22,5,1,1),_OriPPPoEMACtoSessionTableIndex_Type())
oriPPPoEMACtoSessionTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriPPPoEMACtoSessionTableIndex.setStatus(_A)
_OriPPPoEMACtoSessionTableMACAddress_Type=PhysAddress
_OriPPPoEMACtoSessionTableMACAddress_Object=MibTableColumn
oriPPPoEMACtoSessionTableMACAddress=_OriPPPoEMACtoSessionTableMACAddress_Object((1,3,6,1,4,1,11898,2,1,22,5,1,2),_OriPPPoEMACtoSessionTableMACAddress_Type())
oriPPPoEMACtoSessionTableMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoEMACtoSessionTableMACAddress.setStatus(_A)
_OriPPPoEMACtoSessionTableISPName_Type=DisplayString
_OriPPPoEMACtoSessionTableISPName_Object=MibTableColumn
oriPPPoEMACtoSessionTableISPName=_OriPPPoEMACtoSessionTableISPName_Object((1,3,6,1,4,1,11898,2,1,22,5,1,3),_OriPPPoEMACtoSessionTableISPName_Type())
oriPPPoEMACtoSessionTableISPName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoEMACtoSessionTableISPName.setStatus(_A)
class _OriPPPoEMACtoSessionTableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriPPPoEMACtoSessionTableStatus_Type.__name__=_D
_OriPPPoEMACtoSessionTableStatus_Object=MibTableColumn
oriPPPoEMACtoSessionTableStatus=_OriPPPoEMACtoSessionTableStatus_Object((1,3,6,1,4,1,11898,2,1,22,5,1,4),_OriPPPoEMACtoSessionTableStatus_Type())
oriPPPoEMACtoSessionTableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriPPPoEMACtoSessionTableStatus.setStatus(_A)
_OrinocoConfig_ObjectIdentity=ObjectIdentity
orinocoConfig=_OrinocoConfig_ObjectIdentity((1,3,6,1,4,1,11898,2,1,23))
class _OriConfigResetToDefaults_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bridgeMode',1),('gatewayMode',2),('gatewayModeDHCPClient',3),('gatewayModePPPoE',4)))
_OriConfigResetToDefaults_Type.__name__=_D
_OriConfigResetToDefaults_Object=MibScalar
oriConfigResetToDefaults=_OriConfigResetToDefaults_Object((1,3,6,1,4,1,11898,2,1,23,1),_OriConfigResetToDefaults_Type())
oriConfigResetToDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:oriConfigResetToDefaults.setStatus(_A)
_OriConfigFileTable_Object=MibTable
oriConfigFileTable=_OriConfigFileTable_Object((1,3,6,1,4,1,11898,2,1,23,2))
if mibBuilder.loadTexts:oriConfigFileTable.setStatus(_A)
_OriConfigFileTableEntry_Object=MibTableRow
oriConfigFileTableEntry=_OriConfigFileTableEntry_Object((1,3,6,1,4,1,11898,2,1,23,2,1))
oriConfigFileTableEntry.setIndexNames((0,_E,_Ar))
if mibBuilder.loadTexts:oriConfigFileTableEntry.setStatus(_A)
_OriConfigFileTableIndex_Type=Integer32
_OriConfigFileTableIndex_Object=MibTableColumn
oriConfigFileTableIndex=_OriConfigFileTableIndex_Object((1,3,6,1,4,1,11898,2,1,23,2,1,1),_OriConfigFileTableIndex_Type())
oriConfigFileTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriConfigFileTableIndex.setStatus(_A)
_OriConfigFileName_Type=DisplayString
_OriConfigFileName_Object=MibTableColumn
oriConfigFileName=_OriConfigFileName_Object((1,3,6,1,4,1,11898,2,1,23,2,1,2),_OriConfigFileName_Type())
oriConfigFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriConfigFileName.setStatus(_A)
class _OriConfigFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3)))
_OriConfigFileStatus_Type.__name__=_D
_OriConfigFileStatus_Object=MibTableColumn
oriConfigFileStatus=_OriConfigFileStatus_Object((1,3,6,1,4,1,11898,2,1,23,2,1,3),_OriConfigFileStatus_Type())
oriConfigFileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriConfigFileStatus.setStatus(_A)
_OriConfigSaveFile_Type=DisplayString
_OriConfigSaveFile_Object=MibScalar
oriConfigSaveFile=_OriConfigSaveFile_Object((1,3,6,1,4,1,11898,2,1,23,3),_OriConfigSaveFile_Type())
oriConfigSaveFile.setMaxAccess(_B)
if mibBuilder.loadTexts:oriConfigSaveFile.setStatus(_A)
class _OriConfigSaveKnownGood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('saveKnownGood',1))
_OriConfigSaveKnownGood_Type.__name__=_D
_OriConfigSaveKnownGood_Object=MibScalar
oriConfigSaveKnownGood=_OriConfigSaveKnownGood_Object((1,3,6,1,4,1,11898,2,1,23,4),_OriConfigSaveKnownGood_Type())
oriConfigSaveKnownGood.setMaxAccess(_B)
if mibBuilder.loadTexts:oriConfigSaveKnownGood.setStatus(_A)
_OrinocoDNS_ObjectIdentity=ObjectIdentity
orinocoDNS=_OrinocoDNS_ObjectIdentity((1,3,6,1,4,1,11898,2,1,24))
class _OriDNSRedirectStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriDNSRedirectStatus_Type.__name__=_D
_OriDNSRedirectStatus_Object=MibScalar
oriDNSRedirectStatus=_OriDNSRedirectStatus_Object((1,3,6,1,4,1,11898,2,1,24,1),_OriDNSRedirectStatus_Type())
oriDNSRedirectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSRedirectStatus.setStatus(_A)
class _OriDNSRedirectMaxResponseWaitTime_Type(Integer32):defaultValue=10
_OriDNSRedirectMaxResponseWaitTime_Type.__name__=_D
_OriDNSRedirectMaxResponseWaitTime_Object=MibScalar
oriDNSRedirectMaxResponseWaitTime=_OriDNSRedirectMaxResponseWaitTime_Object((1,3,6,1,4,1,11898,2,1,24,2),_OriDNSRedirectMaxResponseWaitTime_Type())
oriDNSRedirectMaxResponseWaitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSRedirectMaxResponseWaitTime.setStatus(_A)
_OriDNSPrimaryDNSIPAddress_Type=IpAddress
_OriDNSPrimaryDNSIPAddress_Object=MibScalar
oriDNSPrimaryDNSIPAddress=_OriDNSPrimaryDNSIPAddress_Object((1,3,6,1,4,1,11898,2,1,24,3),_OriDNSPrimaryDNSIPAddress_Type())
oriDNSPrimaryDNSIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSPrimaryDNSIPAddress.setStatus(_A)
_OriDNSSecondaryDNSIPAddress_Type=IpAddress
_OriDNSSecondaryDNSIPAddress_Object=MibScalar
oriDNSSecondaryDNSIPAddress=_OriDNSSecondaryDNSIPAddress_Object((1,3,6,1,4,1,11898,2,1,24,4),_OriDNSSecondaryDNSIPAddress_Type())
oriDNSSecondaryDNSIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSSecondaryDNSIPAddress.setStatus(_A)
_OrinocoDNSClient_ObjectIdentity=ObjectIdentity
orinocoDNSClient=_OrinocoDNSClient_ObjectIdentity((1,3,6,1,4,1,11898,2,1,24,5))
class _OriDNSClientStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriDNSClientStatus_Type.__name__=_D
_OriDNSClientStatus_Object=MibScalar
oriDNSClientStatus=_OriDNSClientStatus_Object((1,3,6,1,4,1,11898,2,1,24,5,1),_OriDNSClientStatus_Type())
oriDNSClientStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSClientStatus.setStatus(_A)
_OriDNSClientPrimaryServerIPAddress_Type=IpAddress
_OriDNSClientPrimaryServerIPAddress_Object=MibScalar
oriDNSClientPrimaryServerIPAddress=_OriDNSClientPrimaryServerIPAddress_Object((1,3,6,1,4,1,11898,2,1,24,5,2),_OriDNSClientPrimaryServerIPAddress_Type())
oriDNSClientPrimaryServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSClientPrimaryServerIPAddress.setStatus(_A)
_OriDNSClientSecondaryServerIPAddress_Type=IpAddress
_OriDNSClientSecondaryServerIPAddress_Object=MibScalar
oriDNSClientSecondaryServerIPAddress=_OriDNSClientSecondaryServerIPAddress_Object((1,3,6,1,4,1,11898,2,1,24,5,3),_OriDNSClientSecondaryServerIPAddress_Type())
oriDNSClientSecondaryServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSClientSecondaryServerIPAddress.setStatus(_A)
_OriDNSClientDefaultDomainName_Type=DisplayString
_OriDNSClientDefaultDomainName_Object=MibScalar
oriDNSClientDefaultDomainName=_OriDNSClientDefaultDomainName_Object((1,3,6,1,4,1,11898,2,1,24,5,4),_OriDNSClientDefaultDomainName_Type())
oriDNSClientDefaultDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDNSClientDefaultDomainName.setStatus(_A)
_OrinocoAOL_ObjectIdentity=ObjectIdentity
orinocoAOL=_OrinocoAOL_ObjectIdentity((1,3,6,1,4,1,11898,2,1,25))
class _OriAOLNATALGStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriAOLNATALGStatus_Type.__name__=_D
_OriAOLNATALGStatus_Object=MibScalar
oriAOLNATALGStatus=_OriAOLNATALGStatus_Object((1,3,6,1,4,1,11898,2,1,25,1),_OriAOLNATALGStatus_Type())
oriAOLNATALGStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriAOLNATALGStatus.setStatus(_A)
_OrinocoNAT_ObjectIdentity=ObjectIdentity
orinocoNAT=_OrinocoNAT_ObjectIdentity((1,3,6,1,4,1,11898,2,1,26))
class _OriNATStatus_Type(ObjStatus):defaultValue=2
_OriNATStatus_Type.__name__=_J
_OriNATStatus_Object=MibScalar
oriNATStatus=_OriNATStatus_Object((1,3,6,1,4,1,11898,2,1,26,1),_OriNATStatus_Type())
oriNATStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStatus.setStatus(_A)
_OriNATType_Type=Integer32
_OriNATType_Object=MibScalar
oriNATType=_OriNATType_Object((1,3,6,1,4,1,11898,2,1,26,2),_OriNATType_Type())
oriNATType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATType.setStatus(_A)
class _OriNATStaticBindStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriNATStaticBindStatus_Type.__name__=_D
_OriNATStaticBindStatus_Object=MibScalar
oriNATStaticBindStatus=_OriNATStaticBindStatus_Object((1,3,6,1,4,1,11898,2,1,26,3),_OriNATStaticBindStatus_Type())
oriNATStaticBindStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticBindStatus.setStatus(_A)
_OriNATPublicIPAddress_Type=IpAddress
_OriNATPublicIPAddress_Object=MibScalar
oriNATPublicIPAddress=_OriNATPublicIPAddress_Object((1,3,6,1,4,1,11898,2,1,26,4),_OriNATPublicIPAddress_Type())
oriNATPublicIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriNATPublicIPAddress.setStatus(_A)
_OriNATStaticIPBindTable_Object=MibTable
oriNATStaticIPBindTable=_OriNATStaticIPBindTable_Object((1,3,6,1,4,1,11898,2,1,26,5))
if mibBuilder.loadTexts:oriNATStaticIPBindTable.setStatus(_A)
_OriNATStaticIPBindTableEntry_Object=MibTableRow
oriNATStaticIPBindTableEntry=_OriNATStaticIPBindTableEntry_Object((1,3,6,1,4,1,11898,2,1,26,5,1))
oriNATStaticIPBindTableEntry.setIndexNames((0,_E,_As))
if mibBuilder.loadTexts:oriNATStaticIPBindTableEntry.setStatus(_A)
_OriNATStaticIPBindTableIndex_Type=Integer32
_OriNATStaticIPBindTableIndex_Object=MibTableColumn
oriNATStaticIPBindTableIndex=_OriNATStaticIPBindTableIndex_Object((1,3,6,1,4,1,11898,2,1,26,5,1,1),_OriNATStaticIPBindTableIndex_Type())
oriNATStaticIPBindTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriNATStaticIPBindTableIndex.setStatus(_A)
_OriNATStaticIPBindLocalAddress_Type=IpAddress
_OriNATStaticIPBindLocalAddress_Object=MibTableColumn
oriNATStaticIPBindLocalAddress=_OriNATStaticIPBindLocalAddress_Object((1,3,6,1,4,1,11898,2,1,26,5,1,2),_OriNATStaticIPBindLocalAddress_Type())
oriNATStaticIPBindLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticIPBindLocalAddress.setStatus(_A)
_OriNATStaticIPBindRemoteAddress_Type=IpAddress
_OriNATStaticIPBindRemoteAddress_Object=MibTableColumn
oriNATStaticIPBindRemoteAddress=_OriNATStaticIPBindRemoteAddress_Object((1,3,6,1,4,1,11898,2,1,26,5,1,3),_OriNATStaticIPBindRemoteAddress_Type())
oriNATStaticIPBindRemoteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticIPBindRemoteAddress.setStatus(_A)
class _OriNATStaticIPBindTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriNATStaticIPBindTableEntryStatus_Type.__name__=_D
_OriNATStaticIPBindTableEntryStatus_Object=MibTableColumn
oriNATStaticIPBindTableEntryStatus=_OriNATStaticIPBindTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,26,5,1,4),_OriNATStaticIPBindTableEntryStatus_Type())
oriNATStaticIPBindTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticIPBindTableEntryStatus.setStatus(_A)
_OriNATStaticPortBindTable_Object=MibTable
oriNATStaticPortBindTable=_OriNATStaticPortBindTable_Object((1,3,6,1,4,1,11898,2,1,26,6))
if mibBuilder.loadTexts:oriNATStaticPortBindTable.setStatus(_A)
_OriNATStaticPortBindTableEntry_Object=MibTableRow
oriNATStaticPortBindTableEntry=_OriNATStaticPortBindTableEntry_Object((1,3,6,1,4,1,11898,2,1,26,6,1))
oriNATStaticPortBindTableEntry.setIndexNames((0,_E,_At))
if mibBuilder.loadTexts:oriNATStaticPortBindTableEntry.setStatus(_A)
_OriNATStaticPortBindTableIndex_Type=Integer32
_OriNATStaticPortBindTableIndex_Object=MibTableColumn
oriNATStaticPortBindTableIndex=_OriNATStaticPortBindTableIndex_Object((1,3,6,1,4,1,11898,2,1,26,6,1,1),_OriNATStaticPortBindTableIndex_Type())
oriNATStaticPortBindTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriNATStaticPortBindTableIndex.setStatus(_A)
_OriNATStaticPortBindLocalAddress_Type=IpAddress
_OriNATStaticPortBindLocalAddress_Object=MibTableColumn
oriNATStaticPortBindLocalAddress=_OriNATStaticPortBindLocalAddress_Object((1,3,6,1,4,1,11898,2,1,26,6,1,2),_OriNATStaticPortBindLocalAddress_Type())
oriNATStaticPortBindLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticPortBindLocalAddress.setStatus(_A)
_OriNATStaticPortBindStartPortNumber_Type=Integer32
_OriNATStaticPortBindStartPortNumber_Object=MibTableColumn
oriNATStaticPortBindStartPortNumber=_OriNATStaticPortBindStartPortNumber_Object((1,3,6,1,4,1,11898,2,1,26,6,1,3),_OriNATStaticPortBindStartPortNumber_Type())
oriNATStaticPortBindStartPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticPortBindStartPortNumber.setStatus(_A)
_OriNATStaticPortBindEndPortNumber_Type=Integer32
_OriNATStaticPortBindEndPortNumber_Object=MibTableColumn
oriNATStaticPortBindEndPortNumber=_OriNATStaticPortBindEndPortNumber_Object((1,3,6,1,4,1,11898,2,1,26,6,1,4),_OriNATStaticPortBindEndPortNumber_Type())
oriNATStaticPortBindEndPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticPortBindEndPortNumber.setStatus(_A)
class _OriNATStaticPortBindPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('udp',2),(_o,3)))
_OriNATStaticPortBindPortType_Type.__name__=_D
_OriNATStaticPortBindPortType_Object=MibTableColumn
oriNATStaticPortBindPortType=_OriNATStaticPortBindPortType_Object((1,3,6,1,4,1,11898,2,1,26,6,1,5),_OriNATStaticPortBindPortType_Type())
oriNATStaticPortBindPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticPortBindPortType.setStatus(_A)
class _OriNATStaticPortBindTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriNATStaticPortBindTableEntryStatus_Type.__name__=_D
_OriNATStaticPortBindTableEntryStatus_Object=MibTableColumn
oriNATStaticPortBindTableEntryStatus=_OriNATStaticPortBindTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,26,6,1,6),_OriNATStaticPortBindTableEntryStatus_Type())
oriNATStaticPortBindTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriNATStaticPortBindTableEntryStatus.setStatus(_A)
_OrinocoSpectraLink_ObjectIdentity=ObjectIdentity
orinocoSpectraLink=_OrinocoSpectraLink_ObjectIdentity((1,3,6,1,4,1,11898,2,1,29))
class _OriSpectraLinkStatus_Type(ObjStatus):defaultValue=2
_OriSpectraLinkStatus_Type.__name__=_J
_OriSpectraLinkStatus_Object=MibScalar
oriSpectraLinkStatus=_OriSpectraLinkStatus_Object((1,3,6,1,4,1,11898,2,1,29,1),_OriSpectraLinkStatus_Type())
oriSpectraLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSpectraLinkStatus.setStatus(_A)
class _OriSpectraLinkLegacyDeviceSupport_Type(ObjStatus):defaultValue=2
_OriSpectraLinkLegacyDeviceSupport_Type.__name__=_J
_OriSpectraLinkLegacyDeviceSupport_Object=MibScalar
oriSpectraLinkLegacyDeviceSupport=_OriSpectraLinkLegacyDeviceSupport_Object((1,3,6,1,4,1,11898,2,1,29,2),_OriSpectraLinkLegacyDeviceSupport_Type())
oriSpectraLinkLegacyDeviceSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSpectraLinkLegacyDeviceSupport.setStatus(_A)
_OrinocoVLAN_ObjectIdentity=ObjectIdentity
orinocoVLAN=_OrinocoVLAN_ObjectIdentity((1,3,6,1,4,1,11898,2,1,30))
class _OriVLANStatus_Type(ObjStatus):defaultValue=2
_OriVLANStatus_Type.__name__=_J
_OriVLANStatus_Object=MibScalar
oriVLANStatus=_OriVLANStatus_Object((1,3,6,1,4,1,11898,2,1,30,1),_OriVLANStatus_Type())
oriVLANStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriVLANStatus.setStatus(_A)
class _OriVLANMgmtIdentifier_Type(VlanId):defaultValue=-1
_OriVLANMgmtIdentifier_Type.__name__=_a
_OriVLANMgmtIdentifier_Object=MibScalar
oriVLANMgmtIdentifier=_OriVLANMgmtIdentifier_Object((1,3,6,1,4,1,11898,2,1,30,2),_OriVLANMgmtIdentifier_Type())
oriVLANMgmtIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:oriVLANMgmtIdentifier.setStatus(_A)
_OriVLANIDTable_Object=MibTable
oriVLANIDTable=_OriVLANIDTable_Object((1,3,6,1,4,1,11898,2,1,30,3))
if mibBuilder.loadTexts:oriVLANIDTable.setStatus(_H)
_OriVLANIDTableEntry_Object=MibTableRow
oriVLANIDTableEntry=_OriVLANIDTableEntry_Object((1,3,6,1,4,1,11898,2,1,30,3,1))
oriVLANIDTableEntry.setIndexNames((0,_E,_Au))
if mibBuilder.loadTexts:oriVLANIDTableEntry.setStatus(_H)
_OriVLANIDTableIndex_Type=Integer32
_OriVLANIDTableIndex_Object=MibTableColumn
oriVLANIDTableIndex=_OriVLANIDTableIndex_Object((1,3,6,1,4,1,11898,2,1,30,3,1,1),_OriVLANIDTableIndex_Type())
oriVLANIDTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriVLANIDTableIndex.setStatus(_H)
class _OriVLANIDTableIdentifier_Type(VlanId):defaultValue=0
_OriVLANIDTableIdentifier_Type.__name__=_a
_OriVLANIDTableIdentifier_Object=MibTableColumn
oriVLANIDTableIdentifier=_OriVLANIDTableIdentifier_Object((1,3,6,1,4,1,11898,2,1,30,3,1,2),_OriVLANIDTableIdentifier_Type())
oriVLANIDTableIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:oriVLANIDTableIdentifier.setStatus(_H)
_OrinocoDMZ_ObjectIdentity=ObjectIdentity
orinocoDMZ=_OrinocoDMZ_ObjectIdentity((1,3,6,1,4,1,11898,2,1,31))
_OriDMZHostTable_Object=MibTable
oriDMZHostTable=_OriDMZHostTable_Object((1,3,6,1,4,1,11898,2,1,31,1))
if mibBuilder.loadTexts:oriDMZHostTable.setStatus(_A)
_OriDMZHostTableEntry_Object=MibTableRow
oriDMZHostTableEntry=_OriDMZHostTableEntry_Object((1,3,6,1,4,1,11898,2,1,31,1,1))
oriDMZHostTableEntry.setIndexNames((0,_E,_Av))
if mibBuilder.loadTexts:oriDMZHostTableEntry.setStatus(_A)
_OriDMZHostTableIndex_Type=Integer32
_OriDMZHostTableIndex_Object=MibTableColumn
oriDMZHostTableIndex=_OriDMZHostTableIndex_Object((1,3,6,1,4,1,11898,2,1,31,1,1,1),_OriDMZHostTableIndex_Type())
oriDMZHostTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriDMZHostTableIndex.setStatus(_A)
_OriDMZHostTableHostIP_Type=IpAddress
_OriDMZHostTableHostIP_Object=MibTableColumn
oriDMZHostTableHostIP=_OriDMZHostTableHostIP_Object((1,3,6,1,4,1,11898,2,1,31,1,1,2),_OriDMZHostTableHostIP_Type())
oriDMZHostTableHostIP.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDMZHostTableHostIP.setStatus(_A)
_OriDMZHostTableComment_Type=DisplayString
_OriDMZHostTableComment_Object=MibTableColumn
oriDMZHostTableComment=_OriDMZHostTableComment_Object((1,3,6,1,4,1,11898,2,1,31,1,1,3),_OriDMZHostTableComment_Type())
oriDMZHostTableComment.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDMZHostTableComment.setStatus(_A)
class _OriDMZHostTableEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_L,3),(_M,4)))
_OriDMZHostTableEntryStatus_Type.__name__=_D
_OriDMZHostTableEntryStatus_Object=MibTableColumn
oriDMZHostTableEntryStatus=_OriDMZHostTableEntryStatus_Object((1,3,6,1,4,1,11898,2,1,31,1,1,4),_OriDMZHostTableEntryStatus_Type())
oriDMZHostTableEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriDMZHostTableEntryStatus.setStatus(_A)
_OrinocoOEM_ObjectIdentity=ObjectIdentity
orinocoOEM=_OrinocoOEM_ObjectIdentity((1,3,6,1,4,1,11898,2,1,32))
_OriOEMName_Type=DisplayString
_OriOEMName_Object=MibScalar
oriOEMName=_OriOEMName_Object((1,3,6,1,4,1,11898,2,1,32,1),_OriOEMName_Type())
oriOEMName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriOEMName.setStatus(_A)
_OriOEMHomeUrl_Type=DisplayString
_OriOEMHomeUrl_Object=MibScalar
oriOEMHomeUrl=_OriOEMHomeUrl_Object((1,3,6,1,4,1,11898,2,1,32,2),_OriOEMHomeUrl_Type())
oriOEMHomeUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:oriOEMHomeUrl.setStatus(_A)
_OriOEMProductName_Type=DisplayString
_OriOEMProductName_Object=MibScalar
oriOEMProductName=_OriOEMProductName_Object((1,3,6,1,4,1,11898,2,1,32,3),_OriOEMProductName_Type())
oriOEMProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriOEMProductName.setStatus(_A)
_OriOEMProductModel_Type=DisplayString
_OriOEMProductModel_Object=MibScalar
oriOEMProductModel=_OriOEMProductModel_Object((1,3,6,1,4,1,11898,2,1,32,4),_OriOEMProductModel_Type())
oriOEMProductModel.setMaxAccess(_C)
if mibBuilder.loadTexts:oriOEMProductModel.setStatus(_A)
_OriOEMLogoImageFile_Type=DisplayString
_OriOEMLogoImageFile_Object=MibScalar
oriOEMLogoImageFile=_OriOEMLogoImageFile_Object((1,3,6,1,4,1,11898,2,1,32,5),_OriOEMLogoImageFile_Type())
oriOEMLogoImageFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oriOEMLogoImageFile.setStatus(_A)
_OriOEMNoNavLogoImageFile_Type=DisplayString
_OriOEMNoNavLogoImageFile_Object=MibScalar
oriOEMNoNavLogoImageFile=_OriOEMNoNavLogoImageFile_Object((1,3,6,1,4,1,11898,2,1,32,6),_OriOEMNoNavLogoImageFile_Type())
oriOEMNoNavLogoImageFile.setMaxAccess(_C)
if mibBuilder.loadTexts:oriOEMNoNavLogoImageFile.setStatus(_A)
_OrinocoStationStatistics_ObjectIdentity=ObjectIdentity
orinocoStationStatistics=_OrinocoStationStatistics_ObjectIdentity((1,3,6,1,4,1,11898,2,1,33))
_OriStationStatTable_Object=MibTable
oriStationStatTable=_OriStationStatTable_Object((1,3,6,1,4,1,11898,2,1,33,1))
if mibBuilder.loadTexts:oriStationStatTable.setStatus(_A)
_OriStationStatTableEntry_Object=MibTableRow
oriStationStatTableEntry=_OriStationStatTableEntry_Object((1,3,6,1,4,1,11898,2,1,33,1,1))
oriStationStatTableEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:oriStationStatTableEntry.setStatus(_A)
class _OriStationStatTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_OriStationStatTableIndex_Type.__name__=_D
_OriStationStatTableIndex_Object=MibTableColumn
oriStationStatTableIndex=_OriStationStatTableIndex_Object((1,3,6,1,4,1,11898,2,1,33,1,1,1),_OriStationStatTableIndex_Type())
oriStationStatTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableIndex.setStatus(_A)
_OriStationStatTableMACAddress_Type=MacAddress
_OriStationStatTableMACAddress_Object=MibTableColumn
oriStationStatTableMACAddress=_OriStationStatTableMACAddress_Object((1,3,6,1,4,1,11898,2,1,33,1,1,2),_OriStationStatTableMACAddress_Type())
oriStationStatTableMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableMACAddress.setStatus(_A)
_OriStationStatTableIPAddress_Type=IpAddress
_OriStationStatTableIPAddress_Object=MibTableColumn
oriStationStatTableIPAddress=_OriStationStatTableIPAddress_Object((1,3,6,1,4,1,11898,2,1,33,1,1,3),_OriStationStatTableIPAddress_Type())
oriStationStatTableIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableIPAddress.setStatus(_A)
_OriStationStatTableInterface_Type=Integer32
_OriStationStatTableInterface_Object=MibTableColumn
oriStationStatTableInterface=_OriStationStatTableInterface_Object((1,3,6,1,4,1,11898,2,1,33,1,1,4),_OriStationStatTableInterface_Type())
oriStationStatTableInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableInterface.setStatus(_A)
_OriStationStatTableName_Type=DisplayString
_OriStationStatTableName_Object=MibTableColumn
oriStationStatTableName=_OriStationStatTableName_Object((1,3,6,1,4,1,11898,2,1,33,1,1,5),_OriStationStatTableName_Type())
oriStationStatTableName.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableName.setStatus(_A)
class _OriStationStatTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sta',1),('wds',2),('worpBase',3),('worpSatellite',4),('norc',5)))
_OriStationStatTableType_Type.__name__=_D
_OriStationStatTableType_Object=MibTableColumn
oriStationStatTableType=_OriStationStatTableType_Object((1,3,6,1,4,1,11898,2,1,33,1,1,6),_OriStationStatTableType_Type())
oriStationStatTableType.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableType.setStatus(_A)
class _OriStationStatTableMACProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ieee802dot11',1),('ieee802dot11a',2),('ieee802dot11b',3),('worp',4),('ieee802dot11g',5)))
_OriStationStatTableMACProtocol_Type.__name__=_D
_OriStationStatTableMACProtocol_Object=MibTableColumn
oriStationStatTableMACProtocol=_OriStationStatTableMACProtocol_Object((1,3,6,1,4,1,11898,2,1,33,1,1,7),_OriStationStatTableMACProtocol_Type())
oriStationStatTableMACProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableMACProtocol.setStatus(_A)
class _OriStationStatTableAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),('testing',3)))
_OriStationStatTableAdminStatus_Type.__name__=_D
_OriStationStatTableAdminStatus_Object=MibTableColumn
oriStationStatTableAdminStatus=_OriStationStatTableAdminStatus_Object((1,3,6,1,4,1,11898,2,1,33,1,1,8),_OriStationStatTableAdminStatus_Type())
oriStationStatTableAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableAdminStatus.setStatus(_A)
class _OriStationStatTableOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),('testing',3)))
_OriStationStatTableOperStatus_Type.__name__=_D
_OriStationStatTableOperStatus_Object=MibTableColumn
oriStationStatTableOperStatus=_OriStationStatTableOperStatus_Object((1,3,6,1,4,1,11898,2,1,33,1,1,9),_OriStationStatTableOperStatus_Type())
oriStationStatTableOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableOperStatus.setStatus(_A)
_OriStationStatTableLastChange_Type=TimeTicks
_OriStationStatTableLastChange_Object=MibTableColumn
oriStationStatTableLastChange=_OriStationStatTableLastChange_Object((1,3,6,1,4,1,11898,2,1,33,1,1,10),_OriStationStatTableLastChange_Type())
oriStationStatTableLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableLastChange.setStatus(_A)
class _OriStationStatTableLastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_s,1),('registering',2),('authenticating',3),('registered',4),('timeout',5),('aborded',6),('rejected',7),('linktest',8)))
_OriStationStatTableLastState_Type.__name__=_D
_OriStationStatTableLastState_Object=MibTableColumn
oriStationStatTableLastState=_OriStationStatTableLastState_Object((1,3,6,1,4,1,11898,2,1,33,1,1,11),_OriStationStatTableLastState_Type())
oriStationStatTableLastState.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableLastState.setStatus(_A)
_OriStationStatTableInOctets_Type=Counter32
_OriStationStatTableInOctets_Object=MibTableColumn
oriStationStatTableInOctets=_OriStationStatTableInOctets_Object((1,3,6,1,4,1,11898,2,1,33,1,1,12),_OriStationStatTableInOctets_Type())
oriStationStatTableInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableInOctets.setStatus(_A)
_OriStationStatTableInUcastPkts_Type=Counter32
_OriStationStatTableInUcastPkts_Object=MibTableColumn
oriStationStatTableInUcastPkts=_OriStationStatTableInUcastPkts_Object((1,3,6,1,4,1,11898,2,1,33,1,1,13),_OriStationStatTableInUcastPkts_Type())
oriStationStatTableInUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableInUcastPkts.setStatus(_A)
_OriStationStatTableInNUcastPkts_Type=Counter32
_OriStationStatTableInNUcastPkts_Object=MibTableColumn
oriStationStatTableInNUcastPkts=_OriStationStatTableInNUcastPkts_Object((1,3,6,1,4,1,11898,2,1,33,1,1,14),_OriStationStatTableInNUcastPkts_Type())
oriStationStatTableInNUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableInNUcastPkts.setStatus(_A)
_OriStationStatTableInDiscards_Type=Counter32
_OriStationStatTableInDiscards_Object=MibTableColumn
oriStationStatTableInDiscards=_OriStationStatTableInDiscards_Object((1,3,6,1,4,1,11898,2,1,33,1,1,15),_OriStationStatTableInDiscards_Type())
oriStationStatTableInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableInDiscards.setStatus(_A)
_OriStationStatTableOutOctets_Type=Counter32
_OriStationStatTableOutOctets_Object=MibTableColumn
oriStationStatTableOutOctets=_OriStationStatTableOutOctets_Object((1,3,6,1,4,1,11898,2,1,33,1,1,16),_OriStationStatTableOutOctets_Type())
oriStationStatTableOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableOutOctets.setStatus(_A)
_OriStationStatTableOutUcastPkts_Type=Counter32
_OriStationStatTableOutUcastPkts_Object=MibTableColumn
oriStationStatTableOutUcastPkts=_OriStationStatTableOutUcastPkts_Object((1,3,6,1,4,1,11898,2,1,33,1,1,17),_OriStationStatTableOutUcastPkts_Type())
oriStationStatTableOutUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableOutUcastPkts.setStatus(_A)
_OriStationStatTableOutNUcastPkts_Type=Counter32
_OriStationStatTableOutNUcastPkts_Object=MibTableColumn
oriStationStatTableOutNUcastPkts=_OriStationStatTableOutNUcastPkts_Object((1,3,6,1,4,1,11898,2,1,33,1,1,18),_OriStationStatTableOutNUcastPkts_Type())
oriStationStatTableOutNUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableOutNUcastPkts.setStatus(_A)
_OriStationStatTableOutDiscards_Type=Counter32
_OriStationStatTableOutDiscards_Object=MibTableColumn
oriStationStatTableOutDiscards=_OriStationStatTableOutDiscards_Object((1,3,6,1,4,1,11898,2,1,33,1,1,19),_OriStationStatTableOutDiscards_Type())
oriStationStatTableOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableOutDiscards.setStatus(_A)
class _OriStationStatTableInSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriStationStatTableInSignal_Type.__name__=_D
_OriStationStatTableInSignal_Object=MibTableColumn
oriStationStatTableInSignal=_OriStationStatTableInSignal_Object((1,3,6,1,4,1,11898,2,1,33,1,1,20),_OriStationStatTableInSignal_Type())
oriStationStatTableInSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableInSignal.setStatus(_A)
class _OriStationStatTableInNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriStationStatTableInNoise_Type.__name__=_D
_OriStationStatTableInNoise_Object=MibTableColumn
oriStationStatTableInNoise=_OriStationStatTableInNoise_Object((1,3,6,1,4,1,11898,2,1,33,1,1,21),_OriStationStatTableInNoise_Type())
oriStationStatTableInNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableInNoise.setStatus(_A)
class _OriStationStatTableRemoteSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriStationStatTableRemoteSignal_Type.__name__=_D
_OriStationStatTableRemoteSignal_Object=MibTableColumn
oriStationStatTableRemoteSignal=_OriStationStatTableRemoteSignal_Object((1,3,6,1,4,1,11898,2,1,33,1,1,22),_OriStationStatTableRemoteSignal_Type())
oriStationStatTableRemoteSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableRemoteSignal.setStatus(_A)
class _OriStationStatTableRemoteNoise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-102,-10))
_OriStationStatTableRemoteNoise_Type.__name__=_D
_OriStationStatTableRemoteNoise_Object=MibTableColumn
oriStationStatTableRemoteNoise=_OriStationStatTableRemoteNoise_Object((1,3,6,1,4,1,11898,2,1,33,1,1,23),_OriStationStatTableRemoteNoise_Type())
oriStationStatTableRemoteNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableRemoteNoise.setStatus(_A)
_OriStationStatTableLastInPktTime_Type=TimeTicks
_OriStationStatTableLastInPktTime_Object=MibTableColumn
oriStationStatTableLastInPktTime=_OriStationStatTableLastInPktTime_Object((1,3,6,1,4,1,11898,2,1,33,1,1,24),_OriStationStatTableLastInPktTime_Type())
oriStationStatTableLastInPktTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatTableLastInPktTime.setStatus(_A)
class _OriStationStatStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriStationStatStatus_Type.__name__=_D
_OriStationStatStatus_Object=MibScalar
oriStationStatStatus=_OriStationStatStatus_Object((1,3,6,1,4,1,11898,2,1,33,2),_OriStationStatStatus_Type())
oriStationStatStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriStationStatStatus.setStatus(_A)
_OriStationStatNumberOfClients_Type=Counter32
_OriStationStatNumberOfClients_Object=MibScalar
oriStationStatNumberOfClients=_OriStationStatNumberOfClients_Object((1,3,6,1,4,1,11898,2,1,33,3),_OriStationStatNumberOfClients_Type())
oriStationStatNumberOfClients.setMaxAccess(_C)
if mibBuilder.loadTexts:oriStationStatNumberOfClients.setStatus(_A)
_OrinocoSNTP_ObjectIdentity=ObjectIdentity
orinocoSNTP=_OrinocoSNTP_ObjectIdentity((1,3,6,1,4,1,11898,2,1,34))
class _OriSNTPStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_OriSNTPStatus_Type.__name__=_D
_OriSNTPStatus_Object=MibScalar
oriSNTPStatus=_OriSNTPStatus_Object((1,3,6,1,4,1,11898,2,1,34,1),_OriSNTPStatus_Type())
oriSNTPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPStatus.setStatus(_A)
_OriSNTPPrimaryServerNameOrIPAddress_Type=DisplayString
_OriSNTPPrimaryServerNameOrIPAddress_Object=MibScalar
oriSNTPPrimaryServerNameOrIPAddress=_OriSNTPPrimaryServerNameOrIPAddress_Object((1,3,6,1,4,1,11898,2,1,34,2),_OriSNTPPrimaryServerNameOrIPAddress_Type())
oriSNTPPrimaryServerNameOrIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPPrimaryServerNameOrIPAddress.setStatus(_A)
_OriSNTPSecondaryServerNameOrIPAddress_Type=DisplayString
_OriSNTPSecondaryServerNameOrIPAddress_Object=MibScalar
oriSNTPSecondaryServerNameOrIPAddress=_OriSNTPSecondaryServerNameOrIPAddress_Object((1,3,6,1,4,1,11898,2,1,34,3),_OriSNTPSecondaryServerNameOrIPAddress_Type())
oriSNTPSecondaryServerNameOrIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPSecondaryServerNameOrIPAddress.setStatus(_A)
class _OriSNTPTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41)));namedValues=NamedValues(*(('dateline',1),('samoa',2),('hawaii',3),('alaska',4),('pacific-us',5),('mountain-us',6),('arizona',7),('central-us',8),('mexico-city',9),('eastern-us',10),('indiana',11),('atlantic-canada',12),('santiago',13),('newfoundland',14),('brasilia',15),('buenos-aires',16),('mid-atlantic',17),('azores',18),('london',19),('western-europe',20),('eastern-europe',21),('cairo',22),('russia-iraq',23),('iran',24),('arabian',25),('afghanistan',26),('pakistan',27),('india',28),('bangladesh',29),('burma',30),('bangkok',31),('australia-wt',32),('hong-kong',33),('beijing',34),('japan-korea',35),('australia-ct',36),('australia-et',37),('central-pacific',38),('new-zealand',39),('tonga',40),('western-samoa',41)))
_OriSNTPTimeZone_Type.__name__=_D
_OriSNTPTimeZone_Object=MibScalar
oriSNTPTimeZone=_OriSNTPTimeZone_Object((1,3,6,1,4,1,11898,2,1,34,4),_OriSNTPTimeZone_Type())
oriSNTPTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPTimeZone.setStatus(_A)
_OriSNTPDateAndTime_Type=DisplayString
_OriSNTPDateAndTime_Object=MibScalar
oriSNTPDateAndTime=_OriSNTPDateAndTime_Object((1,3,6,1,4,1,11898,2,1,34,5),_OriSNTPDateAndTime_Type())
oriSNTPDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oriSNTPDateAndTime.setStatus(_A)
class _OriSNTPDayLightSavingTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('plus-two',1),('plus-one',2),('unchanged',3),('minus-one',4),('minus-two',5)))
_OriSNTPDayLightSavingTime_Type.__name__=_D
_OriSNTPDayLightSavingTime_Object=MibScalar
oriSNTPDayLightSavingTime=_OriSNTPDayLightSavingTime_Object((1,3,6,1,4,1,11898,2,1,34,6),_OriSNTPDayLightSavingTime_Type())
oriSNTPDayLightSavingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPDayLightSavingTime.setStatus(_A)
_OriSNTPYear_Type=Integer32
_OriSNTPYear_Object=MibScalar
oriSNTPYear=_OriSNTPYear_Object((1,3,6,1,4,1,11898,2,1,34,7),_OriSNTPYear_Type())
oriSNTPYear.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPYear.setStatus(_A)
class _OriSNTPMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_OriSNTPMonth_Type.__name__=_D
_OriSNTPMonth_Object=MibScalar
oriSNTPMonth=_OriSNTPMonth_Object((1,3,6,1,4,1,11898,2,1,34,8),_OriSNTPMonth_Type())
oriSNTPMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPMonth.setStatus(_A)
class _OriSNTPDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_OriSNTPDay_Type.__name__=_D
_OriSNTPDay_Object=MibScalar
oriSNTPDay=_OriSNTPDay_Object((1,3,6,1,4,1,11898,2,1,34,9),_OriSNTPDay_Type())
oriSNTPDay.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPDay.setStatus(_A)
class _OriSNTPHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_OriSNTPHour_Type.__name__=_D
_OriSNTPHour_Object=MibScalar
oriSNTPHour=_OriSNTPHour_Object((1,3,6,1,4,1,11898,2,1,34,10),_OriSNTPHour_Type())
oriSNTPHour.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPHour.setStatus(_A)
class _OriSNTPMinutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_OriSNTPMinutes_Type.__name__=_D
_OriSNTPMinutes_Object=MibScalar
oriSNTPMinutes=_OriSNTPMinutes_Object((1,3,6,1,4,1,11898,2,1,34,11),_OriSNTPMinutes_Type())
oriSNTPMinutes.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPMinutes.setStatus(_A)
class _OriSNTPSeconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_OriSNTPSeconds_Type.__name__=_D
_OriSNTPSeconds_Object=MibScalar
oriSNTPSeconds=_OriSNTPSeconds_Object((1,3,6,1,4,1,11898,2,1,34,12),_OriSNTPSeconds_Type())
oriSNTPSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:oriSNTPSeconds.setStatus(_A)
_OrinocoNotifications_ObjectIdentity=ObjectIdentity
orinocoNotifications=_OrinocoNotifications_ObjectIdentity((1,3,6,1,4,1,11898,2,2))
_OrinocoConformance_ObjectIdentity=ObjectIdentity
orinocoConformance=_OrinocoConformance_ObjectIdentity((1,3,6,1,4,1,11898,2,3))
_OrinocoGroups_ObjectIdentity=ObjectIdentity
orinocoGroups=_OrinocoGroups_ObjectIdentity((1,3,6,1,4,1,11898,2,3,1))
_OrinocoCompliances_ObjectIdentity=ObjectIdentity
orinocoCompliances=_OrinocoCompliances_ObjectIdentity((1,3,6,1,4,1,11898,2,3,2))
_OrinocoProducts_ObjectIdentity=ObjectIdentity
orinocoProducts=_OrinocoProducts_ObjectIdentity((1,3,6,1,4,1,11898,2,4))
_Ap1000_ObjectIdentity=ObjectIdentity
ap1000=_Ap1000_ObjectIdentity((1,3,6,1,4,1,11898,2,4,1))
_Rg1000_ObjectIdentity=ObjectIdentity
rg1000=_Rg1000_ObjectIdentity((1,3,6,1,4,1,11898,2,4,2))
_As1000_ObjectIdentity=ObjectIdentity
as1000=_As1000_ObjectIdentity((1,3,6,1,4,1,11898,2,4,3))
_As2000_ObjectIdentity=ObjectIdentity
as2000=_As2000_ObjectIdentity((1,3,6,1,4,1,11898,2,4,4))
_Ap500_ObjectIdentity=ObjectIdentity
ap500=_Ap500_ObjectIdentity((1,3,6,1,4,1,11898,2,4,5))
_Ap2000_ObjectIdentity=ObjectIdentity
ap2000=_Ap2000_ObjectIdentity((1,3,6,1,4,1,11898,2,4,6))
_Bg2000_ObjectIdentity=ObjectIdentity
bg2000=_Bg2000_ObjectIdentity((1,3,6,1,4,1,11898,2,4,7))
_Rg1100_ObjectIdentity=ObjectIdentity
rg1100=_Rg1100_ObjectIdentity((1,3,6,1,4,1,11898,2,4,8))
_Tmp11_ObjectIdentity=ObjectIdentity
tmp11=_Tmp11_ObjectIdentity((1,3,6,1,4,1,11898,2,4,9))
_Ap600_ObjectIdentity=ObjectIdentity
ap600=_Ap600_ObjectIdentity((1,3,6,1,4,1,11898,2,4,10))
_Ap2500_ObjectIdentity=ObjectIdentity
ap2500=_Ap2500_ObjectIdentity((1,3,6,1,4,1,11898,2,4,11))
_Ap4000_ObjectIdentity=ObjectIdentity
ap4000=_Ap4000_ObjectIdentity((1,3,6,1,4,1,11898,2,4,12))
_Ap700_ObjectIdentity=ObjectIdentity
ap700=_Ap700_ObjectIdentity((1,3,6,1,4,1,11898,2,4,13))
oriTrapDNSIPNotConfigured=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,3))
oriTrapDNSIPNotConfigured.setObjects(*((_E,_K),(_E,_R)))
if mibBuilder.loadTexts:oriTrapDNSIPNotConfigured.setStatus(_A)
oriTrapRADIUSAuthenticationNotConfigured=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,5))
oriTrapRADIUSAuthenticationNotConfigured.setObjects(*((_E,_K),(_E,_R)))
if mibBuilder.loadTexts:oriTrapRADIUSAuthenticationNotConfigured.setStatus(_A)
oriTrapRADIUSAccountingNotConfigured=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,6))
oriTrapRADIUSAccountingNotConfigured.setObjects(*((_E,_K),(_E,_R)))
if mibBuilder.loadTexts:oriTrapRADIUSAccountingNotConfigured.setStatus(_A)
oriTrapDuplicateIPAddressEncountered=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,7))
oriTrapDuplicateIPAddressEncountered.setObjects(*((_E,_K),(_E,_R)))
if mibBuilder.loadTexts:oriTrapDuplicateIPAddressEncountered.setStatus(_A)
oriTrapDHCPRelayServerTableNotConfigured=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,8))
if mibBuilder.loadTexts:oriTrapDHCPRelayServerTableNotConfigured.setStatus(_A)
oriTrapWORPIfNetworkSecretNotConfigured=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,9))
if mibBuilder.loadTexts:oriTrapWORPIfNetworkSecretNotConfigured.setStatus(_A)
oriTrapVLANIDInvalidConfiguration=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,10))
oriTrapVLANIDInvalidConfiguration.setObjects(*((_E,_K),(_E,_Aw),(_E,_Ax)))
if mibBuilder.loadTexts:oriTrapVLANIDInvalidConfiguration.setStatus(_A)
oriTrapAutoConfigFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,11))
oriTrapAutoConfigFailure.setObjects(*((_E,_K),(_E,_Ay),(_E,_Az)))
if mibBuilder.loadTexts:oriTrapAutoConfigFailure.setStatus(_A)
oriTrapBatchExecFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,12))
oriTrapBatchExecFailure.setObjects(*((_E,_K),(_E,_g),(_E,_A_),(_E,_t)))
if mibBuilder.loadTexts:oriTrapBatchExecFailure.setStatus(_A)
oriTrapBatchFileExecStart=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,13))
oriTrapBatchFileExecStart.setObjects(*((_E,_K),(_E,_g)))
if mibBuilder.loadTexts:oriTrapBatchFileExecStart.setStatus(_A)
oriTrapBatchFileExecEnd=NotificationType((1,3,6,1,4,1,11898,2,1,18,2,0,14))
oriTrapBatchFileExecEnd.setObjects(*((_E,_K),(_E,_g),(_E,_t)))
if mibBuilder.loadTexts:oriTrapBatchFileExecEnd.setStatus(_A)
oriTrapInvalidEncryptionKey=NotificationType((1,3,6,1,4,1,11898,2,1,18,3,0,1))
oriTrapInvalidEncryptionKey.setObjects((_E,_u))
if mibBuilder.loadTexts:oriTrapInvalidEncryptionKey.setStatus(_A)
oriTrapAuthenticationFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,3,0,2))
oriTrapAuthenticationFailure.setObjects(*((_E,_u),(_E,_B0)))
if mibBuilder.loadTexts:oriTrapAuthenticationFailure.setStatus(_A)
oriTrapUnauthorizedManagerDetected=NotificationType((1,3,6,1,4,1,11898,2,1,18,3,0,3))
oriTrapUnauthorizedManagerDetected.setObjects(*((_E,_B1),(_E,_B2)))
if mibBuilder.loadTexts:oriTrapUnauthorizedManagerDetected.setStatus(_A)
oriTrapRADScanComplete=NotificationType((1,3,6,1,4,1,11898,2,1,18,3,0,4))
oriTrapRADScanComplete.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapRADScanComplete.setStatus(_A)
oriTrapRADScanResults=NotificationType((1,3,6,1,4,1,11898,2,1,18,3,0,5))
oriTrapRADScanResults.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapRADScanResults.setStatus(_A)
oriTrapRogueScanStationDetected=NotificationType((1,3,6,1,4,1,11898,2,1,18,3,0,6))
oriTrapRogueScanStationDetected.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapRogueScanStationDetected.setStatus(_A)
oriTrapRogueScanCycleComplete=NotificationType((1,3,6,1,4,1,11898,2,1,18,3,0,7))
oriTrapRogueScanCycleComplete.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapRogueScanCycleComplete.setStatus(_A)
oriTrapWLCNotPresent=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,1))
oriTrapWLCNotPresent.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWLCNotPresent.setStatus(_A)
oriTrapWLCFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,2))
oriTrapWLCFailure.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWLCFailure.setStatus(_A)
oriTrapWLCRemoval=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,3))
oriTrapWLCRemoval.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWLCRemoval.setStatus(_A)
oriTrapWLCIncompatibleFirmware=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,4))
oriTrapWLCIncompatibleFirmware.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWLCIncompatibleFirmware.setStatus(_A)
oriTrapWLCVoltageDiscrepancy=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,5))
oriTrapWLCVoltageDiscrepancy.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWLCVoltageDiscrepancy.setStatus(_A)
oriTrapWLCIncompatibleVendor=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,6))
oriTrapWLCIncompatibleVendor.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWLCIncompatibleVendor.setStatus(_A)
oriTrapWLCFirmwareDownloadFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,7))
oriTrapWLCFirmwareDownloadFailure.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWLCFirmwareDownloadFailure.setStatus(_A)
oriTrapWLCFirmwareFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,8))
oriTrapWLCFirmwareFailure.setObjects(*((_E,_P),(_E,_K)))
if mibBuilder.loadTexts:oriTrapWLCFirmwareFailure.setStatus(_A)
oriTrapWLCRadarInterferenceDetected=NotificationType((1,3,6,1,4,1,11898,2,1,18,4,0,9))
oriTrapWLCRadarInterferenceDetected.setObjects(*((_E,_P),(_E,_K)))
if mibBuilder.loadTexts:oriTrapWLCRadarInterferenceDetected.setStatus(_A)
oriTrapUnrecoverableSoftwareErrorDetected=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,1))
oriTrapUnrecoverableSoftwareErrorDetected.setObjects(*((_E,_K),(_E,_R),(_E,_v)))
if mibBuilder.loadTexts:oriTrapUnrecoverableSoftwareErrorDetected.setStatus(_A)
oriTrapRADIUSServerNotResponding=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,2))
oriTrapRADIUSServerNotResponding.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapRADIUSServerNotResponding.setStatus(_A)
oriTrapModuleNotInitialized=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,3))
oriTrapModuleNotInitialized.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapModuleNotInitialized.setStatus(_A)
oriTrapDeviceRebooting=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,5))
oriTrapDeviceRebooting.setObjects(*((_E,_R),(_E,_K),(_E,_B3)))
if mibBuilder.loadTexts:oriTrapDeviceRebooting.setStatus(_A)
oriTrapTaskSuspended=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,6))
oriTrapTaskSuspended.setObjects((_E,_v))
if mibBuilder.loadTexts:oriTrapTaskSuspended.setStatus(_A)
oriTrapBootPFailed=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,7))
oriTrapBootPFailed.setObjects((_E,_R))
if mibBuilder.loadTexts:oriTrapBootPFailed.setStatus(_A)
oriTrapDHCPFailed=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,8))
oriTrapDHCPFailed.setObjects((_E,_R))
if mibBuilder.loadTexts:oriTrapDHCPFailed.setStatus(_A)
oriTrapDNSClientLookupFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,9))
oriTrapDNSClientLookupFailure.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapDNSClientLookupFailure.setStatus(_A)
oriTrapSNTPFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,10))
if mibBuilder.loadTexts:oriTrapSNTPFailure.setStatus(_A)
oriTrapMaximumNumberOfSubscribersReached=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,11))
if mibBuilder.loadTexts:oriTrapMaximumNumberOfSubscribersReached.setStatus(_A)
oriTrapSSLInitializationFailure=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,12))
if mibBuilder.loadTexts:oriTrapSSLInitializationFailure.setStatus(_A)
oriTrapWirelessServiceShutdown=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,13))
oriTrapWirelessServiceShutdown.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWirelessServiceShutdown.setStatus(_A)
oriTrapWirelessServiceResumed=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,14))
oriTrapWirelessServiceResumed.setObjects((_E,_P))
if mibBuilder.loadTexts:oriTrapWirelessServiceResumed.setStatus(_A)
oriTrapSSHInitializationStatus=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,15))
oriTrapSSHInitializationStatus.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapSSHInitializationStatus.setStatus(_A)
oriTrapVLANIDUserAssignment=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,16))
oriTrapVLANIDUserAssignment.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapVLANIDUserAssignment.setStatus(_A)
oriTrapDHCPLeaseRenewal=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,17))
oriTrapDHCPLeaseRenewal.setObjects(*((_E,_B4),(_E,_B5),(_E,_B6),(_E,_B7)))
if mibBuilder.loadTexts:oriTrapDHCPLeaseRenewal.setStatus(_A)
oriTrapTemperatureAlert=NotificationType((1,3,6,1,4,1,11898,2,1,18,5,0,18))
oriTrapTemperatureAlert.setObjects(*((_E,_K),(_E,_B8)))
if mibBuilder.loadTexts:oriTrapTemperatureAlert.setStatus(_A)
oriTrapFlashMemoryEmpty=NotificationType((1,3,6,1,4,1,11898,2,1,18,6,0,1))
if mibBuilder.loadTexts:oriTrapFlashMemoryEmpty.setStatus(_A)
oriTrapFlashMemoryCorrupted=NotificationType((1,3,6,1,4,1,11898,2,1,18,6,0,2))
oriTrapFlashMemoryCorrupted.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapFlashMemoryCorrupted.setStatus(_A)
oriTrapFlashMemoryRestoringLastKnownGoodConfiguration=NotificationType((1,3,6,1,4,1,11898,2,1,18,6,0,3))
if mibBuilder.loadTexts:oriTrapFlashMemoryRestoringLastKnownGoodConfiguration.setStatus(_A)
oriTrapTFTPFailedOperation=NotificationType((1,3,6,1,4,1,11898,2,1,18,7,0,1))
oriTrapTFTPFailedOperation.setObjects(*((_E,_h),(_E,_i),(_E,_j)))
if mibBuilder.loadTexts:oriTrapTFTPFailedOperation.setStatus(_A)
oriTrapTFTPOperationInitiated=NotificationType((1,3,6,1,4,1,11898,2,1,18,7,0,2))
oriTrapTFTPOperationInitiated.setObjects(*((_E,_h),(_E,_i),(_E,_j)))
if mibBuilder.loadTexts:oriTrapTFTPOperationInitiated.setStatus(_A)
oriTrapTFTPOperationCompleted=NotificationType((1,3,6,1,4,1,11898,2,1,18,7,0,3))
oriTrapTFTPOperationCompleted.setObjects(*((_E,_h),(_E,_i),(_E,_j)))
if mibBuilder.loadTexts:oriTrapTFTPOperationCompleted.setStatus(_A)
oriTrapZeroSizeImage=NotificationType((1,3,6,1,4,1,11898,2,1,18,9,0,1))
if mibBuilder.loadTexts:oriTrapZeroSizeImage.setStatus(_A)
oriTrapInvalidImage=NotificationType((1,3,6,1,4,1,11898,2,1,18,9,0,2))
if mibBuilder.loadTexts:oriTrapInvalidImage.setStatus(_A)
oriTrapImageTooLarge=NotificationType((1,3,6,1,4,1,11898,2,1,18,9,0,3))
if mibBuilder.loadTexts:oriTrapImageTooLarge.setStatus(_A)
oriTrapIncompatibleImage=NotificationType((1,3,6,1,4,1,11898,2,1,18,9,0,4))
if mibBuilder.loadTexts:oriTrapIncompatibleImage.setStatus(_A)
oriTrapInvalidImageDigitalSignature=NotificationType((1,3,6,1,4,1,11898,2,1,18,9,0,5))
if mibBuilder.loadTexts:oriTrapInvalidImageDigitalSignature.setStatus(_A)
oriWORPStationRegister=NotificationType((1,3,6,1,4,1,11898,2,1,18,11,0,1))
oriWORPStationRegister.setObjects(*((_E,_w),(_E,_R)))
if mibBuilder.loadTexts:oriWORPStationRegister.setStatus(_A)
oriWORPStationDeRegister=NotificationType((1,3,6,1,4,1,11898,2,1,18,11,0,2))
oriWORPStationDeRegister.setObjects(*((_E,_w),(_E,_R)))
if mibBuilder.loadTexts:oriWORPStationDeRegister.setStatus(_A)
oriTrapIncompatibleLicenseFile=NotificationType((1,3,6,1,4,1,11898,2,1,18,12,0,1))
oriTrapIncompatibleLicenseFile.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapIncompatibleLicenseFile.setStatus(_A)
oriTrapFeatureNotSupported=NotificationType((1,3,6,1,4,1,11898,2,1,18,12,0,2))
oriTrapFeatureNotSupported.setObjects((_E,_l))
if mibBuilder.loadTexts:oriTrapFeatureNotSupported.setStatus(_A)
oriTrapZeroLicenseFiles=NotificationType((1,3,6,1,4,1,11898,2,1,18,12,0,3))
if mibBuilder.loadTexts:oriTrapZeroLicenseFiles.setStatus(_A)
oriTrapInvalidLicenseFile=NotificationType((1,3,6,1,4,1,11898,2,1,18,12,0,4))
oriTrapInvalidLicenseFile.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapInvalidLicenseFile.setStatus(_A)
oriTrapUselessLicense=NotificationType((1,3,6,1,4,1,11898,2,1,18,12,0,5))
oriTrapUselessLicense.setObjects((_E,_K))
if mibBuilder.loadTexts:oriTrapUselessLicense.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_a:VlanId,'InterfaceBitmask':InterfaceBitmask,_J:ObjStatus,'WEPKeyType':WEPKeyType,_N:ObjStatusActive,'DisplayString80':DisplayString80,'DisplayString55':DisplayString55,'DisplayString32':DisplayString32,'agere':agere,'orinoco':orinoco,'orinocoObjects':orinocoObjects,'orinocoSys':orinocoSys,'orinocoSysInvMgmt':orinocoSysInvMgmt,'oriSystemInvMgmtComponentTable':oriSystemInvMgmtComponentTable,'oriSystemInvMgmtComponentTableEntry':oriSystemInvMgmtComponentTableEntry,_k:oriSystemInvMgmtTableComponentIndex,'oriSystemInvMgmtTableComponentSerialNumber':oriSystemInvMgmtTableComponentSerialNumber,'oriSystemInvMgmtTableComponentName':oriSystemInvMgmtTableComponentName,'oriSystemInvMgmtTableComponentId':oriSystemInvMgmtTableComponentId,'oriSystemInvMgmtTableComponentVariant':oriSystemInvMgmtTableComponentVariant,'oriSystemInvMgmtTableComponentReleaseVersion':oriSystemInvMgmtTableComponentReleaseVersion,'oriSystemInvMgmtTableComponentMajorVersion':oriSystemInvMgmtTableComponentMajorVersion,'oriSystemInvMgmtTableComponentMinorVersion':oriSystemInvMgmtTableComponentMinorVersion,'oriSystemInvMgmtTableComponentIfTable':oriSystemInvMgmtTableComponentIfTable,'oriSystemInvMgmtTableComponentIfTableEntry':oriSystemInvMgmtTableComponentIfTableEntry,_y:oriSystemInvMgmtInterfaceTableIndex,'oriSystemInvMgmtInterfaceId':oriSystemInvMgmtInterfaceId,'oriSystemInvMgmtInterfaceRole':oriSystemInvMgmtInterfaceRole,'oriSystemInvMgmtInterfaceVariant':oriSystemInvMgmtInterfaceVariant,'oriSystemInvMgmtInterfaceBottomNumber':oriSystemInvMgmtInterfaceBottomNumber,'oriSystemInvMgmtInterfaceTopNumber':oriSystemInvMgmtInterfaceTopNumber,_B3:oriSystemReboot,'oriSystemContactEmail':oriSystemContactEmail,'oriSystemContactPhoneNumber':oriSystemContactPhoneNumber,'oriSystemFlashUpdate':oriSystemFlashUpdate,'oriSystemFlashBackupInterval':oriSystemFlashBackupInterval,'oriSystemEmergencyResetToDefault':oriSystemEmergencyResetToDefault,'oriSystemMode':oriSystemMode,'oriSystemEventLogTable':oriSystemEventLogTable,'oriSystemEventLogTableEntry':oriSystemEventLogTableEntry,_z:oriSystemEventLogMessage,'oriSystemEventLogTableReset':oriSystemEventLogTableReset,'oriSystemEventLogMask':oriSystemEventLogMask,'oriSystemAccessUserName':oriSystemAccessUserName,'oriSystemAccessPassword':oriSystemAccessPassword,'oriSystemAccessLoginTimeout':oriSystemAccessLoginTimeout,'oriSystemAccessIdleTimeout':oriSystemAccessIdleTimeout,'oriSystemEventLogNumberOfMessages':oriSystemEventLogNumberOfMessages,'orinocoSysFeature':orinocoSysFeature,'oriSystemFeatureTable':oriSystemFeatureTable,'oriSystemFeatureTableEntry':oriSystemFeatureTableEntry,_l:oriSystemFeatureTableCode,'oriSystemFeatureTableSupported':oriSystemFeatureTableSupported,'oriSystemFeatureTableLicensed':oriSystemFeatureTableLicensed,'oriSystemFeatureTableDescription':oriSystemFeatureTableDescription,'oriSystemAccessMaxSessions':oriSystemAccessMaxSessions,'orinocoSyslog':orinocoSyslog,'oriSyslogStatus':oriSyslogStatus,'oriSyslogPort':oriSyslogPort,'oriSyslogPriority':oriSyslogPriority,'oriSyslogHeartbeatStatus':oriSyslogHeartbeatStatus,'oriSyslogHeartbeatInterval':oriSyslogHeartbeatInterval,'oriSyslogHostTable':oriSyslogHostTable,'oriSyslogHostTableEntry':oriSyslogHostTableEntry,_A1:oriSyslogHostTableIndex,'oriSyslogHostIPAddress':oriSyslogHostIPAddress,'oriSyslogHostComment':oriSyslogHostComment,'oriSyslogHostTableEntryStatus':oriSyslogHostTableEntryStatus,'oriSystemCountryCode':oriSystemCountryCode,'orinocoTempLog':orinocoTempLog,_B8:oriUnitTemp,'oriTempLoggingInterval':oriTempLoggingInterval,'oriTempLogTable':oriTempLogTable,'oriTempLogTableEntry':oriTempLogTableEntry,_A2:oriTempLogMessage,'oriTempLogTableReset':oriTempLogTableReset,'oriSystemHwType':oriSystemHwType,'orinocoIf':orinocoIf,'orinocoWirelessIf':orinocoWirelessIf,'oriWirelessIfPropertiesTable':oriWirelessIfPropertiesTable,'oriWirelessIfPropertiesEntry':oriWirelessIfPropertiesEntry,_A3:oriWirelessIfPropertiesIndex,_Aw:oriWirelessIfNetworkName,'oriWirelessIfMediumReservation':oriWirelessIfMediumReservation,'oriWirelessIfInterferenceRobustness':oriWirelessIfInterferenceRobustness,'oriWirelessIfDTIMPeriod':oriWirelessIfDTIMPeriod,'oriWirelessIfChannel':oriWirelessIfChannel,'oriWirelessIfDistancebetweenAPs':oriWirelessIfDistancebetweenAPs,'oriWirelessIfMulticastRate':oriWirelessIfMulticastRate,'oriWirelessIfClosedSystem':oriWirelessIfClosedSystem,'oriWirelessIfAllowedSupportedDataRates':oriWirelessIfAllowedSupportedDataRates,'oriWirelessIfRegulatoryDomainList':oriWirelessIfRegulatoryDomainList,'oriWirelessIfAllowedChannels':oriWirelessIfAllowedChannels,'oriWirelessIfMACAddress':oriWirelessIfMACAddress,'oriWirelessIfLoadBalancing':oriWirelessIfLoadBalancing,'oriWirelessIfMediumDensityDistribution':oriWirelessIfMediumDensityDistribution,'oriWirelessIfTxRate':oriWirelessIfTxRate,'oriWirelessIfAutoChannelSelectStatus':oriWirelessIfAutoChannelSelectStatus,'oriWirelessIfBandwidthLimitIn':oriWirelessIfBandwidthLimitIn,'oriWirelessIfBandwidthLimitOut':oriWirelessIfBandwidthLimitOut,'oriWirelessIfTurboModeStatus':oriWirelessIfTurboModeStatus,'oriWirelessIfSupportedOperationalModes':oriWirelessIfSupportedOperationalModes,'oriWirelessIfOperationalMode':oriWirelessIfOperationalMode,'oriWirelessIfPreambleType':oriWirelessIfPreambleType,'oriWirelessIfProtectionMechanismStatus':oriWirelessIfProtectionMechanismStatus,'oriWirelessIfSupportedMulticastRates':oriWirelessIfSupportedMulticastRates,'oriWirelessIfCapabilities':oriWirelessIfCapabilities,'oriWirelessIfLBTxTimeThreshold':oriWirelessIfLBTxTimeThreshold,'oriWirelessIfLBAdjAPTimeDiffThreshold':oriWirelessIfLBAdjAPTimeDiffThreshold,'oriWirelessIfACSFrequencyBandScan':oriWirelessIfACSFrequencyBandScan,'oriWirelessIfSecurityPerSSIDStatus':oriWirelessIfSecurityPerSSIDStatus,'oriWirelessIfDFSStatus':oriWirelessIfDFSStatus,'oriWirelessIfAntenna':oriWirelessIfAntenna,'oriWirelessIfTPCMode':oriWirelessIfTPCMode,'oriWirelessIfSuperModeStatus':oriWirelessIfSuperModeStatus,'oriWirelessIfWSSStatus':oriWirelessIfWSSStatus,'oriWirelessIfSupportedAuthenticationModes':oriWirelessIfSupportedAuthenticationModes,'oriWirelessIfSupportedCipherModes':oriWirelessIfSupportedCipherModes,'oriWirelessIfQoSStatus':oriWirelessIfQoSStatus,'oriWirelessIfQoSMaxMediumThreshold':oriWirelessIfQoSMaxMediumThreshold,'oriWirelessIfAntennaGain':oriWirelessIfAntennaGain,'oriWirelessIfSecurityTable':oriWirelessIfSecurityTable,'oriWirelessIfSecurityEntry':oriWirelessIfSecurityEntry,_A4:oriWirelessIfSecurityIndex,'oriWirelessIfEncryptionOptions':oriWirelessIfEncryptionOptions,'oriWirelessIfEncryptionStatus':oriWirelessIfEncryptionStatus,'oriWirelessIfEncryptionKey1':oriWirelessIfEncryptionKey1,'oriWirelessIfEncryptionKey2':oriWirelessIfEncryptionKey2,'oriWirelessIfEncryptionKey3':oriWirelessIfEncryptionKey3,'oriWirelessIfEncryptionKey4':oriWirelessIfEncryptionKey4,'oriWirelessIfEncryptionTxKey':oriWirelessIfEncryptionTxKey,'oriWirelessIfDenyNonEncryptedData':oriWirelessIfDenyNonEncryptedData,'oriWirelessIfProfileCode':oriWirelessIfProfileCode,'oriWirelessIfSSIDTable':oriWirelessIfSSIDTable,'oriWirelessIfSSIDTableEntry':oriWirelessIfSSIDTableEntry,_A5:oriWirelessIfSSIDTableIndex,'oriWirelessIfSSIDTableSSID':oriWirelessIfSSIDTableSSID,'oriWirelessIfSSIDTableVLANID':oriWirelessIfSSIDTableVLANID,'oriWirelessIfSSIDTableStatus':oriWirelessIfSSIDTableStatus,'oriWirelessIfSSIDTableSecurityMode':oriWirelessIfSSIDTableSecurityMode,'oriWirelessIfSSIDTableBroadcastSSID':oriWirelessIfSSIDTableBroadcastSSID,'oriWirelessIfSSIDTableClosedSystem':oriWirelessIfSSIDTableClosedSystem,'oriWirelessIfSSIDTableSupportedSecurityModes':oriWirelessIfSSIDTableSupportedSecurityModes,'oriWirelessIfSSIDTableEncryptionKey0':oriWirelessIfSSIDTableEncryptionKey0,'oriWirelessIfSSIDTableEncryptionKey1':oriWirelessIfSSIDTableEncryptionKey1,'oriWirelessIfSSIDTableEncryptionKey2':oriWirelessIfSSIDTableEncryptionKey2,'oriWirelessIfSSIDTableEncryptionKey3':oriWirelessIfSSIDTableEncryptionKey3,'oriWirelessIfSSIDTableEncryptionTxKey':oriWirelessIfSSIDTableEncryptionTxKey,'oriWirelessIfSSIDTableEncryptionKeyLength':oriWirelessIfSSIDTableEncryptionKeyLength,'oriWirelessIfSSIDTableRekeyingInterval':oriWirelessIfSSIDTableRekeyingInterval,'oriWirelessIfSSIDTablePSKValue':oriWirelessIfSSIDTablePSKValue,'oriWirelessIfSSIDTablePSKPassPhrase':oriWirelessIfSSIDTablePSKPassPhrase,'oriWirelessIfSSIDTableDenyNonEncryptedData':oriWirelessIfSSIDTableDenyNonEncryptedData,'oriWirelessIfSSIDTableSSIDAuthorizationStatus':oriWirelessIfSSIDTableSSIDAuthorizationStatus,'oriWirelessIfSSIDTableMACAccessControl':oriWirelessIfSSIDTableMACAccessControl,'oriWirelessIfSSIDTableRADIUSMACAccessControl':oriWirelessIfSSIDTableRADIUSMACAccessControl,'oriWirelessIfSSIDTableSecurityProfile':oriWirelessIfSSIDTableSecurityProfile,'oriWirelessIfSSIDTableRADIUSDot1xProfile':oriWirelessIfSSIDTableRADIUSDot1xProfile,'oriWirelessIfSSIDTableRADIUSMACAuthProfile':oriWirelessIfSSIDTableRADIUSMACAuthProfile,'oriWirelessIfSSIDTableRADIUSAccountingStatus':oriWirelessIfSSIDTableRADIUSAccountingStatus,'oriWirelessIfSSIDTableRADIUSAccountingProfile':oriWirelessIfSSIDTableRADIUSAccountingProfile,'oriWirelessIfSSIDTableQoSPolicy':oriWirelessIfSSIDTableQoSPolicy,'oriWirelessIfTxPowerControl':oriWirelessIfTxPowerControl,'orinocoEthernetIf':orinocoEthernetIf,'oriEthernetIfConfigTable':oriEthernetIfConfigTable,'oriEthernetIfConfigTableEntry':oriEthernetIfConfigTableEntry,_A6:oriEthernetIfConfigTableIndex,'oriEthernetIfConfigSettings':oriEthernetIfConfigSettings,'oriEthernetIfConfigBandwidthLimitIn':oriEthernetIfConfigBandwidthLimitIn,'oriEthernetIfConfigBandwidthLimitOut':oriEthernetIfConfigBandwidthLimitOut,'oriIfWANInterfaceMACAddress':oriIfWANInterfaceMACAddress,'orinocoWORPIf':orinocoWORPIf,'oriWORPIfConfigTable':oriWORPIfConfigTable,'oriWORPIfConfigTableEntry':oriWORPIfConfigTableEntry,'oriWORPIfConfigTableMode':oriWORPIfConfigTableMode,'oriWORPIfConfigTableBaseStationName':oriWORPIfConfigTableBaseStationName,'oriWORPIfConfigTableMaxSatellites':oriWORPIfConfigTableMaxSatellites,'oriWORPIfConfigTableRegistrationTimeout':oriWORPIfConfigTableRegistrationTimeout,'oriWORPIfConfigTableRetries':oriWORPIfConfigTableRetries,'oriWORPIfConfigTableNetworkSecret':oriWORPIfConfigTableNetworkSecret,'oriWORPIfConfigTableNoSleepMode':oriWORPIfConfigTableNoSleepMode,'oriWORPIfStatTable':oriWORPIfStatTable,'oriWORPIfStatTableEntry':oriWORPIfStatTableEntry,'oriWORPIfStatTableRemotePartners':oriWORPIfStatTableRemotePartners,'oriWORPIfStatTableAverageLocalSignal':oriWORPIfStatTableAverageLocalSignal,'oriWORPIfStatTableAverageLocalNoise':oriWORPIfStatTableAverageLocalNoise,'oriWORPIfStatTableAverageRemoteSignal':oriWORPIfStatTableAverageRemoteSignal,'oriWORPIfStatTableAverageRemoteNoise':oriWORPIfStatTableAverageRemoteNoise,'oriWORPIfStatTableBaseStationAnnounces':oriWORPIfStatTableBaseStationAnnounces,'oriWORPIfStatTableRegistrationRequests':oriWORPIfStatTableRegistrationRequests,'oriWORPIfStatTableRegistrationRejects':oriWORPIfStatTableRegistrationRejects,'oriWORPIfStatTableAuthenticationRequests':oriWORPIfStatTableAuthenticationRequests,'oriWORPIfStatTableAuthenticationConfirms':oriWORPIfStatTableAuthenticationConfirms,'oriWORPIfStatTableRegistrationAttempts':oriWORPIfStatTableRegistrationAttempts,'oriWORPIfStatTableRegistrationIncompletes':oriWORPIfStatTableRegistrationIncompletes,'oriWORPIfStatTableRegistrationTimeouts':oriWORPIfStatTableRegistrationTimeouts,'oriWORPIfStatTableRegistrationLastReason':oriWORPIfStatTableRegistrationLastReason,'oriWORPIfStatTablePollData':oriWORPIfStatTablePollData,'oriWORPIfStatTablePollNoData':oriWORPIfStatTablePollNoData,'oriWORPIfStatTableReplyData':oriWORPIfStatTableReplyData,'oriWORPIfStatTableReplyMoreData':oriWORPIfStatTableReplyMoreData,'oriWORPIfStatTableReplyNoData':oriWORPIfStatTableReplyNoData,'oriWORPIfStatTableRequestForService':oriWORPIfStatTableRequestForService,'oriWORPIfStatTableSendSuccess':oriWORPIfStatTableSendSuccess,'oriWORPIfStatTableSendRetries':oriWORPIfStatTableSendRetries,'oriWORPIfStatTableSendFailures':oriWORPIfStatTableSendFailures,'oriWORPIfStatTableReceiveSuccess':oriWORPIfStatTableReceiveSuccess,'oriWORPIfStatTableReceiveRetries':oriWORPIfStatTableReceiveRetries,'oriWORPIfStatTableReceiveFailures':oriWORPIfStatTableReceiveFailures,'oriWORPIfStatTablePollNoReplies':oriWORPIfStatTablePollNoReplies,'orinocoWORPIfSat':orinocoWORPIfSat,'orinocoWORPIfSatConfig':orinocoWORPIfSatConfig,'oriWORPIfSatConfigStatus':oriWORPIfSatConfigStatus,'oriWORPIfSatConfigTable':oriWORPIfSatConfigTable,'oriWORPIfSatConfigTableEntry':oriWORPIfSatConfigTableEntry,_A7:oriWORPIfSatConfigTableIndex,'oriWORPIfSatConfigTableEntryStatus':oriWORPIfSatConfigTableEntryStatus,'oriWORPIfSatConfigTableMacAddress':oriWORPIfSatConfigTableMacAddress,'oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink':oriWORPIfSatConfigTableMinimumBandwidthLimitDownlink,'oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink':oriWORPIfSatConfigTableMaximumBandwidthLimitDownlink,'oriWORPIfSatConfigTableMinimumBandwidthLimitUplink':oriWORPIfSatConfigTableMinimumBandwidthLimitUplink,'oriWORPIfSatConfigTableMaximumBandwidthLimitUplink':oriWORPIfSatConfigTableMaximumBandwidthLimitUplink,'oriWORPIfSatConfigTableComment':oriWORPIfSatConfigTableComment,'orinocoWORPIfSatStat':orinocoWORPIfSatStat,'oriWORPIfSatStatTable':oriWORPIfSatStatTable,'oriWORPIfSatStatTableEntry':oriWORPIfSatStatTableEntry,'oriWORPIfSatStatTableIndex':oriWORPIfSatStatTableIndex,'oriWORPIfSatStatTableMacAddress':oriWORPIfSatStatTableMacAddress,'oriWORPIfSatStatTableAverageLocalSignal':oriWORPIfSatStatTableAverageLocalSignal,'oriWORPIfSatStatTableAverageLocalNoise':oriWORPIfSatStatTableAverageLocalNoise,'oriWORPIfSatStatTableAverageRemoteSignal':oriWORPIfSatStatTableAverageRemoteSignal,'oriWORPIfSatStatTableAverageRemoteNoise':oriWORPIfSatStatTableAverageRemoteNoise,'oriWORPIfSatStatTablePollData':oriWORPIfSatStatTablePollData,'oriWORPIfSatStatTablePollNoData':oriWORPIfSatStatTablePollNoData,'oriWORPIfSatStatTableReplyData':oriWORPIfSatStatTableReplyData,'oriWORPIfSatStatTableReplyNoData':oriWORPIfSatStatTableReplyNoData,'oriWORPIfSatStatTableRequestForService':oriWORPIfSatStatTableRequestForService,'oriWORPIfSatStatTableSendSuccess':oriWORPIfSatStatTableSendSuccess,'oriWORPIfSatStatTableSendRetries':oriWORPIfSatStatTableSendRetries,'oriWORPIfSatStatTableSendFailures':oriWORPIfSatStatTableSendFailures,'oriWORPIfSatStatTableReceiveSuccess':oriWORPIfSatStatTableReceiveSuccess,'oriWORPIfSatStatTableReceiveRetries':oriWORPIfSatStatTableReceiveRetries,'oriWORPIfSatStatTableReceiveFailures':oriWORPIfSatStatTableReceiveFailures,'oriWORPIfSatStatTablePollNoReplies':oriWORPIfSatStatTablePollNoReplies,'oriWORPIfSatStatTableLocalTxRate':oriWORPIfSatStatTableLocalTxRate,'oriWORPIfSatStatTableRemoteTxRate':oriWORPIfSatStatTableRemoteTxRate,'orinocoWORPIfSiteSurvey':orinocoWORPIfSiteSurvey,'oriWORPIfSiteSurveyOperation':oriWORPIfSiteSurveyOperation,'oriWORPIfSiteSurveyTable':oriWORPIfSiteSurveyTable,'oriWORPIfSiteSurveySignalQualityTableEntry':oriWORPIfSiteSurveySignalQualityTableEntry,_A8:oriWORPIfSiteSurveyTableIndex,'oriWORPIfSiteSurveyBaseMACAddress':oriWORPIfSiteSurveyBaseMACAddress,'oriWORPIfSiteSurveyBaseName':oriWORPIfSiteSurveyBaseName,'oriWORPIfSiteSurveyMaxSatAllowed':oriWORPIfSiteSurveyMaxSatAllowed,'oriWORPIfSiteSurveyNumSatRegistered':oriWORPIfSiteSurveyNumSatRegistered,'oriWORPIfSiteSurveyCurrentSatRegistered':oriWORPIfSiteSurveyCurrentSatRegistered,'oriWORPIfSiteSurveyLocalSignalLevel':oriWORPIfSiteSurveyLocalSignalLevel,'oriWORPIfSiteSurveyLocalNoiseLevel':oriWORPIfSiteSurveyLocalNoiseLevel,'oriWORPIfSiteSurveyLocalSNR':oriWORPIfSiteSurveyLocalSNR,'oriWORPIfSiteSurveyRemoteSignalLevel':oriWORPIfSiteSurveyRemoteSignalLevel,'oriWORPIfSiteSurveyRemoteNoiseLevel':oriWORPIfSiteSurveyRemoteNoiseLevel,'oriWORPIfSiteSurveyRemoteSNR':oriWORPIfSiteSurveyRemoteSNR,'orinocoWORPIfRoaming':orinocoWORPIfRoaming,'oriWORPIfRoamingStatus':oriWORPIfRoamingStatus,'oriWORPIfRoamingSlowScanThreshold':oriWORPIfRoamingSlowScanThreshold,'oriWORPIfRoamingFastScanThreshold':oriWORPIfRoamingFastScanThreshold,'oriWORPIfRoamingThreshold':oriWORPIfRoamingThreshold,'oriWORPIfRoamingSlowScanPercentThreshold':oriWORPIfRoamingSlowScanPercentThreshold,'oriWORPIfRoamingFastScanPercentThreshold':oriWORPIfRoamingFastScanPercentThreshold,'orinocoWORPIfDDRS':orinocoWORPIfDDRS,'oriWORPIfDDRSStatus':oriWORPIfDDRSStatus,'oriWORPIfDDRSDefDataRate':oriWORPIfDDRSDefDataRate,'oriWORPIfDDRSMaxDataRate':oriWORPIfDDRSMaxDataRate,'oriWORPIfDDRSMinReqSNRdot11an6Mbps':oriWORPIfDDRSMinReqSNRdot11an6Mbps,'oriWORPIfDDRSMinReqSNRdot11an9Mbps':oriWORPIfDDRSMinReqSNRdot11an9Mbps,'oriWORPIfDDRSMinReqSNRdot11an12Mbps':oriWORPIfDDRSMinReqSNRdot11an12Mbps,'oriWORPIfDDRSMinReqSNRdot11an18Mbps':oriWORPIfDDRSMinReqSNRdot11an18Mbps,'oriWORPIfDDRSMinReqSNRdot11an24Mbps':oriWORPIfDDRSMinReqSNRdot11an24Mbps,'oriWORPIfDDRSMinReqSNRdot11an36Mbps':oriWORPIfDDRSMinReqSNRdot11an36Mbps,'oriWORPIfDDRSMinReqSNRdot11an48Mbps':oriWORPIfDDRSMinReqSNRdot11an48Mbps,'oriWORPIfDDRSMinReqSNRdot11an54Mbps':oriWORPIfDDRSMinReqSNRdot11an54Mbps,'oriWORPIfDDRSMinReqSNRdot11at12Mbps':oriWORPIfDDRSMinReqSNRdot11at12Mbps,'oriWORPIfDDRSMinReqSNRdot11at18Mbps':oriWORPIfDDRSMinReqSNRdot11at18Mbps,'oriWORPIfDDRSMinReqSNRdot11at24Mbps':oriWORPIfDDRSMinReqSNRdot11at24Mbps,'oriWORPIfDDRSMinReqSNRdot11at36Mbps':oriWORPIfDDRSMinReqSNRdot11at36Mbps,'oriWORPIfDDRSMinReqSNRdot11at48Mbps':oriWORPIfDDRSMinReqSNRdot11at48Mbps,'oriWORPIfDDRSMinReqSNRdot11at72Mbps':oriWORPIfDDRSMinReqSNRdot11at72Mbps,'oriWORPIfDDRSMinReqSNRdot11at96Mbps':oriWORPIfDDRSMinReqSNRdot11at96Mbps,'oriWORPIfDDRSMinReqSNRdot11at108Mbps':oriWORPIfDDRSMinReqSNRdot11at108Mbps,'oriWORPIfDDRSDataRateIncAvgSNRThreshold':oriWORPIfDDRSDataRateIncAvgSNRThreshold,'oriWORPIfDDRSDataRateIncReqSNRThreshold':oriWORPIfDDRSDataRateIncReqSNRThreshold,'oriWORPIfDDRSDataRateDecReqSNRThreshold':oriWORPIfDDRSDataRateDecReqSNRThreshold,'oriWORPIfDDRSDataRateIncPercentThreshold':oriWORPIfDDRSDataRateIncPercentThreshold,'oriWORPIfDDRSDataRateDecPercentThreshold':oriWORPIfDDRSDataRateDecPercentThreshold,'orinocoWORPIfBSU':orinocoWORPIfBSU,'orinocoWORPIfBSUStat':orinocoWORPIfBSUStat,'orinocoWORPIfBSUStatMACAddress':orinocoWORPIfBSUStatMACAddress,'orinocoWORPIfBSUStatLocalTxRate':orinocoWORPIfBSUStatLocalTxRate,'orinocoWORPIfBSUStatRemoteTxRate':orinocoWORPIfBSUStatRemoteTxRate,'orinocoWORPIfBSUStatAverageLocalSignal':orinocoWORPIfBSUStatAverageLocalSignal,'orinocoWORPIfBSUStatAverageLocalNoise':orinocoWORPIfBSUStatAverageLocalNoise,'orinocoWORPIfBSUStatAverageRemoteSignal':orinocoWORPIfBSUStatAverageRemoteSignal,'orinocoWORPIfBSUStatAverageRemoteNoise':orinocoWORPIfBSUStatAverageRemoteNoise,'orinocoNet':orinocoNet,'orinocoNetIP':orinocoNetIP,'oriNetworkIPConfigTable':oriNetworkIPConfigTable,'oriNetworkIPConfigTableEntry':oriNetworkIPConfigTableEntry,_A9:oriNetworkIPConfigTableIndex,'oriNetworkIPConfigIPAddress':oriNetworkIPConfigIPAddress,'oriNetworkIPConfigSubnetMask':oriNetworkIPConfigSubnetMask,'oriNetworkIPDefaultRouterIPAddress':oriNetworkIPDefaultRouterIPAddress,'oriNetworkIPDefaultTTL':oriNetworkIPDefaultTTL,'oriNetworkIPAddressType':oriNetworkIPAddressType,'orinocoSNMP':orinocoSNMP,'oriSNMPReadPassword':oriSNMPReadPassword,'oriSNMPReadWritePassword':oriSNMPReadWritePassword,'oriSNMPAuthorizedManagerCount':oriSNMPAuthorizedManagerCount,'oriSNMPAccessTable':oriSNMPAccessTable,'oriSNMPAccessTableEntry':oriSNMPAccessTableEntry,_AA:oriSNMPAccessTableIndex,'oriSNMPAccessTableIPAddress':oriSNMPAccessTableIPAddress,'oriSNMPAccessTableIPMask':oriSNMPAccessTableIPMask,'oriSNMPAccessTableInterfaceBitmask':oriSNMPAccessTableInterfaceBitmask,'oriSNMPAccessTableComment':oriSNMPAccessTableComment,'oriSNMPAccessTableEntryStatus':oriSNMPAccessTableEntryStatus,'oriSNMPTrapHostTable':oriSNMPTrapHostTable,'oriSNMPTrapHostTableEntry':oriSNMPTrapHostTableEntry,_AB:oriSNMPTrapHostTableIndex,'oriSNMPTrapHostTableIPAddress':oriSNMPTrapHostTableIPAddress,'oriSNMPTrapHostTablePassword':oriSNMPTrapHostTablePassword,'oriSNMPTrapHostTableComment':oriSNMPTrapHostTableComment,'oriSNMPTrapHostTableEntryStatus':oriSNMPTrapHostTableEntryStatus,'oriSNMPInterfaceBitmask':oriSNMPInterfaceBitmask,'oriSNMPErrorMessage':oriSNMPErrorMessage,'oriSNMPAccessTableStatus':oriSNMPAccessTableStatus,'oriSNMPTrapType':oriSNMPTrapType,'oriSNMPSecureManagementStatus':oriSNMPSecureManagementStatus,'oriSNMPV3AuthPassword':oriSNMPV3AuthPassword,'oriSNMPV3PrivPassword':oriSNMPV3PrivPassword,'orinocoFiltering':orinocoFiltering,'orinocoProtocolFilter':orinocoProtocolFilter,'oriProtocolFilterOperationType':oriProtocolFilterOperationType,'oriProtocolFilterTable':oriProtocolFilterTable,'oriProtocolFilterTableEntry':oriProtocolFilterTableEntry,_AC:oriProtocolFilterTableIndex,'oriProtocolFilterProtocol':oriProtocolFilterProtocol,'oriProtocolFilterProtocolComment':oriProtocolFilterProtocolComment,'oriProtocolFilterTableEntryStatus':oriProtocolFilterTableEntryStatus,'oriProtocolFilterTableInterfaceBitmask':oriProtocolFilterTableInterfaceBitmask,'oriProtocolFilterProtocolString':oriProtocolFilterProtocolString,'oriProtocolFilterInterfaceBitmask':oriProtocolFilterInterfaceBitmask,'orinocoAccessControl':orinocoAccessControl,'oriAccessControlStatus':oriAccessControlStatus,'oriAccessControlOperationType':oriAccessControlOperationType,'oriAccessControlTable':oriAccessControlTable,'oriAccessControlEntry':oriAccessControlEntry,_AD:oriAccessControlTableIndex,'oriAccessControlTableMACAddress':oriAccessControlTableMACAddress,'oriAccessControlTableComment':oriAccessControlTableComment,'oriAccessControlTableEntryStatus':oriAccessControlTableEntryStatus,'orinocoStaticMACAddressFilter':orinocoStaticMACAddressFilter,'oriStaticMACAddressFilterTable':oriStaticMACAddressFilterTable,'oriStaticMACAddressFilterEntry':oriStaticMACAddressFilterEntry,_AE:oriStaticMACAddressFilterTableIndex,'oriStaticMACAddressFilterWiredAddress':oriStaticMACAddressFilterWiredAddress,'oriStaticMACAddressFilterWiredMask':oriStaticMACAddressFilterWiredMask,'oriStaticMACAddressFilterWirelessAddress':oriStaticMACAddressFilterWirelessAddress,'oriStaticMACAddressFilterWirelessMask':oriStaticMACAddressFilterWirelessMask,'oriStaticMACAddressFilterTableEntryStatus':oriStaticMACAddressFilterTableEntryStatus,'oriStaticMACAddressFilterComment':oriStaticMACAddressFilterComment,'orinocoStormThreshold':orinocoStormThreshold,'oriBroadcastAddressThreshold':oriBroadcastAddressThreshold,'oriMulticastAddressThreshold':oriMulticastAddressThreshold,'oriStormThresholdTable':oriStormThresholdTable,'oriStormThresholdTableEntry':oriStormThresholdTableEntry,'oriStormThresholdIfBroadcast':oriStormThresholdIfBroadcast,'oriStormThresholdIfMulticast':oriStormThresholdIfMulticast,'orinocoPortFilter':orinocoPortFilter,'oriPortFilterStatus':oriPortFilterStatus,'oriPortFilterOperationType':oriPortFilterOperationType,'oriPortFilterTable':oriPortFilterTable,'oriPortFilterTableEntry':oriPortFilterTableEntry,_AF:oriPortFilterTableEntryIndex,'oriPortFilterTableEntryPort':oriPortFilterTableEntryPort,'oriPortFilterTableEntryPortType':oriPortFilterTableEntryPortType,'oriPortFilterTableEntryInterfaceBitmask':oriPortFilterTableEntryInterfaceBitmask,'oriPortFilterTableEntryComment':oriPortFilterTableEntryComment,'oriPortFilterTableEntryStatus':oriPortFilterTableEntryStatus,'orinocoAdvancedFiltering':orinocoAdvancedFiltering,'oriBroadcastFilteringTable':oriBroadcastFilteringTable,'oriBroadcastFilteringTableEntry':oriBroadcastFilteringTableEntry,_AG:oriBroadcastFilteringTableIndex,'oriBroadcastFilteringProtocolName':oriBroadcastFilteringProtocolName,'oriBroadcastFilteringDirection':oriBroadcastFilteringDirection,'oriBroadcastFilteringTableEntryStatus':oriBroadcastFilteringTableEntryStatus,'orinocoPacketForwarding':orinocoPacketForwarding,'oriPacketForwardingStatus':oriPacketForwardingStatus,'oriPacketForwardingMACAddress':oriPacketForwardingMACAddress,'oriPacketForwardingInterface':oriPacketForwardingInterface,'orinocoIBSSTraffic':orinocoIBSSTraffic,'oriIBSSTrafficOperation':oriIBSSTrafficOperation,'orinocoIntraCellBlocking':orinocoIntraCellBlocking,'oriIntraCellBlockingStatus':oriIntraCellBlockingStatus,'oriIntraCellBlockingMACTable':oriIntraCellBlockingMACTable,'oriIntraCellBlockingMACTableEntry':oriIntraCellBlockingMACTableEntry,_AH:oriIntraCellBlockingMACTableIndex,'oriIntraCellBlockingMACTableMACAddress':oriIntraCellBlockingMACTableMACAddress,'oriIntraCellBlockingMACTableGroupID1':oriIntraCellBlockingMACTableGroupID1,'oriIntraCellBlockingMACTableGroupID2':oriIntraCellBlockingMACTableGroupID2,'oriIntraCellBlockingMACTableGroupID3':oriIntraCellBlockingMACTableGroupID3,'oriIntraCellBlockingMACTableGroupID4':oriIntraCellBlockingMACTableGroupID4,'oriIntraCellBlockingMACTableGroupID5':oriIntraCellBlockingMACTableGroupID5,'oriIntraCellBlockingMACTableGroupID6':oriIntraCellBlockingMACTableGroupID6,'oriIntraCellBlockingMACTableGroupID7':oriIntraCellBlockingMACTableGroupID7,'oriIntraCellBlockingMACTableGroupID8':oriIntraCellBlockingMACTableGroupID8,'oriIntraCellBlockingMACTableGroupID9':oriIntraCellBlockingMACTableGroupID9,'oriIntraCellBlockingMACTableGroupID10':oriIntraCellBlockingMACTableGroupID10,'oriIntraCellBlockingMACTableGroupID11':oriIntraCellBlockingMACTableGroupID11,'oriIntraCellBlockingMACTableGroupID12':oriIntraCellBlockingMACTableGroupID12,'oriIntraCellBlockingMACTableGroupID13':oriIntraCellBlockingMACTableGroupID13,'oriIntraCellBlockingMACTableGroupID14':oriIntraCellBlockingMACTableGroupID14,'oriIntraCellBlockingMACTableGroupID15':oriIntraCellBlockingMACTableGroupID15,'oriIntraCellBlockingMACTableGroupID16':oriIntraCellBlockingMACTableGroupID16,'oriIntraCellBlockingMACTableEntryStatus':oriIntraCellBlockingMACTableEntryStatus,'oriIntraCellBlockingGroupTable':oriIntraCellBlockingGroupTable,'oriIntraCellBlockingGroupTableEntry':oriIntraCellBlockingGroupTableEntry,_AI:oriIntraCellBlockingGroupTableIndex,'oriIntraCellBlockingGroupTableName':oriIntraCellBlockingGroupTableName,'oriIntraCellBlockingGroupTableEntryStatus':oriIntraCellBlockingGroupTableEntryStatus,'orinocoSecurityGw':orinocoSecurityGw,'oriSecurityGwStatus':oriSecurityGwStatus,'oriSecurityGwMac':oriSecurityGwMac,'orinocoRADIUS':orinocoRADIUS,'orinocoRADIUSAuth':orinocoRADIUSAuth,'oriRADIUSAuthServerTable':oriRADIUSAuthServerTable,'oriRADIUSAuthServerTableEntry':oriRADIUSAuthServerTableEntry,_AJ:oriRADIUSAuthServerTableIndex,'oriRADIUSAuthServerType':oriRADIUSAuthServerType,'oriRADIUSAuthServerTableEntryStatus':oriRADIUSAuthServerTableEntryStatus,'oriRADIUSAuthServerIPAddress':oriRADIUSAuthServerIPAddress,'oriRADIUSAuthServerDestPort':oriRADIUSAuthServerDestPort,'oriRADIUSAuthServerSharedSecret':oriRADIUSAuthServerSharedSecret,'oriRADIUSAuthServerResponseTime':oriRADIUSAuthServerResponseTime,'oriRADIUSAuthServerMaximumRetransmission':oriRADIUSAuthServerMaximumRetransmission,'oriRADIUSAuthClientAccessRequests':oriRADIUSAuthClientAccessRequests,'oriRADIUSAuthClientAccessRetransmissions':oriRADIUSAuthClientAccessRetransmissions,'oriRADIUSAuthClientAccessAccepts':oriRADIUSAuthClientAccessAccepts,'oriRADIUSAuthClientAccessChallenges':oriRADIUSAuthClientAccessChallenges,'oriRADIUSAuthClientAccessRejects':oriRADIUSAuthClientAccessRejects,'oriRADIUSAuthClientMalformedAccessResponses':oriRADIUSAuthClientMalformedAccessResponses,'oriRADIUSAuthClientAuthInvalidAuthenticators':oriRADIUSAuthClientAuthInvalidAuthenticators,'oriRADIUSAuthClientTimeouts':oriRADIUSAuthClientTimeouts,'oriRADIUSAuthServerNameOrIPAddress':oriRADIUSAuthServerNameOrIPAddress,'oriRADIUSAuthServerAddressingFormat':oriRADIUSAuthServerAddressingFormat,'orinocoRADIUSAcct':orinocoRADIUSAcct,'oriRADIUSAcctStatus':oriRADIUSAcctStatus,'oriRADIUSAcctInactivityTimer':oriRADIUSAcctInactivityTimer,'oriRADIUSAcctServerTable':oriRADIUSAcctServerTable,'oriRADIUSAcctServerTableEntry':oriRADIUSAcctServerTableEntry,_AN:oriRADIUSAcctServerTableIndex,'oriRADIUSAcctServerType':oriRADIUSAcctServerType,'oriRADIUSAcctServerTableEntryStatus':oriRADIUSAcctServerTableEntryStatus,'oriRADIUSAcctServerIPAddress':oriRADIUSAcctServerIPAddress,'oriRADIUSAcctServerDestPort':oriRADIUSAcctServerDestPort,'oriRADIUSAcctServerSharedSecret':oriRADIUSAcctServerSharedSecret,'oriRADIUSAcctServerResponseTime':oriRADIUSAcctServerResponseTime,'oriRADIUSAcctServerMaximumRetransmission':oriRADIUSAcctServerMaximumRetransmission,'oriRADIUSAcctClientAccountingRequests':oriRADIUSAcctClientAccountingRequests,'oriRADIUSAcctClientAccountingRetransmissions':oriRADIUSAcctClientAccountingRetransmissions,'oriRADIUSAcctClientAccountingResponses':oriRADIUSAcctClientAccountingResponses,'oriRADIUSAcctClientAcctInvalidAuthenticators':oriRADIUSAcctClientAcctInvalidAuthenticators,'oriRADIUSAcctServerNameOrIPAddress':oriRADIUSAcctServerNameOrIPAddress,'oriRADIUSAcctServerAddressingFormat':oriRADIUSAcctServerAddressingFormat,'oriRADIUSAcctUpdateInterval':oriRADIUSAcctUpdateInterval,'oriRADIUSClientInvalidServerAddress':oriRADIUSClientInvalidServerAddress,'oriRADIUSMACAccessControl':oriRADIUSMACAccessControl,'oriRADIUSAuthorizationLifeTime':oriRADIUSAuthorizationLifeTime,'oriRADIUSMACAddressFormat':oriRADIUSMACAddressFormat,'oriRADIUSLocalUserStatus':oriRADIUSLocalUserStatus,'oriRADIUSLocalUserPassword':oriRADIUSLocalUserPassword,'oriRADIUSbasedManagementAccessProfile':oriRADIUSbasedManagementAccessProfile,'orinocoRADIUSSvrProfiles':orinocoRADIUSSvrProfiles,'oriRADIUSSvrTable':oriRADIUSSvrTable,'oriRADIUSSvrTableEntry':oriRADIUSSvrTableEntry,_AS:oriRADIUSSvrTableProfileIndex,_AT:oriRADIUSSvrTablePrimaryOrSecondaryIndex,'oriRADIUSSvrTableProfileName':oriRADIUSSvrTableProfileName,'oriRADIUSSvrTableAddressingFormat':oriRADIUSSvrTableAddressingFormat,'oriRADIUSSvrTableNameOrIPAddress':oriRADIUSSvrTableNameOrIPAddress,'oriRADIUSSvrTableDestPort':oriRADIUSSvrTableDestPort,'oriRADIUSSvrTableSharedSecret':oriRADIUSSvrTableSharedSecret,'oriRADIUSSvrTableResponseTime':oriRADIUSSvrTableResponseTime,'oriRADIUSSvrTableMaximumRetransmission':oriRADIUSSvrTableMaximumRetransmission,'oriRADIUSSvrTableVLANID':oriRADIUSSvrTableVLANID,'oriRADIUSSvrTableMACAddressFormat':oriRADIUSSvrTableMACAddressFormat,'oriRADIUSSvrTableAuthorizationLifeTime':oriRADIUSSvrTableAuthorizationLifeTime,'oriRADIUSSvrTableAccountingInactivityTimer':oriRADIUSSvrTableAccountingInactivityTimer,'oriRADIUSSvrTableAccountingUpdateInterval':oriRADIUSSvrTableAccountingUpdateInterval,'oriRADIUSSvrTableRowStatus':oriRADIUSSvrTableRowStatus,'oriRADIUSClientInvalidSvrAddress':oriRADIUSClientInvalidSvrAddress,'oriRADIUSAuthClientStatTable':oriRADIUSAuthClientStatTable,'oriRADIUSAuthClientStatTableEntry':oriRADIUSAuthClientStatTableEntry,_AU:oriRADIUSAuthClientStatTableIndex,_AV:oriRADIUSAuthClientStatTablePrimaryOrSecondaryIndex,'oriRADIUSAuthClientStatTableAccessRequests':oriRADIUSAuthClientStatTableAccessRequests,'oriRADIUSAuthClientStatTableAccessRetransmissions':oriRADIUSAuthClientStatTableAccessRetransmissions,'oriRADIUSAuthClientStatTableAccessAccepts':oriRADIUSAuthClientStatTableAccessAccepts,'oriRADIUSAuthClientStatTableAccessChallenges':oriRADIUSAuthClientStatTableAccessChallenges,'oriRADIUSAuthClientStatTableAccessRejects':oriRADIUSAuthClientStatTableAccessRejects,'oriRADIUSAuthClientStatTableMalformedAccessResponses':oriRADIUSAuthClientStatTableMalformedAccessResponses,'oriRADIUSAuthClientStatTableBadAuthenticators':oriRADIUSAuthClientStatTableBadAuthenticators,'oriRADIUSAuthClientStatTableTimeouts':oriRADIUSAuthClientStatTableTimeouts,'oriRADIUSAcctClientStatTable':oriRADIUSAcctClientStatTable,'oriRADIUSAcctClientStatTableEntry':oriRADIUSAcctClientStatTableEntry,_AW:oriRADIUSAcctClientStatTableIndex,_AX:oriRADIUSAcctClientStatTablePrimaryOrSecondaryIndex,'oriRADIUSAcctClientStatTableAccountingRequests':oriRADIUSAcctClientStatTableAccountingRequests,'oriRADIUSAcctClientStatTableAccountingRetransmissions':oriRADIUSAcctClientStatTableAccountingRetransmissions,'oriRADIUSAcctClientStatTableAccountingResponses':oriRADIUSAcctClientStatTableAccountingResponses,'oriRADIUSAcctClientStatTableBadAuthenticators':oriRADIUSAcctClientStatTableBadAuthenticators,'orinocoTelnet':orinocoTelnet,'oriTelnetSessions':oriTelnetSessions,'oriTelnetPassword':oriTelnetPassword,'oriTelnetPort':oriTelnetPort,'oriTelnetLoginTimeout':oriTelnetLoginTimeout,'oriTelnetIdleTimeout':oriTelnetIdleTimeout,'oriTelnetInterfaceBitmask':oriTelnetInterfaceBitmask,'oriTelnetSSHStatus':oriTelnetSSHStatus,'oriTelnetSSHHostKeyStatus':oriTelnetSSHHostKeyStatus,'oriTelnetSSHFingerPrint':oriTelnetSSHFingerPrint,'oriTelnetRADIUSAccessControl':oriTelnetRADIUSAccessControl,'orinocoTFTP':orinocoTFTP,'oriTFTPServerIPAddress':oriTFTPServerIPAddress,'oriTFTPFileName':oriTFTPFileName,'oriTFTPFileType':oriTFTPFileType,'oriTFTPOperation':oriTFTPOperation,'oriTFTPFileMode':oriTFTPFileMode,'oriTFTPOperationStatus':oriTFTPOperationStatus,'oriTFTPAutoConfigStatus':oriTFTPAutoConfigStatus,_Ay:oriTFTPAutoConfigFilename,_Az:oriTFTPAutoConfigServerIPAddress,'oriTFTPDowngrade':oriTFTPDowngrade,'orinocoSerial':orinocoSerial,'oriSerialBaudRate':oriSerialBaudRate,'oriSerialDataBits':oriSerialDataBits,'oriSerialParity':oriSerialParity,'oriSerialStopBits':oriSerialStopBits,'oriSerialFlowControl':oriSerialFlowControl,'orinocoIAPP':orinocoIAPP,'oriIAPPStatus':oriIAPPStatus,'oriIAPPPeriodicAnnounceInterval':oriIAPPPeriodicAnnounceInterval,'oriIAPPAnnounceResponseTime':oriIAPPAnnounceResponseTime,'oriIAPPHandoverTimeout':oriIAPPHandoverTimeout,'oriIAPPMaximumHandoverRetransmissions':oriIAPPMaximumHandoverRetransmissions,'oriIAPPAnnounceRequestSent':oriIAPPAnnounceRequestSent,'oriIAPPAnnounceRequestReceived':oriIAPPAnnounceRequestReceived,'oriIAPPAnnounceResponseSent':oriIAPPAnnounceResponseSent,'oriIAPPAnnounceResponseReceived':oriIAPPAnnounceResponseReceived,'oriIAPPHandoverRequestSent':oriIAPPHandoverRequestSent,'oriIAPPHandoverRequestReceived':oriIAPPHandoverRequestReceived,'oriIAPPHandoverRequestRetransmissions':oriIAPPHandoverRequestRetransmissions,'oriIAPPHandoverResponseSent':oriIAPPHandoverResponseSent,'oriIAPPHandoverResponseReceived':oriIAPPHandoverResponseReceived,'oriIAPPPDUsDropped':oriIAPPPDUsDropped,'oriIAPPRoamingClients':oriIAPPRoamingClients,'oriIAPPMACIPTable':oriIAPPMACIPTable,'oriIAPPMACIPTableEntry':oriIAPPMACIPTableEntry,_AY:oriIAPPMACIPTableIndex,'oriIAPPMACIPTableSystemName':oriIAPPMACIPTableSystemName,'oriIAPPMACIPTableIPAddress':oriIAPPMACIPTableIPAddress,'oriIAPPMACIPTableBSSID':oriIAPPMACIPTableBSSID,'oriIAPPMACIPTableESSID':oriIAPPMACIPTableESSID,'oriIAPPSendAnnounceRequestOnStart':oriIAPPSendAnnounceRequestOnStart,'orinocoLinkTest':orinocoLinkTest,'oriLinkTestTimeOut':oriLinkTestTimeOut,'oriLinkTestInterval':oriLinkTestInterval,'oriLinkTestExplore':oriLinkTestExplore,'oriLinkTestTable':oriLinkTestTable,'oriLinkTestTableEntry':oriLinkTestTableEntry,_r:oriLinkTestTableIndex,'oriLinkTestInProgress':oriLinkTestInProgress,'oriLinkTestStationName':oriLinkTestStationName,'oriLinkTestMACAddress':oriLinkTestMACAddress,'oriLinkTestStationProfile':oriLinkTestStationProfile,'oriLinkTestOurCurSignalLevel':oriLinkTestOurCurSignalLevel,'oriLinkTestOurCurNoiseLevel':oriLinkTestOurCurNoiseLevel,'oriLinkTestOurCurSNR':oriLinkTestOurCurSNR,'oriLinkTestOurMinSignalLevel':oriLinkTestOurMinSignalLevel,'oriLinkTestOurMinNoiseLevel':oriLinkTestOurMinNoiseLevel,'oriLinkTestOurMinSNR':oriLinkTestOurMinSNR,'oriLinkTestOurMaxSignalLevel':oriLinkTestOurMaxSignalLevel,'oriLinkTestOurMaxNoiseLevel':oriLinkTestOurMaxNoiseLevel,'oriLinkTestOurMaxSNR':oriLinkTestOurMaxSNR,'oriLinkTestOurLowFrameCount':oriLinkTestOurLowFrameCount,'oriLinkTestOurStandardFrameCount':oriLinkTestOurStandardFrameCount,'oriLinkTestOurMediumFrameCount':oriLinkTestOurMediumFrameCount,'oriLinkTestOurHighFrameCount':oriLinkTestOurHighFrameCount,'oriLinkTestHisCurSignalLevel':oriLinkTestHisCurSignalLevel,'oriLinkTestHisCurNoiseLevel':oriLinkTestHisCurNoiseLevel,'oriLinkTestHisCurSNR':oriLinkTestHisCurSNR,'oriLinkTestHisMinSignalLevel':oriLinkTestHisMinSignalLevel,'oriLinkTestHisMinNoiseLevel':oriLinkTestHisMinNoiseLevel,'oriLinkTestHisMinSNR':oriLinkTestHisMinSNR,'oriLinkTestHisMaxSignalLevel':oriLinkTestHisMaxSignalLevel,'oriLinkTestHisMaxNoiseLevel':oriLinkTestHisMaxNoiseLevel,'oriLinkTestHisMaxSNR':oriLinkTestHisMaxSNR,'oriLinkTestHisLowFrameCount':oriLinkTestHisLowFrameCount,'oriLinkTestHisStandardFrameCount':oriLinkTestHisStandardFrameCount,'oriLinkTestHisMediumFrameCount':oriLinkTestHisMediumFrameCount,'oriLinkTestHisHighFrameCount':oriLinkTestHisHighFrameCount,'oriLinkTestInterface':oriLinkTestInterface,'oriLinkTestRadioType':oriLinkTestRadioType,'oriLinkTestDataRateTable':oriLinkTestDataRateTable,'oriLinkTestDataRateTableEntry':oriLinkTestDataRateTableEntry,_AZ:oriLinkTestDataRateTableIndex,'oriLinkTestDataRateTableRemoteCount':oriLinkTestDataRateTableRemoteCount,'oriLinkTestDataRateTableLocalCount':oriLinkTestDataRateTableLocalCount,'orinocoLinkInt':orinocoLinkInt,'oriLinkIntStatus':oriLinkIntStatus,'oriLinkIntPollInterval':oriLinkIntPollInterval,'oriLinkIntPollRetransmissions':oriLinkIntPollRetransmissions,'oriLinkIntTable':oriLinkIntTable,'oriLinkIntTableEntry':oriLinkIntTableEntry,_Aa:oriLinkIntTableIndex,'oriLinkIntTableTargetIPAddress':oriLinkIntTableTargetIPAddress,'oriLinkIntTableComment':oriLinkIntTableComment,'oriLinkIntTableEntryStatus':oriLinkIntTableEntryStatus,'orinocoUPSD':orinocoUPSD,'oriUPSDGPRInterval':oriUPSDGPRInterval,'oriUPSDMaxActiveSU':oriUPSDMaxActiveSU,'oriUPSDE911Reserved':oriUPSDE911Reserved,'oriUPSDRoamingReserved':oriUPSDRoamingReserved,'orinocoQoS':orinocoQoS,'oriQoSPolicyTable':oriQoSPolicyTable,'oriQoSPolicyTableEntry':oriQoSPolicyTableEntry,_Ab:oriQoSPolicyTableIndex,_Ac:oriQoSPolicyTableSecIndex,'oriQoSPolicyName':oriQoSPolicyName,'oriQoSPolicyType':oriQoSPolicyType,'oriQoSPolicyPriorityMapping':oriQoSPolicyPriorityMapping,'oriQoSPolicyMarkingStatus':oriQoSPolicyMarkingStatus,'oriQoSPolicyTableRowStatus':oriQoSPolicyTableRowStatus,'oriQoSDot1DToDot1pMappingTable':oriQoSDot1DToDot1pMappingTable,'oriQoSDot1DToDot1pMappingTableEntry':oriQoSDot1DToDot1pMappingTableEntry,_Ad:oriQoSDot1DToDot1pMappingTableIndex,_Ae:oriQoSDot1dPriority,'oriQoSDot1pPriority':oriQoSDot1pPriority,'oriQoSDot1DToDot1pMappingTableRowStatus':oriQoSDot1DToDot1pMappingTableRowStatus,'oriQoSDot1DToIPDSCPMappingTable':oriQoSDot1DToIPDSCPMappingTable,'oriQoSDot1DToIPDSCPMappingTableEntry':oriQoSDot1DToIPDSCPMappingTableEntry,_Af:oriQoSDot1DToIPDSCPMappingTableIndex,_Ag:oriQoSDot1DToIPDSCPPriority,'oriQoSIPDSCPLowerLimit':oriQoSIPDSCPLowerLimit,'oriQoSIPDSCPUpperLimit':oriQoSIPDSCPUpperLimit,'oriQoSDot1DToIPDSCPMappingTableRowStatus':oriQoSDot1DToIPDSCPMappingTableRowStatus,'orinocoDHCP':orinocoDHCP,'orinocoDHCPServer':orinocoDHCPServer,'oriDHCPServerStatus':oriDHCPServerStatus,'oriDHCPServerIPPoolTable':oriDHCPServerIPPoolTable,'oriDHCPServerIPPoolTableEntry':oriDHCPServerIPPoolTableEntry,_Ah:oriDHCPServerIPPoolTableIndex,'oriDHCPServerIPPoolTableStartIPAddress':oriDHCPServerIPPoolTableStartIPAddress,'oriDHCPServerIPPoolTableEndIPAddress':oriDHCPServerIPPoolTableEndIPAddress,'oriDHCPServerIPPoolTableWidth':oriDHCPServerIPPoolTableWidth,'oriDHCPServerIPPoolTableDefaultLeaseTime':oriDHCPServerIPPoolTableDefaultLeaseTime,'oriDHCPServerIPPoolTableMaximumLeaseTime':oriDHCPServerIPPoolTableMaximumLeaseTime,'oriDHCPServerIPPoolTableComment':oriDHCPServerIPPoolTableComment,'oriDHCPServerIPPoolTableEntryStatus':oriDHCPServerIPPoolTableEntryStatus,'oriDHCPServerDefaultGatewayIPAddress':oriDHCPServerDefaultGatewayIPAddress,'oriDHCPServerSubnetMask':oriDHCPServerSubnetMask,'oriDHCPServerNumIPPoolTableEntries':oriDHCPServerNumIPPoolTableEntries,'oriDHCPServerPrimaryDNSIPAddress':oriDHCPServerPrimaryDNSIPAddress,'oriDHCPServerSecondaryDNSIPAddress':oriDHCPServerSecondaryDNSIPAddress,'orinocoDHCPClient':orinocoDHCPClient,'oriDHCPClientID':oriDHCPClientID,'oriDHCPClientInterfaceBitmask':oriDHCPClientInterfaceBitmask,'orinocoDHCPRelay':orinocoDHCPRelay,'oriDHCPRelayStatus':oriDHCPRelayStatus,'oriDHCPRelayDHCPServerTable':oriDHCPRelayDHCPServerTable,'oriDHCPRelayDHCPServerTableEntry':oriDHCPRelayDHCPServerTableEntry,_Ai:oriDHCPRelayDHCPServerTableIndex,'oriDHCPRelayDHCPServerTableIpAddress':oriDHCPRelayDHCPServerTableIpAddress,'oriDHCPRelayDHCPServerTableComment':oriDHCPRelayDHCPServerTableComment,'oriDHCPRelayDHCPServerTableEntryStatus':oriDHCPRelayDHCPServerTableEntryStatus,'orinocoHTTP':orinocoHTTP,'oriHTTPInterfaceBitmask':oriHTTPInterfaceBitmask,'oriHTTPPassword':oriHTTPPassword,'oriHTTPPort':oriHTTPPort,'oriHTTPWebSitenameTable':oriHTTPWebSitenameTable,'oriHTTPWebSitenameTableEntry':oriHTTPWebSitenameTableEntry,_Aj:oriHTTPWebSitenameTableIndex,'oriHTTPWebSiteFilename':oriHTTPWebSiteFilename,'oriHTTPWebSiteLanguage':oriHTTPWebSiteLanguage,'oriHTTPWebSiteDescription':oriHTTPWebSiteDescription,'oriHTTPWebSitenameTableStatus':oriHTTPWebSitenameTableStatus,'oriHTTPRefreshDelay':oriHTTPRefreshDelay,'oriHTTPHelpInformationLink':oriHTTPHelpInformationLink,'oriHTTPSSLStatus':oriHTTPSSLStatus,'oriHTTPSSLPassphrase':oriHTTPSSLPassphrase,'oriHTTPSetupWizardStatus':oriHTTPSetupWizardStatus,'oriHTTPRADIUSAccessControl':oriHTTPRADIUSAccessControl,'orinocoWDS':orinocoWDS,'oriWDSSetupTable':oriWDSSetupTable,'oriWDSSetupTableEntry':oriWDSSetupTableEntry,_Ak:oriWDSSetupTablePortIndex,'oriWDSSetupTableEntryStatus':oriWDSSetupTableEntryStatus,'oriWDSSetupTablePartnerMACAddress':oriWDSSetupTablePartnerMACAddress,'oriWDSSecurityTable':oriWDSSecurityTable,'oriWDSSecurityTableEntry':oriWDSSecurityTableEntry,'oriWDSSecurityTableSecurityMode':oriWDSSecurityTableSecurityMode,'oriWDSSecurityTableEncryptionKey0':oriWDSSecurityTableEncryptionKey0,'orinocoTrap':orinocoTrap,'oriTrapVariable':oriTrapVariable,_K:oriGenericTrapVariable,_R:oriTrapVarMACAddress,_h:oriTrapVarTFTPIPAddress,_i:oriTrapVarTFTPFilename,_j:oriTrapVarTFTPOperation,_B1:oriTrapVarUnauthorizedManagerIPaddress,_B0:oriTrapVarFailedAuthenticationType,_B2:oriTrapVarUnAuthorizedManagerCount,_v:oriTrapVarTaskSuspended,'oriConfigurationTrapsStatus':oriConfigurationTrapsStatus,'oriSecurityTrapsStatus':oriSecurityTrapsStatus,'oriWirelessIfTrapsStatus':oriWirelessIfTrapsStatus,'oriOperationalTrapsStatus':oriOperationalTrapsStatus,'oriFlashMemoryTrapsStatus':oriFlashMemoryTrapsStatus,'oriTFTPTrapsStatus':oriTFTPTrapsStatus,'oriTrapsImageStatus':oriTrapsImageStatus,_u:oriTrapVarUnauthorizedClientMACAddress,_P:oriTrapVarWirelessCard,'oriADSLIfTrapsStatus':oriADSLIfTrapsStatus,'oriWORPTrapsStatus':oriWORPTrapsStatus,_w:oriTrapVarInterface,_g:oriTrapVarBatchCLIFilename,_t:oriTrapVarBatchCLIMessage,_A_:oriTrapVarBatchCLILineNumber,_B4:oriTrapVarDHCPServerIPAddress,_B5:oriTrapVarIPAddress,_B6:oriTrapVarSubnetMask,_B7:oriTrapVarDefaultRouterIPAddress,'oriConfigurationTraps':oriConfigurationTraps,'oriTrapDNSIPNotConfigured':oriTrapDNSIPNotConfigured,'oriTrapRADIUSAuthenticationNotConfigured':oriTrapRADIUSAuthenticationNotConfigured,'oriTrapRADIUSAccountingNotConfigured':oriTrapRADIUSAccountingNotConfigured,'oriTrapDuplicateIPAddressEncountered':oriTrapDuplicateIPAddressEncountered,'oriTrapDHCPRelayServerTableNotConfigured':oriTrapDHCPRelayServerTableNotConfigured,'oriTrapWORPIfNetworkSecretNotConfigured':oriTrapWORPIfNetworkSecretNotConfigured,'oriTrapVLANIDInvalidConfiguration':oriTrapVLANIDInvalidConfiguration,'oriTrapAutoConfigFailure':oriTrapAutoConfigFailure,'oriTrapBatchExecFailure':oriTrapBatchExecFailure,'oriTrapBatchFileExecStart':oriTrapBatchFileExecStart,'oriTrapBatchFileExecEnd':oriTrapBatchFileExecEnd,'oriSecurityTraps':oriSecurityTraps,'oriTrapInvalidEncryptionKey':oriTrapInvalidEncryptionKey,'oriTrapAuthenticationFailure':oriTrapAuthenticationFailure,'oriTrapUnauthorizedManagerDetected':oriTrapUnauthorizedManagerDetected,'oriTrapRADScanComplete':oriTrapRADScanComplete,'oriTrapRADScanResults':oriTrapRADScanResults,'oriTrapRogueScanStationDetected':oriTrapRogueScanStationDetected,'oriTrapRogueScanCycleComplete':oriTrapRogueScanCycleComplete,'oriWirelessIfTraps':oriWirelessIfTraps,'oriTrapWLCNotPresent':oriTrapWLCNotPresent,'oriTrapWLCFailure':oriTrapWLCFailure,'oriTrapWLCRemoval':oriTrapWLCRemoval,'oriTrapWLCIncompatibleFirmware':oriTrapWLCIncompatibleFirmware,'oriTrapWLCVoltageDiscrepancy':oriTrapWLCVoltageDiscrepancy,'oriTrapWLCIncompatibleVendor':oriTrapWLCIncompatibleVendor,'oriTrapWLCFirmwareDownloadFailure':oriTrapWLCFirmwareDownloadFailure,'oriTrapWLCFirmwareFailure':oriTrapWLCFirmwareFailure,'oriTrapWLCRadarInterferenceDetected':oriTrapWLCRadarInterferenceDetected,'oriOperationalTraps':oriOperationalTraps,'oriTrapUnrecoverableSoftwareErrorDetected':oriTrapUnrecoverableSoftwareErrorDetected,'oriTrapRADIUSServerNotResponding':oriTrapRADIUSServerNotResponding,'oriTrapModuleNotInitialized':oriTrapModuleNotInitialized,'oriTrapDeviceRebooting':oriTrapDeviceRebooting,'oriTrapTaskSuspended':oriTrapTaskSuspended,'oriTrapBootPFailed':oriTrapBootPFailed,'oriTrapDHCPFailed':oriTrapDHCPFailed,'oriTrapDNSClientLookupFailure':oriTrapDNSClientLookupFailure,'oriTrapSNTPFailure':oriTrapSNTPFailure,'oriTrapMaximumNumberOfSubscribersReached':oriTrapMaximumNumberOfSubscribersReached,'oriTrapSSLInitializationFailure':oriTrapSSLInitializationFailure,'oriTrapWirelessServiceShutdown':oriTrapWirelessServiceShutdown,'oriTrapWirelessServiceResumed':oriTrapWirelessServiceResumed,'oriTrapSSHInitializationStatus':oriTrapSSHInitializationStatus,'oriTrapVLANIDUserAssignment':oriTrapVLANIDUserAssignment,'oriTrapDHCPLeaseRenewal':oriTrapDHCPLeaseRenewal,'oriTrapTemperatureAlert':oriTrapTemperatureAlert,'oriFlashTraps':oriFlashTraps,'oriTrapFlashMemoryEmpty':oriTrapFlashMemoryEmpty,'oriTrapFlashMemoryCorrupted':oriTrapFlashMemoryCorrupted,'oriTrapFlashMemoryRestoringLastKnownGoodConfiguration':oriTrapFlashMemoryRestoringLastKnownGoodConfiguration,'oriTFTPTraps':oriTFTPTraps,'oriTrapTFTPFailedOperation':oriTrapTFTPFailedOperation,'oriTrapTFTPOperationInitiated':oriTrapTFTPOperationInitiated,'oriTrapTFTPOperationCompleted':oriTrapTFTPOperationCompleted,'oriMiscTraps':oriMiscTraps,'oriImageTraps':oriImageTraps,'oriTrapZeroSizeImage':oriTrapZeroSizeImage,'oriTrapInvalidImage':oriTrapInvalidImage,'oriTrapImageTooLarge':oriTrapImageTooLarge,'oriTrapIncompatibleImage':oriTrapIncompatibleImage,'oriTrapInvalidImageDigitalSignature':oriTrapInvalidImageDigitalSignature,'oriWORPTraps':oriWORPTraps,'oriWORPStationRegister':oriWORPStationRegister,'oriWORPStationDeRegister':oriWORPStationDeRegister,'oriSysFeatureTraps':oriSysFeatureTraps,'oriTrapIncompatibleLicenseFile':oriTrapIncompatibleLicenseFile,'oriTrapFeatureNotSupported':oriTrapFeatureNotSupported,'oriTrapZeroLicenseFiles':oriTrapZeroLicenseFiles,'oriTrapInvalidLicenseFile':oriTrapInvalidLicenseFile,'oriTrapUselessLicense':oriTrapUselessLicense,'orinocoIPARP':orinocoIPARP,'oriProxyARPStatus':oriProxyARPStatus,'oriIPARPFilteringStatus':oriIPARPFilteringStatus,'oriIPARPFilteringIPAddress':oriIPARPFilteringIPAddress,'oriIPARPFilteringSubnetMask':oriIPARPFilteringSubnetMask,'orinocoSpanningTree':orinocoSpanningTree,'oriSpanningTreeStatus':oriSpanningTreeStatus,'orinocoSecurity':orinocoSecurity,'oriSecurityConfiguration':oriSecurityConfiguration,'oriSecurityEncryptionKeyLengthTable':oriSecurityEncryptionKeyLengthTable,'oriSecurityEncryptionKeyLengthTableEntry':oriSecurityEncryptionKeyLengthTableEntry,'oriSecurityEncryptionKeyLength':oriSecurityEncryptionKeyLength,'oriSecurityRekeyingInterval':oriSecurityRekeyingInterval,'orinocoRAD':orinocoRAD,'oriRADStatus':oriRADStatus,'oriRADInterval':oriRADInterval,'oriRADInterfaceBitmask':oriRADInterfaceBitmask,'oriRADLastSuccessfulScanTime':oriRADLastSuccessfulScanTime,'oriRADAccessPointCount':oriRADAccessPointCount,'oriRADScanResultsTable':oriRADScanResultsTable,'oriRADScanResultsTableEntry':oriRADScanResultsTableEntry,_Al:oriRADScanResultsTableIndex,'oriRADScanResultsMACAddress':oriRADScanResultsMACAddress,'oriRADScanResultsFrequencyChannel':oriRADScanResultsFrequencyChannel,'oriSecurityConfigTable':oriSecurityConfigTable,'oriSecurityConfigTableEntry':oriSecurityConfigTableEntry,'oriSecurityConfigTableSupportedSecurityModes':oriSecurityConfigTableSupportedSecurityModes,'oriSecurityConfigTableSecurityMode':oriSecurityConfigTableSecurityMode,'oriSecurityConfigTableRekeyingInterval':oriSecurityConfigTableRekeyingInterval,'oriSecurityConfigTableEncryptionKeyLength':oriSecurityConfigTableEncryptionKeyLength,'oriSecurityHwConfigResetStatus':oriSecurityHwConfigResetStatus,'oriSecurityHwConfigResetPassword':oriSecurityHwConfigResetPassword,'orinocoRogueScan':orinocoRogueScan,'oriRogueScanConfigTable':oriRogueScanConfigTable,'oriRogueScanConfigTableEntry':oriRogueScanConfigTableEntry,'oriRogueScanConfigTableScanMode':oriRogueScanConfigTableScanMode,'oriRogueScanConfigTableScanCycleTime':oriRogueScanConfigTableScanCycleTime,'oriRogueScanConfigTableScanStatus':oriRogueScanConfigTableScanStatus,'oriRogueScanStationCountWirelessCardA':oriRogueScanStationCountWirelessCardA,'oriRogueScanStationCountWirelessCardB':oriRogueScanStationCountWirelessCardB,'oriRogueScanResultsTableAgingTime':oriRogueScanResultsTableAgingTime,'oriRogueScanResultsTableClearEntries':oriRogueScanResultsTableClearEntries,'oriRogueScanResultsNotificationMode':oriRogueScanResultsNotificationMode,'oriRogueScanResultsTrapReportType':oriRogueScanResultsTrapReportType,'oriRogueScanResultsTable':oriRogueScanResultsTable,'oriRogueScanResultsTableEntry':oriRogueScanResultsTableEntry,_Am:oriRogueScanResultsTableIndex,'oriRogueScanResultsStationType':oriRogueScanResultsStationType,'oriRogueScanResultsMACAddress':oriRogueScanResultsMACAddress,'oriRogueScanResultsFrequencyChannel':oriRogueScanResultsFrequencyChannel,'oriRogueScanResultsSNR':oriRogueScanResultsSNR,'oriRogueScanResultsBSSID':oriRogueScanResultsBSSID,'oriSecurityProfileTable':oriSecurityProfileTable,'oriSecurityProfileTableEntry':oriSecurityProfileTableEntry,_An:oriSecurityProfileTableIndex,_Ao:oriSecurityProfileTableSecModeIndex,'oriSecurityProfileTableAuthenticationMode':oriSecurityProfileTableAuthenticationMode,'oriSecurityProfileTableCipherMode':oriSecurityProfileTableCipherMode,'oriSecurityProfileTableEncryptionKey0':oriSecurityProfileTableEncryptionKey0,'oriSecurityProfileTableEncryptionKey1':oriSecurityProfileTableEncryptionKey1,'oriSecurityProfileTableEncryptionKey2':oriSecurityProfileTableEncryptionKey2,'oriSecurityProfileTableEncryptionKey3':oriSecurityProfileTableEncryptionKey3,'oriSecurityProfileTableEncryptionTxKey':oriSecurityProfileTableEncryptionTxKey,'oriSecurityProfileTableEncryptionKeyLength':oriSecurityProfileTableEncryptionKeyLength,'oriSecurityProfileTablePSKValue':oriSecurityProfileTablePSKValue,'oriSecurityProfileTablePSKPassPhrase':oriSecurityProfileTablePSKPassPhrase,'oriSecurityProfileTableStatus':oriSecurityProfileTableStatus,'oriSecurityProfileFourWEPKeySupport':oriSecurityProfileFourWEPKeySupport,'orinocoPPPoE':orinocoPPPoE,'oriPPPoEStatus':oriPPPoEStatus,'oriPPPoEMaximumNumberOfSessions':oriPPPoEMaximumNumberOfSessions,'oriPPPoENumberOfActiveSessions':oriPPPoENumberOfActiveSessions,'oriPPPoESessionTable':oriPPPoESessionTable,'oriPPPoESessionTableEntry':oriPPPoESessionTableEntry,_Ap:oriPPPoESessionTableIndex,'oriPPPoESessionWANConnectMode':oriPPPoESessionWANConnectMode,'oriPPPoESessionIdleTimeOut':oriPPPoESessionIdleTimeOut,'oriPPPoESessionConnectTime':oriPPPoESessionConnectTime,'oriPPPoESessionConnectTimeLimitation':oriPPPoESessionConnectTimeLimitation,'oriPPPoESessionConfigPADITxInterval':oriPPPoESessionConfigPADITxInterval,'oriPPPoESessionConfigPADIMaxNumberOfRetries':oriPPPoESessionConfigPADIMaxNumberOfRetries,'oriPPPoESessionBindingsNumberPADITx':oriPPPoESessionBindingsNumberPADITx,'oriPPPoESessionBindingsNumberPADTTx':oriPPPoESessionBindingsNumberPADTTx,'oriPPPoESessionBindingsNumberServiceNameErrors':oriPPPoESessionBindingsNumberServiceNameErrors,'oriPPPoESessionBindingsNumberACSystemErrors':oriPPPoESessionBindingsNumberACSystemErrors,'oriPPPoESessionBindingsNumberGenericErrorsRx':oriPPPoESessionBindingsNumberGenericErrorsRx,'oriPPPoESessionBindingsNumberGenericErrorsTx':oriPPPoESessionBindingsNumberGenericErrorsTx,'oriPPPoESessionBindingsNumberMalformedPackets':oriPPPoESessionBindingsNumberMalformedPackets,'oriPPPoESessionBindingsNumberMultiplePADORx':oriPPPoESessionBindingsNumberMultiplePADORx,'oriPPPoESessionUserName':oriPPPoESessionUserName,'oriPPPoESessionUserNamePassword':oriPPPoESessionUserNamePassword,'oriPPPoESessionServiceName':oriPPPoESessionServiceName,'oriPPPoESessionISPName':oriPPPoESessionISPName,'oriPPPoESessionTableStatus':oriPPPoESessionTableStatus,'oriPPPoESessionWANManualConnect':oriPPPoESessionWANManualConnect,'oriPPPoESessionWANConnectionStatus':oriPPPoESessionWANConnectionStatus,'oriPPPoEMACtoSessionTable':oriPPPoEMACtoSessionTable,'oriPPPoEMACtoSessionTableEntry':oriPPPoEMACtoSessionTableEntry,_Aq:oriPPPoEMACtoSessionTableIndex,'oriPPPoEMACtoSessionTableMACAddress':oriPPPoEMACtoSessionTableMACAddress,'oriPPPoEMACtoSessionTableISPName':oriPPPoEMACtoSessionTableISPName,'oriPPPoEMACtoSessionTableStatus':oriPPPoEMACtoSessionTableStatus,'orinocoConfig':orinocoConfig,'oriConfigResetToDefaults':oriConfigResetToDefaults,'oriConfigFileTable':oriConfigFileTable,'oriConfigFileTableEntry':oriConfigFileTableEntry,_Ar:oriConfigFileTableIndex,'oriConfigFileName':oriConfigFileName,'oriConfigFileStatus':oriConfigFileStatus,'oriConfigSaveFile':oriConfigSaveFile,'oriConfigSaveKnownGood':oriConfigSaveKnownGood,'orinocoDNS':orinocoDNS,'oriDNSRedirectStatus':oriDNSRedirectStatus,'oriDNSRedirectMaxResponseWaitTime':oriDNSRedirectMaxResponseWaitTime,'oriDNSPrimaryDNSIPAddress':oriDNSPrimaryDNSIPAddress,'oriDNSSecondaryDNSIPAddress':oriDNSSecondaryDNSIPAddress,'orinocoDNSClient':orinocoDNSClient,'oriDNSClientStatus':oriDNSClientStatus,'oriDNSClientPrimaryServerIPAddress':oriDNSClientPrimaryServerIPAddress,'oriDNSClientSecondaryServerIPAddress':oriDNSClientSecondaryServerIPAddress,'oriDNSClientDefaultDomainName':oriDNSClientDefaultDomainName,'orinocoAOL':orinocoAOL,'oriAOLNATALGStatus':oriAOLNATALGStatus,'orinocoNAT':orinocoNAT,'oriNATStatus':oriNATStatus,'oriNATType':oriNATType,'oriNATStaticBindStatus':oriNATStaticBindStatus,'oriNATPublicIPAddress':oriNATPublicIPAddress,'oriNATStaticIPBindTable':oriNATStaticIPBindTable,'oriNATStaticIPBindTableEntry':oriNATStaticIPBindTableEntry,_As:oriNATStaticIPBindTableIndex,'oriNATStaticIPBindLocalAddress':oriNATStaticIPBindLocalAddress,'oriNATStaticIPBindRemoteAddress':oriNATStaticIPBindRemoteAddress,'oriNATStaticIPBindTableEntryStatus':oriNATStaticIPBindTableEntryStatus,'oriNATStaticPortBindTable':oriNATStaticPortBindTable,'oriNATStaticPortBindTableEntry':oriNATStaticPortBindTableEntry,_At:oriNATStaticPortBindTableIndex,'oriNATStaticPortBindLocalAddress':oriNATStaticPortBindLocalAddress,'oriNATStaticPortBindStartPortNumber':oriNATStaticPortBindStartPortNumber,'oriNATStaticPortBindEndPortNumber':oriNATStaticPortBindEndPortNumber,'oriNATStaticPortBindPortType':oriNATStaticPortBindPortType,'oriNATStaticPortBindTableEntryStatus':oriNATStaticPortBindTableEntryStatus,'orinocoSpectraLink':orinocoSpectraLink,'oriSpectraLinkStatus':oriSpectraLinkStatus,'oriSpectraLinkLegacyDeviceSupport':oriSpectraLinkLegacyDeviceSupport,'orinocoVLAN':orinocoVLAN,'oriVLANStatus':oriVLANStatus,'oriVLANMgmtIdentifier':oriVLANMgmtIdentifier,'oriVLANIDTable':oriVLANIDTable,'oriVLANIDTableEntry':oriVLANIDTableEntry,_Au:oriVLANIDTableIndex,_Ax:oriVLANIDTableIdentifier,'orinocoDMZ':orinocoDMZ,'oriDMZHostTable':oriDMZHostTable,'oriDMZHostTableEntry':oriDMZHostTableEntry,_Av:oriDMZHostTableIndex,'oriDMZHostTableHostIP':oriDMZHostTableHostIP,'oriDMZHostTableComment':oriDMZHostTableComment,'oriDMZHostTableEntryStatus':oriDMZHostTableEntryStatus,'orinocoOEM':orinocoOEM,'oriOEMName':oriOEMName,'oriOEMHomeUrl':oriOEMHomeUrl,'oriOEMProductName':oriOEMProductName,'oriOEMProductModel':oriOEMProductModel,'oriOEMLogoImageFile':oriOEMLogoImageFile,'oriOEMNoNavLogoImageFile':oriOEMNoNavLogoImageFile,'orinocoStationStatistics':orinocoStationStatistics,'oriStationStatTable':oriStationStatTable,'oriStationStatTableEntry':oriStationStatTableEntry,_n:oriStationStatTableIndex,'oriStationStatTableMACAddress':oriStationStatTableMACAddress,'oriStationStatTableIPAddress':oriStationStatTableIPAddress,'oriStationStatTableInterface':oriStationStatTableInterface,'oriStationStatTableName':oriStationStatTableName,'oriStationStatTableType':oriStationStatTableType,'oriStationStatTableMACProtocol':oriStationStatTableMACProtocol,'oriStationStatTableAdminStatus':oriStationStatTableAdminStatus,'oriStationStatTableOperStatus':oriStationStatTableOperStatus,'oriStationStatTableLastChange':oriStationStatTableLastChange,'oriStationStatTableLastState':oriStationStatTableLastState,'oriStationStatTableInOctets':oriStationStatTableInOctets,'oriStationStatTableInUcastPkts':oriStationStatTableInUcastPkts,'oriStationStatTableInNUcastPkts':oriStationStatTableInNUcastPkts,'oriStationStatTableInDiscards':oriStationStatTableInDiscards,'oriStationStatTableOutOctets':oriStationStatTableOutOctets,'oriStationStatTableOutUcastPkts':oriStationStatTableOutUcastPkts,'oriStationStatTableOutNUcastPkts':oriStationStatTableOutNUcastPkts,'oriStationStatTableOutDiscards':oriStationStatTableOutDiscards,'oriStationStatTableInSignal':oriStationStatTableInSignal,'oriStationStatTableInNoise':oriStationStatTableInNoise,'oriStationStatTableRemoteSignal':oriStationStatTableRemoteSignal,'oriStationStatTableRemoteNoise':oriStationStatTableRemoteNoise,'oriStationStatTableLastInPktTime':oriStationStatTableLastInPktTime,'oriStationStatStatus':oriStationStatStatus,'oriStationStatNumberOfClients':oriStationStatNumberOfClients,'orinocoSNTP':orinocoSNTP,'oriSNTPStatus':oriSNTPStatus,'oriSNTPPrimaryServerNameOrIPAddress':oriSNTPPrimaryServerNameOrIPAddress,'oriSNTPSecondaryServerNameOrIPAddress':oriSNTPSecondaryServerNameOrIPAddress,'oriSNTPTimeZone':oriSNTPTimeZone,'oriSNTPDateAndTime':oriSNTPDateAndTime,'oriSNTPDayLightSavingTime':oriSNTPDayLightSavingTime,'oriSNTPYear':oriSNTPYear,'oriSNTPMonth':oriSNTPMonth,'oriSNTPDay':oriSNTPDay,'oriSNTPHour':oriSNTPHour,'oriSNTPMinutes':oriSNTPMinutes,'oriSNTPSeconds':oriSNTPSeconds,'orinocoNotifications':orinocoNotifications,'orinocoConformance':orinocoConformance,'orinocoGroups':orinocoGroups,'orinocoCompliances':orinocoCompliances,'orinocoProducts':orinocoProducts,'ap1000':ap1000,'rg1000':rg1000,'as1000':as1000,'as2000':as2000,'ap500':ap500,'ap2000':ap2000,'bg2000':bg2000,'rg1100':rg1100,'tmp11':tmp11,'ap600':ap600,'ap2500':ap2500,'ap4000':ap4000,'ap700':ap700})