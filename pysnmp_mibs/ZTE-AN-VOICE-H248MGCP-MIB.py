_j='zxAnMgcpProtocolMgId'
_i='disable'
_h='enable'
_g='zxAnMgcpMgId'
_f='zxAnMgcpMgcId'
_e='zxAnSlcTermIDBeginIndex'
_d='zxAnSlcTermIDSlotNo'
_c='zxAnSlcTermIDShelfNo'
_b='zxAnSlcTermIDRackNo'
_a='zxAnH248ProtocolMgId'
_Z='zxAnMgId'
_Y='useDomainName'
_X='zxAnMgcId'
_W='metaswitch'
_V='ericsson'
_U='nortelH248'
_T='zxAnMgcType'
_S='md5infoID'
_R='InetAddressType'
_Q='faxVbd'
_P='siemens'
_O='nortelMgcp'
_N='alcatel'
_M='cisco'
_L='faxT38'
_K='zte'
_J='second'
_I='read-only'
_H='not-accessible'
_G='ZTE-AN-VOICE-H248MGCP-MIB'
_F='DisplayString'
_E='TruthValue'
_D='read-write'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
zxAnVoiceH248MgcpMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnVoiceMgmt_ObjectIdentity=ObjectIdentity
zxAnVoiceMgmt=_ZxAnVoiceMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_ZxAnH248MgcpConfig_ObjectIdentity=ObjectIdentity
zxAnH248MgcpConfig=_ZxAnH248MgcpConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1))
_Md5InfoTable_Object=MibTable
md5InfoTable=_Md5InfoTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12))
if mibBuilder.loadTexts:md5InfoTable.setStatus(_A)
_Md5InfoEntry_Object=MibTableRow
md5InfoEntry=_Md5InfoEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1))
md5InfoEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:md5InfoEntry.setStatus(_A)
class _Md5infoID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_Md5infoID_Type.__name__=_B
_Md5infoID_Object=MibTableColumn
md5infoID=_Md5infoID_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1,1),_Md5infoID_Type())
md5infoID.setMaxAccess(_H)
if mibBuilder.loadTexts:md5infoID.setStatus(_A)
class _Md5infoG_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Md5infoG_Type.__name__=_B
_Md5infoG_Object=MibTableColumn
md5infoG=_Md5infoG_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1,2),_Md5infoG_Type())
md5infoG.setMaxAccess(_C)
if mibBuilder.loadTexts:md5infoG.setStatus(_A)
class _Md5infoKi_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Md5infoKi_Type.__name__=_F
_Md5infoKi_Object=MibTableColumn
md5infoKi=_Md5infoKi_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1,3),_Md5infoKi_Type())
md5infoKi.setMaxAccess(_C)
if mibBuilder.loadTexts:md5infoKi.setStatus(_A)
class _Md5infoMginfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Md5infoMginfo_Type.__name__=_F
_Md5infoMginfo_Object=MibTableColumn
md5infoMginfo=_Md5infoMginfo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1,4),_Md5infoMginfo_Type())
md5infoMginfo.setMaxAccess(_C)
if mibBuilder.loadTexts:md5infoMginfo.setStatus(_A)
class _Md5infoPLenth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Md5infoPLenth_Type.__name__=_B
_Md5infoPLenth_Object=MibTableColumn
md5infoPLenth=_Md5infoPLenth_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1,5),_Md5infoPLenth_Type())
md5infoPLenth.setMaxAccess(_C)
if mibBuilder.loadTexts:md5infoPLenth.setStatus(_A)
class _Md5infoP_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_Md5infoP_Type.__name__=_F
_Md5infoP_Object=MibTableColumn
md5infoP=_Md5infoP_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1,6),_Md5infoP_Type())
md5infoP.setMaxAccess(_C)
if mibBuilder.loadTexts:md5infoP.setStatus(_A)
_Md5infoRowStatus_Type=RowStatus
_Md5infoRowStatus_Object=MibTableColumn
md5infoRowStatus=_Md5infoRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,12,1,7),_Md5infoRowStatus_Type())
md5infoRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:md5infoRowStatus.setStatus(_A)
_ZxAnH248MgcpGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnH248MgcpGlobalObjects=_ZxAnH248MgcpGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,1100))
class _ZxAnH248MgcpMgmtCapabilities_Type(Bits):namedValues=NamedValues(('nbPlatform',0))
_ZxAnH248MgcpMgmtCapabilities_Type.__name__='Bits'
_ZxAnH248MgcpMgmtCapabilities_Object=MibScalar
zxAnH248MgcpMgmtCapabilities=_ZxAnH248MgcpMgmtCapabilities_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1100,1),_ZxAnH248MgcpMgmtCapabilities_Type())
zxAnH248MgcpMgmtCapabilities.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248MgcpMgmtCapabilities.setStatus(_A)
class _ZxAnH248MgcpLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('broken',2)))
_ZxAnH248MgcpLinkStatus_Type.__name__=_B
_ZxAnH248MgcpLinkStatus_Object=MibScalar
zxAnH248MgcpLinkStatus=_ZxAnH248MgcpLinkStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1100,2),_ZxAnH248MgcpLinkStatus_Type())
zxAnH248MgcpLinkStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248MgcpLinkStatus.setStatus(_A)
_ZxAnMgcTypeTable_Object=MibTable
zxAnMgcTypeTable=_ZxAnMgcTypeTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101))
if mibBuilder.loadTexts:zxAnMgcTypeTable.setStatus(_A)
_ZxAnMgcTypeEntry_Object=MibTableRow
zxAnMgcTypeEntry=_ZxAnMgcTypeEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1))
zxAnMgcTypeEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:zxAnMgcTypeEntry.setStatus(_A)
class _ZxAnMgcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_K,1),('hw',2),(_M,3),(_N,4),(_O,5),(_U,6),(_P,7),(_V,8),(_W,9)))
_ZxAnMgcType_Type.__name__=_B
_ZxAnMgcType_Object=MibTableColumn
zxAnMgcType=_ZxAnMgcType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,1),_ZxAnMgcType_Type())
zxAnMgcType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMgcType.setStatus(_A)
class _ZxAnMgcRegPktWithAddress_Type(TruthValue):defaultValue=1
_ZxAnMgcRegPktWithAddress_Type.__name__=_E
_ZxAnMgcRegPktWithAddress_Object=MibTableColumn
zxAnMgcRegPktWithAddress=_ZxAnMgcRegPktWithAddress_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,4),_ZxAnMgcRegPktWithAddress_Type())
zxAnMgcRegPktWithAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktWithAddress.setStatus(_A)
class _ZxAnMgcRegPktWithVersion_Type(TruthValue):defaultValue=1
_ZxAnMgcRegPktWithVersion_Type.__name__=_E
_ZxAnMgcRegPktWithVersion_Object=MibTableColumn
zxAnMgcRegPktWithVersion=_ZxAnMgcRegPktWithVersion_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,5),_ZxAnMgcRegPktWithVersion_Type())
zxAnMgcRegPktWithVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktWithVersion.setStatus(_A)
class _ZxAnMgcRegPktWithDelay_Type(TruthValue):defaultValue=2
_ZxAnMgcRegPktWithDelay_Type.__name__=_E
_ZxAnMgcRegPktWithDelay_Object=MibTableColumn
zxAnMgcRegPktWithDelay=_ZxAnMgcRegPktWithDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,6),_ZxAnMgcRegPktWithDelay_Type())
zxAnMgcRegPktWithDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktWithDelay.setStatus(_A)
class _ZxAnMgcRegPktWithProfile_Type(TruthValue):defaultValue=1
_ZxAnMgcRegPktWithProfile_Type.__name__=_E
_ZxAnMgcRegPktWithProfile_Object=MibTableColumn
zxAnMgcRegPktWithProfile=_ZxAnMgcRegPktWithProfile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,7),_ZxAnMgcRegPktWithProfile_Type())
zxAnMgcRegPktWithProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktWithProfile.setStatus(_A)
class _ZxAnMgcRegPktWithTimeStamp_Type(TruthValue):defaultValue=2
_ZxAnMgcRegPktWithTimeStamp_Type.__name__=_E
_ZxAnMgcRegPktWithTimeStamp_Object=MibTableColumn
zxAnMgcRegPktWithTimeStamp=_ZxAnMgcRegPktWithTimeStamp_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,8),_ZxAnMgcRegPktWithTimeStamp_Type())
zxAnMgcRegPktWithTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktWithTimeStamp.setStatus(_A)
class _ZxAnMgcRegPktWithReason_Type(TruthValue):defaultValue=1
_ZxAnMgcRegPktWithReason_Type.__name__=_E
_ZxAnMgcRegPktWithReason_Object=MibTableColumn
zxAnMgcRegPktWithReason=_ZxAnMgcRegPktWithReason_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,9),_ZxAnMgcRegPktWithReason_Type())
zxAnMgcRegPktWithReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktWithReason.setStatus(_A)
class _ZxAnMgcRegPktBraceDblQuotation_Type(TruthValue):defaultValue=2
_ZxAnMgcRegPktBraceDblQuotation_Type.__name__=_E
_ZxAnMgcRegPktBraceDblQuotation_Object=MibTableColumn
zxAnMgcRegPktBraceDblQuotation=_ZxAnMgcRegPktBraceDblQuotation_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,10),_ZxAnMgcRegPktBraceDblQuotation_Type())
zxAnMgcRegPktBraceDblQuotation.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktBraceDblQuotation.setStatus(_A)
class _ZxAnMgcRegPktMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('failover',1),('restart',2),('graceful',3),('forced',4),('disconnected',5),('handoff',6)))
_ZxAnMgcRegPktMethod_Type.__name__=_B
_ZxAnMgcRegPktMethod_Object=MibTableColumn
zxAnMgcRegPktMethod=_ZxAnMgcRegPktMethod_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,11),_ZxAnMgcRegPktMethod_Type())
zxAnMgcRegPktMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktMethod.setStatus(_A)
class _ZxAnMgcRegPktVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnMgcRegPktVersion_Type.__name__=_B
_ZxAnMgcRegPktVersion_Object=MibTableColumn
zxAnMgcRegPktVersion=_ZxAnMgcRegPktVersion_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,12),_ZxAnMgcRegPktVersion_Type())
zxAnMgcRegPktVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktVersion.setStatus(_A)
class _ZxAnMgcRegPktDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnMgcRegPktDelay_Type.__name__=_B
_ZxAnMgcRegPktDelay_Object=MibTableColumn
zxAnMgcRegPktDelay=_ZxAnMgcRegPktDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,13),_ZxAnMgcRegPktDelay_Type())
zxAnMgcRegPktDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktDelay.setStatus(_A)
class _ZxAnMgcRegPktProfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ZxAnMgcRegPktProfile_Type.__name__=_F
_ZxAnMgcRegPktProfile_Object=MibTableColumn
zxAnMgcRegPktProfile=_ZxAnMgcRegPktProfile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,14),_ZxAnMgcRegPktProfile_Type())
zxAnMgcRegPktProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktProfile.setStatus(_A)
class _ZxAnMgcRegPktReason_Type(Integer32):defaultValue=901;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(900,903))
_ZxAnMgcRegPktReason_Type.__name__=_B
_ZxAnMgcRegPktReason_Object=MibTableColumn
zxAnMgcRegPktReason=_ZxAnMgcRegPktReason_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1101,1,15),_ZxAnMgcRegPktReason_Type())
zxAnMgcRegPktReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcRegPktReason.setStatus(_A)
_ZxAnMgcCfgTable_Object=MibTable
zxAnMgcCfgTable=_ZxAnMgcCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102))
if mibBuilder.loadTexts:zxAnMgcCfgTable.setStatus(_A)
_ZxAnMgcCfgEntry_Object=MibTableRow
zxAnMgcCfgEntry=_ZxAnMgcCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1))
zxAnMgcCfgEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:zxAnMgcCfgEntry.setStatus(_A)
class _ZxAnMgcId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_ZxAnMgcId_Type.__name__=_B
_ZxAnMgcId_Object=MibTableColumn
zxAnMgcId=_ZxAnMgcId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,1),_ZxAnMgcId_Type())
zxAnMgcId.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMgcId.setStatus(_A)
class _ZxAnMgcTypeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_K,1),('hw',2),(_M,3),(_N,4),(_O,5),(_U,6),(_P,7),(_V,8),(_W,9)))
_ZxAnMgcTypeId_Type.__name__=_B
_ZxAnMgcTypeId_Object=MibTableColumn
zxAnMgcTypeId=_ZxAnMgcTypeId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,2),_ZxAnMgcTypeId_Type())
zxAnMgcTypeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcTypeId.setStatus(_A)
class _ZxAnMgcCfgPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnMgcCfgPort_Type.__name__=_B
_ZxAnMgcCfgPort_Object=MibTableColumn
zxAnMgcCfgPort=_ZxAnMgcCfgPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,3),_ZxAnMgcCfgPort_Type())
zxAnMgcCfgPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcCfgPort.setStatus(_A)
class _ZxAnMgcNamingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('useIp',1),(_Y,2)))
_ZxAnMgcNamingType_Type.__name__=_B
_ZxAnMgcNamingType_Object=MibTableColumn
zxAnMgcNamingType=_ZxAnMgcNamingType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,4),_ZxAnMgcNamingType_Type())
zxAnMgcNamingType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcNamingType.setStatus(_A)
_ZxAnMgcIpAddress_Type=IpAddress
_ZxAnMgcIpAddress_Object=MibTableColumn
zxAnMgcIpAddress=_ZxAnMgcIpAddress_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,5),_ZxAnMgcIpAddress_Type())
zxAnMgcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcIpAddress.setStatus(_A)
class _ZxAnMgcDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnMgcDomainName_Type.__name__=_F
_ZxAnMgcDomainName_Object=MibTableColumn
zxAnMgcDomainName=_ZxAnMgcDomainName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,6),_ZxAnMgcDomainName_Type())
zxAnMgcDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcDomainName.setStatus(_A)
class _ZxAnMgcMd5Id_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_ZxAnMgcMd5Id_Type.__name__=_B
_ZxAnMgcMd5Id_Object=MibTableColumn
zxAnMgcMd5Id=_ZxAnMgcMd5Id_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,7),_ZxAnMgcMd5Id_Type())
zxAnMgcMd5Id.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcMd5Id.setStatus(_A)
class _ZxAnMgcDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnMgcDescription_Type.__name__=_F
_ZxAnMgcDescription_Object=MibTableColumn
zxAnMgcDescription=_ZxAnMgcDescription_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,8),_ZxAnMgcDescription_Type())
zxAnMgcDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcDescription.setStatus(_A)
_ZxAnMgcRowStatus_Type=RowStatus
_ZxAnMgcRowStatus_Object=MibTableColumn
zxAnMgcRowStatus=_ZxAnMgcRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1102,1,30),_ZxAnMgcRowStatus_Type())
zxAnMgcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcRowStatus.setStatus(_A)
_ZxAnMgCfgTable_Object=MibTable
zxAnMgCfgTable=_ZxAnMgCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110))
if mibBuilder.loadTexts:zxAnMgCfgTable.setStatus(_A)
_ZxAnMgCfgEntry_Object=MibTableRow
zxAnMgCfgEntry=_ZxAnMgCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1))
zxAnMgCfgEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:zxAnMgCfgEntry.setStatus(_A)
class _ZxAnMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnMgId_Type.__name__=_B
_ZxAnMgId_Object=MibTableColumn
zxAnMgId=_ZxAnMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,1),_ZxAnMgId_Type())
zxAnMgId.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMgId.setStatus(_A)
class _ZxAnMgProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('h248',1),('mgcp',2)))
_ZxAnMgProtocolType_Type.__name__=_B
_ZxAnMgProtocolType_Object=MibTableColumn
zxAnMgProtocolType=_ZxAnMgProtocolType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,2),_ZxAnMgProtocolType_Type())
zxAnMgProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgProtocolType.setStatus('deprecated')
class _ZxAnMgCfgPort_Type(Integer32):defaultValue=2944;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnMgCfgPort_Type.__name__=_B
_ZxAnMgCfgPort_Object=MibTableColumn
zxAnMgCfgPort=_ZxAnMgCfgPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,3),_ZxAnMgCfgPort_Type())
zxAnMgCfgPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgCfgPort.setStatus(_A)
class _ZxAnMgCfgDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnMgCfgDomainName_Type.__name__=_F
_ZxAnMgCfgDomainName_Object=MibTableColumn
zxAnMgCfgDomainName=_ZxAnMgCfgDomainName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,4),_ZxAnMgCfgDomainName_Type())
zxAnMgCfgDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgCfgDomainName.setStatus(_A)
class _ZxAnMgDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnMgDescription_Type.__name__=_F
_ZxAnMgDescription_Object=MibTableColumn
zxAnMgDescription=_ZxAnMgDescription_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,5),_ZxAnMgDescription_Type())
zxAnMgDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgDescription.setStatus(_A)
class _ZxAnMgNamingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('useIp',1),(_Y,2)))
_ZxAnMgNamingType_Type.__name__=_B
_ZxAnMgNamingType_Object=MibTableColumn
zxAnMgNamingType=_ZxAnMgNamingType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,6),_ZxAnMgNamingType_Type())
zxAnMgNamingType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgNamingType.setStatus(_A)
class _ZxAnMgcId1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnMgcId1_Type.__name__=_B
_ZxAnMgcId1_Object=MibTableColumn
zxAnMgcId1=_ZxAnMgcId1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,7),_ZxAnMgcId1_Type())
zxAnMgcId1.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcId1.setStatus(_A)
class _ZxAnMgcId2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnMgcId2_Type.__name__=_B
_ZxAnMgcId2_Object=MibTableColumn
zxAnMgcId2=_ZxAnMgcId2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,8),_ZxAnMgcId2_Type())
zxAnMgcId2.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcId2.setStatus(_A)
class _ZxAnMgcId3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnMgcId3_Type.__name__=_B
_ZxAnMgcId3_Object=MibTableColumn
zxAnMgcId3=_ZxAnMgcId3_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,9),_ZxAnMgcId3_Type())
zxAnMgcId3.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcId3.setStatus(_A)
class _ZxAnMgcId4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnMgcId4_Type.__name__=_B
_ZxAnMgcId4_Object=MibTableColumn
zxAnMgcId4=_ZxAnMgcId4_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,10),_ZxAnMgcId4_Type())
zxAnMgcId4.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcId4.setStatus(_A)
class _ZxAnCurrentMgcId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnCurrentMgcId_Type.__name__=_B
_ZxAnCurrentMgcId_Object=MibTableColumn
zxAnCurrentMgcId=_ZxAnCurrentMgcId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,11),_ZxAnCurrentMgcId_Type())
zxAnCurrentMgcId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnCurrentMgcId.setStatus(_A)
class _ZxAnMgTranslay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('atm',2)))
_ZxAnMgTranslay_Type.__name__=_B
_ZxAnMgTranslay_Object=MibTableColumn
zxAnMgTranslay=_ZxAnMgTranslay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,12),_ZxAnMgTranslay_Type())
zxAnMgTranslay.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgTranslay.setStatus(_A)
class _ZxAnMgTransProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('tcp',2)))
_ZxAnMgTransProtocol_Type.__name__=_B
_ZxAnMgTransProtocol_Object=MibTableColumn
zxAnMgTransProtocol=_ZxAnMgTransProtocol_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,13),_ZxAnMgTransProtocol_Type())
zxAnMgTransProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgTransProtocol.setStatus(_A)
class _ZxAnTransactionNum_Type(Integer32):defaultValue=6000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,7000))
_ZxAnTransactionNum_Type.__name__=_B
_ZxAnTransactionNum_Object=MibTableColumn
zxAnTransactionNum=_ZxAnTransactionNum_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,14),_ZxAnTransactionNum_Type())
zxAnTransactionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnTransactionNum.setStatus(_A)
class _ZxAnRtpFaxPri1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_L,2)))
_ZxAnRtpFaxPri1_Type.__name__=_B
_ZxAnRtpFaxPri1_Object=MibTableColumn
zxAnRtpFaxPri1=_ZxAnRtpFaxPri1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,15),_ZxAnRtpFaxPri1_Type())
zxAnRtpFaxPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnRtpFaxPri1.setStatus(_A)
class _ZxAnRtpFaxPri2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('faxVBD',1),(_L,2)))
_ZxAnRtpFaxPri2_Type.__name__=_B
_ZxAnRtpFaxPri2_Object=MibTableColumn
zxAnRtpFaxPri2=_ZxAnRtpFaxPri2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,16),_ZxAnRtpFaxPri2_Type())
zxAnRtpFaxPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnRtpFaxPri2.setStatus(_A)
class _ZxAnSelfExchange_Type(TruthValue):defaultValue=2
_ZxAnSelfExchange_Type.__name__=_E
_ZxAnSelfExchange_Object=MibTableColumn
zxAnSelfExchange=_ZxAnSelfExchange_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,17),_ZxAnSelfExchange_Type())
zxAnSelfExchange.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSelfExchange.setStatus(_A)
class _ZxAnProtectCall_Type(TruthValue):defaultValue=2
_ZxAnProtectCall_Type.__name__=_E
_ZxAnProtectCall_Object=MibTableColumn
zxAnProtectCall=_ZxAnProtectCall_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,18),_ZxAnProtectCall_Type())
zxAnProtectCall.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnProtectCall.setStatus(_A)
class _ZxAnRtp2833PayloadTypeCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('negotiatedBySdp',1),('specifiedByLocalRtpParameter',2)))
_ZxAnRtp2833PayloadTypeCode_Type.__name__=_B
_ZxAnRtp2833PayloadTypeCode_Object=MibTableColumn
zxAnRtp2833PayloadTypeCode=_ZxAnRtp2833PayloadTypeCode_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,19),_ZxAnRtp2833PayloadTypeCode_Type())
zxAnRtp2833PayloadTypeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnRtp2833PayloadTypeCode.setStatus(_A)
class _ZxAnPacketMaxTransactionNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnPacketMaxTransactionNumber_Type.__name__=_B
_ZxAnPacketMaxTransactionNumber_Object=MibTableColumn
zxAnPacketMaxTransactionNumber=_ZxAnPacketMaxTransactionNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,20),_ZxAnPacketMaxTransactionNumber_Type())
zxAnPacketMaxTransactionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPacketMaxTransactionNumber.setStatus(_A)
class _ZxAnHotlineWithSpace_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('withoutSpace',1),('withSpace',2),('withT',3)))
_ZxAnHotlineWithSpace_Type.__name__=_B
_ZxAnHotlineWithSpace_Object=MibTableColumn
zxAnHotlineWithSpace=_ZxAnHotlineWithSpace_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,21),_ZxAnHotlineWithSpace_Type())
zxAnHotlineWithSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnHotlineWithSpace.setStatus(_A)
class _ZxAnAlwaysReportOffhookEvent_Type(TruthValue):defaultValue=1
_ZxAnAlwaysReportOffhookEvent_Type.__name__=_E
_ZxAnAlwaysReportOffhookEvent_Object=MibTableColumn
zxAnAlwaysReportOffhookEvent=_ZxAnAlwaysReportOffhookEvent_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,22),_ZxAnAlwaysReportOffhookEvent_Type())
zxAnAlwaysReportOffhookEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAlwaysReportOffhookEvent.setStatus(_A)
class _ZxAnAlwaysReportOnhookEvent_Type(TruthValue):defaultValue=1
_ZxAnAlwaysReportOnhookEvent_Type.__name__=_E
_ZxAnAlwaysReportOnhookEvent_Object=MibTableColumn
zxAnAlwaysReportOnhookEvent=_ZxAnAlwaysReportOnhookEvent_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,23),_ZxAnAlwaysReportOnhookEvent_Type())
zxAnAlwaysReportOnhookEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnAlwaysReportOnhookEvent.setStatus(_A)
class _ZxAnSubSuspendRtp_Type(TruthValue):defaultValue=1
_ZxAnSubSuspendRtp_Type.__name__=_E
_ZxAnSubSuspendRtp_Object=MibTableColumn
zxAnSubSuspendRtp=_ZxAnSubSuspendRtp_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,24),_ZxAnSubSuspendRtp_Type())
zxAnSubSuspendRtp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSubSuspendRtp.setStatus(_A)
class _ZxAnDisasterProt_Type(TruthValue):defaultValue=1
_ZxAnDisasterProt_Type.__name__=_E
_ZxAnDisasterProt_Object=MibTableColumn
zxAnDisasterProt=_ZxAnDisasterProt_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,25),_ZxAnDisasterProt_Type())
zxAnDisasterProt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDisasterProt.setStatus(_A)
_ZxAnMgCfgRowStatus_Type=RowStatus
_ZxAnMgCfgRowStatus_Object=MibTableColumn
zxAnMgCfgRowStatus=_ZxAnMgCfgRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1110,1,100),_ZxAnMgCfgRowStatus_Type())
zxAnMgCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgCfgRowStatus.setStatus(_A)
_ZxAnH248ProtocolTable_Object=MibTable
zxAnH248ProtocolTable=_ZxAnH248ProtocolTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111))
if mibBuilder.loadTexts:zxAnH248ProtocolTable.setStatus(_A)
_ZxAnH248ProtocolEntry_Object=MibTableRow
zxAnH248ProtocolEntry=_ZxAnH248ProtocolEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1))
zxAnH248ProtocolEntry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:zxAnH248ProtocolEntry.setStatus(_A)
class _ZxAnH248ProtocolMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnH248ProtocolMgId_Type.__name__=_B
_ZxAnH248ProtocolMgId_Object=MibTableColumn
zxAnH248ProtocolMgId=_ZxAnH248ProtocolMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,1),_ZxAnH248ProtocolMgId_Type())
zxAnH248ProtocolMgId.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnH248ProtocolMgId.setStatus(_A)
class _ZxAnH248ProtocolVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2',2),('v3',3)))
_ZxAnH248ProtocolVersion_Type.__name__=_B
_ZxAnH248ProtocolVersion_Object=MibTableColumn
zxAnH248ProtocolVersion=_ZxAnH248ProtocolVersion_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,2),_ZxAnH248ProtocolVersion_Type())
zxAnH248ProtocolVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248ProtocolVersion.setStatus(_A)
class _ZxAnH248EncodingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('text',1),('binary',2)))
_ZxAnH248EncodingType_Type.__name__=_B
_ZxAnH248EncodingType_Object=MibTableColumn
zxAnH248EncodingType=_ZxAnH248EncodingType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,3),_ZxAnH248EncodingType_Type())
zxAnH248EncodingType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248EncodingType.setStatus(_A)
class _ZxAnH248PacketTokenAbbreviated_Type(TruthValue):defaultValue=1
_ZxAnH248PacketTokenAbbreviated_Type.__name__=_E
_ZxAnH248PacketTokenAbbreviated_Object=MibTableColumn
zxAnH248PacketTokenAbbreviated=_ZxAnH248PacketTokenAbbreviated_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,4),_ZxAnH248PacketTokenAbbreviated_Type())
zxAnH248PacketTokenAbbreviated.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248PacketTokenAbbreviated.setStatus(_A)
class _ZxAnH248MinTransactionId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6000))
_ZxAnH248MinTransactionId_Type.__name__=_B
_ZxAnH248MinTransactionId_Object=MibTableColumn
zxAnH248MinTransactionId=_ZxAnH248MinTransactionId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,5),_ZxAnH248MinTransactionId_Type())
zxAnH248MinTransactionId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248MinTransactionId.setStatus(_A)
class _ZxAnH248MaxTransactionId_Type(Integer32):defaultValue=8000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,429496729))
_ZxAnH248MaxTransactionId_Type.__name__=_B
_ZxAnH248MaxTransactionId_Object=MibTableColumn
zxAnH248MaxTransactionId=_ZxAnH248MaxTransactionId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,6),_ZxAnH248MaxTransactionId_Type())
zxAnH248MaxTransactionId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248MaxTransactionId.setStatus(_A)
class _ZxAnH248SendResponseAck_Type(TruthValue):defaultValue=1
_ZxAnH248SendResponseAck_Type.__name__=_E
_ZxAnH248SendResponseAck_Object=MibTableColumn
zxAnH248SendResponseAck=_ZxAnH248SendResponseAck_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,7),_ZxAnH248SendResponseAck_Type())
zxAnH248SendResponseAck.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248SendResponseAck.setStatus(_A)
class _ZxAnH248ResponseCacheTime_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_ZxAnH248ResponseCacheTime_Type.__name__=_B
_ZxAnH248ResponseCacheTime_Object=MibTableColumn
zxAnH248ResponseCacheTime=_ZxAnH248ResponseCacheTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,8),_ZxAnH248ResponseCacheTime_Type())
zxAnH248ResponseCacheTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248ResponseCacheTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnH248ResponseCacheTime.setUnits(_J)
class _ZxAnH248SendTransactionPending_Type(TruthValue):defaultValue=1
_ZxAnH248SendTransactionPending_Type.__name__=_E
_ZxAnH248SendTransactionPending_Object=MibTableColumn
zxAnH248SendTransactionPending=_ZxAnH248SendTransactionPending_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,9),_ZxAnH248SendTransactionPending_Type())
zxAnH248SendTransactionPending.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248SendTransactionPending.setStatus(_A)
class _ZxAnH248ProfileNegotiation_Type(TruthValue):defaultValue=2
_ZxAnH248ProfileNegotiation_Type.__name__=_E
_ZxAnH248ProfileNegotiation_Object=MibTableColumn
zxAnH248ProfileNegotiation=_ZxAnH248ProfileNegotiation_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,10),_ZxAnH248ProfileNegotiation_Type())
zxAnH248ProfileNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248ProfileNegotiation.setStatus(_A)
class _ZxAnH248RebootMaxWaitingDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_ZxAnH248RebootMaxWaitingDelay_Type.__name__=_B
_ZxAnH248RebootMaxWaitingDelay_Object=MibTableColumn
zxAnH248RebootMaxWaitingDelay=_ZxAnH248RebootMaxWaitingDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,11),_ZxAnH248RebootMaxWaitingDelay_Type())
zxAnH248RebootMaxWaitingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248RebootMaxWaitingDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnH248RebootMaxWaitingDelay.setUnits(_J)
class _ZxAnH248MgcMaxInactivityTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,300))
_ZxAnH248MgcMaxInactivityTime_Type.__name__=_B
_ZxAnH248MgcMaxInactivityTime_Object=MibTableColumn
zxAnH248MgcMaxInactivityTime=_ZxAnH248MgcMaxInactivityTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,12),_ZxAnH248MgcMaxInactivityTime_Type())
zxAnH248MgcMaxInactivityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248MgcMaxInactivityTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnH248MgcMaxInactivityTime.setUnits(_J)
class _ZxAnH248TranRetranMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixedInteval',1),('exponentialGrowthInteval',2)))
_ZxAnH248TranRetranMode_Type.__name__=_B
_ZxAnH248TranRetranMode_Object=MibTableColumn
zxAnH248TranRetranMode=_ZxAnH248TranRetranMode_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,13),_ZxAnH248TranRetranMode_Type())
zxAnH248TranRetranMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248TranRetranMode.setStatus(_A)
class _ZxAnH248TranRetranInterval_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ZxAnH248TranRetranInterval_Type.__name__=_B
_ZxAnH248TranRetranInterval_Object=MibTableColumn
zxAnH248TranRetranInterval=_ZxAnH248TranRetranInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,14),_ZxAnH248TranRetranInterval_Type())
zxAnH248TranRetranInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248TranRetranInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnH248TranRetranInterval.setUnits(_J)
class _ZxAnH248TranMaxRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ZxAnH248TranMaxRetries_Type.__name__=_B
_ZxAnH248TranMaxRetries_Object=MibTableColumn
zxAnH248TranMaxRetries=_ZxAnH248TranMaxRetries_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,15),_ZxAnH248TranMaxRetries_Type())
zxAnH248TranMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248TranMaxRetries.setStatus(_A)
class _ZxAnH248TranPendInterval_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8))
_ZxAnH248TranPendInterval_Type.__name__=_B
_ZxAnH248TranPendInterval_Object=MibTableColumn
zxAnH248TranPendInterval=_ZxAnH248TranPendInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,16),_ZxAnH248TranPendInterval_Type())
zxAnH248TranPendInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248TranPendInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnH248TranPendInterval.setUnits(_J)
class _ZxAnH248TranPendLimit_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,40))
_ZxAnH248TranPendLimit_Type.__name__=_B
_ZxAnH248TranPendLimit_Object=MibTableColumn
zxAnH248TranPendLimit=_ZxAnH248TranPendLimit_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,17),_ZxAnH248TranPendLimit_Type())
zxAnH248TranPendLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248TranPendLimit.setStatus(_A)
class _ZxAnH248HeartbeatMechanism_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlByMgc',1),('controlByMg',2)))
_ZxAnH248HeartbeatMechanism_Type.__name__=_B
_ZxAnH248HeartbeatMechanism_Object=MibTableColumn
zxAnH248HeartbeatMechanism=_ZxAnH248HeartbeatMechanism_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,18),_ZxAnH248HeartbeatMechanism_Type())
zxAnH248HeartbeatMechanism.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248HeartbeatMechanism.setStatus(_A)
class _ZxAnH248MgcHbMaxInactivityTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_ZxAnH248MgcHbMaxInactivityTime_Type.__name__=_B
_ZxAnH248MgcHbMaxInactivityTime_Object=MibTableColumn
zxAnH248MgcHbMaxInactivityTime=_ZxAnH248MgcHbMaxInactivityTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,19),_ZxAnH248MgcHbMaxInactivityTime_Type())
zxAnH248MgcHbMaxInactivityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248MgcHbMaxInactivityTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnH248MgcHbMaxInactivityTime.setUnits(_J)
class _ZxAnH248HeartbeatFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sv',1),('itito',2)))
_ZxAnH248HeartbeatFormat_Type.__name__=_B
_ZxAnH248HeartbeatFormat_Object=MibTableColumn
zxAnH248HeartbeatFormat=_ZxAnH248HeartbeatFormat_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,20),_ZxAnH248HeartbeatFormat_Type())
zxAnH248HeartbeatFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248HeartbeatFormat.setStatus(_A)
class _ZxAnH248HbRetranInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ZxAnH248HbRetranInterval_Type.__name__=_B
_ZxAnH248HbRetranInterval_Object=MibTableColumn
zxAnH248HbRetranInterval=_ZxAnH248HbRetranInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,21),_ZxAnH248HbRetranInterval_Type())
zxAnH248HbRetranInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248HbRetranInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnH248HbRetranInterval.setUnits(_J)
class _ZxAnH248HbMaxRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ZxAnH248HbMaxRetries_Type.__name__=_B
_ZxAnH248HbMaxRetries_Object=MibTableColumn
zxAnH248HbMaxRetries=_ZxAnH248HbMaxRetries_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1111,1,22),_ZxAnH248HbMaxRetries_Type())
zxAnH248HbMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnH248HbMaxRetries.setStatus(_A)
_ZxAnSlcTermIDTable_Object=MibTable
zxAnSlcTermIDTable=_ZxAnSlcTermIDTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120))
if mibBuilder.loadTexts:zxAnSlcTermIDTable.setStatus(_A)
_ZxAnSlcTermIDEntry_Object=MibTableRow
zxAnSlcTermIDEntry=_ZxAnSlcTermIDEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1))
zxAnSlcTermIDEntry.setIndexNames((0,_G,_b),(0,_G,_c),(0,_G,_d),(0,_G,_e))
if mibBuilder.loadTexts:zxAnSlcTermIDEntry.setStatus(_A)
_ZxAnSlcTermIDRackNo_Type=Integer32
_ZxAnSlcTermIDRackNo_Object=MibTableColumn
zxAnSlcTermIDRackNo=_ZxAnSlcTermIDRackNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,1),_ZxAnSlcTermIDRackNo_Type())
zxAnSlcTermIDRackNo.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnSlcTermIDRackNo.setStatus(_A)
_ZxAnSlcTermIDShelfNo_Type=Integer32
_ZxAnSlcTermIDShelfNo_Object=MibTableColumn
zxAnSlcTermIDShelfNo=_ZxAnSlcTermIDShelfNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,2),_ZxAnSlcTermIDShelfNo_Type())
zxAnSlcTermIDShelfNo.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnSlcTermIDShelfNo.setStatus(_A)
_ZxAnSlcTermIDSlotNo_Type=Integer32
_ZxAnSlcTermIDSlotNo_Object=MibTableColumn
zxAnSlcTermIDSlotNo=_ZxAnSlcTermIDSlotNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,3),_ZxAnSlcTermIDSlotNo_Type())
zxAnSlcTermIDSlotNo.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnSlcTermIDSlotNo.setStatus(_A)
class _ZxAnSlcTermIDBeginIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ZxAnSlcTermIDBeginIndex_Type.__name__=_B
_ZxAnSlcTermIDBeginIndex_Object=MibTableColumn
zxAnSlcTermIDBeginIndex=_ZxAnSlcTermIDBeginIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,4),_ZxAnSlcTermIDBeginIndex_Type())
zxAnSlcTermIDBeginIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnSlcTermIDBeginIndex.setStatus(_A)
class _ZxAnSlcTermIDOperSum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,192))
_ZxAnSlcTermIDOperSum_Type.__name__=_B
_ZxAnSlcTermIDOperSum_Object=MibTableColumn
zxAnSlcTermIDOperSum=_ZxAnSlcTermIDOperSum_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,5),_ZxAnSlcTermIDOperSum_Type())
zxAnSlcTermIDOperSum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcTermIDOperSum.setStatus(_A)
class _ZxAnSlcTermIDTMID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnSlcTermIDTMID_Type.__name__=_F
_ZxAnSlcTermIDTMID_Object=MibTableColumn
zxAnSlcTermIDTMID=_ZxAnSlcTermIDTMID_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,6),_ZxAnSlcTermIDTMID_Type())
zxAnSlcTermIDTMID.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcTermIDTMID.setStatus(_A)
class _ZxAnSlcTermIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3)))
_ZxAnSlcTermIDType_Type.__name__=_B
_ZxAnSlcTermIDType_Object=MibTableColumn
zxAnSlcTermIDType=_ZxAnSlcTermIDType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,7),_ZxAnSlcTermIDType_Type())
zxAnSlcTermIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcTermIDType.setStatus(_A)
_ZxAnSlcTermIDBeginNo_Type=Integer32
_ZxAnSlcTermIDBeginNo_Object=MibTableColumn
zxAnSlcTermIDBeginNo=_ZxAnSlcTermIDBeginNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,8),_ZxAnSlcTermIDBeginNo_Type())
zxAnSlcTermIDBeginNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcTermIDBeginNo.setStatus(_A)
class _ZxAnSlcTermIDDigitLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnSlcTermIDDigitLen_Type.__name__=_B
_ZxAnSlcTermIDDigitLen_Object=MibTableColumn
zxAnSlcTermIDDigitLen=_ZxAnSlcTermIDDigitLen_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,9),_ZxAnSlcTermIDDigitLen_Type())
zxAnSlcTermIDDigitLen.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcTermIDDigitLen.setStatus(_A)
class _ZxAnSlcTermIDMgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnSlcTermIDMgId_Type.__name__=_B
_ZxAnSlcTermIDMgId_Object=MibTableColumn
zxAnSlcTermIDMgId=_ZxAnSlcTermIDMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,11),_ZxAnSlcTermIDMgId_Type())
zxAnSlcTermIDMgId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcTermIDMgId.setStatus(_A)
class _ZxAnSlcTerminationID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnSlcTerminationID_Type.__name__=_F
_ZxAnSlcTerminationID_Object=MibTableColumn
zxAnSlcTerminationID=_ZxAnSlcTerminationID_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,12),_ZxAnSlcTerminationID_Type())
zxAnSlcTerminationID.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnSlcTerminationID.setStatus(_A)
_ZxAnSlcTermIDRowStatus_Type=RowStatus
_ZxAnSlcTermIDRowStatus_Object=MibTableColumn
zxAnSlcTermIDRowStatus=_ZxAnSlcTermIDRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1120,1,13),_ZxAnSlcTermIDRowStatus_Type())
zxAnSlcTermIDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSlcTermIDRowStatus.setStatus(_A)
_ZxAnMgcpConfig_ObjectIdentity=ObjectIdentity
zxAnMgcpConfig=_ZxAnMgcpConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,1150))
_ZxAnMgcpMgcCfgTable_Object=MibTable
zxAnMgcpMgcCfgTable=_ZxAnMgcpMgcCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1))
if mibBuilder.loadTexts:zxAnMgcpMgcCfgTable.setStatus(_A)
_ZxAnMgcpMgcCfgEntry_Object=MibTableRow
zxAnMgcpMgcCfgEntry=_ZxAnMgcpMgcCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1))
zxAnMgcpMgcCfgEntry.setIndexNames((0,_G,_f))
if mibBuilder.loadTexts:zxAnMgcpMgcCfgEntry.setStatus(_A)
class _ZxAnMgcpMgcId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ZxAnMgcpMgcId_Type.__name__=_B
_ZxAnMgcpMgcId_Object=MibTableColumn
zxAnMgcpMgcId=_ZxAnMgcpMgcId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,1),_ZxAnMgcpMgcId_Type())
zxAnMgcpMgcId.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMgcpMgcId.setStatus(_A)
class _ZxAnMgcpMgcTypeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*((_K,1),('hw',2),(_M,3),(_N,4),(_O,5),(_P,7)))
_ZxAnMgcpMgcTypeId_Type.__name__=_B
_ZxAnMgcpMgcTypeId_Object=MibTableColumn
zxAnMgcpMgcTypeId=_ZxAnMgcpMgcTypeId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,2),_ZxAnMgcpMgcTypeId_Type())
zxAnMgcpMgcTypeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcTypeId.setStatus(_A)
class _ZxAnMgcpMgcPort_Type(Integer32):defaultValue=2727;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnMgcpMgcPort_Type.__name__=_B
_ZxAnMgcpMgcPort_Object=MibTableColumn
zxAnMgcpMgcPort=_ZxAnMgcpMgcPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,3),_ZxAnMgcpMgcPort_Type())
zxAnMgcpMgcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcPort.setStatus(_A)
class _ZxAnMgcpMgcIpAddrType_Type(InetAddressType):defaultValue=1
_ZxAnMgcpMgcIpAddrType_Type.__name__=_R
_ZxAnMgcpMgcIpAddrType_Object=MibTableColumn
zxAnMgcpMgcIpAddrType=_ZxAnMgcpMgcIpAddrType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,4),_ZxAnMgcpMgcIpAddrType_Type())
zxAnMgcpMgcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcIpAddrType.setStatus(_A)
_ZxAnMgcpMgcIpAddress_Type=InetAddress
_ZxAnMgcpMgcIpAddress_Object=MibTableColumn
zxAnMgcpMgcIpAddress=_ZxAnMgcpMgcIpAddress_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,5),_ZxAnMgcpMgcIpAddress_Type())
zxAnMgcpMgcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcIpAddress.setStatus(_A)
class _ZxAnMgcpMgcDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ZxAnMgcpMgcDomainName_Type.__name__=_F
_ZxAnMgcpMgcDomainName_Object=MibTableColumn
zxAnMgcpMgcDomainName=_ZxAnMgcpMgcDomainName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,6),_ZxAnMgcpMgcDomainName_Type())
zxAnMgcpMgcDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcDomainName.setStatus(_A)
class _ZxAnMgcpMgcDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnMgcpMgcDescription_Type.__name__=_F
_ZxAnMgcpMgcDescription_Object=MibTableColumn
zxAnMgcpMgcDescription=_ZxAnMgcpMgcDescription_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,7),_ZxAnMgcpMgcDescription_Type())
zxAnMgcpMgcDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcDescription.setStatus(_A)
_ZxAnMgcpMgcRowStatus_Type=RowStatus
_ZxAnMgcpMgcRowStatus_Object=MibTableColumn
zxAnMgcpMgcRowStatus=_ZxAnMgcpMgcRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,1,1,100),_ZxAnMgcpMgcRowStatus_Type())
zxAnMgcpMgcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcRowStatus.setStatus(_A)
_ZxAnMgcpMgCfgTable_Object=MibTable
zxAnMgcpMgCfgTable=_ZxAnMgcpMgCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2))
if mibBuilder.loadTexts:zxAnMgcpMgCfgTable.setStatus(_A)
_ZxAnMgcpMgCfgEntry_Object=MibTableRow
zxAnMgcpMgCfgEntry=_ZxAnMgcpMgCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1))
zxAnMgcpMgCfgEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:zxAnMgcpMgCfgEntry.setStatus(_A)
class _ZxAnMgcpMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnMgcpMgId_Type.__name__=_B
_ZxAnMgcpMgId_Object=MibTableColumn
zxAnMgcpMgId=_ZxAnMgcpMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,1),_ZxAnMgcpMgId_Type())
zxAnMgcpMgId.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMgcpMgId.setStatus(_A)
class _ZxAnMgcpMgPort_Type(Integer32):defaultValue=2427;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnMgcpMgPort_Type.__name__=_B
_ZxAnMgcpMgPort_Object=MibTableColumn
zxAnMgcpMgPort=_ZxAnMgcpMgPort_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,2),_ZxAnMgcpMgPort_Type())
zxAnMgcpMgPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgPort.setStatus(_A)
class _ZxAnMgcpMgDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ZxAnMgcpMgDomainName_Type.__name__=_F
_ZxAnMgcpMgDomainName_Object=MibTableColumn
zxAnMgcpMgDomainName=_ZxAnMgcpMgDomainName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,3),_ZxAnMgcpMgDomainName_Type())
zxAnMgcpMgDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgDomainName.setStatus(_A)
class _ZxAnMgcpMgDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnMgcpMgDescription_Type.__name__=_F
_ZxAnMgcpMgDescription_Object=MibTableColumn
zxAnMgcpMgDescription=_ZxAnMgcpMgDescription_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,4),_ZxAnMgcpMgDescription_Type())
zxAnMgcpMgDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgDescription.setStatus(_A)
class _ZxAnMgcpMgcId1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnMgcpMgcId1_Type.__name__=_B
_ZxAnMgcpMgcId1_Object=MibTableColumn
zxAnMgcpMgcId1=_ZxAnMgcpMgcId1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,5),_ZxAnMgcpMgcId1_Type())
zxAnMgcpMgcId1.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcId1.setStatus(_A)
class _ZxAnMgcpMgcId2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnMgcpMgcId2_Type.__name__=_B
_ZxAnMgcpMgcId2_Object=MibTableColumn
zxAnMgcpMgcId2=_ZxAnMgcpMgcId2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,6),_ZxAnMgcpMgcId2_Type())
zxAnMgcpMgcId2.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcId2.setStatus(_A)
class _ZxAnMgcpMgcId3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnMgcpMgcId3_Type.__name__=_B
_ZxAnMgcpMgcId3_Object=MibTableColumn
zxAnMgcpMgcId3=_ZxAnMgcpMgcId3_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,7),_ZxAnMgcpMgcId3_Type())
zxAnMgcpMgcId3.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcId3.setStatus(_A)
class _ZxAnMgcpMgcId4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnMgcpMgcId4_Type.__name__=_B
_ZxAnMgcpMgcId4_Object=MibTableColumn
zxAnMgcpMgcId4=_ZxAnMgcpMgcId4_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,8),_ZxAnMgcpMgcId4_Type())
zxAnMgcpMgcId4.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgcId4.setStatus(_A)
class _ZxAnMgcpRtpFaxPri1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_L,2)))
_ZxAnMgcpRtpFaxPri1_Type.__name__=_B
_ZxAnMgcpRtpFaxPri1_Object=MibTableColumn
zxAnMgcpRtpFaxPri1=_ZxAnMgcpRtpFaxPri1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,9),_ZxAnMgcpRtpFaxPri1_Type())
zxAnMgcpRtpFaxPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpRtpFaxPri1.setStatus(_A)
class _ZxAnMgcpRtpFaxPri2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_L,2)))
_ZxAnMgcpRtpFaxPri2_Type.__name__=_B
_ZxAnMgcpRtpFaxPri2_Object=MibTableColumn
zxAnMgcpRtpFaxPri2=_ZxAnMgcpRtpFaxPri2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,10),_ZxAnMgcpRtpFaxPri2_Type())
zxAnMgcpRtpFaxPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpRtpFaxPri2.setStatus(_A)
class _ZxAnMgcpMgSelfSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_ZxAnMgcpMgSelfSwitch_Type.__name__=_B
_ZxAnMgcpMgSelfSwitch_Object=MibTableColumn
zxAnMgcpMgSelfSwitch=_ZxAnMgcpMgSelfSwitch_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,11),_ZxAnMgcpMgSelfSwitch_Type())
zxAnMgcpMgSelfSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgSelfSwitch.setStatus(_A)
class _ZxAnMgcpMgProtectCall_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_ZxAnMgcpMgProtectCall_Type.__name__=_B
_ZxAnMgcpMgProtectCall_Object=MibTableColumn
zxAnMgcpMgProtectCall=_ZxAnMgcpMgProtectCall_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,12),_ZxAnMgcpMgProtectCall_Type())
zxAnMgcpMgProtectCall.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgProtectCall.setStatus(_A)
class _ZxAnMgcpMgRtp2833Type_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type2833Redun',1),('typeRtp',2)))
_ZxAnMgcpMgRtp2833Type_Type.__name__=_B
_ZxAnMgcpMgRtp2833Type_Object=MibTableColumn
zxAnMgcpMgRtp2833Type=_ZxAnMgcpMgRtp2833Type_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,13),_ZxAnMgcpMgRtp2833Type_Type())
zxAnMgcpMgRtp2833Type.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgRtp2833Type.setStatus(_A)
_ZxAnMgcpMgRowStatus_Type=RowStatus
_ZxAnMgcpMgRowStatus_Object=MibTableColumn
zxAnMgcpMgRowStatus=_ZxAnMgcpMgRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,2,1,100),_ZxAnMgcpMgRowStatus_Type())
zxAnMgcpMgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnMgcpMgRowStatus.setStatus(_A)
_ZxAnMgcpProtocolTable_Object=MibTable
zxAnMgcpProtocolTable=_ZxAnMgcpProtocolTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3))
if mibBuilder.loadTexts:zxAnMgcpProtocolTable.setStatus(_A)
_ZxAnMgcpProtocolEntry_Object=MibTableRow
zxAnMgcpProtocolEntry=_ZxAnMgcpProtocolEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1))
zxAnMgcpProtocolEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:zxAnMgcpProtocolEntry.setStatus(_A)
class _ZxAnMgcpProtocolMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnMgcpProtocolMgId_Type.__name__=_B
_ZxAnMgcpProtocolMgId_Object=MibTableColumn
zxAnMgcpProtocolMgId=_ZxAnMgcpProtocolMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,1),_ZxAnMgcpProtocolMgId_Type())
zxAnMgcpProtocolMgId.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnMgcpProtocolMgId.setStatus(_A)
class _ZxAnMgcpProtocolVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2',2)))
_ZxAnMgcpProtocolVersion_Type.__name__=_B
_ZxAnMgcpProtocolVersion_Object=MibTableColumn
zxAnMgcpProtocolVersion=_ZxAnMgcpProtocolVersion_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,2),_ZxAnMgcpProtocolVersion_Type())
zxAnMgcpProtocolVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpProtocolVersion.setStatus(_A)
class _ZxAnMgcpMgcMaxInactivityTime_Type(Integer32):defaultValue=126;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,300))
_ZxAnMgcpMgcMaxInactivityTime_Type.__name__=_B
_ZxAnMgcpMgcMaxInactivityTime_Object=MibTableColumn
zxAnMgcpMgcMaxInactivityTime=_ZxAnMgcpMgcMaxInactivityTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,3),_ZxAnMgcpMgcMaxInactivityTime_Type())
zxAnMgcpMgcMaxInactivityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpMgcMaxInactivityTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnMgcpMgcMaxInactivityTime.setUnits(_J)
class _ZxAnMgcpMinTransactionId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_ZxAnMgcpMinTransactionId_Type.__name__=_B
_ZxAnMgcpMinTransactionId_Object=MibTableColumn
zxAnMgcpMinTransactionId=_ZxAnMgcpMinTransactionId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,4),_ZxAnMgcpMinTransactionId_Type())
zxAnMgcpMinTransactionId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpMinTransactionId.setStatus(_A)
class _ZxAnMgcpMaxTransactionId_Type(Integer32):defaultValue=80000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ZxAnMgcpMaxTransactionId_Type.__name__=_B
_ZxAnMgcpMaxTransactionId_Object=MibTableColumn
zxAnMgcpMaxTransactionId=_ZxAnMgcpMaxTransactionId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,5),_ZxAnMgcpMaxTransactionId_Type())
zxAnMgcpMaxTransactionId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpMaxTransactionId.setStatus(_A)
class _ZxAnMgcpResponseCacheTime_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_ZxAnMgcpResponseCacheTime_Type.__name__=_B
_ZxAnMgcpResponseCacheTime_Object=MibTableColumn
zxAnMgcpResponseCacheTime=_ZxAnMgcpResponseCacheTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,6),_ZxAnMgcpResponseCacheTime_Type())
zxAnMgcpResponseCacheTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpResponseCacheTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnMgcpResponseCacheTime.setUnits(_J)
class _ZxAnMgcpTranMaxRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ZxAnMgcpTranMaxRetries_Type.__name__=_B
_ZxAnMgcpTranMaxRetries_Object=MibTableColumn
zxAnMgcpTranMaxRetries=_ZxAnMgcpTranMaxRetries_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,7),_ZxAnMgcpTranMaxRetries_Type())
zxAnMgcpTranMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpTranMaxRetries.setStatus(_A)
class _ZxAnMgcpTranPendInterval_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,8))
_ZxAnMgcpTranPendInterval_Type.__name__=_B
_ZxAnMgcpTranPendInterval_Object=MibTableColumn
zxAnMgcpTranPendInterval=_ZxAnMgcpTranPendInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,8),_ZxAnMgcpTranPendInterval_Type())
zxAnMgcpTranPendInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpTranPendInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnMgcpTranPendInterval.setUnits(_J)
class _ZxAnMgcpTranPendLimit_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,40))
_ZxAnMgcpTranPendLimit_Type.__name__=_B
_ZxAnMgcpTranPendLimit_Object=MibTableColumn
zxAnMgcpTranPendLimit=_ZxAnMgcpTranPendLimit_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,9),_ZxAnMgcpTranPendLimit_Type())
zxAnMgcpTranPendLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpTranPendLimit.setStatus(_A)
class _ZxAnMgcpRebootMaxWaitingDelay_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_ZxAnMgcpRebootMaxWaitingDelay_Type.__name__=_B
_ZxAnMgcpRebootMaxWaitingDelay_Object=MibTableColumn
zxAnMgcpRebootMaxWaitingDelay=_ZxAnMgcpRebootMaxWaitingDelay_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1150,3,1,10),_ZxAnMgcpRebootMaxWaitingDelay_Type())
zxAnMgcpRebootMaxWaitingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnMgcpRebootMaxWaitingDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnMgcpRebootMaxWaitingDelay.setUnits(_J)
_ZxAnH248Perf_ObjectIdentity=ObjectIdentity
zxAnH248Perf=_ZxAnH248Perf_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,1170))
_ZxAnH248PSRecMsg_Type=Integer32
_ZxAnH248PSRecMsg_Object=MibScalar
zxAnH248PSRecMsg=_ZxAnH248PSRecMsg_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,1),_ZxAnH248PSRecMsg_Type())
zxAnH248PSRecMsg.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSRecMsg.setStatus(_A)
_ZxAnH248PSSendMsg_Type=Integer32
_ZxAnH248PSSendMsg_Object=MibScalar
zxAnH248PSSendMsg=_ZxAnH248PSSendMsg_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,2),_ZxAnH248PSSendMsg_Type())
zxAnH248PSSendMsg.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSSendMsg.setStatus(_A)
_ZxAnH248PSRecMsgByte_Type=Integer32
_ZxAnH248PSRecMsgByte_Object=MibScalar
zxAnH248PSRecMsgByte=_ZxAnH248PSRecMsgByte_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,3),_ZxAnH248PSRecMsgByte_Type())
zxAnH248PSRecMsgByte.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSRecMsgByte.setStatus(_A)
_ZxAnH248PSSendMsgByte_Type=Integer32
_ZxAnH248PSSendMsgByte_Object=MibScalar
zxAnH248PSSendMsgByte=_ZxAnH248PSSendMsgByte_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,4),_ZxAnH248PSSendMsgByte_Type())
zxAnH248PSSendMsgByte.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSSendMsgByte.setStatus(_A)
_ZxAnH248PSProtocolError_Type=Integer32
_ZxAnH248PSProtocolError_Object=MibScalar
zxAnH248PSProtocolError=_ZxAnH248PSProtocolError_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,5),_ZxAnH248PSProtocolError_Type())
zxAnH248PSProtocolError.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSProtocolError.setStatus(_A)
_ZxAnH248PSTimerOut_Type=Integer32
_ZxAnH248PSTimerOut_Object=MibScalar
zxAnH248PSTimerOut=_ZxAnH248PSTimerOut_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,6),_ZxAnH248PSTimerOut_Type())
zxAnH248PSTimerOut.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSTimerOut.setStatus(_A)
_ZxAnH248PSDisconnect_Type=Integer32
_ZxAnH248PSDisconnect_Object=MibScalar
zxAnH248PSDisconnect=_ZxAnH248PSDisconnect_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,7),_ZxAnH248PSDisconnect_Type())
zxAnH248PSDisconnect.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSDisconnect.setStatus(_A)
_ZxAnH248PSMGCChange_Type=Integer32
_ZxAnH248PSMGCChange_Object=MibScalar
zxAnH248PSMGCChange=_ZxAnH248PSMGCChange_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,8),_ZxAnH248PSMGCChange_Type())
zxAnH248PSMGCChange.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSMGCChange.setStatus(_A)
_ZxAnH248PSTransmitError_Type=Integer32
_ZxAnH248PSTransmitError_Object=MibScalar
zxAnH248PSTransmitError=_ZxAnH248PSTransmitError_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1170,9),_ZxAnH248PSTransmitError_Type())
zxAnH248PSTransmitError.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnH248PSTransmitError.setStatus(_A)
mibBuilder.exportSymbols(_G,**{_K:zte,'zxAn':zxAn,'zxAnVoiceH248MgcpMib':zxAnVoiceH248MgcpMib,'zxAnVoiceMgmt':zxAnVoiceMgmt,'zxAnH248MgcpConfig':zxAnH248MgcpConfig,'md5InfoTable':md5InfoTable,'md5InfoEntry':md5InfoEntry,_S:md5infoID,'md5infoG':md5infoG,'md5infoKi':md5infoKi,'md5infoMginfo':md5infoMginfo,'md5infoPLenth':md5infoPLenth,'md5infoP':md5infoP,'md5infoRowStatus':md5infoRowStatus,'zxAnH248MgcpGlobalObjects':zxAnH248MgcpGlobalObjects,'zxAnH248MgcpMgmtCapabilities':zxAnH248MgcpMgmtCapabilities,'zxAnH248MgcpLinkStatus':zxAnH248MgcpLinkStatus,'zxAnMgcTypeTable':zxAnMgcTypeTable,'zxAnMgcTypeEntry':zxAnMgcTypeEntry,_T:zxAnMgcType,'zxAnMgcRegPktWithAddress':zxAnMgcRegPktWithAddress,'zxAnMgcRegPktWithVersion':zxAnMgcRegPktWithVersion,'zxAnMgcRegPktWithDelay':zxAnMgcRegPktWithDelay,'zxAnMgcRegPktWithProfile':zxAnMgcRegPktWithProfile,'zxAnMgcRegPktWithTimeStamp':zxAnMgcRegPktWithTimeStamp,'zxAnMgcRegPktWithReason':zxAnMgcRegPktWithReason,'zxAnMgcRegPktBraceDblQuotation':zxAnMgcRegPktBraceDblQuotation,'zxAnMgcRegPktMethod':zxAnMgcRegPktMethod,'zxAnMgcRegPktVersion':zxAnMgcRegPktVersion,'zxAnMgcRegPktDelay':zxAnMgcRegPktDelay,'zxAnMgcRegPktProfile':zxAnMgcRegPktProfile,'zxAnMgcRegPktReason':zxAnMgcRegPktReason,'zxAnMgcCfgTable':zxAnMgcCfgTable,'zxAnMgcCfgEntry':zxAnMgcCfgEntry,_X:zxAnMgcId,'zxAnMgcTypeId':zxAnMgcTypeId,'zxAnMgcCfgPort':zxAnMgcCfgPort,'zxAnMgcNamingType':zxAnMgcNamingType,'zxAnMgcIpAddress':zxAnMgcIpAddress,'zxAnMgcDomainName':zxAnMgcDomainName,'zxAnMgcMd5Id':zxAnMgcMd5Id,'zxAnMgcDescription':zxAnMgcDescription,'zxAnMgcRowStatus':zxAnMgcRowStatus,'zxAnMgCfgTable':zxAnMgCfgTable,'zxAnMgCfgEntry':zxAnMgCfgEntry,_Z:zxAnMgId,'zxAnMgProtocolType':zxAnMgProtocolType,'zxAnMgCfgPort':zxAnMgCfgPort,'zxAnMgCfgDomainName':zxAnMgCfgDomainName,'zxAnMgDescription':zxAnMgDescription,'zxAnMgNamingType':zxAnMgNamingType,'zxAnMgcId1':zxAnMgcId1,'zxAnMgcId2':zxAnMgcId2,'zxAnMgcId3':zxAnMgcId3,'zxAnMgcId4':zxAnMgcId4,'zxAnCurrentMgcId':zxAnCurrentMgcId,'zxAnMgTranslay':zxAnMgTranslay,'zxAnMgTransProtocol':zxAnMgTransProtocol,'zxAnTransactionNum':zxAnTransactionNum,'zxAnRtpFaxPri1':zxAnRtpFaxPri1,'zxAnRtpFaxPri2':zxAnRtpFaxPri2,'zxAnSelfExchange':zxAnSelfExchange,'zxAnProtectCall':zxAnProtectCall,'zxAnRtp2833PayloadTypeCode':zxAnRtp2833PayloadTypeCode,'zxAnPacketMaxTransactionNumber':zxAnPacketMaxTransactionNumber,'zxAnHotlineWithSpace':zxAnHotlineWithSpace,'zxAnAlwaysReportOffhookEvent':zxAnAlwaysReportOffhookEvent,'zxAnAlwaysReportOnhookEvent':zxAnAlwaysReportOnhookEvent,'zxAnSubSuspendRtp':zxAnSubSuspendRtp,'zxAnDisasterProt':zxAnDisasterProt,'zxAnMgCfgRowStatus':zxAnMgCfgRowStatus,'zxAnH248ProtocolTable':zxAnH248ProtocolTable,'zxAnH248ProtocolEntry':zxAnH248ProtocolEntry,_a:zxAnH248ProtocolMgId,'zxAnH248ProtocolVersion':zxAnH248ProtocolVersion,'zxAnH248EncodingType':zxAnH248EncodingType,'zxAnH248PacketTokenAbbreviated':zxAnH248PacketTokenAbbreviated,'zxAnH248MinTransactionId':zxAnH248MinTransactionId,'zxAnH248MaxTransactionId':zxAnH248MaxTransactionId,'zxAnH248SendResponseAck':zxAnH248SendResponseAck,'zxAnH248ResponseCacheTime':zxAnH248ResponseCacheTime,'zxAnH248SendTransactionPending':zxAnH248SendTransactionPending,'zxAnH248ProfileNegotiation':zxAnH248ProfileNegotiation,'zxAnH248RebootMaxWaitingDelay':zxAnH248RebootMaxWaitingDelay,'zxAnH248MgcMaxInactivityTime':zxAnH248MgcMaxInactivityTime,'zxAnH248TranRetranMode':zxAnH248TranRetranMode,'zxAnH248TranRetranInterval':zxAnH248TranRetranInterval,'zxAnH248TranMaxRetries':zxAnH248TranMaxRetries,'zxAnH248TranPendInterval':zxAnH248TranPendInterval,'zxAnH248TranPendLimit':zxAnH248TranPendLimit,'zxAnH248HeartbeatMechanism':zxAnH248HeartbeatMechanism,'zxAnH248MgcHbMaxInactivityTime':zxAnH248MgcHbMaxInactivityTime,'zxAnH248HeartbeatFormat':zxAnH248HeartbeatFormat,'zxAnH248HbRetranInterval':zxAnH248HbRetranInterval,'zxAnH248HbMaxRetries':zxAnH248HbMaxRetries,'zxAnSlcTermIDTable':zxAnSlcTermIDTable,'zxAnSlcTermIDEntry':zxAnSlcTermIDEntry,_b:zxAnSlcTermIDRackNo,_c:zxAnSlcTermIDShelfNo,_d:zxAnSlcTermIDSlotNo,_e:zxAnSlcTermIDBeginIndex,'zxAnSlcTermIDOperSum':zxAnSlcTermIDOperSum,'zxAnSlcTermIDTMID':zxAnSlcTermIDTMID,'zxAnSlcTermIDType':zxAnSlcTermIDType,'zxAnSlcTermIDBeginNo':zxAnSlcTermIDBeginNo,'zxAnSlcTermIDDigitLen':zxAnSlcTermIDDigitLen,'zxAnSlcTermIDMgId':zxAnSlcTermIDMgId,'zxAnSlcTerminationID':zxAnSlcTerminationID,'zxAnSlcTermIDRowStatus':zxAnSlcTermIDRowStatus,'zxAnMgcpConfig':zxAnMgcpConfig,'zxAnMgcpMgcCfgTable':zxAnMgcpMgcCfgTable,'zxAnMgcpMgcCfgEntry':zxAnMgcpMgcCfgEntry,_f:zxAnMgcpMgcId,'zxAnMgcpMgcTypeId':zxAnMgcpMgcTypeId,'zxAnMgcpMgcPort':zxAnMgcpMgcPort,'zxAnMgcpMgcIpAddrType':zxAnMgcpMgcIpAddrType,'zxAnMgcpMgcIpAddress':zxAnMgcpMgcIpAddress,'zxAnMgcpMgcDomainName':zxAnMgcpMgcDomainName,'zxAnMgcpMgcDescription':zxAnMgcpMgcDescription,'zxAnMgcpMgcRowStatus':zxAnMgcpMgcRowStatus,'zxAnMgcpMgCfgTable':zxAnMgcpMgCfgTable,'zxAnMgcpMgCfgEntry':zxAnMgcpMgCfgEntry,_g:zxAnMgcpMgId,'zxAnMgcpMgPort':zxAnMgcpMgPort,'zxAnMgcpMgDomainName':zxAnMgcpMgDomainName,'zxAnMgcpMgDescription':zxAnMgcpMgDescription,'zxAnMgcpMgcId1':zxAnMgcpMgcId1,'zxAnMgcpMgcId2':zxAnMgcpMgcId2,'zxAnMgcpMgcId3':zxAnMgcpMgcId3,'zxAnMgcpMgcId4':zxAnMgcpMgcId4,'zxAnMgcpRtpFaxPri1':zxAnMgcpRtpFaxPri1,'zxAnMgcpRtpFaxPri2':zxAnMgcpRtpFaxPri2,'zxAnMgcpMgSelfSwitch':zxAnMgcpMgSelfSwitch,'zxAnMgcpMgProtectCall':zxAnMgcpMgProtectCall,'zxAnMgcpMgRtp2833Type':zxAnMgcpMgRtp2833Type,'zxAnMgcpMgRowStatus':zxAnMgcpMgRowStatus,'zxAnMgcpProtocolTable':zxAnMgcpProtocolTable,'zxAnMgcpProtocolEntry':zxAnMgcpProtocolEntry,_j:zxAnMgcpProtocolMgId,'zxAnMgcpProtocolVersion':zxAnMgcpProtocolVersion,'zxAnMgcpMgcMaxInactivityTime':zxAnMgcpMgcMaxInactivityTime,'zxAnMgcpMinTransactionId':zxAnMgcpMinTransactionId,'zxAnMgcpMaxTransactionId':zxAnMgcpMaxTransactionId,'zxAnMgcpResponseCacheTime':zxAnMgcpResponseCacheTime,'zxAnMgcpTranMaxRetries':zxAnMgcpTranMaxRetries,'zxAnMgcpTranPendInterval':zxAnMgcpTranPendInterval,'zxAnMgcpTranPendLimit':zxAnMgcpTranPendLimit,'zxAnMgcpRebootMaxWaitingDelay':zxAnMgcpRebootMaxWaitingDelay,'zxAnH248Perf':zxAnH248Perf,'zxAnH248PSRecMsg':zxAnH248PSRecMsg,'zxAnH248PSSendMsg':zxAnH248PSSendMsg,'zxAnH248PSRecMsgByte':zxAnH248PSRecMsgByte,'zxAnH248PSSendMsgByte':zxAnH248PSSendMsgByte,'zxAnH248PSProtocolError':zxAnH248PSProtocolError,'zxAnH248PSTimerOut':zxAnH248PSTimerOut,'zxAnH248PSDisconnect':zxAnH248PSDisconnect,'zxAnH248PSMGCChange':zxAnH248PSMGCChange,'zxAnH248PSTransmitError':zxAnH248PSTransmitError})