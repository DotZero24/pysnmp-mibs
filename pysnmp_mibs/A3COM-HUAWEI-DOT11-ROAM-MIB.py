_N='h3cDot11RoamTrackIndex'
_M='h3cDot11MobGrpMemberIpAddr'
_L='H3cDot11RoamAuthMode'
_K='H3cDot11RoamMobileTunnelType'
_J='TruthValue'
_I='h3cDot11RoamClientMAC'
_H='second'
_G='h3cDot11MobGrpName'
_F='OctetString'
_E='not-accessible'
_D='read-create'
_C='A3COM-HUAWEI-DOT11-ROAM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cDot11,=mibBuilder.importSymbols('A3COM-HUAWEI-DOT11-REF-MIB','h3cDot11')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
h3cDot11ROAM=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,75,10))
if mibBuilder.loadTexts:h3cDot11ROAM.setRevisions(('2010-08-04 18:00','2009-05-07 20:00','2008-07-23 12:00'))
class H3cDot11RoamMobileTunnelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
class H3cDot11RoamAuthMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('md5',2)))
class H3cDot11RoamIACTPStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('idle',2),('joinRequestWait',3),('joinResponseWait',4),('joinConfirmWait',5),('joinError',6),('run',7)))
_H3cDot11RoamCfgGroup_ObjectIdentity=ObjectIdentity
h3cDot11RoamCfgGroup=_H3cDot11RoamCfgGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,10,1))
_H3cDot11MobGrpTable_Object=MibTable
h3cDot11MobGrpTable=_H3cDot11MobGrpTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1))
if mibBuilder.loadTexts:h3cDot11MobGrpTable.setStatus(_A)
_H3cDot11MobGrpEntry_Object=MibTableRow
h3cDot11MobGrpEntry=_H3cDot11MobGrpEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1))
h3cDot11MobGrpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:h3cDot11MobGrpEntry.setStatus(_A)
class _H3cDot11MobGrpName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_H3cDot11MobGrpName_Type.__name__=_F
_H3cDot11MobGrpName_Object=MibTableColumn
h3cDot11MobGrpName=_H3cDot11MobGrpName_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1,1),_H3cDot11MobGrpName_Type())
h3cDot11MobGrpName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11MobGrpName.setStatus(_A)
class _H3cdot11MobGrpTunnelType_Type(H3cDot11RoamMobileTunnelType):defaultValue=1
_H3cdot11MobGrpTunnelType_Type.__name__=_K
_H3cdot11MobGrpTunnelType_Object=MibTableColumn
h3cdot11MobGrpTunnelType=_H3cdot11MobGrpTunnelType_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1,2),_H3cdot11MobGrpTunnelType_Type())
h3cdot11MobGrpTunnelType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdot11MobGrpTunnelType.setStatus(_A)
_H3cDot11MobGrpSrcIPAddr_Type=InetAddress
_H3cDot11MobGrpSrcIPAddr_Object=MibTableColumn
h3cDot11MobGrpSrcIPAddr=_H3cDot11MobGrpSrcIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1,3),_H3cDot11MobGrpSrcIPAddr_Type())
h3cDot11MobGrpSrcIPAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MobGrpSrcIPAddr.setStatus(_A)
class _H3cDot11MobGrpAuthMode_Type(H3cDot11RoamAuthMode):defaultValue=1
_H3cDot11MobGrpAuthMode_Type.__name__=_L
_H3cDot11MobGrpAuthMode_Object=MibTableColumn
h3cDot11MobGrpAuthMode=_H3cDot11MobGrpAuthMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1,4),_H3cDot11MobGrpAuthMode_Type())
h3cDot11MobGrpAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MobGrpAuthMode.setStatus(_A)
class _H3cDot11MobGrpAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_H3cDot11MobGrpAuthKey_Type.__name__=_F
_H3cDot11MobGrpAuthKey_Object=MibTableColumn
h3cDot11MobGrpAuthKey=_H3cDot11MobGrpAuthKey_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1,5),_H3cDot11MobGrpAuthKey_Type())
h3cDot11MobGrpAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MobGrpAuthKey.setStatus(_A)
class _H3cDot11MobGrpEnable_Type(TruthValue):defaultValue=2
_H3cDot11MobGrpEnable_Type.__name__=_J
_H3cDot11MobGrpEnable_Object=MibTableColumn
h3cDot11MobGrpEnable=_H3cDot11MobGrpEnable_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1,6),_H3cDot11MobGrpEnable_Type())
h3cDot11MobGrpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MobGrpEnable.setStatus(_A)
_H3cDot11MobGrpRowStatus_Type=RowStatus
_H3cDot11MobGrpRowStatus_Object=MibTableColumn
h3cDot11MobGrpRowStatus=_H3cDot11MobGrpRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,1,1,7),_H3cDot11MobGrpRowStatus_Type())
h3cDot11MobGrpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MobGrpRowStatus.setStatus(_A)
_H3cDot11MobGrpMemberTable_Object=MibTable
h3cDot11MobGrpMemberTable=_H3cDot11MobGrpMemberTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,2))
if mibBuilder.loadTexts:h3cDot11MobGrpMemberTable.setStatus(_A)
_H3cDot11MobGrpMemberEntry_Object=MibTableRow
h3cDot11MobGrpMemberEntry=_H3cDot11MobGrpMemberEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,2,1))
h3cDot11MobGrpMemberEntry.setIndexNames((0,_C,_G),(0,_C,_M))
if mibBuilder.loadTexts:h3cDot11MobGrpMemberEntry.setStatus(_A)
_H3cDot11MobGrpMemberIpAddr_Type=InetAddress
_H3cDot11MobGrpMemberIpAddr_Object=MibTableColumn
h3cDot11MobGrpMemberIpAddr=_H3cDot11MobGrpMemberIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,2,1,1),_H3cDot11MobGrpMemberIpAddr_Type())
h3cDot11MobGrpMemberIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11MobGrpMemberIpAddr.setStatus(_A)
_H3cDot11MobGrpMemberStatus_Type=H3cDot11RoamIACTPStatus
_H3cDot11MobGrpMemberStatus_Object=MibTableColumn
h3cDot11MobGrpMemberStatus=_H3cDot11MobGrpMemberStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,2,1,2),_H3cDot11MobGrpMemberStatus_Type())
h3cDot11MobGrpMemberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MobGrpMemberStatus.setStatus(_A)
_H3cDot11MobGrpMemberIf_Type=OctetString
_H3cDot11MobGrpMemberIf_Object=MibTableColumn
h3cDot11MobGrpMemberIf=_H3cDot11MobGrpMemberIf_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,2,1,3),_H3cDot11MobGrpMemberIf_Type())
h3cDot11MobGrpMemberIf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MobGrpMemberIf.setStatus(_A)
_H3cDot11MobGrpMemberUpTime_Type=Integer32
_H3cDot11MobGrpMemberUpTime_Object=MibTableColumn
h3cDot11MobGrpMemberUpTime=_H3cDot11MobGrpMemberUpTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,2,1,4),_H3cDot11MobGrpMemberUpTime_Type())
h3cDot11MobGrpMemberUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MobGrpMemberUpTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11MobGrpMemberUpTime.setUnits(_H)
_H3cDot11MobGrpMemberRowStatus_Type=RowStatus
_H3cDot11MobGrpMemberRowStatus_Object=MibTableColumn
h3cDot11MobGrpMemberRowStatus=_H3cDot11MobGrpMemberRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,1,2,1,5),_H3cDot11MobGrpMemberRowStatus_Type())
h3cDot11MobGrpMemberRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MobGrpMemberRowStatus.setStatus(_A)
_H3cDot11RoamStatusGroup_ObjectIdentity=ObjectIdentity
h3cDot11RoamStatusGroup=_H3cDot11RoamStatusGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,10,2))
_H3cDot11RoamInInfoTable_Object=MibTable
h3cDot11RoamInInfoTable=_H3cDot11RoamInInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,1))
if mibBuilder.loadTexts:h3cDot11RoamInInfoTable.setStatus(_A)
_H3cDot11RoamInInfoEntry_Object=MibTableRow
h3cDot11RoamInInfoEntry=_H3cDot11RoamInInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,1,1))
h3cDot11RoamInInfoEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:h3cDot11RoamInInfoEntry.setStatus(_A)
_H3cDot11RoamClientMAC_Type=MacAddress
_H3cDot11RoamClientMAC_Object=MibTableColumn
h3cDot11RoamClientMAC=_H3cDot11RoamClientMAC_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,1,1,1),_H3cDot11RoamClientMAC_Type())
h3cDot11RoamClientMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11RoamClientMAC.setStatus(_A)
_H3cDot11RoamInClientBSSID_Type=MacAddress
_H3cDot11RoamInClientBSSID_Object=MibTableColumn
h3cDot11RoamInClientBSSID=_H3cDot11RoamInClientBSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,1,1,2),_H3cDot11RoamInClientBSSID_Type())
h3cDot11RoamInClientBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamInClientBSSID.setStatus(_A)
_H3cDot11RoamInClientVlanID_Type=Integer32
_H3cDot11RoamInClientVlanID_Object=MibTableColumn
h3cDot11RoamInClientVlanID=_H3cDot11RoamInClientVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,1,1,3),_H3cDot11RoamInClientVlanID_Type())
h3cDot11RoamInClientVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamInClientVlanID.setStatus(_A)
_H3cDot11RoamInHomeACIPType_Type=InetAddressType
_H3cDot11RoamInHomeACIPType_Object=MibTableColumn
h3cDot11RoamInHomeACIPType=_H3cDot11RoamInHomeACIPType_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,1,1,4),_H3cDot11RoamInHomeACIPType_Type())
h3cDot11RoamInHomeACIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamInHomeACIPType.setStatus(_A)
_H3cDot11RoamInHomeACIPAddr_Type=InetAddress
_H3cDot11RoamInHomeACIPAddr_Object=MibTableColumn
h3cDot11RoamInHomeACIPAddr=_H3cDot11RoamInHomeACIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,1,1,5),_H3cDot11RoamInHomeACIPAddr_Type())
h3cDot11RoamInHomeACIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamInHomeACIPAddr.setStatus(_A)
_H3cDot11RoamOutInfoTable_Object=MibTable
h3cDot11RoamOutInfoTable=_H3cDot11RoamOutInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,2))
if mibBuilder.loadTexts:h3cDot11RoamOutInfoTable.setStatus(_A)
_H3cDot11RoamOutInfoEntry_Object=MibTableRow
h3cDot11RoamOutInfoEntry=_H3cDot11RoamOutInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,2,1))
h3cDot11RoamOutInfoEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:h3cDot11RoamOutInfoEntry.setStatus(_A)
_H3cDot11RoamOutClientBSSID_Type=MacAddress
_H3cDot11RoamOutClientBSSID_Object=MibTableColumn
h3cDot11RoamOutClientBSSID=_H3cDot11RoamOutClientBSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,2,1,1),_H3cDot11RoamOutClientBSSID_Type())
h3cDot11RoamOutClientBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamOutClientBSSID.setStatus(_A)
_H3cDot11RoamOutClientVlanID_Type=Integer32
_H3cDot11RoamOutClientVlanID_Object=MibTableColumn
h3cDot11RoamOutClientVlanID=_H3cDot11RoamOutClientVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,2,1,2),_H3cDot11RoamOutClientVlanID_Type())
h3cDot11RoamOutClientVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamOutClientVlanID.setStatus(_A)
_H3cDot11RoamOutForeignACIPType_Type=InetAddressType
_H3cDot11RoamOutForeignACIPType_Object=MibTableColumn
h3cDot11RoamOutForeignACIPType=_H3cDot11RoamOutForeignACIPType_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,2,1,3),_H3cDot11RoamOutForeignACIPType_Type())
h3cDot11RoamOutForeignACIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamOutForeignACIPType.setStatus(_A)
_H3cDot11RoamOutForeignACIPAddr_Type=InetAddress
_H3cDot11RoamOutForeignACIPAddr_Object=MibTableColumn
h3cDot11RoamOutForeignACIPAddr=_H3cDot11RoamOutForeignACIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,2,1,4),_H3cDot11RoamOutForeignACIPAddr_Type())
h3cDot11RoamOutForeignACIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamOutForeignACIPAddr.setStatus(_A)
_H3cDot11RoamOutClientUpTime_Type=Integer32
_H3cDot11RoamOutClientUpTime_Object=MibTableColumn
h3cDot11RoamOutClientUpTime=_H3cDot11RoamOutClientUpTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,2,1,5),_H3cDot11RoamOutClientUpTime_Type())
h3cDot11RoamOutClientUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamOutClientUpTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RoamOutClientUpTime.setUnits(_H)
_H3cDot11RoamTrackTable_Object=MibTable
h3cDot11RoamTrackTable=_H3cDot11RoamTrackTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3))
if mibBuilder.loadTexts:h3cDot11RoamTrackTable.setStatus(_A)
_H3cDot11RoamTrackEntry_Object=MibTableRow
h3cDot11RoamTrackEntry=_H3cDot11RoamTrackEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3,1))
h3cDot11RoamTrackEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:h3cDot11RoamTrackEntry.setStatus(_A)
_H3cDot11RoamTrackIndex_Type=Integer32
_H3cDot11RoamTrackIndex_Object=MibTableColumn
h3cDot11RoamTrackIndex=_H3cDot11RoamTrackIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3,1,1),_H3cDot11RoamTrackIndex_Type())
h3cDot11RoamTrackIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11RoamTrackIndex.setStatus(_A)
_H3cDot11RoamTrackClientMAC_Type=MacAddress
_H3cDot11RoamTrackClientMAC_Object=MibTableColumn
h3cDot11RoamTrackClientMAC=_H3cDot11RoamTrackClientMAC_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3,1,2),_H3cDot11RoamTrackClientMAC_Type())
h3cDot11RoamTrackClientMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamTrackClientMAC.setStatus(_A)
_H3cDot11RoamTrackBSSID_Type=MacAddress
_H3cDot11RoamTrackBSSID_Object=MibTableColumn
h3cDot11RoamTrackBSSID=_H3cDot11RoamTrackBSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3,1,3),_H3cDot11RoamTrackBSSID_Type())
h3cDot11RoamTrackBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamTrackBSSID.setStatus(_A)
_H3cDot11RoamTrackUpTime_Type=Integer32
_H3cDot11RoamTrackUpTime_Object=MibTableColumn
h3cDot11RoamTrackUpTime=_H3cDot11RoamTrackUpTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3,1,4),_H3cDot11RoamTrackUpTime_Type())
h3cDot11RoamTrackUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamTrackUpTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RoamTrackUpTime.setUnits(_H)
_H3cDot11RoamTrackACIPType_Type=InetAddressType
_H3cDot11RoamTrackACIPType_Object=MibTableColumn
h3cDot11RoamTrackACIPType=_H3cDot11RoamTrackACIPType_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3,1,5),_H3cDot11RoamTrackACIPType_Type())
h3cDot11RoamTrackACIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamTrackACIPType.setStatus(_A)
_H3cDot11RoamTrackACIPAddr_Type=InetAddress
_H3cDot11RoamTrackACIPAddr_Object=MibTableColumn
h3cDot11RoamTrackACIPAddr=_H3cDot11RoamTrackACIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,2,3,1,6),_H3cDot11RoamTrackACIPAddr_Type())
h3cDot11RoamTrackACIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RoamTrackACIPAddr.setStatus(_A)
_H3cDot11RoamStatisGroup_ObjectIdentity=ObjectIdentity
h3cDot11RoamStatisGroup=_H3cDot11RoamStatisGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,10,3))
_H3cDot11IntraACRoamingSuccCnt_Type=Integer32
_H3cDot11IntraACRoamingSuccCnt_Object=MibScalar
h3cDot11IntraACRoamingSuccCnt=_H3cDot11IntraACRoamingSuccCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,3,1),_H3cDot11IntraACRoamingSuccCnt_Type())
h3cDot11IntraACRoamingSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11IntraACRoamingSuccCnt.setStatus(_A)
_H3cDot11InterACRoamingSuccCnt_Type=Integer32
_H3cDot11InterACRoamingSuccCnt_Object=MibScalar
h3cDot11InterACRoamingSuccCnt=_H3cDot11InterACRoamingSuccCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,3,2),_H3cDot11InterACRoamingSuccCnt_Type())
h3cDot11InterACRoamingSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11InterACRoamingSuccCnt.setStatus(_A)
_H3cDot11InterACRoamOutSuccCnt_Type=Integer32
_H3cDot11InterACRoamOutSuccCnt_Object=MibScalar
h3cDot11InterACRoamOutSuccCnt=_H3cDot11InterACRoamOutSuccCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,3,3),_H3cDot11InterACRoamOutSuccCnt_Type())
h3cDot11InterACRoamOutSuccCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11InterACRoamOutSuccCnt.setStatus(_A)
_H3cDot11RoamStatis2Group_ObjectIdentity=ObjectIdentity
h3cDot11RoamStatis2Group=_H3cDot11RoamStatis2Group_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,10,4))
_H3cDot11IntraACRoamingSuccCnt2_Type=Counter32
_H3cDot11IntraACRoamingSuccCnt2_Object=MibScalar
h3cDot11IntraACRoamingSuccCnt2=_H3cDot11IntraACRoamingSuccCnt2_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,4,1),_H3cDot11IntraACRoamingSuccCnt2_Type())
h3cDot11IntraACRoamingSuccCnt2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11IntraACRoamingSuccCnt2.setStatus(_A)
_H3cDot11InterACRoamingSuccCnt2_Type=Counter32
_H3cDot11InterACRoamingSuccCnt2_Object=MibScalar
h3cDot11InterACRoamingSuccCnt2=_H3cDot11InterACRoamingSuccCnt2_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,4,2),_H3cDot11InterACRoamingSuccCnt2_Type())
h3cDot11InterACRoamingSuccCnt2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11InterACRoamingSuccCnt2.setStatus(_A)
_H3cDot11InterACRoamOutSuccCnt2_Type=Counter32
_H3cDot11InterACRoamOutSuccCnt2_Object=MibScalar
h3cDot11InterACRoamOutSuccCnt2=_H3cDot11InterACRoamOutSuccCnt2_Object((1,3,6,1,4,1,43,45,1,10,2,75,10,4,3),_H3cDot11InterACRoamOutSuccCnt2_Type())
h3cDot11InterACRoamOutSuccCnt2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11InterACRoamOutSuccCnt2.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_K:H3cDot11RoamMobileTunnelType,_L:H3cDot11RoamAuthMode,'H3cDot11RoamIACTPStatus':H3cDot11RoamIACTPStatus,'h3cDot11ROAM':h3cDot11ROAM,'h3cDot11RoamCfgGroup':h3cDot11RoamCfgGroup,'h3cDot11MobGrpTable':h3cDot11MobGrpTable,'h3cDot11MobGrpEntry':h3cDot11MobGrpEntry,_G:h3cDot11MobGrpName,'h3cdot11MobGrpTunnelType':h3cdot11MobGrpTunnelType,'h3cDot11MobGrpSrcIPAddr':h3cDot11MobGrpSrcIPAddr,'h3cDot11MobGrpAuthMode':h3cDot11MobGrpAuthMode,'h3cDot11MobGrpAuthKey':h3cDot11MobGrpAuthKey,'h3cDot11MobGrpEnable':h3cDot11MobGrpEnable,'h3cDot11MobGrpRowStatus':h3cDot11MobGrpRowStatus,'h3cDot11MobGrpMemberTable':h3cDot11MobGrpMemberTable,'h3cDot11MobGrpMemberEntry':h3cDot11MobGrpMemberEntry,_M:h3cDot11MobGrpMemberIpAddr,'h3cDot11MobGrpMemberStatus':h3cDot11MobGrpMemberStatus,'h3cDot11MobGrpMemberIf':h3cDot11MobGrpMemberIf,'h3cDot11MobGrpMemberUpTime':h3cDot11MobGrpMemberUpTime,'h3cDot11MobGrpMemberRowStatus':h3cDot11MobGrpMemberRowStatus,'h3cDot11RoamStatusGroup':h3cDot11RoamStatusGroup,'h3cDot11RoamInInfoTable':h3cDot11RoamInInfoTable,'h3cDot11RoamInInfoEntry':h3cDot11RoamInInfoEntry,_I:h3cDot11RoamClientMAC,'h3cDot11RoamInClientBSSID':h3cDot11RoamInClientBSSID,'h3cDot11RoamInClientVlanID':h3cDot11RoamInClientVlanID,'h3cDot11RoamInHomeACIPType':h3cDot11RoamInHomeACIPType,'h3cDot11RoamInHomeACIPAddr':h3cDot11RoamInHomeACIPAddr,'h3cDot11RoamOutInfoTable':h3cDot11RoamOutInfoTable,'h3cDot11RoamOutInfoEntry':h3cDot11RoamOutInfoEntry,'h3cDot11RoamOutClientBSSID':h3cDot11RoamOutClientBSSID,'h3cDot11RoamOutClientVlanID':h3cDot11RoamOutClientVlanID,'h3cDot11RoamOutForeignACIPType':h3cDot11RoamOutForeignACIPType,'h3cDot11RoamOutForeignACIPAddr':h3cDot11RoamOutForeignACIPAddr,'h3cDot11RoamOutClientUpTime':h3cDot11RoamOutClientUpTime,'h3cDot11RoamTrackTable':h3cDot11RoamTrackTable,'h3cDot11RoamTrackEntry':h3cDot11RoamTrackEntry,_N:h3cDot11RoamTrackIndex,'h3cDot11RoamTrackClientMAC':h3cDot11RoamTrackClientMAC,'h3cDot11RoamTrackBSSID':h3cDot11RoamTrackBSSID,'h3cDot11RoamTrackUpTime':h3cDot11RoamTrackUpTime,'h3cDot11RoamTrackACIPType':h3cDot11RoamTrackACIPType,'h3cDot11RoamTrackACIPAddr':h3cDot11RoamTrackACIPAddr,'h3cDot11RoamStatisGroup':h3cDot11RoamStatisGroup,'h3cDot11IntraACRoamingSuccCnt':h3cDot11IntraACRoamingSuccCnt,'h3cDot11InterACRoamingSuccCnt':h3cDot11InterACRoamingSuccCnt,'h3cDot11InterACRoamOutSuccCnt':h3cDot11InterACRoamOutSuccCnt,'h3cDot11RoamStatis2Group':h3cDot11RoamStatis2Group,'h3cDot11IntraACRoamingSuccCnt2':h3cDot11IntraACRoamingSuccCnt2,'h3cDot11InterACRoamingSuccCnt2':h3cDot11InterACRoamingSuccCnt2,'h3cDot11InterACRoamOutSuccCnt2':h3cDot11InterACRoamOutSuccCnt2})