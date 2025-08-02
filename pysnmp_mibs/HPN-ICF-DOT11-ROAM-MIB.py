_N='hpnicfDot11RoamTrackIndex'
_M='hpnicfDot11MobGrpMemberIpAddr'
_L='HpnicfDot11RoamAuthMode'
_K='HpnicfDot11RoamMobileTunnelType'
_J='TruthValue'
_I='hpnicfDot11RoamClientMAC'
_H='second'
_G='hpnicfDot11MobGrpName'
_F='OctetString'
_E='not-accessible'
_D='read-create'
_C='HPN-ICF-DOT11-ROAM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfDot11,=mibBuilder.importSymbols('HPN-ICF-DOT11-REF-MIB','hpnicfDot11')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
hpnicfDot11ROAM=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,10))
if mibBuilder.loadTexts:hpnicfDot11ROAM.setRevisions(('2010-08-04 18:00','2009-05-07 20:00','2008-07-23 12:00'))
class HpnicfDot11RoamMobileTunnelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
class HpnicfDot11RoamAuthMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('md5',2)))
class HpnicfDot11RoamIACTPStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('idle',2),('joinRequestWait',3),('joinResponseWait',4),('joinConfirmWait',5),('joinError',6),('run',7)))
_HpnicfDot11RoamCfgGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RoamCfgGroup=_HpnicfDot11RoamCfgGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1))
_HpnicfDot11MobGrpTable_Object=MibTable
hpnicfDot11MobGrpTable=_HpnicfDot11MobGrpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1))
if mibBuilder.loadTexts:hpnicfDot11MobGrpTable.setStatus(_A)
_HpnicfDot11MobGrpEntry_Object=MibTableRow
hpnicfDot11MobGrpEntry=_HpnicfDot11MobGrpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1))
hpnicfDot11MobGrpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:hpnicfDot11MobGrpEntry.setStatus(_A)
class _HpnicfDot11MobGrpName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_HpnicfDot11MobGrpName_Type.__name__=_F
_HpnicfDot11MobGrpName_Object=MibTableColumn
hpnicfDot11MobGrpName=_HpnicfDot11MobGrpName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1,1),_HpnicfDot11MobGrpName_Type())
hpnicfDot11MobGrpName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11MobGrpName.setStatus(_A)
class _Hpnicfdot11MobGrpTunnelType_Type(HpnicfDot11RoamMobileTunnelType):defaultValue=1
_Hpnicfdot11MobGrpTunnelType_Type.__name__=_K
_Hpnicfdot11MobGrpTunnelType_Object=MibTableColumn
hpnicfdot11MobGrpTunnelType=_Hpnicfdot11MobGrpTunnelType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1,2),_Hpnicfdot11MobGrpTunnelType_Type())
hpnicfdot11MobGrpTunnelType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot11MobGrpTunnelType.setStatus(_A)
_HpnicfDot11MobGrpSrcIPAddr_Type=InetAddress
_HpnicfDot11MobGrpSrcIPAddr_Object=MibTableColumn
hpnicfDot11MobGrpSrcIPAddr=_HpnicfDot11MobGrpSrcIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1,3),_HpnicfDot11MobGrpSrcIPAddr_Type())
hpnicfDot11MobGrpSrcIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11MobGrpSrcIPAddr.setStatus(_A)
class _HpnicfDot11MobGrpAuthMode_Type(HpnicfDot11RoamAuthMode):defaultValue=1
_HpnicfDot11MobGrpAuthMode_Type.__name__=_L
_HpnicfDot11MobGrpAuthMode_Object=MibTableColumn
hpnicfDot11MobGrpAuthMode=_HpnicfDot11MobGrpAuthMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1,4),_HpnicfDot11MobGrpAuthMode_Type())
hpnicfDot11MobGrpAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11MobGrpAuthMode.setStatus(_A)
class _HpnicfDot11MobGrpAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HpnicfDot11MobGrpAuthKey_Type.__name__=_F
_HpnicfDot11MobGrpAuthKey_Object=MibTableColumn
hpnicfDot11MobGrpAuthKey=_HpnicfDot11MobGrpAuthKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1,5),_HpnicfDot11MobGrpAuthKey_Type())
hpnicfDot11MobGrpAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11MobGrpAuthKey.setStatus(_A)
class _HpnicfDot11MobGrpEnable_Type(TruthValue):defaultValue=2
_HpnicfDot11MobGrpEnable_Type.__name__=_J
_HpnicfDot11MobGrpEnable_Object=MibTableColumn
hpnicfDot11MobGrpEnable=_HpnicfDot11MobGrpEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1,6),_HpnicfDot11MobGrpEnable_Type())
hpnicfDot11MobGrpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11MobGrpEnable.setStatus(_A)
_HpnicfDot11MobGrpRowStatus_Type=RowStatus
_HpnicfDot11MobGrpRowStatus_Object=MibTableColumn
hpnicfDot11MobGrpRowStatus=_HpnicfDot11MobGrpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,1,1,7),_HpnicfDot11MobGrpRowStatus_Type())
hpnicfDot11MobGrpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11MobGrpRowStatus.setStatus(_A)
_HpnicfDot11MobGrpMemberTable_Object=MibTable
hpnicfDot11MobGrpMemberTable=_HpnicfDot11MobGrpMemberTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,2))
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberTable.setStatus(_A)
_HpnicfDot11MobGrpMemberEntry_Object=MibTableRow
hpnicfDot11MobGrpMemberEntry=_HpnicfDot11MobGrpMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,2,1))
hpnicfDot11MobGrpMemberEntry.setIndexNames((0,_C,_G),(0,_C,_M))
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberEntry.setStatus(_A)
_HpnicfDot11MobGrpMemberIpAddr_Type=InetAddress
_HpnicfDot11MobGrpMemberIpAddr_Object=MibTableColumn
hpnicfDot11MobGrpMemberIpAddr=_HpnicfDot11MobGrpMemberIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,2,1,1),_HpnicfDot11MobGrpMemberIpAddr_Type())
hpnicfDot11MobGrpMemberIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberIpAddr.setStatus(_A)
_HpnicfDot11MobGrpMemberStatus_Type=HpnicfDot11RoamIACTPStatus
_HpnicfDot11MobGrpMemberStatus_Object=MibTableColumn
hpnicfDot11MobGrpMemberStatus=_HpnicfDot11MobGrpMemberStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,2,1,2),_HpnicfDot11MobGrpMemberStatus_Type())
hpnicfDot11MobGrpMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberStatus.setStatus(_A)
_HpnicfDot11MobGrpMemberIf_Type=OctetString
_HpnicfDot11MobGrpMemberIf_Object=MibTableColumn
hpnicfDot11MobGrpMemberIf=_HpnicfDot11MobGrpMemberIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,2,1,3),_HpnicfDot11MobGrpMemberIf_Type())
hpnicfDot11MobGrpMemberIf.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberIf.setStatus(_A)
_HpnicfDot11MobGrpMemberUpTime_Type=Integer32
_HpnicfDot11MobGrpMemberUpTime_Object=MibTableColumn
hpnicfDot11MobGrpMemberUpTime=_HpnicfDot11MobGrpMemberUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,2,1,4),_HpnicfDot11MobGrpMemberUpTime_Type())
hpnicfDot11MobGrpMemberUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberUpTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberUpTime.setUnits(_H)
_HpnicfDot11MobGrpMemberRowStatus_Type=RowStatus
_HpnicfDot11MobGrpMemberRowStatus_Object=MibTableColumn
hpnicfDot11MobGrpMemberRowStatus=_HpnicfDot11MobGrpMemberRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,1,2,1,5),_HpnicfDot11MobGrpMemberRowStatus_Type())
hpnicfDot11MobGrpMemberRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11MobGrpMemberRowStatus.setStatus(_A)
_HpnicfDot11RoamStatusGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RoamStatusGroup=_HpnicfDot11RoamStatusGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2))
_HpnicfDot11RoamInInfoTable_Object=MibTable
hpnicfDot11RoamInInfoTable=_HpnicfDot11RoamInInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,1))
if mibBuilder.loadTexts:hpnicfDot11RoamInInfoTable.setStatus(_A)
_HpnicfDot11RoamInInfoEntry_Object=MibTableRow
hpnicfDot11RoamInInfoEntry=_HpnicfDot11RoamInInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,1,1))
hpnicfDot11RoamInInfoEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:hpnicfDot11RoamInInfoEntry.setStatus(_A)
_HpnicfDot11RoamClientMAC_Type=MacAddress
_HpnicfDot11RoamClientMAC_Object=MibTableColumn
hpnicfDot11RoamClientMAC=_HpnicfDot11RoamClientMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,1,1,1),_HpnicfDot11RoamClientMAC_Type())
hpnicfDot11RoamClientMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11RoamClientMAC.setStatus(_A)
_HpnicfDot11RoamInClientBSSID_Type=MacAddress
_HpnicfDot11RoamInClientBSSID_Object=MibTableColumn
hpnicfDot11RoamInClientBSSID=_HpnicfDot11RoamInClientBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,1,1,2),_HpnicfDot11RoamInClientBSSID_Type())
hpnicfDot11RoamInClientBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamInClientBSSID.setStatus(_A)
_HpnicfDot11RoamInClientVlanID_Type=Integer32
_HpnicfDot11RoamInClientVlanID_Object=MibTableColumn
hpnicfDot11RoamInClientVlanID=_HpnicfDot11RoamInClientVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,1,1,3),_HpnicfDot11RoamInClientVlanID_Type())
hpnicfDot11RoamInClientVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamInClientVlanID.setStatus(_A)
_HpnicfDot11RoamInHomeACIPType_Type=InetAddressType
_HpnicfDot11RoamInHomeACIPType_Object=MibTableColumn
hpnicfDot11RoamInHomeACIPType=_HpnicfDot11RoamInHomeACIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,1,1,4),_HpnicfDot11RoamInHomeACIPType_Type())
hpnicfDot11RoamInHomeACIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamInHomeACIPType.setStatus(_A)
_HpnicfDot11RoamInHomeACIPAddr_Type=InetAddress
_HpnicfDot11RoamInHomeACIPAddr_Object=MibTableColumn
hpnicfDot11RoamInHomeACIPAddr=_HpnicfDot11RoamInHomeACIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,1,1,5),_HpnicfDot11RoamInHomeACIPAddr_Type())
hpnicfDot11RoamInHomeACIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamInHomeACIPAddr.setStatus(_A)
_HpnicfDot11RoamOutInfoTable_Object=MibTable
hpnicfDot11RoamOutInfoTable=_HpnicfDot11RoamOutInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,2))
if mibBuilder.loadTexts:hpnicfDot11RoamOutInfoTable.setStatus(_A)
_HpnicfDot11RoamOutInfoEntry_Object=MibTableRow
hpnicfDot11RoamOutInfoEntry=_HpnicfDot11RoamOutInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,2,1))
hpnicfDot11RoamOutInfoEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:hpnicfDot11RoamOutInfoEntry.setStatus(_A)
_HpnicfDot11RoamOutClientBSSID_Type=MacAddress
_HpnicfDot11RoamOutClientBSSID_Object=MibTableColumn
hpnicfDot11RoamOutClientBSSID=_HpnicfDot11RoamOutClientBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,2,1,1),_HpnicfDot11RoamOutClientBSSID_Type())
hpnicfDot11RoamOutClientBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamOutClientBSSID.setStatus(_A)
_HpnicfDot11RoamOutClientVlanID_Type=Integer32
_HpnicfDot11RoamOutClientVlanID_Object=MibTableColumn
hpnicfDot11RoamOutClientVlanID=_HpnicfDot11RoamOutClientVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,2,1,2),_HpnicfDot11RoamOutClientVlanID_Type())
hpnicfDot11RoamOutClientVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamOutClientVlanID.setStatus(_A)
_HpnicfDot11RoamOutForeignACIPType_Type=InetAddressType
_HpnicfDot11RoamOutForeignACIPType_Object=MibTableColumn
hpnicfDot11RoamOutForeignACIPType=_HpnicfDot11RoamOutForeignACIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,2,1,3),_HpnicfDot11RoamOutForeignACIPType_Type())
hpnicfDot11RoamOutForeignACIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamOutForeignACIPType.setStatus(_A)
_HpnicfDot11RoamOutForeignACIPAddr_Type=InetAddress
_HpnicfDot11RoamOutForeignACIPAddr_Object=MibTableColumn
hpnicfDot11RoamOutForeignACIPAddr=_HpnicfDot11RoamOutForeignACIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,2,1,4),_HpnicfDot11RoamOutForeignACIPAddr_Type())
hpnicfDot11RoamOutForeignACIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamOutForeignACIPAddr.setStatus(_A)
_HpnicfDot11RoamOutClientUpTime_Type=Integer32
_HpnicfDot11RoamOutClientUpTime_Object=MibTableColumn
hpnicfDot11RoamOutClientUpTime=_HpnicfDot11RoamOutClientUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,2,1,5),_HpnicfDot11RoamOutClientUpTime_Type())
hpnicfDot11RoamOutClientUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamOutClientUpTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RoamOutClientUpTime.setUnits(_H)
_HpnicfDot11RoamTrackTable_Object=MibTable
hpnicfDot11RoamTrackTable=_HpnicfDot11RoamTrackTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3))
if mibBuilder.loadTexts:hpnicfDot11RoamTrackTable.setStatus(_A)
_HpnicfDot11RoamTrackEntry_Object=MibTableRow
hpnicfDot11RoamTrackEntry=_HpnicfDot11RoamTrackEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3,1))
hpnicfDot11RoamTrackEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:hpnicfDot11RoamTrackEntry.setStatus(_A)
_HpnicfDot11RoamTrackIndex_Type=Integer32
_HpnicfDot11RoamTrackIndex_Object=MibTableColumn
hpnicfDot11RoamTrackIndex=_HpnicfDot11RoamTrackIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3,1,1),_HpnicfDot11RoamTrackIndex_Type())
hpnicfDot11RoamTrackIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDot11RoamTrackIndex.setStatus(_A)
_HpnicfDot11RoamTrackClientMAC_Type=MacAddress
_HpnicfDot11RoamTrackClientMAC_Object=MibTableColumn
hpnicfDot11RoamTrackClientMAC=_HpnicfDot11RoamTrackClientMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3,1,2),_HpnicfDot11RoamTrackClientMAC_Type())
hpnicfDot11RoamTrackClientMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamTrackClientMAC.setStatus(_A)
_HpnicfDot11RoamTrackBSSID_Type=MacAddress
_HpnicfDot11RoamTrackBSSID_Object=MibTableColumn
hpnicfDot11RoamTrackBSSID=_HpnicfDot11RoamTrackBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3,1,3),_HpnicfDot11RoamTrackBSSID_Type())
hpnicfDot11RoamTrackBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamTrackBSSID.setStatus(_A)
_HpnicfDot11RoamTrackUpTime_Type=Integer32
_HpnicfDot11RoamTrackUpTime_Object=MibTableColumn
hpnicfDot11RoamTrackUpTime=_HpnicfDot11RoamTrackUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3,1,4),_HpnicfDot11RoamTrackUpTime_Type())
hpnicfDot11RoamTrackUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamTrackUpTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RoamTrackUpTime.setUnits(_H)
_HpnicfDot11RoamTrackACIPType_Type=InetAddressType
_HpnicfDot11RoamTrackACIPType_Object=MibTableColumn
hpnicfDot11RoamTrackACIPType=_HpnicfDot11RoamTrackACIPType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3,1,5),_HpnicfDot11RoamTrackACIPType_Type())
hpnicfDot11RoamTrackACIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamTrackACIPType.setStatus(_A)
_HpnicfDot11RoamTrackACIPAddr_Type=InetAddress
_HpnicfDot11RoamTrackACIPAddr_Object=MibTableColumn
hpnicfDot11RoamTrackACIPAddr=_HpnicfDot11RoamTrackACIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,2,3,1,6),_HpnicfDot11RoamTrackACIPAddr_Type())
hpnicfDot11RoamTrackACIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RoamTrackACIPAddr.setStatus(_A)
_HpnicfDot11RoamStatisGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RoamStatisGroup=_HpnicfDot11RoamStatisGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,10,3))
_HpnicfDot11IntraACRoamingSuccCnt_Type=Integer32
_HpnicfDot11IntraACRoamingSuccCnt_Object=MibScalar
hpnicfDot11IntraACRoamingSuccCnt=_HpnicfDot11IntraACRoamingSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,3,1),_HpnicfDot11IntraACRoamingSuccCnt_Type())
hpnicfDot11IntraACRoamingSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11IntraACRoamingSuccCnt.setStatus(_A)
_HpnicfDot11InterACRoamingSuccCnt_Type=Integer32
_HpnicfDot11InterACRoamingSuccCnt_Object=MibScalar
hpnicfDot11InterACRoamingSuccCnt=_HpnicfDot11InterACRoamingSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,3,2),_HpnicfDot11InterACRoamingSuccCnt_Type())
hpnicfDot11InterACRoamingSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11InterACRoamingSuccCnt.setStatus(_A)
_HpnicfDot11InterACRoamOutSuccCnt_Type=Integer32
_HpnicfDot11InterACRoamOutSuccCnt_Object=MibScalar
hpnicfDot11InterACRoamOutSuccCnt=_HpnicfDot11InterACRoamOutSuccCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,3,3),_HpnicfDot11InterACRoamOutSuccCnt_Type())
hpnicfDot11InterACRoamOutSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11InterACRoamOutSuccCnt.setStatus(_A)
_HpnicfDot11RoamStatis2Group_ObjectIdentity=ObjectIdentity
hpnicfDot11RoamStatis2Group=_HpnicfDot11RoamStatis2Group_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,10,4))
_HpnicfDot11IntraACRoamingSuccCnt2_Type=Counter32
_HpnicfDot11IntraACRoamingSuccCnt2_Object=MibScalar
hpnicfDot11IntraACRoamingSuccCnt2=_HpnicfDot11IntraACRoamingSuccCnt2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,4,1),_HpnicfDot11IntraACRoamingSuccCnt2_Type())
hpnicfDot11IntraACRoamingSuccCnt2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11IntraACRoamingSuccCnt2.setStatus(_A)
_HpnicfDot11InterACRoamingSuccCnt2_Type=Counter32
_HpnicfDot11InterACRoamingSuccCnt2_Object=MibScalar
hpnicfDot11InterACRoamingSuccCnt2=_HpnicfDot11InterACRoamingSuccCnt2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,4,2),_HpnicfDot11InterACRoamingSuccCnt2_Type())
hpnicfDot11InterACRoamingSuccCnt2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11InterACRoamingSuccCnt2.setStatus(_A)
_HpnicfDot11InterACRoamOutSuccCnt2_Type=Counter32
_HpnicfDot11InterACRoamOutSuccCnt2_Object=MibScalar
hpnicfDot11InterACRoamOutSuccCnt2=_HpnicfDot11InterACRoamOutSuccCnt2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,10,4,3),_HpnicfDot11InterACRoamOutSuccCnt2_Type())
hpnicfDot11InterACRoamOutSuccCnt2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11InterACRoamOutSuccCnt2.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_K:HpnicfDot11RoamMobileTunnelType,_L:HpnicfDot11RoamAuthMode,'HpnicfDot11RoamIACTPStatus':HpnicfDot11RoamIACTPStatus,'hpnicfDot11ROAM':hpnicfDot11ROAM,'hpnicfDot11RoamCfgGroup':hpnicfDot11RoamCfgGroup,'hpnicfDot11MobGrpTable':hpnicfDot11MobGrpTable,'hpnicfDot11MobGrpEntry':hpnicfDot11MobGrpEntry,_G:hpnicfDot11MobGrpName,'hpnicfdot11MobGrpTunnelType':hpnicfdot11MobGrpTunnelType,'hpnicfDot11MobGrpSrcIPAddr':hpnicfDot11MobGrpSrcIPAddr,'hpnicfDot11MobGrpAuthMode':hpnicfDot11MobGrpAuthMode,'hpnicfDot11MobGrpAuthKey':hpnicfDot11MobGrpAuthKey,'hpnicfDot11MobGrpEnable':hpnicfDot11MobGrpEnable,'hpnicfDot11MobGrpRowStatus':hpnicfDot11MobGrpRowStatus,'hpnicfDot11MobGrpMemberTable':hpnicfDot11MobGrpMemberTable,'hpnicfDot11MobGrpMemberEntry':hpnicfDot11MobGrpMemberEntry,_M:hpnicfDot11MobGrpMemberIpAddr,'hpnicfDot11MobGrpMemberStatus':hpnicfDot11MobGrpMemberStatus,'hpnicfDot11MobGrpMemberIf':hpnicfDot11MobGrpMemberIf,'hpnicfDot11MobGrpMemberUpTime':hpnicfDot11MobGrpMemberUpTime,'hpnicfDot11MobGrpMemberRowStatus':hpnicfDot11MobGrpMemberRowStatus,'hpnicfDot11RoamStatusGroup':hpnicfDot11RoamStatusGroup,'hpnicfDot11RoamInInfoTable':hpnicfDot11RoamInInfoTable,'hpnicfDot11RoamInInfoEntry':hpnicfDot11RoamInInfoEntry,_I:hpnicfDot11RoamClientMAC,'hpnicfDot11RoamInClientBSSID':hpnicfDot11RoamInClientBSSID,'hpnicfDot11RoamInClientVlanID':hpnicfDot11RoamInClientVlanID,'hpnicfDot11RoamInHomeACIPType':hpnicfDot11RoamInHomeACIPType,'hpnicfDot11RoamInHomeACIPAddr':hpnicfDot11RoamInHomeACIPAddr,'hpnicfDot11RoamOutInfoTable':hpnicfDot11RoamOutInfoTable,'hpnicfDot11RoamOutInfoEntry':hpnicfDot11RoamOutInfoEntry,'hpnicfDot11RoamOutClientBSSID':hpnicfDot11RoamOutClientBSSID,'hpnicfDot11RoamOutClientVlanID':hpnicfDot11RoamOutClientVlanID,'hpnicfDot11RoamOutForeignACIPType':hpnicfDot11RoamOutForeignACIPType,'hpnicfDot11RoamOutForeignACIPAddr':hpnicfDot11RoamOutForeignACIPAddr,'hpnicfDot11RoamOutClientUpTime':hpnicfDot11RoamOutClientUpTime,'hpnicfDot11RoamTrackTable':hpnicfDot11RoamTrackTable,'hpnicfDot11RoamTrackEntry':hpnicfDot11RoamTrackEntry,_N:hpnicfDot11RoamTrackIndex,'hpnicfDot11RoamTrackClientMAC':hpnicfDot11RoamTrackClientMAC,'hpnicfDot11RoamTrackBSSID':hpnicfDot11RoamTrackBSSID,'hpnicfDot11RoamTrackUpTime':hpnicfDot11RoamTrackUpTime,'hpnicfDot11RoamTrackACIPType':hpnicfDot11RoamTrackACIPType,'hpnicfDot11RoamTrackACIPAddr':hpnicfDot11RoamTrackACIPAddr,'hpnicfDot11RoamStatisGroup':hpnicfDot11RoamStatisGroup,'hpnicfDot11IntraACRoamingSuccCnt':hpnicfDot11IntraACRoamingSuccCnt,'hpnicfDot11InterACRoamingSuccCnt':hpnicfDot11InterACRoamingSuccCnt,'hpnicfDot11InterACRoamOutSuccCnt':hpnicfDot11InterACRoamOutSuccCnt,'hpnicfDot11RoamStatis2Group':hpnicfDot11RoamStatis2Group,'hpnicfDot11IntraACRoamingSuccCnt2':hpnicfDot11IntraACRoamingSuccCnt2,'hpnicfDot11InterACRoamingSuccCnt2':hpnicfDot11InterACRoamingSuccCnt2,'hpnicfDot11InterACRoamOutSuccCnt2':hpnicfDot11InterACRoamOutSuccCnt2})