_AH='crmRadiusServerNotifCntlGroup'
_AG='crmRadiusServerNotifGroup'
_AF='crmConfigurationGroupSup1'
_AE='crRadiusServerRetransHiNotif'
_AD='crRadiusServerRetransNormNotif'
_AC='crRadiusServerRTTHiNotif'
_AB='crRadiusServerRTTNormNotif'
_AA='crRadiusServerRetransHiNotifEnable'
_A9='crRadiusServerRetransNormNotifEnable'
_A8='crRadiusServerRTTHiNotifEnable'
_A7='crRadiusServerRTTNormNotifEnable'
_A6='crRadiusKeepAliveUserName'
_A5='crRadiusFramedMtu'
_A4='crRadiusPortAutoInitialize'
_A3='crRadiusKeepAliveServerStatus'
_A2='crRadiusKeepAliveInterval'
_A1='crRadiusKeepAliveEnabled'
_A0='crVlanGroupRowStatus'
_z='crVlanGroupVlansHigh'
_y='crVlanGroupVlansLow'
_x='crRadiusVlanAssignmentEnabled'
_w='crRadiusFramedIpAddrIncluded'
_v='crRadiusServerRowStatus'
_u='crRadiusServerMode'
_t='crRadiusServerType'
_s='crRadiusServerKey'
_r='crRadiusServerAcctPort'
_q='crRadiusServerAddrType'
_p='crRadiusServerTableMaxEntries'
_o='crRadiusAccountingMethod'
_n='crRadiusAccountingLogMaxSize'
_m='crRadiusDeadtime'
_l='crRadiusRetransmits'
_k='crRadiusTimeout'
_j='crRadiusAuthKey'
_i='crRadiusLoginAuthentication'
_h='crVlanGroupName'
_g='CiscoRadiusAuthKey'
_f='not-accessible'
_e='read-only'
_d='seconds'
_c='InetAddressType'
_b='TimeIntervalSec'
_a='TimeIntervalMin'
_Z='crmRadiusKeepAliveUserGroup'
_Y='crmVlanConfigGroup'
_X='deprecated'
_W='crRadiusServerRetransThldHi'
_V='crRadiusServerRetransThldNorm'
_U='crRadiusServerRTTThldHi'
_T='crRadiusServerRTTThldNorm'
_S='crRadiusServerIndex'
_R='Bits'
_Q='CiscoPort'
_P='OctetString'
_O='crmAttributesGroup2'
_N='crmAutoInitializeConfigGroup'
_M='crmKeepAliveGroup'
_L='crmAttributesGroup'
_K='percent'
_J='Integer32'
_I='crmConfigurationGroup'
_H='TruthValue'
_G='Unsigned32'
_F='crRadiusServerAuthPort'
_E='crRadiusServerAddr'
_D='read-create'
_C='read-write'
_B='current'
_A='CISCO-RADIUS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,TimeIntervalMin,TimeIntervalSec=mibBuilder.importSymbols('CISCO-TC',_Q,_a,_b)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_c)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_R,'Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
ciscoRadiusMIB=ModuleIdentity((1,3,6,1,4,1,9,9,288))
if mibBuilder.loadTexts:ciscoRadiusMIB.setRevisions(('2009-02-06 00:00','2007-07-22 00:00','2007-01-03 00:00','2004-03-03 00:00','2002-11-09 00:00','2002-10-08 00:00'))
class CiscoRadiusAuthKey(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65))
class CiscoRadiusRoundTripTimePercent(TextualConvention,Unsigned32):status=_B;displayHint='d-2';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
class CiscoRadiusRetransPercent(TextualConvention,Unsigned32):status=_B;displayHint='d-2';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CiscoRadiusMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRadiusMIBObjects=_CiscoRadiusMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,288,1))
_CrRadiusGenericConfig_ObjectIdentity=ObjectIdentity
crRadiusGenericConfig=_CrRadiusGenericConfig_ObjectIdentity((1,3,6,1,4,1,9,9,288,1,1))
class _CrRadiusLoginAuthentication_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('telnet',0),('console',1),('http',2)))
_CrRadiusLoginAuthentication_Type.__name__=_R
_CrRadiusLoginAuthentication_Object=MibScalar
crRadiusLoginAuthentication=_CrRadiusLoginAuthentication_Object((1,3,6,1,4,1,9,9,288,1,1,1),_CrRadiusLoginAuthentication_Type())
crRadiusLoginAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusLoginAuthentication.setStatus(_B)
class _CrRadiusDeadtime_Type(TimeIntervalMin):defaultValue=0;subtypeSpec=TimeIntervalMin.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CrRadiusDeadtime_Type.__name__=_a
_CrRadiusDeadtime_Object=MibScalar
crRadiusDeadtime=_CrRadiusDeadtime_Object((1,3,6,1,4,1,9,9,288,1,1,2),_CrRadiusDeadtime_Type())
crRadiusDeadtime.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusDeadtime.setStatus(_B)
if mibBuilder.loadTexts:crRadiusDeadtime.setUnits('minutes')
_CrRadiusAuthKey_Type=CiscoRadiusAuthKey
_CrRadiusAuthKey_Object=MibScalar
crRadiusAuthKey=_CrRadiusAuthKey_Object((1,3,6,1,4,1,9,9,288,1,1,3),_CrRadiusAuthKey_Type())
crRadiusAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusAuthKey.setStatus(_B)
class _CrRadiusTimeout_Type(TimeIntervalSec):defaultValue=1;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CrRadiusTimeout_Type.__name__=_b
_CrRadiusTimeout_Object=MibScalar
crRadiusTimeout=_CrRadiusTimeout_Object((1,3,6,1,4,1,9,9,288,1,1,4),_CrRadiusTimeout_Type())
crRadiusTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusTimeout.setStatus(_B)
if mibBuilder.loadTexts:crRadiusTimeout.setUnits(_d)
class _CrRadiusRetransmits_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CrRadiusRetransmits_Type.__name__=_G
_CrRadiusRetransmits_Object=MibScalar
crRadiusRetransmits=_CrRadiusRetransmits_Object((1,3,6,1,4,1,9,9,288,1,1,5),_CrRadiusRetransmits_Type())
crRadiusRetransmits.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusRetransmits.setStatus(_B)
if mibBuilder.loadTexts:crRadiusRetransmits.setUnits('retransmits')
class _CrRadiusAccountingLogMaxSize_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_CrRadiusAccountingLogMaxSize_Type.__name__=_G
_CrRadiusAccountingLogMaxSize_Object=MibScalar
crRadiusAccountingLogMaxSize=_CrRadiusAccountingLogMaxSize_Object((1,3,6,1,4,1,9,9,288,1,1,6),_CrRadiusAccountingLogMaxSize_Type())
crRadiusAccountingLogMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusAccountingLogMaxSize.setStatus(_B)
if mibBuilder.loadTexts:crRadiusAccountingLogMaxSize.setUnits('bytes')
class _CrRadiusAccountingMethod_Type(Bits):namedValues=NamedValues(*(('radius',0),('local',1)))
_CrRadiusAccountingMethod_Type.__name__=_R
_CrRadiusAccountingMethod_Object=MibScalar
crRadiusAccountingMethod=_CrRadiusAccountingMethod_Object((1,3,6,1,4,1,9,9,288,1,1,7),_CrRadiusAccountingMethod_Type())
crRadiusAccountingMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusAccountingMethod.setStatus(_B)
_CrRadiusServerConfig_ObjectIdentity=ObjectIdentity
crRadiusServerConfig=_CrRadiusServerConfig_ObjectIdentity((1,3,6,1,4,1,9,9,288,1,2))
class _CrRadiusServerTableMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_CrRadiusServerTableMaxEntries_Type.__name__=_G
_CrRadiusServerTableMaxEntries_Object=MibScalar
crRadiusServerTableMaxEntries=_CrRadiusServerTableMaxEntries_Object((1,3,6,1,4,1,9,9,288,1,2,1),_CrRadiusServerTableMaxEntries_Type())
crRadiusServerTableMaxEntries.setMaxAccess(_e)
if mibBuilder.loadTexts:crRadiusServerTableMaxEntries.setStatus(_B)
_CrRadiusServerTable_Object=MibTable
crRadiusServerTable=_CrRadiusServerTable_Object((1,3,6,1,4,1,9,9,288,1,2,2))
if mibBuilder.loadTexts:crRadiusServerTable.setStatus(_B)
_CrRadiusServerEntry_Object=MibTableRow
crRadiusServerEntry=_CrRadiusServerEntry_Object((1,3,6,1,4,1,9,9,288,1,2,2,1))
crRadiusServerEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:crRadiusServerEntry.setStatus(_B)
class _CrRadiusServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CrRadiusServerIndex_Type.__name__=_G
_CrRadiusServerIndex_Object=MibTableColumn
crRadiusServerIndex=_CrRadiusServerIndex_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,1),_CrRadiusServerIndex_Type())
crRadiusServerIndex.setMaxAccess(_f)
if mibBuilder.loadTexts:crRadiusServerIndex.setStatus(_B)
class _CrRadiusServerAddrType_Type(InetAddressType):defaultValue=1
_CrRadiusServerAddrType_Type.__name__=_c
_CrRadiusServerAddrType_Object=MibTableColumn
crRadiusServerAddrType=_CrRadiusServerAddrType_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,2),_CrRadiusServerAddrType_Type())
crRadiusServerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerAddrType.setStatus(_B)
_CrRadiusServerAddr_Type=InetAddress
_CrRadiusServerAddr_Object=MibTableColumn
crRadiusServerAddr=_CrRadiusServerAddr_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,3),_CrRadiusServerAddr_Type())
crRadiusServerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerAddr.setStatus(_B)
class _CrRadiusServerAuthPort_Type(CiscoPort):defaultValue=1812
_CrRadiusServerAuthPort_Type.__name__=_Q
_CrRadiusServerAuthPort_Object=MibTableColumn
crRadiusServerAuthPort=_CrRadiusServerAuthPort_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,4),_CrRadiusServerAuthPort_Type())
crRadiusServerAuthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerAuthPort.setStatus(_B)
class _CrRadiusServerAcctPort_Type(CiscoPort):defaultValue=1813
_CrRadiusServerAcctPort_Type.__name__=_Q
_CrRadiusServerAcctPort_Object=MibTableColumn
crRadiusServerAcctPort=_CrRadiusServerAcctPort_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,5),_CrRadiusServerAcctPort_Type())
crRadiusServerAcctPort.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerAcctPort.setStatus(_B)
class _CrRadiusServerKey_Type(CiscoRadiusAuthKey):defaultHexValue='00000000'
_CrRadiusServerKey_Type.__name__=_g
_CrRadiusServerKey_Object=MibTableColumn
crRadiusServerKey=_CrRadiusServerKey_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,6),_CrRadiusServerKey_Type())
crRadiusServerKey.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerKey.setStatus(_B)
class _CrRadiusServerType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('primary',2)))
_CrRadiusServerType_Type.__name__=_J
_CrRadiusServerType_Object=MibTableColumn
crRadiusServerType=_CrRadiusServerType_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,7),_CrRadiusServerType_Type())
crRadiusServerType.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerType.setStatus(_B)
class _CrRadiusServerMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('authAndAcct',2),('authOnly',3),('acctOnly',4)))
_CrRadiusServerMode_Type.__name__=_J
_CrRadiusServerMode_Object=MibTableColumn
crRadiusServerMode=_CrRadiusServerMode_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,8),_CrRadiusServerMode_Type())
crRadiusServerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerMode.setStatus(_B)
_CrRadiusServerRowStatus_Type=RowStatus
_CrRadiusServerRowStatus_Object=MibTableColumn
crRadiusServerRowStatus=_CrRadiusServerRowStatus_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,9),_CrRadiusServerRowStatus_Type())
crRadiusServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerRowStatus.setStatus(_B)
_CrRadiusServerRTTThldNorm_Type=CiscoRadiusRoundTripTimePercent
_CrRadiusServerRTTThldNorm_Object=MibTableColumn
crRadiusServerRTTThldNorm=_CrRadiusServerRTTThldNorm_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,10),_CrRadiusServerRTTThldNorm_Type())
crRadiusServerRTTThldNorm.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerRTTThldNorm.setStatus(_B)
if mibBuilder.loadTexts:crRadiusServerRTTThldNorm.setUnits(_K)
_CrRadiusServerRTTThldHi_Type=CiscoRadiusRoundTripTimePercent
_CrRadiusServerRTTThldHi_Object=MibTableColumn
crRadiusServerRTTThldHi=_CrRadiusServerRTTThldHi_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,11),_CrRadiusServerRTTThldHi_Type())
crRadiusServerRTTThldHi.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerRTTThldHi.setStatus(_B)
if mibBuilder.loadTexts:crRadiusServerRTTThldHi.setUnits(_K)
_CrRadiusServerRetransThldNorm_Type=CiscoRadiusRetransPercent
_CrRadiusServerRetransThldNorm_Object=MibTableColumn
crRadiusServerRetransThldNorm=_CrRadiusServerRetransThldNorm_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,12),_CrRadiusServerRetransThldNorm_Type())
crRadiusServerRetransThldNorm.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerRetransThldNorm.setStatus(_B)
if mibBuilder.loadTexts:crRadiusServerRetransThldNorm.setUnits(_K)
_CrRadiusServerRetransThldHi_Type=CiscoRadiusRetransPercent
_CrRadiusServerRetransThldHi_Object=MibTableColumn
crRadiusServerRetransThldHi=_CrRadiusServerRetransThldHi_Object((1,3,6,1,4,1,9,9,288,1,2,2,1,13),_CrRadiusServerRetransThldHi_Type())
crRadiusServerRetransThldHi.setMaxAccess(_D)
if mibBuilder.loadTexts:crRadiusServerRetransThldHi.setStatus(_B)
if mibBuilder.loadTexts:crRadiusServerRetransThldHi.setUnits(_K)
_CrRadiusAttributesConfig_ObjectIdentity=ObjectIdentity
crRadiusAttributesConfig=_CrRadiusAttributesConfig_ObjectIdentity((1,3,6,1,4,1,9,9,288,1,3))
_CrRadiusFramedIpAddrIncluded_Type=TruthValue
_CrRadiusFramedIpAddrIncluded_Object=MibScalar
crRadiusFramedIpAddrIncluded=_CrRadiusFramedIpAddrIncluded_Object((1,3,6,1,4,1,9,9,288,1,3,1),_CrRadiusFramedIpAddrIncluded_Type())
crRadiusFramedIpAddrIncluded.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusFramedIpAddrIncluded.setStatus(_B)
_CrRadiusFramedMtu_Type=Unsigned32
_CrRadiusFramedMtu_Object=MibScalar
crRadiusFramedMtu=_CrRadiusFramedMtu_Object((1,3,6,1,4,1,9,9,288,1,3,2),_CrRadiusFramedMtu_Type())
crRadiusFramedMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusFramedMtu.setStatus(_B)
_CrRadiusVlanConfigGroup_ObjectIdentity=ObjectIdentity
crRadiusVlanConfigGroup=_CrRadiusVlanConfigGroup_ObjectIdentity((1,3,6,1,4,1,9,9,288,1,4))
_CrRadiusVlanAssignmentEnabled_Type=TruthValue
_CrRadiusVlanAssignmentEnabled_Object=MibScalar
crRadiusVlanAssignmentEnabled=_CrRadiusVlanAssignmentEnabled_Object((1,3,6,1,4,1,9,9,288,1,4,1),_CrRadiusVlanAssignmentEnabled_Type())
crRadiusVlanAssignmentEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusVlanAssignmentEnabled.setStatus(_B)
_CrVlanGroupTable_Object=MibTable
crVlanGroupTable=_CrVlanGroupTable_Object((1,3,6,1,4,1,9,9,288,1,4,2))
if mibBuilder.loadTexts:crVlanGroupTable.setStatus(_B)
_CrVlanGroupEntry_Object=MibTableRow
crVlanGroupEntry=_CrVlanGroupEntry_Object((1,3,6,1,4,1,9,9,288,1,4,2,1))
crVlanGroupEntry.setIndexNames((0,_A,_h))
if mibBuilder.loadTexts:crVlanGroupEntry.setStatus(_B)
_CrVlanGroupName_Type=SnmpAdminString
_CrVlanGroupName_Object=MibTableColumn
crVlanGroupName=_CrVlanGroupName_Object((1,3,6,1,4,1,9,9,288,1,4,2,1,1),_CrVlanGroupName_Type())
crVlanGroupName.setMaxAccess(_f)
if mibBuilder.loadTexts:crVlanGroupName.setStatus(_B)
class _CrVlanGroupVlansLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CrVlanGroupVlansLow_Type.__name__=_P
_CrVlanGroupVlansLow_Object=MibTableColumn
crVlanGroupVlansLow=_CrVlanGroupVlansLow_Object((1,3,6,1,4,1,9,9,288,1,4,2,1,2),_CrVlanGroupVlansLow_Type())
crVlanGroupVlansLow.setMaxAccess(_D)
if mibBuilder.loadTexts:crVlanGroupVlansLow.setStatus(_B)
class _CrVlanGroupVlansHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CrVlanGroupVlansHigh_Type.__name__=_P
_CrVlanGroupVlansHigh_Object=MibTableColumn
crVlanGroupVlansHigh=_CrVlanGroupVlansHigh_Object((1,3,6,1,4,1,9,9,288,1,4,2,1,3),_CrVlanGroupVlansHigh_Type())
crVlanGroupVlansHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:crVlanGroupVlansHigh.setStatus(_B)
_CrVlanGroupRowStatus_Type=RowStatus
_CrVlanGroupRowStatus_Object=MibTableColumn
crVlanGroupRowStatus=_CrVlanGroupRowStatus_Object((1,3,6,1,4,1,9,9,288,1,4,2,1,4),_CrVlanGroupRowStatus_Type())
crVlanGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:crVlanGroupRowStatus.setStatus(_B)
_CrRadiusKeepAliveConfig_ObjectIdentity=ObjectIdentity
crRadiusKeepAliveConfig=_CrRadiusKeepAliveConfig_ObjectIdentity((1,3,6,1,4,1,9,9,288,1,5))
_CrRadiusKeepAliveEnabled_Type=TruthValue
_CrRadiusKeepAliveEnabled_Object=MibScalar
crRadiusKeepAliveEnabled=_CrRadiusKeepAliveEnabled_Object((1,3,6,1,4,1,9,9,288,1,5,1),_CrRadiusKeepAliveEnabled_Type())
crRadiusKeepAliveEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusKeepAliveEnabled.setStatus(_B)
_CrRadiusKeepAliveInterval_Type=Unsigned32
_CrRadiusKeepAliveInterval_Object=MibScalar
crRadiusKeepAliveInterval=_CrRadiusKeepAliveInterval_Object((1,3,6,1,4,1,9,9,288,1,5,2),_CrRadiusKeepAliveInterval_Type())
crRadiusKeepAliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusKeepAliveInterval.setStatus(_B)
if mibBuilder.loadTexts:crRadiusKeepAliveInterval.setUnits(_d)
_CrRadiusKeepAliveServerTable_Object=MibTable
crRadiusKeepAliveServerTable=_CrRadiusKeepAliveServerTable_Object((1,3,6,1,4,1,9,9,288,1,5,3))
if mibBuilder.loadTexts:crRadiusKeepAliveServerTable.setStatus(_B)
_CrRadiusKeepAliveServerEntry_Object=MibTableRow
crRadiusKeepAliveServerEntry=_CrRadiusKeepAliveServerEntry_Object((1,3,6,1,4,1,9,9,288,1,5,3,1))
crRadiusKeepAliveServerEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:crRadiusKeepAliveServerEntry.setStatus(_B)
class _CrRadiusKeepAliveServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('init',2),('active',3),('checkup',4),('dead',5)))
_CrRadiusKeepAliveServerStatus_Type.__name__=_J
_CrRadiusKeepAliveServerStatus_Object=MibTableColumn
crRadiusKeepAliveServerStatus=_CrRadiusKeepAliveServerStatus_Object((1,3,6,1,4,1,9,9,288,1,5,3,1,1),_CrRadiusKeepAliveServerStatus_Type())
crRadiusKeepAliveServerStatus.setMaxAccess(_e)
if mibBuilder.loadTexts:crRadiusKeepAliveServerStatus.setStatus(_B)
_CrRadiusPortAutoInitialize_Type=TruthValue
_CrRadiusPortAutoInitialize_Object=MibScalar
crRadiusPortAutoInitialize=_CrRadiusPortAutoInitialize_Object((1,3,6,1,4,1,9,9,288,1,5,4),_CrRadiusPortAutoInitialize_Type())
crRadiusPortAutoInitialize.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusPortAutoInitialize.setStatus(_B)
_CrRadiusKeepAliveUserName_Type=SnmpAdminString
_CrRadiusKeepAliveUserName_Object=MibScalar
crRadiusKeepAliveUserName=_CrRadiusKeepAliveUserName_Object((1,3,6,1,4,1,9,9,288,1,5,5),_CrRadiusKeepAliveUserName_Type())
crRadiusKeepAliveUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusKeepAliveUserName.setStatus(_B)
_CrRadiusServerNotifCntl_ObjectIdentity=ObjectIdentity
crRadiusServerNotifCntl=_CrRadiusServerNotifCntl_ObjectIdentity((1,3,6,1,4,1,9,9,288,1,6))
class _CrRadiusServerRTTNormNotifEnable_Type(TruthValue):defaultValue=2
_CrRadiusServerRTTNormNotifEnable_Type.__name__=_H
_CrRadiusServerRTTNormNotifEnable_Object=MibScalar
crRadiusServerRTTNormNotifEnable=_CrRadiusServerRTTNormNotifEnable_Object((1,3,6,1,4,1,9,9,288,1,6,1),_CrRadiusServerRTTNormNotifEnable_Type())
crRadiusServerRTTNormNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusServerRTTNormNotifEnable.setStatus(_B)
class _CrRadiusServerRTTHiNotifEnable_Type(TruthValue):defaultValue=2
_CrRadiusServerRTTHiNotifEnable_Type.__name__=_H
_CrRadiusServerRTTHiNotifEnable_Object=MibScalar
crRadiusServerRTTHiNotifEnable=_CrRadiusServerRTTHiNotifEnable_Object((1,3,6,1,4,1,9,9,288,1,6,2),_CrRadiusServerRTTHiNotifEnable_Type())
crRadiusServerRTTHiNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusServerRTTHiNotifEnable.setStatus(_B)
class _CrRadiusServerRetransNormNotifEnable_Type(TruthValue):defaultValue=2
_CrRadiusServerRetransNormNotifEnable_Type.__name__=_H
_CrRadiusServerRetransNormNotifEnable_Object=MibScalar
crRadiusServerRetransNormNotifEnable=_CrRadiusServerRetransNormNotifEnable_Object((1,3,6,1,4,1,9,9,288,1,6,3),_CrRadiusServerRetransNormNotifEnable_Type())
crRadiusServerRetransNormNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusServerRetransNormNotifEnable.setStatus(_B)
class _CrRadiusServerRetransHiNotifEnable_Type(TruthValue):defaultValue=2
_CrRadiusServerRetransHiNotifEnable_Type.__name__=_H
_CrRadiusServerRetransHiNotifEnable_Object=MibScalar
crRadiusServerRetransHiNotifEnable=_CrRadiusServerRetransHiNotifEnable_Object((1,3,6,1,4,1,9,9,288,1,6,4),_CrRadiusServerRetransHiNotifEnable_Type())
crRadiusServerRetransHiNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:crRadiusServerRetransHiNotifEnable.setStatus(_B)
_CiscoRadiusMIBConformance_ObjectIdentity=ObjectIdentity
ciscoRadiusMIBConformance=_CiscoRadiusMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,288,2))
_CiscoRadiusMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoRadiusMIBCompliances=_CiscoRadiusMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,288,2,1))
_CiscoRadiusMIBGroups_ObjectIdentity=ObjectIdentity
ciscoRadiusMIBGroups=_CiscoRadiusMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,288,2,2))
_CiscoRadiusMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoRadiusMIBNotifications=_CiscoRadiusMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,288,3))
crmConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,1))
crmConfigurationGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_E),(_A,_F),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:crmConfigurationGroup.setStatus(_B)
crmAttributesGroup=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,2))
crmAttributesGroup.setObjects((_A,_w))
if mibBuilder.loadTexts:crmAttributesGroup.setStatus(_B)
crmVlanConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,3))
crmVlanConfigGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:crmVlanConfigGroup.setStatus(_B)
crmKeepAliveGroup=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,4))
crmKeepAliveGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:crmKeepAliveGroup.setStatus(_B)
crmAutoInitializeConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,5))
crmAutoInitializeConfigGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:crmAutoInitializeConfigGroup.setStatus(_B)
crmAttributesGroup2=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,6))
crmAttributesGroup2.setObjects((_A,_A5))
if mibBuilder.loadTexts:crmAttributesGroup2.setStatus(_B)
crmRadiusKeepAliveUserGroup=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,7))
crmRadiusKeepAliveUserGroup.setObjects((_A,_A6))
if mibBuilder.loadTexts:crmRadiusKeepAliveUserGroup.setStatus(_B)
crmConfigurationGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,9))
crmConfigurationGroupSup1.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:crmConfigurationGroupSup1.setStatus(_B)
crmRadiusServerNotifCntlGroup=ObjectGroup((1,3,6,1,4,1,9,9,288,2,2,10))
crmRadiusServerNotifCntlGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:crmRadiusServerNotifCntlGroup.setStatus(_B)
crRadiusServerRTTNormNotif=NotificationType((1,3,6,1,4,1,9,9,288,3,1))
crRadiusServerRTTNormNotif.setObjects(*((_A,_T),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:crRadiusServerRTTNormNotif.setStatus(_B)
crRadiusServerRTTHiNotif=NotificationType((1,3,6,1,4,1,9,9,288,3,2))
crRadiusServerRTTHiNotif.setObjects(*((_A,_U),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:crRadiusServerRTTHiNotif.setStatus(_B)
crRadiusServerRetransNormNotif=NotificationType((1,3,6,1,4,1,9,9,288,3,3))
crRadiusServerRetransNormNotif.setObjects(*((_A,_V),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:crRadiusServerRetransNormNotif.setStatus(_B)
crRadiusServerRetransHiNotif=NotificationType((1,3,6,1,4,1,9,9,288,3,4))
crRadiusServerRetransHiNotif.setObjects(*((_A,_W),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:crRadiusServerRetransHiNotif.setStatus(_B)
crmRadiusServerNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,288,2,2,8))
crmRadiusServerNotifGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:crmRadiusServerNotifGroup.setStatus(_B)
ciscoRadiusMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,288,2,1,1))
ciscoRadiusMIBCompliance.setObjects((_A,_I))
if mibBuilder.loadTexts:ciscoRadiusMIBCompliance.setStatus(_X)
ciscoRadiusMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,288,2,1,2))
ciscoRadiusMIBCompliance2.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoRadiusMIBCompliance2.setStatus(_X)
ciscoRadiusMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,288,2,1,3))
ciscoRadiusMIBCompliance3.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoRadiusMIBCompliance3.setStatus(_X)
ciscoRadiusMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,288,2,1,4))
ciscoRadiusMIBCompliance4.setObjects(*((_A,_I),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoRadiusMIBCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_g:CiscoRadiusAuthKey,'CiscoRadiusRoundTripTimePercent':CiscoRadiusRoundTripTimePercent,'CiscoRadiusRetransPercent':CiscoRadiusRetransPercent,'ciscoRadiusMIB':ciscoRadiusMIB,'ciscoRadiusMIBObjects':ciscoRadiusMIBObjects,'crRadiusGenericConfig':crRadiusGenericConfig,_i:crRadiusLoginAuthentication,_m:crRadiusDeadtime,_j:crRadiusAuthKey,_k:crRadiusTimeout,_l:crRadiusRetransmits,_n:crRadiusAccountingLogMaxSize,_o:crRadiusAccountingMethod,'crRadiusServerConfig':crRadiusServerConfig,_p:crRadiusServerTableMaxEntries,'crRadiusServerTable':crRadiusServerTable,'crRadiusServerEntry':crRadiusServerEntry,_S:crRadiusServerIndex,_q:crRadiusServerAddrType,_E:crRadiusServerAddr,_F:crRadiusServerAuthPort,_r:crRadiusServerAcctPort,_s:crRadiusServerKey,_t:crRadiusServerType,_u:crRadiusServerMode,_v:crRadiusServerRowStatus,_T:crRadiusServerRTTThldNorm,_U:crRadiusServerRTTThldHi,_V:crRadiusServerRetransThldNorm,_W:crRadiusServerRetransThldHi,'crRadiusAttributesConfig':crRadiusAttributesConfig,_w:crRadiusFramedIpAddrIncluded,_A5:crRadiusFramedMtu,'crRadiusVlanConfigGroup':crRadiusVlanConfigGroup,_x:crRadiusVlanAssignmentEnabled,'crVlanGroupTable':crVlanGroupTable,'crVlanGroupEntry':crVlanGroupEntry,_h:crVlanGroupName,_y:crVlanGroupVlansLow,_z:crVlanGroupVlansHigh,_A0:crVlanGroupRowStatus,'crRadiusKeepAliveConfig':crRadiusKeepAliveConfig,_A1:crRadiusKeepAliveEnabled,_A2:crRadiusKeepAliveInterval,'crRadiusKeepAliveServerTable':crRadiusKeepAliveServerTable,'crRadiusKeepAliveServerEntry':crRadiusKeepAliveServerEntry,_A3:crRadiusKeepAliveServerStatus,_A4:crRadiusPortAutoInitialize,_A6:crRadiusKeepAliveUserName,'crRadiusServerNotifCntl':crRadiusServerNotifCntl,_A7:crRadiusServerRTTNormNotifEnable,_A8:crRadiusServerRTTHiNotifEnable,_A9:crRadiusServerRetransNormNotifEnable,_AA:crRadiusServerRetransHiNotifEnable,'ciscoRadiusMIBConformance':ciscoRadiusMIBConformance,'ciscoRadiusMIBCompliances':ciscoRadiusMIBCompliances,'ciscoRadiusMIBCompliance':ciscoRadiusMIBCompliance,'ciscoRadiusMIBCompliance2':ciscoRadiusMIBCompliance2,'ciscoRadiusMIBCompliance3':ciscoRadiusMIBCompliance3,'ciscoRadiusMIBCompliance4':ciscoRadiusMIBCompliance4,'ciscoRadiusMIBGroups':ciscoRadiusMIBGroups,_I:crmConfigurationGroup,_L:crmAttributesGroup,_Y:crmVlanConfigGroup,_M:crmKeepAliveGroup,_N:crmAutoInitializeConfigGroup,_O:crmAttributesGroup2,_Z:crmRadiusKeepAliveUserGroup,_AG:crmRadiusServerNotifGroup,_AF:crmConfigurationGroupSup1,_AH:crmRadiusServerNotifCntlGroup,'ciscoRadiusMIBNotifications':ciscoRadiusMIBNotifications,_AB:crRadiusServerRTTNormNotif,_AC:crRadiusServerRTTHiNotif,_AD:crRadiusServerRetransNormNotif,_AE:crRadiusServerRetransHiNotif})