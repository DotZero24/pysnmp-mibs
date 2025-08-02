_i='securityPortID'
_h='securityGroupID'
_g='backupIndex'
_f='switchPortStatsID'
_e='switchPortStatsGroupID'
_d='switchPortID'
_c='switchPortGroupID'
_b='portID'
_a='portGroupID'
_Z='backplaneSegmentID'
_Y='backplaneGroupID'
_X='standby'
_W='unknown'
_V='groupID'
_U='disabled'
_T='enabled'
_S='sNIndex'
_R='noReset'
_Q='elh100TrapMgtIndex'
_P='elh100CommunityIndex'
_O='inactive'
_N='noLink'
_M='notApplicable'
_L='notPresent'
_K='DisplayString'
_J='oneHundredMbps'
_I='tenMbps'
_H='active'
_G='invalid'
_F='OctetString'
_E='ELH100-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_CabletronOEM_ObjectIdentity=ObjectIdentity
cabletronOEM=_CabletronOEM_ObjectIdentity((1,3,6,1,4,1,52,259))
_CabletronRepeaters_ObjectIdentity=ObjectIdentity
cabletronRepeaters=_CabletronRepeaters_ObjectIdentity((1,3,6,1,4,1,52,259,10))
_CabletronELH100_ObjectIdentity=ObjectIdentity
cabletronELH100=_CabletronELH100_ObjectIdentity((1,3,6,1,4,1,52,259,10,3))
_CabletronELH100Common_ObjectIdentity=ObjectIdentity
cabletronELH100Common=_CabletronELH100Common_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,1))
_Elh100System_ObjectIdentity=ObjectIdentity
elh100System=_Elh100System_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,1,1))
_Elh100MajorVer_Type=Integer32
_Elh100MajorVer_Object=MibScalar
elh100MajorVer=_Elh100MajorVer_Object((1,3,6,1,4,1,52,259,10,3,1,1,1),_Elh100MajorVer_Type())
elh100MajorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:elh100MajorVer.setStatus(_A)
_Elh100MinorVer_Type=Integer32
_Elh100MinorVer_Object=MibScalar
elh100MinorVer=_Elh100MinorVer_Object((1,3,6,1,4,1,52,259,10,3,1,1,2),_Elh100MinorVer_Type())
elh100MinorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:elh100MinorVer.setStatus(_A)
_Elh100HardwareVer_Type=Integer32
_Elh100HardwareVer_Object=MibScalar
elh100HardwareVer=_Elh100HardwareVer_Object((1,3,6,1,4,1,52,259,10,3,1,1,3),_Elh100HardwareVer_Type())
elh100HardwareVer.setMaxAccess(_B)
if mibBuilder.loadTexts:elh100HardwareVer.setStatus(_A)
_Elh100CommunityMgt_ObjectIdentity=ObjectIdentity
elh100CommunityMgt=_Elh100CommunityMgt_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,1,2))
_Elh100CommunityTable_Object=MibTable
elh100CommunityTable=_Elh100CommunityTable_Object((1,3,6,1,4,1,52,259,10,3,1,2,3))
if mibBuilder.loadTexts:elh100CommunityTable.setStatus(_A)
_Elh100CommunityEntry_Object=MibTableRow
elh100CommunityEntry=_Elh100CommunityEntry_Object((1,3,6,1,4,1,52,259,10,3,1,2,3,1))
elh100CommunityEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:elh100CommunityEntry.setStatus(_A)
_Elh100CommunityIndex_Type=Integer32
_Elh100CommunityIndex_Object=MibTableColumn
elh100CommunityIndex=_Elh100CommunityIndex_Object((1,3,6,1,4,1,52,259,10,3,1,2,3,1,1),_Elh100CommunityIndex_Type())
elh100CommunityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:elh100CommunityIndex.setStatus(_A)
class _Elh100CommunityRowCreation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_G,2)))
_Elh100CommunityRowCreation_Type.__name__=_C
_Elh100CommunityRowCreation_Object=MibTableColumn
elh100CommunityRowCreation=_Elh100CommunityRowCreation_Object((1,3,6,1,4,1,52,259,10,3,1,2,3,1,2),_Elh100CommunityRowCreation_Type())
elh100CommunityRowCreation.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100CommunityRowCreation.setStatus(_A)
class _Elh100CommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_Elh100CommunityString_Type.__name__=_K
_Elh100CommunityString_Object=MibTableColumn
elh100CommunityString=_Elh100CommunityString_Object((1,3,6,1,4,1,52,259,10,3,1,2,3,1,3),_Elh100CommunityString_Type())
elh100CommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100CommunityString.setStatus(_A)
class _Elh100CommunityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('readOnly',2),('readWrite',3)))
_Elh100CommunityStatus_Type.__name__=_C
_Elh100CommunityStatus_Object=MibTableColumn
elh100CommunityStatus=_Elh100CommunityStatus_Object((1,3,6,1,4,1,52,259,10,3,1,2,3,1,4),_Elh100CommunityStatus_Type())
elh100CommunityStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100CommunityStatus.setStatus(_A)
_Elh100TrapManagerMgt_ObjectIdentity=ObjectIdentity
elh100TrapManagerMgt=_Elh100TrapManagerMgt_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,1,3))
_Elh100TrapManagerTable_Object=MibTable
elh100TrapManagerTable=_Elh100TrapManagerTable_Object((1,3,6,1,4,1,52,259,10,3,1,3,2))
if mibBuilder.loadTexts:elh100TrapManagerTable.setStatus(_A)
_Elh100TrapMgtEntry_Object=MibTableRow
elh100TrapMgtEntry=_Elh100TrapMgtEntry_Object((1,3,6,1,4,1,52,259,10,3,1,3,2,1))
elh100TrapMgtEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:elh100TrapMgtEntry.setStatus(_A)
_Elh100TrapMgtIndex_Type=Integer32
_Elh100TrapMgtIndex_Object=MibTableColumn
elh100TrapMgtIndex=_Elh100TrapMgtIndex_Object((1,3,6,1,4,1,52,259,10,3,1,3,2,1,1),_Elh100TrapMgtIndex_Type())
elh100TrapMgtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:elh100TrapMgtIndex.setStatus(_A)
class _Elh100TrapMgtRowCreation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_G,2)))
_Elh100TrapMgtRowCreation_Type.__name__=_C
_Elh100TrapMgtRowCreation_Object=MibTableColumn
elh100TrapMgtRowCreation=_Elh100TrapMgtRowCreation_Object((1,3,6,1,4,1,52,259,10,3,1,3,2,1,2),_Elh100TrapMgtRowCreation_Type())
elh100TrapMgtRowCreation.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100TrapMgtRowCreation.setStatus(_A)
class _Elh100TrapMgtCommunityString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_Elh100TrapMgtCommunityString_Type.__name__=_K
_Elh100TrapMgtCommunityString_Object=MibTableColumn
elh100TrapMgtCommunityString=_Elh100TrapMgtCommunityString_Object((1,3,6,1,4,1,52,259,10,3,1,3,2,1,3),_Elh100TrapMgtCommunityString_Type())
elh100TrapMgtCommunityString.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100TrapMgtCommunityString.setStatus(_A)
_Elh100TrapMgtIpAddress_Type=IpAddress
_Elh100TrapMgtIpAddress_Object=MibTableColumn
elh100TrapMgtIpAddress=_Elh100TrapMgtIpAddress_Object((1,3,6,1,4,1,52,259,10,3,1,3,2,1,4),_Elh100TrapMgtIpAddress_Type())
elh100TrapMgtIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100TrapMgtIpAddress.setStatus(_A)
_Elh100DownloadMgt_ObjectIdentity=ObjectIdentity
elh100DownloadMgt=_Elh100DownloadMgt_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,1,4))
_Elh100DownloadServerIP_Type=IpAddress
_Elh100DownloadServerIP_Object=MibScalar
elh100DownloadServerIP=_Elh100DownloadServerIP_Object((1,3,6,1,4,1,52,259,10,3,1,4,1),_Elh100DownloadServerIP_Type())
elh100DownloadServerIP.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100DownloadServerIP.setStatus(_A)
_Elh100DownloadFilename_Type=OctetString
_Elh100DownloadFilename_Object=MibScalar
elh100DownloadFilename=_Elh100DownloadFilename_Object((1,3,6,1,4,1,52,259,10,3,1,4,2),_Elh100DownloadFilename_Type())
elh100DownloadFilename.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100DownloadFilename.setStatus(_A)
class _Elh100DownloadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permanent',1),('temporary',2)))
_Elh100DownloadMode_Type.__name__=_C
_Elh100DownloadMode_Object=MibScalar
elh100DownloadMode=_Elh100DownloadMode_Object((1,3,6,1,4,1,52,259,10,3,1,4,3),_Elh100DownloadMode_Type())
elh100DownloadMode.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100DownloadMode.setStatus(_A)
class _Elh100DownloadAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('run',1),('noRun',2)))
_Elh100DownloadAction_Type.__name__=_C
_Elh100DownloadAction_Object=MibScalar
elh100DownloadAction=_Elh100DownloadAction_Object((1,3,6,1,4,1,52,259,10,3,1,4,4),_Elh100DownloadAction_Type())
elh100DownloadAction.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100DownloadAction.setStatus(_A)
_Elh100Restart_Type=Integer32
_Elh100Restart_Object=MibScalar
elh100Restart=_Elh100Restart_Object((1,3,6,1,4,1,52,259,10,3,1,5),_Elh100Restart_Type())
elh100Restart.setMaxAccess(_D)
if mibBuilder.loadTexts:elh100Restart.setStatus(_A)
_CabletronELH100BasicCapability_ObjectIdentity=ObjectIdentity
cabletronELH100BasicCapability=_CabletronELH100BasicCapability_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,2))
_CabletronELH100StackInfo_ObjectIdentity=ObjectIdentity
cabletronELH100StackInfo=_CabletronELH100StackInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,2,1))
_StackInusedIP_Type=IpAddress
_StackInusedIP_Object=MibScalar
stackInusedIP=_StackInusedIP_Object((1,3,6,1,4,1,52,259,10,3,2,1,1),_StackInusedIP_Type())
stackInusedIP.setMaxAccess(_B)
if mibBuilder.loadTexts:stackInusedIP.setStatus(_A)
_StackInusedNetMask_Type=IpAddress
_StackInusedNetMask_Object=MibScalar
stackInusedNetMask=_StackInusedNetMask_Object((1,3,6,1,4,1,52,259,10,3,2,1,2),_StackInusedNetMask_Type())
stackInusedNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:stackInusedNetMask.setStatus(_A)
_StackInusedGateway_Type=IpAddress
_StackInusedGateway_Object=MibScalar
stackInusedGateway=_StackInusedGateway_Object((1,3,6,1,4,1,52,259,10,3,2,1,3),_StackInusedGateway_Type())
stackInusedGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:stackInusedGateway.setStatus(_A)
_StackBootpIP_Type=IpAddress
_StackBootpIP_Object=MibScalar
stackBootpIP=_StackBootpIP_Object((1,3,6,1,4,1,52,259,10,3,2,1,4),_StackBootpIP_Type())
stackBootpIP.setMaxAccess(_B)
if mibBuilder.loadTexts:stackBootpIP.setStatus(_A)
_StackTemporalIP_Type=IpAddress
_StackTemporalIP_Object=MibScalar
stackTemporalIP=_StackTemporalIP_Object((1,3,6,1,4,1,52,259,10,3,2,1,5),_StackTemporalIP_Type())
stackTemporalIP.setMaxAccess(_D)
if mibBuilder.loadTexts:stackTemporalIP.setStatus(_A)
_StackTemporalNetMask_Type=IpAddress
_StackTemporalNetMask_Object=MibScalar
stackTemporalNetMask=_StackTemporalNetMask_Object((1,3,6,1,4,1,52,259,10,3,2,1,6),_StackTemporalNetMask_Type())
stackTemporalNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:stackTemporalNetMask.setStatus(_A)
_StackTemporalGateway_Type=IpAddress
_StackTemporalGateway_Object=MibScalar
stackTemporalGateway=_StackTemporalGateway_Object((1,3,6,1,4,1,52,259,10,3,2,1,7),_StackTemporalGateway_Type())
stackTemporalGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:stackTemporalGateway.setStatus(_A)
class _StackBootpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable-bootp',1),('enable-bootp',2)))
_StackBootpEnable_Type.__name__=_C
_StackBootpEnable_Object=MibScalar
stackBootpEnable=_StackBootpEnable_Object((1,3,6,1,4,1,52,259,10,3,2,1,8),_StackBootpEnable_Type())
stackBootpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:stackBootpEnable.setStatus(_A)
class _IpInformationReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),('reset',2)))
_IpInformationReset_Type.__name__=_C
_IpInformationReset_Object=MibScalar
ipInformationReset=_IpInformationReset_Object((1,3,6,1,4,1,52,259,10,3,2,1,9),_IpInformationReset_Type())
ipInformationReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ipInformationReset.setStatus(_A)
class _StackHealthMonitor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_StackHealthMonitor_Type.__name__=_F
_StackHealthMonitor_Object=MibScalar
stackHealthMonitor=_StackHealthMonitor_Object((1,3,6,1,4,1,52,259,10,3,2,1,10),_StackHealthMonitor_Type())
stackHealthMonitor.setMaxAccess(_B)
if mibBuilder.loadTexts:stackHealthMonitor.setStatus(_A)
_CabletronELH100AgentInfo_ObjectIdentity=ObjectIdentity
cabletronELH100AgentInfo=_CabletronELH100AgentInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,2,2))
_NicAttachSegment_Type=Integer32
_NicAttachSegment_Object=MibScalar
nicAttachSegment=_NicAttachSegment_Object((1,3,6,1,4,1,52,259,10,3,2,2,1),_NicAttachSegment_Type())
nicAttachSegment.setMaxAccess(_D)
if mibBuilder.loadTexts:nicAttachSegment.setStatus(_A)
_SerialNumberTable_Object=MibTable
serialNumberTable=_SerialNumberTable_Object((1,3,6,1,4,1,52,259,10,3,2,2,2))
if mibBuilder.loadTexts:serialNumberTable.setStatus(_A)
_SerialNumberEntry_Object=MibTableRow
serialNumberEntry=_SerialNumberEntry_Object((1,3,6,1,4,1,52,259,10,3,2,2,2,1))
serialNumberEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:serialNumberEntry.setStatus(_A)
class _SNIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_SNIndex_Type.__name__=_C
_SNIndex_Object=MibTableColumn
sNIndex=_SNIndex_Object((1,3,6,1,4,1,52,259,10,3,2,2,2,1,1),_SNIndex_Type())
sNIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sNIndex.setStatus(_A)
class _SerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SerialNumber_Type.__name__=_F
_SerialNumber_Object=MibTableColumn
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,52,259,10,3,2,2,2,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_SNCurrentUnitID_Type=Integer32
_SNCurrentUnitID_Object=MibTableColumn
sNCurrentUnitID=_SNCurrentUnitID_Object((1,3,6,1,4,1,52,259,10,3,2,2,2,1,3),_SNCurrentUnitID_Type())
sNCurrentUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:sNCurrentUnitID.setStatus(_A)
class _TelnetMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_TelnetMaxSessions_Type.__name__=_C
_TelnetMaxSessions_Object=MibScalar
telnetMaxSessions=_TelnetMaxSessions_Object((1,3,6,1,4,1,52,259,10,3,2,2,3),_TelnetMaxSessions_Type())
telnetMaxSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetMaxSessions.setStatus(_A)
class _TelnetAutoLogoutEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_TelnetAutoLogoutEnable_Type.__name__=_C
_TelnetAutoLogoutEnable_Object=MibScalar
telnetAutoLogoutEnable=_TelnetAutoLogoutEnable_Object((1,3,6,1,4,1,52,259,10,3,2,2,4),_TelnetAutoLogoutEnable_Type())
telnetAutoLogoutEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetAutoLogoutEnable.setStatus(_A)
class _TelnetAutoLogoutTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_TelnetAutoLogoutTimeout_Type.__name__=_C
_TelnetAutoLogoutTimeout_Object=MibScalar
telnetAutoLogoutTimeout=_TelnetAutoLogoutTimeout_Object((1,3,6,1,4,1,52,259,10,3,2,2,5),_TelnetAutoLogoutTimeout_Type())
telnetAutoLogoutTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:telnetAutoLogoutTimeout.setStatus(_A)
class _VT100RefreshInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,30,60,120,180,300)));namedValues=NamedValues(*(('seconds5',5),('seconds30',30),('seconds60',60),('seconds120',120),('seconds180',180),('seconds300',300)))
_VT100RefreshInterval_Type.__name__=_C
_VT100RefreshInterval_Object=MibScalar
vT100RefreshInterval=_VT100RefreshInterval_Object((1,3,6,1,4,1,52,259,10,3,2,2,6),_VT100RefreshInterval_Type())
vT100RefreshInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:vT100RefreshInterval.setStatus(_A)
_CabletronELH100gGroupInfo_ObjectIdentity=ObjectIdentity
cabletronELH100gGroupInfo=_CabletronELH100gGroupInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,2,3))
_GroupTable_Object=MibTable
groupTable=_GroupTable_Object((1,3,6,1,4,1,52,259,10,3,2,3,1))
if mibBuilder.loadTexts:groupTable.setStatus(_A)
_GroupEntry_Object=MibTableRow
groupEntry=_GroupEntry_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1))
groupEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:groupEntry.setStatus(_A)
class _GroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_GroupID_Type.__name__=_C
_GroupID_Object=MibTableColumn
groupID=_GroupID_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1,1),_GroupID_Type())
groupID.setMaxAccess(_B)
if mibBuilder.loadTexts:groupID.setStatus(_A)
class _GroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_W,2),('elh100-12tx',3),('elh100-24tx',4)))
_GroupType_Type.__name__=_C
_GroupType_Object=MibTableColumn
groupType=_GroupType_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1,2),_GroupType_Type())
groupType.setMaxAccess(_B)
if mibBuilder.loadTexts:groupType.setStatus(_A)
class _GroupCounterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),('reset',2)))
_GroupCounterReset_Type.__name__=_C
_GroupCounterReset_Object=MibTableColumn
groupCounterReset=_GroupCounterReset_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1,3),_GroupCounterReset_Type())
groupCounterReset.setMaxAccess(_D)
if mibBuilder.loadTexts:groupCounterReset.setStatus(_A)
class _MgmtModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_H,2),(_X,3)))
_MgmtModuleStatus_Type.__name__=_C
_MgmtModuleStatus_Object=MibTableColumn
mgmtModuleStatus=_MgmtModuleStatus_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1,4),_MgmtModuleStatus_Type())
mgmtModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtModuleStatus.setStatus(_A)
class _MgmtModuleDatabaseVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_MgmtModuleDatabaseVersion_Type.__name__=_F
_MgmtModuleDatabaseVersion_Object=MibTableColumn
mgmtModuleDatabaseVersion=_MgmtModuleDatabaseVersion_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1,5),_MgmtModuleDatabaseVersion_Type())
mgmtModuleDatabaseVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtModuleDatabaseVersion.setStatus(_A)
class _SwitchModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_L,1),(_W,2),('internalSwitch10-100',3),('mediaTX-10-100',4),('mediaFX-SC',5),('mediaFX-ST',6),('switchMediaTX-10-100',7),('switchMediaFX-SC',8),('switchMediaFX-ST',9)))
_SwitchModuleType_Type.__name__=_C
_SwitchModuleType_Object=MibTableColumn
switchModuleType=_SwitchModuleType_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1,6),_SwitchModuleType_Type())
switchModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:switchModuleType.setStatus(_A)
class _SwitchModuleActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('notActive',2),(_M,3)))
_SwitchModuleActive_Type.__name__=_C
_SwitchModuleActive_Object=MibTableColumn
switchModuleActive=_SwitchModuleActive_Object((1,3,6,1,4,1,52,259,10,3,2,3,1,1,7),_SwitchModuleActive_Type())
switchModuleActive.setMaxAccess(_B)
if mibBuilder.loadTexts:switchModuleActive.setStatus(_A)
_BackplaneTable_Object=MibTable
backplaneTable=_BackplaneTable_Object((1,3,6,1,4,1,52,259,10,3,2,3,2))
if mibBuilder.loadTexts:backplaneTable.setStatus(_A)
_BackplaneEntry_Object=MibTableRow
backplaneEntry=_BackplaneEntry_Object((1,3,6,1,4,1,52,259,10,3,2,3,2,1))
backplaneEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:backplaneEntry.setStatus(_A)
class _BackplaneGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_BackplaneGroupID_Type.__name__=_C
_BackplaneGroupID_Object=MibTableColumn
backplaneGroupID=_BackplaneGroupID_Object((1,3,6,1,4,1,52,259,10,3,2,3,2,1,1),_BackplaneGroupID_Type())
backplaneGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:backplaneGroupID.setStatus(_A)
class _BackplaneSegmentID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,100)));namedValues=NamedValues(*((_I,10),(_J,100)))
_BackplaneSegmentID_Type.__name__=_C
_BackplaneSegmentID_Object=MibTableColumn
backplaneSegmentID=_BackplaneSegmentID_Object((1,3,6,1,4,1,52,259,10,3,2,3,2,1,2),_BackplaneSegmentID_Type())
backplaneSegmentID.setMaxAccess(_B)
if mibBuilder.loadTexts:backplaneSegmentID.setStatus(_A)
class _BackplaneIsolated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('isolated',1),('attached',2)))
_BackplaneIsolated_Type.__name__=_C
_BackplaneIsolated_Object=MibTableColumn
backplaneIsolated=_BackplaneIsolated_Object((1,3,6,1,4,1,52,259,10,3,2,3,2,1,3),_BackplaneIsolated_Type())
backplaneIsolated.setMaxAccess(_D)
if mibBuilder.loadTexts:backplaneIsolated.setStatus(_A)
_CabletronELH100PortInfo_ObjectIdentity=ObjectIdentity
cabletronELH100PortInfo=_CabletronELH100PortInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,2,4))
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,52,259,10,3,2,4,1))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,52,259,10,3,2,4,1,1))
portEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
class _PortGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_PortGroupID_Type.__name__=_C
_PortGroupID_Object=MibTableColumn
portGroupID=_PortGroupID_Object((1,3,6,1,4,1,52,259,10,3,2,4,1,1,1),_PortGroupID_Type())
portGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:portGroupID.setStatus(_A)
_PortID_Type=Integer32
_PortID_Object=MibTableColumn
portID=_PortID_Object((1,3,6,1,4,1,52,259,10,3,2,4,1,1,2),_PortID_Type())
portID.setMaxAccess(_B)
if mibBuilder.loadTexts:portID.setStatus(_A)
class _PortLinkSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,100)));namedValues=NamedValues(*((_N,1),(_I,10),(_J,100)))
_PortLinkSpeed_Type.__name__=_C
_PortLinkSpeed_Object=MibTableColumn
portLinkSpeed=_PortLinkSpeed_Object((1,3,6,1,4,1,52,259,10,3,2,4,1,1,3),_PortLinkSpeed_Type())
portLinkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:portLinkSpeed.setStatus(_A)
class _PortSpeedConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,100)));namedValues=NamedValues(*(('autoNegotiate',1),(_I,10),(_J,100)))
_PortSpeedConfig_Type.__name__=_C
_PortSpeedConfig_Object=MibTableColumn
portSpeedConfig=_PortSpeedConfig_Object((1,3,6,1,4,1,52,259,10,3,2,4,1,1,4),_PortSpeedConfig_Type())
portSpeedConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:portSpeedConfig.setStatus(_A)
_CabletronELH100PerfMonCapability_ObjectIdentity=ObjectIdentity
cabletronELH100PerfMonCapability=_CabletronELH100PerfMonCapability_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,3))
_CabletronELH100PerfMonAgentInfo_ObjectIdentity=ObjectIdentity
cabletronELH100PerfMonAgentInfo=_CabletronELH100PerfMonAgentInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,3,1))
_PerfMonAgentCRCErrors_Type=Counter32
_PerfMonAgentCRCErrors_Object=MibScalar
perfMonAgentCRCErrors=_PerfMonAgentCRCErrors_Object((1,3,6,1,4,1,52,259,10,3,3,1,1),_PerfMonAgentCRCErrors_Type())
perfMonAgentCRCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfMonAgentCRCErrors.setStatus(_A)
_PerfMonAgentAlignmentErrors_Type=Counter32
_PerfMonAgentAlignmentErrors_Object=MibScalar
perfMonAgentAlignmentErrors=_PerfMonAgentAlignmentErrors_Object((1,3,6,1,4,1,52,259,10,3,3,1,2),_PerfMonAgentAlignmentErrors_Type())
perfMonAgentAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfMonAgentAlignmentErrors.setStatus(_A)
_PerfMonAgentCollisions_Type=Counter32
_PerfMonAgentCollisions_Object=MibScalar
perfMonAgentCollisions=_PerfMonAgentCollisions_Object((1,3,6,1,4,1,52,259,10,3,3,1,3),_PerfMonAgentCollisions_Type())
perfMonAgentCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:perfMonAgentCollisions.setStatus(_A)
_PerfMonAgentTotalPortIsolates_Type=Counter32
_PerfMonAgentTotalPortIsolates_Object=MibScalar
perfMonAgentTotalPortIsolates=_PerfMonAgentTotalPortIsolates_Object((1,3,6,1,4,1,52,259,10,3,3,1,4),_PerfMonAgentTotalPortIsolates_Type())
perfMonAgentTotalPortIsolates.setMaxAccess(_B)
if mibBuilder.loadTexts:perfMonAgentTotalPortIsolates.setStatus(_A)
_PerfMonAgentSymbolErrors_Type=Counter32
_PerfMonAgentSymbolErrors_Object=MibScalar
perfMonAgentSymbolErrors=_PerfMonAgentSymbolErrors_Object((1,3,6,1,4,1,52,259,10,3,3,1,5),_PerfMonAgentSymbolErrors_Type())
perfMonAgentSymbolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfMonAgentSymbolErrors.setStatus(_A)
_CabletronELH100SwitchCapability_ObjectIdentity=ObjectIdentity
cabletronELH100SwitchCapability=_CabletronELH100SwitchCapability_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,4))
_CabletronELH100SwitchInfo_ObjectIdentity=ObjectIdentity
cabletronELH100SwitchInfo=_CabletronELH100SwitchInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,4,1))
_SwitchPortTable_Object=MibTable
switchPortTable=_SwitchPortTable_Object((1,3,6,1,4,1,52,259,10,3,4,1,1))
if mibBuilder.loadTexts:switchPortTable.setStatus(_A)
_SwitchPortEntry_Object=MibTableRow
switchPortEntry=_SwitchPortEntry_Object((1,3,6,1,4,1,52,259,10,3,4,1,1,1))
switchPortEntry.setIndexNames((0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:switchPortEntry.setStatus(_A)
_SwitchPortGroupID_Type=Integer32
_SwitchPortGroupID_Object=MibTableColumn
switchPortGroupID=_SwitchPortGroupID_Object((1,3,6,1,4,1,52,259,10,3,4,1,1,1,1),_SwitchPortGroupID_Type())
switchPortGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortGroupID.setStatus(_A)
class _SwitchPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwitchPortID_Type.__name__=_C
_SwitchPortID_Object=MibTableColumn
switchPortID=_SwitchPortID_Object((1,3,6,1,4,1,52,259,10,3,4,1,1,1,2),_SwitchPortID_Type())
switchPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortID.setStatus(_A)
class _SwitchPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_U,2),(_M,3)))
_SwitchPortAdminStatus_Type.__name__=_C
_SwitchPortAdminStatus_Object=MibTableColumn
switchPortAdminStatus=_SwitchPortAdminStatus_Object((1,3,6,1,4,1,52,259,10,3,4,1,1,1,3),_SwitchPortAdminStatus_Type())
switchPortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:switchPortAdminStatus.setStatus(_A)
class _SwitchPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,100)));namedValues=NamedValues(*((_N,1),(_I,10),(_J,100)))
_SwitchPortSpeed_Type.__name__=_C
_SwitchPortSpeed_Object=MibTableColumn
switchPortSpeed=_SwitchPortSpeed_Object((1,3,6,1,4,1,52,259,10,3,4,1,1,1,4),_SwitchPortSpeed_Type())
switchPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortSpeed.setStatus(_A)
class _SwitchPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('halfDuplex',1),('fullDuplex',2),(_M,3)))
_SwitchPortDuplex_Type.__name__=_C
_SwitchPortDuplex_Object=MibTableColumn
switchPortDuplex=_SwitchPortDuplex_Object((1,3,6,1,4,1,52,259,10,3,4,1,1,1,5),_SwitchPortDuplex_Type())
switchPortDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortDuplex.setStatus(_A)
class _SwitchPortLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link',1),(_N,2)))
_SwitchPortLink_Type.__name__=_C
_SwitchPortLink_Object=MibTableColumn
switchPortLink=_SwitchPortLink_Object((1,3,6,1,4,1,52,259,10,3,4,1,1,1,6),_SwitchPortLink_Type())
switchPortLink.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortLink.setStatus(_A)
_CabletronELH100SwitchStatsInfo_ObjectIdentity=ObjectIdentity
cabletronELH100SwitchStatsInfo=_CabletronELH100SwitchStatsInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,4,2))
_SwitchPortStatsTable_Object=MibTable
switchPortStatsTable=_SwitchPortStatsTable_Object((1,3,6,1,4,1,52,259,10,3,4,2,1))
if mibBuilder.loadTexts:switchPortStatsTable.setStatus(_A)
_SwitchPortStatsEntry_Object=MibTableRow
switchPortStatsEntry=_SwitchPortStatsEntry_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1))
switchPortStatsEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:switchPortStatsEntry.setStatus(_A)
_SwitchPortStatsGroupID_Type=Integer32
_SwitchPortStatsGroupID_Object=MibTableColumn
switchPortStatsGroupID=_SwitchPortStatsGroupID_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,1),_SwitchPortStatsGroupID_Type())
switchPortStatsGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortStatsGroupID.setStatus(_A)
class _SwitchPortStatsID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwitchPortStatsID_Type.__name__=_C
_SwitchPortStatsID_Object=MibTableColumn
switchPortStatsID=_SwitchPortStatsID_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,2),_SwitchPortStatsID_Type())
switchPortStatsID.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortStatsID.setStatus(_A)
_SwitchPortReadableFrames_Type=Counter32
_SwitchPortReadableFrames_Object=MibTableColumn
switchPortReadableFrames=_SwitchPortReadableFrames_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,3),_SwitchPortReadableFrames_Type())
switchPortReadableFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortReadableFrames.setStatus(_A)
_SwitchPortReadableOctets_Type=Counter32
_SwitchPortReadableOctets_Object=MibTableColumn
switchPortReadableOctets=_SwitchPortReadableOctets_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,4),_SwitchPortReadableOctets_Type())
switchPortReadableOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortReadableOctets.setStatus(_A)
_SwitchPortFCSErrors_Type=Counter32
_SwitchPortFCSErrors_Object=MibTableColumn
switchPortFCSErrors=_SwitchPortFCSErrors_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,5),_SwitchPortFCSErrors_Type())
switchPortFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortFCSErrors.setStatus(_A)
_SwitchPortAlignmentErrors_Type=Counter32
_SwitchPortAlignmentErrors_Object=MibTableColumn
switchPortAlignmentErrors=_SwitchPortAlignmentErrors_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,6),_SwitchPortAlignmentErrors_Type())
switchPortAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortAlignmentErrors.setStatus(_A)
_SwitchPortFramesTooLong_Type=Counter32
_SwitchPortFramesTooLong_Object=MibTableColumn
switchPortFramesTooLong=_SwitchPortFramesTooLong_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,7),_SwitchPortFramesTooLong_Type())
switchPortFramesTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortFramesTooLong.setStatus(_A)
_SwitchPortShortEvents_Type=Counter32
_SwitchPortShortEvents_Object=MibTableColumn
switchPortShortEvents=_SwitchPortShortEvents_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,8),_SwitchPortShortEvents_Type())
switchPortShortEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortShortEvents.setStatus(_A)
_SwitchPortRunts_Type=Counter32
_SwitchPortRunts_Object=MibTableColumn
switchPortRunts=_SwitchPortRunts_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,9),_SwitchPortRunts_Type())
switchPortRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortRunts.setStatus(_A)
_SwitchPortCollisions_Type=Counter32
_SwitchPortCollisions_Object=MibTableColumn
switchPortCollisions=_SwitchPortCollisions_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,10),_SwitchPortCollisions_Type())
switchPortCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortCollisions.setStatus(_A)
_SwitchPortLateEvents_Type=Counter32
_SwitchPortLateEvents_Object=MibTableColumn
switchPortLateEvents=_SwitchPortLateEvents_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,11),_SwitchPortLateEvents_Type())
switchPortLateEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortLateEvents.setStatus(_A)
_SwitchPortVeryLongEvents_Type=Counter32
_SwitchPortVeryLongEvents_Object=MibTableColumn
switchPortVeryLongEvents=_SwitchPortVeryLongEvents_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,12),_SwitchPortVeryLongEvents_Type())
switchPortVeryLongEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortVeryLongEvents.setStatus(_A)
_SwitchPortDataRateMismatches_Type=Counter32
_SwitchPortDataRateMismatches_Object=MibTableColumn
switchPortDataRateMismatches=_SwitchPortDataRateMismatches_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,13),_SwitchPortDataRateMismatches_Type())
switchPortDataRateMismatches.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortDataRateMismatches.setStatus(_A)
_SwitchPortAutoPartitions_Type=Counter32
_SwitchPortAutoPartitions_Object=MibTableColumn
switchPortAutoPartitions=_SwitchPortAutoPartitions_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,14),_SwitchPortAutoPartitions_Type())
switchPortAutoPartitions.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortAutoPartitions.setStatus(_A)
_SwitchPortBroadcastPackets_Type=Counter32
_SwitchPortBroadcastPackets_Object=MibTableColumn
switchPortBroadcastPackets=_SwitchPortBroadcastPackets_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,15),_SwitchPortBroadcastPackets_Type())
switchPortBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortBroadcastPackets.setStatus(_A)
_SwitchPortMulticastPackets_Type=Counter32
_SwitchPortMulticastPackets_Object=MibTableColumn
switchPortMulticastPackets=_SwitchPortMulticastPackets_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,16),_SwitchPortMulticastPackets_Type())
switchPortMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortMulticastPackets.setStatus(_A)
_SwitchPortIsolates_Type=Counter32
_SwitchPortIsolates_Object=MibTableColumn
switchPortIsolates=_SwitchPortIsolates_Object((1,3,6,1,4,1,52,259,10,3,4,2,1,1,17),_SwitchPortIsolates_Type())
switchPortIsolates.setMaxAccess(_B)
if mibBuilder.loadTexts:switchPortIsolates.setStatus(_A)
_CabletronELH100BackupCapability_ObjectIdentity=ObjectIdentity
cabletronELH100BackupCapability=_CabletronELH100BackupCapability_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,5))
_CabletronELH100BackupInfo_ObjectIdentity=ObjectIdentity
cabletronELH100BackupInfo=_CabletronELH100BackupInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,5,1))
_BackupPortTable_Object=MibTable
backupPortTable=_BackupPortTable_Object((1,3,6,1,4,1,52,259,10,3,5,1,1))
if mibBuilder.loadTexts:backupPortTable.setStatus(_A)
_BackupPortEntry_Object=MibTableRow
backupPortEntry=_BackupPortEntry_Object((1,3,6,1,4,1,52,259,10,3,5,1,1,1))
backupPortEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:backupPortEntry.setStatus(_A)
class _BackupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,72))
_BackupIndex_Type.__name__=_C
_BackupIndex_Object=MibTableColumn
backupIndex=_BackupIndex_Object((1,3,6,1,4,1,52,259,10,3,5,1,1,1,1),_BackupIndex_Type())
backupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:backupIndex.setStatus(_A)
_BackupPriPortGroup_Type=Integer32
_BackupPriPortGroup_Object=MibTableColumn
backupPriPortGroup=_BackupPriPortGroup_Object((1,3,6,1,4,1,52,259,10,3,5,1,1,1,2),_BackupPriPortGroup_Type())
backupPriPortGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:backupPriPortGroup.setStatus(_A)
_BackupPriPortPort_Type=Integer32
_BackupPriPortPort_Object=MibTableColumn
backupPriPortPort=_BackupPriPortPort_Object((1,3,6,1,4,1,52,259,10,3,5,1,1,1,3),_BackupPriPortPort_Type())
backupPriPortPort.setMaxAccess(_D)
if mibBuilder.loadTexts:backupPriPortPort.setStatus(_A)
_BackupSecPortGroup_Type=Integer32
_BackupSecPortGroup_Object=MibTableColumn
backupSecPortGroup=_BackupSecPortGroup_Object((1,3,6,1,4,1,52,259,10,3,5,1,1,1,4),_BackupSecPortGroup_Type())
backupSecPortGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:backupSecPortGroup.setStatus(_A)
_BackupSecPortPort_Type=Integer32
_BackupSecPortPort_Object=MibTableColumn
backupSecPortPort=_BackupSecPortPort_Object((1,3,6,1,4,1,52,259,10,3,5,1,1,1,5),_BackupSecPortPort_Type())
backupSecPortPort.setMaxAccess(_D)
if mibBuilder.loadTexts:backupSecPortPort.setStatus(_A)
class _BackupPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_H,2),(_X,3),('backup',4),(_G,5),('delete',6)))
_BackupPortAction_Type.__name__=_C
_BackupPortAction_Object=MibTableColumn
backupPortAction=_BackupPortAction_Object((1,3,6,1,4,1,52,259,10,3,5,1,1,1,6),_BackupPortAction_Type())
backupPortAction.setMaxAccess(_D)
if mibBuilder.loadTexts:backupPortAction.setStatus(_A)
_CabletronELH100SecurityCapability_ObjectIdentity=ObjectIdentity
cabletronELH100SecurityCapability=_CabletronELH100SecurityCapability_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,6))
_CabletronELH100SecurityInfo_ObjectIdentity=ObjectIdentity
cabletronELH100SecurityInfo=_CabletronELH100SecurityInfo_ObjectIdentity((1,3,6,1,4,1,52,259,10,3,6,1))
_SecurityTable_Object=MibTable
securityTable=_SecurityTable_Object((1,3,6,1,4,1,52,259,10,3,6,1,1))
if mibBuilder.loadTexts:securityTable.setStatus(_A)
_SecurityEntry_Object=MibTableRow
securityEntry=_SecurityEntry_Object((1,3,6,1,4,1,52,259,10,3,6,1,1,1))
securityEntry.setIndexNames((0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:securityEntry.setStatus(_A)
_SecurityGroupID_Type=Integer32
_SecurityGroupID_Object=MibTableColumn
securityGroupID=_SecurityGroupID_Object((1,3,6,1,4,1,52,259,10,3,6,1,1,1,1),_SecurityGroupID_Type())
securityGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:securityGroupID.setStatus(_A)
_SecurityPortID_Type=Integer32
_SecurityPortID_Object=MibTableColumn
securityPortID=_SecurityPortID_Object((1,3,6,1,4,1,52,259,10,3,6,1,1,1,2),_SecurityPortID_Type())
securityPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:securityPortID.setStatus(_A)
_SecurityAddr_Type=PhysAddress
_SecurityAddr_Object=MibTableColumn
securityAddr=_SecurityAddr_Object((1,3,6,1,4,1,52,259,10,3,6,1,1,1,3),_SecurityAddr_Type())
securityAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:securityAddr.setStatus(_A)
class _SecurityAutoLearnAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_H,2),('learned',3)))
_SecurityAutoLearnAction_Type.__name__=_C
_SecurityAutoLearnAction_Object=MibTableColumn
securityAutoLearnAction=_SecurityAutoLearnAction_Object((1,3,6,1,4,1,52,259,10,3,6,1,1,1,4),_SecurityAutoLearnAction_Type())
securityAutoLearnAction.setMaxAccess(_D)
if mibBuilder.loadTexts:securityAutoLearnAction.setStatus(_A)
class _SecurityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('warningAndDisable',2)))
_SecurityEnable_Type.__name__=_C
_SecurityEnable_Object=MibTableColumn
securityEnable=_SecurityEnable_Object((1,3,6,1,4,1,52,259,10,3,6,1,1,1,5),_SecurityEnable_Type())
securityEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:securityEnable.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cabletron':cabletron,'cabletronOEM':cabletronOEM,'cabletronRepeaters':cabletronRepeaters,'cabletronELH100':cabletronELH100,'cabletronELH100Common':cabletronELH100Common,'elh100System':elh100System,'elh100MajorVer':elh100MajorVer,'elh100MinorVer':elh100MinorVer,'elh100HardwareVer':elh100HardwareVer,'elh100CommunityMgt':elh100CommunityMgt,'elh100CommunityTable':elh100CommunityTable,'elh100CommunityEntry':elh100CommunityEntry,_P:elh100CommunityIndex,'elh100CommunityRowCreation':elh100CommunityRowCreation,'elh100CommunityString':elh100CommunityString,'elh100CommunityStatus':elh100CommunityStatus,'elh100TrapManagerMgt':elh100TrapManagerMgt,'elh100TrapManagerTable':elh100TrapManagerTable,'elh100TrapMgtEntry':elh100TrapMgtEntry,_Q:elh100TrapMgtIndex,'elh100TrapMgtRowCreation':elh100TrapMgtRowCreation,'elh100TrapMgtCommunityString':elh100TrapMgtCommunityString,'elh100TrapMgtIpAddress':elh100TrapMgtIpAddress,'elh100DownloadMgt':elh100DownloadMgt,'elh100DownloadServerIP':elh100DownloadServerIP,'elh100DownloadFilename':elh100DownloadFilename,'elh100DownloadMode':elh100DownloadMode,'elh100DownloadAction':elh100DownloadAction,'elh100Restart':elh100Restart,'cabletronELH100BasicCapability':cabletronELH100BasicCapability,'cabletronELH100StackInfo':cabletronELH100StackInfo,'stackInusedIP':stackInusedIP,'stackInusedNetMask':stackInusedNetMask,'stackInusedGateway':stackInusedGateway,'stackBootpIP':stackBootpIP,'stackTemporalIP':stackTemporalIP,'stackTemporalNetMask':stackTemporalNetMask,'stackTemporalGateway':stackTemporalGateway,'stackBootpEnable':stackBootpEnable,'ipInformationReset':ipInformationReset,'stackHealthMonitor':stackHealthMonitor,'cabletronELH100AgentInfo':cabletronELH100AgentInfo,'nicAttachSegment':nicAttachSegment,'serialNumberTable':serialNumberTable,'serialNumberEntry':serialNumberEntry,_S:sNIndex,'serialNumber':serialNumber,'sNCurrentUnitID':sNCurrentUnitID,'telnetMaxSessions':telnetMaxSessions,'telnetAutoLogoutEnable':telnetAutoLogoutEnable,'telnetAutoLogoutTimeout':telnetAutoLogoutTimeout,'vT100RefreshInterval':vT100RefreshInterval,'cabletronELH100gGroupInfo':cabletronELH100gGroupInfo,'groupTable':groupTable,'groupEntry':groupEntry,_V:groupID,'groupType':groupType,'groupCounterReset':groupCounterReset,'mgmtModuleStatus':mgmtModuleStatus,'mgmtModuleDatabaseVersion':mgmtModuleDatabaseVersion,'switchModuleType':switchModuleType,'switchModuleActive':switchModuleActive,'backplaneTable':backplaneTable,'backplaneEntry':backplaneEntry,_Y:backplaneGroupID,_Z:backplaneSegmentID,'backplaneIsolated':backplaneIsolated,'cabletronELH100PortInfo':cabletronELH100PortInfo,'portTable':portTable,'portEntry':portEntry,_a:portGroupID,_b:portID,'portLinkSpeed':portLinkSpeed,'portSpeedConfig':portSpeedConfig,'cabletronELH100PerfMonCapability':cabletronELH100PerfMonCapability,'cabletronELH100PerfMonAgentInfo':cabletronELH100PerfMonAgentInfo,'perfMonAgentCRCErrors':perfMonAgentCRCErrors,'perfMonAgentAlignmentErrors':perfMonAgentAlignmentErrors,'perfMonAgentCollisions':perfMonAgentCollisions,'perfMonAgentTotalPortIsolates':perfMonAgentTotalPortIsolates,'perfMonAgentSymbolErrors':perfMonAgentSymbolErrors,'cabletronELH100SwitchCapability':cabletronELH100SwitchCapability,'cabletronELH100SwitchInfo':cabletronELH100SwitchInfo,'switchPortTable':switchPortTable,'switchPortEntry':switchPortEntry,_c:switchPortGroupID,_d:switchPortID,'switchPortAdminStatus':switchPortAdminStatus,'switchPortSpeed':switchPortSpeed,'switchPortDuplex':switchPortDuplex,'switchPortLink':switchPortLink,'cabletronELH100SwitchStatsInfo':cabletronELH100SwitchStatsInfo,'switchPortStatsTable':switchPortStatsTable,'switchPortStatsEntry':switchPortStatsEntry,_e:switchPortStatsGroupID,_f:switchPortStatsID,'switchPortReadableFrames':switchPortReadableFrames,'switchPortReadableOctets':switchPortReadableOctets,'switchPortFCSErrors':switchPortFCSErrors,'switchPortAlignmentErrors':switchPortAlignmentErrors,'switchPortFramesTooLong':switchPortFramesTooLong,'switchPortShortEvents':switchPortShortEvents,'switchPortRunts':switchPortRunts,'switchPortCollisions':switchPortCollisions,'switchPortLateEvents':switchPortLateEvents,'switchPortVeryLongEvents':switchPortVeryLongEvents,'switchPortDataRateMismatches':switchPortDataRateMismatches,'switchPortAutoPartitions':switchPortAutoPartitions,'switchPortBroadcastPackets':switchPortBroadcastPackets,'switchPortMulticastPackets':switchPortMulticastPackets,'switchPortIsolates':switchPortIsolates,'cabletronELH100BackupCapability':cabletronELH100BackupCapability,'cabletronELH100BackupInfo':cabletronELH100BackupInfo,'backupPortTable':backupPortTable,'backupPortEntry':backupPortEntry,_g:backupIndex,'backupPriPortGroup':backupPriPortGroup,'backupPriPortPort':backupPriPortPort,'backupSecPortGroup':backupSecPortGroup,'backupSecPortPort':backupSecPortPort,'backupPortAction':backupPortAction,'cabletronELH100SecurityCapability':cabletronELH100SecurityCapability,'cabletronELH100SecurityInfo':cabletronELH100SecurityInfo,'securityTable':securityTable,'securityEntry':securityEntry,_h:securityGroupID,_i:securityPortID,'securityAddr':securityAddr,'securityAutoLearnAction':securityAutoLearnAction,'securityEnable':securityEnable})