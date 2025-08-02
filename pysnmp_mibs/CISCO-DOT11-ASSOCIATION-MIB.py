_Ak='ciscoDot11ClientStatusTrapsGroup'
_Aj='cDot11ClientNewKeyManagement'
_Ai='cDot11ClientDevObjectID'
_Ah='cDot11ClientMulticastCipher'
_Ag='cDot11ClientUnicastCipher'
_Af='cDot11ClientKeyManagement'
_Ae='cDot11ClientDot1xAuthenAlgorithm'
_Ad='cDot11ClientAdditionalAuthen'
_Ac='cDot11ClientAuthenAlgorithm'
_Ab='cDot11ClientSubIfIndex'
_Aa='cDot11ClientVlanId'
_AZ='cd11IfCipherTkipReplaysDetected'
_AY='cd11IfCipherCcmpReplaysDiscarded'
_AX='cd11IfCipherTkipCounterMeasInvok'
_AW='cd11IfCipherTkipRemotMicFailures'
_AV='cd11IfCipherTkipLocalMicFailures'
_AU='cd11IfCipherMicFailClientAddress'
_AT='cDot11ClientIpAddress'
_AS='cDot11ClientIpAddressType'
_AR='cDot11ClientAssociationState'
_AQ='cDot11ClientName'
_AP='cDot11ClientSoftwareVersion'
_AO='cDot11ClientMicMissingFrames'
_AN='cDot11ClientMicErrors'
_AM='cDot11ClientWepErrors'
_AL='cDot11ClientMsduFails'
_AK='cDot11ClientMsduRetries'
_AJ='cDot11ClientDuplicates'
_AI='cDot11ClientAgingLeft'
_AH='cDot11ClientBytesSent'
_AG='cDot11ClientPacketsSent'
_AF='cDot11ClientBytesReceived'
_AE='cDot11ClientPacketsReceived'
_AD='cDot11ClientSigQuality'
_AC='cDot11ClientSignalStrength'
_AB='cDot11ClientUpTime'
_AA='cDot11ClientCurrentTxRateSet'
_A9='cDot11ClientDataRateSet'
_A8='cDot11ClientAid'
_A7='cDot11ClientPowerSaveMode'
_A6='cDot11ClientMicEnabled'
_A5='cDot11ClientWepKeyMixEnabled'
_A4='cDot11ClientWepEnabled'
_A3='cDot11ClientRadioType'
_A2='cDot11ClientDevType'
_A1='cDot11ClientRoleClassType'
_A0='cDot11ClientParentAddress'
_z='cDot11ClientStatisticEntry'
_y='second'
_x='cDot11ClientAddress'
_w='unknown'
_v='ethernetClient'
_u='cd11IfAuxSsid'
_t='CISCO-DOT11-IF-MIB'
_s='ciscoDot11ClientNewAuthenGroup'
_r='ciscoDot11AssocGlobalGroup'
_q='clientDisassocReasonStr'
_p='clientStationState'
_o='apIpv6Address'
_n='apIpv4Address'
_m='apMacAddr'
_l='clientIpv6Address'
_k='clientIpv4Address'
_j='clientDeviceName'
_i='clientDeviceType'
_h='clientMacAddr'
_g='cDot11AssStatsDisassociated'
_f='cDot11AssStatsDeauthenticated'
_e='cDot11AssStatsRoamedAway'
_d='cDot11AssStatsRoamedIn'
_c='cDot11AssStatsAuthenticated'
_b='cDot11AssStatsAssociated'
_a='cDot11ActiveRepeaters'
_Z='cDot11ActiveBridges'
_Y='cDot11ActiveWirelessClients'
_X='cDot11ParentAddress'
_W='Device'
_V='Unsigned32'
_U='OctetString'
_T='ciscoDot11ClientConfigExtGroup'
_S='TruthValue'
_R='Gauge32'
_Q='ciscoDot11ClientAuthenGroup'
_P='Integer32'
_O='ciscoDot11ApAssocGlobalGroup'
_N='ciscoDot11IfCipherStatGroup'
_M='ciscoDot11IfAssocStatGroup'
_L='client'
_K='ciscoDot11ClientInfoGroup'
_J='packet'
_I='ifIndex'
_H='IF-MIB'
_G='ciscoDot11ClientStatGroup'
_F='ciscoDot11ClientConfigGroup'
_E='deprecated'
_D='accessible-for-notify'
_C='read-only'
_B='current'
_A='CISCO-DOT11-ASSOCIATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_U,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CDot11IfCipherType,CDot11IfVlanIdOrZero,cd11IfAuxSsid=mibBuilder.importSymbols(_t,'CDot11IfCipherType','CDot11IfVlanIdOrZero',_u)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_R,_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_S)
ciscoDot11AssociationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,273))
if mibBuilder.loadTexts:ciscoDot11AssociationMIB.setRevisions(('2016-12-06 00:00','2007-01-05 00:00','2006-06-12 00:00','2005-03-08 00:00','2004-11-28 00:00','2004-10-18 00:00','2004-02-19 00:00','2003-07-27 00:00','2003-04-11 00:00','2003-01-29 00:00','2002-07-15 00:00','2002-04-17 00:00','2002-03-06 00:00'))
class CDot11ClientRoleClassType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('clientStation',0),('repeater',1),('accessPoint',2),('bridgeHost',3),('bridge',4),('bridgeRoot',5),(_v,6)))
class CDot11ClientDevType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,76,77,84,85,86,101,102,104,109,110,111,112,117,123,124,127,128,129,130,132,133,134,135,136,137,138,139,140)));namedValues=NamedValues(*((_w,1),('ethernetAP',76),('ethernetBridge',77),('pc3000Client',84),('serialUC',85),('ethernetUC',86),('pc3500Client',101),('pc4500Client',102),('generic80211Client',104),('pc4800Client',109),('pc3100Client',110),('mc',111),(_v,112),('pc4800bClient',117),('wgbNoDiversity',123),('wgb',124),('series350Client',127),('series370Client',128),('c1100SeriesAP',129),('c1410SeriesBridge',130),('c1200SeriesAP',132),('mp2xClient',133),('c350SeriesAP',134),('cb21agClient',135),('radioKodiak',136),('c1130SeriesAP',137),('c1310SeriesBridge',138),('c7920phone',139),('c1240SeriesAP',140)))
class CDot11ClientRadioType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,12,13,33,34,35,36,37,38,39,40,46)));namedValues=NamedValues(*((_w,1),('ccxClient',2),('pc3500',3),('pc3000',4),('pc4500',6),('pc4800',12),('pc3100',13),('series340',33),('series350',34),('series370',35),('bridge1410',36),('mp2xSeries',37),('rm2xSeries',38),('rm2gSeries',39),('mp2xMAR',40),('cb21ag',46)))
class CDot11AuthenticationMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,129)));namedValues=NamedValues(*(('open',1),('sharedKey',2),('networkEap',129)))
class CDot11AdditionalAuthenMethod(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('mac',0),('eap',1)))
class CDot11Dot1xAuthenMethod(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('md5',0),('leap',1),('peap',2),('eapTls',3),('eapSim',4),('eapFast',5)))
class CDot11KeyManagementMethod(TextualConvention,Bits):status=_E;namedValues=NamedValues(*(('wpa',0),('cckm',1)))
class CDot11NewKeyManagementMethod(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('cckm',0),('wpa1',1),('wpa2',2)))
_CiscoDot11AssocMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11AssocMIBObjects=_CiscoDot11AssocMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,273,1))
_CDot11AssociationGlobal_ObjectIdentity=ObjectIdentity
cDot11AssociationGlobal=_CDot11AssociationGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,273,1,1))
_CDot11ParentAddress_Type=MacAddress
_CDot11ParentAddress_Object=MibScalar
cDot11ParentAddress=_CDot11ParentAddress_Object((1,3,6,1,4,1,9,9,273,1,1,1),_CDot11ParentAddress_Type())
cDot11ParentAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ParentAddress.setStatus(_B)
_CDot11ActiveDevicesTable_Object=MibTable
cDot11ActiveDevicesTable=_CDot11ActiveDevicesTable_Object((1,3,6,1,4,1,9,9,273,1,1,2))
if mibBuilder.loadTexts:cDot11ActiveDevicesTable.setStatus(_B)
_CDot11ActiveDevicesEntry_Object=MibTableRow
cDot11ActiveDevicesEntry=_CDot11ActiveDevicesEntry_Object((1,3,6,1,4,1,9,9,273,1,1,2,1))
cDot11ActiveDevicesEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cDot11ActiveDevicesEntry.setStatus(_B)
class _CDot11ActiveWirelessClients_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2007))
_CDot11ActiveWirelessClients_Type.__name__=_R
_CDot11ActiveWirelessClients_Object=MibTableColumn
cDot11ActiveWirelessClients=_CDot11ActiveWirelessClients_Object((1,3,6,1,4,1,9,9,273,1,1,2,1,1),_CDot11ActiveWirelessClients_Type())
cDot11ActiveWirelessClients.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ActiveWirelessClients.setStatus(_B)
if mibBuilder.loadTexts:cDot11ActiveWirelessClients.setUnits(_W)
class _CDot11ActiveBridges_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2007))
_CDot11ActiveBridges_Type.__name__=_R
_CDot11ActiveBridges_Object=MibTableColumn
cDot11ActiveBridges=_CDot11ActiveBridges_Object((1,3,6,1,4,1,9,9,273,1,1,2,1,2),_CDot11ActiveBridges_Type())
cDot11ActiveBridges.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ActiveBridges.setStatus(_B)
if mibBuilder.loadTexts:cDot11ActiveBridges.setUnits(_W)
class _CDot11ActiveRepeaters_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2007))
_CDot11ActiveRepeaters_Type.__name__=_R
_CDot11ActiveRepeaters_Object=MibTableColumn
cDot11ActiveRepeaters=_CDot11ActiveRepeaters_Object((1,3,6,1,4,1,9,9,273,1,1,2,1,3),_CDot11ActiveRepeaters_Type())
cDot11ActiveRepeaters.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ActiveRepeaters.setStatus(_B)
if mibBuilder.loadTexts:cDot11ActiveRepeaters.setUnits(_W)
_CDot11AssociationStatsTable_Object=MibTable
cDot11AssociationStatsTable=_CDot11AssociationStatsTable_Object((1,3,6,1,4,1,9,9,273,1,1,3))
if mibBuilder.loadTexts:cDot11AssociationStatsTable.setStatus(_B)
_CDot11AssociationStatsEntry_Object=MibTableRow
cDot11AssociationStatsEntry=_CDot11AssociationStatsEntry_Object((1,3,6,1,4,1,9,9,273,1,1,3,1))
cDot11AssociationStatsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cDot11AssociationStatsEntry.setStatus(_B)
_CDot11AssStatsAssociated_Type=Counter32
_CDot11AssStatsAssociated_Object=MibTableColumn
cDot11AssStatsAssociated=_CDot11AssStatsAssociated_Object((1,3,6,1,4,1,9,9,273,1,1,3,1,1),_CDot11AssStatsAssociated_Type())
cDot11AssStatsAssociated.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11AssStatsAssociated.setStatus(_B)
if mibBuilder.loadTexts:cDot11AssStatsAssociated.setUnits(_L)
_CDot11AssStatsAuthenticated_Type=Counter32
_CDot11AssStatsAuthenticated_Object=MibTableColumn
cDot11AssStatsAuthenticated=_CDot11AssStatsAuthenticated_Object((1,3,6,1,4,1,9,9,273,1,1,3,1,2),_CDot11AssStatsAuthenticated_Type())
cDot11AssStatsAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11AssStatsAuthenticated.setStatus(_B)
if mibBuilder.loadTexts:cDot11AssStatsAuthenticated.setUnits(_L)
_CDot11AssStatsRoamedIn_Type=Counter32
_CDot11AssStatsRoamedIn_Object=MibTableColumn
cDot11AssStatsRoamedIn=_CDot11AssStatsRoamedIn_Object((1,3,6,1,4,1,9,9,273,1,1,3,1,3),_CDot11AssStatsRoamedIn_Type())
cDot11AssStatsRoamedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11AssStatsRoamedIn.setStatus(_B)
if mibBuilder.loadTexts:cDot11AssStatsRoamedIn.setUnits(_L)
_CDot11AssStatsRoamedAway_Type=Counter32
_CDot11AssStatsRoamedAway_Object=MibTableColumn
cDot11AssStatsRoamedAway=_CDot11AssStatsRoamedAway_Object((1,3,6,1,4,1,9,9,273,1,1,3,1,4),_CDot11AssStatsRoamedAway_Type())
cDot11AssStatsRoamedAway.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11AssStatsRoamedAway.setStatus(_B)
if mibBuilder.loadTexts:cDot11AssStatsRoamedAway.setUnits(_L)
_CDot11AssStatsDeauthenticated_Type=Counter32
_CDot11AssStatsDeauthenticated_Object=MibTableColumn
cDot11AssStatsDeauthenticated=_CDot11AssStatsDeauthenticated_Object((1,3,6,1,4,1,9,9,273,1,1,3,1,5),_CDot11AssStatsDeauthenticated_Type())
cDot11AssStatsDeauthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11AssStatsDeauthenticated.setStatus(_B)
if mibBuilder.loadTexts:cDot11AssStatsDeauthenticated.setUnits(_L)
_CDot11AssStatsDisassociated_Type=Counter32
_CDot11AssStatsDisassociated_Object=MibTableColumn
cDot11AssStatsDisassociated=_CDot11AssStatsDisassociated_Object((1,3,6,1,4,1,9,9,273,1,1,3,1,6),_CDot11AssStatsDisassociated_Type())
cDot11AssStatsDisassociated.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11AssStatsDisassociated.setStatus(_B)
if mibBuilder.loadTexts:cDot11AssStatsDisassociated.setUnits(_L)
_Cd11IfCipherStatsTable_Object=MibTable
cd11IfCipherStatsTable=_Cd11IfCipherStatsTable_Object((1,3,6,1,4,1,9,9,273,1,1,4))
if mibBuilder.loadTexts:cd11IfCipherStatsTable.setStatus(_B)
_Cd11IfCipherStatsEntry_Object=MibTableRow
cd11IfCipherStatsEntry=_Cd11IfCipherStatsEntry_Object((1,3,6,1,4,1,9,9,273,1,1,4,1))
cd11IfCipherStatsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cd11IfCipherStatsEntry.setStatus(_B)
_Cd11IfCipherMicFailClientAddress_Type=MacAddress
_Cd11IfCipherMicFailClientAddress_Object=MibTableColumn
cd11IfCipherMicFailClientAddress=_Cd11IfCipherMicFailClientAddress_Object((1,3,6,1,4,1,9,9,273,1,1,4,1,1),_Cd11IfCipherMicFailClientAddress_Type())
cd11IfCipherMicFailClientAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cd11IfCipherMicFailClientAddress.setStatus(_B)
_Cd11IfCipherTkipLocalMicFailures_Type=Counter32
_Cd11IfCipherTkipLocalMicFailures_Object=MibTableColumn
cd11IfCipherTkipLocalMicFailures=_Cd11IfCipherTkipLocalMicFailures_Object((1,3,6,1,4,1,9,9,273,1,1,4,1,2),_Cd11IfCipherTkipLocalMicFailures_Type())
cd11IfCipherTkipLocalMicFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cd11IfCipherTkipLocalMicFailures.setStatus(_B)
_Cd11IfCipherTkipRemotMicFailures_Type=Counter32
_Cd11IfCipherTkipRemotMicFailures_Object=MibTableColumn
cd11IfCipherTkipRemotMicFailures=_Cd11IfCipherTkipRemotMicFailures_Object((1,3,6,1,4,1,9,9,273,1,1,4,1,3),_Cd11IfCipherTkipRemotMicFailures_Type())
cd11IfCipherTkipRemotMicFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cd11IfCipherTkipRemotMicFailures.setStatus(_B)
_Cd11IfCipherTkipCounterMeasInvok_Type=Counter32
_Cd11IfCipherTkipCounterMeasInvok_Object=MibTableColumn
cd11IfCipherTkipCounterMeasInvok=_Cd11IfCipherTkipCounterMeasInvok_Object((1,3,6,1,4,1,9,9,273,1,1,4,1,4),_Cd11IfCipherTkipCounterMeasInvok_Type())
cd11IfCipherTkipCounterMeasInvok.setMaxAccess(_C)
if mibBuilder.loadTexts:cd11IfCipherTkipCounterMeasInvok.setStatus(_B)
_Cd11IfCipherCcmpReplaysDiscarded_Type=Counter32
_Cd11IfCipherCcmpReplaysDiscarded_Object=MibTableColumn
cd11IfCipherCcmpReplaysDiscarded=_Cd11IfCipherCcmpReplaysDiscarded_Object((1,3,6,1,4,1,9,9,273,1,1,4,1,5),_Cd11IfCipherCcmpReplaysDiscarded_Type())
cd11IfCipherCcmpReplaysDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:cd11IfCipherCcmpReplaysDiscarded.setStatus(_B)
_Cd11IfCipherTkipReplaysDetected_Type=Counter32
_Cd11IfCipherTkipReplaysDetected_Object=MibTableColumn
cd11IfCipherTkipReplaysDetected=_Cd11IfCipherTkipReplaysDetected_Object((1,3,6,1,4,1,9,9,273,1,1,4,1,6),_Cd11IfCipherTkipReplaysDetected_Type())
cd11IfCipherTkipReplaysDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:cd11IfCipherTkipReplaysDetected.setStatus(_B)
_CDot11ClientConfiguration_ObjectIdentity=ObjectIdentity
cDot11ClientConfiguration=_CDot11ClientConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,273,1,2))
_CDot11ClientConfigInfoTable_Object=MibTable
cDot11ClientConfigInfoTable=_CDot11ClientConfigInfoTable_Object((1,3,6,1,4,1,9,9,273,1,2,1))
if mibBuilder.loadTexts:cDot11ClientConfigInfoTable.setStatus(_B)
_CDot11ClientConfigInfoEntry_Object=MibTableRow
cDot11ClientConfigInfoEntry=_CDot11ClientConfigInfoEntry_Object((1,3,6,1,4,1,9,9,273,1,2,1,1))
cDot11ClientConfigInfoEntry.setIndexNames((0,_H,_I),(0,_t,_u),(0,_A,_x))
if mibBuilder.loadTexts:cDot11ClientConfigInfoEntry.setStatus(_B)
_CDot11ClientAddress_Type=MacAddress
_CDot11ClientAddress_Object=MibTableColumn
cDot11ClientAddress=_CDot11ClientAddress_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,1),_CDot11ClientAddress_Type())
cDot11ClientAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cDot11ClientAddress.setStatus(_B)
_CDot11ClientParentAddress_Type=MacAddress
_CDot11ClientParentAddress_Object=MibTableColumn
cDot11ClientParentAddress=_CDot11ClientParentAddress_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,2),_CDot11ClientParentAddress_Type())
cDot11ClientParentAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientParentAddress.setStatus(_B)
_CDot11ClientRoleClassType_Type=CDot11ClientRoleClassType
_CDot11ClientRoleClassType_Object=MibTableColumn
cDot11ClientRoleClassType=_CDot11ClientRoleClassType_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,3),_CDot11ClientRoleClassType_Type())
cDot11ClientRoleClassType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientRoleClassType.setStatus(_B)
_CDot11ClientDevType_Type=CDot11ClientDevType
_CDot11ClientDevType_Object=MibTableColumn
cDot11ClientDevType=_CDot11ClientDevType_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,4),_CDot11ClientDevType_Type())
cDot11ClientDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientDevType.setStatus(_B)
_CDot11ClientRadioType_Type=CDot11ClientRadioType
_CDot11ClientRadioType_Object=MibTableColumn
cDot11ClientRadioType=_CDot11ClientRadioType_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,5),_CDot11ClientRadioType_Type())
cDot11ClientRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientRadioType.setStatus(_B)
class _CDot11ClientWepEnabled_Type(TruthValue):defaultValue=2
_CDot11ClientWepEnabled_Type.__name__=_S
_CDot11ClientWepEnabled_Object=MibTableColumn
cDot11ClientWepEnabled=_CDot11ClientWepEnabled_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,6),_CDot11ClientWepEnabled_Type())
cDot11ClientWepEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientWepEnabled.setStatus(_B)
class _CDot11ClientWepKeyMixEnabled_Type(TruthValue):defaultValue=2
_CDot11ClientWepKeyMixEnabled_Type.__name__=_S
_CDot11ClientWepKeyMixEnabled_Object=MibTableColumn
cDot11ClientWepKeyMixEnabled=_CDot11ClientWepKeyMixEnabled_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,7),_CDot11ClientWepKeyMixEnabled_Type())
cDot11ClientWepKeyMixEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientWepKeyMixEnabled.setStatus(_B)
class _CDot11ClientMicEnabled_Type(TruthValue):defaultValue=2
_CDot11ClientMicEnabled_Type.__name__=_S
_CDot11ClientMicEnabled_Object=MibTableColumn
cDot11ClientMicEnabled=_CDot11ClientMicEnabled_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,8),_CDot11ClientMicEnabled_Type())
cDot11ClientMicEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientMicEnabled.setStatus(_B)
class _CDot11ClientPowerSaveMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('powersave',2)))
_CDot11ClientPowerSaveMode_Type.__name__=_P
_CDot11ClientPowerSaveMode_Object=MibTableColumn
cDot11ClientPowerSaveMode=_CDot11ClientPowerSaveMode_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,9),_CDot11ClientPowerSaveMode_Type())
cDot11ClientPowerSaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientPowerSaveMode.setStatus(_B)
class _CDot11ClientAid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2008))
_CDot11ClientAid_Type.__name__=_V
_CDot11ClientAid_Object=MibTableColumn
cDot11ClientAid=_CDot11ClientAid_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,10),_CDot11ClientAid_Type())
cDot11ClientAid.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientAid.setStatus(_B)
class _CDot11ClientDataRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_CDot11ClientDataRateSet_Type.__name__=_U
_CDot11ClientDataRateSet_Object=MibTableColumn
cDot11ClientDataRateSet=_CDot11ClientDataRateSet_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,11),_CDot11ClientDataRateSet_Type())
cDot11ClientDataRateSet.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientDataRateSet.setStatus(_B)
_CDot11ClientSoftwareVersion_Type=SnmpAdminString
_CDot11ClientSoftwareVersion_Object=MibTableColumn
cDot11ClientSoftwareVersion=_CDot11ClientSoftwareVersion_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,12),_CDot11ClientSoftwareVersion_Type())
cDot11ClientSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientSoftwareVersion.setStatus(_B)
_CDot11ClientName_Type=SnmpAdminString
_CDot11ClientName_Object=MibTableColumn
cDot11ClientName=_CDot11ClientName_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,13),_CDot11ClientName_Type())
cDot11ClientName.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientName.setStatus(_B)
class _CDot11ClientAssociationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initial',1),('authenNotAssociated',2),('assocAndAuthenticated',3),('assocNotAnuthenticated',4)))
_CDot11ClientAssociationState_Type.__name__=_P
_CDot11ClientAssociationState_Object=MibTableColumn
cDot11ClientAssociationState=_CDot11ClientAssociationState_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,14),_CDot11ClientAssociationState_Type())
cDot11ClientAssociationState.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientAssociationState.setStatus(_B)
_CDot11ClientIpAddressType_Type=InetAddressType
_CDot11ClientIpAddressType_Object=MibTableColumn
cDot11ClientIpAddressType=_CDot11ClientIpAddressType_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,15),_CDot11ClientIpAddressType_Type())
cDot11ClientIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientIpAddressType.setStatus(_B)
_CDot11ClientIpAddress_Type=InetAddress
_CDot11ClientIpAddress_Object=MibTableColumn
cDot11ClientIpAddress=_CDot11ClientIpAddress_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,16),_CDot11ClientIpAddress_Type())
cDot11ClientIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientIpAddress.setStatus(_B)
_CDot11ClientVlanId_Type=CDot11IfVlanIdOrZero
_CDot11ClientVlanId_Object=MibTableColumn
cDot11ClientVlanId=_CDot11ClientVlanId_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,17),_CDot11ClientVlanId_Type())
cDot11ClientVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientVlanId.setStatus(_B)
_CDot11ClientSubIfIndex_Type=InterfaceIndex
_CDot11ClientSubIfIndex_Object=MibTableColumn
cDot11ClientSubIfIndex=_CDot11ClientSubIfIndex_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,18),_CDot11ClientSubIfIndex_Type())
cDot11ClientSubIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientSubIfIndex.setStatus(_B)
_CDot11ClientAuthenAlgorithm_Type=CDot11AuthenticationMethod
_CDot11ClientAuthenAlgorithm_Object=MibTableColumn
cDot11ClientAuthenAlgorithm=_CDot11ClientAuthenAlgorithm_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,19),_CDot11ClientAuthenAlgorithm_Type())
cDot11ClientAuthenAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientAuthenAlgorithm.setStatus(_B)
_CDot11ClientAdditionalAuthen_Type=CDot11AdditionalAuthenMethod
_CDot11ClientAdditionalAuthen_Object=MibTableColumn
cDot11ClientAdditionalAuthen=_CDot11ClientAdditionalAuthen_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,20),_CDot11ClientAdditionalAuthen_Type())
cDot11ClientAdditionalAuthen.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientAdditionalAuthen.setStatus(_B)
_CDot11ClientDot1xAuthenAlgorithm_Type=CDot11Dot1xAuthenMethod
_CDot11ClientDot1xAuthenAlgorithm_Object=MibTableColumn
cDot11ClientDot1xAuthenAlgorithm=_CDot11ClientDot1xAuthenAlgorithm_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,21),_CDot11ClientDot1xAuthenAlgorithm_Type())
cDot11ClientDot1xAuthenAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientDot1xAuthenAlgorithm.setStatus(_B)
_CDot11ClientKeyManagement_Type=CDot11KeyManagementMethod
_CDot11ClientKeyManagement_Object=MibTableColumn
cDot11ClientKeyManagement=_CDot11ClientKeyManagement_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,22),_CDot11ClientKeyManagement_Type())
cDot11ClientKeyManagement.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientKeyManagement.setStatus(_E)
_CDot11ClientUnicastCipher_Type=CDot11IfCipherType
_CDot11ClientUnicastCipher_Object=MibTableColumn
cDot11ClientUnicastCipher=_CDot11ClientUnicastCipher_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,23),_CDot11ClientUnicastCipher_Type())
cDot11ClientUnicastCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientUnicastCipher.setStatus(_B)
_CDot11ClientMulticastCipher_Type=CDot11IfCipherType
_CDot11ClientMulticastCipher_Object=MibTableColumn
cDot11ClientMulticastCipher=_CDot11ClientMulticastCipher_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,24),_CDot11ClientMulticastCipher_Type())
cDot11ClientMulticastCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientMulticastCipher.setStatus(_B)
_CDot11ClientDevObjectID_Type=ObjectIdentifier
_CDot11ClientDevObjectID_Object=MibTableColumn
cDot11ClientDevObjectID=_CDot11ClientDevObjectID_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,25),_CDot11ClientDevObjectID_Type())
cDot11ClientDevObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientDevObjectID.setStatus(_B)
_CDot11ClientNewKeyManagement_Type=CDot11NewKeyManagementMethod
_CDot11ClientNewKeyManagement_Object=MibTableColumn
cDot11ClientNewKeyManagement=_CDot11ClientNewKeyManagement_Object((1,3,6,1,4,1,9,9,273,1,2,1,1,26),_CDot11ClientNewKeyManagement_Type())
cDot11ClientNewKeyManagement.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientNewKeyManagement.setStatus(_B)
_CDot11ClientStatistics_ObjectIdentity=ObjectIdentity
cDot11ClientStatistics=_CDot11ClientStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,273,1,3))
_CDot11ClientStatisticTable_Object=MibTable
cDot11ClientStatisticTable=_CDot11ClientStatisticTable_Object((1,3,6,1,4,1,9,9,273,1,3,1))
if mibBuilder.loadTexts:cDot11ClientStatisticTable.setStatus(_B)
_CDot11ClientStatisticEntry_Object=MibTableRow
cDot11ClientStatisticEntry=_CDot11ClientStatisticEntry_Object((1,3,6,1,4,1,9,9,273,1,3,1,1))
if mibBuilder.loadTexts:cDot11ClientStatisticEntry.setStatus(_B)
class _CDot11ClientCurrentTxRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_CDot11ClientCurrentTxRateSet_Type.__name__=_U
_CDot11ClientCurrentTxRateSet_Object=MibTableColumn
cDot11ClientCurrentTxRateSet=_CDot11ClientCurrentTxRateSet_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,1),_CDot11ClientCurrentTxRateSet_Type())
cDot11ClientCurrentTxRateSet.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientCurrentTxRateSet.setStatus(_B)
_CDot11ClientUpTime_Type=Unsigned32
_CDot11ClientUpTime_Object=MibTableColumn
cDot11ClientUpTime=_CDot11ClientUpTime_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,2),_CDot11ClientUpTime_Type())
cDot11ClientUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientUpTime.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientUpTime.setUnits(_y)
class _CDot11ClientSignalStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,0))
_CDot11ClientSignalStrength_Type.__name__=_P
_CDot11ClientSignalStrength_Object=MibTableColumn
cDot11ClientSignalStrength=_CDot11ClientSignalStrength_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,3),_CDot11ClientSignalStrength_Type())
cDot11ClientSignalStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientSignalStrength.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientSignalStrength.setUnits('dBm')
class _CDot11ClientSigQuality_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CDot11ClientSigQuality_Type.__name__=_V
_CDot11ClientSigQuality_Object=MibTableColumn
cDot11ClientSigQuality=_CDot11ClientSigQuality_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,4),_CDot11ClientSigQuality_Type())
cDot11ClientSigQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientSigQuality.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientSigQuality.setUnits('percentage')
_CDot11ClientAgingLeft_Type=Gauge32
_CDot11ClientAgingLeft_Object=MibTableColumn
cDot11ClientAgingLeft=_CDot11ClientAgingLeft_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,5),_CDot11ClientAgingLeft_Type())
cDot11ClientAgingLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientAgingLeft.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientAgingLeft.setUnits(_y)
_CDot11ClientPacketsReceived_Type=Counter32
_CDot11ClientPacketsReceived_Object=MibTableColumn
cDot11ClientPacketsReceived=_CDot11ClientPacketsReceived_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,6),_CDot11ClientPacketsReceived_Type())
cDot11ClientPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientPacketsReceived.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientPacketsReceived.setUnits(_J)
_CDot11ClientBytesReceived_Type=Counter32
_CDot11ClientBytesReceived_Object=MibTableColumn
cDot11ClientBytesReceived=_CDot11ClientBytesReceived_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,7),_CDot11ClientBytesReceived_Type())
cDot11ClientBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientBytesReceived.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientBytesReceived.setUnits('byte')
_CDot11ClientPacketsSent_Type=Counter32
_CDot11ClientPacketsSent_Object=MibTableColumn
cDot11ClientPacketsSent=_CDot11ClientPacketsSent_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,8),_CDot11ClientPacketsSent_Type())
cDot11ClientPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientPacketsSent.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientPacketsSent.setUnits(_J)
_CDot11ClientBytesSent_Type=Counter32
_CDot11ClientBytesSent_Object=MibTableColumn
cDot11ClientBytesSent=_CDot11ClientBytesSent_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,9),_CDot11ClientBytesSent_Type())
cDot11ClientBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientBytesSent.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientBytesSent.setUnits('byte')
_CDot11ClientDuplicates_Type=Counter32
_CDot11ClientDuplicates_Object=MibTableColumn
cDot11ClientDuplicates=_CDot11ClientDuplicates_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,10),_CDot11ClientDuplicates_Type())
cDot11ClientDuplicates.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientDuplicates.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientDuplicates.setUnits(_J)
_CDot11ClientMsduRetries_Type=Counter32
_CDot11ClientMsduRetries_Object=MibTableColumn
cDot11ClientMsduRetries=_CDot11ClientMsduRetries_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,11),_CDot11ClientMsduRetries_Type())
cDot11ClientMsduRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientMsduRetries.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientMsduRetries.setUnits(_J)
_CDot11ClientMsduFails_Type=Counter32
_CDot11ClientMsduFails_Object=MibTableColumn
cDot11ClientMsduFails=_CDot11ClientMsduFails_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,12),_CDot11ClientMsduFails_Type())
cDot11ClientMsduFails.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientMsduFails.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientMsduFails.setUnits(_J)
_CDot11ClientWepErrors_Type=Counter32
_CDot11ClientWepErrors_Object=MibTableColumn
cDot11ClientWepErrors=_CDot11ClientWepErrors_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,13),_CDot11ClientWepErrors_Type())
cDot11ClientWepErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientWepErrors.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientWepErrors.setUnits(_J)
_CDot11ClientMicErrors_Type=Counter32
_CDot11ClientMicErrors_Object=MibTableColumn
cDot11ClientMicErrors=_CDot11ClientMicErrors_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,14),_CDot11ClientMicErrors_Type())
cDot11ClientMicErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientMicErrors.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientMicErrors.setUnits('error')
_CDot11ClientMicMissingFrames_Type=Counter32
_CDot11ClientMicMissingFrames_Object=MibTableColumn
cDot11ClientMicMissingFrames=_CDot11ClientMicMissingFrames_Object((1,3,6,1,4,1,9,9,273,1,3,1,1,15),_CDot11ClientMicMissingFrames_Type())
cDot11ClientMicMissingFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11ClientMicMissingFrames.setStatus(_B)
if mibBuilder.loadTexts:cDot11ClientMicMissingFrames.setUnits(_J)
_CiscoDot11StationTraps_ObjectIdentity=ObjectIdentity
ciscoDot11StationTraps=_CiscoDot11StationTraps_ObjectIdentity((1,3,6,1,4,1,9,9,273,1,4))
_CiscoDot11StationInfoTable_Object=MibTable
ciscoDot11StationInfoTable=_CiscoDot11StationInfoTable_Object((1,3,6,1,4,1,9,9,273,1,5))
if mibBuilder.loadTexts:ciscoDot11StationInfoTable.setStatus(_B)
_CiscoDot11StationInfoEntry_Object=MibTableRow
ciscoDot11StationInfoEntry=_CiscoDot11StationInfoEntry_Object((1,3,6,1,4,1,9,9,273,1,5,1))
ciscoDot11StationInfoEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ciscoDot11StationInfoEntry.setStatus(_B)
_ClientMacAddr_Type=MacAddress
_ClientMacAddr_Object=MibTableColumn
clientMacAddr=_ClientMacAddr_Object((1,3,6,1,4,1,9,9,273,1,5,1,1),_ClientMacAddr_Type())
clientMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:clientMacAddr.setStatus(_B)
_ClientDeviceType_Type=CDot11ClientRoleClassType
_ClientDeviceType_Object=MibTableColumn
clientDeviceType=_ClientDeviceType_Object((1,3,6,1,4,1,9,9,273,1,5,1,2),_ClientDeviceType_Type())
clientDeviceType.setMaxAccess(_D)
if mibBuilder.loadTexts:clientDeviceType.setStatus(_B)
_ClientDeviceName_Type=SnmpAdminString
_ClientDeviceName_Object=MibTableColumn
clientDeviceName=_ClientDeviceName_Object((1,3,6,1,4,1,9,9,273,1,5,1,3),_ClientDeviceName_Type())
clientDeviceName.setMaxAccess(_D)
if mibBuilder.loadTexts:clientDeviceName.setStatus(_B)
_ClientIpv4Address_Type=InetAddress
_ClientIpv4Address_Object=MibTableColumn
clientIpv4Address=_ClientIpv4Address_Object((1,3,6,1,4,1,9,9,273,1,5,1,4),_ClientIpv4Address_Type())
clientIpv4Address.setMaxAccess(_D)
if mibBuilder.loadTexts:clientIpv4Address.setStatus(_B)
_ClientIpv6Address_Type=InetAddress
_ClientIpv6Address_Object=MibTableColumn
clientIpv6Address=_ClientIpv6Address_Object((1,3,6,1,4,1,9,9,273,1,5,1,5),_ClientIpv6Address_Type())
clientIpv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:clientIpv6Address.setStatus(_B)
_ApMacAddr_Type=InetAddress
_ApMacAddr_Object=MibTableColumn
apMacAddr=_ApMacAddr_Object((1,3,6,1,4,1,9,9,273,1,5,1,6),_ApMacAddr_Type())
apMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:apMacAddr.setStatus(_B)
_ApIpv4Address_Type=InetAddress
_ApIpv4Address_Object=MibTableColumn
apIpv4Address=_ApIpv4Address_Object((1,3,6,1,4,1,9,9,273,1,5,1,7),_ApIpv4Address_Type())
apIpv4Address.setMaxAccess(_D)
if mibBuilder.loadTexts:apIpv4Address.setStatus(_B)
_ApIpv6Address_Type=InetAddress
_ApIpv6Address_Object=MibTableColumn
apIpv6Address=_ApIpv6Address_Object((1,3,6,1,4,1,9,9,273,1,5,1,8),_ApIpv6Address_Type())
apIpv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:apIpv6Address.setStatus(_B)
class _ClientStationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('associated',1),('disAssociated',2),('run',3)))
_ClientStationState_Type.__name__=_P
_ClientStationState_Object=MibTableColumn
clientStationState=_ClientStationState_Object((1,3,6,1,4,1,9,9,273,1,5,1,9),_ClientStationState_Type())
clientStationState.setMaxAccess(_D)
if mibBuilder.loadTexts:clientStationState.setStatus(_B)
_ClientDisassocReasonStr_Type=SnmpAdminString
_ClientDisassocReasonStr_Object=MibTableColumn
clientDisassocReasonStr=_ClientDisassocReasonStr_Object((1,3,6,1,4,1,9,9,273,1,5,1,10),_ClientDisassocReasonStr_Type())
clientDisassocReasonStr.setMaxAccess(_D)
if mibBuilder.loadTexts:clientDisassocReasonStr.setStatus(_B)
_CiscoDot11AssocMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDot11AssocMIBConformance=_CiscoDot11AssocMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,273,2))
_CiscoDot11AssocMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11AssocMIBCompliances=_CiscoDot11AssocMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,273,2,1))
_CiscoDot11AssocMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11AssocMIBGroups=_CiscoDot11AssocMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,273,2,2))
cDot11ClientConfigInfoEntry.registerAugmentions((_A,_z))
cDot11ClientStatisticEntry.setIndexNames(*cDot11ClientConfigInfoEntry.getIndexNames())
ciscoDot11AssocGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,1))
ciscoDot11AssocGlobalGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoDot11AssocGlobalGroup.setStatus(_E)
ciscoDot11ClientConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,2))
ciscoDot11ClientConfigGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ciscoDot11ClientConfigGroup.setStatus(_B)
ciscoDot11ClientStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,3))
ciscoDot11ClientStatGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:ciscoDot11ClientStatGroup.setStatus(_B)
ciscoDot11ClientInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,4))
ciscoDot11ClientInfoGroup.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:ciscoDot11ClientInfoGroup.setStatus(_B)
ciscoDot11ApAssocGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,5))
ciscoDot11ApAssocGlobalGroup.setObjects((_A,_X))
if mibBuilder.loadTexts:ciscoDot11ApAssocGlobalGroup.setStatus(_B)
ciscoDot11IfAssocStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,6))
ciscoDot11IfAssocStatGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoDot11IfAssocStatGroup.setStatus(_B)
ciscoDot11IfCipherStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,7))
ciscoDot11IfCipherStatGroup.setObjects(*((_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:ciscoDot11IfCipherStatGroup.setStatus(_B)
ciscoDot11ClientAuthenGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,8))
ciscoDot11ClientAuthenGroup.setObjects(*((_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:ciscoDot11ClientAuthenGroup.setStatus(_E)
ciscoDot11ClientConfigExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,9))
ciscoDot11ClientConfigExtGroup.setObjects((_A,_Ai))
if mibBuilder.loadTexts:ciscoDot11ClientConfigExtGroup.setStatus(_B)
ciscoDot11ClientNewAuthenGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,10))
ciscoDot11ClientNewAuthenGroup.setObjects((_A,_Aj))
if mibBuilder.loadTexts:ciscoDot11ClientNewAuthenGroup.setStatus(_B)
ciscoDot11ClientStatusTrapsGroup=ObjectGroup((1,3,6,1,4,1,9,9,273,2,2,11))
ciscoDot11ClientStatusTrapsGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoDot11ClientStatusTrapsGroup.setStatus(_B)
ciscoDot11StationStatusTrap=NotificationType((1,3,6,1,4,1,9,9,273,1,4,1))
ciscoDot11StationStatusTrap.setObjects(*((_H,_I),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoDot11StationStatusTrap.setStatus(_B)
ciscoDot11AssocMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,273,2,1,1))
ciscoDot11AssocMIBCompliance.setObjects(*((_A,_r),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ciscoDot11AssocMIBCompliance.setStatus(_E)
ciscoDot11AssocMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,273,2,1,2))
ciscoDot11AssocMIBComplianceRev1.setObjects(*((_A,_r),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:ciscoDot11AssocMIBComplianceRev1.setStatus(_E)
ciscoDot11AssocMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,273,2,1,3))
ciscoDot11AssocMIBComplianceRev2.setObjects(*((_A,_F),(_A,_G),(_A,_K),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoDot11AssocMIBComplianceRev2.setStatus(_E)
ciscoDot11AssocMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,273,2,1,4))
ciscoDot11AssocMIBComplianceRev3.setObjects(*((_A,_F),(_A,_Q),(_A,_G),(_A,_K),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoDot11AssocMIBComplianceRev3.setStatus(_E)
ciscoDot11AssocMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,273,2,1,5))
ciscoDot11AssocMIBComplianceRev4.setObjects(*((_A,_F),(_A,_Q),(_A,_G),(_A,_K),(_A,_M),(_A,_N),(_A,_T),(_A,_O)))
if mibBuilder.loadTexts:ciscoDot11AssocMIBComplianceRev4.setStatus(_B)
ciscoDot11AssocMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,273,2,1,6))
ciscoDot11AssocMIBComplianceRev5.setObjects(*((_A,_F),(_A,_Q),(_A,_G),(_A,_K),(_A,_M),(_A,_N),(_A,_T),(_A,_s),(_A,_O)))
if mibBuilder.loadTexts:ciscoDot11AssocMIBComplianceRev5.setStatus(_B)
ciscoDot11AssocMIBComplianceRev6=ModuleCompliance((1,3,6,1,4,1,9,9,273,2,1,7))
ciscoDot11AssocMIBComplianceRev6.setObjects(*((_A,_F),(_A,_Q),(_A,_G),(_A,_K),(_A,_M),(_A,_N),(_A,_T),(_A,_s),(_A,_O),(_A,_Ak)))
if mibBuilder.loadTexts:ciscoDot11AssocMIBComplianceRev6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CDot11ClientRoleClassType':CDot11ClientRoleClassType,'CDot11ClientDevType':CDot11ClientDevType,'CDot11ClientRadioType':CDot11ClientRadioType,'CDot11AuthenticationMethod':CDot11AuthenticationMethod,'CDot11AdditionalAuthenMethod':CDot11AdditionalAuthenMethod,'CDot11Dot1xAuthenMethod':CDot11Dot1xAuthenMethod,'CDot11KeyManagementMethod':CDot11KeyManagementMethod,'CDot11NewKeyManagementMethod':CDot11NewKeyManagementMethod,'ciscoDot11AssociationMIB':ciscoDot11AssociationMIB,'ciscoDot11AssocMIBObjects':ciscoDot11AssocMIBObjects,'cDot11AssociationGlobal':cDot11AssociationGlobal,_X:cDot11ParentAddress,'cDot11ActiveDevicesTable':cDot11ActiveDevicesTable,'cDot11ActiveDevicesEntry':cDot11ActiveDevicesEntry,_Y:cDot11ActiveWirelessClients,_Z:cDot11ActiveBridges,_a:cDot11ActiveRepeaters,'cDot11AssociationStatsTable':cDot11AssociationStatsTable,'cDot11AssociationStatsEntry':cDot11AssociationStatsEntry,_b:cDot11AssStatsAssociated,_c:cDot11AssStatsAuthenticated,_d:cDot11AssStatsRoamedIn,_e:cDot11AssStatsRoamedAway,_f:cDot11AssStatsDeauthenticated,_g:cDot11AssStatsDisassociated,'cd11IfCipherStatsTable':cd11IfCipherStatsTable,'cd11IfCipherStatsEntry':cd11IfCipherStatsEntry,_AU:cd11IfCipherMicFailClientAddress,_AV:cd11IfCipherTkipLocalMicFailures,_AW:cd11IfCipherTkipRemotMicFailures,_AX:cd11IfCipherTkipCounterMeasInvok,_AY:cd11IfCipherCcmpReplaysDiscarded,_AZ:cd11IfCipherTkipReplaysDetected,'cDot11ClientConfiguration':cDot11ClientConfiguration,'cDot11ClientConfigInfoTable':cDot11ClientConfigInfoTable,'cDot11ClientConfigInfoEntry':cDot11ClientConfigInfoEntry,_x:cDot11ClientAddress,_A0:cDot11ClientParentAddress,_A1:cDot11ClientRoleClassType,_A2:cDot11ClientDevType,_A3:cDot11ClientRadioType,_A4:cDot11ClientWepEnabled,_A5:cDot11ClientWepKeyMixEnabled,_A6:cDot11ClientMicEnabled,_A7:cDot11ClientPowerSaveMode,_A8:cDot11ClientAid,_A9:cDot11ClientDataRateSet,_AP:cDot11ClientSoftwareVersion,_AQ:cDot11ClientName,_AR:cDot11ClientAssociationState,_AS:cDot11ClientIpAddressType,_AT:cDot11ClientIpAddress,_Aa:cDot11ClientVlanId,_Ab:cDot11ClientSubIfIndex,_Ac:cDot11ClientAuthenAlgorithm,_Ad:cDot11ClientAdditionalAuthen,_Ae:cDot11ClientDot1xAuthenAlgorithm,_Af:cDot11ClientKeyManagement,_Ag:cDot11ClientUnicastCipher,_Ah:cDot11ClientMulticastCipher,_Ai:cDot11ClientDevObjectID,_Aj:cDot11ClientNewKeyManagement,'cDot11ClientStatistics':cDot11ClientStatistics,'cDot11ClientStatisticTable':cDot11ClientStatisticTable,_z:cDot11ClientStatisticEntry,_AA:cDot11ClientCurrentTxRateSet,_AB:cDot11ClientUpTime,_AC:cDot11ClientSignalStrength,_AD:cDot11ClientSigQuality,_AI:cDot11ClientAgingLeft,_AE:cDot11ClientPacketsReceived,_AF:cDot11ClientBytesReceived,_AG:cDot11ClientPacketsSent,_AH:cDot11ClientBytesSent,_AJ:cDot11ClientDuplicates,_AK:cDot11ClientMsduRetries,_AL:cDot11ClientMsduFails,_AM:cDot11ClientWepErrors,_AN:cDot11ClientMicErrors,_AO:cDot11ClientMicMissingFrames,'ciscoDot11StationTraps':ciscoDot11StationTraps,'ciscoDot11StationStatusTrap':ciscoDot11StationStatusTrap,'ciscoDot11StationInfoTable':ciscoDot11StationInfoTable,'ciscoDot11StationInfoEntry':ciscoDot11StationInfoEntry,_h:clientMacAddr,_i:clientDeviceType,_j:clientDeviceName,_k:clientIpv4Address,_l:clientIpv6Address,_m:apMacAddr,_n:apIpv4Address,_o:apIpv6Address,_p:clientStationState,_q:clientDisassocReasonStr,'ciscoDot11AssocMIBConformance':ciscoDot11AssocMIBConformance,'ciscoDot11AssocMIBCompliances':ciscoDot11AssocMIBCompliances,'ciscoDot11AssocMIBCompliance':ciscoDot11AssocMIBCompliance,'ciscoDot11AssocMIBComplianceRev1':ciscoDot11AssocMIBComplianceRev1,'ciscoDot11AssocMIBComplianceRev2':ciscoDot11AssocMIBComplianceRev2,'ciscoDot11AssocMIBComplianceRev3':ciscoDot11AssocMIBComplianceRev3,'ciscoDot11AssocMIBComplianceRev4':ciscoDot11AssocMIBComplianceRev4,'ciscoDot11AssocMIBComplianceRev5':ciscoDot11AssocMIBComplianceRev5,'ciscoDot11AssocMIBComplianceRev6':ciscoDot11AssocMIBComplianceRev6,'ciscoDot11AssocMIBGroups':ciscoDot11AssocMIBGroups,_r:ciscoDot11AssocGlobalGroup,_F:ciscoDot11ClientConfigGroup,_G:ciscoDot11ClientStatGroup,_K:ciscoDot11ClientInfoGroup,_O:ciscoDot11ApAssocGlobalGroup,_M:ciscoDot11IfAssocStatGroup,_N:ciscoDot11IfCipherStatGroup,_Q:ciscoDot11ClientAuthenGroup,_T:ciscoDot11ClientConfigExtGroup,_s:ciscoDot11ClientNewAuthenGroup,_Ak:ciscoDot11ClientStatusTrapsGroup})