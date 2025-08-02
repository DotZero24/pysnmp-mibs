_AR='ipIfGroupV2'
_AQ='ipGeneralGroupV6'
_AP='ipGeneralGroupV4'
_AO='ipGeneralGroupV3'
_AN='ipGeneralGroupV2'
_AM='ipIfDstAddr'
_AL='ipGeneralNetconfMode'
_AK='ospfIfPassive'
_AJ='ospfNbrName'
_AI='ipRouteName'
_AH='ospfGeneralDistrMetric'
_AG='ospfGeneralDistrMetricType'
_AF='ospfGeneralDistrMode'
_AE='ospfGeneralRouterId'
_AD='ipGeneralGroupV7'
_AC='ipGeneralGroupV5'
_AB='ipGeneralGroup'
_AA='ipGeneralTftpMode'
_A9='ipGeneralSftpMode'
_A8='ospfNbrOperStatus'
_A7='ospfNbrIfName'
_A6='ospfNbrRtrId'
_A5='ospfNbrIpAddr'
_A4='ospfIfRowStatus'
_A3='ospfIfOperStatus'
_A2='ospfIfAdminStatus'
_A1='ospfIfBackupDesignatedRouterId'
_A0='ospfIfDesignatedRouterId'
_z='ospfIfRtrPriority'
_y='ospfIfMetric'
_x='ospfIfAreaId'
_w='ospfIfName'
_v='ipRouteOperStatus'
_u='ipRouteMetric'
_t='ipRouteProto'
_s='ipRouteRowStatus'
_r='ipRouteIfName'
_q='ipRouteNextHop'
_p='ipRouteMask'
_o='ipRouteDest'
_n='ipIfOperStatus'
_m='ipIfNetMask'
_l='ipIfAddr'
_k='ipIfName'
_j='read-create'
_i='ipGeneralChangeNextMgmtAddr'
_h='ospfNbrIndex'
_g='ospfIfIndex'
_f='ipRouteIndex'
_e='ipIfIndex'
_d='ospfIfGroupV2'
_c='ospfNbrGroup'
_b='ipGeneralOspfNbrTableSize'
_a='ipGeneralOspfIfTableSize'
_Z='ipGeneralRouteTableSize'
_Y='ipGeneralIfTableSize'
_X='down'
_W='ospfNbrGroupV2'
_V='ipRouteGroupV2'
_U='ospfIfGroup'
_T='ipRouteGroup'
_S='ipGeneralFtpMode'
_R='ipGeneralTelnetMode'
_Q='ipGeneralConfigLastChangeTime'
_P='disabled'
_O='enabled'
_N='ipGeneralStoredMgmtNetMask'
_M='ipGeneralNextMgmtNetMask'
_L='ipGeneralStoredMgmtAddress'
_K='ipGeneralNextMgmtAddress'
_J='ipGeneralLastChangeTime'
_I='Unsigned32'
_H='ospfGeneralGroup'
_G='ipIfGroup'
_F='Integer32'
_E='deprecated'
_D='read-write'
_C='read-only'
_B='current'
_A='LUM-IP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIpMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIpMIB','lumModules')
CommandString,MgmtNameString=mibBuilder.importSymbols('LUM-TC','CommandString','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
lumIpMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,15))
if mibBuilder.loadTexts:lumIpMIBModule.setRevisions(('2018-12-20 00:00','2018-05-31 00:00','2017-06-15 00:00','2016-06-14 00:00','2016-01-11 00:00','2013-08-14 00:00','2009-01-23 00:00','2004-12-06 00:00','2004-12-03 00:00','2004-10-01 00:00','2003-05-15 00:00','2002-09-13 00:00','2002-03-12 00:00','2001-11-21 00:00','2001-11-20 00:00','2001-11-16 00:00'))
_LumIpConfs_ObjectIdentity=ObjectIdentity
lumIpConfs=_LumIpConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,14,1))
_LumIpGroups_ObjectIdentity=ObjectIdentity
lumIpGroups=_LumIpGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,14,1,1))
_LumIpCompl_ObjectIdentity=ObjectIdentity
lumIpCompl=_LumIpCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,14,1,2))
_LumIpMIBObjects_ObjectIdentity=ObjectIdentity
lumIpMIBObjects=_LumIpMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,14,2))
_IpGeneral_ObjectIdentity=ObjectIdentity
ipGeneral=_IpGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,14,2,1))
_IpGeneralLastChangeTime_Type=DateAndTime
_IpGeneralLastChangeTime_Object=MibScalar
ipGeneralLastChangeTime=_IpGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,14,2,1,1),_IpGeneralLastChangeTime_Type())
ipGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralLastChangeTime.setStatus(_B)
_IpGeneralNextMgmtAddress_Type=IpAddress
_IpGeneralNextMgmtAddress_Object=MibScalar
ipGeneralNextMgmtAddress=_IpGeneralNextMgmtAddress_Object((1,3,6,1,4,1,8708,2,14,2,1,2),_IpGeneralNextMgmtAddress_Type())
ipGeneralNextMgmtAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipGeneralNextMgmtAddress.setStatus(_B)
_IpGeneralStoredMgmtAddress_Type=IpAddress
_IpGeneralStoredMgmtAddress_Object=MibScalar
ipGeneralStoredMgmtAddress=_IpGeneralStoredMgmtAddress_Object((1,3,6,1,4,1,8708,2,14,2,1,3),_IpGeneralStoredMgmtAddress_Type())
ipGeneralStoredMgmtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralStoredMgmtAddress.setStatus(_B)
_IpGeneralNextMgmtNetMask_Type=IpAddress
_IpGeneralNextMgmtNetMask_Object=MibScalar
ipGeneralNextMgmtNetMask=_IpGeneralNextMgmtNetMask_Object((1,3,6,1,4,1,8708,2,14,2,1,4),_IpGeneralNextMgmtNetMask_Type())
ipGeneralNextMgmtNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipGeneralNextMgmtNetMask.setStatus(_B)
_IpGeneralStoredMgmtNetMask_Type=IpAddress
_IpGeneralStoredMgmtNetMask_Object=MibScalar
ipGeneralStoredMgmtNetMask=_IpGeneralStoredMgmtNetMask_Object((1,3,6,1,4,1,8708,2,14,2,1,5),_IpGeneralStoredMgmtNetMask_Type())
ipGeneralStoredMgmtNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralStoredMgmtNetMask.setStatus(_B)
_IpGeneralConfigLastChangeTime_Type=DateAndTime
_IpGeneralConfigLastChangeTime_Object=MibScalar
ipGeneralConfigLastChangeTime=_IpGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,14,2,1,6),_IpGeneralConfigLastChangeTime_Type())
ipGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralConfigLastChangeTime.setStatus(_B)
class _IpGeneralTelnetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_IpGeneralTelnetMode_Type.__name__=_F
_IpGeneralTelnetMode_Object=MibScalar
ipGeneralTelnetMode=_IpGeneralTelnetMode_Object((1,3,6,1,4,1,8708,2,14,2,1,7),_IpGeneralTelnetMode_Type())
ipGeneralTelnetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralTelnetMode.setStatus(_B)
class _IpGeneralFtpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_IpGeneralFtpMode_Type.__name__=_F
_IpGeneralFtpMode_Object=MibScalar
ipGeneralFtpMode=_IpGeneralFtpMode_Object((1,3,6,1,4,1,8708,2,14,2,1,8),_IpGeneralFtpMode_Type())
ipGeneralFtpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralFtpMode.setStatus(_B)
_IpGeneralIfTableSize_Type=Unsigned32
_IpGeneralIfTableSize_Object=MibScalar
ipGeneralIfTableSize=_IpGeneralIfTableSize_Object((1,3,6,1,4,1,8708,2,14,2,1,9),_IpGeneralIfTableSize_Type())
ipGeneralIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralIfTableSize.setStatus(_B)
_IpGeneralRouteTableSize_Type=Unsigned32
_IpGeneralRouteTableSize_Object=MibScalar
ipGeneralRouteTableSize=_IpGeneralRouteTableSize_Object((1,3,6,1,4,1,8708,2,14,2,1,10),_IpGeneralRouteTableSize_Type())
ipGeneralRouteTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralRouteTableSize.setStatus(_B)
_IpGeneralOspfIfTableSize_Type=Unsigned32
_IpGeneralOspfIfTableSize_Object=MibScalar
ipGeneralOspfIfTableSize=_IpGeneralOspfIfTableSize_Object((1,3,6,1,4,1,8708,2,14,2,1,11),_IpGeneralOspfIfTableSize_Type())
ipGeneralOspfIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralOspfIfTableSize.setStatus(_B)
_IpGeneralOspfNbrTableSize_Type=Unsigned32
_IpGeneralOspfNbrTableSize_Object=MibScalar
ipGeneralOspfNbrTableSize=_IpGeneralOspfNbrTableSize_Object((1,3,6,1,4,1,8708,2,14,2,1,12),_IpGeneralOspfNbrTableSize_Type())
ipGeneralOspfNbrTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralOspfNbrTableSize.setStatus(_B)
_IpGeneralChangeNextMgmtAddr_Type=CommandString
_IpGeneralChangeNextMgmtAddr_Object=MibScalar
ipGeneralChangeNextMgmtAddr=_IpGeneralChangeNextMgmtAddr_Object((1,3,6,1,4,1,8708,2,14,2,1,13),_IpGeneralChangeNextMgmtAddr_Type())
ipGeneralChangeNextMgmtAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ipGeneralChangeNextMgmtAddr.setStatus(_B)
class _IpGeneralSftpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_IpGeneralSftpMode_Type.__name__=_F
_IpGeneralSftpMode_Object=MibScalar
ipGeneralSftpMode=_IpGeneralSftpMode_Object((1,3,6,1,4,1,8708,2,14,2,1,14),_IpGeneralSftpMode_Type())
ipGeneralSftpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralSftpMode.setStatus(_B)
class _IpGeneralTftpMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_IpGeneralTftpMode_Type.__name__=_F
_IpGeneralTftpMode_Object=MibScalar
ipGeneralTftpMode=_IpGeneralTftpMode_Object((1,3,6,1,4,1,8708,2,14,2,1,15),_IpGeneralTftpMode_Type())
ipGeneralTftpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralTftpMode.setStatus(_B)
class _IpGeneralNetconfMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_IpGeneralNetconfMode_Type.__name__=_F
_IpGeneralNetconfMode_Object=MibScalar
ipGeneralNetconfMode=_IpGeneralNetconfMode_Object((1,3,6,1,4,1,8708,2,14,2,1,16),_IpGeneralNetconfMode_Type())
ipGeneralNetconfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGeneralNetconfMode.setStatus(_B)
_IpIfList_ObjectIdentity=ObjectIdentity
ipIfList=_IpIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,14,2,2))
_IpIfTable_Object=MibTable
ipIfTable=_IpIfTable_Object((1,3,6,1,4,1,8708,2,14,2,2,1))
if mibBuilder.loadTexts:ipIfTable.setStatus(_B)
_IpIfEntry_Object=MibTableRow
ipIfEntry=_IpIfEntry_Object((1,3,6,1,4,1,8708,2,14,2,2,1,1))
ipIfEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:ipIfEntry.setStatus(_B)
class _IpIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpIfIndex_Type.__name__=_I
_IpIfIndex_Object=MibTableColumn
ipIfIndex=_IpIfIndex_Object((1,3,6,1,4,1,8708,2,14,2,2,1,1,1),_IpIfIndex_Type())
ipIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipIfIndex.setStatus(_B)
_IpIfName_Type=MgmtNameString
_IpIfName_Object=MibTableColumn
ipIfName=_IpIfName_Object((1,3,6,1,4,1,8708,2,14,2,2,1,1,2),_IpIfName_Type())
ipIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipIfName.setStatus(_B)
_IpIfAddr_Type=IpAddress
_IpIfAddr_Object=MibTableColumn
ipIfAddr=_IpIfAddr_Object((1,3,6,1,4,1,8708,2,14,2,2,1,1,3),_IpIfAddr_Type())
ipIfAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipIfAddr.setStatus(_B)
_IpIfNetMask_Type=IpAddress
_IpIfNetMask_Object=MibTableColumn
ipIfNetMask=_IpIfNetMask_Object((1,3,6,1,4,1,8708,2,14,2,2,1,1,4),_IpIfNetMask_Type())
ipIfNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipIfNetMask.setStatus(_B)
class _IpIfOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('up',2)))
_IpIfOperStatus_Type.__name__=_F
_IpIfOperStatus_Object=MibTableColumn
ipIfOperStatus=_IpIfOperStatus_Object((1,3,6,1,4,1,8708,2,14,2,2,1,1,5),_IpIfOperStatus_Type())
ipIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipIfOperStatus.setStatus(_B)
_IpIfDstAddr_Type=IpAddress
_IpIfDstAddr_Object=MibTableColumn
ipIfDstAddr=_IpIfDstAddr_Object((1,3,6,1,4,1,8708,2,14,2,2,1,1,6),_IpIfDstAddr_Type())
ipIfDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipIfDstAddr.setStatus(_B)
_IpRouteList_ObjectIdentity=ObjectIdentity
ipRouteList=_IpRouteList_ObjectIdentity((1,3,6,1,4,1,8708,2,14,2,3))
_IpRouteTable_Object=MibTable
ipRouteTable=_IpRouteTable_Object((1,3,6,1,4,1,8708,2,14,2,3,1))
if mibBuilder.loadTexts:ipRouteTable.setStatus(_B)
_IpRouteEntry_Object=MibTableRow
ipRouteEntry=_IpRouteEntry_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1))
ipRouteEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:ipRouteEntry.setStatus(_B)
class _IpRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpRouteIndex_Type.__name__=_I
_IpRouteIndex_Object=MibTableColumn
ipRouteIndex=_IpRouteIndex_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,1),_IpRouteIndex_Type())
ipRouteIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteIndex.setStatus(_B)
_IpRouteDest_Type=IpAddress
_IpRouteDest_Object=MibTableColumn
ipRouteDest=_IpRouteDest_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,2),_IpRouteDest_Type())
ipRouteDest.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRouteDest.setStatus(_B)
_IpRouteMask_Type=IpAddress
_IpRouteMask_Object=MibTableColumn
ipRouteMask=_IpRouteMask_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,3),_IpRouteMask_Type())
ipRouteMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRouteMask.setStatus(_B)
_IpRouteNextHop_Type=IpAddress
_IpRouteNextHop_Object=MibTableColumn
ipRouteNextHop=_IpRouteNextHop_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,4),_IpRouteNextHop_Type())
ipRouteNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRouteNextHop.setStatus(_B)
_IpRouteIfName_Type=MgmtNameString
_IpRouteIfName_Object=MibTableColumn
ipRouteIfName=_IpRouteIfName_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,5),_IpRouteIfName_Type())
ipRouteIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRouteIfName.setStatus(_B)
_IpRouteRowStatus_Type=RowStatus
_IpRouteRowStatus_Object=MibTableColumn
ipRouteRowStatus=_IpRouteRowStatus_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,6),_IpRouteRowStatus_Type())
ipRouteRowStatus.setMaxAccess(_j)
if mibBuilder.loadTexts:ipRouteRowStatus.setStatus(_B)
class _IpRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('system',1),('kernel',2),('connect',3),('static',4),('rip',5),('ripng',6),('ospf',7),('ospf6',8),('bgp',9)))
_IpRouteProto_Type.__name__=_F
_IpRouteProto_Object=MibTableColumn
ipRouteProto=_IpRouteProto_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,7),_IpRouteProto_Type())
ipRouteProto.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteProto.setStatus(_B)
class _IpRouteMetric_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IpRouteMetric_Type.__name__=_I
_IpRouteMetric_Object=MibTableColumn
ipRouteMetric=_IpRouteMetric_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,8),_IpRouteMetric_Type())
ipRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ipRouteMetric.setStatus(_B)
class _IpRouteOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('up',2)))
_IpRouteOperStatus_Type.__name__=_F
_IpRouteOperStatus_Object=MibTableColumn
ipRouteOperStatus=_IpRouteOperStatus_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,9),_IpRouteOperStatus_Type())
ipRouteOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteOperStatus.setStatus(_B)
_IpRouteName_Type=MgmtNameString
_IpRouteName_Object=MibTableColumn
ipRouteName=_IpRouteName_Object((1,3,6,1,4,1,8708,2,14,2,3,1,1,10),_IpRouteName_Type())
ipRouteName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipRouteName.setStatus(_B)
_OspfGeneral_ObjectIdentity=ObjectIdentity
ospfGeneral=_OspfGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,14,2,4))
_OspfGeneralRouterId_Type=IpAddress
_OspfGeneralRouterId_Object=MibScalar
ospfGeneralRouterId=_OspfGeneralRouterId_Object((1,3,6,1,4,1,8708,2,14,2,4,1),_OspfGeneralRouterId_Type())
ospfGeneralRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfGeneralRouterId.setStatus(_B)
class _OspfGeneralDistrMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_OspfGeneralDistrMode_Type.__name__=_F
_OspfGeneralDistrMode_Object=MibScalar
ospfGeneralDistrMode=_OspfGeneralDistrMode_Object((1,3,6,1,4,1,8708,2,14,2,4,2),_OspfGeneralDistrMode_Type())
ospfGeneralDistrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfGeneralDistrMode.setStatus(_B)
class _OspfGeneralDistrMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('comparableCost',1),('nonComparable',2)))
_OspfGeneralDistrMetricType_Type.__name__=_F
_OspfGeneralDistrMetricType_Object=MibScalar
ospfGeneralDistrMetricType=_OspfGeneralDistrMetricType_Object((1,3,6,1,4,1,8708,2,14,2,4,3),_OspfGeneralDistrMetricType_Type())
ospfGeneralDistrMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfGeneralDistrMetricType.setStatus(_B)
class _OspfGeneralDistrMetric_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_OspfGeneralDistrMetric_Type.__name__=_I
_OspfGeneralDistrMetric_Object=MibScalar
ospfGeneralDistrMetric=_OspfGeneralDistrMetric_Object((1,3,6,1,4,1,8708,2,14,2,4,4),_OspfGeneralDistrMetric_Type())
ospfGeneralDistrMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfGeneralDistrMetric.setStatus(_B)
_OspfIfList_ObjectIdentity=ObjectIdentity
ospfIfList=_OspfIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,14,2,5))
_OspfIfTable_Object=MibTable
ospfIfTable=_OspfIfTable_Object((1,3,6,1,4,1,8708,2,14,2,5,1))
if mibBuilder.loadTexts:ospfIfTable.setStatus(_B)
_OspfIfEntry_Object=MibTableRow
ospfIfEntry=_OspfIfEntry_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1))
ospfIfEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:ospfIfEntry.setStatus(_B)
class _OspfIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OspfIfIndex_Type.__name__=_I
_OspfIfIndex_Object=MibTableColumn
ospfIfIndex=_OspfIfIndex_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,1),_OspfIfIndex_Type())
ospfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfIndex.setStatus(_B)
_OspfIfName_Type=MgmtNameString
_OspfIfName_Object=MibTableColumn
ospfIfName=_OspfIfName_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,3),_OspfIfName_Type())
ospfIfName.setMaxAccess(_j)
if mibBuilder.loadTexts:ospfIfName.setStatus(_B)
_OspfIfAreaId_Type=IpAddress
_OspfIfAreaId_Object=MibTableColumn
ospfIfAreaId=_OspfIfAreaId_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,4),_OspfIfAreaId_Type())
ospfIfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfIfAreaId.setStatus(_B)
class _OspfIfMetric_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OspfIfMetric_Type.__name__=_I
_OspfIfMetric_Object=MibTableColumn
ospfIfMetric=_OspfIfMetric_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,5),_OspfIfMetric_Type())
ospfIfMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfIfMetric.setStatus(_B)
class _OspfIfRtrPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OspfIfRtrPriority_Type.__name__=_F
_OspfIfRtrPriority_Object=MibTableColumn
ospfIfRtrPriority=_OspfIfRtrPriority_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,6),_OspfIfRtrPriority_Type())
ospfIfRtrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfIfRtrPriority.setStatus(_B)
_OspfIfDesignatedRouterId_Type=IpAddress
_OspfIfDesignatedRouterId_Object=MibTableColumn
ospfIfDesignatedRouterId=_OspfIfDesignatedRouterId_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,7),_OspfIfDesignatedRouterId_Type())
ospfIfDesignatedRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfDesignatedRouterId.setStatus(_B)
_OspfIfBackupDesignatedRouterId_Type=IpAddress
_OspfIfBackupDesignatedRouterId_Object=MibTableColumn
ospfIfBackupDesignatedRouterId=_OspfIfBackupDesignatedRouterId_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,8),_OspfIfBackupDesignatedRouterId_Type())
ospfIfBackupDesignatedRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfBackupDesignatedRouterId.setStatus(_B)
class _OspfIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_X,2)))
_OspfIfAdminStatus_Type.__name__=_F
_OspfIfAdminStatus_Object=MibTableColumn
ospfIfAdminStatus=_OspfIfAdminStatus_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,9),_OspfIfAdminStatus_Type())
ospfIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfIfAdminStatus.setStatus(_B)
class _OspfIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('undefined',0),(_X,1),('loopback',2),('waiting',3),('ptp',4),('dr',5),('bdr',6),('odr',7)))
_OspfIfOperStatus_Type.__name__=_F
_OspfIfOperStatus_Object=MibTableColumn
ospfIfOperStatus=_OspfIfOperStatus_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,10),_OspfIfOperStatus_Type())
ospfIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfIfOperStatus.setStatus(_B)
_OspfIfRowStatus_Type=RowStatus
_OspfIfRowStatus_Object=MibTableColumn
ospfIfRowStatus=_OspfIfRowStatus_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,11),_OspfIfRowStatus_Type())
ospfIfRowStatus.setMaxAccess(_j)
if mibBuilder.loadTexts:ospfIfRowStatus.setStatus(_B)
class _OspfIfPassive_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_OspfIfPassive_Type.__name__=_F
_OspfIfPassive_Object=MibTableColumn
ospfIfPassive=_OspfIfPassive_Object((1,3,6,1,4,1,8708,2,14,2,5,1,1,12),_OspfIfPassive_Type())
ospfIfPassive.setMaxAccess(_D)
if mibBuilder.loadTexts:ospfIfPassive.setStatus(_B)
_OspfNbrList_ObjectIdentity=ObjectIdentity
ospfNbrList=_OspfNbrList_ObjectIdentity((1,3,6,1,4,1,8708,2,14,2,6))
_OspfNbrTable_Object=MibTable
ospfNbrTable=_OspfNbrTable_Object((1,3,6,1,4,1,8708,2,14,2,6,1))
if mibBuilder.loadTexts:ospfNbrTable.setStatus(_B)
_OspfNbrEntry_Object=MibTableRow
ospfNbrEntry=_OspfNbrEntry_Object((1,3,6,1,4,1,8708,2,14,2,6,1,1))
ospfNbrEntry.setIndexNames((0,_A,_h))
if mibBuilder.loadTexts:ospfNbrEntry.setStatus(_B)
class _OspfNbrIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OspfNbrIndex_Type.__name__=_I
_OspfNbrIndex_Object=MibTableColumn
ospfNbrIndex=_OspfNbrIndex_Object((1,3,6,1,4,1,8708,2,14,2,6,1,1,1),_OspfNbrIndex_Type())
ospfNbrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrIndex.setStatus(_B)
_OspfNbrIpAddr_Type=IpAddress
_OspfNbrIpAddr_Object=MibTableColumn
ospfNbrIpAddr=_OspfNbrIpAddr_Object((1,3,6,1,4,1,8708,2,14,2,6,1,1,2),_OspfNbrIpAddr_Type())
ospfNbrIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrIpAddr.setStatus(_B)
_OspfNbrRtrId_Type=IpAddress
_OspfNbrRtrId_Object=MibTableColumn
ospfNbrRtrId=_OspfNbrRtrId_Object((1,3,6,1,4,1,8708,2,14,2,6,1,1,3),_OspfNbrRtrId_Type())
ospfNbrRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrRtrId.setStatus(_B)
_OspfNbrIfName_Type=MgmtNameString
_OspfNbrIfName_Object=MibTableColumn
ospfNbrIfName=_OspfNbrIfName_Object((1,3,6,1,4,1,8708,2,14,2,6,1,1,4),_OspfNbrIfName_Type())
ospfNbrIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrIfName.setStatus(_B)
class _OspfNbrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),('attempt',2),('init',3),('twoWay',4),('exchangeStart',5),('exchange',6),('loading',7),('full',8)))
_OspfNbrOperStatus_Type.__name__=_F
_OspfNbrOperStatus_Object=MibTableColumn
ospfNbrOperStatus=_OspfNbrOperStatus_Object((1,3,6,1,4,1,8708,2,14,2,6,1,1,5),_OspfNbrOperStatus_Type())
ospfNbrOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrOperStatus.setStatus(_B)
_OspfNbrName_Type=MgmtNameString
_OspfNbrName_Object=MibTableColumn
ospfNbrName=_OspfNbrName_Object((1,3,6,1,4,1,8708,2,14,2,6,1,1,6),_OspfNbrName_Type())
ospfNbrName.setMaxAccess(_C)
if mibBuilder.loadTexts:ospfNbrName.setStatus(_B)
ipGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,1))
ipGeneralGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ipGeneralGroup.setStatus(_B)
ipIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,2))
ipIfGroup.setObjects(*((_A,_e),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ipIfGroup.setStatus(_E)
ipRouteGroup=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,3))
ipRouteGroup.setObjects(*((_A,_f),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ipRouteGroup.setStatus(_E)
ospfGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,4))
ospfGeneralGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ospfGeneralGroup.setStatus(_B)
ospfIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,5))
ospfIfGroup.setObjects(*((_A,_g),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:ospfIfGroup.setStatus(_E)
ospfNbrGroup=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,6))
ospfNbrGroup.setObjects(*((_A,_h),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ospfNbrGroup.setStatus(_E)
ipGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,7))
ipGeneralGroupV2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q)))
if mibBuilder.loadTexts:ipGeneralGroupV2.setStatus(_E)
ipGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,8))
ipGeneralGroupV3.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ipGeneralGroupV3.setStatus(_B)
ipGeneralGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,9))
ipGeneralGroupV4.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:ipGeneralGroupV4.setStatus(_E)
ipRouteGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,10))
ipRouteGroupV2.setObjects(*((_A,_f),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_AI)))
if mibBuilder.loadTexts:ipRouteGroupV2.setStatus(_B)
ospfNbrGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,11))
ospfNbrGroupV2.setObjects(*((_A,_h),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_AJ)))
if mibBuilder.loadTexts:ospfNbrGroupV2.setStatus(_B)
ipGeneralGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,12))
ipGeneralGroupV5.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_i)))
if mibBuilder.loadTexts:ipGeneralGroupV5.setStatus(_E)
ospfIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,13))
ospfIfGroupV2.setObjects(*((_A,_g),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_AK)))
if mibBuilder.loadTexts:ospfIfGroupV2.setStatus(_B)
ipGeneralGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,14))
ipGeneralGroupV6.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_i),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ipGeneralGroupV6.setStatus(_E)
ipGeneralGroupV7=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,15))
ipGeneralGroupV7.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_Q),(_A,_R),(_A,_S),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_i),(_A,_A9),(_A,_AA),(_A,_AL)))
if mibBuilder.loadTexts:ipGeneralGroupV7.setStatus(_B)
ipIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,14,1,1,16))
ipIfGroupV2.setObjects(*((_A,_e),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_AM)))
if mibBuilder.loadTexts:ipIfGroupV2.setStatus(_B)
lumIpBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,1))
lumIpBasicComplV1.setObjects(*((_A,_AB),(_A,_G),(_A,_T)))
if mibBuilder.loadTexts:lumIpBasicComplV1.setStatus(_E)
lumIpBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,2))
lumIpBasicComplV2.setObjects(*((_A,_AB),(_A,_G),(_A,_T),(_A,_H),(_A,_U),(_A,_c)))
if mibBuilder.loadTexts:lumIpBasicComplV2.setStatus(_E)
lumIpBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,3))
lumIpBasicComplV3.setObjects(*((_A,_AN),(_A,_G),(_A,_T),(_A,_H),(_A,_U),(_A,_c)))
if mibBuilder.loadTexts:lumIpBasicComplV3.setStatus(_E)
lumIpBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,4))
lumIpBasicComplV4.setObjects(*((_A,_AO),(_A,_G),(_A,_T),(_A,_H),(_A,_U),(_A,_c)))
if mibBuilder.loadTexts:lumIpBasicComplV4.setStatus(_E)
lumIpBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,5))
lumIpBasicComplV5.setObjects(*((_A,_AP),(_A,_G),(_A,_T),(_A,_H),(_A,_U),(_A,_c)))
if mibBuilder.loadTexts:lumIpBasicComplV5.setStatus(_E)
lumIpBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,6))
lumIpBasicComplV6.setObjects(*((_A,_AC),(_A,_G),(_A,_V),(_A,_H),(_A,_U),(_A,_W)))
if mibBuilder.loadTexts:lumIpBasicComplV6.setStatus(_E)
lumIpBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,7))
lumIpBasicComplV7.setObjects(*((_A,_AC),(_A,_G),(_A,_V),(_A,_H),(_A,_d),(_A,_W)))
if mibBuilder.loadTexts:lumIpBasicComplV7.setStatus(_E)
lumIpBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,8))
lumIpBasicComplV8.setObjects(*((_A,_AQ),(_A,_G),(_A,_V),(_A,_H),(_A,_d),(_A,_W)))
if mibBuilder.loadTexts:lumIpBasicComplV8.setStatus(_E)
lumIpBasicComplV9=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,9))
lumIpBasicComplV9.setObjects(*((_A,_AD),(_A,_G),(_A,_V),(_A,_H),(_A,_d),(_A,_W)))
if mibBuilder.loadTexts:lumIpBasicComplV9.setStatus(_E)
lumIpBasicComplV10=ModuleCompliance((1,3,6,1,4,1,8708,2,14,1,2,10))
lumIpBasicComplV10.setObjects(*((_A,_AD),(_A,_AR),(_A,_V),(_A,_H),(_A,_d),(_A,_W)))
if mibBuilder.loadTexts:lumIpBasicComplV10.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIpMIBModule':lumIpMIBModule,'lumIpConfs':lumIpConfs,'lumIpGroups':lumIpGroups,_AB:ipGeneralGroup,_G:ipIfGroup,_T:ipRouteGroup,_H:ospfGeneralGroup,_U:ospfIfGroup,_c:ospfNbrGroup,_AN:ipGeneralGroupV2,_AO:ipGeneralGroupV3,_AP:ipGeneralGroupV4,_V:ipRouteGroupV2,_W:ospfNbrGroupV2,_AC:ipGeneralGroupV5,_d:ospfIfGroupV2,_AQ:ipGeneralGroupV6,_AD:ipGeneralGroupV7,_AR:ipIfGroupV2,'lumIpCompl':lumIpCompl,'lumIpBasicComplV1':lumIpBasicComplV1,'lumIpBasicComplV2':lumIpBasicComplV2,'lumIpBasicComplV3':lumIpBasicComplV3,'lumIpBasicComplV4':lumIpBasicComplV4,'lumIpBasicComplV5':lumIpBasicComplV5,'lumIpBasicComplV6':lumIpBasicComplV6,'lumIpBasicComplV7':lumIpBasicComplV7,'lumIpBasicComplV8':lumIpBasicComplV8,'lumIpBasicComplV9':lumIpBasicComplV9,'lumIpBasicComplV10':lumIpBasicComplV10,'lumIpMIBObjects':lumIpMIBObjects,'ipGeneral':ipGeneral,_J:ipGeneralLastChangeTime,_K:ipGeneralNextMgmtAddress,_L:ipGeneralStoredMgmtAddress,_M:ipGeneralNextMgmtNetMask,_N:ipGeneralStoredMgmtNetMask,_Q:ipGeneralConfigLastChangeTime,_R:ipGeneralTelnetMode,_S:ipGeneralFtpMode,_Y:ipGeneralIfTableSize,_Z:ipGeneralRouteTableSize,_a:ipGeneralOspfIfTableSize,_b:ipGeneralOspfNbrTableSize,_i:ipGeneralChangeNextMgmtAddr,_A9:ipGeneralSftpMode,_AA:ipGeneralTftpMode,_AL:ipGeneralNetconfMode,'ipIfList':ipIfList,'ipIfTable':ipIfTable,'ipIfEntry':ipIfEntry,_e:ipIfIndex,_k:ipIfName,_l:ipIfAddr,_m:ipIfNetMask,_n:ipIfOperStatus,_AM:ipIfDstAddr,'ipRouteList':ipRouteList,'ipRouteTable':ipRouteTable,'ipRouteEntry':ipRouteEntry,_f:ipRouteIndex,_o:ipRouteDest,_p:ipRouteMask,_q:ipRouteNextHop,_r:ipRouteIfName,_s:ipRouteRowStatus,_t:ipRouteProto,_u:ipRouteMetric,_v:ipRouteOperStatus,_AI:ipRouteName,'ospfGeneral':ospfGeneral,_AE:ospfGeneralRouterId,_AF:ospfGeneralDistrMode,_AG:ospfGeneralDistrMetricType,_AH:ospfGeneralDistrMetric,'ospfIfList':ospfIfList,'ospfIfTable':ospfIfTable,'ospfIfEntry':ospfIfEntry,_g:ospfIfIndex,_w:ospfIfName,_x:ospfIfAreaId,_y:ospfIfMetric,_z:ospfIfRtrPriority,_A0:ospfIfDesignatedRouterId,_A1:ospfIfBackupDesignatedRouterId,_A2:ospfIfAdminStatus,_A3:ospfIfOperStatus,_A4:ospfIfRowStatus,_AK:ospfIfPassive,'ospfNbrList':ospfNbrList,'ospfNbrTable':ospfNbrTable,'ospfNbrEntry':ospfNbrEntry,_h:ospfNbrIndex,_A5:ospfNbrIpAddr,_A6:ospfNbrRtrId,_A7:ospfNbrIfName,_A8:ospfNbrOperStatus,_AJ:ospfNbrName})