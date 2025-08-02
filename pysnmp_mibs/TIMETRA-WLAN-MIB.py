_AA='tmnxWlanOperGroup'
_A9='tmnxWlanConfigGroup'
_A8='tmnxWlanRadioOperCentreFreq'
_A7='tmnxWlanAPClientAuthorized'
_A6='tmnxWlanAPClientConnectTime'
_A5='tmnxWlanRadioOperFreqBand'
_A4='tmnxWlanRadioOperChannel'
_A3='tmnxWlanRadioOperChBandwidth'
_A2='tmnxWlanRadioOperStatus'
_A1='tmnxWlanAPTotalAuthFails'
_A0='tmnxWlanAPTotalAuthSuccess'
_z='tmnxWlanAPTotalDetaches'
_y='tmnxWlanAPTotalAttaches'
_x='tmnxWlanAPConnectedClients'
_w='tmnxWlanRadioApBeaconInterval'
_v='tmnxWlanRadioCfgFreqBand'
_u='tmnxWlanRadioCountry'
_t='tmnxWlanRadioCfgChannel'
_s='tmnxWlanRadioCfgChBandwidth'
_r='tmnxWlanRadioAdminStatus'
_q='tmnxWlanRadioType'
_p='tmnxWlanAPDhcpAdminState'
_o='tmnxWlanAPDot1xReauthPeriod'
_n='tmnxWlanAPDot1xRadiusPlcy'
_m='tmnxWlanAPClientTimeout'
_l='tmnxWlanAPClientLimit'
_k='tmnxWlanAPBroadcastSSID'
_j='tmnxWlanNetworkWpaPassphrase'
_i='tmnxWlanNetworkWpaEncryption'
_h='tmnxWlanNetworkSecurity'
_g='tmnxWlanNetworkSSID'
_f='tmnxWlanNetworkRowStatus'
_e='tmnxWlanPortOperFlags'
_d='tmnxWlanPortRadio'
_c='tmnxWlanPortMode'
_b='tmnxWlanNetworkSecurityEntry'
_a='tmnxWlanAPClientMacAddress'
_Z='TmnxWlanRadioChBandwidth'
_Y='TmnxWlanRadioFreqBand'
_X='TmnxWlanRadioAdminStatus'
_W='seconds'
_V='TmnxWlanWpaPassphrase'
_U='read-create'
_T='tmnxWlanNetworkId'
_S='TmnxAdminState'
_R='TPolicyStatementNameOrEmpty'
_Q='TruthValue'
_P='tmnxMDARadioNum'
_O='none'
_N='not-accessible'
_M='tmnxMDASlotNum'
_L='tmnxChassisIndex'
_K='tmnxCardSlotNum'
_J='unknown'
_I='Integer32'
_H='tmnxPortPortID'
_G='TIMETRA-PORT-MIB'
_F='Unsigned32'
_E='TIMETRA-CHASSIS-MIB'
_D='read-write'
_C='read-only'
_B='TIMETRA-WLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_Q)
tmnxCardSlotNum,tmnxChassisIndex,tmnxMDASlotNum=mibBuilder.importSymbols(_E,_K,_L,_M)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
tmnxPortPortID,=mibBuilder.importSymbols(_G,_H)
TPolicyStatementNameOrEmpty,TmnxAdminState=mibBuilder.importSymbols('TIMETRA-TC-MIB',_R,_S)
timetraWlanMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,117))
if mibBuilder.loadTexts:timetraWlanMIBModule.setRevisions(('2017-07-18 00:00',))
class TmnxWlanNetworkId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
class TmnxWlanSSID(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class TmnxWlanWpaPassphrase(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,63))
class TmnxWlanRadioType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('dualbandWifi',1)))
class TmnxWlanRadioAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inService',1),('outOfService',2)))
class TmnxWlanRadioOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('down',1),('scanning',2),('up',3)))
class TmnxWlanRadioFreqBand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('band24Ghz',1),('band50Ghz',2)))
class TmnxWlanRadioChBandwidth(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('width20mhz',1),('width40mhz',2)))
_TmnxWlanConformance_ObjectIdentity=ObjectIdentity
tmnxWlanConformance=_TmnxWlanConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,117))
_TmnxWlanCompliances_ObjectIdentity=ObjectIdentity
tmnxWlanCompliances=_TmnxWlanCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,117,1))
_TmnxWlanGroups_ObjectIdentity=ObjectIdentity
tmnxWlanGroups=_TmnxWlanGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,117,2))
_TmnxWlanV15v0Groups_ObjectIdentity=ObjectIdentity
tmnxWlanV15v0Groups=_TmnxWlanV15v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,117,2,1))
_TmnxWlanV20Groups_ObjectIdentity=ObjectIdentity
tmnxWlanV20Groups=_TmnxWlanV20Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,117,2,2))
_TmnxWlanObjs_ObjectIdentity=ObjectIdentity
tmnxWlanObjs=_TmnxWlanObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,117))
_TmnxWlanConfigObjs_ObjectIdentity=ObjectIdentity
tmnxWlanConfigObjs=_TmnxWlanConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,117,2))
_TmnxWlanPortConfigObjs_ObjectIdentity=ObjectIdentity
tmnxWlanPortConfigObjs=_TmnxWlanPortConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,117,2,1))
_TmnxWlanPortTable_Object=MibTable
tmnxWlanPortTable=_TmnxWlanPortTable_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,1))
if mibBuilder.loadTexts:tmnxWlanPortTable.setStatus(_A)
_TmnxWlanPortEntry_Object=MibTableRow
tmnxWlanPortEntry=_TmnxWlanPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,1,1))
tmnxWlanPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tmnxWlanPortEntry.setStatus(_A)
class _TmnxWlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('access-point',1),('reserved2',2)))
_TmnxWlanPortMode_Type.__name__=_I
_TmnxWlanPortMode_Object=MibTableColumn
tmnxWlanPortMode=_TmnxWlanPortMode_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,1,1,1),_TmnxWlanPortMode_Type())
tmnxWlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanPortMode.setStatus(_A)
_TmnxWlanPortRadio_Type=Unsigned32
_TmnxWlanPortRadio_Object=MibTableColumn
tmnxWlanPortRadio=_TmnxWlanPortRadio_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,1,1,2),_TmnxWlanPortRadio_Type())
tmnxWlanPortRadio.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanPortRadio.setStatus(_A)
class _TmnxWlanPortOperFlags_Type(Bits):namedValues=NamedValues(*(('adminDown',0),('rfAdminDown',1),('rfChNotLocked',2),('noRadiusPlcyCfg',3),('dot1xDisabled',4),('radiusPlcyDisabled',5),('noRadiusAuthSvr',6),('noNasIpAddr',7)))
_TmnxWlanPortOperFlags_Type.__name__='Bits'
_TmnxWlanPortOperFlags_Object=MibTableColumn
tmnxWlanPortOperFlags=_TmnxWlanPortOperFlags_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,1,1,3),_TmnxWlanPortOperFlags_Type())
tmnxWlanPortOperFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanPortOperFlags.setStatus(_A)
_TmnxWlanNetworkTable_Object=MibTable
tmnxWlanNetworkTable=_TmnxWlanNetworkTable_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,2))
if mibBuilder.loadTexts:tmnxWlanNetworkTable.setStatus(_A)
_TmnxWlanNetworkEntry_Object=MibTableRow
tmnxWlanNetworkEntry=_TmnxWlanNetworkEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,2,1))
tmnxWlanNetworkEntry.setIndexNames((0,_G,_H),(0,_B,_T))
if mibBuilder.loadTexts:tmnxWlanNetworkEntry.setStatus(_A)
_TmnxWlanNetworkId_Type=TmnxWlanNetworkId
_TmnxWlanNetworkId_Object=MibTableColumn
tmnxWlanNetworkId=_TmnxWlanNetworkId_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,2,1,1),_TmnxWlanNetworkId_Type())
tmnxWlanNetworkId.setMaxAccess(_N)
if mibBuilder.loadTexts:tmnxWlanNetworkId.setStatus(_A)
_TmnxWlanNetworkRowStatus_Type=RowStatus
_TmnxWlanNetworkRowStatus_Object=MibTableColumn
tmnxWlanNetworkRowStatus=_TmnxWlanNetworkRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,2,1,2),_TmnxWlanNetworkRowStatus_Type())
tmnxWlanNetworkRowStatus.setMaxAccess(_U)
if mibBuilder.loadTexts:tmnxWlanNetworkRowStatus.setStatus(_A)
_TmnxWlanNetworkSSID_Type=TmnxWlanSSID
_TmnxWlanNetworkSSID_Object=MibTableColumn
tmnxWlanNetworkSSID=_TmnxWlanNetworkSSID_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,2,1,3),_TmnxWlanNetworkSSID_Type())
tmnxWlanNetworkSSID.setMaxAccess(_U)
if mibBuilder.loadTexts:tmnxWlanNetworkSSID.setStatus(_A)
_TmnxWlanNetworkSecurityTable_Object=MibTable
tmnxWlanNetworkSecurityTable=_TmnxWlanNetworkSecurityTable_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,3))
if mibBuilder.loadTexts:tmnxWlanNetworkSecurityTable.setStatus(_A)
_TmnxWlanNetworkSecurityEntry_Object=MibTableRow
tmnxWlanNetworkSecurityEntry=_TmnxWlanNetworkSecurityEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,3,1))
if mibBuilder.loadTexts:tmnxWlanNetworkSecurityEntry.setStatus(_A)
class _TmnxWlanNetworkSecurity_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('wpa2-psk',1),('wpa2-enterprise',2)))
_TmnxWlanNetworkSecurity_Type.__name__=_I
_TmnxWlanNetworkSecurity_Object=MibTableColumn
tmnxWlanNetworkSecurity=_TmnxWlanNetworkSecurity_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,3,1,1),_TmnxWlanNetworkSecurity_Type())
tmnxWlanNetworkSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanNetworkSecurity.setStatus(_A)
class _TmnxWlanNetworkWpaEncryption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('aes',1),('tkip',2)))
_TmnxWlanNetworkWpaEncryption_Type.__name__=_I
_TmnxWlanNetworkWpaEncryption_Object=MibTableColumn
tmnxWlanNetworkWpaEncryption=_TmnxWlanNetworkWpaEncryption_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,3,1,2),_TmnxWlanNetworkWpaEncryption_Type())
tmnxWlanNetworkWpaEncryption.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanNetworkWpaEncryption.setStatus(_A)
class _TmnxWlanNetworkWpaPassphrase_Type(TmnxWlanWpaPassphrase):defaultValue=OctetString('')
_TmnxWlanNetworkWpaPassphrase_Type.__name__=_V
_TmnxWlanNetworkWpaPassphrase_Object=MibTableColumn
tmnxWlanNetworkWpaPassphrase=_TmnxWlanNetworkWpaPassphrase_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,3,1,3),_TmnxWlanNetworkWpaPassphrase_Type())
tmnxWlanNetworkWpaPassphrase.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanNetworkWpaPassphrase.setStatus(_A)
_TmnxWlanAPTable_Object=MibTable
tmnxWlanAPTable=_TmnxWlanAPTable_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4))
if mibBuilder.loadTexts:tmnxWlanAPTable.setStatus(_A)
_TmnxWlanAPEntry_Object=MibTableRow
tmnxWlanAPEntry=_TmnxWlanAPEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4,1))
tmnxWlanAPEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tmnxWlanAPEntry.setStatus(_A)
class _TmnxWlanAPBroadcastSSID_Type(TruthValue):defaultValue=1
_TmnxWlanAPBroadcastSSID_Type.__name__=_Q
_TmnxWlanAPBroadcastSSID_Object=MibTableColumn
tmnxWlanAPBroadcastSSID=_TmnxWlanAPBroadcastSSID_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4,1,1),_TmnxWlanAPBroadcastSSID_Type())
tmnxWlanAPBroadcastSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanAPBroadcastSSID.setStatus(_A)
class _TmnxWlanAPClientLimit_Type(Unsigned32):defaultValue=24;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_TmnxWlanAPClientLimit_Type.__name__=_F
_TmnxWlanAPClientLimit_Object=MibTableColumn
tmnxWlanAPClientLimit=_TmnxWlanAPClientLimit_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4,1,2),_TmnxWlanAPClientLimit_Type())
tmnxWlanAPClientLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanAPClientLimit.setStatus(_A)
class _TmnxWlanAPClientTimeout_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_TmnxWlanAPClientTimeout_Type.__name__=_F
_TmnxWlanAPClientTimeout_Object=MibTableColumn
tmnxWlanAPClientTimeout=_TmnxWlanAPClientTimeout_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4,1,3),_TmnxWlanAPClientTimeout_Type())
tmnxWlanAPClientTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanAPClientTimeout.setStatus(_A)
if mibBuilder.loadTexts:tmnxWlanAPClientTimeout.setUnits(_W)
class _TmnxWlanAPDot1xRadiusPlcy_Type(TPolicyStatementNameOrEmpty):defaultValue=OctetString('')
_TmnxWlanAPDot1xRadiusPlcy_Type.__name__=_R
_TmnxWlanAPDot1xRadiusPlcy_Object=MibTableColumn
tmnxWlanAPDot1xRadiusPlcy=_TmnxWlanAPDot1xRadiusPlcy_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4,1,4),_TmnxWlanAPDot1xRadiusPlcy_Type())
tmnxWlanAPDot1xRadiusPlcy.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanAPDot1xRadiusPlcy.setStatus(_A)
class _TmnxWlanAPDot1xReauthPeriod_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_TmnxWlanAPDot1xReauthPeriod_Type.__name__=_F
_TmnxWlanAPDot1xReauthPeriod_Object=MibTableColumn
tmnxWlanAPDot1xReauthPeriod=_TmnxWlanAPDot1xReauthPeriod_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4,1,5),_TmnxWlanAPDot1xReauthPeriod_Type())
tmnxWlanAPDot1xReauthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanAPDot1xReauthPeriod.setStatus(_A)
if mibBuilder.loadTexts:tmnxWlanAPDot1xReauthPeriod.setUnits(_W)
class _TmnxWlanAPDhcpAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxWlanAPDhcpAdminState_Type.__name__=_S
_TmnxWlanAPDhcpAdminState_Object=MibTableColumn
tmnxWlanAPDhcpAdminState=_TmnxWlanAPDhcpAdminState_Object((1,3,6,1,4,1,6527,3,1,2,117,2,1,4,1,6),_TmnxWlanAPDhcpAdminState_Type())
tmnxWlanAPDhcpAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanAPDhcpAdminState.setStatus(_A)
_TmnxWlanCardConfigObjs_ObjectIdentity=ObjectIdentity
tmnxWlanCardConfigObjs=_TmnxWlanCardConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,117,2,2))
_TmnxWlanRadioTable_Object=MibTable
tmnxWlanRadioTable=_TmnxWlanRadioTable_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1))
if mibBuilder.loadTexts:tmnxWlanRadioTable.setStatus(_A)
_TmnxWlanRadioEntry_Object=MibTableRow
tmnxWlanRadioEntry=_TmnxWlanRadioEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1))
tmnxWlanRadioEntry.setIndexNames((0,_E,_L),(0,_E,_K),(0,_E,_M),(0,_B,_P))
if mibBuilder.loadTexts:tmnxWlanRadioEntry.setStatus(_A)
_TmnxMDARadioNum_Type=Unsigned32
_TmnxMDARadioNum_Object=MibTableColumn
tmnxMDARadioNum=_TmnxMDARadioNum_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,1),_TmnxMDARadioNum_Type())
tmnxMDARadioNum.setMaxAccess(_N)
if mibBuilder.loadTexts:tmnxMDARadioNum.setStatus(_A)
_TmnxWlanRadioType_Type=TmnxWlanRadioType
_TmnxWlanRadioType_Object=MibTableColumn
tmnxWlanRadioType=_TmnxWlanRadioType_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,2),_TmnxWlanRadioType_Type())
tmnxWlanRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanRadioType.setStatus(_A)
class _TmnxWlanRadioAdminStatus_Type(TmnxWlanRadioAdminStatus):defaultValue=2
_TmnxWlanRadioAdminStatus_Type.__name__=_X
_TmnxWlanRadioAdminStatus_Object=MibTableColumn
tmnxWlanRadioAdminStatus=_TmnxWlanRadioAdminStatus_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,3),_TmnxWlanRadioAdminStatus_Type())
tmnxWlanRadioAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanRadioAdminStatus.setStatus(_A)
class _TmnxWlanRadioCountry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_O,0),('australia',1),('belgium',2),('bolivia',3),('brazil',4),('canada',5),('chile',6),('colombia',7),('france',8),('germany',9),('india',10),('iran',11),('italy',12),('japan',13),('malaysia',14),('mexico',15),('newZealand',16),('peru',17),('russia',18),('singapore',19),('southAfrica',20),('usa',21),('venezuela',22)))
_TmnxWlanRadioCountry_Type.__name__=_I
_TmnxWlanRadioCountry_Object=MibTableColumn
tmnxWlanRadioCountry=_TmnxWlanRadioCountry_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,4),_TmnxWlanRadioCountry_Type())
tmnxWlanRadioCountry.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanRadioCountry.setStatus(_A)
class _TmnxWlanRadioCfgFreqBand_Type(TmnxWlanRadioFreqBand):defaultValue=1
_TmnxWlanRadioCfgFreqBand_Type.__name__=_Y
_TmnxWlanRadioCfgFreqBand_Object=MibTableColumn
tmnxWlanRadioCfgFreqBand=_TmnxWlanRadioCfgFreqBand_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,5),_TmnxWlanRadioCfgFreqBand_Type())
tmnxWlanRadioCfgFreqBand.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanRadioCfgFreqBand.setStatus(_A)
class _TmnxWlanRadioCfgChannel_Type(Unsigned32):defaultValue=0
_TmnxWlanRadioCfgChannel_Type.__name__=_F
_TmnxWlanRadioCfgChannel_Object=MibTableColumn
tmnxWlanRadioCfgChannel=_TmnxWlanRadioCfgChannel_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,6),_TmnxWlanRadioCfgChannel_Type())
tmnxWlanRadioCfgChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanRadioCfgChannel.setStatus(_A)
class _TmnxWlanRadioCfgChBandwidth_Type(TmnxWlanRadioChBandwidth):defaultValue=1
_TmnxWlanRadioCfgChBandwidth_Type.__name__=_Z
_TmnxWlanRadioCfgChBandwidth_Object=MibTableColumn
tmnxWlanRadioCfgChBandwidth=_TmnxWlanRadioCfgChBandwidth_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,7),_TmnxWlanRadioCfgChBandwidth_Type())
tmnxWlanRadioCfgChBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanRadioCfgChBandwidth.setStatus(_A)
class _TmnxWlanRadioApBeaconInterval_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,999))
_TmnxWlanRadioApBeaconInterval_Type.__name__=_F
_TmnxWlanRadioApBeaconInterval_Object=MibTableColumn
tmnxWlanRadioApBeaconInterval=_TmnxWlanRadioApBeaconInterval_Object((1,3,6,1,4,1,6527,3,1,2,117,2,2,1,1,8),_TmnxWlanRadioApBeaconInterval_Type())
tmnxWlanRadioApBeaconInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxWlanRadioApBeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:tmnxWlanRadioApBeaconInterval.setUnits('msecs')
_TmnxWlanOperObjs_ObjectIdentity=ObjectIdentity
tmnxWlanOperObjs=_TmnxWlanOperObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,117,3))
_TmnxWlanRadioOperTable_Object=MibTable
tmnxWlanRadioOperTable=_TmnxWlanRadioOperTable_Object((1,3,6,1,4,1,6527,3,1,2,117,3,2))
if mibBuilder.loadTexts:tmnxWlanRadioOperTable.setStatus(_A)
_TmnxWlanRadioOperEntry_Object=MibTableRow
tmnxWlanRadioOperEntry=_TmnxWlanRadioOperEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,3,2,1))
tmnxWlanRadioOperEntry.setIndexNames((0,_E,_L),(0,_E,_K),(0,_E,_M),(0,_B,_P))
if mibBuilder.loadTexts:tmnxWlanRadioOperEntry.setStatus(_A)
_TmnxWlanRadioOperStatus_Type=TmnxWlanRadioOperStatus
_TmnxWlanRadioOperStatus_Object=MibTableColumn
tmnxWlanRadioOperStatus=_TmnxWlanRadioOperStatus_Object((1,3,6,1,4,1,6527,3,1,2,117,3,2,1,1),_TmnxWlanRadioOperStatus_Type())
tmnxWlanRadioOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanRadioOperStatus.setStatus(_A)
_TmnxWlanRadioOperFreqBand_Type=TmnxWlanRadioFreqBand
_TmnxWlanRadioOperFreqBand_Object=MibTableColumn
tmnxWlanRadioOperFreqBand=_TmnxWlanRadioOperFreqBand_Object((1,3,6,1,4,1,6527,3,1,2,117,3,2,1,2),_TmnxWlanRadioOperFreqBand_Type())
tmnxWlanRadioOperFreqBand.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanRadioOperFreqBand.setStatus(_A)
_TmnxWlanRadioOperChannel_Type=Unsigned32
_TmnxWlanRadioOperChannel_Object=MibTableColumn
tmnxWlanRadioOperChannel=_TmnxWlanRadioOperChannel_Object((1,3,6,1,4,1,6527,3,1,2,117,3,2,1,3),_TmnxWlanRadioOperChannel_Type())
tmnxWlanRadioOperChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanRadioOperChannel.setStatus(_A)
_TmnxWlanRadioOperChBandwidth_Type=TmnxWlanRadioChBandwidth
_TmnxWlanRadioOperChBandwidth_Object=MibTableColumn
tmnxWlanRadioOperChBandwidth=_TmnxWlanRadioOperChBandwidth_Object((1,3,6,1,4,1,6527,3,1,2,117,3,2,1,4),_TmnxWlanRadioOperChBandwidth_Type())
tmnxWlanRadioOperChBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanRadioOperChBandwidth.setStatus(_A)
_TmnxWlanRadioOperCentreFreq_Type=Unsigned32
_TmnxWlanRadioOperCentreFreq_Object=MibTableColumn
tmnxWlanRadioOperCentreFreq=_TmnxWlanRadioOperCentreFreq_Object((1,3,6,1,4,1,6527,3,1,2,117,3,2,1,5),_TmnxWlanRadioOperCentreFreq_Type())
tmnxWlanRadioOperCentreFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanRadioOperCentreFreq.setStatus(_A)
if mibBuilder.loadTexts:tmnxWlanRadioOperCentreFreq.setUnits('MHz')
_TmnxWlanAPOperTable_Object=MibTable
tmnxWlanAPOperTable=_TmnxWlanAPOperTable_Object((1,3,6,1,4,1,6527,3,1,2,117,3,3))
if mibBuilder.loadTexts:tmnxWlanAPOperTable.setStatus(_A)
_TmnxWlanAPOperEntry_Object=MibTableRow
tmnxWlanAPOperEntry=_TmnxWlanAPOperEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,3,3,1))
tmnxWlanAPOperEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tmnxWlanAPOperEntry.setStatus(_A)
_TmnxWlanAPConnectedClients_Type=Unsigned32
_TmnxWlanAPConnectedClients_Object=MibTableColumn
tmnxWlanAPConnectedClients=_TmnxWlanAPConnectedClients_Object((1,3,6,1,4,1,6527,3,1,2,117,3,3,1,1),_TmnxWlanAPConnectedClients_Type())
tmnxWlanAPConnectedClients.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanAPConnectedClients.setStatus(_A)
_TmnxWlanAPTotalAttaches_Type=Counter64
_TmnxWlanAPTotalAttaches_Object=MibTableColumn
tmnxWlanAPTotalAttaches=_TmnxWlanAPTotalAttaches_Object((1,3,6,1,4,1,6527,3,1,2,117,3,3,1,2),_TmnxWlanAPTotalAttaches_Type())
tmnxWlanAPTotalAttaches.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanAPTotalAttaches.setStatus(_A)
_TmnxWlanAPTotalDetaches_Type=Counter64
_TmnxWlanAPTotalDetaches_Object=MibTableColumn
tmnxWlanAPTotalDetaches=_TmnxWlanAPTotalDetaches_Object((1,3,6,1,4,1,6527,3,1,2,117,3,3,1,3),_TmnxWlanAPTotalDetaches_Type())
tmnxWlanAPTotalDetaches.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanAPTotalDetaches.setStatus(_A)
_TmnxWlanAPTotalAuthSuccess_Type=Counter64
_TmnxWlanAPTotalAuthSuccess_Object=MibTableColumn
tmnxWlanAPTotalAuthSuccess=_TmnxWlanAPTotalAuthSuccess_Object((1,3,6,1,4,1,6527,3,1,2,117,3,3,1,4),_TmnxWlanAPTotalAuthSuccess_Type())
tmnxWlanAPTotalAuthSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanAPTotalAuthSuccess.setStatus(_A)
_TmnxWlanAPTotalAuthFails_Type=Counter64
_TmnxWlanAPTotalAuthFails_Object=MibTableColumn
tmnxWlanAPTotalAuthFails=_TmnxWlanAPTotalAuthFails_Object((1,3,6,1,4,1,6527,3,1,2,117,3,3,1,5),_TmnxWlanAPTotalAuthFails_Type())
tmnxWlanAPTotalAuthFails.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanAPTotalAuthFails.setStatus(_A)
_TmnxWlanAPClientTable_Object=MibTable
tmnxWlanAPClientTable=_TmnxWlanAPClientTable_Object((1,3,6,1,4,1,6527,3,1,2,117,3,4))
if mibBuilder.loadTexts:tmnxWlanAPClientTable.setStatus(_A)
_TmnxWlanAPClientEntry_Object=MibTableRow
tmnxWlanAPClientEntry=_TmnxWlanAPClientEntry_Object((1,3,6,1,4,1,6527,3,1,2,117,3,4,1))
tmnxWlanAPClientEntry.setIndexNames((0,_G,_H),(0,_B,_a))
if mibBuilder.loadTexts:tmnxWlanAPClientEntry.setStatus(_A)
_TmnxWlanAPClientMacAddress_Type=MacAddress
_TmnxWlanAPClientMacAddress_Object=MibTableColumn
tmnxWlanAPClientMacAddress=_TmnxWlanAPClientMacAddress_Object((1,3,6,1,4,1,6527,3,1,2,117,3,4,1,1),_TmnxWlanAPClientMacAddress_Type())
tmnxWlanAPClientMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:tmnxWlanAPClientMacAddress.setStatus(_A)
_TmnxWlanAPClientConnectTime_Type=TimeStamp
_TmnxWlanAPClientConnectTime_Object=MibTableColumn
tmnxWlanAPClientConnectTime=_TmnxWlanAPClientConnectTime_Object((1,3,6,1,4,1,6527,3,1,2,117,3,4,1,2),_TmnxWlanAPClientConnectTime_Type())
tmnxWlanAPClientConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanAPClientConnectTime.setStatus(_A)
_TmnxWlanAPClientAuthorized_Type=TruthValue
_TmnxWlanAPClientAuthorized_Object=MibTableColumn
tmnxWlanAPClientAuthorized=_TmnxWlanAPClientAuthorized_Object((1,3,6,1,4,1,6527,3,1,2,117,3,4,1,3),_TmnxWlanAPClientAuthorized_Type())
tmnxWlanAPClientAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxWlanAPClientAuthorized.setStatus(_A)
_TmnxWlanNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxWlanNotifyPrefix=_TmnxWlanNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,117))
_TmnxWlanNotifications_ObjectIdentity=ObjectIdentity
tmnxWlanNotifications=_TmnxWlanNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,117,0))
tmnxWlanNetworkEntry.registerAugmentions((_B,_b))
tmnxWlanNetworkSecurityEntry.setIndexNames(*tmnxWlanNetworkEntry.getIndexNames())
tmnxWlanConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,117,2,1,1))
tmnxWlanConfigGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:tmnxWlanConfigGroup.setStatus(_A)
tmnxWlanOperGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,117,2,1,2))
tmnxWlanOperGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:tmnxWlanOperGroup.setStatus(_A)
tmnxWlanrCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,117,1,1))
tmnxWlanrCompliance.setObjects(*((_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:tmnxWlanrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TmnxWlanNetworkId':TmnxWlanNetworkId,'TmnxWlanSSID':TmnxWlanSSID,_V:TmnxWlanWpaPassphrase,'TmnxWlanRadioType':TmnxWlanRadioType,_X:TmnxWlanRadioAdminStatus,'TmnxWlanRadioOperStatus':TmnxWlanRadioOperStatus,_Y:TmnxWlanRadioFreqBand,_Z:TmnxWlanRadioChBandwidth,'timetraWlanMIBModule':timetraWlanMIBModule,'tmnxWlanConformance':tmnxWlanConformance,'tmnxWlanCompliances':tmnxWlanCompliances,'tmnxWlanrCompliance':tmnxWlanrCompliance,'tmnxWlanGroups':tmnxWlanGroups,'tmnxWlanV15v0Groups':tmnxWlanV15v0Groups,_A9:tmnxWlanConfigGroup,_AA:tmnxWlanOperGroup,'tmnxWlanV20Groups':tmnxWlanV20Groups,'tmnxWlanObjs':tmnxWlanObjs,'tmnxWlanConfigObjs':tmnxWlanConfigObjs,'tmnxWlanPortConfigObjs':tmnxWlanPortConfigObjs,'tmnxWlanPortTable':tmnxWlanPortTable,'tmnxWlanPortEntry':tmnxWlanPortEntry,_c:tmnxWlanPortMode,_d:tmnxWlanPortRadio,_e:tmnxWlanPortOperFlags,'tmnxWlanNetworkTable':tmnxWlanNetworkTable,'tmnxWlanNetworkEntry':tmnxWlanNetworkEntry,_T:tmnxWlanNetworkId,_f:tmnxWlanNetworkRowStatus,_g:tmnxWlanNetworkSSID,'tmnxWlanNetworkSecurityTable':tmnxWlanNetworkSecurityTable,_b:tmnxWlanNetworkSecurityEntry,_h:tmnxWlanNetworkSecurity,_i:tmnxWlanNetworkWpaEncryption,_j:tmnxWlanNetworkWpaPassphrase,'tmnxWlanAPTable':tmnxWlanAPTable,'tmnxWlanAPEntry':tmnxWlanAPEntry,_k:tmnxWlanAPBroadcastSSID,_l:tmnxWlanAPClientLimit,_m:tmnxWlanAPClientTimeout,_n:tmnxWlanAPDot1xRadiusPlcy,_o:tmnxWlanAPDot1xReauthPeriod,_p:tmnxWlanAPDhcpAdminState,'tmnxWlanCardConfigObjs':tmnxWlanCardConfigObjs,'tmnxWlanRadioTable':tmnxWlanRadioTable,'tmnxWlanRadioEntry':tmnxWlanRadioEntry,_P:tmnxMDARadioNum,_q:tmnxWlanRadioType,_r:tmnxWlanRadioAdminStatus,_u:tmnxWlanRadioCountry,_v:tmnxWlanRadioCfgFreqBand,_t:tmnxWlanRadioCfgChannel,_s:tmnxWlanRadioCfgChBandwidth,_w:tmnxWlanRadioApBeaconInterval,'tmnxWlanOperObjs':tmnxWlanOperObjs,'tmnxWlanRadioOperTable':tmnxWlanRadioOperTable,'tmnxWlanRadioOperEntry':tmnxWlanRadioOperEntry,_A2:tmnxWlanRadioOperStatus,_A5:tmnxWlanRadioOperFreqBand,_A4:tmnxWlanRadioOperChannel,_A3:tmnxWlanRadioOperChBandwidth,_A8:tmnxWlanRadioOperCentreFreq,'tmnxWlanAPOperTable':tmnxWlanAPOperTable,'tmnxWlanAPOperEntry':tmnxWlanAPOperEntry,_x:tmnxWlanAPConnectedClients,_y:tmnxWlanAPTotalAttaches,_z:tmnxWlanAPTotalDetaches,_A0:tmnxWlanAPTotalAuthSuccess,_A1:tmnxWlanAPTotalAuthFails,'tmnxWlanAPClientTable':tmnxWlanAPClientTable,'tmnxWlanAPClientEntry':tmnxWlanAPClientEntry,_a:tmnxWlanAPClientMacAddress,_A6:tmnxWlanAPClientConnectTime,_A7:tmnxWlanAPClientAuthorized,'tmnxWlanNotifyPrefix':tmnxWlanNotifyPrefix,'tmnxWlanNotifications':tmnxWlanNotifications})