_P='wirelessAPKeysSetEnabled'
_O='wirelessAPControlListMacAddr'
_N='wirelessAPConnectedStationMacAddr'
_M='Enable'
_L='Disable'
_K='NotificationType'
_J='OctetString'
_I='off'
_H='NETGEAR-ME-MIB'
_G='DisplayString'
_F='enAbled'
_E='disAbled'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Netgear_ObjectIdentity=ObjectIdentity
netgear=_Netgear_ObjectIdentity((1,3,6,1,4,1,4526))
_WirelessProducts_ObjectIdentity=ObjectIdentity
wirelessProducts=_WirelessProducts_ObjectIdentity((1,3,6,1,4,1,4526,4))
_WirelessAccessPointDev_ObjectIdentity=ObjectIdentity
wirelessAccessPointDev=_WirelessAccessPointDev_ObjectIdentity((1,3,6,1,4,1,4526,4,1))
_WirelessAPSystemGroup_ObjectIdentity=ObjectIdentity
wirelessAPSystemGroup=_WirelessAPSystemGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,1))
_WirelessAPMacAddr_Type=PhysAddress
_WirelessAPMacAddr_Object=MibScalar
wirelessAPMacAddr=_WirelessAPMacAddr_Object((1,3,6,1,4,1,4526,4,1,1,1),_WirelessAPMacAddr_Type())
wirelessAPMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPMacAddr.setStatus(_A)
_WirelessAPFWVer_Type=DisplayString
_WirelessAPFWVer_Object=MibScalar
wirelessAPFWVer=_WirelessAPFWVer_Object((1,3,6,1,4,1,4526,4,1,1,2),_WirelessAPFWVer_Type())
wirelessAPFWVer.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPFWVer.setStatus(_A)
_WirelessAPDateTime_Type=DisplayString
_WirelessAPDateTime_Object=MibScalar
wirelessAPDateTime=_WirelessAPDateTime_Object((1,3,6,1,4,1,4526,4,1,1,3),_WirelessAPDateTime_Type())
wirelessAPDateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPDateTime.setStatus(_A)
_WirelessAPUpTime_Type=TimeTicks
_WirelessAPUpTime_Object=MibScalar
wirelessAPUpTime=_WirelessAPUpTime_Object((1,3,6,1,4,1,4526,4,1,1,4),_WirelessAPUpTime_Type())
wirelessAPUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPUpTime.setStatus(_A)
class _WirelessAPResetNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-reset',0),('reset',1)))
_WirelessAPResetNow_Type.__name__=_C
_WirelessAPResetNow_Object=MibScalar
wirelessAPResetNow=_WirelessAPResetNow_Object((1,3,6,1,4,1,4526,4,1,1,5),_WirelessAPResetNow_Type())
wirelessAPResetNow.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPResetNow.setStatus(_A)
class _WirelessAPResetToFactoryDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-erase',0),('erase',1)))
_WirelessAPResetToFactoryDefault_Type.__name__=_C
_WirelessAPResetToFactoryDefault_Object=MibScalar
wirelessAPResetToFactoryDefault=_WirelessAPResetToFactoryDefault_Object((1,3,6,1,4,1,4526,4,1,1,6),_WirelessAPResetToFactoryDefault_Type())
wirelessAPResetToFactoryDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPResetToFactoryDefault.setStatus(_A)
class _WirelessAPPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_WirelessAPPassword_Type.__name__=_G
_WirelessAPPassword_Object=MibScalar
wirelessAPPassword=_WirelessAPPassword_Object((1,3,6,1,4,1,4526,4,1,1,7),_WirelessAPPassword_Type())
wirelessAPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPPassword.setStatus(_A)
class _WirelessAPClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-clear',0),('clear',1)))
_WirelessAPClearLog_Type.__name__=_C
_WirelessAPClearLog_Object=MibScalar
wirelessAPClearLog=_WirelessAPClearLog_Object((1,3,6,1,4,1,4526,4,1,1,8),_WirelessAPClearLog_Type())
wirelessAPClearLog.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPClearLog.setStatus(_A)
class _WirelessAPSaveConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-save',0),('save',1)))
_WirelessAPSaveConfiguration_Type.__name__=_C
_WirelessAPSaveConfiguration_Object=MibScalar
wirelessAPSaveConfiguration=_WirelessAPSaveConfiguration_Object((1,3,6,1,4,1,4526,4,1,1,9),_WirelessAPSaveConfiguration_Type())
wirelessAPSaveConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPSaveConfiguration.setStatus(_A)
class _SnmpTrapVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('V1',0),('V2c',1)))
_SnmpTrapVersion_Type.__name__=_C
_SnmpTrapVersion_Object=MibScalar
snmpTrapVersion=_SnmpTrapVersion_Object((1,3,6,1,4,1,4526,4,1,1,10),_SnmpTrapVersion_Type())
snmpTrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapVersion.setStatus(_A)
class _SnmpTrapRcvIpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('Uni-cast',0),('Broadcast',1)))
_SnmpTrapRcvIpType_Type.__name__=_C
_SnmpTrapRcvIpType_Object=MibScalar
snmpTrapRcvIpType=_SnmpTrapRcvIpType_Object((1,3,6,1,4,1,4526,4,1,1,11),_SnmpTrapRcvIpType_Type())
snmpTrapRcvIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapRcvIpType.setStatus(_A)
_SnmpAPTrapRcvIpAddress_Type=IpAddress
_SnmpAPTrapRcvIpAddress_Object=MibScalar
snmpAPTrapRcvIpAddress=_SnmpAPTrapRcvIpAddress_Object((1,3,6,1,4,1,4526,4,1,1,12),_SnmpAPTrapRcvIpAddress_Type())
snmpAPTrapRcvIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAPTrapRcvIpAddress.setStatus(_A)
class _SnmpAPSNMPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SnmpAPSNMPEnable_Type.__name__=_C
_SnmpAPSNMPEnable_Object=MibScalar
snmpAPSNMPEnable=_SnmpAPSNMPEnable_Object((1,3,6,1,4,1,4526,4,1,1,13),_SnmpAPSNMPEnable_Type())
snmpAPSNMPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAPSNMPEnable.setStatus(_A)
class _SnmpAPCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_SnmpAPCommunity_Type.__name__=_G
_SnmpAPCommunity_Object=MibScalar
snmpAPCommunity=_SnmpAPCommunity_Object((1,3,6,1,4,1,4526,4,1,1,14),_SnmpAPCommunity_Type())
snmpAPCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAPCommunity.setStatus(_A)
class _SnmpAPAccessRight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('Read-Only',0),('Read-and-Write',1)))
_SnmpAPAccessRight_Type.__name__=_C
_SnmpAPAccessRight_Object=MibScalar
snmpAPAccessRight=_SnmpAPAccessRight_Object((1,3,6,1,4,1,4526,4,1,1,15),_SnmpAPAccessRight_Type())
snmpAPAccessRight.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAPAccessRight.setStatus(_A)
class _SnmpAPManagersType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('A-Specific-Station',0),('Any-Station',1)))
_SnmpAPManagersType_Type.__name__=_C
_SnmpAPManagersType_Object=MibScalar
snmpAPManagersType=_SnmpAPManagersType_Object((1,3,6,1,4,1,4526,4,1,1,16),_SnmpAPManagersType_Type())
snmpAPManagersType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAPManagersType.setStatus(_A)
_SnmpAPSpecificStationIp_Type=IpAddress
_SnmpAPSpecificStationIp_Object=MibScalar
snmpAPSpecificStationIp=_SnmpAPSpecificStationIp_Object((1,3,6,1,4,1,4526,4,1,1,17),_SnmpAPSpecificStationIp_Type())
snmpAPSpecificStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAPSpecificStationIp.setStatus(_A)
class _SnmpAPTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_SnmpAPTrapEnable_Type.__name__=_C
_SnmpAPTrapEnable_Object=MibScalar
snmpAPTrapEnable=_SnmpAPTrapEnable_Object((1,3,6,1,4,1,4526,4,1,1,18),_SnmpAPTrapEnable_Type())
snmpAPTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAPTrapEnable.setStatus(_A)
_WirelessAPConnectedStationGroup_ObjectIdentity=ObjectIdentity
wirelessAPConnectedStationGroup=_WirelessAPConnectedStationGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,2))
class _WirelessAPConnectedStationTableRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-refresh',0),('refresh',1)))
_WirelessAPConnectedStationTableRefresh_Type.__name__=_C
_WirelessAPConnectedStationTableRefresh_Object=MibScalar
wirelessAPConnectedStationTableRefresh=_WirelessAPConnectedStationTableRefresh_Object((1,3,6,1,4,1,4526,4,1,2,1),_WirelessAPConnectedStationTableRefresh_Type())
wirelessAPConnectedStationTableRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPConnectedStationTableRefresh.setStatus(_A)
_WirelessAPConnectedStation_ObjectIdentity=ObjectIdentity
wirelessAPConnectedStation=_WirelessAPConnectedStation_ObjectIdentity((1,3,6,1,4,1,4526,4,1,2,2))
_WirelessAPConnectedStationTable_Object=MibTable
wirelessAPConnectedStationTable=_WirelessAPConnectedStationTable_Object((1,3,6,1,4,1,4526,4,1,2,2,1))
if mibBuilder.loadTexts:wirelessAPConnectedStationTable.setStatus(_A)
_WirelessAPConnectedStationEntry_Object=MibTableRow
wirelessAPConnectedStationEntry=_WirelessAPConnectedStationEntry_Object((1,3,6,1,4,1,4526,4,1,2,2,1,1))
wirelessAPConnectedStationEntry.setIndexNames((0,_H,_N))
if mibBuilder.loadTexts:wirelessAPConnectedStationEntry.setStatus(_A)
_WirelessAPConnectedStationMacAddr_Type=PhysAddress
_WirelessAPConnectedStationMacAddr_Object=MibTableColumn
wirelessAPConnectedStationMacAddr=_WirelessAPConnectedStationMacAddr_Object((1,3,6,1,4,1,4526,4,1,2,2,1,1,2),_WirelessAPConnectedStationMacAddr_Type())
wirelessAPConnectedStationMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPConnectedStationMacAddr.setStatus(_A)
class _WirelessAPConnectedStationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('associated',0),('athenticating',1),('authenticated',2),('not-associated',3)))
_WirelessAPConnectedStationStatus_Type.__name__=_C
_WirelessAPConnectedStationStatus_Object=MibTableColumn
wirelessAPConnectedStationStatus=_WirelessAPConnectedStationStatus_Object((1,3,6,1,4,1,4526,4,1,2,2,1,1,3),_WirelessAPConnectedStationStatus_Type())
wirelessAPConnectedStationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPConnectedStationStatus.setStatus(_A)
class _WirelessAPControl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('on',1)))
_WirelessAPControl_Type.__name__=_C
_WirelessAPControl_Object=MibScalar
wirelessAPControl=_WirelessAPControl_Object((1,3,6,1,4,1,4526,4,1,2,3),_WirelessAPControl_Type())
wirelessAPControl.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPControl.setStatus(_A)
_WirelessAPControlList_ObjectIdentity=ObjectIdentity
wirelessAPControlList=_WirelessAPControlList_ObjectIdentity((1,3,6,1,4,1,4526,4,1,2,4))
_WirelessAPControlListTable_Object=MibTable
wirelessAPControlListTable=_WirelessAPControlListTable_Object((1,3,6,1,4,1,4526,4,1,2,4,1))
if mibBuilder.loadTexts:wirelessAPControlListTable.setStatus(_A)
_WirelessAPControlListEntry_Object=MibTableRow
wirelessAPControlListEntry=_WirelessAPControlListEntry_Object((1,3,6,1,4,1,4526,4,1,2,4,1,1))
wirelessAPControlListEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:wirelessAPControlListEntry.setStatus(_A)
_WirelessAPControlListMacAddr_Type=PhysAddress
_WirelessAPControlListMacAddr_Object=MibTableColumn
wirelessAPControlListMacAddr=_WirelessAPControlListMacAddr_Object((1,3,6,1,4,1,4526,4,1,2,4,1,1,2),_WirelessAPControlListMacAddr_Type())
wirelessAPControlListMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPControlListMacAddr.setStatus(_A)
_WirelessAPCtlOperate_ObjectIdentity=ObjectIdentity
wirelessAPCtlOperate=_WirelessAPCtlOperate_ObjectIdentity((1,3,6,1,4,1,4526,4,1,2,5))
_WirelessAPAddCtlMacAddr_Type=PhysAddress
_WirelessAPAddCtlMacAddr_Object=MibScalar
wirelessAPAddCtlMacAddr=_WirelessAPAddCtlMacAddr_Object((1,3,6,1,4,1,4526,4,1,2,5,1),_WirelessAPAddCtlMacAddr_Type())
wirelessAPAddCtlMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPAddCtlMacAddr.setStatus(_A)
_WirelessAPDelCtlMacAddr_Type=PhysAddress
_WirelessAPDelCtlMacAddr_Object=MibScalar
wirelessAPDelCtlMacAddr=_WirelessAPDelCtlMacAddr_Object((1,3,6,1,4,1,4526,4,1,2,5,2),_WirelessAPDelCtlMacAddr_Type())
wirelessAPDelCtlMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPDelCtlMacAddr.setStatus(_A)
_WirelessAPIfTrafficGroup_ObjectIdentity=ObjectIdentity
wirelessAPIfTrafficGroup=_WirelessAPIfTrafficGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,3))
_WirelessAPIfWiredTrafficGroup_ObjectIdentity=ObjectIdentity
wirelessAPIfWiredTrafficGroup=_WirelessAPIfWiredTrafficGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,3,1))
_WirelessAPIfWiredTotalOctetsIn_Type=Counter32
_WirelessAPIfWiredTotalOctetsIn_Object=MibScalar
wirelessAPIfWiredTotalOctetsIn=_WirelessAPIfWiredTotalOctetsIn_Object((1,3,6,1,4,1,4526,4,1,3,1,1),_WirelessAPIfWiredTotalOctetsIn_Type())
wirelessAPIfWiredTotalOctetsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredTotalOctetsIn.setStatus(_A)
_WirelessAPIfWiredTotalOctetsOut_Type=Counter32
_WirelessAPIfWiredTotalOctetsOut_Object=MibScalar
wirelessAPIfWiredTotalOctetsOut=_WirelessAPIfWiredTotalOctetsOut_Object((1,3,6,1,4,1,4526,4,1,3,1,2),_WirelessAPIfWiredTotalOctetsOut_Type())
wirelessAPIfWiredTotalOctetsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredTotalOctetsOut.setStatus(_A)
_WirelessAPIfWiredPacketsIn_Type=Counter32
_WirelessAPIfWiredPacketsIn_Object=MibScalar
wirelessAPIfWiredPacketsIn=_WirelessAPIfWiredPacketsIn_Object((1,3,6,1,4,1,4526,4,1,3,1,3),_WirelessAPIfWiredPacketsIn_Type())
wirelessAPIfWiredPacketsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredPacketsIn.setStatus(_A)
_WirelessAPIfWiredPacketsOut_Type=Counter32
_WirelessAPIfWiredPacketsOut_Object=MibScalar
wirelessAPIfWiredPacketsOut=_WirelessAPIfWiredPacketsOut_Object((1,3,6,1,4,1,4526,4,1,3,1,4),_WirelessAPIfWiredPacketsOut_Type())
wirelessAPIfWiredPacketsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredPacketsOut.setStatus(_A)
_WirelessAPIfWiredThroughputIn_Type=Counter32
_WirelessAPIfWiredThroughputIn_Object=MibScalar
wirelessAPIfWiredThroughputIn=_WirelessAPIfWiredThroughputIn_Object((1,3,6,1,4,1,4526,4,1,3,1,5),_WirelessAPIfWiredThroughputIn_Type())
wirelessAPIfWiredThroughputIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredThroughputIn.setStatus(_A)
_WirelessAPIfWiredThroughputOut_Type=Counter32
_WirelessAPIfWiredThroughputOut_Object=MibScalar
wirelessAPIfWiredThroughputOut=_WirelessAPIfWiredThroughputOut_Object((1,3,6,1,4,1,4526,4,1,3,1,6),_WirelessAPIfWiredThroughputOut_Type())
wirelessAPIfWiredThroughputOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredThroughputOut.setStatus(_A)
_WirelessAPIfWiredErrorsIn_Type=Counter32
_WirelessAPIfWiredErrorsIn_Object=MibScalar
wirelessAPIfWiredErrorsIn=_WirelessAPIfWiredErrorsIn_Object((1,3,6,1,4,1,4526,4,1,3,1,7),_WirelessAPIfWiredErrorsIn_Type())
wirelessAPIfWiredErrorsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredErrorsIn.setStatus(_A)
_WirelessAPIfWiredErrorsOut_Type=Counter32
_WirelessAPIfWiredErrorsOut_Object=MibScalar
wirelessAPIfWiredErrorsOut=_WirelessAPIfWiredErrorsOut_Object((1,3,6,1,4,1,4526,4,1,3,1,8),_WirelessAPIfWiredErrorsOut_Type())
wirelessAPIfWiredErrorsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWiredErrorsOut.setStatus(_A)
class _WirelessAPIfWiredTrafficResetCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_WirelessAPIfWiredTrafficResetCounter_Type.__name__=_C
_WirelessAPIfWiredTrafficResetCounter_Object=MibScalar
wirelessAPIfWiredTrafficResetCounter=_WirelessAPIfWiredTrafficResetCounter_Object((1,3,6,1,4,1,4526,4,1,3,1,9),_WirelessAPIfWiredTrafficResetCounter_Type())
wirelessAPIfWiredTrafficResetCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPIfWiredTrafficResetCounter.setStatus(_A)
_WirelessAPIfWlanTrafficGroup_ObjectIdentity=ObjectIdentity
wirelessAPIfWlanTrafficGroup=_WirelessAPIfWlanTrafficGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,3,2))
_WirelessAPIfWLANTotalOctetsIn_Type=Counter32
_WirelessAPIfWLANTotalOctetsIn_Object=MibScalar
wirelessAPIfWLANTotalOctetsIn=_WirelessAPIfWLANTotalOctetsIn_Object((1,3,6,1,4,1,4526,4,1,3,2,1),_WirelessAPIfWLANTotalOctetsIn_Type())
wirelessAPIfWLANTotalOctetsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANTotalOctetsIn.setStatus(_A)
_WirelessAPIfWLANTotalOctetsOut_Type=Counter32
_WirelessAPIfWLANTotalOctetsOut_Object=MibScalar
wirelessAPIfWLANTotalOctetsOut=_WirelessAPIfWLANTotalOctetsOut_Object((1,3,6,1,4,1,4526,4,1,3,2,2),_WirelessAPIfWLANTotalOctetsOut_Type())
wirelessAPIfWLANTotalOctetsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANTotalOctetsOut.setStatus(_A)
_WirelessAPIfWLANUnicastPacketsIn_Type=Counter32
_WirelessAPIfWLANUnicastPacketsIn_Object=MibScalar
wirelessAPIfWLANUnicastPacketsIn=_WirelessAPIfWLANUnicastPacketsIn_Object((1,3,6,1,4,1,4526,4,1,3,2,3),_WirelessAPIfWLANUnicastPacketsIn_Type())
wirelessAPIfWLANUnicastPacketsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANUnicastPacketsIn.setStatus(_A)
_WirelessAPIfWLANUnicastPacketsOut_Type=Counter32
_WirelessAPIfWLANUnicastPacketsOut_Object=MibScalar
wirelessAPIfWLANUnicastPacketsOut=_WirelessAPIfWLANUnicastPacketsOut_Object((1,3,6,1,4,1,4526,4,1,3,2,4),_WirelessAPIfWLANUnicastPacketsOut_Type())
wirelessAPIfWLANUnicastPacketsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANUnicastPacketsOut.setStatus(_A)
_WirelessAPIfWLANBroadcastPacketsIn_Type=Counter32
_WirelessAPIfWLANBroadcastPacketsIn_Object=MibScalar
wirelessAPIfWLANBroadcastPacketsIn=_WirelessAPIfWLANBroadcastPacketsIn_Object((1,3,6,1,4,1,4526,4,1,3,2,5),_WirelessAPIfWLANBroadcastPacketsIn_Type())
wirelessAPIfWLANBroadcastPacketsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANBroadcastPacketsIn.setStatus(_A)
_WirelessAPIfWLANBroadcastPacketsOut_Type=Counter32
_WirelessAPIfWLANBroadcastPacketsOut_Object=MibScalar
wirelessAPIfWLANBroadcastPacketsOut=_WirelessAPIfWLANBroadcastPacketsOut_Object((1,3,6,1,4,1,4526,4,1,3,2,6),_WirelessAPIfWLANBroadcastPacketsOut_Type())
wirelessAPIfWLANBroadcastPacketsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANBroadcastPacketsOut.setStatus(_A)
_WirelessAPIfWLANMulticastPacketsIn_Type=Counter32
_WirelessAPIfWLANMulticastPacketsIn_Object=MibScalar
wirelessAPIfWLANMulticastPacketsIn=_WirelessAPIfWLANMulticastPacketsIn_Object((1,3,6,1,4,1,4526,4,1,3,2,7),_WirelessAPIfWLANMulticastPacketsIn_Type())
wirelessAPIfWLANMulticastPacketsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANMulticastPacketsIn.setStatus(_A)
_WirelessAPIfWLANMulticastPacketsOut_Type=Counter32
_WirelessAPIfWLANMulticastPacketsOut_Object=MibScalar
wirelessAPIfWLANMulticastPacketsOut=_WirelessAPIfWLANMulticastPacketsOut_Object((1,3,6,1,4,1,4526,4,1,3,2,8),_WirelessAPIfWLANMulticastPacketsOut_Type())
wirelessAPIfWLANMulticastPacketsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANMulticastPacketsOut.setStatus(_A)
_WirelessAPIfWLANThroughputIn_Type=Counter32
_WirelessAPIfWLANThroughputIn_Object=MibScalar
wirelessAPIfWLANThroughputIn=_WirelessAPIfWLANThroughputIn_Object((1,3,6,1,4,1,4526,4,1,3,2,9),_WirelessAPIfWLANThroughputIn_Type())
wirelessAPIfWLANThroughputIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANThroughputIn.setStatus(_A)
_WirelessAPIfWLANThroughputOut_Type=Counter32
_WirelessAPIfWLANThroughputOut_Object=MibScalar
wirelessAPIfWLANThroughputOut=_WirelessAPIfWLANThroughputOut_Object((1,3,6,1,4,1,4526,4,1,3,2,10),_WirelessAPIfWLANThroughputOut_Type())
wirelessAPIfWLANThroughputOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANThroughputOut.setStatus(_A)
_WirelessAPIfWLANPacketsIn_Type=Counter32
_WirelessAPIfWLANPacketsIn_Object=MibScalar
wirelessAPIfWLANPacketsIn=_WirelessAPIfWLANPacketsIn_Object((1,3,6,1,4,1,4526,4,1,3,2,11),_WirelessAPIfWLANPacketsIn_Type())
wirelessAPIfWLANPacketsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANPacketsIn.setStatus(_A)
_WirelessAPIfWLANPacketsOut_Type=Counter32
_WirelessAPIfWLANPacketsOut_Object=MibScalar
wirelessAPIfWLANPacketsOut=_WirelessAPIfWLANPacketsOut_Object((1,3,6,1,4,1,4526,4,1,3,2,12),_WirelessAPIfWLANPacketsOut_Type())
wirelessAPIfWLANPacketsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPIfWLANPacketsOut.setStatus(_A)
class _WirelessAPIfWLANTrafficResetCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_WirelessAPIfWLANTrafficResetCounter_Type.__name__=_C
_WirelessAPIfWLANTrafficResetCounter_Object=MibScalar
wirelessAPIfWLANTrafficResetCounter=_WirelessAPIfWLANTrafficResetCounter_Object((1,3,6,1,4,1,4526,4,1,3,2,13),_WirelessAPIfWLANTrafficResetCounter_Type())
wirelessAPIfWLANTrafficResetCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPIfWLANTrafficResetCounter.setStatus(_A)
_WirelessAPIfSettingsGroup_ObjectIdentity=ObjectIdentity
wirelessAPIfSettingsGroup=_WirelessAPIfSettingsGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,4))
class _WirelessAPDHCPClientObtainIPchoice_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),('automatic',1)))
_WirelessAPDHCPClientObtainIPchoice_Type.__name__=_C
_WirelessAPDHCPClientObtainIPchoice_Object=MibScalar
wirelessAPDHCPClientObtainIPchoice=_WirelessAPDHCPClientObtainIPchoice_Object((1,3,6,1,4,1,4526,4,1,4,1),_WirelessAPDHCPClientObtainIPchoice_Type())
wirelessAPDHCPClientObtainIPchoice.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPDHCPClientObtainIPchoice.setStatus(_A)
_WirelessAPDHCPClientIPaddr_Type=IpAddress
_WirelessAPDHCPClientIPaddr_Object=MibScalar
wirelessAPDHCPClientIPaddr=_WirelessAPDHCPClientIPaddr_Object((1,3,6,1,4,1,4526,4,1,4,2),_WirelessAPDHCPClientIPaddr_Type())
wirelessAPDHCPClientIPaddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPDHCPClientIPaddr.setStatus(_A)
_WirelessAPDHCPClientIPsubnetMask_Type=IpAddress
_WirelessAPDHCPClientIPsubnetMask_Object=MibScalar
wirelessAPDHCPClientIPsubnetMask=_WirelessAPDHCPClientIPsubnetMask_Object((1,3,6,1,4,1,4526,4,1,4,3),_WirelessAPDHCPClientIPsubnetMask_Type())
wirelessAPDHCPClientIPsubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPDHCPClientIPsubnetMask.setStatus(_A)
_WirelessAPDHCPClientGateway_Type=IpAddress
_WirelessAPDHCPClientGateway_Object=MibScalar
wirelessAPDHCPClientGateway=_WirelessAPDHCPClientGateway_Object((1,3,6,1,4,1,4526,4,1,4,4),_WirelessAPDHCPClientGateway_Type())
wirelessAPDHCPClientGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPDHCPClientGateway.setStatus(_A)
_WirelessAPDHCPClientPriDNS_Type=IpAddress
_WirelessAPDHCPClientPriDNS_Object=MibScalar
wirelessAPDHCPClientPriDNS=_WirelessAPDHCPClientPriDNS_Object((1,3,6,1,4,1,4526,4,1,4,5),_WirelessAPDHCPClientPriDNS_Type())
wirelessAPDHCPClientPriDNS.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPDHCPClientPriDNS.setStatus(_A)
_WirelessAPDHCPClientSecDNS_Type=IpAddress
_WirelessAPDHCPClientSecDNS_Object=MibScalar
wirelessAPDHCPClientSecDNS=_WirelessAPDHCPClientSecDNS_Object((1,3,6,1,4,1,4526,4,1,4,6),_WirelessAPDHCPClientSecDNS_Type())
wirelessAPDHCPClientSecDNS.setMaxAccess(_D)
if mibBuilder.loadTexts:wirelessAPDHCPClientSecDNS.setStatus(_A)
_WirelessAPDHCPClientStaticIPaddr_Type=IpAddress
_WirelessAPDHCPClientStaticIPaddr_Object=MibScalar
wirelessAPDHCPClientStaticIPaddr=_WirelessAPDHCPClientStaticIPaddr_Object((1,3,6,1,4,1,4526,4,1,4,7),_WirelessAPDHCPClientStaticIPaddr_Type())
wirelessAPDHCPClientStaticIPaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPDHCPClientStaticIPaddr.setStatus(_A)
_WirelessAPDHCPClientStaticIPsubnetMask_Type=IpAddress
_WirelessAPDHCPClientStaticIPsubnetMask_Object=MibScalar
wirelessAPDHCPClientStaticIPsubnetMask=_WirelessAPDHCPClientStaticIPsubnetMask_Object((1,3,6,1,4,1,4526,4,1,4,8),_WirelessAPDHCPClientStaticIPsubnetMask_Type())
wirelessAPDHCPClientStaticIPsubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPDHCPClientStaticIPsubnetMask.setStatus(_A)
_WirelessAPDHCPClientStaticGateway_Type=IpAddress
_WirelessAPDHCPClientStaticGateway_Object=MibScalar
wirelessAPDHCPClientStaticGateway=_WirelessAPDHCPClientStaticGateway_Object((1,3,6,1,4,1,4526,4,1,4,9),_WirelessAPDHCPClientStaticGateway_Type())
wirelessAPDHCPClientStaticGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPDHCPClientStaticGateway.setStatus(_A)
_WirelessAPDHCPClientStaticPriDNS_Type=IpAddress
_WirelessAPDHCPClientStaticPriDNS_Object=MibScalar
wirelessAPDHCPClientStaticPriDNS=_WirelessAPDHCPClientStaticPriDNS_Object((1,3,6,1,4,1,4526,4,1,4,10),_WirelessAPDHCPClientStaticPriDNS_Type())
wirelessAPDHCPClientStaticPriDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPDHCPClientStaticPriDNS.setStatus(_A)
_WirelessAPDHCPClientStaticSecDNS_Type=IpAddress
_WirelessAPDHCPClientStaticSecDNS_Object=MibScalar
wirelessAPDHCPClientStaticSecDNS=_WirelessAPDHCPClientStaticSecDNS_Object((1,3,6,1,4,1,4526,4,1,4,11),_WirelessAPDHCPClientStaticSecDNS_Type())
wirelessAPDHCPClientStaticSecDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPDHCPClientStaticSecDNS.setStatus(_A)
class _WirelessAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WirelessAPName_Type.__name__=_G
_WirelessAPName_Object=MibScalar
wirelessAPName=_WirelessAPName_Object((1,3,6,1,4,1,4526,4,1,4,12),_WirelessAPName_Type())
wirelessAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPName.setStatus(_A)
class _WirelessAPWINSchoice_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPWINSchoice_Type.__name__=_C
_WirelessAPWINSchoice_Object=MibScalar
wirelessAPWINSchoice=_WirelessAPWINSchoice_Object((1,3,6,1,4,1,4526,4,1,4,13),_WirelessAPWINSchoice_Type())
wirelessAPWINSchoice.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPWINSchoice.setStatus(_A)
class _WirelessAPWINSServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WirelessAPWINSServerName_Type.__name__=_G
_WirelessAPWINSServerName_Object=MibScalar
wirelessAPWINSServerName=_WirelessAPWINSServerName_Object((1,3,6,1,4,1,4526,4,1,4,14),_WirelessAPWINSServerName_Type())
wirelessAPWINSServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPWINSServerName.setStatus(_A)
_WirelessAPWirelessSettingsGroup_ObjectIdentity=ObjectIdentity
wirelessAPWirelessSettingsGroup=_WirelessAPWirelessSettingsGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,5))
class _WirelessAPCountryDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',0),('africa',1),('asia',2),('australia',3),('canada',4),('europe',5),('france',6),('israel',7),('japan',8),('mexico',9),('southAmerica',10),('usa',11)))
_WirelessAPCountryDomain_Type.__name__=_C
_WirelessAPCountryDomain_Object=MibScalar
wirelessAPCountryDomain=_WirelessAPCountryDomain_Object((1,3,6,1,4,1,4526,4,1,5,1),_WirelessAPCountryDomain_Type())
wirelessAPCountryDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPCountryDomain.setStatus(_A)
class _WirelessAPChannelNo_Type(Integer32):defaultValue=11;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_WirelessAPChannelNo_Type.__name__=_C
_WirelessAPChannelNo_Object=MibScalar
wirelessAPChannelNo=_WirelessAPChannelNo_Object((1,3,6,1,4,1,4526,4,1,5,2),_WirelessAPChannelNo_Type())
wirelessAPChannelNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPChannelNo.setStatus(_A)
class _WirelessAPSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WirelessAPSSID_Type.__name__=_G
_WirelessAPSSID_Object=MibScalar
wirelessAPSSID=_WirelessAPSSID_Object((1,3,6,1,4,1,4526,4,1,5,3),_WirelessAPSSID_Type())
wirelessAPSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPSSID.setStatus(_A)
class _WirelessAPPassphrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WirelessAPPassphrase_Type.__name__=_G
_WirelessAPPassphrase_Object=MibScalar
wirelessAPPassphrase=_WirelessAPPassphrase_Object((1,3,6,1,4,1,4526,4,1,5,7),_WirelessAPPassphrase_Type())
wirelessAPPassphrase.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPPassphrase.setStatus(_A)
class _WirelessAPGenerateKeysEnabled_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPGenerateKeysEnabled_Type.__name__=_C
_WirelessAPGenerateKeysEnabled_Object=MibScalar
wirelessAPGenerateKeysEnabled=_WirelessAPGenerateKeysEnabled_Object((1,3,6,1,4,1,4526,4,1,5,8),_WirelessAPGenerateKeysEnabled_Type())
wirelessAPGenerateKeysEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPGenerateKeysEnabled.setStatus(_A)
_WirelessAPKeysSet_ObjectIdentity=ObjectIdentity
wirelessAPKeysSet=_WirelessAPKeysSet_ObjectIdentity((1,3,6,1,4,1,4526,4,1,5,9))
_WirelessAPKeysSetTable_Object=MibTable
wirelessAPKeysSetTable=_WirelessAPKeysSetTable_Object((1,3,6,1,4,1,4526,4,1,5,9,1))
if mibBuilder.loadTexts:wirelessAPKeysSetTable.setStatus(_A)
_WirelessAPKeysSetEntry_Object=MibTableRow
wirelessAPKeysSetEntry=_WirelessAPKeysSetEntry_Object((1,3,6,1,4,1,4526,4,1,5,9,1,1))
wirelessAPKeysSetEntry.setIndexNames((0,_H,_P))
if mibBuilder.loadTexts:wirelessAPKeysSetEntry.setStatus(_A)
class _WirelessAPKeysSetEnabled_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPKeysSetEnabled_Type.__name__=_C
_WirelessAPKeysSetEnabled_Object=MibTableColumn
wirelessAPKeysSetEnabled=_WirelessAPKeysSetEnabled_Object((1,3,6,1,4,1,4526,4,1,5,9,1,1,2),_WirelessAPKeysSetEnabled_Type())
wirelessAPKeysSetEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPKeysSetEnabled.setStatus(_A)
class _WirelessAPKeys_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_WirelessAPKeys_Type.__name__=_J
_WirelessAPKeys_Object=MibTableColumn
wirelessAPKeys=_WirelessAPKeys_Object((1,3,6,1,4,1,4526,4,1,5,9,1,1,3),_WirelessAPKeys_Type())
wirelessAPKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPKeys.setStatus(_A)
class _WirelessAPBasicRateChoice_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('auto',0),('fixed',1)))
_WirelessAPBasicRateChoice_Type.__name__=_C
_WirelessAPBasicRateChoice_Object=MibScalar
wirelessAPBasicRateChoice=_WirelessAPBasicRateChoice_Object((1,3,6,1,4,1,4526,4,1,5,10),_WirelessAPBasicRateChoice_Type())
wirelessAPBasicRateChoice.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPBasicRateChoice.setStatus(_A)
_WirelessAPFixedRate_ObjectIdentity=ObjectIdentity
wirelessAPFixedRate=_WirelessAPFixedRate_ObjectIdentity((1,3,6,1,4,1,4526,4,1,5,11))
class _WirelessAPFixedRate1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('oneM-disabled',0),('oneM-enabled',1)))
_WirelessAPFixedRate1_Type.__name__=_C
_WirelessAPFixedRate1_Object=MibScalar
wirelessAPFixedRate1=_WirelessAPFixedRate1_Object((1,3,6,1,4,1,4526,4,1,5,11,1),_WirelessAPFixedRate1_Type())
wirelessAPFixedRate1.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPFixedRate1.setStatus(_A)
class _WirelessAPFixedRate2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('twoM-disabled',0),('twoM-enabled',1)))
_WirelessAPFixedRate2_Type.__name__=_C
_WirelessAPFixedRate2_Object=MibScalar
wirelessAPFixedRate2=_WirelessAPFixedRate2_Object((1,3,6,1,4,1,4526,4,1,5,11,2),_WirelessAPFixedRate2_Type())
wirelessAPFixedRate2.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPFixedRate2.setStatus(_A)
class _WirelessAPFixedRate5_5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fiveDotFiveM-disabled',0),('fiveDotFiveM-enabled',1)))
_WirelessAPFixedRate5_5_Type.__name__=_C
_WirelessAPFixedRate5_5_Object=MibScalar
wirelessAPFixedRate5_5=_WirelessAPFixedRate5_5_Object((1,3,6,1,4,1,4526,4,1,5,11,3),_WirelessAPFixedRate5_5_Type())
wirelessAPFixedRate5_5.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPFixedRate5_5.setStatus(_A)
class _WirelessAPFixedRate11_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('elevenM-disabled',0),('elevenM-enabled',1)))
_WirelessAPFixedRate11_Type.__name__=_C
_WirelessAPFixedRate11_Object=MibScalar
wirelessAPFixedRate11=_WirelessAPFixedRate11_Object((1,3,6,1,4,1,4526,4,1,5,11,4),_WirelessAPFixedRate11_Type())
wirelessAPFixedRate11.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPFixedRate11.setStatus(_A)
class _WirelessAPRTSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_WirelessAPRTSThreshold_Type.__name__=_C
_WirelessAPRTSThreshold_Object=MibScalar
wirelessAPRTSThreshold=_WirelessAPRTSThreshold_Object((1,3,6,1,4,1,4526,4,1,5,12),_WirelessAPRTSThreshold_Type())
wirelessAPRTSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRTSThreshold.setStatus(_A)
class _WirelessAPFragmentationThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_WirelessAPFragmentationThreshold_Type.__name__=_C
_WirelessAPFragmentationThreshold_Object=MibScalar
wirelessAPFragmentationThreshold=_WirelessAPFragmentationThreshold_Object((1,3,6,1,4,1,4526,4,1,5,13),_WirelessAPFragmentationThreshold_Type())
wirelessAPFragmentationThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPFragmentationThreshold.setStatus(_A)
class _WirelessAPBeaconPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WirelessAPBeaconPeriod_Type.__name__=_C
_WirelessAPBeaconPeriod_Object=MibScalar
wirelessAPBeaconPeriod=_WirelessAPBeaconPeriod_Object((1,3,6,1,4,1,4526,4,1,5,14),_WirelessAPBeaconPeriod_Type())
wirelessAPBeaconPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPBeaconPeriod.setStatus(_A)
class _WirelessAPShortPreambleOptionImplemented_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('short',0),('long',1)))
_WirelessAPShortPreambleOptionImplemented_Type.__name__=_C
_WirelessAPShortPreambleOptionImplemented_Object=MibScalar
wirelessAPShortPreambleOptionImplemented=_WirelessAPShortPreambleOptionImplemented_Object((1,3,6,1,4,1,4526,4,1,5,15),_WirelessAPShortPreambleOptionImplemented_Type())
wirelessAPShortPreambleOptionImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPShortPreambleOptionImplemented.setStatus(_A)
class _WirelessAPAntennaSelection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('diversity',3)))
_WirelessAPAntennaSelection_Type.__name__=_C
_WirelessAPAntennaSelection_Object=MibScalar
wirelessAPAntennaSelection=_WirelessAPAntennaSelection_Object((1,3,6,1,4,1,4526,4,1,5,16),_WirelessAPAntennaSelection_Type())
wirelessAPAntennaSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPAntennaSelection.setStatus(_A)
class _WirelessAPMaximumTransmitPowerLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('eighteendbm',1),('seventeendbm',2),('fifteendbm',3),('thirteendbm',4),('sevendbm',5),('zerodbm',6)))
_WirelessAPMaximumTransmitPowerLevel_Type.__name__=_C
_WirelessAPMaximumTransmitPowerLevel_Object=MibScalar
wirelessAPMaximumTransmitPowerLevel=_WirelessAPMaximumTransmitPowerLevel_Object((1,3,6,1,4,1,4526,4,1,5,17),_WirelessAPMaximumTransmitPowerLevel_Type())
wirelessAPMaximumTransmitPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPMaximumTransmitPowerLevel.setStatus(_A)
class _WirelessAPOperatingMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('eight0twoDot1xAP',0),('noneight0twoDot1xAP',1)))
_WirelessAPOperatingMode_Type.__name__=_C
_WirelessAPOperatingMode_Object=MibScalar
wirelessAPOperatingMode=_WirelessAPOperatingMode_Object((1,3,6,1,4,1,4526,4,1,5,18),_WirelessAPOperatingMode_Type())
wirelessAPOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPOperatingMode.setStatus(_A)
class _WirelessAPSSIDEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPSSIDEnabled_Type.__name__=_C
_WirelessAPSSIDEnabled_Object=MibScalar
wirelessAPSSIDEnabled=_WirelessAPSSIDEnabled_Object((1,3,6,1,4,1,4526,4,1,5,19),_WirelessAPSSIDEnabled_Type())
wirelessAPSSIDEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPSSIDEnabled.setStatus(_A)
_WirelessAPSecuritySettingsGroup_ObjectIdentity=ObjectIdentity
wirelessAPSecuritySettingsGroup=_WirelessAPSecuritySettingsGroup_ObjectIdentity((1,3,6,1,4,1,4526,4,1,6))
class _WirelessAP802dot1xSecurityEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_E,1)))
_WirelessAP802dot1xSecurityEnabled_Type.__name__=_C
_WirelessAP802dot1xSecurityEnabled_Object=MibScalar
wirelessAP802dot1xSecurityEnabled=_WirelessAP802dot1xSecurityEnabled_Object((1,3,6,1,4,1,4526,4,1,6,1),_WirelessAP802dot1xSecurityEnabled_Type())
wirelessAP802dot1xSecurityEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAP802dot1xSecurityEnabled.setStatus(_A)
class _WirelessAPEAPauthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('NotAllowEAP-MD5',0),('AllowEAP-MD5',1)))
_WirelessAPEAPauthType_Type.__name__=_C
_WirelessAPEAPauthType_Object=MibScalar
wirelessAPEAPauthType=_WirelessAPEAPauthType_Object((1,3,6,1,4,1,4526,4,1,6,2),_WirelessAPEAPauthType_Type())
wirelessAPEAPauthType.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPEAPauthType.setStatus(_A)
_WirelessAPRadiusServer_Type=DisplayString
_WirelessAPRadiusServer_Object=MibScalar
wirelessAPRadiusServer=_WirelessAPRadiusServer_Object((1,3,6,1,4,1,4526,4,1,6,3),_WirelessAPRadiusServer_Type())
wirelessAPRadiusServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadiusServer.setStatus(_A)
class _WirelessAPRadiusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WirelessAPRadiusPort_Type.__name__=_C
_WirelessAPRadiusPort_Object=MibScalar
wirelessAPRadiusPort=_WirelessAPRadiusPort_Object((1,3,6,1,4,1,4526,4,1,6,4),_WirelessAPRadiusPort_Type())
wirelessAPRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadiusPort.setStatus(_A)
class _WirelessAPSharedKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WirelessAPSharedKey_Type.__name__=_G
_WirelessAPSharedKey_Object=MibScalar
wirelessAPSharedKey=_WirelessAPSharedKey_Object((1,3,6,1,4,1,4526,4,1,6,5),_WirelessAPSharedKey_Type())
wirelessAPSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPSharedKey.setStatus(_A)
_WirelessAPRadiusServer2_Type=DisplayString
_WirelessAPRadiusServer2_Object=MibScalar
wirelessAPRadiusServer2=_WirelessAPRadiusServer2_Object((1,3,6,1,4,1,4526,4,1,6,7),_WirelessAPRadiusServer2_Type())
wirelessAPRadiusServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadiusServer2.setStatus(_A)
class _WirelessAPRadAccountPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WirelessAPRadAccountPort_Type.__name__=_C
_WirelessAPRadAccountPort_Object=MibScalar
wirelessAPRadAccountPort=_WirelessAPRadAccountPort_Object((1,3,6,1,4,1,4526,4,1,6,11),_WirelessAPRadAccountPort_Type())
wirelessAPRadAccountPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadAccountPort.setStatus(_A)
class _WirelessAPKeyExchange_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPKeyExchange_Type.__name__=_C
_WirelessAPKeyExchange_Object=MibScalar
wirelessAPKeyExchange=_WirelessAPKeyExchange_Object((1,3,6,1,4,1,4526,4,1,6,16),_WirelessAPKeyExchange_Type())
wirelessAPKeyExchange.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPKeyExchange.setStatus(_A)
class _WirelessAPKeyExchangeKeylife_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WirelessAPKeyExchangeKeylife_Type.__name__=_C
_WirelessAPKeyExchangeKeylife_Object=MibScalar
wirelessAPKeyExchangeKeylife=_WirelessAPKeyExchangeKeylife_Object((1,3,6,1,4,1,4526,4,1,6,17),_WirelessAPKeyExchangeKeylife_Type())
wirelessAPKeyExchangeKeylife.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPKeyExchangeKeylife.setStatus(_A)
class _WirelessAPRadAccountEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPRadAccountEnable_Type.__name__=_C
_WirelessAPRadAccountEnable_Object=MibScalar
wirelessAPRadAccountEnable=_WirelessAPRadAccountEnable_Object((1,3,6,1,4,1,4526,4,1,6,18),_WirelessAPRadAccountEnable_Type())
wirelessAPRadAccountEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadAccountEnable.setStatus(_A)
class _WirelessAPMacAuthEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPMacAuthEnable_Type.__name__=_C
_WirelessAPMacAuthEnable_Object=MibScalar
wirelessAPMacAuthEnable=_WirelessAPMacAuthEnable_Object((1,3,6,1,4,1,4526,4,1,6,19),_WirelessAPMacAuthEnable_Type())
wirelessAPMacAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPMacAuthEnable.setStatus(_A)
class _WirelessAPRadAccountUpdateEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WirelessAPRadAccountUpdateEnable_Type.__name__=_C
_WirelessAPRadAccountUpdateEnable_Object=MibScalar
wirelessAPRadAccountUpdateEnable=_WirelessAPRadAccountUpdateEnable_Object((1,3,6,1,4,1,4526,4,1,6,21),_WirelessAPRadAccountUpdateEnable_Type())
wirelessAPRadAccountUpdateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadAccountUpdateEnable.setStatus(_A)
class _WirelessAPRadAccountUpdatePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WirelessAPRadAccountUpdatePeriod_Type.__name__=_C
_WirelessAPRadAccountUpdatePeriod_Object=MibScalar
wirelessAPRadAccountUpdatePeriod=_WirelessAPRadAccountUpdatePeriod_Object((1,3,6,1,4,1,4526,4,1,6,22),_WirelessAPRadAccountUpdatePeriod_Type())
wirelessAPRadAccountUpdatePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadAccountUpdatePeriod.setStatus(_A)
class _WirelessAPRadAccountIdlePeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_WirelessAPRadAccountIdlePeriod_Type.__name__=_C
_WirelessAPRadAccountIdlePeriod_Object=MibScalar
wirelessAPRadAccountIdlePeriod=_WirelessAPRadAccountIdlePeriod_Object((1,3,6,1,4,1,4526,4,1,6,23),_WirelessAPRadAccountIdlePeriod_Type())
wirelessAPRadAccountIdlePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPRadAccountIdlePeriod.setStatus(_A)
class _WirelessTIOperateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5)));namedValues=NamedValues(*(('WirelessAccessPoint',0),('RepeaterAccessPoint',2),('ClientAccessPoint',3),('Point-to-PointBridge',4),('Point-to-Multi-PointBridge',5)))
_WirelessTIOperateMode_Type.__name__=_C
_WirelessTIOperateMode_Object=MibScalar
wirelessTIOperateMode=_WirelessTIOperateMode_Object((1,3,6,1,4,1,4526,4,1,6,25),_WirelessTIOperateMode_Type())
wirelessTIOperateMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessTIOperateMode.setStatus(_A)
_WirelessTIDstMac_Type=PhysAddress
_WirelessTIDstMac_Object=MibScalar
wirelessTIDstMac=_WirelessTIDstMac_Object((1,3,6,1,4,1,4526,4,1,6,26),_WirelessTIDstMac_Type())
wirelessTIDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessTIDstMac.setStatus(_A)
class _WirelessTIIsolation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('on',1)))
_WirelessTIIsolation_Type.__name__=_C
_WirelessTIIsolation_Object=MibScalar
wirelessTIIsolation=_WirelessTIIsolation_Object((1,3,6,1,4,1,4526,4,1,6,28),_WirelessTIIsolation_Type())
wirelessTIIsolation.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessTIIsolation.setStatus(_A)
class _WirelessTIEnable80211d_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('on',1)))
_WirelessTIEnable80211d_Type.__name__=_C
_WirelessTIEnable80211d_Object=MibScalar
wirelessTIEnable80211d=_WirelessTIEnable80211d_Object((1,3,6,1,4,1,4526,4,1,6,29),_WirelessTIEnable80211d_Type())
wirelessTIEnable80211d.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessTIEnable80211d.setStatus(_A)
class _WirelessAPSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('OPEN-DISABLE-MODE',0),('OPEN-64WEP-MODE',1),('OPEN-128WEP-MODE',2),('SHARED-64WEP-MODE',3),('SHARED-128WEP-MODE',4)))
_WirelessAPSecurityMode_Type.__name__=_C
_WirelessAPSecurityMode_Object=MibScalar
wirelessAPSecurityMode=_WirelessAPSecurityMode_Object((1,3,6,1,4,1,4526,4,1,6,37),_WirelessAPSecurityMode_Type())
wirelessAPSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wirelessAPSecurityMode.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'netgear':netgear,'wirelessProducts':wirelessProducts,'wirelessAccessPointDev':wirelessAccessPointDev,'wirelessAPSystemGroup':wirelessAPSystemGroup,'wirelessAPMacAddr':wirelessAPMacAddr,'wirelessAPFWVer':wirelessAPFWVer,'wirelessAPDateTime':wirelessAPDateTime,'wirelessAPUpTime':wirelessAPUpTime,'wirelessAPResetNow':wirelessAPResetNow,'wirelessAPResetToFactoryDefault':wirelessAPResetToFactoryDefault,'wirelessAPPassword':wirelessAPPassword,'wirelessAPClearLog':wirelessAPClearLog,'wirelessAPSaveConfiguration':wirelessAPSaveConfiguration,'snmpTrapVersion':snmpTrapVersion,'snmpTrapRcvIpType':snmpTrapRcvIpType,'snmpAPTrapRcvIpAddress':snmpAPTrapRcvIpAddress,'snmpAPSNMPEnable':snmpAPSNMPEnable,'snmpAPCommunity':snmpAPCommunity,'snmpAPAccessRight':snmpAPAccessRight,'snmpAPManagersType':snmpAPManagersType,'snmpAPSpecificStationIp':snmpAPSpecificStationIp,'snmpAPTrapEnable':snmpAPTrapEnable,'wirelessAPConnectedStationGroup':wirelessAPConnectedStationGroup,'wirelessAPConnectedStationTableRefresh':wirelessAPConnectedStationTableRefresh,'wirelessAPConnectedStation':wirelessAPConnectedStation,'wirelessAPConnectedStationTable':wirelessAPConnectedStationTable,'wirelessAPConnectedStationEntry':wirelessAPConnectedStationEntry,_N:wirelessAPConnectedStationMacAddr,'wirelessAPConnectedStationStatus':wirelessAPConnectedStationStatus,'wirelessAPControl':wirelessAPControl,'wirelessAPControlList':wirelessAPControlList,'wirelessAPControlListTable':wirelessAPControlListTable,'wirelessAPControlListEntry':wirelessAPControlListEntry,_O:wirelessAPControlListMacAddr,'wirelessAPCtlOperate':wirelessAPCtlOperate,'wirelessAPAddCtlMacAddr':wirelessAPAddCtlMacAddr,'wirelessAPDelCtlMacAddr':wirelessAPDelCtlMacAddr,'wirelessAPIfTrafficGroup':wirelessAPIfTrafficGroup,'wirelessAPIfWiredTrafficGroup':wirelessAPIfWiredTrafficGroup,'wirelessAPIfWiredTotalOctetsIn':wirelessAPIfWiredTotalOctetsIn,'wirelessAPIfWiredTotalOctetsOut':wirelessAPIfWiredTotalOctetsOut,'wirelessAPIfWiredPacketsIn':wirelessAPIfWiredPacketsIn,'wirelessAPIfWiredPacketsOut':wirelessAPIfWiredPacketsOut,'wirelessAPIfWiredThroughputIn':wirelessAPIfWiredThroughputIn,'wirelessAPIfWiredThroughputOut':wirelessAPIfWiredThroughputOut,'wirelessAPIfWiredErrorsIn':wirelessAPIfWiredErrorsIn,'wirelessAPIfWiredErrorsOut':wirelessAPIfWiredErrorsOut,'wirelessAPIfWiredTrafficResetCounter':wirelessAPIfWiredTrafficResetCounter,'wirelessAPIfWlanTrafficGroup':wirelessAPIfWlanTrafficGroup,'wirelessAPIfWLANTotalOctetsIn':wirelessAPIfWLANTotalOctetsIn,'wirelessAPIfWLANTotalOctetsOut':wirelessAPIfWLANTotalOctetsOut,'wirelessAPIfWLANUnicastPacketsIn':wirelessAPIfWLANUnicastPacketsIn,'wirelessAPIfWLANUnicastPacketsOut':wirelessAPIfWLANUnicastPacketsOut,'wirelessAPIfWLANBroadcastPacketsIn':wirelessAPIfWLANBroadcastPacketsIn,'wirelessAPIfWLANBroadcastPacketsOut':wirelessAPIfWLANBroadcastPacketsOut,'wirelessAPIfWLANMulticastPacketsIn':wirelessAPIfWLANMulticastPacketsIn,'wirelessAPIfWLANMulticastPacketsOut':wirelessAPIfWLANMulticastPacketsOut,'wirelessAPIfWLANThroughputIn':wirelessAPIfWLANThroughputIn,'wirelessAPIfWLANThroughputOut':wirelessAPIfWLANThroughputOut,'wirelessAPIfWLANPacketsIn':wirelessAPIfWLANPacketsIn,'wirelessAPIfWLANPacketsOut':wirelessAPIfWLANPacketsOut,'wirelessAPIfWLANTrafficResetCounter':wirelessAPIfWLANTrafficResetCounter,'wirelessAPIfSettingsGroup':wirelessAPIfSettingsGroup,'wirelessAPDHCPClientObtainIPchoice':wirelessAPDHCPClientObtainIPchoice,'wirelessAPDHCPClientIPaddr':wirelessAPDHCPClientIPaddr,'wirelessAPDHCPClientIPsubnetMask':wirelessAPDHCPClientIPsubnetMask,'wirelessAPDHCPClientGateway':wirelessAPDHCPClientGateway,'wirelessAPDHCPClientPriDNS':wirelessAPDHCPClientPriDNS,'wirelessAPDHCPClientSecDNS':wirelessAPDHCPClientSecDNS,'wirelessAPDHCPClientStaticIPaddr':wirelessAPDHCPClientStaticIPaddr,'wirelessAPDHCPClientStaticIPsubnetMask':wirelessAPDHCPClientStaticIPsubnetMask,'wirelessAPDHCPClientStaticGateway':wirelessAPDHCPClientStaticGateway,'wirelessAPDHCPClientStaticPriDNS':wirelessAPDHCPClientStaticPriDNS,'wirelessAPDHCPClientStaticSecDNS':wirelessAPDHCPClientStaticSecDNS,'wirelessAPName':wirelessAPName,'wirelessAPWINSchoice':wirelessAPWINSchoice,'wirelessAPWINSServerName':wirelessAPWINSServerName,'wirelessAPWirelessSettingsGroup':wirelessAPWirelessSettingsGroup,'wirelessAPCountryDomain':wirelessAPCountryDomain,'wirelessAPChannelNo':wirelessAPChannelNo,'wirelessAPSSID':wirelessAPSSID,'wirelessAPPassphrase':wirelessAPPassphrase,'wirelessAPGenerateKeysEnabled':wirelessAPGenerateKeysEnabled,'wirelessAPKeysSet':wirelessAPKeysSet,'wirelessAPKeysSetTable':wirelessAPKeysSetTable,'wirelessAPKeysSetEntry':wirelessAPKeysSetEntry,_P:wirelessAPKeysSetEnabled,'wirelessAPKeys':wirelessAPKeys,'wirelessAPBasicRateChoice':wirelessAPBasicRateChoice,'wirelessAPFixedRate':wirelessAPFixedRate,'wirelessAPFixedRate1':wirelessAPFixedRate1,'wirelessAPFixedRate2':wirelessAPFixedRate2,'wirelessAPFixedRate5-5':wirelessAPFixedRate5_5,'wirelessAPFixedRate11':wirelessAPFixedRate11,'wirelessAPRTSThreshold':wirelessAPRTSThreshold,'wirelessAPFragmentationThreshold':wirelessAPFragmentationThreshold,'wirelessAPBeaconPeriod':wirelessAPBeaconPeriod,'wirelessAPShortPreambleOptionImplemented':wirelessAPShortPreambleOptionImplemented,'wirelessAPAntennaSelection':wirelessAPAntennaSelection,'wirelessAPMaximumTransmitPowerLevel':wirelessAPMaximumTransmitPowerLevel,'wirelessAPOperatingMode':wirelessAPOperatingMode,'wirelessAPSSIDEnabled':wirelessAPSSIDEnabled,'wirelessAPSecuritySettingsGroup':wirelessAPSecuritySettingsGroup,'wirelessAP802dot1xSecurityEnabled':wirelessAP802dot1xSecurityEnabled,'wirelessAPEAPauthType':wirelessAPEAPauthType,'wirelessAPRadiusServer':wirelessAPRadiusServer,'wirelessAPRadiusPort':wirelessAPRadiusPort,'wirelessAPSharedKey':wirelessAPSharedKey,'wirelessAPRadiusServer2':wirelessAPRadiusServer2,'wirelessAPRadAccountPort':wirelessAPRadAccountPort,'wirelessAPKeyExchange':wirelessAPKeyExchange,'wirelessAPKeyExchangeKeylife':wirelessAPKeyExchangeKeylife,'wirelessAPRadAccountEnable':wirelessAPRadAccountEnable,'wirelessAPMacAuthEnable':wirelessAPMacAuthEnable,'wirelessAPRadAccountUpdateEnable':wirelessAPRadAccountUpdateEnable,'wirelessAPRadAccountUpdatePeriod':wirelessAPRadAccountUpdatePeriod,'wirelessAPRadAccountIdlePeriod':wirelessAPRadAccountIdlePeriod,'wirelessTIOperateMode':wirelessTIOperateMode,'wirelessTIDstMac':wirelessTIDstMac,'wirelessTIIsolation':wirelessTIIsolation,'wirelessTIEnable80211d':wirelessTIEnable80211d,'wirelessAPSecurityMode':wirelessAPSecurityMode})