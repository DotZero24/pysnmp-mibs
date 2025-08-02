_V='ciscoDot11LbsConfigGroup'
_U='cdot11LbsProfInterfaceRowStatus'
_T='cdot11LbsProfileRowStatus'
_S='cdot11LbsMatchChannel'
_R='cdot11LbsTrackMulticast'
_Q='cdot11LbsPsPacketType'
_P='cdot11LbsTrackMethod'
_O='cdot11LbsServerUdpPort'
_N='cdot11LbsServerAddress'
_M='cdot11LbsServerAddressType'
_L='Cdot11LbsPsPacketType'
_K='Cdot11LbsTrackMethodType'
_J='TruthValue'
_I='MacAddress'
_H='SnmpAdminString'
_G='InetAddressType'
_F='ifIndex'
_E='IF-MIB'
_D='cdot11LbsProfileName'
_C='read-create'
_B='CISCO-DOT11-LBS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_G,'InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_I,'PhysAddress','RowStatus','TextualConvention',_J)
ciscoDot11LbsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,454))
if mibBuilder.loadTexts:ciscoDot11LbsMIB.setRevisions(('2004-11-17 00:00',))
class Cdot11LbsTrackMethodType(TextualConvention,Bits):status=_A;namedValues=NamedValues(('rssi',0))
class Cdot11LbsPsPacketType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('extended',1),('short',2)))
_CiscoDot11LbsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDot11LbsMIBNotifs=_CiscoDot11LbsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,454,0))
_CiscoDot11LbsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11LbsMIBObjects=_CiscoDot11LbsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,454,1))
_CiscoDot11LbsConfigInfo_ObjectIdentity=ObjectIdentity
ciscoDot11LbsConfigInfo=_CiscoDot11LbsConfigInfo_ObjectIdentity((1,3,6,1,4,1,9,9,454,1,1))
_Cdot11LbsProfileTable_Object=MibTable
cdot11LbsProfileTable=_Cdot11LbsProfileTable_Object((1,3,6,1,4,1,9,9,454,1,1,1))
if mibBuilder.loadTexts:cdot11LbsProfileTable.setStatus(_A)
_Cdot11LbsProfileEntry_Object=MibTableRow
cdot11LbsProfileEntry=_Cdot11LbsProfileEntry_Object((1,3,6,1,4,1,9,9,454,1,1,1,1))
cdot11LbsProfileEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cdot11LbsProfileEntry.setStatus(_A)
class _Cdot11LbsProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Cdot11LbsProfileName_Type.__name__=_H
_Cdot11LbsProfileName_Object=MibTableColumn
cdot11LbsProfileName=_Cdot11LbsProfileName_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,1),_Cdot11LbsProfileName_Type())
cdot11LbsProfileName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cdot11LbsProfileName.setStatus(_A)
class _Cdot11LbsServerAddressType_Type(InetAddressType):defaultValue=1
_Cdot11LbsServerAddressType_Type.__name__=_G
_Cdot11LbsServerAddressType_Object=MibTableColumn
cdot11LbsServerAddressType=_Cdot11LbsServerAddressType_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,2),_Cdot11LbsServerAddressType_Type())
cdot11LbsServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsServerAddressType.setStatus(_A)
_Cdot11LbsServerAddress_Type=InetAddress
_Cdot11LbsServerAddress_Object=MibTableColumn
cdot11LbsServerAddress=_Cdot11LbsServerAddress_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,3),_Cdot11LbsServerAddress_Type())
cdot11LbsServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsServerAddress.setStatus(_A)
_Cdot11LbsServerUdpPort_Type=InetPortNumber
_Cdot11LbsServerUdpPort_Object=MibTableColumn
cdot11LbsServerUdpPort=_Cdot11LbsServerUdpPort_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,4),_Cdot11LbsServerUdpPort_Type())
cdot11LbsServerUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsServerUdpPort.setStatus(_A)
class _Cdot11LbsTrackMethod_Type(Cdot11LbsTrackMethodType):defaultBinValue='1'
_Cdot11LbsTrackMethod_Type.__name__=_K
_Cdot11LbsTrackMethod_Object=MibTableColumn
cdot11LbsTrackMethod=_Cdot11LbsTrackMethod_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,5),_Cdot11LbsTrackMethod_Type())
cdot11LbsTrackMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsTrackMethod.setStatus(_A)
class _Cdot11LbsPsPacketType_Type(Cdot11LbsPsPacketType):defaultValue=1
_Cdot11LbsPsPacketType_Type.__name__=_L
_Cdot11LbsPsPacketType_Object=MibTableColumn
cdot11LbsPsPacketType=_Cdot11LbsPsPacketType_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,6),_Cdot11LbsPsPacketType_Type())
cdot11LbsPsPacketType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsPsPacketType.setStatus(_A)
class _Cdot11LbsTrackMulticast_Type(MacAddress):defaultHexValue='014096000010'
_Cdot11LbsTrackMulticast_Type.__name__=_I
_Cdot11LbsTrackMulticast_Object=MibTableColumn
cdot11LbsTrackMulticast=_Cdot11LbsTrackMulticast_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,7),_Cdot11LbsTrackMulticast_Type())
cdot11LbsTrackMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsTrackMulticast.setStatus(_A)
class _Cdot11LbsMatchChannel_Type(TruthValue):defaultValue=1
_Cdot11LbsMatchChannel_Type.__name__=_J
_Cdot11LbsMatchChannel_Object=MibTableColumn
cdot11LbsMatchChannel=_Cdot11LbsMatchChannel_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,8),_Cdot11LbsMatchChannel_Type())
cdot11LbsMatchChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsMatchChannel.setStatus(_A)
_Cdot11LbsProfileRowStatus_Type=RowStatus
_Cdot11LbsProfileRowStatus_Object=MibTableColumn
cdot11LbsProfileRowStatus=_Cdot11LbsProfileRowStatus_Object((1,3,6,1,4,1,9,9,454,1,1,1,1,9),_Cdot11LbsProfileRowStatus_Type())
cdot11LbsProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsProfileRowStatus.setStatus(_A)
_Cdot11LbsProfInterfaceTable_Object=MibTable
cdot11LbsProfInterfaceTable=_Cdot11LbsProfInterfaceTable_Object((1,3,6,1,4,1,9,9,454,1,1,2))
if mibBuilder.loadTexts:cdot11LbsProfInterfaceTable.setStatus(_A)
_Cdot11LbsProfInterfaceEntry_Object=MibTableRow
cdot11LbsProfInterfaceEntry=_Cdot11LbsProfInterfaceEntry_Object((1,3,6,1,4,1,9,9,454,1,1,2,1))
cdot11LbsProfInterfaceEntry.setIndexNames((0,_B,_D),(0,_E,_F))
if mibBuilder.loadTexts:cdot11LbsProfInterfaceEntry.setStatus(_A)
_Cdot11LbsProfInterfaceRowStatus_Type=RowStatus
_Cdot11LbsProfInterfaceRowStatus_Object=MibTableColumn
cdot11LbsProfInterfaceRowStatus=_Cdot11LbsProfInterfaceRowStatus_Object((1,3,6,1,4,1,9,9,454,1,1,2,1,1),_Cdot11LbsProfInterfaceRowStatus_Type())
cdot11LbsProfInterfaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11LbsProfInterfaceRowStatus.setStatus(_A)
_CiscoDot11LbsStatistics_ObjectIdentity=ObjectIdentity
ciscoDot11LbsStatistics=_CiscoDot11LbsStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,454,1,2))
_CiscoDot11LbsMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDot11LbsMIBConformance=_CiscoDot11LbsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,454,2))
_CiscoDot11LbsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11LbsMIBCompliances=_CiscoDot11LbsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,454,2,1))
_CiscoDot11LbsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11LbsMIBGroups=_CiscoDot11LbsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,454,2,2))
ciscoDot11LbsConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,454,2,2,1))
ciscoDot11LbsConfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoDot11LbsConfigGroup.setStatus(_A)
ciscoDot11LbsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,454,2,1,1))
ciscoDot11LbsMIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:ciscoDot11LbsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_K:Cdot11LbsTrackMethodType,_L:Cdot11LbsPsPacketType,'ciscoDot11LbsMIB':ciscoDot11LbsMIB,'ciscoDot11LbsMIBNotifs':ciscoDot11LbsMIBNotifs,'ciscoDot11LbsMIBObjects':ciscoDot11LbsMIBObjects,'ciscoDot11LbsConfigInfo':ciscoDot11LbsConfigInfo,'cdot11LbsProfileTable':cdot11LbsProfileTable,'cdot11LbsProfileEntry':cdot11LbsProfileEntry,_D:cdot11LbsProfileName,_M:cdot11LbsServerAddressType,_N:cdot11LbsServerAddress,_O:cdot11LbsServerUdpPort,_P:cdot11LbsTrackMethod,_Q:cdot11LbsPsPacketType,_R:cdot11LbsTrackMulticast,_S:cdot11LbsMatchChannel,_T:cdot11LbsProfileRowStatus,'cdot11LbsProfInterfaceTable':cdot11LbsProfInterfaceTable,'cdot11LbsProfInterfaceEntry':cdot11LbsProfInterfaceEntry,_U:cdot11LbsProfInterfaceRowStatus,'ciscoDot11LbsStatistics':ciscoDot11LbsStatistics,'ciscoDot11LbsMIBConformance':ciscoDot11LbsMIBConformance,'ciscoDot11LbsMIBCompliances':ciscoDot11LbsMIBCompliances,'ciscoDot11LbsMIBCompliance':ciscoDot11LbsMIBCompliance,'ciscoDot11LbsMIBGroups':ciscoDot11LbsMIBGroups,_V:ciscoDot11LbsConfigGroup})