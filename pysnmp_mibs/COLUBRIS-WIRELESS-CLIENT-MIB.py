_A0='colubrisWirelessClientMIBGroupCounters'
_z='colubrisWirelessClientNotificationGroup'
_y='colubrisWirelessClientMIBGroup'
_x='colubrisWirelessClientConnectionNotification'
_w='colubrisWirelessClientPktsRxRate54'
_v='colubrisWirelessClientPktsRxRate48'
_u='colubrisWirelessClientPktsRxRate36'
_t='colubrisWirelessClientPktsRxRate24'
_s='colubrisWirelessClientPktsRxRate18'
_r='colubrisWirelessClientPktsRxRate12'
_q='colubrisWirelessClientPktsRxRate9'
_p='colubrisWirelessClientPktsRxRate6'
_o='colubrisWirelessClientPktsRxRate11'
_n='colubrisWirelessClientPktsRxRate5dot5'
_m='colubrisWirelessClientPktsRxRate2'
_l='colubrisWirelessClientPktsRxRate1'
_k='colubrisWirelessClientPktsTxRate54'
_j='colubrisWirelessClientPktsTxRate48'
_i='colubrisWirelessClientPktsTxRate36'
_h='colubrisWirelessClientPktsTxRate24'
_g='colubrisWirelessClientPktsTxRate18'
_f='colubrisWirelessClientPktsTxRate12'
_e='colubrisWirelessClientPktsTxRate9'
_d='colubrisWirelessClientPktsTxRate6'
_c='colubrisWirelessClientPktsTxRate11'
_b='colubrisWirelessClientPktsTxRate5dot5'
_a='colubrisWirelessClientPktsTxRate2'
_Z='colubrisWirelessClientPktsTxRate1'
_Y='colubrisWirelessClientOutOctets'
_X='colubrisWirelessClientInOctets'
_W='colubrisWirelessClientOutPkts'
_V='colubrisWirelessClientInPkts'
_U='colubrisWirelessClientEncryptionStatus'
_T='colubrisWirelessClientAuthorizedState'
_S='colubrisWirelessClientConnectTime'
_R='colubrisWirelessClientReceiveRate'
_Q='colubrisWirelessClientTransmitRate'
_P='colubrisWirelessClientConnectionNotificationEnabled'
_O='colubrisWirelessClientSNR'
_N='colubrisWirelessClientNoiseLevel'
_M='colubrisWirelessClientSignalLevel'
_L='colubrisWirelessClientState'
_K='sysName'
_J='SNMPv2-MIB'
_I='ColubrisNotificationEnable'
_H='systemSerialNumber'
_G='COLUBRIS-SYSTEM-MIB'
_F='colubrisWirelessClientBSSID'
_E='colubrisWirelessClientSSID'
_D='Integer32'
_C='read-only'
_B='current'
_A='COLUBRIS-WIRELESS-CLIENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
systemSerialNumber,=mibBuilder.importSymbols(_G,_H)
ColubrisNotificationEnable,ColubrisSSID=mibBuilder.importSymbols('COLUBRIS-TC',_I,'ColubrisSSID')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
colubrisWirelessClientMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,20))
_ColubrisWirelessClientMIBObjects_ObjectIdentity=ObjectIdentity
colubrisWirelessClientMIBObjects=_ColubrisWirelessClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,20,1))
_ColubrisWirelessClientInfo_ObjectIdentity=ObjectIdentity
colubrisWirelessClientInfo=_ColubrisWirelessClientInfo_ObjectIdentity((1,3,6,1,4,1,8744,5,20,1,1))
class _ColubrisWirelessClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('disconnected',1),('scanning',2),('authenticating',3),('associating',4),('associated',5)))
_ColubrisWirelessClientState_Type.__name__=_D
_ColubrisWirelessClientState_Object=MibScalar
colubrisWirelessClientState=_ColubrisWirelessClientState_Object((1,3,6,1,4,1,8744,5,20,1,1,1),_ColubrisWirelessClientState_Type())
colubrisWirelessClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientState.setStatus(_B)
_ColubrisWirelessClientSSID_Type=ColubrisSSID
_ColubrisWirelessClientSSID_Object=MibScalar
colubrisWirelessClientSSID=_ColubrisWirelessClientSSID_Object((1,3,6,1,4,1,8744,5,20,1,1,2),_ColubrisWirelessClientSSID_Type())
colubrisWirelessClientSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientSSID.setStatus(_B)
_ColubrisWirelessClientBSSID_Type=MacAddress
_ColubrisWirelessClientBSSID_Object=MibScalar
colubrisWirelessClientBSSID=_ColubrisWirelessClientBSSID_Object((1,3,6,1,4,1,8744,5,20,1,1,3),_ColubrisWirelessClientBSSID_Type())
colubrisWirelessClientBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientBSSID.setStatus(_B)
_ColubrisWirelessClientSignalLevel_Type=Integer32
_ColubrisWirelessClientSignalLevel_Object=MibScalar
colubrisWirelessClientSignalLevel=_ColubrisWirelessClientSignalLevel_Object((1,3,6,1,4,1,8744,5,20,1,1,4),_ColubrisWirelessClientSignalLevel_Type())
colubrisWirelessClientSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientSignalLevel.setStatus(_B)
_ColubrisWirelessClientNoiseLevel_Type=Integer32
_ColubrisWirelessClientNoiseLevel_Object=MibScalar
colubrisWirelessClientNoiseLevel=_ColubrisWirelessClientNoiseLevel_Object((1,3,6,1,4,1,8744,5,20,1,1,5),_ColubrisWirelessClientNoiseLevel_Type())
colubrisWirelessClientNoiseLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientNoiseLevel.setStatus(_B)
_ColubrisWirelessClientSNR_Type=Integer32
_ColubrisWirelessClientSNR_Object=MibScalar
colubrisWirelessClientSNR=_ColubrisWirelessClientSNR_Object((1,3,6,1,4,1,8744,5,20,1,1,6),_ColubrisWirelessClientSNR_Type())
colubrisWirelessClientSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientSNR.setStatus(_B)
class _ColubrisWirelessClientConnectionNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_ColubrisWirelessClientConnectionNotificationEnabled_Type.__name__=_I
_ColubrisWirelessClientConnectionNotificationEnabled_Object=MibScalar
colubrisWirelessClientConnectionNotificationEnabled=_ColubrisWirelessClientConnectionNotificationEnabled_Object((1,3,6,1,4,1,8744,5,20,1,1,7),_ColubrisWirelessClientConnectionNotificationEnabled_Type())
colubrisWirelessClientConnectionNotificationEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:colubrisWirelessClientConnectionNotificationEnabled.setStatus(_B)
_ColubrisWirelessClientConnectTime_Type=Counter32
_ColubrisWirelessClientConnectTime_Object=MibScalar
colubrisWirelessClientConnectTime=_ColubrisWirelessClientConnectTime_Object((1,3,6,1,4,1,8744,5,20,1,1,8),_ColubrisWirelessClientConnectTime_Type())
colubrisWirelessClientConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientConnectTime.setStatus(_B)
if mibBuilder.loadTexts:colubrisWirelessClientConnectTime.setUnits('seconds')
class _ColubrisWirelessClientAuthorizedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notAuthorized',1),('authorized',2)))
_ColubrisWirelessClientAuthorizedState_Type.__name__=_D
_ColubrisWirelessClientAuthorizedState_Object=MibScalar
colubrisWirelessClientAuthorizedState=_ColubrisWirelessClientAuthorizedState_Object((1,3,6,1,4,1,8744,5,20,1,1,9),_ColubrisWirelessClientAuthorizedState_Type())
colubrisWirelessClientAuthorizedState.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientAuthorizedState.setStatus(_B)
class _ColubrisWirelessClientEncryptionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('wep',2),('tkip',3),('aes',4),('aesTkip',5)))
_ColubrisWirelessClientEncryptionStatus_Type.__name__=_D
_ColubrisWirelessClientEncryptionStatus_Object=MibScalar
colubrisWirelessClientEncryptionStatus=_ColubrisWirelessClientEncryptionStatus_Object((1,3,6,1,4,1,8744,5,20,1,1,10),_ColubrisWirelessClientEncryptionStatus_Type())
colubrisWirelessClientEncryptionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientEncryptionStatus.setStatus(_B)
_ColubrisWirelessClientTransmitRate_Type=Unsigned32
_ColubrisWirelessClientTransmitRate_Object=MibScalar
colubrisWirelessClientTransmitRate=_ColubrisWirelessClientTransmitRate_Object((1,3,6,1,4,1,8744,5,20,1,1,11),_ColubrisWirelessClientTransmitRate_Type())
colubrisWirelessClientTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientTransmitRate.setStatus(_B)
_ColubrisWirelessClientReceiveRate_Type=Unsigned32
_ColubrisWirelessClientReceiveRate_Object=MibScalar
colubrisWirelessClientReceiveRate=_ColubrisWirelessClientReceiveRate_Object((1,3,6,1,4,1,8744,5,20,1,1,12),_ColubrisWirelessClientReceiveRate_Type())
colubrisWirelessClientReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientReceiveRate.setStatus(_B)
_ColubrisWirelessClientStats_ObjectIdentity=ObjectIdentity
colubrisWirelessClientStats=_ColubrisWirelessClientStats_ObjectIdentity((1,3,6,1,4,1,8744,5,20,1,2))
_ColubrisWirelessClientInPkts_Type=Counter32
_ColubrisWirelessClientInPkts_Object=MibScalar
colubrisWirelessClientInPkts=_ColubrisWirelessClientInPkts_Object((1,3,6,1,4,1,8744,5,20,1,2,1),_ColubrisWirelessClientInPkts_Type())
colubrisWirelessClientInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientInPkts.setStatus(_B)
_ColubrisWirelessClientOutPkts_Type=Counter32
_ColubrisWirelessClientOutPkts_Object=MibScalar
colubrisWirelessClientOutPkts=_ColubrisWirelessClientOutPkts_Object((1,3,6,1,4,1,8744,5,20,1,2,2),_ColubrisWirelessClientOutPkts_Type())
colubrisWirelessClientOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientOutPkts.setStatus(_B)
_ColubrisWirelessClientInOctets_Type=Counter64
_ColubrisWirelessClientInOctets_Object=MibScalar
colubrisWirelessClientInOctets=_ColubrisWirelessClientInOctets_Object((1,3,6,1,4,1,8744,5,20,1,2,3),_ColubrisWirelessClientInOctets_Type())
colubrisWirelessClientInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientInOctets.setStatus(_B)
_ColubrisWirelessClientOutOctets_Type=Counter64
_ColubrisWirelessClientOutOctets_Object=MibScalar
colubrisWirelessClientOutOctets=_ColubrisWirelessClientOutOctets_Object((1,3,6,1,4,1,8744,5,20,1,2,4),_ColubrisWirelessClientOutOctets_Type())
colubrisWirelessClientOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientOutOctets.setStatus(_B)
_ColubrisWirelessClientPktsTxRate1_Type=Counter32
_ColubrisWirelessClientPktsTxRate1_Object=MibScalar
colubrisWirelessClientPktsTxRate1=_ColubrisWirelessClientPktsTxRate1_Object((1,3,6,1,4,1,8744,5,20,1,2,5),_ColubrisWirelessClientPktsTxRate1_Type())
colubrisWirelessClientPktsTxRate1.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate1.setStatus(_B)
_ColubrisWirelessClientPktsTxRate2_Type=Counter32
_ColubrisWirelessClientPktsTxRate2_Object=MibScalar
colubrisWirelessClientPktsTxRate2=_ColubrisWirelessClientPktsTxRate2_Object((1,3,6,1,4,1,8744,5,20,1,2,6),_ColubrisWirelessClientPktsTxRate2_Type())
colubrisWirelessClientPktsTxRate2.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate2.setStatus(_B)
_ColubrisWirelessClientPktsTxRate5dot5_Type=Counter32
_ColubrisWirelessClientPktsTxRate5dot5_Object=MibScalar
colubrisWirelessClientPktsTxRate5dot5=_ColubrisWirelessClientPktsTxRate5dot5_Object((1,3,6,1,4,1,8744,5,20,1,2,7),_ColubrisWirelessClientPktsTxRate5dot5_Type())
colubrisWirelessClientPktsTxRate5dot5.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate5dot5.setStatus(_B)
_ColubrisWirelessClientPktsTxRate11_Type=Counter32
_ColubrisWirelessClientPktsTxRate11_Object=MibScalar
colubrisWirelessClientPktsTxRate11=_ColubrisWirelessClientPktsTxRate11_Object((1,3,6,1,4,1,8744,5,20,1,2,8),_ColubrisWirelessClientPktsTxRate11_Type())
colubrisWirelessClientPktsTxRate11.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate11.setStatus(_B)
_ColubrisWirelessClientPktsTxRate6_Type=Counter32
_ColubrisWirelessClientPktsTxRate6_Object=MibScalar
colubrisWirelessClientPktsTxRate6=_ColubrisWirelessClientPktsTxRate6_Object((1,3,6,1,4,1,8744,5,20,1,2,9),_ColubrisWirelessClientPktsTxRate6_Type())
colubrisWirelessClientPktsTxRate6.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate6.setStatus(_B)
_ColubrisWirelessClientPktsTxRate9_Type=Counter32
_ColubrisWirelessClientPktsTxRate9_Object=MibScalar
colubrisWirelessClientPktsTxRate9=_ColubrisWirelessClientPktsTxRate9_Object((1,3,6,1,4,1,8744,5,20,1,2,10),_ColubrisWirelessClientPktsTxRate9_Type())
colubrisWirelessClientPktsTxRate9.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate9.setStatus(_B)
_ColubrisWirelessClientPktsTxRate12_Type=Counter32
_ColubrisWirelessClientPktsTxRate12_Object=MibScalar
colubrisWirelessClientPktsTxRate12=_ColubrisWirelessClientPktsTxRate12_Object((1,3,6,1,4,1,8744,5,20,1,2,11),_ColubrisWirelessClientPktsTxRate12_Type())
colubrisWirelessClientPktsTxRate12.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate12.setStatus(_B)
_ColubrisWirelessClientPktsTxRate18_Type=Counter32
_ColubrisWirelessClientPktsTxRate18_Object=MibScalar
colubrisWirelessClientPktsTxRate18=_ColubrisWirelessClientPktsTxRate18_Object((1,3,6,1,4,1,8744,5,20,1,2,12),_ColubrisWirelessClientPktsTxRate18_Type())
colubrisWirelessClientPktsTxRate18.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate18.setStatus(_B)
_ColubrisWirelessClientPktsTxRate24_Type=Counter32
_ColubrisWirelessClientPktsTxRate24_Object=MibScalar
colubrisWirelessClientPktsTxRate24=_ColubrisWirelessClientPktsTxRate24_Object((1,3,6,1,4,1,8744,5,20,1,2,13),_ColubrisWirelessClientPktsTxRate24_Type())
colubrisWirelessClientPktsTxRate24.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate24.setStatus(_B)
_ColubrisWirelessClientPktsTxRate36_Type=Counter32
_ColubrisWirelessClientPktsTxRate36_Object=MibScalar
colubrisWirelessClientPktsTxRate36=_ColubrisWirelessClientPktsTxRate36_Object((1,3,6,1,4,1,8744,5,20,1,2,14),_ColubrisWirelessClientPktsTxRate36_Type())
colubrisWirelessClientPktsTxRate36.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate36.setStatus(_B)
_ColubrisWirelessClientPktsTxRate48_Type=Counter32
_ColubrisWirelessClientPktsTxRate48_Object=MibScalar
colubrisWirelessClientPktsTxRate48=_ColubrisWirelessClientPktsTxRate48_Object((1,3,6,1,4,1,8744,5,20,1,2,15),_ColubrisWirelessClientPktsTxRate48_Type())
colubrisWirelessClientPktsTxRate48.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate48.setStatus(_B)
_ColubrisWirelessClientPktsTxRate54_Type=Counter32
_ColubrisWirelessClientPktsTxRate54_Object=MibScalar
colubrisWirelessClientPktsTxRate54=_ColubrisWirelessClientPktsTxRate54_Object((1,3,6,1,4,1,8744,5,20,1,2,16),_ColubrisWirelessClientPktsTxRate54_Type())
colubrisWirelessClientPktsTxRate54.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsTxRate54.setStatus(_B)
_ColubrisWirelessClientPktsRxRate1_Type=Counter32
_ColubrisWirelessClientPktsRxRate1_Object=MibScalar
colubrisWirelessClientPktsRxRate1=_ColubrisWirelessClientPktsRxRate1_Object((1,3,6,1,4,1,8744,5,20,1,2,17),_ColubrisWirelessClientPktsRxRate1_Type())
colubrisWirelessClientPktsRxRate1.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate1.setStatus(_B)
_ColubrisWirelessClientPktsRxRate2_Type=Counter32
_ColubrisWirelessClientPktsRxRate2_Object=MibScalar
colubrisWirelessClientPktsRxRate2=_ColubrisWirelessClientPktsRxRate2_Object((1,3,6,1,4,1,8744,5,20,1,2,18),_ColubrisWirelessClientPktsRxRate2_Type())
colubrisWirelessClientPktsRxRate2.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate2.setStatus(_B)
_ColubrisWirelessClientPktsRxRate5dot5_Type=Counter32
_ColubrisWirelessClientPktsRxRate5dot5_Object=MibScalar
colubrisWirelessClientPktsRxRate5dot5=_ColubrisWirelessClientPktsRxRate5dot5_Object((1,3,6,1,4,1,8744,5,20,1,2,19),_ColubrisWirelessClientPktsRxRate5dot5_Type())
colubrisWirelessClientPktsRxRate5dot5.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate5dot5.setStatus(_B)
_ColubrisWirelessClientPktsRxRate11_Type=Counter32
_ColubrisWirelessClientPktsRxRate11_Object=MibScalar
colubrisWirelessClientPktsRxRate11=_ColubrisWirelessClientPktsRxRate11_Object((1,3,6,1,4,1,8744,5,20,1,2,20),_ColubrisWirelessClientPktsRxRate11_Type())
colubrisWirelessClientPktsRxRate11.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate11.setStatus(_B)
_ColubrisWirelessClientPktsRxRate6_Type=Counter32
_ColubrisWirelessClientPktsRxRate6_Object=MibScalar
colubrisWirelessClientPktsRxRate6=_ColubrisWirelessClientPktsRxRate6_Object((1,3,6,1,4,1,8744,5,20,1,2,21),_ColubrisWirelessClientPktsRxRate6_Type())
colubrisWirelessClientPktsRxRate6.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate6.setStatus(_B)
_ColubrisWirelessClientPktsRxRate9_Type=Counter32
_ColubrisWirelessClientPktsRxRate9_Object=MibScalar
colubrisWirelessClientPktsRxRate9=_ColubrisWirelessClientPktsRxRate9_Object((1,3,6,1,4,1,8744,5,20,1,2,22),_ColubrisWirelessClientPktsRxRate9_Type())
colubrisWirelessClientPktsRxRate9.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate9.setStatus(_B)
_ColubrisWirelessClientPktsRxRate12_Type=Counter32
_ColubrisWirelessClientPktsRxRate12_Object=MibScalar
colubrisWirelessClientPktsRxRate12=_ColubrisWirelessClientPktsRxRate12_Object((1,3,6,1,4,1,8744,5,20,1,2,23),_ColubrisWirelessClientPktsRxRate12_Type())
colubrisWirelessClientPktsRxRate12.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate12.setStatus(_B)
_ColubrisWirelessClientPktsRxRate18_Type=Counter32
_ColubrisWirelessClientPktsRxRate18_Object=MibScalar
colubrisWirelessClientPktsRxRate18=_ColubrisWirelessClientPktsRxRate18_Object((1,3,6,1,4,1,8744,5,20,1,2,24),_ColubrisWirelessClientPktsRxRate18_Type())
colubrisWirelessClientPktsRxRate18.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate18.setStatus(_B)
_ColubrisWirelessClientPktsRxRate24_Type=Counter32
_ColubrisWirelessClientPktsRxRate24_Object=MibScalar
colubrisWirelessClientPktsRxRate24=_ColubrisWirelessClientPktsRxRate24_Object((1,3,6,1,4,1,8744,5,20,1,2,25),_ColubrisWirelessClientPktsRxRate24_Type())
colubrisWirelessClientPktsRxRate24.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate24.setStatus(_B)
_ColubrisWirelessClientPktsRxRate36_Type=Counter32
_ColubrisWirelessClientPktsRxRate36_Object=MibScalar
colubrisWirelessClientPktsRxRate36=_ColubrisWirelessClientPktsRxRate36_Object((1,3,6,1,4,1,8744,5,20,1,2,26),_ColubrisWirelessClientPktsRxRate36_Type())
colubrisWirelessClientPktsRxRate36.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate36.setStatus(_B)
_ColubrisWirelessClientPktsRxRate48_Type=Counter32
_ColubrisWirelessClientPktsRxRate48_Object=MibScalar
colubrisWirelessClientPktsRxRate48=_ColubrisWirelessClientPktsRxRate48_Object((1,3,6,1,4,1,8744,5,20,1,2,27),_ColubrisWirelessClientPktsRxRate48_Type())
colubrisWirelessClientPktsRxRate48.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate48.setStatus(_B)
_ColubrisWirelessClientPktsRxRate54_Type=Counter32
_ColubrisWirelessClientPktsRxRate54_Object=MibScalar
colubrisWirelessClientPktsRxRate54=_ColubrisWirelessClientPktsRxRate54_Object((1,3,6,1,4,1,8744,5,20,1,2,28),_ColubrisWirelessClientPktsRxRate54_Type())
colubrisWirelessClientPktsRxRate54.setMaxAccess(_C)
if mibBuilder.loadTexts:colubrisWirelessClientPktsRxRate54.setStatus(_B)
_ColubrisWirelessClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisWirelessClientMIBNotificationPrefix=_ColubrisWirelessClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,20,2))
_ColubrisWirelessClientMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisWirelessClientMIBNotifications=_ColubrisWirelessClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,20,2,0))
_ColubrisWirelessClientMIBConformance_ObjectIdentity=ObjectIdentity
colubrisWirelessClientMIBConformance=_ColubrisWirelessClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,20,3))
_ColubrisWirelessClientMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisWirelessClientMIBCompliances=_ColubrisWirelessClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,20,3,1))
_ColubrisWirelessClientMIBGroups_ObjectIdentity=ObjectIdentity
colubrisWirelessClientMIBGroups=_ColubrisWirelessClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,20,3,2))
colubrisWirelessClientMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,20,3,2,1))
colubrisWirelessClientMIBGroup.setObjects(*((_A,_L),(_A,_E),(_A,_F),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:colubrisWirelessClientMIBGroup.setStatus(_B)
colubrisWirelessClientMIBGroupCounters=ObjectGroup((1,3,6,1,4,1,8744,5,20,3,2,3))
colubrisWirelessClientMIBGroupCounters.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:colubrisWirelessClientMIBGroupCounters.setStatus(_B)
colubrisWirelessClientConnectionNotification=NotificationType((1,3,6,1,4,1,8744,5,20,2,0,1))
colubrisWirelessClientConnectionNotification.setObjects(*((_J,_K),(_G,_H),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:colubrisWirelessClientConnectionNotification.setStatus(_B)
colubrisWirelessClientNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,20,3,2,2))
colubrisWirelessClientNotificationGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:colubrisWirelessClientNotificationGroup.setStatus(_B)
colubrisWirelessClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,20,3,1,1))
colubrisWirelessClientMIBCompliance.setObjects(*((_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:colubrisWirelessClientMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'colubrisWirelessClientMIB':colubrisWirelessClientMIB,'colubrisWirelessClientMIBObjects':colubrisWirelessClientMIBObjects,'colubrisWirelessClientInfo':colubrisWirelessClientInfo,_L:colubrisWirelessClientState,_E:colubrisWirelessClientSSID,_F:colubrisWirelessClientBSSID,_M:colubrisWirelessClientSignalLevel,_N:colubrisWirelessClientNoiseLevel,_O:colubrisWirelessClientSNR,_P:colubrisWirelessClientConnectionNotificationEnabled,_S:colubrisWirelessClientConnectTime,_T:colubrisWirelessClientAuthorizedState,_U:colubrisWirelessClientEncryptionStatus,_Q:colubrisWirelessClientTransmitRate,_R:colubrisWirelessClientReceiveRate,'colubrisWirelessClientStats':colubrisWirelessClientStats,_V:colubrisWirelessClientInPkts,_W:colubrisWirelessClientOutPkts,_X:colubrisWirelessClientInOctets,_Y:colubrisWirelessClientOutOctets,_Z:colubrisWirelessClientPktsTxRate1,_a:colubrisWirelessClientPktsTxRate2,_b:colubrisWirelessClientPktsTxRate5dot5,_c:colubrisWirelessClientPktsTxRate11,_d:colubrisWirelessClientPktsTxRate6,_e:colubrisWirelessClientPktsTxRate9,_f:colubrisWirelessClientPktsTxRate12,_g:colubrisWirelessClientPktsTxRate18,_h:colubrisWirelessClientPktsTxRate24,_i:colubrisWirelessClientPktsTxRate36,_j:colubrisWirelessClientPktsTxRate48,_k:colubrisWirelessClientPktsTxRate54,_l:colubrisWirelessClientPktsRxRate1,_m:colubrisWirelessClientPktsRxRate2,_n:colubrisWirelessClientPktsRxRate5dot5,_o:colubrisWirelessClientPktsRxRate11,_p:colubrisWirelessClientPktsRxRate6,_q:colubrisWirelessClientPktsRxRate9,_r:colubrisWirelessClientPktsRxRate12,_s:colubrisWirelessClientPktsRxRate18,_t:colubrisWirelessClientPktsRxRate24,_u:colubrisWirelessClientPktsRxRate36,_v:colubrisWirelessClientPktsRxRate48,_w:colubrisWirelessClientPktsRxRate54,'colubrisWirelessClientMIBNotificationPrefix':colubrisWirelessClientMIBNotificationPrefix,'colubrisWirelessClientMIBNotifications':colubrisWirelessClientMIBNotifications,_x:colubrisWirelessClientConnectionNotification,'colubrisWirelessClientMIBConformance':colubrisWirelessClientMIBConformance,'colubrisWirelessClientMIBCompliances':colubrisWirelessClientMIBCompliances,'colubrisWirelessClientMIBCompliance':colubrisWirelessClientMIBCompliance,'colubrisWirelessClientMIBGroups':colubrisWirelessClientMIBGroups,_y:colubrisWirelessClientMIBGroup,_z:colubrisWirelessClientNotificationGroup,_A0:colubrisWirelessClientMIBGroupCounters})