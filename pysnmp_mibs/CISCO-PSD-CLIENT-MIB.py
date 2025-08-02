_g='cPsdClientMIBNotifMgmtGroup'
_f='cPsdClientMIBNotifInfoGroup'
_e='cPsdClientMIBNotifGroup'
_d='cPsdClientMIBConfigurationsGroup'
_c='cPsdClientMIBStatisticsGroup'
_b='cPsdClientDiskFullNotif'
_a='cPsdClientUpNotif'
_Z='cPsdClientDownNotif'
_Y='cPsdClientNotifEnable'
_X='cPsdClientDSRetrieveOnly'
_W='cPsdClientDSServerRowStatus'
_V='cPsdClientDSMaxRetrieve'
_U='cPsdClientDSAutoRetrieve'
_T='cPsdClientDSRowStatus'
_S='cPsdClientDSDiskFullTrans'
_R='cPsdClientDSRdWrRetrans'
_Q='cPsdClientDSReadReq'
_P='cPsdClientDSWriteReq'
_O='accessible-for-notify'
_N='cPsdClientDSServerAddress'
_M='cPsdClientDSServerAddressType'
_L='Integer32'
_K='SnmpAdminString'
_J='InetAddress'
_I='not-accessible'
_H='cPsdClientDSName'
_G='TruthValue'
_F='read-only'
_E='cPsdClientNotifDSServerAddress'
_D='cPsdClientNotifDSServerAddrType'
_C='read-create'
_B='current'
_A='CISCO-PSD-CLIENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
ciscoPsdClientMIB=ModuleIdentity((1,3,6,1,4,1,9,9,495))
if mibBuilder.loadTexts:ciscoPsdClientMIB.setRevisions(('2005-08-24 18:00',))
_CiscoPsdClientMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPsdClientMIBNotifs=_CiscoPsdClientMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,495,0))
_CiscoPsdClientMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPsdClientMIBObjects=_CiscoPsdClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,495,1))
_CiscoPsdClientStatistics_ObjectIdentity=ObjectIdentity
ciscoPsdClientStatistics=_CiscoPsdClientStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,495,1,1))
_CPsdClientDSWriteReq_Type=Counter32
_CPsdClientDSWriteReq_Object=MibScalar
cPsdClientDSWriteReq=_CPsdClientDSWriteReq_Object((1,3,6,1,4,1,9,9,495,1,1,1),_CPsdClientDSWriteReq_Type())
cPsdClientDSWriteReq.setMaxAccess(_F)
if mibBuilder.loadTexts:cPsdClientDSWriteReq.setStatus(_B)
_CPsdClientDSReadReq_Type=Counter32
_CPsdClientDSReadReq_Object=MibScalar
cPsdClientDSReadReq=_CPsdClientDSReadReq_Object((1,3,6,1,4,1,9,9,495,1,1,2),_CPsdClientDSReadReq_Type())
cPsdClientDSReadReq.setMaxAccess(_F)
if mibBuilder.loadTexts:cPsdClientDSReadReq.setStatus(_B)
_CPsdClientDSRdWrRetrans_Type=Counter32
_CPsdClientDSRdWrRetrans_Object=MibScalar
cPsdClientDSRdWrRetrans=_CPsdClientDSRdWrRetrans_Object((1,3,6,1,4,1,9,9,495,1,1,3),_CPsdClientDSRdWrRetrans_Type())
cPsdClientDSRdWrRetrans.setMaxAccess(_F)
if mibBuilder.loadTexts:cPsdClientDSRdWrRetrans.setStatus(_B)
_CPsdClientDSDiskFullTrans_Type=Counter32
_CPsdClientDSDiskFullTrans_Object=MibScalar
cPsdClientDSDiskFullTrans=_CPsdClientDSDiskFullTrans_Object((1,3,6,1,4,1,9,9,495,1,1,4),_CPsdClientDSDiskFullTrans_Type())
cPsdClientDSDiskFullTrans.setMaxAccess(_F)
if mibBuilder.loadTexts:cPsdClientDSDiskFullTrans.setStatus(_B)
_CiscoPsdClientNotifMgmt_ObjectIdentity=ObjectIdentity
ciscoPsdClientNotifMgmt=_CiscoPsdClientNotifMgmt_ObjectIdentity((1,3,6,1,4,1,9,9,495,1,2))
class _CPsdClientNotifEnable_Type(TruthValue):defaultValue=2
_CPsdClientNotifEnable_Type.__name__=_G
_CPsdClientNotifEnable_Object=MibScalar
cPsdClientNotifEnable=_CPsdClientNotifEnable_Object((1,3,6,1,4,1,9,9,495,1,2,1),_CPsdClientNotifEnable_Type())
cPsdClientNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cPsdClientNotifEnable.setStatus(_B)
_CiscoPsdClientConfigurations_ObjectIdentity=ObjectIdentity
ciscoPsdClientConfigurations=_CiscoPsdClientConfigurations_ObjectIdentity((1,3,6,1,4,1,9,9,495,1,3))
_CPsdClientDSTable_Object=MibTable
cPsdClientDSTable=_CPsdClientDSTable_Object((1,3,6,1,4,1,9,9,495,1,3,1))
if mibBuilder.loadTexts:cPsdClientDSTable.setStatus(_B)
_CPsdClientDSEntry_Object=MibTableRow
cPsdClientDSEntry=_CPsdClientDSEntry_Object((1,3,6,1,4,1,9,9,495,1,3,1,1))
cPsdClientDSEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cPsdClientDSEntry.setStatus(_B)
class _CPsdClientDSName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CPsdClientDSName_Type.__name__=_K
_CPsdClientDSName_Object=MibTableColumn
cPsdClientDSName=_CPsdClientDSName_Object((1,3,6,1,4,1,9,9,495,1,3,1,1,1),_CPsdClientDSName_Type())
cPsdClientDSName.setMaxAccess(_I)
if mibBuilder.loadTexts:cPsdClientDSName.setStatus(_B)
class _CPsdClientDSAutoRetrieve_Type(TruthValue):defaultValue=2
_CPsdClientDSAutoRetrieve_Type.__name__=_G
_CPsdClientDSAutoRetrieve_Object=MibTableColumn
cPsdClientDSAutoRetrieve=_CPsdClientDSAutoRetrieve_Object((1,3,6,1,4,1,9,9,495,1,3,1,1,2),_CPsdClientDSAutoRetrieve_Type())
cPsdClientDSAutoRetrieve.setMaxAccess(_C)
if mibBuilder.loadTexts:cPsdClientDSAutoRetrieve.setStatus(_B)
class _CPsdClientDSMaxRetrieve_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6000))
_CPsdClientDSMaxRetrieve_Type.__name__=_L
_CPsdClientDSMaxRetrieve_Object=MibTableColumn
cPsdClientDSMaxRetrieve=_CPsdClientDSMaxRetrieve_Object((1,3,6,1,4,1,9,9,495,1,3,1,1,3),_CPsdClientDSMaxRetrieve_Type())
cPsdClientDSMaxRetrieve.setMaxAccess(_C)
if mibBuilder.loadTexts:cPsdClientDSMaxRetrieve.setStatus(_B)
if mibBuilder.loadTexts:cPsdClientDSMaxRetrieve.setUnits('messages/minute')
_CPsdClientDSRowStatus_Type=RowStatus
_CPsdClientDSRowStatus_Object=MibTableColumn
cPsdClientDSRowStatus=_CPsdClientDSRowStatus_Object((1,3,6,1,4,1,9,9,495,1,3,1,1,4),_CPsdClientDSRowStatus_Type())
cPsdClientDSRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cPsdClientDSRowStatus.setStatus(_B)
_CPsdClientDSServerTable_Object=MibTable
cPsdClientDSServerTable=_CPsdClientDSServerTable_Object((1,3,6,1,4,1,9,9,495,1,3,2))
if mibBuilder.loadTexts:cPsdClientDSServerTable.setStatus(_B)
_CPsdClientDSServerEntry_Object=MibTableRow
cPsdClientDSServerEntry=_CPsdClientDSServerEntry_Object((1,3,6,1,4,1,9,9,495,1,3,2,1))
cPsdClientDSServerEntry.setIndexNames((0,_A,_H),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:cPsdClientDSServerEntry.setStatus(_B)
_CPsdClientDSServerAddressType_Type=InetAddressType
_CPsdClientDSServerAddressType_Object=MibTableColumn
cPsdClientDSServerAddressType=_CPsdClientDSServerAddressType_Object((1,3,6,1,4,1,9,9,495,1,3,2,1,1),_CPsdClientDSServerAddressType_Type())
cPsdClientDSServerAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:cPsdClientDSServerAddressType.setStatus(_B)
class _CPsdClientDSServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_CPsdClientDSServerAddress_Type.__name__=_J
_CPsdClientDSServerAddress_Object=MibTableColumn
cPsdClientDSServerAddress=_CPsdClientDSServerAddress_Object((1,3,6,1,4,1,9,9,495,1,3,2,1,2),_CPsdClientDSServerAddress_Type())
cPsdClientDSServerAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:cPsdClientDSServerAddress.setStatus(_B)
_CPsdClientDSRetrieveOnly_Type=TruthValue
_CPsdClientDSRetrieveOnly_Object=MibTableColumn
cPsdClientDSRetrieveOnly=_CPsdClientDSRetrieveOnly_Object((1,3,6,1,4,1,9,9,495,1,3,2,1,3),_CPsdClientDSRetrieveOnly_Type())
cPsdClientDSRetrieveOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:cPsdClientDSRetrieveOnly.setStatus(_B)
_CPsdClientDSServerRowStatus_Type=RowStatus
_CPsdClientDSServerRowStatus_Object=MibTableColumn
cPsdClientDSServerRowStatus=_CPsdClientDSServerRowStatus_Object((1,3,6,1,4,1,9,9,495,1,3,2,1,4),_CPsdClientDSServerRowStatus_Type())
cPsdClientDSServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cPsdClientDSServerRowStatus.setStatus(_B)
_CiscoPsdClientNotifInfo_ObjectIdentity=ObjectIdentity
ciscoPsdClientNotifInfo=_CiscoPsdClientNotifInfo_ObjectIdentity((1,3,6,1,4,1,9,9,495,1,4))
_CPsdClientNotifDSServerAddrType_Type=InetAddressType
_CPsdClientNotifDSServerAddrType_Object=MibScalar
cPsdClientNotifDSServerAddrType=_CPsdClientNotifDSServerAddrType_Object((1,3,6,1,4,1,9,9,495,1,4,1),_CPsdClientNotifDSServerAddrType_Type())
cPsdClientNotifDSServerAddrType.setMaxAccess(_O)
if mibBuilder.loadTexts:cPsdClientNotifDSServerAddrType.setStatus(_B)
_CPsdClientNotifDSServerAddress_Type=InetAddress
_CPsdClientNotifDSServerAddress_Object=MibScalar
cPsdClientNotifDSServerAddress=_CPsdClientNotifDSServerAddress_Object((1,3,6,1,4,1,9,9,495,1,4,2),_CPsdClientNotifDSServerAddress_Type())
cPsdClientNotifDSServerAddress.setMaxAccess(_O)
if mibBuilder.loadTexts:cPsdClientNotifDSServerAddress.setStatus(_B)
_CiscoPsdClientMIBConform_ObjectIdentity=ObjectIdentity
ciscoPsdClientMIBConform=_CiscoPsdClientMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,495,2))
_CPsdClientMIBCompliances_ObjectIdentity=ObjectIdentity
cPsdClientMIBCompliances=_CPsdClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,495,2,1))
_CPsdClientMIBGroups_ObjectIdentity=ObjectIdentity
cPsdClientMIBGroups=_CPsdClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,495,2,2))
cPsdClientMIBStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,495,2,2,1))
cPsdClientMIBStatisticsGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cPsdClientMIBStatisticsGroup.setStatus(_B)
cPsdClientMIBConfigurationsGroup=ObjectGroup((1,3,6,1,4,1,9,9,495,2,2,2))
cPsdClientMIBConfigurationsGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cPsdClientMIBConfigurationsGroup.setStatus(_B)
cPsdClientMIBNotifInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,495,2,2,4))
cPsdClientMIBNotifInfoGroup.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:cPsdClientMIBNotifInfoGroup.setStatus(_B)
cPsdClientMIBNotifMgmtGroup=ObjectGroup((1,3,6,1,4,1,9,9,495,2,2,5))
cPsdClientMIBNotifMgmtGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:cPsdClientMIBNotifMgmtGroup.setStatus(_B)
cPsdClientDownNotif=NotificationType((1,3,6,1,4,1,9,9,495,0,1))
cPsdClientDownNotif.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:cPsdClientDownNotif.setStatus(_B)
cPsdClientUpNotif=NotificationType((1,3,6,1,4,1,9,9,495,0,2))
cPsdClientUpNotif.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:cPsdClientUpNotif.setStatus(_B)
cPsdClientDiskFullNotif=NotificationType((1,3,6,1,4,1,9,9,495,0,3))
cPsdClientDiskFullNotif.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:cPsdClientDiskFullNotif.setStatus(_B)
cPsdClientMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,495,2,2,3))
cPsdClientMIBNotifGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cPsdClientMIBNotifGroup.setStatus(_B)
cPsdClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,495,2,1,1))
cPsdClientMIBCompliance.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:cPsdClientMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoPsdClientMIB':ciscoPsdClientMIB,'ciscoPsdClientMIBNotifs':ciscoPsdClientMIBNotifs,_Z:cPsdClientDownNotif,_a:cPsdClientUpNotif,_b:cPsdClientDiskFullNotif,'ciscoPsdClientMIBObjects':ciscoPsdClientMIBObjects,'ciscoPsdClientStatistics':ciscoPsdClientStatistics,_P:cPsdClientDSWriteReq,_Q:cPsdClientDSReadReq,_R:cPsdClientDSRdWrRetrans,_S:cPsdClientDSDiskFullTrans,'ciscoPsdClientNotifMgmt':ciscoPsdClientNotifMgmt,_Y:cPsdClientNotifEnable,'ciscoPsdClientConfigurations':ciscoPsdClientConfigurations,'cPsdClientDSTable':cPsdClientDSTable,'cPsdClientDSEntry':cPsdClientDSEntry,_H:cPsdClientDSName,_U:cPsdClientDSAutoRetrieve,_V:cPsdClientDSMaxRetrieve,_T:cPsdClientDSRowStatus,'cPsdClientDSServerTable':cPsdClientDSServerTable,'cPsdClientDSServerEntry':cPsdClientDSServerEntry,_M:cPsdClientDSServerAddressType,_N:cPsdClientDSServerAddress,_X:cPsdClientDSRetrieveOnly,_W:cPsdClientDSServerRowStatus,'ciscoPsdClientNotifInfo':ciscoPsdClientNotifInfo,_D:cPsdClientNotifDSServerAddrType,_E:cPsdClientNotifDSServerAddress,'ciscoPsdClientMIBConform':ciscoPsdClientMIBConform,'cPsdClientMIBCompliances':cPsdClientMIBCompliances,'cPsdClientMIBCompliance':cPsdClientMIBCompliance,'cPsdClientMIBGroups':cPsdClientMIBGroups,_c:cPsdClientMIBStatisticsGroup,_d:cPsdClientMIBConfigurationsGroup,_e:cPsdClientMIBNotifGroup,_f:cPsdClientMIBNotifInfoGroup,_g:cPsdClientMIBNotifMgmtGroup})